"""
ssdl.utils — la plomería aburrida, en un solo lugar.

Acá vive todo lo que no es ni gráficos, ni datos, ni entrenamiento: fijar la
semilla, elegir si corremos en CPU o GPU, contar cuántas perillas tiene un
modelo y medir cuánto tardó algo.

Nada de esto es "el contenido" del curso. Justamente por eso está acá: para no
copiarlo en diez notebooks distintos.

    from ssdl import utils
    utils.fijar_semilla(1983)
    device = utils.elegir_device()
"""

from __future__ import annotations

import os
import pathlib
import random
import sys
import time
from contextlib import contextmanager

# La semilla del curso. 1983: el año de la vuelta de la democracia en Argentina.
# La usamos SIEMPRE la misma para que una corrida sea determinista: en la misma
# máquina y con las mismas versiones de las librerías, los mismos números. Con
# otras versiones (o en GPU) los números cambian un poco. Eso se llama
# reproducibilidad y es un tema de la clase 10, no un capricho.
SEMILLA_DEL_CURSO = 1983


# ---------------------------------------------------------------------------
# torch es opcional a nivel import: así podés usar ssdl.graficos y ssdl.datos
# aunque torch todavía se esté instalando.
# ---------------------------------------------------------------------------
try:
    import torch as _torch
except ImportError:  # pragma: no cover
    _torch = None


def _pedir_torch():
    """Devuelve el módulo torch, o explica en castellano por qué no puede."""
    if _torch is None:
        raise ImportError(
            "Esta función necesita PyTorch y no lo encuentro.\n"
            "En Colab: !pip install torch\n"
            "En tu máquina: pip install torch\n"
            "(Ver recursos/setup.md, sección 'si algo explota'.)"
        )
    return _torch


# ---------------------------------------------------------------------------
# ¿Dónde estamos corriendo?
# ---------------------------------------------------------------------------

def estamos_en_colab() -> bool:
    """
    ¿Este notebook está corriendo en Google Colab?

    Sirve para que el mismo notebook funcione en Colab (donde hay que clonar el
    repo) y en tu máquina (donde ya lo tenés). No adivina por la ruta ni por el
    nombre de usuario: le pregunta a Python si existe el módulo de Colab, que es
    la única señal que no miente.

    >>> isinstance(estamos_en_colab(), bool)
    True
    """
    return "google.colab" in sys.modules or _puede_importar("google.colab")


def _puede_importar(nombre: str) -> bool:
    """¿Existe este módulo, sin llegar a importarlo del todo?"""
    import importlib.util
    try:
        return importlib.util.find_spec(nombre) is not None
    except (ImportError, ValueError, ModuleNotFoundError):
        return False


def estamos_en_notebook() -> bool:
    """
    ¿Estamos adentro de un notebook (Jupyter o Colab) o en una terminal?

    Lo usa la barra de progreso para decidir si puede pisar la línea con '\\r'.
    """
    try:
        from IPython import get_ipython  # type: ignore
        shell = get_ipython()
        if shell is None:
            return False
        return shell.__class__.__name__ in ("ZMQInteractiveShell", "Shell")
    except Exception:
        return False


def raiz_del_repo(desde: str | os.PathLike | None = None) -> pathlib.Path:
    """
    Encuentra la carpeta raíz del repo del curso (la que tiene `_shared/` y `datos/`).

    Busca en este orden:
      1. La variable de entorno DLSS_RAIZ (la setea la celda de bootstrap).
      2. Subiendo carpeta por carpeta desde `desde` (o desde este archivo).

    Así el mismo código encuentra los datos tanto si el notebook está en
    `clases/03-loss-y-gradiente/` como si estás parado en la raíz o en Colab.

    Devuelve un `pathlib.Path`. Si no encuentra nada, avisa con un mensaje que
    se entiende en vez de explotar en un `FileNotFoundError` críptico.
    """
    del_entorno = os.environ.get("DLSS_RAIZ")
    if del_entorno:
        candidata = pathlib.Path(del_entorno).expanduser().resolve()
        if _parece_la_raiz(candidata):
            return candidata

    puntos_de_partida = []
    if desde is not None:
        puntos_de_partida.append(pathlib.Path(desde).resolve())
    puntos_de_partida.append(pathlib.Path(__file__).resolve())
    puntos_de_partida.append(pathlib.Path.cwd().resolve())

    for punto in puntos_de_partida:
        for candidata in [punto, *punto.parents]:
            if _parece_la_raiz(candidata):
                return candidata

    raise FileNotFoundError(
        "No encuentro la raíz del repo del curso (la carpeta que tiene "
        "`_shared/` y `datos/`).\n"
        "Si estás en Colab, corré la celda de bootstrap de arriba.\n"
        "Si estás en tu máquina, abrí el notebook desde adentro del repo, o "
        "seteá la variable de entorno DLSS_RAIZ apuntando a la carpeta `dlss`."
    )


