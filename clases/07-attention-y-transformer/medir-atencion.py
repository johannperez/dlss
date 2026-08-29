#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
medir-atencion.py — clase 7
===========================

Entrena un transformer chiquito **de verdad** sobre los discursos de apertura
de sesiones (1984-2019, corpus real) y **exporta los mapas de atención que
salieron**, sin retocarlos, a `datos-atencion.js`.

Por qué existe este archivo: la especificación de la clase pide que los pesos
de las visualizaciones vengan de un modelo real y no de números inventados.
Un patrón imperfecto real enseña más que uno perfecto inventado, y además
permite decir en el aula "esta cabeza hace algo que no entendemos", que es la
verdad del campo.

El modelo es **el mismo bloque que se construye en el notebook de la clase**:
pre-norm, attention multi-cabeza con máscara causal, MLP de dos capas con
ReLU, dos conexiones residuales. Si cambiás uno, cambiá el otro.

Uso:
    PYTHONPATH=_shared python3 clases/07-attention-y-transformer/medir-atencion.py
    ... --pasos 300            (corrida corta, para probar que anda)
    ... --listar-candidatas    (todas las oraciones elegibles del corpus)

Los valores por defecto (2000 pasos, lr 3e-3, semilla 1983) son EXACTAMENTE los que
produjeron el `datos-atencion.js` que está en el repo. Si los cambiás, cambian los
mapas de las cuatro visualizaciones y los números del notebook. Corrélo y te da los
mismos números hasta el cuarto decimal: se verificó dos veces, en CPU, y lo único que
cambia entre corridas es el campo `segundos` del `meta`. Tarda **entre 50 y 60 s** con
la CPU libre (751 s la primera vez, con la máquina cargada por otros procesos).

Se probó también una corrida más larga y más suave (--pasos 6000 con lr 1.2e-3): baja
la loss de validación de 4,60 a 4,23 **y arruina la clase**. Las cabezas quedan
difusas, «lo» se mira sobre todo a sí misma y la enumeración se va a los artículos: se
pierden los dos momentos aha de las visualizaciones. Está anotado acá para que nadie
lo vuelva a intentar creyendo que mejora.

Salidas:
    clases/07-attention-y-transformer/datos-atencion.js    (lo que leen las viz)
    clases/07-attention-y-transformer/datos-atencion.json  (lo mismo, para el notebook)
