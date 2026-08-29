#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exporta a `figuras/` las cinco figuras que dibuja `notebook.ipynb`.

    python3 clases/10-criterio-validacion-y-etica/exportar-figuras.py

**No duplica el código del notebook: lo corre.** Lee `notebook.ipynb`, ejecuta
sus celdas de código en orden y guarda cada figura que aparezca, en el orden en
que aparece. Así es imposible que las imágenes de `figuras/` digan una cosa y el
notebook otra, que es exactamente el problema que enseña esta clase.

Tarda lo mismo que el notebook (menos de medio minuto en CPU) y no necesita red.
"""
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import nbformat  # noqa: E402

AQUI = pathlib.Path(__file__).resolve().parent
SALIDA = AQUI / "figuras"

# El orden es el de aparición en el notebook. Si agregás una figura, agregá acá
# su nombre; si sobran o faltan nombres, el script avisa en vez de callarse.
NOMBRES = [
    "01-matriz-de-confusion.png",
    "02-terminos-influyentes.png",
    "03-ablacion-vs-ruido.png",
    "04-pares-minimos.png",
    "05-sesgo-por-sujeto.png",
]


def main():
    SALIDA.mkdir(exist_ok=True)
    nb = nbformat.read(AQUI / "notebook.ipynb", as_version=4)

    # Corremos desde la carpeta de la clase para que el bootstrap del notebook
    # encuentre la raíz del repo subiendo carpetas, igual que en Colab o Jupyter.
    entorno = {"__name__": "__main__", "get_ipython": lambda: None}
    guardadas = []

    for i, celda in enumerate(nb.cells):
        if celda.cell_type != "code":
            continue
        vistas = set(plt.get_fignums())
        try:
            exec(compile(celda.source, f"<celda {i}>", "exec"), entorno)
        except SystemExit as e:               # el bootstrap corta así si no halla el repo
            print(f"El notebook cortó en la celda {i}: {e}")
            return 1
        for num in sorted(set(plt.get_fignums()) - vistas):
            fig = plt.figure(num)
            if not fig.get_axes():
                continue
            k = len(guardadas)
            nombre = NOMBRES[k] if k < len(NOMBRES) else f"{k + 1:02d}-sin-nombre.png"
            fig.savefig(SALIDA / nombre, dpi=140, bbox_inches="tight",
                        facecolor=fig.get_facecolor())
            guardadas.append(nombre)
            print(f"  celda {i:>2} -> figuras/{nombre}")
        plt.close("all")

    print(f"\n{len(guardadas)} figuras en {SALIDA}")
    if len(guardadas) != len(NOMBRES):
        print(f"OJO: esperaba {len(NOMBRES)} y salieron {len(guardadas)}. "
              f"Actualizá la lista NOMBRES de este script.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
