#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preparar_corpus.py — Limpieza, normalizacion, medicion y particion.

Todo lo de aca es deliberadamente simple y leible. No hay magia: cada
funcion es algo que un cientista social podria haber hecho a mano, hecho
una sola vez y bien.

Dos cosas que este archivo enseña ademas de hacer:

1. NORMALIZAR ES DECIDIR. Cada `.lower()` y cada acento que sacamos es una
   decision de medicion, no un detalle tecnico. Estan marcadas con [DECISION].

2. PARTIR MAL ES HACER TRAMPA. `particion_*` implementa las tres estrategias
   de la viz de la clase 4 y devuelve, ademas de la particion, el diagnostico
   de fuga (leakage) que esa estrategia produce.

Verificacion:
    python3 preparar_corpus.py            # corre los doctests + un informe real
    python3 -m doctest preparar_corpus.py -v
"""
from __future__ import annotations

import csv
import os
import random
import re
import unicodedata
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# NORMALIZACION
# ----------------------------------------------------------------------

# Basura tipica de estos corpus: numeracion de pagina, marcas de OCR,
# encabezados repetidos del Diario de Sesiones.
_RUIDO = [
    re.compile(r"^\s*-?\s*\d{1,4}\s*-?\s*$", re.M),          # numeros de pagina sueltos
    re.compile(r"^\s*P[áa]g(ina)?\.?\s*\d+\s*$", re.M | re.I),
    re.compile(r"\f"),                                        # saltos de pagina
    re.compile(r"\[\s*Aplausos?\.?\s*\]", re.I),
    re.compile(r"\(\s*Aplausos?\.?\s*\)", re.I),
]


def limpiar(texto: str) -> str:
    """Saca ruido de digitalizacion y normaliza espacios en blanco.

    NO toca mayusculas ni acentos: eso es medicion, no limpieza, y va aparte.

    >>> limpiar("Hola   mundo.\\n\\n\\n- 12 -\\nSegunda parte. (Aplausos)")
    'Hola mundo.\\n\\nSegunda parte.'
    >>> limpiar("uno\\f\\ndos")
    'uno\\ndos'
    """
    t = texto.replace("\r\n", "\n").replace("\r", "\n")
    for rx in _RUIDO:
        t = rx.sub("", t)
    t = re.sub(r"[ \t ]+", " ", t)          # espacios horizontales -> uno
    t = re.sub(r" *\n *", "\n", t)                # sin espacios al borde de linea
    t = re.sub(r"\n{3,}", "\n\n", t)              # como mucho un renglon en blanco
    return t.strip()


def sin_acentos(texto: str) -> str:
    """Saca tildes y diereses. [DECISION] Colapsa 'publico' y 'público'.

    Es lo que queres para CONTAR palabras en un corpus con OCR desparejo
    (donde los acentos se pierden a veces). Es lo que NO queres si el acento
    distingue significado ('publico' verbo vs 'público' sustantivo).

    >>> sin_acentos("Educación pública, mañana")
    'Educacion publica, manana'
    """
    d = unicodedata.normalize("NFD", texto)
    return unicodedata.normalize("NFC", "".join(c for c in d
                                                if unicodedata.category(c) != "Mn"))


def normalizar(texto: str, minusculas=True, quitar_acentos=True) -> str:
    """Normalizacion completa para conteo de palabras.

    >>> normalizar("La INFLACIÓN y la Inflación")
    'la inflacion y la inflacion'
    """
    t = limpiar(texto)
    if minusculas:
        t = t.lower()          # [DECISION] 'Estado' y 'estado' pasan a ser lo mismo
    if quitar_acentos:
        t = sin_acentos(t)     # [DECISION] ver arriba
    return t


_PALABRA = re.compile(r"[a-zñ]+", re.I)


def tokenizar(texto: str) -> list[str]:
    """Parte en palabras. Tira numeros y puntuacion.

    [DECISION] Tirar los numeros es razonable para medir TEMAS y desastroso
    para medir, por ejemplo, si un discurso cita cifras. Depende de la pregunta.

    >>> tokenizar("El artículo 5 dice: no.")
    ['el', 'articulo', 'dice', 'no']
    """
    return _PALABRA.findall(normalizar(texto))


# ----------------------------------------------------------------------
# MEDICION: de texto a numero
# ----------------------------------------------------------------------

# El diccionario tematico. ESTO ES EL INSTRUMENTO DE MEDICION del curso,
# y es donde vive casi toda la validez de constructo de las clases 1 a 4.
# Cambiar una palabra de aca cambia la serie. Por eso esta versionado, a la
# vista, y se discute en clase (clase 10, caso "el atajo lexico").
LEXICO = {
    "seguridad": ["seguridad", "inseguridad", "delito", "delitos", "delincuencia",
                  "delincuente", "delincuentes", "policia", "policial", "policiales",
                  "narcotrafico", "robo", "robos", "homicidio", "homicidios", "crimen",
                  "crimenes", "carcel", "carceles", "penitenciario", "penitenciaria",
                  "gendarmeria", "prefectura", "criminalidad"],
    "inflacion": ["inflacion", "inflacionario", "inflacionaria", "inflacionarias",
                  "precios", "devaluacion", "carestia", "hiperinflacion",
                  "estabilizacion", "indexacion"],
    "educacion": ["educacion", "educativo", "educativa", "educativas", "escuela",
                  "escuelas", "docente", "docentes", "universidad", "universidades",
                  "alumno", "alumnos", "alumnas", "maestro", "maestros", "maestras",
                  "analfabetismo", "alfabetizacion"],
    "trabajo": ["trabajo", "trabajadores", "trabajadoras", "empleo", "desempleo",
                "desocupacion", "salario", "salarios", "sindicato", "sindicatos",
                "sindical", "paritaria", "paritarias", "jubilacion", "jubilaciones",
                "jubilados"],
    "salud": ["salud", "hospital", "hospitales", "sanitario", "sanitaria", "medico",
              "medicos", "medicamentos", "enfermedad", "enfermedades", "vacuna",
              "vacunas", "epidemia", "pandemia"],
}


def porcentaje_tematico(texto: str, palabras_tema: list[str]) -> float:
    """% de palabras del texto que pertenecen al lexico del tema.

    Se normaliza por el largo del discurso PORQUE LOS DISCURSOS MIDEN DISTINTO:
    en este corpus van de 2.800 a 25.000 palabras. Contar menciones crudas
    mediria elocuencia, no agenda.

    >>> round(porcentaje_tematico("delito y delito y otra cosa", ["delito"]), 2)
    33.33
    >>> porcentaje_tematico("", ["delito"])
    0.0
    """
    toks = tokenizar(texto)
    if not toks:
        return 0.0
    tema = set(palabras_tema)
    return 100.0 * sum(1 for t in toks if t in tema) / len(toks)


def serie_de_menciones(discursos: dict, lexico: dict | None = None,
                       min_palabras: int = 200) -> list[dict]:
    """De {anio: {presidente, texto}} a la tabla que usan las clases 1 a 4.

    `min_palabras` descarta discursos truncos: en este corpus hay archivos que
    quedaron a medio digitalizar y meterlos ensucia la serie sin avisar.

    >>> d = {1990: {"presidente": "x", "texto": "delito delito paz"}}
    >>> f = serie_de_menciones(d, {"seguridad": ["delito"]}, min_palabras=0)
    >>> f[0]["anio"], f[0]["palabras"], round(f[0]["seguridad"], 2)
    (1990, 3, 66.67)
    >>> serie_de_menciones(d, {"seguridad": ["delito"]})   # 3 palabras < 200
    []
    """
    lex = lexico or LEXICO
    filas = []
    for anio in sorted(discursos):
        texto = discursos[anio]["texto"]
        toks = tokenizar(texto)
        if len(toks) < min_palabras:          # descarta fragmentos truncos
            continue
        fila = {"anio": anio,
                "presidente": discursos[anio]["presidente"],
                "palabras": len(toks)}
        for tema, ws in lex.items():
            fila[tema] = round(porcentaje_tematico(texto, ws), 4)
        filas.append(fila)
    # columnas suavizadas, para que coincidan con el CSV versionado.
    # La ventana cuenta AÑOS, no filas: la serie tiene huecos (1976-1983,
    # por ejemplo) y promediar por filas mezclaba 1984 con 1975.
    anios = [f["anio"] for f in filas]
    for tema in lex:
        suave = media_movil([f[tema] for f in filas], 3, anios=anios)
        for f, v in zip(filas, suave):
            f[tema + "_suave"] = round(v, 4)
    return filas



def media_movil(valores: list[float], ventana: int = 3,
                anios: list[int] | None = None) -> list[float]:
    """Media movil centrada. Suaviza la serie.

    Si pasas `anios`, la ventana cuenta AÑOS y no posiciones: cada año
    promedia solo con los años que estan a `ventana // 2` o menos. Hace falta
    cuando la serie tiene huecos: sin `anios`, el 1984 de la serie completa
    se promediaba con 1975, que es la fila anterior pero nueve años antes.
    En los bordes y al lado de un hueco se promedia con los vecinos que hay.

    [DECISION] Suavizar NO es cosmetica: cambia la pregunta. La serie cruda
    responde "cuanto hablo de esto ESE año"; la suavizada responde "en que
    parte del periodo estaba el tema en agenda". Las dos son legitimas y hay
    que decir cual usaste. La clase 2 usa la suavizada para que la forma se
    vea; la clase 4 usa la cruda, porque el ruido es justamente el punto.

    >>> media_movil([1, 2, 3, 4, 5], 3)
    [1.5, 2.0, 3.0, 4.0, 4.5]
    >>> media_movil([1, 2, 3], 1)
    [1.0, 2.0, 3.0]
    >>> media_movil([0.0, 2.0, 4.0], 3, anios=[1975, 1984, 1985])
    [0.0, 3.0, 3.0]
    """
    n, r = len(valores), []
    m = ventana // 2
    for i in range(n):
        if anios is None:
            lo, hi = max(0, i - m), min(n, i + m + 1)
            tramo = valores[lo:hi]
        else:
            tramo = [v for a, v in zip(anios, valores) if abs(a - anios[i]) <= m]
        r.append(round(sum(tramo) / len(tramo), 6))
    return r


def vocabulario(texto: str, minimo=1) -> Counter:
    """Frecuencias de palabra.

    >>> v = vocabulario("la casa la calle")
    >>> v["la"], len(v)
    (2, 3)
    """
    c = Counter(tokenizar(texto))
    return Counter({k: v for k, v in c.items() if v >= minimo})


# ----------------------------------------------------------------------
# PARTICION.  La clase 4 vive aca.
# ----------------------------------------------------------------------

def particion_aleatoria(n: int, p_train=0.7, p_val=0.15, semilla=1983):
    """Al azar. La estrategia por defecto y la que mas fugas causa.

    >>> tr, va, te = particion_aleatoria(100)
    >>> len(tr), len(va), len(te)
    (70, 15, 15)
    >>> particion_aleatoria(10) == particion_aleatoria(10)   # semilla fija
    True
    """
    idx = list(range(n))
    random.Random(semilla).shuffle(idx)
    a, b = int(n * p_train), int(n * (p_train + p_val))
    return idx[:a], idx[a:b], idx[b:]


def particion_temporal(anios: list[int], corte_val: int, corte_test: int):
    """Por tiempo: entreno con el pasado, valido y pruebo con el futuro.

    Es la unica honesta si tu pregunta es "¿sirve para lo que viene?".

    >>> a = [1990, 1995, 2000, 2005, 2010, 2015]
    >>> particion_temporal(a, 2005, 2012)
    ([0, 1, 2], [3, 4], [5])
    """
    tr = [i for i, y in enumerate(anios) if y < corte_val]
    va = [i for i, y in enumerate(anios) if corte_val <= y < corte_test]
    te = [i for i, y in enumerate(anios) if y >= corte_test]
    return tr, va, te


def particion_por_grupo(grupos: list, p_train=0.7, p_val=0.15, semilla=1983):
    """Por grupo: ningun grupo (persona, medio, provincia) cae en dos lados.

    La que necesitás con datos de panel, con varios discursos por presidente,
    o con varias notas por diario.

    >>> g = ["a","a","b","b","c","c","d","d"]
    >>> tr, va, te = particion_por_grupo(g, 0.5, 0.25)
    >>> set(g[i] for i in tr) & set(g[i] for i in te)
    set()
    """
    unicos = sorted(set(grupos), key=str)
    random.Random(semilla).shuffle(unicos)
    a, b = int(len(unicos) * p_train), int(len(unicos) * (p_train + p_val))
    s_tr, s_va = set(unicos[:a]), set(unicos[a:b])
    tr, va, te = [], [], []
    for i, g in enumerate(grupos):
        (tr if g in s_tr else va if g in s_va else te).append(i)
    return tr, va, te


def diagnostico_de_fuga(indices_train, indices_test, grupos=None, textos=None):
    """Cuenta las fugas concretas de una particion. Devuelve un dict legible.

    Dos fugas que aparecen de verdad en los corpus de este curso:
      - MISMO GRUPO en train y test (mismo presidente, mismo diario).
      - TEXTO DUPLICADO exacto entre train y test (pasa: ver el caso 2005/2006
        de los discursos de apertura, documentado en README.md).

    >>> g = ["a","a","b"]
    >>> d = diagnostico_de_fuga([0,1],[2], grupos=g)
    >>> d["grupos_compartidos"]
    0
    >>> d = diagnostico_de_fuga([0],[1], grupos=g)
    >>> d["grupos_compartidos"]
    1
    """
    out = {"n_train": len(indices_train), "n_test": len(indices_test),
           "grupos_compartidos": 0, "duplicados_exactos": 0, "detalle": []}
    if grupos is not None:
        gt = {grupos[i] for i in indices_train}
        ge = {grupos[i] for i in indices_test}
        comp = sorted(gt & ge, key=str)
        out["grupos_compartidos"] = len(comp)
        for g in comp[:10]:
            out["detalle"].append(f"grupo '{g}' aparece en train y en test")
    if textos is not None:
        ht = {hash(textos[i]) for i in indices_train}
        dup = [i for i in indices_test if hash(textos[i]) in ht]
        out["duplicados_exactos"] = len(dup)
        for i in dup[:10]:
            out["detalle"].append(f"el caso #{i} de test es identico a uno de train")
    return out


def guardar_csv(filas: list[dict], ruta: str) -> str:
    """Escribe una lista de dicts a CSV. Devuelve la ruta."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    return ruta


