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
  · slides.html                    -> la slide «el piso de la recta»
  · notebook.ipynb                 -> la sección del ajuste a ojo
"""

import numpy as np

from ssdl import datos

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


if __name__ == "__main__":
    piso_de_la_recta()
    piso_del_zoo()
    fracaso_de_la_recta()
    numeros_del_cuestionario()
