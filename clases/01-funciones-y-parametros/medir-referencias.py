#!/usr/bin/env python3
"""
Los números de referencia de la clase 1, MEDIDOS.

En este curso está prohibido escribir en una visualización una frase del tipo
«lo mejor que se consigue ronda 0,015» sin haberlo medido. Este script es el
que lo mide. Cada número que sale por acá está copiado, con su nombre, adentro
de una viz o de una slide de la clase 1.

    PYTHONPATH=_shared python3 clases/01-funciones-y-parametros/medir-referencias.py

Si algún día cambian los datos o cambian los pasos de los sliders, corré esto
otra vez y actualizá los números en:

  · viz/maquina-de-perillas.html   -> MEJOR_RECTA, MEJOR_A, MEJOR_B, RAYA_PROMEDIO
  · viz/zoo-de-funciones.html      -> el diccionario MEJORES
  · slides.html                    -> la slide «el piso de la recta», la slide 31
                                      (INFLACION, INF_A, INF_B) y la slide 4
  · notebook.ipynb                 -> la sección del ajuste a ojo, §3 (salvedades)
                                      y §6 (inflación y la copia de emergencia)
  · notas-docente.md, cuestionario-soluciones.md, referencias.md, VERIFICACION.md

No hay azar en ninguna cuenta: los resultados son deterministas en la misma
máquina y con las mismas versiones de las librerías; con otras versiones los
números pueden cambiar un poco.
"""

from collections import Counter
from pathlib import Path
import sys

import numpy as np

from ssdl import datos

RAIZ = Path(__file__).resolve().parents[2]

ANIO0 = 1984


def grilla(desde, hasta, paso):
    """La misma grilla que recorre un slider con ese `paso`."""
    n = int(round((hasta - desde) / paso))
    return desde + paso * np.arange(n + 1)


def mse(observado, predicho):
    return float(np.mean((np.asarray(observado) - np.asarray(predicho)) ** 2))


# =============================================================================
# 1. La recta sobre la serie de «seguridad» (viz/maquina-de-perillas.html)
# =============================================================================
def piso_de_la_recta():
    anios, seguridad = datos.serie_menciones("seguridad", desde=1984, hasta=2019)
    x = anios - ANIO0

    mejor = (1e18, None, None)
    for a in grilla(-0.02, 0.02, 0.0005):
        for b in grilla(0.0, 0.40, 0.005):
            m = mse(seguridad, a * x + b)
            if m < mejor[0]:
                mejor = (m, a, b)

    plana = mse(seguridad, np.full_like(seguridad, seguridad.mean()))

    print("=" * 72)
    print("1. La recta sobre «seguridad» (36 años, datos reales)")
    print("=" * 72)
    print(f"  MEJOR_RECTA (en la grilla de los sliders) : {mejor[0]:.5f}")
    print(f"  MEJOR_A                                   : {mejor[1]:.4f}")
    print(f"  MEJOR_B                                   : {mejor[2]:.3f}")
    print(f"  RAYA_PROMEDIO (una horizontal en la media): {plana:.5f}")
    print(f"  Arranque de la viz (a=-0.010, b=0.350)    : "
          f"{mse(seguridad, -0.010 * x + 0.350):.5f}")
    print(f"  Lectura sustantiva: cada año sube {mejor[1]:.4f} puntos porcentuales,")
    print(f"  o sea {mejor[1] * 35:.3f} puntos en los 35 años del período.")
    print(f"  desajuste(0, 0.10), el arranque del TODO 2 : "
          f"{mse(seguridad, np.full_like(seguridad, 0.10)):.5f}")
    i05, i06 = int(np.where(anios == 2005)[0][0]), int(np.where(anios == 2006)[0][0])
    print(f"  2005 y 2006 (el mismo discurso en la fuente): "
          f"{seguridad[i05]:.4f} y {seguridad[i06]:.4f}")
    print(f"  Los dos ceros: {[int(a) for a in anios[seguridad == 0]]}")
    print()


