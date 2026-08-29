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

Tarda ~15 segundos en CPU y escribe tres archivos:

    datos-embeddings.js            el mapa completo (2000 x 100) — la viz central
    datos-texto.js                 la parte liviana — tokenizador, one-hot, frases
    datos-embeddings-resumen.json  lo mismo sin las matrices, para leerlo con los ojos

Deja además dos `.npz` de cache al lado para que una segunda corrida sea
instantánea. **Esos `.npz` no van al repo**: son reproducibles corriendo esto, y
el script los regenera solo si no están. Borralos cuando termines (y siempre que
toques CONFIG).
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

# Cuántas palabras se DIBUJAN en el mapa de la viz. Los vectores van todos
# (las palabras interesantes —"embarazadas", "indigencia", "formosa"— están en
# el puesto 1500 y pico, y son justamente los vecinos que cuentan la historia).
N_MAPA = 2000        # cuántas entran como puntos y como universo de búsqueda
N_ETIQUETAS = 320    # cuántas llevan el nombre escrito encima, para que se lea

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
                 "dólar", "economía", "económica", "económico",
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
    # La MISMA partición en palabras que hace el notebook a mano, para que el
    # número que ve el aula en la slide sea el que le sale a ella en la compu.
    fichas = re.findall(r"[a-záéíóúñü]+", texto.lower())
    frec = Counter(fichas)

    # --- el mapa -----------------------------------------------------------
    mapa = palabras[:N_MAPA]
    Vm = V[:N_MAPA]
    XY, var2d = pca2d(Vm)
    # Normalizamos CADA EJE por separado a [-1, 1]. Ojo: eso reescala los dos
    # ejes distinto, así que la nube llena el recuadro y los grupos se ven.
    # La viz lo dice en el pie: las distancias que valen son las de las 100
    # dimensiones, no las del dibujo.
    XY = XY / np.abs(XY).max(axis=0, keepdims=True)

    lex = {}
    for tema, ws in LEXICO_TEMA.items():
        for w in ws:
            if w in idx:
                lex[w] = tema

    # cuáles llevan el nombre escrito: las más frecuentes que NO son de función,
    # más todo el léxico temático (aunque sea raro, si es del dominio se rotula).
    etiquetadas, vistas = [], set()
    for i, w in enumerate(mapa):
        if w in FUNCION or len(w) < 4:
            continue
        etiquetadas.append(i)
        vistas.add(i)
        if len(etiquetadas) >= N_ETIQUETAS:
            break
    for i, w in enumerate(mapa):
        if w in lex and i not in vistas:
            etiquetadas.append(i)
            vistas.add(i)
    etiquetadas.sort()

    salida = {
        "meta": {
            "corpus": "discursos de apertura de sesiones, Argentina 1984-2019",
            "fuente": "datos/muestras/discursos-apertura/corpus-mini-gpt.txt",
            "real": True,
            "caracteres": len(texto),
            "discursos": len(porAnio),
            "anios": [int(anios[0]), int(anios[-1])],
            "tokens": len(fichas),
            "vocabulario_util": len(palabras),
            "tipos_totales": len(frec),
            "hapax": int(sum(1 for c in frec.values() if c == 1)),
            "segundos": round(seg, 1),
            "semilla": SEMILLA,
            "config": CONFIG,
            "generado_por": "clases/06-texto-secuencias-embeddings/medir-embeddings.py",
        },
        "mapa": {
            "palabras": mapa,
            "xy": [[round(float(a), 4), round(float(b), 4)] for a, b in XY],
            "vec": [[round(float(x), 3) for x in v] for v in Vm],
            "frec": [int(frec[p_]) for p_ in mapa],
            "funcion": [1 if p_ in FUNCION else 0 for p_ in mapa],
            "tema": [lex.get(p_, "") for p_ in mapa],
            "etiquetadas": etiquetadas,
            "varianza_2d": round(var2d, 3),
        },
    }

    # --- vocabularios para el tokenizador ----------------------------------
    # (por palabras: las mismas 2000 del embedding; por caracteres: los que
    #  aparecen en el corpus, ordenados por frecuencia)
    frec_car = Counter(texto.lower())
    caracteres = [c for c, n in frec_car.most_common() if n >= 20 and c not in "\n\r"]
    salida["vocab"] = {"palabras": mapa, "caracteres": caracteres}

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

    # Cada analogía viene con lo que UNA PERSONA esperaría de antemano
    # (`esperado`), y `acierta` se calcula: ¿está esa palabra entre las 5 que
    # devuelve el modelo? No se elige después de mirar el resultado. Con un
    # corpus de 350.000 tokens, casi ninguna acierta, y eso es el contenido.
    candidatos = [
        ("inflación", "precios", "desempleo", "desocupación",
         "la relación «el problema y su síntoma» sí queda dibujada en el espacio"),
        ("presidente", "ejecutivo", "legislativo", "asamblea",
         "el corpus está lleno de «Asamblea Legislativa»: la analogía funciona "
         "porque la frase existe, no porque el modelo razone"),
        ("córdoba", "provincia", "salta", "provincias",
         "no devuelve «provincias», devuelve OTRAS provincias (formosa, mendoza, "
         "catamarca). El barrio es el correcto, la casa no"),
        ("escuelas", "escuela", "hospitales", "hospital",
         "plural → singular: no lo captura. El singular de una palabra rara "
         "aparece poco y su vector es peor"),
        ("senadores", "senado", "diputados", "cámara",
         "la relación «cuerpo → sus miembros» no está: devuelve otros cargos"),
        ("mujeres", "hombres", "niños", "niñas",
         "«niñas» ni siquiera está en el vocabulario del corpus. Ese dato "
         "también es un hallazgo sobre de qué se habla y de qué no"),
        ("leyes", "ley", "decretos", "decreto",
         "otra vez plural → singular. No hay relación morfológica en el espacio"),
        ("ministro", "ministerio", "juez", "justicia",
         "devuelve nombres propios y causas: el corpus habla de jueces "
         "concretos, no de la categoría"),
        ("educación", "escuelas", "salud", "hospitales",
         "devuelve palabras de política pública en general: el espacio agrupa "
         "por tema, no por la relación específica"),
        ("importaciones", "importar", "exportaciones", "exportar",
         "sustantivo → verbo tampoco. Los verbos aparecen en contextos muy "
         "distintos de los sustantivos"),
    ]
    salida["aritmetica"] = []
    for a, b, c, esperado, nota in candidatos:
        r = aritmetica(a, b, c)
        if r is None:
            continue
        salida["aritmetica"].append({
            "a": a, "b": b, "c": c, "esperado": esperado, "nota": nota,
            "esperado_en_vocab": esperado in idx,
            "acierta": esperado in [w for w, _ in r],
            "resultados": r,
        })
    n_ok = sum(1 for x in salida["aritmetica"] if x["acierta"])
    print(f"  aritmética: {n_ok} de {len(salida['aritmetica'])} analogías aciertan")

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
    # el vocabulario de sub-palabras: todas las fichas que produce el BPE sobre
    # las palabras del corpus, ordenadas por cuántas palabras distintas las usan.
    palabras_corpus = [w for w, _ in Counter(
        re.findall(r"[a-záéíóúñü]+", texto.lower())).most_common(8000)]
    uso = Counter()
    for w in palabras_corpus:
        for f in aplicar_bpe(w, rango):
            uso[f] += 1
    for c in caracteres:
        uso[c] += 0
    voc_bpe = [f for f, _ in uso.most_common()]
    salida["bpe"] = {
        "fusiones": fusiones,
        "n_fusiones": len(fusiones),
        "vocabulario": voc_bpe,
        "ejemplos": {w: aplicar_bpe(w, rango) for w in prueba},
    }
    print(f"    vocabulario de sub-palabras: {len(voc_bpe)} fichas")
    for w in prueba:
        print("   ", w, "->", " · ".join(aplicar_bpe(w, rango)))

    # --- similitud entre discursos (para el pie de la viz y la coherencia
    #     con el notebook) ----------------------------------------------------
    def vector_doc(t):
        ff = [f for f in re.findall(r"[a-záéíóúñü]+", t.lower()) if f in idx]
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

    # --- los pares de frases de `viz/bolsa-vs-orden.html` -------------------
    # La cuenta se hace ACÁ, no en el navegador, para que lo que se ve en la
    # slide sea un número medido y no una promesa.
    PARES = [
        {"id": "agencia", "titulo": "quién le hizo qué a quién",
         "a": "el gobierno criticó al congreso",
         "b": "el congreso criticó al gobierno",
         "roles_a": {"agente": "el gobierno", "paciente": "al congreso"},
         "roles_b": {"agente": "el congreso", "paciente": "al gobierno"},
         "humano": "En una son las mismas cinco palabras en otro orden, y cambia "
                   "quién es el que critica. Para un análisis de responsabilidad "
                   "política, es lo único que importa."},
        {"id": "gancho", "titulo": "el par del principio de la clase",
         "a": "la comisión rechazó al ministro",
         "b": "el ministro rechazó a la comisión",
         "roles_a": {"agente": "la comisión", "paciente": "al ministro"},
         "roles_b": {"agente": "el ministro", "paciente": "a la comisión"},
         "humano": "Acá la bolsa no queda idéntica del todo: cambian los "
                   "artículos («al» contra «a la»). Ninguna palabra con "
                   "contenido cambia. Y como casi todo pipeline de texto tira "
                   "las palabras vacías antes de contar, en la práctica el "
                   "vector que llega al modelo es el mismo."},
        {"id": "negacion", "titulo": "la negación",
         "a": "el proyecto fue aprobado por la cámara",
         "b": "el proyecto no fue aprobado por la cámara",
         "roles_a": {"resultado": "aprobado"},
         "roles_b": {"resultado": "NO aprobado"},
         "humano": "Difieren en una palabra de ocho y dicen lo contrario. "
                   "Un método que pesa todas las palabras igual va a decir que "
                   "estos dos documentos son casi el mismo documento. Y de "
                   "regalo, otra trampa: «aprobado» ni siquiera entró al "
                   "vocabulario de 2.000 palabras, así que se cae del promedio "
                   "y nadie te avisa. Las palabras fuera de vocabulario "
                   "desaparecen en silencio."},
        {"id": "denuncia", "titulo": "quién denuncia a quién",
         "a": "el sindicato denunció al empresario",
         "b": "el empresario denunció al sindicato",
         "roles_a": {"agente": "el sindicato", "paciente": "al empresario"},
         "roles_b": {"agente": "el empresario", "paciente": "al sindicato"},
         "humano": "Si estás codificando conflicto laboral, esta diferencia es "
                   "tu variable. Para la bolsa de palabras no existe."},
        {"id": "orden", "titulo": "el orden del procedimiento",
         "a": "primero se votó y después se debatió",
         "b": "primero se debatió y después se votó",
         "roles_a": {"secuencia": "votar → debatir"},
         "roles_b": {"secuencia": "debatir → votar"},
         "humano": "Mismísimas palabras, misma cantidad. Una describe un "
                   "parlamento que funciona y la otra un escándalo reglamentario."},
    ]

    def bolsa(frase):
        return Counter(frase.split())

    def prom_emb(frase):
        ws = [w for w in frase.split() if w in idx]
        if not ws:
            return None, []
        v = V[[idx[w] for w in ws]].mean(axis=0)
        return v / (np.linalg.norm(v) + 1e-9), ws

    salida["frases"] = []
    for par in PARES:
        ca, cb = bolsa(par["a"]), bolsa(par["b"])
        va, wa = prom_emb(par["a"])
        vb, wb = prom_emb(par["b"])
        fila = dict(par)
        fila["conteos"] = sorted(set(ca) | set(cb))
        fila["conteo_a"] = [int(ca.get(w, 0)) for w in fila["conteos"]]
        fila["conteo_b"] = [int(cb.get(w, 0)) for w in fila["conteos"]]
        fila["bolsa_identica"] = bool(ca == cb)
        fila["fuera_de_vocabulario"] = sorted(
            set(par["a"].split()) | set(par["b"].split()) - set())
        fila["fuera_de_vocabulario"] = [
            w for w in sorted(set(par["a"].split()) | set(par["b"].split()))
            if w not in idx]
        if va is not None and vb is not None:
            fila["coseno_promedio"] = round(float(va @ vb), 4)
            fila["vec_a"] = [round(float(x), 3) for x in va[:40]]
            fila["vec_b"] = [round(float(x), 3) for x in vb[:40]]
        salida["frases"].append(fila)
        print(f"    {par['id']}: bolsa idéntica={fila['bolsa_identica']} "
              f"coseno del promedio={fila.get('coseno_promedio')}")

    # --- las 6 palabras de `viz/one-hot-vs-embedding.html` ------------------
    ONEHOT = ["diputados", "senadores", "escuelas", "hospitales", "inflación", "trigo"]
    onehot = {"palabras": [], "vec": [], "id": [], "vecinos": {}, "coseno": []}
    for w in ONEHOT:
        if w not in idx:
            continue
        onehot["palabras"].append(w)
        onehot["id"].append(int(idx[w]))          # su posición en el vocabulario
        onehot["vec"].append([round(float(x), 3) for x in V[idx[w]]])
        onehot["vecinos"][w] = vecinos_de(w, V, palabras, idx, k=6,
                                          excluir_funcion=True)
    for a in onehot["palabras"]:
        onehot["coseno"].append([round(float(V[idx[a]] @ V[idx[b]]), 3)
                                 for b in onehot["palabras"]])
    onehot["dim_onehot"] = len(palabras)
    onehot["dim_emb"] = CONFIG["dim"]
    salida["onehot"] = onehot
    print("    one-hot: cos(diputados,senadores) =",
          onehot["coseno"][0][1], "· cos(diputados,trigo) =", onehot["coseno"][0][-1])

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

    # el archivo chico: lo que necesitan el tokenizador, la comparación
    # one-hot vs embedding y bolsa-vs-orden. Sin la matriz de 2000x100.
    chico_js = AQUI / "datos-texto.js"
    cuerpo_chico = json.dumps(
        {k: salida[k] for k in ("meta", "vocab", "bpe", "frases", "onehot",
                                "vecinos_ejemplo", "antonimos")},
        ensure_ascii=False, separators=(",", ":"))
    chico_js.write_text(
        "/* GENERADO por medir-embeddings.py — no lo edites a mano.\n"
        "   La parte liviana de los datos de la clase 6: vocabularios, BPE,\n"
        "   pares de frases y las seis palabras de one-hot vs embedding. */\n"
        "const DATOS_TEXTO = " + cuerpo_chico + ";\n"
        "if (typeof window !== 'undefined') window.DATOS_TEXTO = DATOS_TEXTO;\n",
        encoding="utf-8")
    print(f"Escrito {chico_js} ({chico_js.stat().st_size/1024:.0f} KB)")

    resumen = AQUI / "datos-embeddings-resumen.json"
    chico = {k: v for k, v in salida.items()
             if k not in ("mapa", "epocas", "vocab")}
    chico["bpe"] = {k: v for k, v in salida["bpe"].items() if k != "vocabulario"}
    chico["bpe"]["n_vocabulario"] = len(salida["bpe"]["vocabulario"])
    resumen.write_text(json.dumps(chico, ensure_ascii=False, indent=1),
                       encoding="utf-8")
    print(f"Escrito {resumen} (el mismo contenido, sin las matrices, para leerlo)")


if __name__ == "__main__":
    main()