"""

import argparse
import collections
import json
import math
import os
import pathlib
import re
import sys
import time

import torch
import torch.nn as nn
import torch.nn.functional as F

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "_shared"))
os.environ.setdefault("DLSS_RAIZ", str(RAIZ))

from ssdl import datos, utils  # noqa: E402

SALIDA = pathlib.Path(__file__).resolve().parent
SEMILLA = 1983

# --- configuración del modelo (chiquito a propósito: tiene que correr en CPU) --
CTX = 24          # cuántas fichas mira hacia atrás
DIM = 96          # tamaño del vector de cada ficha
CABEZAS = 4       # cuántos "libros de códigos" en paralelo
CAPAS = 2         # cuántos bloques apilados
VOCAB = 3000      # las 3000 palabras más frecuentes; el resto -> <desc>
LOTE = 16


# =============================================================================
# 1. Texto -> fichas
# =============================================================================

PATRON = re.compile(r"[a-záéíóúüñ]+|[.,;:()¿?¡!«»—\"-]")


def partir(texto):
    return PATRON.findall(texto.lower())


def cargar_corpus():
    crudo = datos.corpus_mini_gpt()
    cuerpo = "\n".join(l for l in crudo.split("\n") if not l.startswith("#"))
    return cuerpo


class Vocabulario:
    def __init__(self, fichas, tope):
        cuenta = collections.Counter(fichas)
        self.a_ficha = ["<desc>"] + [p for p, _ in cuenta.most_common(tope - 1)]
        self.a_id = {p: i for i, p in enumerate(self.a_ficha)}
        self.cuenta = cuenta

    def __len__(self):
        return len(self.a_ficha)

    def codificar(self, fichas):
        return [self.a_id.get(f, 0) for f in fichas]

    def tiene(self, f):
        return f in self.a_id


# =============================================================================
# 2. El modelo — el mismo bloque que arma el notebook
# =============================================================================

class AtencionMulticabeza(nn.Module):
    """Cada palabra le pregunta a las anteriores qué tan relevantes son."""

    def __init__(self, dim, cabezas, ctx):
        super().__init__()
        self.cabezas = cabezas
        self.d_cabeza = dim // cabezas
        self.proy_q = nn.Linear(dim, dim, bias=False)   # "lo que busco"
        self.proy_k = nn.Linear(dim, dim, bias=False)   # "lo que ofrezco"
        self.proy_v = nn.Linear(dim, dim, bias=False)   # "lo que aporto"
        self.proy_salida = nn.Linear(dim, dim, bias=False)
        self.register_buffer("mascara", torch.tril(torch.ones(ctx, ctx)))

    def forward(self, x, devolver_pesos=False):
        B, T, D = x.shape
        H, dc = self.cabezas, self.d_cabeza
        q = self.proy_q(x).view(B, T, H, dc).transpose(1, 2)   # (B,H,T,dc)
        k = self.proy_k(x).view(B, T, H, dc).transpose(1, 2)
        v = self.proy_v(x).view(B, T, H, dc).transpose(1, 2)

        crudos = (q @ k.transpose(-2, -1)) / math.sqrt(dc)     # (B,H,T,T)
        puntajes = crudos.masked_fill(self.mascara[:T, :T] == 0, float("-inf"))
        pesos = F.softmax(puntajes, dim=-1)                    # filas suman 1

        salida = pesos @ v                                     # (B,H,T,dc)
        salida = salida.transpose(1, 2).contiguous().view(B, T, D)
        salida = self.proy_salida(salida)
        if not devolver_pesos:
            return salida, None
        # Los MISMOS puntajes, pero sin tapar el futuro. El modelo nunca los usó
        # (se entrenó siempre con máscara): sirven para ver, en la viz, qué es
        # exactamente lo que la máscara tapa.
        sin_mascara = F.softmax(crudos, dim=-1)
        return salida, {"con": pesos, "sin": sin_mascara}


class BloqueTransformer(nn.Module):
    """attention + MLP, cada uno con su normalización y su conexión residual."""

    def __init__(self, dim, cabezas, ctx):
        super().__init__()
        self.norma1 = nn.LayerNorm(dim)
        self.atencion = AtencionMulticabeza(dim, cabezas, ctx)
        self.norma2 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, 4 * dim), nn.ReLU(), nn.Linear(4 * dim, dim))

    def forward(self, x, devolver_pesos=False):
        a, pesos = self.atencion(self.norma1(x), devolver_pesos)
        x = x + a                       # conexión residual 1
        x = x + self.mlp(self.norma2(x))  # conexión residual 2
        return x, pesos


class ModeloLenguaje(nn.Module):
    def __init__(self, vocab, dim=DIM, cabezas=CABEZAS, capas=CAPAS, ctx=CTX):
        super().__init__()
        self.ctx = ctx
        self.emb_ficha = nn.Embedding(vocab, dim)
        self.emb_posicion = nn.Embedding(ctx, dim)
        self.bloques = nn.ModuleList(
            [BloqueTransformer(dim, cabezas, ctx) for _ in range(capas)])
        self.norma_final = nn.LayerNorm(dim)
        self.cabeza = nn.Linear(dim, vocab, bias=False)
        self.cabeza.weight = self.emb_ficha.weight   # pesos atados
        self.apply(self._iniciar)

    @staticmethod
    def _iniciar(modulo):
        """Pesos chiquitos al arrancar: si arrancan grandes, el softmax se satura."""
        if isinstance(modulo, nn.Linear):
            nn.init.normal_(modulo.weight, mean=0.0, std=0.02)
            if modulo.bias is not None:
                nn.init.zeros_(modulo.bias)
        elif isinstance(modulo, nn.Embedding):
            nn.init.normal_(modulo.weight, mean=0.0, std=0.02)

    def forward(self, idx, objetivos=None, devolver_pesos=False):
        B, T = idx.shape
        pos = torch.arange(T, device=idx.device)
        x = self.emb_ficha(idx) + self.emb_posicion(pos)
        mapas = []
        for bloque in self.bloques:
            x, pesos = bloque(x, devolver_pesos)
            if devolver_pesos:
                mapas.append(pesos)
        logits = self.cabeza(self.norma_final(x))
        perdida = None
        if objetivos is not None:
            perdida = F.cross_entropy(
                logits.view(-1, logits.size(-1)), objetivos.reshape(-1))
        return logits, perdida, mapas


# =============================================================================
# 3. Entrenar
# =============================================================================

def lote(ids, tam, ctx, gen):
    i = torch.randint(len(ids) - ctx - 1, (tam,), generator=gen)
    x = torch.stack([ids[j:j + ctx] for j in i])
    y = torch.stack([ids[j + 1:j + ctx + 1] for j in i])
    return x, y


def entrenar(modelo, ids_train, ids_val, pasos, lr=3e-3):
    gen = torch.Generator().manual_seed(SEMILLA)
    opt = torch.optim.AdamW(modelo.parameters(), lr=lr, weight_decay=0.01)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=pasos)
    historial = []
    t0 = time.time()
    for paso in range(1, pasos + 1):
        x, y = lote(ids_train, LOTE, CTX, gen)
        _, perdida, _ = modelo(x, y)
        opt.zero_grad(set_to_none=True)
        perdida.backward()
        torch.nn.utils.clip_grad_norm_(modelo.parameters(), 1.0)
        opt.step()
        sched.step()
        if paso % 50 == 0 or paso == 1:
            modelo.eval()
            with torch.no_grad():
                xv, yv = lote(ids_val, 64, CTX, torch.Generator().manual_seed(7))
                _, pv, _ = modelo(xv, yv)
            modelo.train()
            historial.append({"paso": paso, "train": round(float(perdida.detach()), 4),
                              "val": round(float(pv), 4)})
            print(f"  paso {paso:5d}  train {float(perdida.detach()):.3f}  "
                  f"val {float(pv):.3f}  ({time.time()-t0:.0f} s)", flush=True)
    return historial, time.time() - t0


# =============================================================================
# 4. Elegir oraciones reales del corpus
# =============================================================================

# Cada oración busca un fenómeno lingüístico distinto. Se eligen del corpus
# real: no se inventa ni una palabra. `buscar_oraciones` imprime candidatas
# para que quien mantenga esto pueda cambiarlas con criterio.
# Cada oración busca un fenómeno lingüístico distinto y **todas salen del corpus
# real**: no se inventó ni una palabra. Se eligieron a mano de la lista que
# imprime `--listar-candidatas`, y el script verifica que sigan estando ahí.
# Si alguna dejara de aparecer, el script avisa en vez de inventarla.
ORACIONES_ELEGIDAS = [
    ("anafora",
     "una anáfora: cuando leés «lo» tenés que ir a buscar a qué se refiere",
     "si tenemos que corregir algo , lo vamos a corregir"),
    ("negacion",
     "una negación, que le da vuelta el sentido a toda la oración",
     "la deuda no es un problema que haya creado este gobierno"),
    ("subordinada",
     "una subordinada larga metida entre el sujeto y el verbo",
     "queremos una economía popular de mercado que esté al servicio del hombre"),
    ("enumeracion",
     "una enumeración de cuatro temas separados por comas",
     "la educación , la salud , la seguridad y la justicia"),
    ("comparacion",
     "una comparación con superlativo («más formidable»)",
     "creemos que ésta es la revolución más formidable para nuestro tiempo"),
]


def oraciones_del_corpus(cuerpo, vocabulario, minimo=9, maximo=14):
    """Oraciones reales, cortas, con todas sus palabras dentro del vocabulario."""
    crudas = re.split(r"(?<=[.;:])\s+", cuerpo.replace("\n", " "))
    salida = []
    for oracion in crudas:
        fichas = partir(oracion)
        if not (minimo <= len(fichas) <= maximo):
            continue
        if any(not vocabulario.tiene(f) for f in fichas):
            continue
        if fichas[-1] in ".;:":
            fichas = fichas[:-1]
        if len(fichas) < minimo:
            continue
        salida.append(fichas)
    return salida


def buscar_oraciones(candidatas, listar=False):
    """Verifica que cada oración elegida siga estando en el corpus."""
    indice = {" ".join(f): f for f in candidatas}
    if listar:
        for f in candidatas:
            print("   ", " ".join(f))
    elegidas = []
    for clave, fenomeno, texto in ORACIONES_ELEGIDAS:
        fichas = indice.get(texto)
        if fichas is None:
            print(f"   ! OJO: '{clave}' ya no aparece en el corpus. "
                  f"Elegí otra de --listar-candidatas y actualizá ORACIONES_ELEGIDAS.")
            continue
        elegidas.append({"clave": clave, "fenomeno": fenomeno, "fichas": fichas})
    return elegidas


# =============================================================================
# 5. Describir qué hace cada cabeza (medido, no imaginado)
# =============================================================================

def estadisticas_cabeza(mapas_por_oracion):
    """Promedia, sobre todas las oraciones, en qué se fija una cabeza.

    - `anterior`: cuánta atención va a la ficha inmediatamente previa
    - `primera` : cuánta va a la primera ficha de la oración
    - `misma`   : cuánta se queda en sí misma
    - `entropia`: qué tan repartida está (0 = mira a una sola; 1 = mira a todas)
    """
    ant = pri = mis = ent = 0.0
    n = 0
    for A in mapas_por_oracion:
        T = len(A)
        for i in range(T):
            fila = A[i]
            ant += fila[i - 1] if i > 0 else 0.0
            pri += fila[0]
            mis += fila[i]
            h = -sum(p * math.log(p + 1e-12) for p in fila[:i + 1])
            ent += h / math.log(i + 1) if i > 0 else 0.0
            n += 1
    return {"anterior": ant / n, "primera": pri / n,
            "misma": mis / n, "entropia": ent / n}


def describir(est):
    """Un rótulo en castellano derivado de los números, no de la ilusión."""
    if est["anterior"] > 0.35:
        return ("mira a la palabra anterior",
                "casi toda su atención va a la ficha inmediatamente previa: "
                "está leyendo de a pares")
    if est["primera"] > 0.45:
        return ("se ancla en la primera palabra",
                "descarga su atención en la ficha inicial. Es un patrón conocido "
                "(«attention sink»): cuando no tiene nada mejor que mirar, mira ahí")
    if est["misma"] > 0.45:
        return ("se mira a sí misma",
                "se queda casi entera en su propia ficha: aporta poco contexto")
    if est["entropia"] > 0.80:
        return ("reparte parejo (difusa)",
                "reparte su atención entre casi todas las palabras anteriores. "
                "No es interpretable, y así funciona igual")
    return ("mezcla: mira atrás sin un patrón fijo",
            "no se deja resumir en una regla simple. La mayoría de las cabezas "
            "de un modelo real son así")


# =============================================================================
# 6. Programa principal
# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasos", type=int, default=2000)
    ap.add_argument("--listar-candidatas", action="store_true",
                    help="imprime todas las oraciones candidatas y sale")
    args = ap.parse_args()

    utils.fijar_semilla(SEMILLA)
    print("1. Cargando el corpus real (discursos de apertura 1984-2019)...")
    cuerpo = cargar_corpus()
    fichas = partir(cuerpo)
    voc = Vocabulario(fichas, VOCAB)
    ids = torch.tensor(voc.codificar(fichas), dtype=torch.long)
    corte = int(0.9 * len(ids))
    ids_train, ids_val = ids[:corte], ids[corte:]
    cobertura = sum(1 for f in fichas if voc.tiene(f)) / len(fichas)
    print(f"   {len(fichas):,} fichas · vocabulario {len(voc):,} · "
          f"cobertura {cobertura*100:.1f}%")

    if args.listar_candidatas:
        # atajo para quien quiera cambiar las oraciones: lista y sale, sin entrenar
        candidatas = oraciones_del_corpus(cuerpo, voc)
        print(f"   {len(candidatas)} oraciones candidatas (todas del corpus real):")
        for f in candidatas:
            print("   ", " ".join(f))
        return

    print("2. Entrenando el transformer (el mismo bloque del notebook)...")
    modelo = ModeloLenguaje(len(voc))
    n_param = sum(p.numel() for p in modelo.parameters())
    print(f"   {n_param:,} parámetros · {CAPAS} bloques · {CABEZAS} cabezas · "
          f"contexto {CTX}")
    historial, segundos = entrenar(modelo, ids_train, ids_val, args.pasos)
    modelo.eval()

    print("3. Eligiendo oraciones reales del corpus...")
    candidatas = oraciones_del_corpus(cuerpo, voc)
    print(f"   {len(candidatas)} oraciones candidatas")
    oraciones = buscar_oraciones(candidatas, listar=args.listar_candidatas)
    for o in oraciones:
        print(f"   [{o['clave']}] {' '.join(o['fichas'])}")

    print("4. Sacando los mapas de atención que salieron...")
    salida_oraciones = []
    mapas_por_cabeza = [[[] for _ in range(CABEZAS)] for _ in range(CAPAS)]
    for o in oraciones:
        x = torch.tensor([voc.codificar(o["fichas"])], dtype=torch.long)
        with torch.no_grad():
            _, _, mapas = modelo(x, devolver_pesos=True)
        capas, capas_sin = [], []
        for c, m in enumerate(mapas):
            cabezas, cabezas_sin = [], []
            for h in range(CABEZAS):
                A = [[round(v, 4) for v in fila] for fila in m["con"][0, h].tolist()]
                B = [[round(v, 4) for v in fila] for fila in m["sin"][0, h].tolist()]
                cabezas.append(A)
                cabezas_sin.append(B)
                mapas_por_cabeza[c][h].append(A)
            capas.append(cabezas)
            capas_sin.append(cabezas_sin)
        salida_oraciones.append({
            "clave": o["clave"], "fenomeno": o["fenomeno"],
            "fichas": o["fichas"], "atencion": capas,
            "atencion_sin_mascara": capas_sin})

    print("5. Midiendo qué hace cada cabeza...")
    descripciones = []
    for c in range(CAPAS):
        fila = []
        for h in range(CABEZAS):
            est = estadisticas_cabeza(mapas_por_cabeza[c][h])
            titulo, detalle = describir(est)
            fila.append({"capa": c + 1, "cabeza": h + 1, "titulo": titulo,
                         "detalle": detalle,
                         "est": {k: round(v, 3) for k, v in est.items()}})
            print(f"   bloque {c+1} cabeza {h+1}: {titulo}   "
                  f"(anterior {est['anterior']:.2f} · primera {est['primera']:.2f} "
                  f"· misma {est['misma']:.2f} · entropía {est['entropia']:.2f})")
        descripciones.append(fila)

    # una muestra generada, para que se vea que el modelo aprendió algo
    print("6. Una muestra generada por el modelo...")
    gen = torch.Generator().manual_seed(SEMILLA)
    ctxt = torch.tensor([voc.codificar(partir("el gobierno nacional"))],
                        dtype=torch.long)
    for _ in range(28):
        with torch.no_grad():
            logits, _, _ = modelo(ctxt[:, -CTX:])
        prob = F.softmax(logits[0, -1] / 0.85, dim=-1)
        sig = torch.multinomial(prob, 1, generator=gen)
        ctxt = torch.cat([ctxt, sig.view(1, 1)], dim=1)
    muestra = " ".join(voc.a_ficha[i] for i in ctxt[0].tolist())
    print(f"   «{muestra}»")

    paquete = {
        "meta": {
            "corpus": "discursos de apertura de sesiones, Argentina 1984-2019",
            "fuente": "datos/muestras/discursos-apertura/corpus-mini-gpt.txt",
            "real": True,
            "fichas": len(fichas),
            "vocabulario": len(voc),
            "cobertura": round(cobertura, 4),
            "parametros": n_param,
            "capas": CAPAS, "cabezas": CABEZAS, "dim": DIM, "contexto": CTX,
            "pasos": args.pasos,
            "segundos": round(segundos, 1),
            "loss_inicial": historial[0]["val"],
            "loss_final": historial[-1]["val"],
            "semilla": SEMILLA,
            "muestra_generada": muestra,
            "generado_por": "clases/07-attention-y-transformer/medir-atencion.py",
        },
        "historial": historial,
        "oraciones": salida_oraciones,
        "cabezas": descripciones,
    }

    (SALIDA / "datos-atencion.json").write_text(
        json.dumps(paquete, ensure_ascii=False), encoding="utf-8")
    js = ("/* GENERADO por medir-atencion.py — no lo edites a mano.\n"
          "   Mapas de atención de un transformer entrenado de verdad sobre los\n"
          "   discursos de apertura de sesiones (1984-2019). Sin retoques. */\n"
          "const DATOS_ATENCION = " + json.dumps(paquete, ensure_ascii=False) + ";\n")
    (SALIDA / "datos-atencion.js").write_text(js, encoding="utf-8")
    kb = (SALIDA / "datos-atencion.js").stat().st_size / 1024
    print(f"\nListo. datos-atencion.js ({kb:.0f} KB) y datos-atencion.json escritos.")


if __name__ == "__main__":
    main()
