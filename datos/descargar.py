#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
descargar.py — Descarga y cachea los datasets del curso.

FILOSOFIA DE ESTE ARCHIVO
=========================
Ninguna clase puede fallar porque se cayo un servidor. Por eso TODA funcion
de aca sigue el mismo patron, que es el patron obligatorio de los notebooks:

    1. Si ya esta en cache  -> lo usa.
    2. Si no, lo descarga   -> lo cachea.
    3. Si la descarga falla -> cae a datos/muestras/, que esta versionado en el repo.
    4. Nunca lanza excepcion por falta de red. Avisa por pantalla y sigue.

Uso desde un notebook de Colab:

    !git clone --depth 1 https://github.com/<org>/dlss.git
    import sys; sys.path.insert(0, 'dlss/datos')
    import descargar
    serie = descargar.serie_menciones()          # clases 1-4
    texto = descargar.corpus_discursos_texto()   # clases 6-8
    prensa = descargar.prensa_titulares()        # clases 9-10

Uso desde la linea de comandos (verifica todo y reporta):

    python3 descargar.py            # baja lo que pueda, reporta estado
    python3 descargar.py --solo-muestras   # ni intenta la red
    python3 descargar.py --verificar-urls  # solo prueba conectividad
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import unicodedata
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:          # para que `import preparar_corpus` ande
    sys.path.insert(0, AQUI)      # se importe desde donde se importe
CACHE = os.path.join(AQUI, "cache")
MUESTRAS = os.path.join(AQUI, "muestras")
TIMEOUT = 30

# ----------------------------------------------------------------------
# FUENTES.  Cada URL de aca fue probada con curl. El estado esta anotado
# en datos/README.md.  raw.githubusercontent.com es la unica puerta que
# quedo abierta en el contenedor de construccion, y tambien anda en Colab.
# ----------------------------------------------------------------------

RAW = "https://raw.githubusercontent.com"

FUENTES = {
    "discursos_apertura": {
        "base": f"{RAW}/lucariel/discursos_presidenciales/master/data/sesiones_ordinarias",
        "repo": "https://github.com/lucariel/discursos_presidenciales",
        "licencia": "sin licencia declarada en el repo; los textos fuente son "
                    "mensajes presidenciales al Congreso argentino (actos oficiales)",
    },
    "casarosada": {
        "url": f"{RAW}/jmdieguez/discursos/main/discursos_sample.csv",
        "repo": "https://github.com/jmdieguez/discursos",
        "licencia": "sin licencia declarada; textos scrapeados de casarosada.gob.ar",
    },
    "prensa_fakedes": {
        "urls": {
            "train": f"{RAW}/jpposadas/FakeNewsCorpusSpanish/master/train.xlsx",
            "dev": f"{RAW}/jpposadas/FakeNewsCorpusSpanish/master/development.xlsx",
            "test": f"{RAW}/jpposadas/FakeNewsCorpusSpanish/master/test.xlsx",
        },
        "repo": "https://github.com/jpposadas/FakeNewsCorpusSpanish",
        "licencia": "CC BY 4.0",
    },
    "fashion_mnist": {
        "base": f"{RAW}/zalandoresearch/fashion-mnist/master/data/fashion",
        "repo": "https://github.com/zalandoresearch/fashion-mnist",
        "licencia": "MIT",
        "archivos": ["train-images-idx3-ubyte.gz", "train-labels-idx1-ubyte.gz",
                     "t10k-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz"],
    },
}