# ----------------------------------------------------------------------
# __main__: doctests + un informe sobre los datos DE VERDAD
# ----------------------------------------------------------------------

def _informe():
    import descargar

    print("\n" + "=" * 68)
    print("INFORME SOBRE LOS DATOS REALES")
    print("=" * 68)

    d = descargar.discursos_apertura()
    if not d:
        print("sin discursos; nada que informar")
        return

    print(f"\nDiscursos disponibles: {len(d)}  ({min(d)}-{max(d)})")

    filas = serie_de_menciones(d)
    dem = [f for f in filas if f["anio"] >= 1984]
    print(f"Serie construida: {len(filas)} filas ({len(dem)} en democracia post-1983)")

    largos = [f["palabras"] for f in dem]
    print(f"\nLargo de los discursos (post-1983): min {min(largos):,} / "
          f"mediana {sorted(largos)[len(largos)//2]:,} / max {max(largos):,} palabras")
    print("  -> por eso la serie es un PORCENTAJE y no un conteo crudo.")

    print("\n%% de palabras por tema, primeras y ultimas filas:")
    cab = ["anio", "palabras"] + list(LEXICO)
    print("  " + "".join(c.rjust(11) for c in cab))
    for f in dem[:3] + [None] + dem[-3:]:
        if f is None:
            print("  " + "...".rjust(11))
            continue
        print("  " + "".join(str(f[c] if c in ("anio", "palabras") else f"{f[c]:.3f}").rjust(11)
                             for c in cab))

    # duplicados exactos: la trampa documentada del corpus
    print("\nBusqueda de discursos duplicados exactos:")
    vistos, dups = {}, []
    for anio in sorted(d):
        h = hash(limpiar(d[anio]["texto"]))
        if h in vistos:
            dups.append((vistos[h], anio))
        vistos[h] = anio
    if dups:
        for a, b in dups:
            print(f"  [!] {a} y {b} son el MISMO texto, palabra por palabra.")
        print("      Es un error del corpus fuente, no del codigo. Documentado en README.md.")
    else:
        print("  sin duplicados")

    # las tres particiones, con su diagnostico
    print("\nTres estrategias de particion sobre los mismos 36 casos:")
    anios = [f["anio"] for f in dem]
    pres = [f["presidente"] for f in dem]
    textos = [d[f["anio"]]["texto"] for f in dem]

    tr, va, te = particion_aleatoria(len(dem))
    dg = diagnostico_de_fuga(tr, te, grupos=pres, textos=textos)
    print(f"  al azar     : train {len(tr)} / val {len(va)} / test {len(te)}"
          f"  -> {dg['grupos_compartidos']} presidentes compartidos, "
          f"{dg['duplicados_exactos']} duplicados")

    tr, va, te = particion_temporal(anios, 2010, 2016)
    dg = diagnostico_de_fuga(tr, te, grupos=pres, textos=textos)
    print(f"  por tiempo  : train {len(tr)} / val {len(va)} / test {len(te)}"
          f"  -> {dg['grupos_compartidos']} presidentes compartidos, "
          f"{dg['duplicados_exactos']} duplicados")

    tr, va, te = particion_por_grupo(pres)
    dg = diagnostico_de_fuga(tr, te, grupos=pres, textos=textos)
    print(f"  por grupo   : train {len(tr)} / val {len(va)} / test {len(te)}"
          f"  -> {dg['grupos_compartidos']} presidentes compartidos, "
          f"{dg['duplicados_exactos']} duplicados")
    print("\n  Leelo despacio: partir AL AZAR mete al mismo presidente de los dos")
    print("  lados. El modelo no aprende 'como habla un presidente', aprende")
    print("  'como habla ESTE presidente', y despues no replica. Clase 4.")

    print("\n" + "=" * 68)


if __name__ == "__main__":
    import doctest
    import sys
    sys.path.insert(0, AQUI)
    r = doctest.testmod(verbose=False)
    print(f"doctests: {r.attempted - r.failed}/{r.attempted} pasaron")
    if r.failed:
        raise SystemExit(1)
    _informe()
