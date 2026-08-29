#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
entrenar-mini-gpt.py — clase 8
==============================

Entrena **de verdad** el mini-GPT de la clase (1.541.056 perillas, nivel
caracter) sobre el corpus sintetico Aguasclaras y exporta todo lo que comen las
cuatro visualizaciones a `datos-mini-gpt.js` (para el navegador) y
`datos-mini-gpt.json` (para el notebook).

Por que existe este archivo: la guia de construccion prohibe numeros inventados
en una viz. Todo lo que muestran `temperatura.html`, `ventana-de-contexto.html`,
`por-que-alucina.html` y `contar-letras.html` sale de esta corrida.

**El modelo es letra por letra el del notebook.** Misma clase, misma config,
misma semilla. Si tocas uno, tocas el otro: si no, el aula ve dos modelos
distintos y se rompe la coherencia del material.

Uso:
    PYTHONPATH=_shared python3 clases/08-mini-gpt-y-los-llm/entrenar-mini-gpt.py
    ... --pasos 100        (corrida corta, solo para probar que anda)

Salidas (en esta misma carpeta):
    datos-mini-gpt.js     lo que leen las cuatro viz
    datos-mini-gpt.json   lo mismo, para el notebook
"""

import argparse
import json
import os
import pathlib
import platform
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

# --- la configuracion del curso. NO la cambies sin cambiar el notebook. -------
CTX = 128        # cuantos caracteres mira hacia atras
DIM = 176        # cuantos numeros lleva cada caracter
CABEZAS = 4      # cuantas cabezas de atencion por bloque
CAPAS = 4        # cuantos bloques transformer apilados
LOTE = 32        # cuantas ventanas por paso
PASOS = 1200     # cuantos pasos de descenso
LR = 1e-3


# =============================================================================
# 1. El tokenizador mas simple del mundo: un caracter, una ficha
# =============================================================================

class TokenizadorCaracteres:
    def __init__(self, texto):
        self.fichas = sorted(set(texto))
        self.a_id = {c: i for i, c in enumerate(self.fichas)}
        self.a_ficha = {i: c for i, c in enumerate(self.fichas)}

    def __len__(self):
        return len(self.fichas)

    def codificar(self, s):
        return [self.a_id[c] for c in s if c in self.a_id]

    def decodificar(self, ids):
        return "".join(self.a_ficha[int(i)] for i in ids)


# =============================================================================
# 2. El modelo — el bloque de la clase 7, apilado
# =============================================================================

class AtencionMulticabeza(nn.Module):
    """Cada ficha le pregunta a las anteriores que tan relevantes son para ella."""

    def __init__(self, dim, cabezas, ctx):
        super().__init__()
        self.cabezas = cabezas
        self.d_cabeza = dim // cabezas
        self.proy_q = nn.Linear(dim, dim, bias=False)
        self.proy_k = nn.Linear(dim, dim, bias=False)
        self.proy_v = nn.Linear(dim, dim, bias=False)
        self.proy_salida = nn.Linear(dim, dim, bias=False)
        self.register_buffer("mascara", torch.tril(torch.ones(ctx, ctx)))

    def forward(self, x):
        B, T, D = x.shape
        H, dc = self.cabezas, self.d_cabeza
        q = self.proy_q(x).view(B, T, H, dc).transpose(1, 2)
        k = self.proy_k(x).view(B, T, H, dc).transpose(1, 2)
        v = self.proy_v(x).view(B, T, H, dc).transpose(1, 2)
        puntajes = (q @ k.transpose(-2, -1)) / dc ** 0.5
        puntajes = puntajes.masked_fill(self.mascara[:T, :T] == 0, float("-inf"))
        pesos = torch.softmax(puntajes, dim=-1)
        salida = (pesos @ v).transpose(1, 2).contiguous().view(B, T, D)
        return self.proy_salida(salida)


class BloqueTransformer(nn.Module):
    """attention + MLP, cada uno con su normalizacion y su conexion residual."""

    def __init__(self, dim, cabezas, ctx):
        super().__init__()
        self.norma1 = nn.LayerNorm(dim)
        self.atencion = AtencionMulticabeza(dim, cabezas, ctx)
        self.norma2 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, 4 * dim), nn.ReLU(), nn.Linear(4 * dim, dim))

    def forward(self, x):
        x = x + self.atencion(self.norma1(x))
        return x + self.mlp(self.norma2(x))


class MiniGPT(nn.Module):
    def __init__(self, vocab, dim=DIM, cabezas=CABEZAS, capas=CAPAS, ctx=CTX):
        super().__init__()
        self.ctx = ctx
        self.emb_ficha = nn.Embedding(vocab, dim)
        self.emb_posicion = nn.Embedding(ctx, dim)
        self.bloques = nn.ModuleList(
            [BloqueTransformer(dim, cabezas, ctx) for _ in range(capas)])
        self.norma_final = nn.LayerNorm(dim)
        self.cabeza = nn.Linear(dim, vocab, bias=False)
        self.apply(self._iniciar)

    @staticmethod
    def _iniciar(modulo):
        if isinstance(modulo, nn.Linear):
            nn.init.normal_(modulo.weight, mean=0.0, std=0.02)
            if modulo.bias is not None:
                nn.init.zeros_(modulo.bias)
        elif isinstance(modulo, nn.Embedding):
            nn.init.normal_(modulo.weight, mean=0.0, std=0.02)

    def forward(self, idx, objetivos=None):
        T = idx.shape[1]
        pos = torch.arange(T, device=idx.device)
        x = self.emb_ficha(idx) + self.emb_posicion(pos)
        for bloque in self.bloques:
            x = bloque(x)
        logits = self.cabeza(self.norma_final(x))
        if objetivos is None:
            return logits, None
        perdida = F.cross_entropy(
            logits.reshape(-1, logits.shape[-1]), objetivos.reshape(-1))
        return logits, perdida

    @torch.no_grad()
    def generar(self, idx, n, temperatura=1.0, gen=None):
        """Genera n fichas. temperatura 0 = siempre la mas probable (sin sorteo)."""
        for _ in range(n):
            recorte = idx[:, -self.ctx:]
            logits, _ = self(recorte)
            logits = logits[:, -1, :]
            if temperatura <= 0:
                siguiente = logits.argmax(dim=-1, keepdim=True)
            else:
                probs = torch.softmax(logits / temperatura, dim=-1)
                siguiente = torch.multinomial(probs, num_samples=1, generator=gen)
            idx = torch.cat([idx, siguiente], dim=1)
        return idx


# =============================================================================
# 3. Datos
# =============================================================================

def lote_de(ids, tam, ctx, gen):
    i = torch.randint(len(ids) - ctx - 1, (tam,), generator=gen)
    x = torch.stack([ids[j:j + ctx] for j in i])
    y = torch.stack([ids[j + 1:j + ctx + 1] for j in i])
    return x, y


@torch.no_grad()
def perdida_media(modelo, ids, tam, ctx, gen, veces=20):
    modelo.eval()
    total = 0.0
    for _ in range(veces):
        x, y = lote_de(ids, tam, ctx, gen)
        _, p = modelo(x, y)
        total += float(p)
    modelo.train()
    return total / veces


# =============================================================================
# 4. Ayudas para los paquetes de datos de las viz
# =============================================================================

@torch.no_grad()
def distribucion(modelo, tok, prompt, tope=None):   # noqa: D401
    """La distribucion de la PROXIMA ficha despues de `prompt`, sin temperatura."""
    idx = torch.tensor([tok.codificar(prompt)[-CTX:]])
    logits, _ = modelo(idx)
    v = logits[0, -1, :]
    probs = torch.softmax(v, dim=-1)
    orden = torch.argsort(probs, descending=True)
    if tope:
        orden = orden[:tope]
    return [{"ficha": tok.a_ficha[int(i)], "logit": round(float(v[i]), 4),
             "prob": round(float(probs[i]), 6)} for i in orden]


@torch.no_grad()
def generar_texto(modelo, tok, prompt, n, temperatura, semilla):
    gen = torch.Generator().manual_seed(semilla)
    idx = torch.tensor([tok.codificar(prompt)[-CTX:]])
    salida = modelo.generar(idx, n, temperatura, gen)
    return tok.decodificar(salida[0].tolist()[len(tok.codificar(prompt)[-CTX:]):])


@torch.no_grad()
def generar_lote(modelo, tok, prompts, temps, semillas, n):
    """Genera todo de una: (prompt x temperatura x sorteo) en un solo lote.

    Un solo generador con semilla fija para toda la tanda: las cinco "tiradas"
    de cada combinacion son cinco sorteos independientes, que es exactamente lo
    que muestra el boton "generar 5 veces con el mismo prompt".
    """
    combos = [(ip, it, isem) for ip in range(len(prompts))
              for it in range(len(temps)) for isem in range(len(semillas))]
    filas = [tok.codificar(prompts[ip])[-CTX:] for ip, _, _ in combos]
    largo = max(len(f) for f in filas)
    relleno = tok.a_id[" "]
    salida = torch.tensor([[relleno] * (largo - len(f)) + f for f in filas])
    temps_t = torch.tensor([temps[it] for _, it, _ in combos], dtype=torch.float32)
    frios = (temps_t <= 0).unsqueeze(1)
    temps_c = temps_t.clamp(min=1e-6).unsqueeze(1)
    g = torch.Generator().manual_seed(SEMILLA)
    for _ in range(n):
        logits, _ = modelo(salida[:, -CTX:])
        v = logits[:, -1, :]
        sorteadas = torch.multinomial(torch.softmax(v / temps_c, dim=-1), 1,
                                      generator=g)
        elegidas = torch.where(frios, v.argmax(dim=-1, keepdim=True), sorteadas)
        salida = torch.cat([salida, elegidas], dim=1)
    textos = {}
    for fila, (ip, it, isem) in enumerate(combos):
        cont = tok.decodificar(salida[fila, largo:].tolist())
        textos.setdefault(str(ip), {}).setdefault(f"{temps[it]:.1f}", []).append(cont)
    return textos


@torch.no_grad()
def completar_lote(modelo, tok, prompts, n):
    """Completa muchos prompts a la vez, siempre con la ficha mas probable."""
    filas = [tok.codificar(p)[-CTX:] for p in prompts]
    largo = max(len(f) for f in filas)
    relleno = tok.a_id[" "]
    salida = torch.tensor([[relleno] * (largo - len(f)) + f for f in filas])
    for _ in range(n):
        logits, _ = modelo(salida[:, -CTX:])
        salida = torch.cat([salida, logits[:, -1, :].argmax(dim=-1, keepdim=True)],
                           dim=1)
    return [tok.decodificar(salida[i, largo:].tolist()) for i in range(len(prompts))]


@torch.no_grad()
def prob_de_la_continuacion(modelo, tok, contexto, objetivo):
    """Probabilidad que el modelo le da a `objetivo`, ficha por ficha."""
    p, ctx = 1.0, contexto
    detalle = []
    for ch in objetivo:
        ii = torch.tensor([tok.codificar(ctx)[-CTX:]])
        logits, _ = modelo(ii)
        probs = torch.softmax(logits[0, -1, :], dim=-1)
        pi = float(probs[tok.a_id[ch]])
        detalle.append({"ficha": ch, "prob": round(pi, 6)})
        p *= pi
        ctx += ch
    return p, detalle


# =============================================================================
# 5. Main
# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasos", type=int, default=PASOS)
    ap.add_argument("--solo-exportar", action="store_true",
                    help="no entrena: levanta el checkpoint guardado y rehace "
                         "los paquetes de las viz")
    args = ap.parse_args()
    CHECK = SALIDA / "mini-gpt.pt"     # gitignoreado (*.pt): es un artefacto local

    utils.fijar_semilla(SEMILLA)
    gen = torch.Generator().manual_seed(SEMILLA)

    print("=" * 74)
    print("mini-GPT de la clase 8 — corpus SINTETICO Aguasclaras")
    print("=" * 74)

    texto = datos.debates_aguasclaras()
    verdad = datos.verdad_aguasclaras()
    tok = TokenizadorCaracteres(texto)
    ids = torch.tensor(tok.codificar(texto), dtype=torch.long)
    corte = int(0.9 * len(ids))
    ids_tr, ids_va = ids[:corte], ids[corte:]
    print(f"corpus: {len(texto):,} caracteres · vocabulario de {len(tok)} fichas")
    print(f"train: {len(ids_tr):,} · val: {len(ids_va):,}")

    modelo = MiniGPT(len(tok))
    n_par = utils.contar_parametros(modelo)
    print(f"modelo: {n_par:,} perillas "
          f"({CAPAS} bloques · {CABEZAS} cabezas · dim {DIM} · contexto {CTX})")

    opt = torch.optim.AdamW(modelo.parameters(), lr=LR)

    prompt_teatro = "Señor presidente, "
    muestras, historial = [], []

    def muestra(paso):
        t = generar_texto(modelo, tok, prompt_teatro, 260, 0.8, SEMILLA + paso)
        muestras.append({"paso": paso, "prompt": prompt_teatro, "texto": t})
        print(f"\n--- muestra en el paso {paso} " + "-" * 40)
        print(prompt_teatro + t.replace("\n", " ⏎ "))
        print("-" * 60)

    hitos = {0, 50, 150, 400, 800, args.pasos}

    if args.solo_exportar:
        guardado = torch.load(CHECK, weights_only=False)
        modelo.load_state_dict(guardado["pesos"])
        historial = guardado["historial"]
        muestras = guardado["muestras"]
        segundos = guardado["segundos"]
        print(f"checkpoint levantado: {args.pasos} pasos, {segundos:.0f} s")
        modelo.eval()
        return exportar(modelo, tok, texto, verdad, historial, muestras,
                        segundos, n_par, ids_tr, ids_va, args)

    muestra(0)
    historial.append({"paso": 0,
                      "train": round(perdida_media(modelo, ids_tr, LOTE, CTX, gen, 8), 4),
                      "val": round(perdida_media(modelo, ids_va, LOTE, CTX, gen, 8), 4)})

    t0 = time.time()
    for paso in range(1, args.pasos + 1):
        x, y = lote_de(ids_tr, LOTE, CTX, gen)
        _, perdida = modelo(x, y)
        opt.zero_grad(set_to_none=True)
        perdida.backward()
        opt.step()
        if paso % 50 == 0 or paso == args.pasos:
            tr = perdida_media(modelo, ids_tr, LOTE, CTX, gen, 8)
            va = perdida_media(modelo, ids_va, LOTE, CTX, gen, 8)
            historial.append({"paso": paso, "train": round(tr, 4), "val": round(va, 4)})
            transcurrido = time.time() - t0
            resto = transcurrido / paso * (args.pasos - paso)
            print(f"paso {paso:5d}/{args.pasos} · train {tr:.3f} · val {va:.3f} · "
                  f"faltan ~{resto/60:.1f} min", flush=True)
        if paso in hitos:
            muestra(paso)
    segundos = time.time() - t0
    print(f"\nENTRENAMIENTO: {segundos:.0f} s ({segundos/60:.1f} min) "
          f"en CPU con {torch.get_num_threads()} hilos, {args.pasos} pasos")

    modelo.eval()
    torch.save({"pesos": modelo.state_dict(), "historial": historial,
                "muestras": muestras, "segundos": segundos}, CHECK)
    print(f"checkpoint guardado en {CHECK} (no se versiona: *.pt está en .gitignore)")
    return exportar(modelo, tok, texto, verdad, historial, muestras,
                    segundos, n_par, ids_tr, ids_va, args)


def exportar(modelo, tok, texto, verdad, historial, muestras, segundos,
             n_par, ids_tr, ids_va, args):
    """Arma los paquetes de datos que comen las cuatro visualizaciones."""
    # ---------------------------------------------------------------- bigrama
    print("\nentrenando el bigrama (la linea de base tonta)...")
    tabla = torch.zeros(len(tok), len(tok))
    for a, b in zip(ids_tr[:-1].tolist(), ids_tr[1:].tolist()):
        tabla[a, b] += 1
    probs_bi = tabla / tabla.sum(1, keepdim=True).clamp(min=1)
    gbi = torch.Generator().manual_seed(SEMILLA)
    cur = tok.a_id["S"]
    bi = []
    for _ in range(260):
        cur = int(torch.multinomial(probs_bi[cur], 1, generator=gbi))
        bi.append(cur)
    texto_bigrama = tok.decodificar(bi)
    perdida_bigrama = float(
        -torch.log(probs_bi[ids_va[:-1], ids_va[1:]].clamp(min=1e-9)).mean())
    print("bigrama:", texto_bigrama[:120].replace("\n", " ⏎ "))
    print(f"loss del bigrama en validacion: {perdida_bigrama:.3f}")

    # ----------------------------------------------- 1. viz/temperatura.html
    print("\nexportando temperatura.html ...")
    prompts_T = [
        {"id": "apertura", "texto": "Señor presidente, ",
         "por_que": "arranque de discurso: el modelo tiene muchas continuaciones posibles"},
        {"id": "medio", "texto": "Quiero ser cl",
         "por_que": "en el medio de una palabra: casi no hay duda"},
        {"id": "bloque", "texto": "El bloque del ",
         "por_que": "acá viene el nombre de un partido: hay pocos, y todos plausibles"},
        {"id": "voto", "texto": "Se va a votar en gener",
         "por_que": "una fórmula ritual del reglamento: la sabe de memoria"},
    ]
    temps = [round(0.1 * i, 1) for i in range(0, 21)]      # 0.0 .. 2.0
    semillas = [1, 2, 3, 4, 5]
    t1 = time.time()
    generaciones = generar_lote(modelo, tok, [p["texto"] for p in prompts_T],
                                temps, semillas, 200)
    print(f"  {len(prompts_T)*len(temps)*len(semillas)} generaciones en "
          f"{time.time()-t1:.0f} s")
    for i, p in enumerate(prompts_T):
        p["distribucion"] = distribucion(modelo, tok, p["texto"])
        p["generaciones"] = generaciones[str(i)]

    # ------------------------------------------ 2. viz/ventana-de-contexto.html
    print("exportando ventana-de-contexto.html ...")
    #
    # ESTA SECCION SE REESCRIBIO DESPUES DE MEDIR. La version original iba a
    # mostrar que el modelo pierde el bloque de quien habla cuando el encabezado
    # se cae de la ventana. Se midio y NO PASA: el modelo nunca aprendio esa
    # dependencia larga (acierta al nivel del azar con la ventana entera).
    # Publicar esa viz habria sido inventar un resultado. Lo que si aprendio es
    # la dependencia CORTA —el nombre del diputado predice su bloque— y ahi el
    # corte se ve perfecto. Exportamos las dos: la que funciona muestra el corte
    # duro de la ventana, y la que no funciona muestra que estar adentro de la
    # ventana no alcanza (el "lost in the middle" de los modelos grandes, en
    # chiquito). Las dos son mediciones reales sobre 30 y 24 casos del corpus.
    #
    patron_enc = re.compile(
        r"Diputad[oa] ([A-Z][a-z]+ [A-Z][a-z]+) \(([A-Z]{3}) — ([^)]+)\)\.")
    NOMBRE_PARTIDO = {pp["sigla"]: pp["nombre"] for pp in verdad["partidos"]}
    ventanas = list(range(4, CTX + 1, 4))

    # --- caso A: la pista CERCA (el nombre, a ~16 fichas del corte) -----------
    vistos, cerca = set(), []
    for mm in patron_enc.finditer(texto):
        if mm.group(1) in vistos or mm.start() < 300:
            continue
        vistos.add(mm.group(1))
        corte = mm.start(2)                       # justo despues del "("
        cerca.append({"texto": texto[mm.start() - 150:corte],
                      "objetivo": mm.group(2), "nombre": mm.group(1),
                      "dist": corte - mm.start(1)})
    cerca = cerca[:30]

    # --- caso B: la pista LEJOS (el encabezado, a 40-120 fichas) --------------
    lejos = []
    for mm in patron_enc.finditer(texto):
        fin_enc = mm.end()
        b = texto.find("El bloque del ", fin_enc, fin_enc + 600)
        sig = texto.find("Diputad", fin_enc)
        if b > 0 and (sig < 0 or b < sig):
            corte = b + len("El bloque del ")
            d = corte - mm.start(2)
            if 40 <= d <= 120:
                lejos.append({"texto": texto[mm.start():corte],
                              "objetivo": NOMBRE_PARTIDO[mm.group(2)],
                              "nombre": mm.group(1), "sigla": mm.group(2),
                              "dist": d})
    lejos = lejos[:24]

    casos_ventana = []
    for cid, grupo, largo_obj, pregunta, titulo, explicacion, tramo_de in [
        ("cerca", cerca, 3,
         "¿de qué bloque es este diputado?",
         "La pista está CERCA: el nombre, a unas 16 fichas",
         "El modelo aprendió que el nombre de cada diputado predice su bloque. "
         "La pista es el nombre completo. Achicá la ventana hasta que el nombre "
         "de pila quede afuera y mirá qué pasa.",
         lambda c: (c["texto"].rindex(c["nombre"]),
                    c["texto"].rindex(c["nombre"]) + len(c["nombre"]))),
        ("lejos", lejos, 10,
         "¿de qué bloque es quien viene hablando?",
         "La pista está LEJOS: el encabezado, a unas 70 fichas",
         "Acá el dato está en el encabezado del turno, mucho más atrás. "
         "Ojo con esta curva: es plana. Aunque la pista esté ADENTRO de la "
         "ventana, este modelo no la usa. Su horizonte efectivo es más corto "
         "que su ventana.",
         lambda c: (c["texto"].index("("), c["texto"].index(")") + 1)),
    ]:
        curva, ok_por_k = [], {}
        for k in ventanas:
            recortes = [c["texto"][-k:] for c in grupo]
            conts = completar_lote(modelo, tok, recortes, largo_obj + 2)
            ok = [x.startswith(c["objetivo"][:largo_obj])
                  for c, x in zip(grupo, conts)]
            dentro = sum(1 for c in grupo if c["dist"] <= k)
            curva.append({"ventana": k, "aciertos": sum(ok), "n": len(grupo),
                          "con_pista": dentro})
            ok_por_k[k] = ok
        print(f"  [{cid}] pista a ~{sorted(c['dist'] for c in grupo)[len(grupo)//2]} "
              f"fichas · {len(grupo)} casos reales del corpus")
        for c in curva:
            if c["ventana"] in (4, 8, 12, 16, 24, 32, 64, 128):
                print(f"     ventana {c['ventana']:3d}: {c['aciertos']:2d}/{c['n']} "
                      f"aciertos (pista adentro en {c['con_pista']})")

        # el ejemplo concreto: uno que falle con la ventana chica y acierte con
        # la entera. Si ninguno flipea (caso "lejos"), se toma el primero y se dice.
        cand = [i for i in range(len(grupo))
                if ok_por_k[CTX][i] and not ok_por_k[8][i]]
        iEj = cand[0] if cand else 0
        c = grupo[iEj]
        print(f"     ejemplo: {c['nombre']} ({'flipea' if cand else 'NO flipea'})")
        barrido = []
        for k in ventanas:
            recorte = c["texto"][-k:]
            idx = torch.tensor([tok.codificar(recorte)])
            with torch.no_grad():
                logits, _ = modelo(idx)
                probs = torch.softmax(logits[0, -1, :], dim=-1)
            orden = torch.argsort(probs, descending=True)[:6]
            cont = completar_lote(modelo, tok, [recorte], largo_obj + 12)[0]
            p_obj, _ = prob_de_la_continuacion(modelo, tok, recorte,
                                               c["objetivo"][:largo_obj])
            barrido.append({
                "ventana": k,
                "top": [{"ficha": tok.a_ficha[int(i)], "prob": round(float(probs[i]), 5)}
                        for i in orden],
                "continuacion": cont,
                "prob_correcta": p_obj,
                "acierta": cont.startswith(c["objetivo"][:largo_obj]),
            })
        a, b = tramo_de(c)
        casos_ventana.append({
            "id": cid, "pregunta": pregunta, "titulo": titulo,
            "explicacion": explicacion,
            "ejemplo": {"texto": c["texto"], "objetivo": c["objetivo"],
                        "nombre": c["nombre"], "distancia_pista": c["dist"],
                        "tramo_pista": [a, b], "flipea": bool(cand),
                        "barrido": barrido},
            "curva": curva, "n_casos": len(grupo),
        })
    ventana_pack = {"casos": casos_ventana, "contexto_maximo": CTX,
                    "azar": round(1 / len(verdad["partidos"]), 3)}

    # -------------------------------------------- 3. viz/por-que-alucina.html
    print("exportando por-que-alucina.html ...")
    # Primero, un numero honesto: de los 60 diputados que SI existen, ¿a cuantos
    # les acierta el bloque? Porque "alucina" no quiere decir "no sabe nada".
    # De a uno, sin relleno: `completar_lote` empareja los prompts agregando
    # espacios a la izquierda, y con nombres de distinto largo eso cambia un poco
    # el contexto. El notebook lo hace de a uno, así que acá también: los dos
    # tienen que dar EXACTAMENTE el mismo número.
    prompts_padron = [f"{d['tratamiento'].capitalize()} {d['nombre']} ("
                      for d in verdad["diputados"]]
    completados = [completar_lote(modelo, tok, [pr], 26)[0] for pr in prompts_padron]
    aciertos_partido, aciertos_prov, detalle_padron = 0, 0, []
    for d, cont in zip(verdad["diputados"], completados):
        ok_p = cont.startswith(d["partido"])
        ok_v = cont.split(")")[0].endswith(d["provincia"])
        aciertos_partido += ok_p
        aciertos_prov += ok_v
        detalle_padron.append({"nombre": d["nombre"], "partido": d["partido"],
                               "provincia": d["provincia"],
                               "generado": cont.split(")")[0] + ")",
                               "acierta_partido": ok_p, "acierta_provincia": ok_v})
    print(f"  el modelo acierta el bloque de {aciertos_partido}/60 diputados "
          f"y la provincia de {aciertos_prov}/60")

    # Para la demostracion elegimos uno que acierta LAS DOS COSAS, y lo decimos.
    elegido = next((d for d, x in zip(verdad["diputados"], detalle_padron)
                    if x["acierta_partido"] and x["acierta_provincia"]),
                   verdad["diputados"][0])
    reales = {d["nombre"] for d in verdad["diputados"]}
    casos_aluc = [
        {"id": "existe",
         "titulo": "Un diputado que SÍ está en el padrón",
         "prompt": f"{elegido['tratamiento'].capitalize()} {elegido['nombre']} (",
         "verdad": f"{elegido['partido']} — {elegido['provincia']}",
         "existe": True},
        {"id": "no-existe",
         "titulo": "Una diputada que NO existe (nos la inventamos nosotros)",
         "prompt": "Diputada Marisol Bengoechea (",
         "verdad": None, "existe": False},
        {"id": "ley",
         "titulo": "Una ley que no está en el padrón",
         "prompt": "Cuando discutimos la Ley 7841 de ",
         "verdad": None, "existe": False},
        {"id": "cita",
         "titulo": "Una cita atribuida a una provincia que no existe",
         "prompt": ("Los intendentes de Puerto Bermejo nos mandaron una nota. "
                    "Dice, textual: \""),
         "verdad": None, "existe": False},
    ]
    for caso in casos_aluc:
        caso["generado"] = completar_lote(modelo, tok, [caso["prompt"]], 110)[0]
        caso["distribucion"] = distribucion(modelo, tok, caso["prompt"], tope=10)
        _, caso["confianza"] = prob_de_la_continuacion(
            modelo, tok, caso["prompt"], caso["generado"][:18])
        print(f"  [{caso['id']}] {caso['prompt']}«{caso['generado'][:62]}»")
    aluc_pack = {
        "casos": casos_aluc,
        "aciertos_partido": aciertos_partido,
        "aciertos_provincia": aciertos_prov,
        "total_diputados": len(verdad["diputados"]),
        "padron_detalle": detalle_padron,
        "padron": {
            "diputados": sorted(reales),
            "partidos": [{"sigla": pp["sigla"], "nombre": pp["nombre"]}
                         for pp in verdad["partidos"]],
            "leyes": [{"numero": l["numero"], "titulo": l["titulo"]}
                      for l in verdad["leyes"]],
            "provincias": verdad["provincias"],
        },
    }

    # ----------------------------------------------- 4. viz/contar-letras.html
    print("exportando contar-letras.html ...")
    palabras_contar = ["ferrocarril", "arroz", "irresponsabilidad",
                       "inconstitucionalidad", "reglamentaria", "carro"]
    contar_pack = []
    for pal in palabras_contar:
        pregunta = (f"Pregunta: ¿cuantas letras R tiene la palabra {pal}? "
                    f"Respuesta: tiene ")
        contar_pack.append({
            "palabra": pal,
            "erres_de_verdad": pal.lower().count("r"),
            "prompt": pregunta,
            "respuesta_modelo": completar_lote(modelo, tok, [pregunta], 30)[0],
        })
        print(f"  {pal}: tiene {pal.count('r')} · el modelo contesta "
              f"«{contar_pack[-1]['respuesta_modelo'][:26]}»")

    # ------------------------------------------------------------ el paquete
    paquete = {
        "meta": {
            "corpus": "Aguasclaras — debates parlamentarios SINTETICOS",
            "sintetico": True,
            "caracteres": len(texto),
            "vocabulario": len(tok),
            "fichas_vocabulario": tok.fichas,
            "parametros": n_par,
            "capas": CAPAS, "cabezas": CABEZAS, "dim": DIM, "contexto": CTX,
            "lote": LOTE, "pasos": args.pasos, "lr": LR, "semilla": SEMILLA,
            "segundos_cpu": round(segundos, 1),
            "hilos_cpu": torch.get_num_threads(),
            "cpu": platform.processor() or platform.machine(),
            "torch": torch.__version__,
            "loss_inicial": historial[0]["val"],
            "loss_final_train": historial[-1]["train"],
            "loss_final_val": historial[-1]["val"],
            "loss_bigrama_val": round(perdida_bigrama, 4),
            "generado_por": "clases/08-mini-gpt-y-los-llm/entrenar-mini-gpt.py",
        },
        "historial": historial,
        "muestras": muestras,
        "bigrama": {"texto": texto_bigrama, "loss_val": round(perdida_bigrama, 4)},
        "temperatura": {"prompts": prompts_T, "temperaturas": temps,
                        "semillas": semillas},
        "ventana": ventana_pack,
        "alucinacion": aluc_pack,
        "contar": contar_pack,
    }

    (SALIDA / "datos-mini-gpt.json").write_text(
        json.dumps(paquete, ensure_ascii=False, indent=1), encoding="utf-8")
    (SALIDA / "datos-mini-gpt.js").write_text(
        "/* GENERADO por entrenar-mini-gpt.py — no lo edites a mano.\n"
        "   Todo lo que muestran las viz de la clase 8 sale de esta corrida real\n"
        "   del mini-GPT sobre el corpus SINTETICO Aguasclaras. */\n"
        "const DATOS_MINIGPT = " + json.dumps(paquete, ensure_ascii=False) + ";\n"
        "if (typeof window !== 'undefined') window.DATOS_MINIGPT = DATOS_MINIGPT;\n",
        encoding="utf-8")

    print("\n" + "=" * 74)
    print(f"escrito: {SALIDA/'datos-mini-gpt.js'}")
    print(f"escrito: {SALIDA/'datos-mini-gpt.json'}")
    print(f"NUMERO PARA LAS SLIDES: {n_par:,} perillas · "
          f"{segundos/60:.1f} min de CPU ({torch.get_num_threads()} hilos) · "
          f"loss val {historial[0]['val']:.2f} -> {historial[-1]['val']:.2f}")
    print("=" * 74)


if __name__ == "__main__":
    main()