# =============================================================================
# 2. El zoo contra los tres desafíos (viz/zoo-de-funciones.html)
# =============================================================================
FORMAS = {
    "recta":       (lambda x, p1, p2: p1 * x + p2,
                    (-1.5, 1.5, 0.05), (-1, 9, 0.1)),
    "parabola":    (lambda x, p1, p2: 4 + p1 * (x - p2) ** 2,
                    (-0.5, 0.5, 0.02), (0, 10, 0.2)),
    "exponencial": (lambda x, p1, p2: p2 * np.exp(p1 * x),
                    (-0.5, 0.5, 0.02), (0.05, 3, 0.05)),
    "sigmoide":    (lambda x, p1, p2: 8 / (1 + np.exp(-p1 * (x - p2))),
                    (0.1, 4, 0.05), (0, 10, 0.2)),
    "seno":        (lambda x, p1, p2: 4 + p2 * np.sin(2 * np.pi * x / p1),
                    (1, 20, 0.25), (0, 4, 0.1)),
    "rampa":       (lambda x, p1, p2: 1.0 + p2 * np.maximum(0, x - p1),
                    (0, 10, 0.2), (-1.5, 1.5, 0.05)),
}

DESAFIOS = {
    1: ("una tendencia constante",
        lambda x: 0.55 * x + 1.0),
    2: ("una S que arranca lento, se acelera y se satura",
        lambda x: 8 / (1 + np.exp(-1.6 * (x - 5)))),
    3: ("dos picos y un valle",
        lambda x: (4 + 2.2 * np.exp(-((x - 2.3) / 1.0) ** 2)
                   - 1.6 * np.exp(-((x - 5.5) / 1.1) ** 2)
                   + 1.9 * np.exp(-((x - 8.5) / 0.9) ** 2))),
}

UMBRAL = 0.02   # por debajo de esto la tarjeta se pone verde


def piso_del_zoo():
    X = np.linspace(0, 10, 60)
    print("=" * 72)
    print("2. El zoo contra los tres desafíos (mejor MSE de cada forma)")
    print(f"   La tarjeta se pone verde con MSE < {UMBRAL}")
    print("=" * 72)
    for nivel, (nombre, f_objetivo) in DESAFIOS.items():
        objetivo = f_objetivo(X)
        print(f"  Desafío {nivel}: {nombre}")
        for forma, (f, g1, g2) in FORMAS.items():
            gr1, gr2 = grilla(*g1), grilla(*g2)
            mejor, donde = 1e18, None
            for p1 in gr1:
                Y = f(X[None, :], p1, gr2[:, None])
                e = ((Y - objetivo[None, :]) ** 2).mean(axis=1)
                i = int(np.argmin(e))
                if e[i] < mejor:
                    mejor, donde = float(e[i]), (float(p1), float(gr2[i]))
            marca = "  <- LA SACA" if mejor < UMBRAL else ""
            print(f"      {forma:12s} {mejor:8.4f}   con {donde[0]:6.2f} , "
                  f"{donde[1]:6.2f}{marca}")
        print()


# =============================================================================
# 3. La recta contra «inflación» (la slide del fracaso, gancho de la clase 2)
# =============================================================================
def fracaso_de_la_recta():
    anios, inflacion = datos.serie_menciones("inflacion", desde=1984, hasta=2019)
    _, suave = datos.serie_menciones("inflacion", desde=1984, hasta=2019, suavizada=True)
    x = anios - ANIO0

    print("=" * 72)
    print("3. La mejor recta sobre «inflación» (el fracaso de la slide «Pero…»)")
    print("=" * 72)
    for nombre, serie in [("cruda", inflacion), ("suavizada (media móvil de 3)", suave)]:
        a, b = np.polyfit(x, serie, 1)
        print(f"  --- serie {nombre}")
        print(f"      pendiente {a:.6f} por año, arranque {b:.4f}")
        print(f"      MSE de la mejor recta        : {mse(serie, a * x + b):.5f}")
        print(f"      MSE de la raya en el promedio: "
              f"{mse(serie, np.full_like(serie, serie.mean())):.5f}")
    print("  O sea: la mejor recta casi no le gana a no hacer nada.")
    print(f"  Arranque del ejercicio del notebook (a=-0.002, b=0.12): "
          f"{mse(suave, -0.002 * x + 0.12):.5f}")
    print("  Valores de la serie suavizada, para copiar a la slide:")
    print("  " + ", ".join(f"{v:.4f}" for v in suave))
    print()


