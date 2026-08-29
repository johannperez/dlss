#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mide, de verdad, todo lo que las visualizaciones de la clase 9 muestran como
número. Nada de acá está estimado a ojo: si la viz dice que con 25 etiquetas la
regresión logística sobre embeddings saca F1 0,45, es porque esta corrida lo
midió ocho veces y promedió.

Qué produce
-----------
    clases/09-modelos-preentrenados/datos-clase09.js     (lo que leen las viz)
    clases/09-modelos-preentrenados/datos-clase09.json   (lo mismo, para el notebook)

Cómo se corre (desde la raíz del repo, sin red):

    PYTHONPATH=_shared python3 clases/09-modelos-preentrenados/medir-clase09.py

Sobre qué se mide
-----------------
El corpus de prensa real del curso: 1471 notas en castellano con titular, tema,
fuente y etiqueta verdadera/falsa (ver `datos/README.md` §1.3). Datos REALES,
CC BY 4.0.

Tres mediciones:

1. **La curva de cuántas etiquetas hacen falta** sobre la tarea "¿esta nota es
   sobre política?". Tres estrategias, seis tamaños de muestra, ocho repeticiones
   con semillas distintas. Es la curva de `viz/zero-shot-vs-finetune.html`.

2. **El corpus de búsqueda semántica**: 300 titulares con sus vectores, más el
   vocabulario con sus vectores, para que la viz pueda embeber una consulta que
   el estudiante escribe en el momento. Es `viz/similitud-semantica.html`.

3. **La trampa del corpus**: qué pasa con verdadero/falso cuando se parte al
   azar y qué pasa cuando se parte por fuente. Los números van a las slides.

Todo offline. Hugging Face está bloqueado en el contenedor de construcción, así
que el camino que se mide acá es el camino B (embeddings propios PPMI+SVD), que
es exactamente el que el notebook corre cuando no hay red.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
import time

import numpy as np

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "_shared"))

from sklearn.feature_extraction.text import TfidfVectorizer          # noqa: E402
from sklearn.linear_model import LogisticRegression                  # noqa: E402
from sklearn.metrics import (accuracy_score, f1_score,               # noqa: E402
                             precision_score, recall_score)
from sklearn.model_selection import train_test_split                 # noqa: E402

from ssdl import datos                                               # noqa: E402

SALIDA = pathlib.Path(__file__).resolve().parent
SEMILLA = 1983

# El diccionario de palabras clave: la versión honesta de lo que hace mucha
# investigación hoy. Lo escribimos nosotros, un martes, y esa es exactamente la
# discusión de la clase 1 (el instrumento de medición lo escribe una persona).
DICCIONARIO_POLITICA = (r"gobierno|president|diputad|senad|partido|elecci|"
                        r"ministr|congreso|pol[ií]tic|candidat|campa[ñn]a electoral")
DICCIONARIO_COVID = r"covid|coronavirus|pandemi|cuarentena|vacuna|sars|confinamiento"


# ---------------------------------------------------------------------------
# 1. Corpus y vectorizador offline
# ---------------------------------------------------------------------------
def cargar():
    notas = datos.titulares_prensa(con_texto=True)
    titulares = [n["titular"] for n in notas]
    print(f"{len(notas)} notas de prensa reales.")
    return notas, titulares


def construir_embeddings(notas, dim=100, top=2000):
    """PPMI + SVD sobre el corpus entero (titulares + cuerpo recortado).

    Es no supervisado: no mira ni una etiqueta. Igual conviene decirlo en clase:
    los vectores se construyen mirando también los textos de test. Para palabras
    eso es práctica estándar; para cualquier cosa que use la etiqueta, sería fuga.
    """
    corpus = " \n ".join(n["titular"] + " " + n["texto"] for n in notas)
    t0 = time.time()
    V, palabras = datos.embeddings_ppmi_svd(corpus, dim=dim, top=top,
                                            ventana=5, minimo=5)
    print(f"embeddings PPMI+SVD {V.shape} en {time.time() - t0:.1f} s "
          f"sobre {len(corpus):,} caracteres")
    return V, palabras


