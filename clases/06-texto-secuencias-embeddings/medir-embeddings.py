#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera `datos-embeddings.js`: los números REALES que consumen las
visualizaciones de la clase 6.

Regla de la casa: una viz no muestra números inventados. Todo lo que se ve en
`viz/*.html` sale de acá, y acá sale del corpus real de discursos de apertura
(1984-2019, `datos/muestras/discursos-apertura/corpus-mini-gpt.txt`).

La configuración de abajo (CONFIG) es **la misma que usa el notebook de la
clase**. Si la tocás acá, tocala también en `notebook.ipynb`, o los vecinos que
el aula ve en la pantalla dejan de ser los que le salen a ella en la compu.

Uso:

    PYTHONPATH=_shared python3 clases/06-texto-secuencias-embeddings/medir-embeddings.py

Tarda ~2 minutos en CPU. Deja además un `.npz` de cache al lado, para que una
segunda corrida sea instantánea (borralo si cambiás CONFIG).
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time
from collections import Counter

import numpy as np

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(RAIZ / "_shared"))

from ssdl import datos  # noqa: E402

# --- la configuración compartida con el notebook -----------------------------
CONFIG = dict(dim=100, top=2000, ventana=5, minimo=8)
SEMILLA = 1983

# cuántas palabras entran al mapa de la viz (las más frecuentes del vocabulario)
N_MAPA = 700

# palabras de función: no las sacamos del vocabulario (PPMI las deja adentro y
# eso es parte de la lección), pero el mapa las puede esconder con un toggle.
FUNCION = set("""
de la que el en y a los las del se por un una con no para es su al lo como más
pero sus le ya o este sí porque esta entre cuando muy sin sobre también me hasta
hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante
ellos e esto mí antes algunos qué unos yo otro otras otra él tanto esa estos mucho
quienes nada muchos cual poco ella estar estas algunas algo nosotros mi mis tú te
ti tu tus ellas nosotras vosotros vosotras os mío mía míos mías tuyo tuya suyo
suya nuestro nuestra nuestros nuestras esos esas fue ser son era han ha he has
había habían hemos hacia cada tras según ademas además cuyo cuya cuyos cuyas
así aún aun bien solo sólo entonces luego mientras siempre nunca casi tal cuanto
sea sean fueron será serán sido siendo estamos están está estaba estaban puede
pueden podemos debe deben hace hacer tiene tienen tener haber hoy ahora acá aquí
allí ahí toda todas dos tres mil millones ciento por
""".split())

# el léxico temático del curso (datos/preparar_corpus.py) + vocabulario
# institucional. Sirve para el filtro "sólo léxico político" del mapa.
LEXICO_TEMA = {
    "seguridad": ["seguridad", "inseguridad", "delito", "delitos", "delincuencia",
                  "policía", "policial", "narcotráfico", "robo", "crimen",
                  "cárcel", "cárceles", "gendarmería", "criminalidad", "penal"],
    "economía": ["inflación", "precios", "devaluación", "deuda", "déficit",
                 "dólar", "экономía", "economía", "económica", "económico",
                 "impuestos", "impuesto", "fiscal", "presupuesto", "inversión",
                 "exportaciones", "crecimiento", "pobreza", "producción"],
    "educación": ["educación", "educativa", "educativo", "escuela", "escuelas",
                  "docente", "docentes", "universidad", "universidades",
                  "alumnos", "maestros", "ciencia", "investigación"],
    "trabajo": ["trabajo", "trabajadores", "empleo", "desempleo", "desocupación",
                "salario", "salarios", "sindicatos", "jubilación", "jubilados",
                "paritarias"],
    "salud": ["salud", "hospital", "hospitales", "sanitario", "médicos",
              "medicamentos", "enfermedades", "vacunas", "epidemia"],
    "instituciones": ["congreso", "senado", "diputados", "senadores", "ley",
                      "leyes", "proyecto", "sanción", "constitución", "justicia",
                      "corte", "poder", "estado", "gobierno", "provincias",
                      "municipios", "federal", "democracia", "república",
                      "elecciones", "voto", "reforma", "decreto"],
}