# =============================================================================
# 4. Los números que aparecen en el cuestionario
# =============================================================================
def numeros_del_cuestionario():
    anios, seguridad = datos.serie_menciones("seguridad", desde=1984, hasta=2019)
    _, educacion = datos.serie_menciones("educacion", desde=1984, hasta=2019)
    x = anios - ANIO0

    print("=" * 72)
    print("4. Los números del cuestionario")
    print("=" * 72)
    print("  Ítem 5 — tres rectas sobre «seguridad», de menor a mayor desajuste:")
    print(f"      R (arranca en 0.085 y sube 0.004/año) : "
          f"{mse(seguridad, 0.004 * x + 0.085):.4f}")
    print(f"      P (horizontal en el promedio 0.155)   : "
          f"{mse(seguridad, np.full_like(seguridad, 0.155)):.4f}")
    print(f"      Q (horizontal en 0.40)                : "
          f"{mse(seguridad, np.full_like(seguridad, 0.40)):.4f}")

    a, b = np.polyfit(x, educacion, 1)
    print("  Ítem 8 — la mejor recta sobre «educación»:")
    print(f"      a = {a:.4f} por año, b = {b:.3f} en 1984")
    print(f"      desajuste {mse(educacion, a * x + b):.4f}")
    print(f"      la serie va de {educacion.min():.3f} a {educacion.max():.3f}, "
          f"promedio {educacion.mean():.3f}")
    print(f"      en los 35 años del período, la recta sube {a * 35:.3f} puntos")
    print()


# =============================================================================
# 5. La polisemia de «seguridad» (notebook §3, notas §8, solucionario P10)
# =============================================================================
def polisemia_de_seguridad():
    """Cuántas de las apariciones de «seguridad» no hablan de delito.

    Se mide sobre corpus-mini-gpt.txt (los 35 discursos distintos 1984-2019,
    sin la copia de 2006), con el mismo tokenizador y el mismo léxico que
    arman la serie.
    """
    sys.path.insert(0, str(RAIZ / "datos"))
    from preparar_corpus import LEXICO, normalizar, tokenizar

    ruta = RAIZ / "datos/muestras/discursos-apertura/corpus-mini-gpt.txt"
    lineas = [l for l in ruta.read_text(encoding="utf-8").splitlines()
              if not l.startswith("#")]
    toks = tokenizar(normalizar("\n".join(lineas)))
    lexico = set(LEXICO["seguridad"])
    aciertos = [i for i, w in enumerate(toks) if w in lexico]
    de_seguridad = [i for i in aciertos if toks[i] == "seguridad"]
    siguiente = Counter(toks[i + 1] for i in de_seguridad if i + 1 < len(toks))
    otras = {k: siguiente[k] for k in ("social", "juridica", "alimentaria", "vial")}

    print("=" * 72)
    print("5. La polisemia de «seguridad»")
    print("=" * 72)
    print(f"  Palabras del léxico                 : {len(LEXICO['seguridad'])}")
    print(f"  Aciertos del léxico (35 discursos)  : {len(aciertos)}")
    print(f"  …de los cuales, la palabra seguridad: {len(de_seguridad)}")
    print(f"  «seguridad» + social/jurídica/alimentaria/vial: {otras} "
          f"= {sum(otras.values())}")
    print(f"  = {sum(otras.values()) / len(aciertos):.0%} de todos los aciertos")
    print()


if __name__ == "__main__":
    piso_de_la_recta()
    piso_del_zoo()
    fracaso_de_la_recta()
    numeros_del_cuestionario()
    polisemia_de_seguridad()