# Los 108 discursos de apertura de sesiones. Manifiesto explicito para no
# depender de la API de GitHub (que suele estar bloqueada) ni de git.
DISCURSOS_ARCHIVOS = [
    "1854-justo_jose_de_urquiza", "1855-justo_jose_de_urquiza", "1856-justo_jose_de_urquiza",
    "1857-justo_jose_de_urquiza", "1858-justo_jose_de_urquiza", "1859-justo_jose_de_urquiza",
    "1860-santiago_derqui", "1861-santiago_derqui", "1863-bartolome_mitre",
    "1864-bartolome_mitre", "1865-bartolome_mitre", "1866-bartolome_mitre",
    "1867-bartolome_mitre", "1868-bartolome_mitre", "1869-domingo_f_sarmiento",
    "1870-domingo_f_sarmiento", "1873-domingo_f_sarmiento", "1874-domingo_f_sarmiento",
    "1875-nicolas_avellaneda", "1877-nicolas_avellaneda", "1878-nicolas_avellaneda",
    "1879-nicolas_avellaneda", "1880-nicolas_avellaneda", "1881-julio_A_Roca",
    "1882-julio_A_Roca", "1884-julio_A_Roca", "1885-julio_A_Roca", "1886-julio_A_Roca",
    "1887-miguel_juarez_celman", "1888-miguel_juarez_celman", "1889-miguel_juarez_celman",
    "1890-miguel_juarez_celman", "1891-carlos_pellegrini", "1895-jose_evaristo_uriburu",
    "1899-julio_a_roca", "1901-julio_a_roca", "1904-julio_a_roca",
    "1906-jose_figueroa_alcorta", "1913-roque_saenz_penia", "1915-roque_saenz_penia",
    "1916-victorino_dela_plaza", "1917-hipolito_yrigoyen", "1918-hipolito_yrigoyen",
    "1920-hipolito_yrigoyen", "1926-marcelo_torcuato_de_alvear", "1929-hipolito_yrigoyen",
    "1932-agustin_p_justo", "1933-agustin_p_justo", "1935-agustin_p_justo",
    "1936-agustin_p_justo", "1937-agustin_p_justo", "1939-roberto_ortiz", "1940-roberto_ortiz",
    "1941-roberto_ortiz", "1942-ramon_castillo", "1946-juan_peron", "1947-juan_peron",
    "1948-juan_peron", "1949-juan_peron", "1950-juan_peron", "1951-juan_peron",
    "1952-juan_peron", "1953-juan_peron", "1955-juan_peron", "1959-arturo_frondizi",
    "1960-arturo_frondizi", "1961-arturo_frondizi", "1964-arturo_illia", "1965-arturo_illia",
    "1966-arturo_illia", "1974-juan_domingo_peron", "1975-maria_estela_martinez_de_peron",
    "1984-raul_alfonsin", "1985-raul_alfonsin", "1986-raul_alfonsin", "1987-raul_alfonsin",
    "1988-raul_alfonsin", "1989-raul_alfonsin", "1990-carlos_menem", "1991-carlos_menem",
    "1992-carlos_menem", "1993-carlos_menem", "1994-carlos_menem", "1995-carlos_menem",
    "1996-carlos_menem", "1997-carlos_menem", "1998-carlos_menem", "1999-carlos_menem",
    "2000-fernando_de_la_rua", "2001-fernando_de_la_rua", "2002-eduardo_duhalde",
    "2003-eduardo_duhalde", "2004-nestor_kirchner", "2005-nestor_kirchner",
    "2006-nestor_kirchner", "2007-nestor_kirchner", "2008-cristina_fernandez_de_kirchner",
    "2009-cristina_fernandez_de_kirchner", "2010-cristina_fernandez_de_kirchner",
    "2011-cristina_fernandez_de_kirchner", "2012-cristina_fernandez_de_kirchner",
    "2013-cristina_fernandez_de_kirchner", "2014-cristina_fernandez_de_kirchner",
    "2015-cristina_fernandez_de_kirchner", "2016-mauricio_macri", "2017-mauricio_macri",
    "2018-mauricio_macri", "2019-mauricio_macri"
]

# ----------------------------------------------------------------------
# Plomeria
# ----------------------------------------------------------------------


def _log(msg):
    print(msg, file=sys.stderr if not sys.stdout.isatty() else sys.stdout, flush=True)


def _cache_path(*partes):
    p = os.path.join(CACHE, *partes)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def bajar(url, destino, timeout=TIMEOUT, silencioso=False):
    """Baja `url` a `destino` si no existe ya. Devuelve True/False, nunca explota."""
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "dlss-curso/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            datos = r.read()
        if not datos:
            raise ValueError("respuesta vacia")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "wb") as fh:
            fh.write(datos)
        return True
    except Exception as e:  # red, DNS, proxy, 404, lo que sea
        if not silencioso:
            _log(f"  [x] no se pudo bajar {url}\n      motivo: {type(e).__name__}: {e}")
        return False


