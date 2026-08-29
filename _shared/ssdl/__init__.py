"""
ssdl — Social Science Deep Learning
El paquete de plomería del curso "Deep Learning para Cientistas Sociales".

Acá NO está el contenido del curso. El contenido está en los notebooks, en las
slides y en las visualizaciones. Acá está lo aburrido que si no habría que
copiar y pegar en diez notebooks: cargar los datos, fijar la semilla, dibujar
con los colores de siempre, correr el loop de entrenamiento.

Cuatro módulos, y ninguno esconde nada importante:

    ssdl.datos          traer datos, tokenizar, partir en train/val/test
    ssdl.graficos       figuras con la identidad visual y la semántica de color
    ssdl.entrenamiento  el loop de la clase 4, explícito, con barra de progreso
    ssdl.utils          semillas, device, contar perillas, medir tiempo

Arranque típico de un notebook:

    from ssdl import datos, graficos as g, entrenamiento as ent, utils
    utils.fijar_semilla(1983)

    anios, seguridad = datos.serie_menciones("seguridad")
    g.plot_serie(anios, seguridad, titulo="Menciones a seguridad")

La referencia completa de la API, con ejemplos copiables, está en
_shared/ssdl/README.md.
"""

__version__ = "1.0"
__all__ = [
    "datos", "graficos", "entrenamiento", "utils",
    "fijar_semilla", "elegir_device", "contar_parametros", "medir_tiempo",
    "estamos_en_colab", "resumen_del_entorno", "SEMILLA_DEL_CURSO",
    "entrenar", "evaluar", "predecir", "Historial",
]

from . import utils
from . import datos
from . import graficos
from . import entrenamiento

# Los atajos que se usan en casi todos los notebooks, para poder escribir
# `ssdl.fijar_semilla()` sin tener que acordarse de en qué módulo estaba.
from .utils import (
    SEMILLA_DEL_CURSO,
    fijar_semilla,
    elegir_device,
    contar_parametros,
    medir_tiempo,
    estamos_en_colab,
    resumen_del_entorno,
)
from .entrenamiento import entrenar, evaluar, predecir, Historial


def hola():
    """
    Chequeo de que todo importó bien. Corré esto en la primera celda si algo
    huele raro: te dice la versión del paquete, dónde encontró los datos y si
    hay GPU.
    """
    print(f"ssdl {__version__} — Deep Learning para Cientistas Sociales")
    utils.resumen_del_entorno()
    try:
        anios, v = datos.serie_menciones("seguridad")
        print(f"\n✓ Datos OK: la serie de menciones a seguridad tiene "
              f"{len(anios)} años ({int(anios[0])}-{int(anios[-1])}).")
    except Exception as error:
        print(f"\n✗ No pude cargar los datos: {error}")