# =============================================================================
# 1. corpus
# =============================================================================
def cargar_corpus():
    """Devuelve (texto_completo, {anio: texto}) desde las muestras del repo."""
    texto = datos.corpus_mini_gpt()
    # el archivo trae marcas "### 1984 — Raul Alfonsin" entre discursos
    partes = re.split(r"^###\s+(\d{4})\s+—\s+(.+)$", texto, flags=re.M)
    porAnio = {}
    for i in range(1, len(partes), 3):
        anio = int(partes[i])
        porAnio[anio] = partes[i + 2]
    return texto, porAnio


# =============================================================================
# 2. embeddings (el mismo motor que usa el notebook)
# =============================================================================
def embeddings(texto, **cfg):
    t0 = time.time()
    V, palabras = datos.embeddings_ppmi_svd(texto, **cfg)
    return V, palabras, time.time() - t0


def pca2d(V):
    """PCA a mano: centrar y quedarse con las dos direcciones más grandes."""
    X = V - V.mean(axis=0, keepdims=True)
    U, S, Wt = np.linalg.svd(X, full_matrices=False)
    XY = U[:, :2] * S[:2]
    var = float((S[:2] ** 2).sum() / (S ** 2).sum())
    return XY, var


def vecinos_de(w, V, palabras, idx, k=10, excluir_funcion=False):
    i = idx[w]
    sim = V @ V[i]
    orden = np.argsort(-sim)
    out = []
    for j in orden:
        if j == i:
            continue
        if excluir_funcion and palabras[j] in FUNCION:
            continue
        out.append([palabras[j], round(float(sim[j]), 3)])
        if len(out) >= k:
            break
    return out


# =============================================================================
# 3. un BPE chiquito, entrenado sobre el corpus
# =============================================================================
def entrenar_bpe(texto, n_merges=600, max_palabras=6000):
    """
    BPE de manual: arrancar con caracteres y pegar el par más frecuente,
    `n_merges` veces. Devuelve la lista de fusiones en orden.

    Es el mismo algoritmo que usan los tokenizadores de verdad; lo que cambia
    es la escala (acá 600 fusiones sobre un corpus de 2 MB; GPT-4 usa ~100.000
    fichas sobre terabytes).
    """
    palabras = re.findall(r"[a-záéíóúñü]+", texto.lower())
    frec = Counter(palabras).most_common(max_palabras)
    vocab = {" ".join(list(p)) + " </w>": c for p, c in frec}
    fusiones = []
    for _ in range(n_merges):
        pares = Counter()
        for palabra, c in vocab.items():
            fichas = palabra.split()
            for a, b in zip(fichas, fichas[1:]):
                pares[(a, b)] += c
        if not pares:
            break
        (a, b), _ = pares.most_common(1)[0]
        fusiones.append([a, b])
        patron = re.compile(r"(?<!\S)" + re.escape(a + " " + b) + r"(?!\S)")
        vocab = {patron.sub(a + b, p): c for p, c in vocab.items()}
    return fusiones


def aplicar_bpe(palabra, rango):
    """Aplica las fusiones a una palabra. Es la misma función que va en JS."""
    fichas = list(palabra) + ["</w>"]
    while True:
        mejor, mejor_i = None, -1
        for i in range(len(fichas) - 1):
            r = rango.get((fichas[i], fichas[i + 1]))
            if r is not None and (mejor is None or r < mejor):
                mejor, mejor_i = r, i
        if mejor is None:
            break
        fichas[mejor_i:mejor_i + 2] = [fichas[mejor_i] + fichas[mejor_i + 1]]
    return fichas