def _aviso_fallback(que, ruta):
    _log(f"  [!] {que}: usando la MUESTRA versionada del repo ({os.path.relpath(ruta, AQUI)}).")
    _log(f"      Es mas chica que el dataset completo. Todo el curso funciona igual;")
    _log(f"      lo unico que cambia son los numeros exactos de los ejemplos.")


# ----------------------------------------------------------------------
# 1) DISCURSOS DE APERTURA DE SESIONES  (clases 1-4, 6-8)
# ----------------------------------------------------------------------

def discursos_apertura(anios=None, forzar_muestra=False):
    """Discursos presidenciales de apertura de sesiones ordinarias (Argentina).

    Devuelve dict {anio: {"presidente": str, "texto": str}}.
    Si no hay red, cae a los discursos versionados en muestras/.
    """
    quiero = set(anios) if anios else None
    salida, bajados = {}, 0

    if not forzar_muestra:
        for stem in DISCURSOS_ARCHIVOS:
            anio = int(stem[:4])
            if quiero and anio not in quiero:
                continue
            destino = _cache_path("discursos-apertura", stem + ".txt")
            url = f"{FUENTES['discursos_apertura']['base']}/{stem}.txt"
            if bajar(url, destino, silencioso=(bajados == 0 and False)):
                bajados += 1
                salida[anio] = {
                    "presidente": stem[5:].replace("_", " "),
                    "texto": open(destino, encoding="utf-8", errors="replace").read(),
                }
        if bajados:
            _log(f"  [ok] discursos de apertura: {bajados} discursos "
                 f"({'cache' if bajados else ''})")
            return salida

    dirm = os.path.join(MUESTRAS, "discursos-apertura")
    _aviso_fallback("discursos de apertura", dirm)
    for f in sorted(os.listdir(dirm)):
        if not f.endswith(".txt") or f.startswith("corpus-"):
            continue
        anio = int(f[:4])
        if quiero and anio not in quiero:
            continue
        salida[anio] = {
            "presidente": f[5:-4].replace("_", " "),
            "texto": open(os.path.join(dirm, f), encoding="utf-8", errors="replace").read(),
        }
    return salida


def corpus_discursos_texto(min_anio=1984, max_anio=2019, forzar_muestra=False):
    """Un unico string con los discursos concatenados. Es el corpus del mini-GPT.

    Por defecto arranca en 1984 (la era democratica) por tres razones:
      - es castellano contemporaneo, no decimononico (que es otra lengua);
      - es EL MISMO recorte de la serie de las clases 1-4, asi que el corpus
        del mini-GPT y la serie hablan del mismo periodo;
      - da ~2,2 MB, de sobra para un mini-GPT y poco para esperar de mas.
    Se excluye 2006, que en el corpus fuente es copia byte a byte de 2005.
    """
    d = discursos_apertura(forzar_muestra=forzar_muestra)
    if not d:
        return ""
    partes = []
    for anio in sorted(d):
        if anio == 2006:            # duplicado exacto de 2005 en el corpus fuente
            continue
        if min_anio <= anio <= max_anio:
            partes.append(f"### {anio} — {d[anio]['presidente'].title()}\n\n{d[anio]['texto'].strip()}\n")
    txt = "\n".join(partes)
    if len(txt) < 400_000:
        muestra = os.path.join(MUESTRAS, "discursos-apertura", "corpus-mini-gpt.txt")
        if os.path.exists(muestra):
            _aviso_fallback("corpus para el mini-GPT", muestra)
            txt = open(muestra, encoding="utf-8").read()
    return txt


# ----------------------------------------------------------------------
# 2) SERIE DE MENCIONES POR TEMA Y POR AÑO  (clases 1-4)
# ----------------------------------------------------------------------