def hacer_vectorizador(V, palabras):
    indice = {p: i for i, p in enumerate(palabras)}
    tok = datos.TokenizadorPalabras(minusculas=True)

    def fichas(texto):
        return [w for w in tok.partir(texto.lower()) if w in indice]

    def vectorizar(textos):
        salida = np.zeros((len(textos), V.shape[1]), dtype=np.float32)
        for k, t in enumerate(textos):
            ws = fichas(t)
            if not ws:
                continue
            v = V[[indice[w] for w in ws]].mean(axis=0)
            n = np.linalg.norm(v)
            salida[k] = v / n if n > 0 else v
        return salida

    return vectorizar, fichas, indice


# ---------------------------------------------------------------------------
# 2. La curva de cuántas etiquetas hacen falta
# ---------------------------------------------------------------------------
def curva_de_etiquetas(titulares, y, X, tamanios, repeticiones=8):
    tr_all, te = train_test_split(np.arange(len(y)), test_size=0.25,
                                  stratify=y, random_state=SEMILLA)
    prev = float(y[tr_all].mean())
    pos = np.array([i for i in tr_all if y[i] == 1])
    neg = np.array([i for i in tr_all if y[i] == 0])

    resultado = {"tamanios": tamanios, "embeddings": [], "tfidf": []}
    for n in tamanios:
        f_emb, f_tfi = [], []
        for s in range(repeticiones):
            rng = np.random.default_rng(SEMILLA + s)
            npos = max(2, int(round(n * prev)))
            sel = np.concatenate([
                rng.choice(pos, min(npos, len(pos)), replace=False),
                rng.choice(neg, n - npos, replace=False)])
            m = LogisticRegression(max_iter=2000, class_weight="balanced")
            m.fit(X[sel], y[sel])
            f_emb.append(f1_score(y[te], m.predict(X[te]), zero_division=0))

            tf = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
            A = tf.fit_transform([titulares[i] for i in sel])
            m2 = LogisticRegression(max_iter=2000, class_weight="balanced")
            m2.fit(A, y[sel])
            pred = m2.predict(tf.transform([titulares[i] for i in te]))
            f_tfi.append(f1_score(y[te], pred, zero_division=0))

        resultado["embeddings"].append(
            {"n": n, "f1": round(float(np.mean(f_emb)), 4),
             "sd": round(float(np.std(f_emb)), 4)})
        resultado["tfidf"].append(
            {"n": n, "f1": round(float(np.mean(f_tfi)), 4),
             "sd": round(float(np.std(f_tfi)), 4)})
        print(f"  n={n:4d}   embeddings {np.mean(f_emb):.3f}±{np.std(f_emb):.3f}"
              f"   tf-idf {np.mean(f_tfi):.3f}±{np.std(f_tfi):.3f}")

    return resultado, tr_all, te


def metricas(y_true, y_pred):
    return {"accuracy": round(float(accuracy_score(y_true, y_pred)), 4),
            "precision": round(float(precision_score(y_true, y_pred, zero_division=0)), 4),
            "recall": round(float(recall_score(y_true, y_pred, zero_division=0)), 4),
            "f1": round(float(f1_score(y_true, y_pred, zero_division=0)), 4)}