# =============================================================================
# 4. el programa
# =============================================================================
def main():
    np.random.seed(SEMILLA)
    print("Corpus...")
    texto, porAnio = cargar_corpus()
    anios = sorted(porAnio)
    print(f"  {len(texto):,} caracteres · {len(porAnio)} discursos "
          f"({anios[0]}-{anios[-1]})")

    cache = AQUI / "cache-embeddings.npz"
    if cache.exists():
        z = np.load(cache, allow_pickle=True)
        V, palabras, seg = z["V"], list(z["palabras"]), float(z["seg"])
        print(f"  (embeddings leídos del cache, la corrida original tardó {seg:.0f} s)")
    else:
        print(f"Embeddings PPMI+SVD {CONFIG} ...")
        V, palabras, seg = embeddings(texto, **CONFIG)
        np.savez_compressed(cache, V=V, palabras=np.array(palabras), seg=seg)
        print(f"  {V.shape} en {seg:.0f} s")
    idx = {p: i for i, p in enumerate(palabras)}

    # --- frecuencias (para ordenar el mapa) ---------------------------------
    tok = datos.TokenizadorPalabras(minusculas=True)
    fichas = [f for f in tok.partir(texto) if f.isalpha()]
    frec = Counter(fichas)

    # --- las palabras del mapa ---------------------------------------------
    mapa = palabras[:N_MAPA]
    Vm = V[:N_MAPA]
    XY, var2d = pca2d(Vm)
    # normalizamos a [-1, 1] para que la viz no tenga que pensar en escalas
    XY = XY / np.abs(XY).max()

    lex = {}
    for tema, ws in LEXICO_TEMA.items():
        for w in ws:
            if w in idx:
                lex[w] = tema

    salida = {
        "meta": {
            "corpus": "discursos de apertura de sesiones, Argentina 1984-2019",
            "fuente": "datos/muestras/discursos-apertura/corpus-mini-gpt.txt",
            "real": True,
            "caracteres": len(texto),
            "discursos": len(porAnio),
            "tokens": len(fichas),
            "vocabulario_util": len(palabras),
            "segundos": round(seg, 1),
            "semilla": SEMILLA,
            "config": CONFIG,
            "generado_por": "clases/06-texto-secuencias-embeddings/medir-embeddings.py",
        },
        "mapa": {
            "palabras": mapa,
            "xy": [[round(float(a), 4), round(float(b), 4)] for a, b in XY],
            "vec": [[round(float(x), 4) for x in v] for v in Vm],
            "frec": [int(frec[p]) for p in mapa],
            "funcion": [1 if p in FUNCION else 0 for p in mapa],
            "tema": [lex.get(p, "") for p in mapa],
            "varianza_2d": round(var2d, 3),
        },
    }

    # --- vecinos de ejemplo (los de la slide 20) ----------------------------
    ejemplos = ["seguridad", "reforma", "docentes", "provincias", "mujeres",
                "inflación", "educación", "trabajo", "justicia", "pobreza"]
    salida["vecinos_ejemplo"] = {
        w: vecinos_de(w, V, palabras, idx, k=10)
        for w in ejemplos if w in idx
    }

    # --- antónimos: la advertencia de validez -------------------------------
    pares = [("guerra", "paz"), ("aprobar", "rechazar"), ("aumentar", "disminuir"),
             ("mayoría", "minoría"), ("público", "privado"), ("importaciones", "exportaciones")]
    salida["antonimos"] = [
        [a, b, round(float(V[idx[a]] @ V[idx[b]]), 3)]
        for a, b in pares if a in idx and b in idx
    ]

    # --- aritmética: los que funcionan y los que no -------------------------
    def aritmetica(a, b, c, k=5):
        if not all(w in idx for w in (a, b, c)):
            return None
        v = V[idx[a]] - V[idx[b]] + V[idx[c]]
        v = v / (np.linalg.norm(v) + 1e-9)
        sim = V @ v
        fuera = {idx[a], idx[b], idx[c]}
        out = []
        for j in np.argsort(-sim):
            if j in fuera:
                continue
            out.append([palabras[j], round(float(sim[j]), 3)])
            if len(out) >= k:
                break
        return out

    candidatos = [
        ("senadores", "senado", "diputados"),
        ("provincias", "provincia", "municipios"),
        ("escuelas", "escuela", "hospitales"),
        ("ministro", "ministerio", "secretaría"),
        ("mujeres", "hombres", "trabajadores"),
        ("inflación", "precios", "desempleo"),
        ("educación", "escuelas", "salud"),
        ("buenos", "aires", "córdoba"),
        ("presidente", "ejecutivo", "legislativo"),
        ("ley", "congreso", "decreto"),
    ]
    salida["aritmetica"] = [
        {"a": a, "b": b, "c": c, "resultados": r}
        for a, b, c in candidatos
        if (r := aritmetica(a, b, c)) is not None
    ]

    # --- ejes (el modo del paper de Kozlowski et al.) -----------------------
    def proyectar(pos, neg, lista):
        """Proyecta cada palabra sobre el eje (pos − neg). Devuelve ordenado."""
        if pos not in idx or neg not in idx:
            return None
        eje = V[idx[pos]] - V[idx[neg]]
        eje = eje / (np.linalg.norm(eje) + 1e-9)
        out = []
        for w in lista:
            if w in idx:
                out.append([w, round(float(V[idx[w]] @ eje), 3)])
        out.sort(key=lambda t: -t[1])
        return out

    ocupaciones = ["docentes", "maestros", "enfermeras", "médicos", "científicos",
                   "trabajadores", "empresarios", "obreros", "jueces", "policías",
                   "militares", "diputados", "senadores", "ministros", "dirigentes",
                   "productores", "estudiantes", "profesionales", "investigadores",
                   "jubilados", "agricultores", "industriales", "sindicalistas"]
    conceptos = ["familia", "hogar", "cuidado", "hijos", "niños", "trabajo",
                 "empresa", "fuerza", "casa", "escuela", "salario", "poder",
                 "protección", "derechos", "violencia", "salud", "seguridad"]
    ejes = [
        {"id": "genero", "pos": "mujeres", "neg": "hombres",
         "etiqueta": "mujeres ←→ hombres",
         "listas": {"ocupaciones": ocupaciones, "conceptos": conceptos}},
        {"id": "estado", "pos": "estado", "neg": "mercado",
         "etiqueta": "Estado ←→ mercado",
         "listas": {"ocupaciones": ocupaciones, "conceptos": conceptos}},
        {"id": "tiempo", "pos": "futuro", "neg": "pasado",
         "etiqueta": "futuro ←→ pasado",
         "listas": {"ocupaciones": ocupaciones, "conceptos": conceptos}},
    ]
    salida["ejes"] = []
    for e in ejes:
        listas = {}
        for nombre, lista in e["listas"].items():
            pr = proyectar(e["pos"], e["neg"], lista)
            if pr:
                listas[nombre] = pr
        if listas and e["pos"] in idx and e["neg"] in idx:
            salida["ejes"].append({"id": e["id"], "pos": e["pos"], "neg": e["neg"],
                                   "etiqueta": e["etiqueta"], "listas": listas})

    # --- dos épocas: cambio semántico ---------------------------------------
    print("Embeddings por época...")
    epocas = [("1984-1999", [a for a in anios if a <= 1999]),
              ("2004-2019", [a for a in anios if a >= 2004])]
    cache_ep = AQUI / "cache-epocas.npz"
    guardar_ep = {}
    if cache_ep.exists():
        z = np.load(cache_ep, allow_pickle=True)
        pares_ep = {k: (z[k + "_V"], list(z[k + "_p"])) for k, _ in epocas}
    else:
        pares_ep = {}
        for nombre, aa in epocas:
            t = "\n".join(porAnio[a] for a in aa)
            Ve, pe, se = embeddings(t, dim=60, top=1200, ventana=5, minimo=4)
            print(f"  {nombre}: {len(aa)} discursos, vocab {len(pe)}, {se:.0f} s")
            pares_ep[nombre] = (Ve, pe)
            guardar_ep[nombre + "_V"] = Ve
            guardar_ep[nombre + "_p"] = np.array(pe)
        np.savez_compressed(cache_ep, **guardar_ep)

    comunes = None
    for nombre, _ in epocas:
        s = set(pares_ep[nombre][1])
        comunes = s if comunes is None else (comunes & s)
    interes = [w for w in mapa[:400] if w in comunes and w not in FUNCION][:220]
    salida["epocas"] = {"nombres": [n for n, _ in epocas], "palabras": interes,
                        "vecinos": {}}
    for nombre, _ in epocas:
        Ve, pe = pares_ep[nombre]
        ie = {p: i for i, p in enumerate(pe)}
        salida["epocas"]["vecinos"][nombre] = {
            w: vecinos_de(w, Ve, pe, ie, k=8, excluir_funcion=True)
            for w in interes
        }

    # --- BPE ----------------------------------------------------------------
    print("BPE...")
    fusiones = entrenar_bpe(texto, n_merges=600)
    rango = {(a, b): i for i, (a, b) in enumerate(fusiones)}
    prueba = ["inconstitucionalidad", "desfinanciamiento", "presidente", "ley",
              "gobernabilidad", "irreprochable"]
    salida["bpe"] = {
        "fusiones": fusiones,
        "n_fusiones": len(fusiones),
        "ejemplos": {w: aplicar_bpe(w, rango) for w in prueba},
    }
    for w in prueba:
        print("   ", w, "->", " · ".join(aplicar_bpe(w, rango)))

    # --- similitud entre discursos (para el pie de la viz y la coherencia
    #     con el notebook) ----------------------------------------------------
    def vector_doc(t):
        ff = [f for f in tok.partir(t) if f.isalpha() and f in idx]
        if not ff:
            return None
        v = V[[idx[f] for f in ff]].mean(axis=0)
        return v / (np.linalg.norm(v) + 1e-9)

    docs = {a: vector_doc(porAnio[a]) for a in anios}
    D = np.array([docs[a] for a in anios])
    S = D @ D.T
    np.fill_diagonal(S, -2)
    i, j = np.unravel_index(np.argmax(S), S.shape)
    k, l = np.unravel_index(np.argmin(np.where(S < -1, 2, S)), S.shape)
    salida["discursos"] = {
        "anios": [int(a) for a in anios],
        "similitud": [[round(float(x), 3) for x in fila] for fila in (D @ D.T)],
        "mas_parecidos": [int(anios[i]), int(anios[j]), round(float(S[i, j]), 3)],
        "mas_distintos": [int(anios[k]), int(anios[l]),
                          round(float((D @ D.T)[k, l]), 3)],
    }
    print("  más parecidos:", salida["discursos"]["mas_parecidos"])
    print("  más distintos:", salida["discursos"]["mas_distintos"])

    # --- a disco ------------------------------------------------------------
    js = AQUI / "datos-embeddings.js"
    cuerpo = json.dumps(salida, ensure_ascii=False, separators=(",", ":"))
    js.write_text(
        "/* GENERADO por medir-embeddings.py — no lo edites a mano.\n"
        "   Números reales del corpus de discursos de apertura 1984-2019.\n"
        "   Misma configuración que el notebook de la clase: "
        + json.dumps(CONFIG) + " */\n"
        "const DATOS_EMB = " + cuerpo + ";\n"
        "if (typeof window !== 'undefined') window.DATOS_EMB = DATOS_EMB;\n",
        encoding="utf-8")
    print(f"\nEscrito {js} ({js.stat().st_size/1024:.0f} KB)")

    resumen = AQUI / "datos-embeddings-resumen.json"
    chico = {k: v for k, v in salida.items() if k not in ("mapa", "epocas")}
    resumen.write_text(json.dumps(chico, ensure_ascii=False, indent=1),
                       encoding="utf-8")
    print(f"Escrito {resumen} (el mismo contenido, sin las matrices, para leerlo)")


if __name__ == "__main__":
    main()