def serie_menciones(forzar_muestra=False):
    """La serie que atraviesa las clases 1 a 4.

    Filas: anio, presidente, palabras, y el % de palabras dedicadas a cada tema.
    Se recalcula desde los discursos si hay red; si no, lee el CSV versionado.
    """
    csv_muestra = os.path.join(MUESTRAS, "series", "menciones-por-tema-apertura.csv")

    if not forzar_muestra:
        try:
            from preparar_corpus import serie_de_menciones  # import perezoso
            d = discursos_apertura()
            if len(d) > 60:
                filas = serie_de_menciones(d)
                _log(f"  [ok] serie recalculada desde {len(d)} discursos: {len(filas)} filas")
                return filas
        except Exception as e:
            _log(f"  [x] no se pudo recalcular la serie ({type(e).__name__}: {e})")

    _aviso_fallback("serie de menciones", csv_muestra)
    with open(csv_muestra, encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    for f in filas:
        f["anio"] = int(f["anio"])
        f["palabras"] = int(f["palabras"])
        for k in f:
            if k not in ("anio", "presidente", "palabras"):
                f[k] = float(f[k])
    return filas


# ----------------------------------------------------------------------
# 3) PRENSA EN CASTELLANO  (clases 4, 9, 10)
# ----------------------------------------------------------------------

def prensa_titulares(forzar_muestra=False):
    """Titulares y notas de prensa en castellano, con etiquetas.

    Fuente real: Spanish Fake News Corpus 2.0 (CC BY 4.0). Devuelve una lista
    de dicts con: id, categoria (Fake/True), tema, fuente, titular, texto.
    """
    if not forzar_muestra:
        ok = {}
        for k, url in FUENTES["prensa_fakedes"]["urls"].items():
            destino = _cache_path("prensa", f"{k}.xlsx")
            if bajar(url, destino):
                ok[k] = destino
        if ok:
            try:
                import pandas as pd
                dfs = []
                for k, p in ok.items():
                    df = pd.read_excel(p)
                    df.columns = [c.strip().lower() for c in df.columns]
                    df = df.rename(columns={"topics": "topic", "id": "id"})
                    df["particion_original"] = k
                    dfs.append(df)
                d = pd.concat(dfs, ignore_index=True)
                _log(f"  [ok] prensa (FakeDeS): {len(d)} notas desde {len(ok)} archivos")
                return _normalizar_prensa(d.to_dict("records"))
            except ImportError:
                _log("  [x] falta pandas/openpyxl para leer los .xlsx; uso la muestra")
            except Exception as e:
                _log(f"  [x] error leyendo los .xlsx ({type(e).__name__}: {e}); uso la muestra")

    csvm = os.path.join(MUESTRAS, "prensa", "titulares-prensa-es.csv")
    _aviso_fallback("prensa", csvm)
    with open(csvm, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# El corpus fuente viene con las etiquetas mezcladas entre archivos:
# train/dev usan "Fake"/"True" y test usa "False"/"True". Ademas los temas
# estan en ingles en train/dev y en castellano en test. Si concatenas los tres
# archivos sin mirar, te quedan 3 clases donde hay 2 y 16 temas donde hay 9.
# Lo unificamos aca, y guardamos el valor original al lado para que la
# correccion sea auditable y no una desaparicion silenciosa.
_MAPA_CATEGORIA = {"fake": "Fake", "false": "Fake", "true": "True"}
_MAPA_TEMA = {
    "politics": "Politica", "politica": "Politica",
    "society": "Sociedad", "sociedad": "Sociedad",
    "science": "Ciencia", "ciencia": "Ciencia",
    "sport": "Deporte", "deporte": "Deporte",
    "health": "Salud", "salud": "Salud",
    "economy": "Economia", "economia": "Economia",
    "security": "Seguridad", "seguridad": "Seguridad",
    "education": "Educacion", "educacion": "Educacion",
    "entertainment": "Espectaculos", "espectaculos": "Espectaculos",
    "covid-19": "Covid-19", "covid19": "Covid-19",
    "environment": "Ambiental", "ambiental": "Ambiental",
    "international": "Internacional", "internacional": "Internacional",
}


def _normalizar_prensa(regs):
    out = []
    for r in regs:
        cat_cruda = str(r.get("category", "")).strip()
        tema_crudo = str(r.get("topic", "")).strip()
        # el mismo tema viene con y sin tilde ("Politica" / "Política")
        clave_tema = "".join(
            c for c in unicodedata.normalize("NFD", tema_crudo.lower())
            if unicodedata.category(c) != "Mn")
        out.append({
            "id": str(r.get("id", "")),
            "categoria": _MAPA_CATEGORIA.get(cat_cruda.lower(), cat_cruda),
            "categoria_original": cat_cruda,
            "tema": _MAPA_TEMA.get(clave_tema, tema_crudo),
            "tema_original": tema_crudo,
            "fuente": str(r.get("source", "")).strip(),
            "titular": str(r.get("headline", "")).strip(),
            "texto": str(r.get("text", "")).strip(),
            "particion_original": r.get("particion_original", ""),
        })
    return out


# ----------------------------------------------------------------------
# 4) DISCURSOS RECIENTES DE CASA ROSADA  (clase 6 "dos epocas", clase 10)
# ----------------------------------------------------------------------

def discursos_casarosada(forzar_muestra=False):
    """1311 discursos presidenciales 2015-2024 con orador y fecha.

    OJO: solo 3 oradores, y muy desbalanceados. Ver las trampas en README.md.
    """
    if not forzar_muestra:
        destino = _cache_path("casarosada", "discursos.csv")
        if bajar(FUENTES["casarosada"]["url"], destino):
            with open(destino, encoding="utf-8") as fh:
                filas = list(csv.DictReader(fh))
            _log(f"  [ok] casarosada: {len(filas)} discursos 2015-2024")
            return filas

    csvm = os.path.join(MUESTRAS, "casarosada", "discursos-muestra.csv")
    _aviso_fallback("discursos de Casa Rosada", csvm)
    with open(csvm, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ----------------------------------------------------------------------
# 5) AGUASCLARAS — corpus sintetico  (clase 8; fallback general)
# ----------------------------------------------------------------------

def aguasclaras(regenerar=False):
    """Corpus SINTETICO. Devuelve dict con 'debates' (str), 'verdad' (dict),
    'prensa' (list of dicts).

    No usa red nunca: si falta, lo genera. Ver generar_aguasclaras.py para
    por que existe y que se pierde por ser sintetico.
    """
    d = os.path.join(MUESTRAS, "aguasclaras")
    faltan = not all(os.path.exists(os.path.join(d, f))
                     for f in ("debates.txt", "verdad.json", "prensa.csv"))
    if regenerar or faltan:
        _log("  [..] generando Aguasclaras (sintetico, semilla fija)...")
        import subprocess
        subprocess.run([sys.executable, os.path.join(AQUI, "generar_aguasclaras.py"),
                        "--salida", d], check=True)
    with open(os.path.join(d, "prensa.csv"), encoding="utf-8") as fh:
        prensa = list(csv.DictReader(fh))
    return {
        "debates": open(os.path.join(d, "debates.txt"), encoding="utf-8").read(),
        "verdad": json.load(open(os.path.join(d, "verdad.json"), encoding="utf-8")),
        "prensa": prensa,
        "ADVERTENCIA": "CORPUS SINTETICO. Pais, personas, partidos y leyes ficticios.",
    }


# ----------------------------------------------------------------------
# 6) FASHION-MNIST  (clase 5, sandbox tecnico explicitamente rotulado)
# ----------------------------------------------------------------------

def fashion_mnist(split="train"):
    """Devuelve (imagenes uint8 [N,28,28], etiquetas uint8 [N]) o None sin red.

    Es un SANDBOX TECNICO, no un dato de ciencias sociales. Rotularlo asi en
    la slide: sirve para ver como funciona una convolucion, y despues se
    vuelve al dominio.
    """
    import gzip
    import numpy as np
    pre = "train" if split == "train" else "t10k"
    base = FUENTES["fashion_mnist"]["base"]
    px = _cache_path("fashion-mnist", f"{pre}-images-idx3-ubyte.gz")
    py = _cache_path("fashion-mnist", f"{pre}-labels-idx1-ubyte.gz")
    if not (bajar(f"{base}/{pre}-images-idx3-ubyte.gz", px)
            and bajar(f"{base}/{pre}-labels-idx1-ubyte.gz", py)):
        _log("  [x] FashionMNIST no disponible. En Colab suele andar; "
             "si no, la clase 5 usa el corpus visual sintetico.")
        return None
    with gzip.open(px, "rb") as fh:
        X = np.frombuffer(fh.read(), np.uint8, offset=16).reshape(-1, 28, 28)
    with gzip.open(py, "rb") as fh:
        y = np.frombuffer(fh.read(), np.uint8, offset=8)
    _log(f"  [ok] FashionMNIST {split}: {X.shape[0]} imagenes")
    return X, y


ETIQUETAS_FASHION = ["remera/top", "pantalon", "pullover", "vestido", "abrigo",
                     "sandalia", "camisa", "zapatilla", "cartera", "botineta"]


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

URLS_A_VERIFICAR = [
    ("raw.githubusercontent.com (todos los corpus de texto)",
     f"{RAW}/lucariel/discursos_presidenciales/master/README.md"),
    ("FakeNewsCorpusSpanish (prensa, CC BY 4.0)",
     FUENTES["prensa_fakedes"]["urls"]["train"]),
    ("Casa Rosada (discursos 2015-2024)", FUENTES["casarosada"]["url"]),
    ("FashionMNIST (sandbox clase 5)",
     f"{FUENTES['fashion_mnist']['base']}/t10k-labels-idx1-ubyte.gz"),
]


def verificar_urls():
    print("Verificando conectividad de las fuentes...\n")
    for nombre, url in URLS_A_VERIFICAR:
        try:
            req = urllib.request.Request(url, method="GET",
                                         headers={"User-Agent": "dlss-curso/1.0",
                                                  "Range": "bytes=0-64"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                print(f"  VERIFICADA-OK  [{r.status}]  {nombre}")
        except Exception as e:
            print(f"  FALLA          [{type(e).__name__}]  {nombre}")
            print(f"                 {url}")
    print("\nSi todo falla, el curso igual corre entero con datos/muestras/.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--solo-muestras", action="store_true",
                    help="no toca la red, usa unicamente datos/muestras/")
    ap.add_argument("--verificar-urls", action="store_true")
    args = ap.parse_args()

    if args.verificar_urls:
        verificar_urls()
        return

    fm = args.solo_muestras
    print("=" * 68)
    print("DATASETS DEL CURSO — descarga y verificacion")
    print("=" * 68)

    print("\n[1/6] Discursos de apertura de sesiones (clases 1-4, 6-8)")
    d = discursos_apertura(forzar_muestra=fm)
    print(f"      -> {len(d)} discursos, años {min(d)}-{max(d)}"
          if d else "      -> VACIO")

    print("\n[2/6] Serie de menciones por tema y año (clases 1-4)")
    s = serie_menciones(forzar_muestra=fm)
    print(f"      -> {len(s)} filas, años {s[0]['anio']}-{s[-1]['anio']}")

    print("\n[3/6] Corpus de texto para el mini-GPT (clases 6-8)")
    t = corpus_discursos_texto(forzar_muestra=fm)
    print(f"      -> {len(t):,} caracteres ({len(t.encode('utf-8'))/1e6:.2f} MB)")

    print("\n[4/6] Prensa en castellano (clases 4, 9, 10)")
    p = prensa_titulares(forzar_muestra=fm)
    print(f"      -> {len(p)} notas")

    print("\n[5/6] Aguasclaras (SINTETICO — clase 8)")
    a = aguasclaras()
    print(f"      -> {len(a['debates']):,} caracteres de debates, "
          f"{len(a['verdad']['diputados'])} diputados en el padron, "
          f"{len(a['prensa'])} titulares")

    print("\n[6/6] FashionMNIST (sandbox clase 5)")
    if fm:
        print("      -> salteado (--solo-muestras)")
    else:
        r = fashion_mnist("t10k")
        print(f"      -> {r[0].shape}" if r else "      -> no disponible sin red")

    print("\n" + "=" * 68)
    print("Listo. Si algo cayo a muestra, el curso corre igual.")
    print("=" * 68)


if __name__ == "__main__":
    main()