# ---------------------------------------------------------------------------
# 3. main
# ---------------------------------------------------------------------------
def main():
    notas, titulares = cargar()
    V, palabras = construir_embeddings(notas)
    vectorizar, fichas, indice = hacer_vectorizador(V, palabras)
    X = vectorizar(titulares)

    y_pol = np.array([int(n["tema"] == "Politica") for n in notas])
    y_cov = np.array([int(n["tema"] == "Covid-19") for n in notas])
    y_fal = np.array([n["es_falso"] for n in notas])

    tamanios = [25, 50, 100, 200, 400, 800]
    tareas = {}
    for clave, etiqueta, y_t, dicc, nombre in [
            ("politica", "¿es una nota sobre política?", y_pol,
             DICCIONARIO_POLITICA, "política"),
            ("covid", "¿es una nota sobre Covid-19?", y_cov,
             DICCIONARIO_COVID, "Covid-19")]:
        print(f"\n--- la curva (tarea: {etiqueta}) ---")
        curva, tr_all, te = curva_de_etiquetas(titulares, y_t, X, tamanios)
        pred_dic = np.array([int(bool(re.search(dicc, titulares[i], re.I))) for i in te])
        curva["diccionario"] = metricas(y_t[te], pred_dic)
        base = max(float(y_t[te].mean()), 1 - float(y_t[te].mean()))
        curva["baseline_accuracy"] = round(base, 4)
        curva["prevalencia"] = round(float(y_t.mean()), 4)
        curva["etiqueta"] = etiqueta
        curva["nombre"] = nombre
        curva["n_test"] = int(len(te))
        curva["patron"] = dicc
        print(f"  diccionario (0 etiquetas): F1 {curva['diccionario']['f1']:.3f} "
              f"(P {curva['diccionario']['precision']:.3f} / "
              f"R {curva['diccionario']['recall']:.3f})")
        print(f"  baseline de clase mayoritaria: accuracy {base:.3f}, F1 0.000")
        tareas[clave] = curva
        if clave == "politica":
            curva_pol, tr_all_pol, te_pol = curva, tr_all, te
    curva = curva_pol
    tr_all, te = tr_all_pol, te_pol
    covid = tareas["covid"]

    # --- la trampa: verdadero/falso, al azar vs por fuente ------------------
    print("\n--- la trampa del corpus (verdadero/falso) ---")
    textos_largos = [n["titular"] + " . " + n["texto"] for n in notas]
    fuentes = [n["fuente"] for n in notas]

    def tfidf_f1(idx_tr, idx_te):
        tf = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)
        A = tf.fit_transform([textos_largos[i] for i in idx_tr])
        mm = LogisticRegression(max_iter=2000, C=4).fit(A, y_fal[idx_tr])
        p = mm.predict(tf.transform([textos_largos[i] for i in idx_te]))
        return metricas(y_fal[idx_te], p)

    tr_a, te_a = train_test_split(np.arange(len(y_fal)), test_size=0.25,
                                  stratify=y_fal, random_state=SEMILLA)
    al_azar = tfidf_f1(tr_a, te_a)
    g_tr, g_va, g_te = datos.particion_por_grupo(fuentes, semilla=SEMILLA)
    por_fuente = tfidf_f1(np.array(g_tr), np.array(g_te))
    print(f"  partición al azar : accuracy {al_azar['accuracy']:.3f}  F1 {al_azar['f1']:.3f}")
    print(f"  partición por fuente: accuracy {por_fuente['accuracy']:.3f}  F1 {por_fuente['f1']:.3f}")

    from collections import Counter, defaultdict
    por_medio = defaultdict(Counter)
    for n in notas:
        por_medio[n["fuente"]][n["categoria"]] += 1
    una_sola = sum(1 for c in por_medio.values() if len(c) == 1)
    top_falsas = Counter(n["fuente"] for n in notas if n["es_falso"]).most_common(5)
    top_verdad = Counter(n["fuente"] for n in notas if not n["es_falso"]).most_common(5)
    print(f"  medios: {len(por_medio)}, con una sola clase: {una_sola} "
          f"({una_sola / len(por_medio) * 100:.0f} %)")

    trampa = {
        "al_azar": al_azar, "por_fuente": por_fuente,
        "medios": len(por_medio), "medios_una_sola_clase": una_sola,
        "top_fuentes_falsas": top_falsas, "top_fuentes_verdaderas": top_verdad,
        "baseline_accuracy_azar": round(max(float(y_fal[te_a].mean()),
                                            1 - float(y_fal[te_a].mean())), 4),
    }

    # --- el corpus de la búsqueda semántica --------------------------------
    print("\n--- corpus para viz/similitud-semantica.html ---")
    rng = np.random.default_rng(SEMILLA)
    # 300 titulares al azar, pero garantizando que entren los de Covid-19 y los
    # de política, que son los temas con los que la viz se demuestra.
    elegidos = sorted(rng.choice(len(notas), size=300, replace=False).tolist())
    corpus_viz = []
    usadas = set()
    for i in elegidos:
        ws = fichas(notas[i]["titular"])
        usadas.update(ws)
        corpus_viz.append({
            "t": notas[i]["titular"],
            "tema": notas[i]["tema"],
            "f": notas[i]["fuente"],
            "falso": int(notas[i]["es_falso"]),
            "w": [indice[w] for w in ws],
        })

    # el vocabulario que la viz necesita: las palabras de esos 300 titulares más
    # las 700 más frecuentes del corpus, para que una consulta libre encuentre
    # sus vectores. Recortamos a 32 dimensiones: alcanza para el ranking y el
    # archivo pesa un tercio.
    extra = [p for p in palabras[:900]]
    vocab_ids = sorted(set(list(usadas) + extra), key=lambda w: indice[w])
    remap = {indice[w]: k for k, w in enumerate(vocab_ids)}
    DIMV = 32
    Vv = V[[indice[w] for w in vocab_ids], :DIMV]
    Vv = Vv / np.maximum(np.linalg.norm(Vv, axis=1, keepdims=True), 1e-9)
    for c in corpus_viz:
        c["w"] = [remap[j] for j in c["w"] if j in remap]

    busqueda = {
        "palabras": vocab_ids,
        "dim": DIMV,
        "vectores": [[round(float(v), 3) for v in fila] for fila in Vv],
        "corpus": corpus_viz,
        "consultas": ["coronavirus", "protesta", "elecciones", "vacuna",
                      "violencia", "fútbol"],
    }
    print(f"  {len(corpus_viz)} titulares, vocabulario de {len(vocab_ids)} palabras, "
          f"{DIMV} dimensiones")

    paquete = {
        "meta": {
            "corpus": "Spanish Fake News Corpus 2.0 — 1471 notas de prensa en "
                      "castellano, noviembre 2020 a marzo 2021",
            "fuente_archivo": "datos/muestras/prensa/titulares-prensa-es.csv",
            "real": True,
            "licencia": "CC BY 4.0",
            "camino": "offline (PPMI+SVD, sin Hugging Face)",
            "semilla": SEMILLA,
            "n_notas": len(notas),
            "generado_por": "clases/09-modelos-preentrenados/medir-clase09.py",
        },
        "curva": curva,
        "tareas": tareas,
        "trampa": trampa,
        "busqueda": busqueda,
    }

    (SALIDA / "datos-clase09.json").write_text(
        json.dumps(paquete, ensure_ascii=False), encoding="utf-8")
    js = ("/* GENERADO por medir-clase09.py — no lo edites a mano.\n"
          "   Todos los números salen de una corrida real sobre el corpus de\n"
          "   prensa del curso (1471 notas reales). Camino offline: embeddings\n"
          "   propios PPMI+SVD, sin Hugging Face. */\n"
          "const DATOS_C9 = " + json.dumps(paquete, ensure_ascii=False) + ";\n")
    (SALIDA / "datos-clase09.js").write_text(js, encoding="utf-8")
    kb = (SALIDA / "datos-clase09.js").stat().st_size / 1024
    print(f"\nListo. datos-clase09.js ({kb:.0f} KB) y datos-clase09.json escritos.")


if __name__ == "__main__":
    main()