def _parece_la_raiz(carpeta: pathlib.Path) -> bool:
    """Una carpeta es la raíz si tiene el paquete ssdl y la carpeta de datos."""
    return (carpeta / "_shared" / "ssdl").is_dir() and (carpeta / "datos").is_dir()


# ---------------------------------------------------------------------------
# Semillas
# ---------------------------------------------------------------------------

def fijar_semilla(semilla: int = SEMILLA_DEL_CURSO, verboso: bool = False) -> int:
    """
    Fija la semilla de TODOS los generadores de azar que usamos.

    Un modelo arranca con perillas al azar y los lotes se barajan al azar. Si no
    fijás la semilla, cada vez que corrés el notebook te dan números distintos y
    no podés saber si mejoró porque cambiaste algo o porque tuviste suerte.

    Fijar la semilla no hace al modelo mejor. Hace a tu resultado *comparable*,
    que es una condición para poder afirmar cualquier cosa.

    Parámetros
    ----------
    semilla : int
        El número mágico. Por defecto 1983, la semilla del curso.
    verboso : bool
        Si es True imprime qué fijó.

    Devuelve la semilla usada, para que puedas guardarla en tu paper.

    >>> fijar_semilla(7)
    7
    """
    random.seed(semilla)
    os.environ["PYTHONHASHSEED"] = str(semilla)

    try:
        import numpy as np
        np.random.seed(semilla)
    except ImportError:
        pass

    if _torch is not None:
        _torch.manual_seed(semilla)
        if _torch.cuda.is_available():
            _torch.cuda.manual_seed_all(semilla)
            # Que cuDNN elija siempre el mismo algoritmo, aunque sea más lento.
            _torch.backends.cudnn.deterministic = True
            _torch.backends.cudnn.benchmark = False

    if verboso:
        print(f"Semilla fijada en {semilla} (random, numpy y torch).")
    return semilla


# ---------------------------------------------------------------------------
# CPU / GPU
# ---------------------------------------------------------------------------

def elegir_device(preferir_gpu: bool = True, verboso: bool = False):
    """
    Elige dónde van a vivir los tensores: la GPU si hay, la CPU si no.

    En este curso casi todo corre en CPU en segundos. La GPU sólo hace falta
    para el mini-GPT de la clase 8, y ni siquiera ahí es obligatoria.

    Parámetros
    ----------
    preferir_gpu : bool
        Poné False para forzar CPU (útil para comparar tiempos, o para
        descartar que un bug sea culpa de la GPU).
    verboso : bool
        Si es True imprime qué eligió y con qué placa.

    Devuelve un `torch.device`.
    """
    torch = _pedir_torch()
    if preferir_gpu and torch.cuda.is_available():
        device = torch.device("cuda")
        nombre = torch.cuda.get_device_name(0)
    elif preferir_gpu and getattr(torch.backends, "mps", None) is not None \
            and torch.backends.mps.is_available():
        # Mac con chip Apple.
        device = torch.device("mps")
        nombre = "GPU de Apple (MPS)"
    else:
        device = torch.device("cpu")
        nombre = "CPU"

    if verboso:
        print(f"Corriendo en: {device}  ({nombre})")
    return device


# ---------------------------------------------------------------------------
# Contar perillas
# ---------------------------------------------------------------------------

def contar_parametros(modelo, solo_entrenables: bool = True,
                      detallado: bool = False) -> int:
    """
    Cuenta cuántas perillas tiene un modelo.

    En la clase 1 un modelo tiene 2 perillas (pendiente y ordenada) y las podés
    mover a mano. En la clase 8 tiene 3 millones. Es exactamente la misma idea,
    y este número es la mejor forma de sentir la diferencia.

    Parámetros
    ----------
    modelo : torch.nn.Module
    solo_entrenables : bool
        Si es True cuenta sólo las que el optimizador puede mover
        (las que tienen requires_grad=True). Cuando congelás un modelo
        pre-entrenado en la clase 9, la diferencia entre los dos números
        es justo lo que estás congelando.
    detallado : bool
        Si es True imprime una tabla capa por capa.

    Devuelve el total (int).
    """
    _pedir_torch()
    filas = []
    total = 0
    for nombre, p in modelo.named_parameters():
        if solo_entrenables and not p.requires_grad:
            continue
        n = p.numel()
        total += n
        filas.append((nombre, tuple(p.shape), n))

    if detallado:
        ancho = max([len(f[0]) for f in filas], default=10)
        print(f"{'capa'.ljust(ancho)}  {'forma':>18}  {'perillas':>12}")
        print("-" * (ancho + 36))
        for nombre, forma, n in filas:
            print(f"{nombre.ljust(ancho)}  {str(forma):>18}  {n:>12,}")
        print("-" * (ancho + 36))
        print(f"{'TOTAL'.ljust(ancho)}  {'':>18}  {total:>12,}")

    return total


def formatear_cantidad(n: float) -> str:
    """
    Convierte 3141592 en '3,1 M'. Para decir cantidades en voz alta.

    >>> formatear_cantidad(3141592)
    '3,1 M'
    >>> formatear_cantidad(950)
    '950'
    """
    n = float(n)
    for limite, sufijo in ((1e9, " MM"), (1e6, " M"), (1e3, " mil")):
        if abs(n) >= limite:
            return f"{n / limite:.1f}".replace(".", ",") + sufijo
    return f"{n:.0f}"


# ---------------------------------------------------------------------------
# Tiempo
# ---------------------------------------------------------------------------

@contextmanager
def medir_tiempo(que: str = "eso", verboso: bool = True):
    """
    Cronómetro para bloques de código. Se usa con `with`.

        with utils.medir_tiempo("entrenar el mini-GPT"):
            entrenar(...)
        # -> entrenar el mini-GPT: 42,3 s

    Guarda el resultado en el objeto que devuelve, por si lo querés usar:

        with utils.medir_tiempo("cargar", verboso=False) as t:
            corpus = datos.debates_aguasclaras()
        print(t.segundos)
    """
    class _Cronometro:
        segundos = 0.0

    crono = _Cronometro()
    arranque = time.perf_counter()
    try:
        yield crono
    finally:
        crono.segundos = time.perf_counter() - arranque
        if verboso:
            print(f"{que}: {formatear_duracion(crono.segundos)}")


def formatear_duracion(segundos: float) -> str:
    """
    Convierte 125.4 en '2 min 5 s'. Los milisegundos también se entienden.

    >>> formatear_duracion(0.042)
    '42 ms'
    >>> formatear_duracion(125.4)
    '2 min 5 s'
    """
    if segundos < 1:
        return f"{segundos * 1000:.0f} ms"
    if segundos < 60:
        return f"{segundos:.1f} s".replace(".", ",")
    minutos = int(segundos // 60)
    resto = segundos - minutos * 60
    return f"{minutos} min {resto:.0f} s"


# ---------------------------------------------------------------------------
# Diagnóstico general
# ---------------------------------------------------------------------------

def resumen_del_entorno(imprimir: bool = True) -> dict:
    """
    Dice dónde estás parada y con qué versiones. Es la primera celda que
    conviene correr cuando algo no anda, y lo primero que te va a pedir alguien
    que te ayude a debuggear.

    Devuelve un diccionario con los datos, e (por defecto) los imprime.
    """
    info = {
        "python": sys.version.split()[0],
        "colab": estamos_en_colab(),
        "notebook": estamos_en_notebook(),
    }
    try:
        info["raiz_del_repo"] = str(raiz_del_repo())
    except FileNotFoundError:
        info["raiz_del_repo"] = "(no encontrada)"

    for nombre_modulo, clave in (("torch", "torch"), ("numpy", "numpy"),
                                 ("matplotlib", "matplotlib")):
        try:
            modulo = __import__(nombre_modulo)
            info[clave] = getattr(modulo, "__version__", "?")
        except ImportError:
            info[clave] = "(no instalado)"

    if _torch is not None:
        info["gpu"] = (_torch.cuda.get_device_name(0)
                       if _torch.cuda.is_available() else "no hay (CPU)")
    else:
        info["gpu"] = "(torch no instalado)"

    if imprimir:
        print("Entorno")
        print("-" * 46)
        for clave, valor in info.items():
            print(f"  {clave.ljust(16)} {valor}")
    return info


if __name__ == "__main__":
    import doctest
    fallas, corridos = doctest.testmod()
    print(f"doctests: {corridos - fallas}/{corridos} OK")
    resumen_del_entorno()
