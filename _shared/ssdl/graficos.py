"""
ssdl.graficos — que todas las figuras del curso se parezcan entre sí.

Dos razones para que esto exista, y ninguna es estética:

1. LA SEMÁNTICA DE COLOR. En este curso el color no decora: significa. Los
   datos son TINTA, el modelo es AZUL, las perillas son VIOLETA, el error es
   ROJO, lo que el modelo no vio es NARANJA. Diez clases seguidas. Si en el
   notebook de la clase 3 la recta del modelo saliera verde, le estaríamos
   pidiendo al estudiante que aprenda el código de colores de nuevo cada martes.
   Son los mismos colores de las slides y de las visualizaciones (curso.css).

2. NO REPETIR PLOMERÍA. Nadie tiene que acordarse de `ax.spines[...]` para
   dibujar una nube de puntos.

Uso típico:

    from ssdl import graficos as g
    fig, ax = g.figura(titulo="Menciones a seguridad")
    g.plot_serie(anios, valores, ax=ax)

El estilo se aplica solo al importar el módulo. Si trabajás en un notebook de
tema oscuro y querés las figuras oscuras, llamá a `g.estilo_curso(oscuro=True)`.
"""

from __future__ import annotations

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

# ---------------------------------------------------------------------------
# LA PALETA. Copiada a mano de _shared/css/curso.css. Si cambia allá, cambia acá.
# ---------------------------------------------------------------------------

PALETA_CLARA = {
    "papel":     "#fbf4e8",   # el fondo de la página
    "fondo":     "#fffaf1",   # el fondo de la figura (un pelín más claro)
    "tinta":     "#2a2521",   # texto principal
    "tinta_2":   "#59504a",   # texto secundario
    "tinta_3":   "#8c8079",   # ticks, notas al pie
    "grilla":    "#e6d9c0",
    "eje":       "#6f645c",
    "borde":     "#d9c9ae",
    # --- los seis colores que significan algo ---
    "datos":     "#33302c",   # lo observado: la nube de puntos, el corpus
    "verdad":    "#9a9089",   # la verdad subyacente (sólo con datos sintéticos)
    "modelo":    "#1f6fb5",   # lo que el modelo dibuja: recta, curva, predicción
    "parametro": "#8244c4",   # las perillas: pesos, gradientes, el punto en el mapa
    "error":     "#cf3b28",   # el desajuste: segmentos, loss, falsos positivos
    "val":       "#e08519",   # lo que el modelo NO vio: validación, test
    "ok":        "#2f8a56",   # correcto, aceptado, semáforo en verde
    "acento":    "#0d9488",   # "mirá acá". Sin significado técnico.
}

PALETA_OSCURA = {
    "papel":     "#1a1714",
    "fondo":     "#14120f",
    "tinta":     "#f2e8da",
    "tinta_2":   "#c4b8aa",
    "tinta_3":   "#8e8377",
    "grilla":    "#302b25",
    "eje":       "#9a8f83",
    "borde":     "#3d372f",
    "datos":     "#ece1d2",
    "verdad":    "#8b8177",
    "modelo":    "#64b0f0",
    "parametro": "#c091f5",
    "error":     "#ff7a63",
    "val":       "#ffab4d",
    "ok":        "#5fcb8c",
    "acento":    "#2dd4bf",
}

# La paleta activa. `estilo_curso()` la cambia; el resto del módulo la lee.
C = dict(PALETA_CLARA)

# Atajos cómodos para escribir en los notebooks: g.DATOS, g.MODELO, ...
DATOS = PALETA_CLARA["datos"]
VERDAD = PALETA_CLARA["verdad"]
MODELO = PALETA_CLARA["modelo"]
PARAMETRO = PALETA_CLARA["parametro"]
ERROR = PALETA_CLARA["error"]
VAL = PALETA_CLARA["val"]
OK = PALETA_CLARA["ok"]
ACENTO = PALETA_CLARA["acento"]

# Colores por clase para clasificación. UNA sola lista, usada por
# `scatter_clases` y por `frontera_de_decision`: si cada función eligiera la
# suya, el mismo dataset saldría con los colores invertidos entre la nube y la
# frontera, y el estudiante creería que el modelo predice todo al revés.
COLORES_CLASES = [MODELO, ERROR, OK, VAL, PARAMETRO, ACENTO]


def colores_clases() -> list:
    """
    Colores por clase para clasificación, en la paleta activa (clara u oscura).

        c0, c1 = g.colores_clases()[:2]     # azul «modelo», rojo «error»
    """
    return [C["modelo"], C["error"], C["ok"], C["val"], C["parametro"], C["acento"]]


def paleta() -> dict:
    """
    Devuelve el diccionario de colores activo, por si querés dibujar algo a mano.

        c = g.paleta()
        ax.plot(x, y, color=c["modelo"])
    """
    return dict(C)


# ---------------------------------------------------------------------------
# Mapas de color (colormaps) con la misma semántica
# ---------------------------------------------------------------------------

def _construir_colormaps(c: dict) -> dict:
    """Arma los degradés a partir de la paleta activa."""
    return {
        # Paisaje de loss: claro donde la loss es baja, rojo donde es alta.
        # Se lee como un mapa topográfico: el fondo del valle es lo claro.
        "loss": LinearSegmentedColormap.from_list(
            "ssdl_loss", [c["fondo"], "#f6e3b8", c["val"], c["error"], "#6d1a10"]),
        # Atención / probabilidad: de nada (papel) a mucho (azul del modelo).
        "atencion": LinearSegmentedColormap.from_list(
            "ssdl_atencion", [c["fondo"], "#bcd8ef", c["modelo"], "#0d3a63"]),
        # Filtros de una CNN: azul negativo, blanco cero, rojo positivo.
        # Mismo criterio que la viz kernel-deslizante.html de la clase 5.
        "filtro": LinearSegmentedColormap.from_list(
            "ssdl_filtro", [c["modelo"], "#9dc4e4", "#ffffff", "#eda294", c["error"]]),
        # Conteos (matriz de confusión).
        "conteo": LinearSegmentedColormap.from_list(
            "ssdl_conteo", [c["fondo"], "#cfe1f1", c["modelo"]]),
    }


CMAPS = _construir_colormaps(C)


# ---------------------------------------------------------------------------
# El estilo
# ---------------------------------------------------------------------------

def estilo_curso(escala: float = 1.0, oscuro: bool = False) -> None:
    """
    Aplica el estilo visual del curso a todas las figuras de matplotlib.

    Se llama solo cuando importás el módulo. Volvé a llamarlo si querés:

    Parámetros
    ----------
    escala : float
        Multiplica todos los tamaños de letra. Para proyectar en un aula grande,
        `estilo_curso(escala=1.4)`.
    oscuro : bool
        Usa la paleta oscura (mismos roles, distintos tonos).
    """
    global C, CMAPS, DATOS, VERDAD, MODELO, PARAMETRO, ERROR, VAL, OK, ACENTO
    global COLORES_CLASES

    C = dict(PALETA_OSCURA if oscuro else PALETA_CLARA)
    CMAPS = _construir_colormaps(C)
    DATOS, VERDAD, MODELO = C["datos"], C["verdad"], C["modelo"]
    PARAMETRO, ERROR, VAL = C["parametro"], C["error"], C["val"]
    OK, ACENTO = C["ok"], C["acento"]
    COLORES_CLASES = [MODELO, ERROR, OK, VAL, PARAMETRO, ACENTO]

    base = 11 * escala
    matplotlib.rcParams.update({
        # --- superficies ---
        "figure.facecolor": C["fondo"],
        "axes.facecolor": C["fondo"],
        "savefig.facecolor": C["fondo"],
        "savefig.bbox": "tight",
        "figure.dpi": 110,
        "savefig.dpi": 140,
        # --- tipografía: sólo familias que existen en cualquier máquina ---
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial", "sans-serif"],
        "font.size": base,
        "axes.titlesize": base * 1.25,
        "axes.labelsize": base * 1.0,
        "xtick.labelsize": base * 0.88,
        "ytick.labelsize": base * 0.88,
        "legend.fontsize": base * 0.90,
        "figure.titlesize": base * 1.4,
        # --- ejes: sin la cajita, sólo abajo e izquierda ---
        "axes.edgecolor": C["eje"],
        "axes.labelcolor": C["tinta_2"],
        "axes.titlecolor": C["tinta"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.titlepad": 12,
        "axes.titleweight": "bold",
        "axes.linewidth": 1.0,
        "text.color": C["tinta"],
        # --- grilla suave, siempre detrás ---
        "axes.grid": True,
        "grid.color": C["grilla"],
        "grid.linewidth": 0.9,
        "grid.alpha": 1.0,
        "axes.axisbelow": True,
        # --- ticks ---
        "xtick.color": C["tinta_3"],
        "ytick.color": C["tinta_3"],
        "xtick.direction": "out",
        "ytick.direction": "out",
        # --- leyenda ---
        "legend.frameon": True,
        "legend.facecolor": C["papel"],
        "legend.edgecolor": C["borde"],
        "legend.framealpha": 0.95,
        "legend.borderpad": 0.6,
        # --- líneas y puntos ---
        "lines.linewidth": 2.2,
        "lines.markersize": 6,
        "scatter.edgecolors": "none",
        "image.cmap": "viridis",
        # --- layout que no encima las etiquetas ---
        "figure.constrained_layout.use": True,
        "figure.constrained_layout.h_pad": 0.08,
        "figure.constrained_layout.w_pad": 0.08,
    })


estilo_curso()  # se aplica al importar


# ---------------------------------------------------------------------------
# Helpers básicos
# ---------------------------------------------------------------------------

def figura(ancho: float = 8, alto: float = 5, titulo: str | None = None,
           xlabel: str | None = None, ylabel: str | None = None,
           filas: int = 1, columnas: int = 1, **kwargs):
    """
    Crea una figura con el estilo del curso ya puesto.

        fig, ax = g.figura(titulo="Menciones a seguridad", xlabel="año", ylabel="%")

    Con `filas`/`columnas` devuelve un array de ejes, como `plt.subplots`.
    """
    fig, ax = plt.subplots(filas, columnas, figsize=(ancho, alto), **kwargs)
    if filas * columnas == 1:
        if titulo:
            ax.set_title(titulo)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
    elif titulo:
        fig.suptitle(titulo)
    return fig, ax


def guardar(fig, ruta: str, dpi: int = 140) -> str:
    """
    Guarda la figura en disco y devuelve la ruta. Crea la carpeta si no existe.
    """
    import os
    carpeta = os.path.dirname(os.path.abspath(ruta))
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    fig.savefig(ruta, dpi=dpi, facecolor=fig.get_facecolor())
    return ruta


def _a_numpy(x):
    """Acepta lo que le tires (lista, numpy, tensor de torch) y devuelve numpy."""
    if x is None:
        return None
    if hasattr(x, "detach"):          # tensor de torch
        x = x.detach().cpu().numpy()
    return np.asarray(x)


def _ejes(ax, ancho=8, alto=5, titulo=None, xlabel=None, ylabel=None):
    """
    Si te pasaron un `ax` lo usa; si no, crea uno nuevo.

    En los dos casos aplica título y etiquetas: si sólo las pusiera al crear el
    eje, `g.plot_serie(x, y, ax=mi_eje, titulo="...")` perdería el título en
    silencio, que es justo lo que uno hace al armar una grilla de subplots.
    """
    if ax is None:
        _, ax = figura(ancho, alto)
    if titulo:
        ax.set_title(titulo)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return ax


def _nota(ax, texto: str, color: str | None = None, arriba: bool = False):
    """Cartelito dentro del gráfico, arriba a la izquierda o abajo a la derecha."""
    ax.text(
        0.02 if arriba else 0.98, 0.97 if arriba else 0.03, texto,
        transform=ax.transAxes, fontsize=matplotlib.rcParams["font.size"] * 0.92,
        va="top" if arriba else "bottom", ha="left" if arriba else "right",
        color=color or C["tinta_2"],
        bbox=dict(boxstyle="round,pad=0.45", facecolor=C["papel"],
                  edgecolor=C["borde"], alpha=0.95),
    )


# ===========================================================================
# CLASES 1-2: funciones, parámetros, composición
# ===========================================================================

def plot_funcion(f, x=(-5, 5), n=400, ax=None, etiqueta=None,
                 color=None, titulo=None, xlabel="x", ylabel="f(x)", **kw):
    """
    Dibuja una función. `f` puede ser un callable f(x) o directamente un array
    de valores (en cuyo caso `x` tiene que ser el array de las x).

        g.plot_funcion(lambda x: x**2, x=(-3, 3))

    Parámetros
    ----------
    f : callable o array
    x : (min, max) o array de x
    color : por defecto AZUL, que es el color de "lo que el modelo dibuja".
    """
    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    xs = np.linspace(x[0], x[1], n) if (isinstance(x, tuple) and len(x) == 2) else _a_numpy(x)
    ys = _a_numpy(f(xs)) if callable(f) else _a_numpy(f)
    ax.plot(xs, ys, color=color or C["modelo"], label=etiqueta,
            zorder=3, solid_capstyle="round", **kw)
    if etiqueta:
        ax.legend()
    return ax


def plot_familia(f, valores, x=(-5, 5), n=400, nombre_parametro="a",
                 destacar=None, ax=None, titulo=None,
                 xlabel="x", ylabel="f(x)", leyenda=True):
    """
    LA figura de la clase 1: la misma función dibujada con distintos valores de
    UN parámetro. Todas las curvas en violeta (color de las perillas), de claro
    a oscuro; la destacada, en azul y más gruesa.

    El punto pedagógico: mover x te mueve A LO LARGO de una curva; mover el
    parámetro te cambia DE curva. El montón de curvas grises-violetas es
    "todas las teorías posibles"; elegir el parámetro es elegir una.

        g.plot_familia(lambda x, a: a * x**2, valores=[0.2, 0.5, 1, 2, 4],
                       nombre_parametro="a", destacar=1)

    Parámetros
    ----------
    f : callable f(x, parametro)
    valores : lista de valores del parámetro
    destacar : uno de los valores, que se dibuja en azul y grueso
    """
    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    xs = np.linspace(x[0], x[1], n) if (isinstance(x, tuple) and len(x) == 2) else _a_numpy(x)
    valores = list(valores)

    # Degradé de violetas: claro para los extremos, oscuro para el medio.
    degrade = LinearSegmentedColormap.from_list(
        "perillas", ["#dcc7f2", C["parametro"], "#3f1d66"])
    intensidades = np.linspace(0.15, 0.95, max(len(valores), 2))

    for i, v in enumerate(valores):
        es_destacada = (destacar is not None and np.isclose(v, destacar))
        ys = _a_numpy(f(xs, v))
        ax.plot(
            xs, ys,
            color=C["modelo"] if es_destacada else degrade(intensidades[i]),
            linewidth=3.2 if es_destacada else 1.7,
            alpha=1.0 if es_destacada else 0.85,
            zorder=5 if es_destacada else 3,
            label=f"{nombre_parametro} = {v:g}",
        )

    if leyenda and len(valores) <= 9:
        ax.legend(title=f"perilla «{nombre_parametro}»", loc="best",
                  labelcolor=C["tinta_2"])
    return ax


def plot_serie(anios, valores, ax=None, etiqueta=None, color=None,
               titulo=None, xlabel="año", ylabel="% de palabras del discurso",
               con_linea=True, con_puntos=True, **kw):
    """
    La serie temporal que atraviesa las clases 1 a 4: puntos gordos (los datos
    observados, en TINTA) unidos por una línea fina que sólo ayuda a leer.

        g.plot_serie(anios, seguridad, titulo="Menciones a seguridad")
    """
    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    anios, valores = _a_numpy(anios), _a_numpy(valores)
    color = color or C["datos"]
    if con_linea:
        ax.plot(anios, valores, color=color, linewidth=1.1, alpha=0.55, zorder=2)
    if con_puntos:
        ax.scatter(anios, valores, s=42, color=color, zorder=4,
                   label=etiqueta, edgecolors=C["fondo"], linewidths=0.8, **kw)
    if etiqueta:
        ax.legend()
    return ax


def plot_ajuste(x, y, modelo=None, y_pred=None, mostrar_errores=True,
                verdad=None, ax=None, titulo=None, xlabel="x", ylabel="y",
                etiqueta_modelo="modelo", loss=None, nombre_loss="MSE"):
    """
    LA figura del curso: los datos, la curva del modelo, y los errores como
    segmentos verticales rojos que van del punto a la curva.

    Es la clase 1 (mover perillas a ojo), la clase 3 (el mundo real al lado del
    mapa de loss) y la clase 4 (la curva que se acomoda mientras entrena).

        g.plot_ajuste(x, y, modelo=lambda x: 2*x + 1)

    Parámetros
    ----------
    x, y : los datos observados
    modelo : callable que toma x y devuelve la predicción (se dibuja densa)
    y_pred : alternativa a `modelo`: las predicciones ya calculadas en x
    mostrar_errores : dibuja los segmentos rojos, uno por caso
    verdad : callable opcional con la verdad subyacente (datos sintéticos):
             se dibuja en gris punteado, como corresponde
    loss : si le pasás el número, lo muestra en un cartelito
    """
    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    x, y = _a_numpy(x), _a_numpy(y)

    # 1. la verdad subyacente, si la conocemos (siempre punteada: es una cortesía
    #    del simulador, no algo que tengas en la vida real)
    if verdad is not None:
        xs = np.linspace(x.min(), x.max(), 300)
        ys = _a_numpy(verdad(xs)) if callable(verdad) else _a_numpy(verdad)
        ax.plot(xs, ys, color=C["verdad"], linestyle=(0, (5, 4)), linewidth=2.0,
                zorder=2, label="verdad subyacente")

    # 2. las predicciones en los puntos observados (para los segmentos)
    if y_pred is None and modelo is not None:
        y_pred = _a_numpy(modelo(x))
    y_pred = _a_numpy(y_pred)

    # 3. los errores, ANTES de los puntos para que no los tapen
    if mostrar_errores and y_pred is not None:
        for xi, yi, pi in zip(x, y, y_pred):
            ax.plot([xi, xi], [yi, pi], color=C["error"], linewidth=1.6,
                    alpha=0.75, zorder=3, solid_capstyle="butt")

    # 4. la curva del modelo, densa
    if modelo is not None:
        xs = np.linspace(x.min(), x.max(), 300)
        ax.plot(xs, _a_numpy(modelo(xs)), color=C["modelo"], linewidth=2.6,
                zorder=5, label=etiqueta_modelo)
    elif y_pred is not None:
        orden = np.argsort(x)
        ax.plot(x[orden], y_pred[orden], color=C["modelo"], linewidth=2.6,
                zorder=5, label=etiqueta_modelo)

    # 5. los datos, arriba de todo
    ax.scatter(x, y, s=46, color=C["datos"], zorder=6, label="datos",
               edgecolors=C["fondo"], linewidths=0.9)

    if loss is None and y_pred is not None:
        loss = float(np.mean((y - y_pred) ** 2))
    if loss is not None:
        _nota(ax, f"{nombre_loss} = {loss:.4g}", color=C["error"])

    ax.legend(loc="best")
    return ax


# ===========================================================================
# CLASES 2-4: clasificación en el plano
# ===========================================================================

def scatter_clases(X, y, ax=None, titulo=None, xlabel="x₁", ylabel="x₂",
                   etiquetas=None, colores=None, s=38):
    """
    Nube de puntos coloreada por clase. Para los datasets de juguete
    (espiral, dos lunas, círculos, XOR) de las clases 2 a 4.
    """
    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    X, y = _a_numpy(X), _a_numpy(y).astype(int).ravel()
    clases = np.unique(y)
    colores = colores or colores_clases()
    for i, clase in enumerate(clases):
        m = y == clase
        nombre = etiquetas[i] if etiquetas is not None else f"clase {clase}"
        ax.scatter(X[m, 0], X[m, 1], s=s, color=colores[i % len(colores)],
                   label=nombre, zorder=4, edgecolors=C["fondo"], linewidths=0.7)
    ax.legend(loc="best")
    ax.set_aspect("equal", adjustable="datalim")
    return ax


def frontera_de_decision(predecir, X, y, ax=None, titulo=None, resolucion=250,
                         margen=0.5, etiquetas=None, xlabel="x₁", ylabel="x₂"):
    """
    Pinta el fondo con lo que el modelo decidiría en CADA punto del plano, y
    encima dibuja los datos. La frontera es donde cambia el color de fondo.

    `predecir` es una función que toma una matriz (n, 2) de numpy y devuelve
    (n,) con la probabilidad de la clase 1 (o el score, o la clase). Si le pasás
    un modelo de PyTorch, envolvelo:

        g.frontera_de_decision(
            lambda XX: torch.sigmoid(modelo(torch.tensor(XX, dtype=torch.float32))).detach().numpy().ravel(),
            X, y)

    El momento pedagógico: cuando la frontera es una recta, es porque el modelo
    no tiene dobleces. Es la clase 2 dibujada en dos dimensiones.
    """
    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    X, y = _a_numpy(X), _a_numpy(y).astype(int).ravel()

    x_min, x_max = X[:, 0].min() - margen, X[:, 0].max() + margen
    y_min, y_max = X[:, 1].min() - margen, X[:, 1].max() + margen
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, resolucion),
                         np.linspace(y_min, y_max, resolucion))
    rejilla = np.c_[xx.ravel(), yy.ravel()]
    z = _a_numpy(predecir(rejilla)).astype(float).ravel().reshape(xx.shape)

    # Fondo del MISMO color que los puntos de esa clase: donde el modelo dice
    # "clase 0" pinta del color de la clase 0, donde dice "clase 1" del color
    # de la clase 1. Si el fondo y los puntos no coinciden, el estudiante lee
    # cada acierto como un error.
    fondo = LinearSegmentedColormap.from_list(
        "frontera", [colores_clases()[0], C["fondo"], colores_clases()[1]])
    centro = 0.5 if (0.0 <= np.nanmin(z) and np.nanmax(z) <= 1.0) else 0.0
    lim = max(abs(np.nanmin(z) - centro), abs(np.nanmax(z) - centro), 1e-9)
    # Fondo con imshow y no con contourf: contourf dibuja bandas discretas y en
    # una superficie suave se ven como rayas diagonales que no significan nada.
    ax.imshow(z, extent=(x_min, x_max, y_min, y_max), origin="lower",
              aspect="auto", cmap=fondo, alpha=0.6, zorder=1,
              interpolation="bilinear",
              norm=TwoSlopeNorm(vmin=centro - lim, vcenter=centro, vmax=centro + lim))
    # La frontera: la línea donde el modelo cambia de opinión.
    ax.contour(xx, yy, z, levels=[centro], colors=[C["tinta"]],
               linewidths=2.0, zorder=2)

    clases = np.unique(y)
    for i, clase in enumerate(clases):
        m = y == clase
        nombre = etiquetas[i] if etiquetas is not None else f"clase {clase}"
        ax.scatter(X[m, 0], X[m, 1], s=38, zorder=4, label=nombre,
                   color=colores_clases()[i % 6],
                   edgecolors=C["fondo"], linewidths=0.9)
    ax.legend(loc="best")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid(False)
    return ax


# ===========================================================================
# CLASE 3: el paisaje de la loss
# ===========================================================================

def superficie_de_loss(loss_fn, rango_a=(-2, 4), rango_b=(-2, 4), n=90,
                       trayectoria=None, modo="ambos", titulo=None,
                       nombre_a="a  (pendiente)", nombre_b="b  (ordenada)",
                       optimo=None, escala_log=False, fig=None):
    """
    El paisaje de la clase 3: para cada combinación de perillas (a, b), qué tan
    mal la estás dibujando. Claro = fondo del valle, rojo = ladera alta.

        g.superficie_de_loss(lambda a, b: ((a*x + b - y)**2).mean(),
                             trayectoria=historial_de_pasos)

    Parámetros
    ----------
    loss_fn : callable loss(a, b) -> número. No hace falta que sea vectorizada.
    trayectoria : lista de (a, b), el rastro del descenso. Se dibuja en violeta
                  (color de las perillas) con puntitos, porque LA ANIMACIÓN ES
                  EL CONTENIDO: cada punto es un paso cuesta abajo.
    modo : "contorno" (el mapa), "3d" (el paisaje), o "ambos" lado a lado.
    optimo : (a, b) del mínimo, si lo conocés, para marcarlo con una estrella.

    Devuelve (fig, ejes).
    """
    a_vals = np.linspace(rango_a[0], rango_a[1], n)
    b_vals = np.linspace(rango_b[0], rango_b[1], n)
    A, B = np.meshgrid(a_vals, b_vals)

    # Evaluamos punto por punto: lento pero clarísimo, y n=90 tarda nada.
    Z = np.empty_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            Z[i, j] = float(loss_fn(A[i, j], B[i, j]))
    if escala_log:
        Z = np.log10(np.maximum(Z, 1e-12))

    if modo == "ambos":
        fig = fig or plt.figure(figsize=(12.5, 5.2))
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2, projection="3d")
        ejes = (ax1, ax2)
    elif modo == "3d":
        fig = fig or plt.figure(figsize=(7.2, 5.6))
        ax2 = fig.add_subplot(1, 1, 1, projection="3d")
        ax1, ejes = None, (ax2,)
    else:
        fig = fig or plt.figure(figsize=(7.0, 5.4))
        ax1 = fig.add_subplot(1, 1, 1)
        ax2, ejes = None, (ax1,)

    etiqueta_z = "log₁₀(loss)" if escala_log else "loss"

    # --- el mapa (contornos rellenos, tipo carta topográfica) ---
    if ax1 is not None:
        relleno = ax1.contourf(A, B, Z, levels=28, cmap=CMAPS["loss"], zorder=1)
        ax1.contour(A, B, Z, levels=14, colors=[C["tinta_3"]],
                    linewidths=0.6, alpha=0.6, zorder=2)
        cb = fig.colorbar(relleno, ax=ax1, shrink=0.9, pad=0.02)
        cb.set_label(etiqueta_z, color=C["tinta_2"])
        cb.outline.set_edgecolor(C["borde"])
        ax1.set_xlabel(nombre_a)
        ax1.set_ylabel(nombre_b)
        ax1.set_title("El mapa de las perillas")
        ax1.grid(False)

    # --- el paisaje 3D ---
    if ax2 is not None:
        ax2.plot_surface(A, B, Z, cmap=CMAPS["loss"], linewidth=0,
                         antialiased=True, alpha=0.94, rstride=2, cstride=2)
        ax2.set_xlabel(nombre_a, labelpad=8)
        ax2.set_ylabel(nombre_b, labelpad=8)
        ax2.set_zlabel(etiqueta_z, labelpad=6)
        ax2.set_title("El mismo paisaje, en relieve")
        ax2.view_init(elev=32, azim=-125)
        ax2.set_facecolor(C["fondo"])
        for pane in (ax2.xaxis, ax2.yaxis, ax2.zaxis):
            pane.pane.set_facecolor(C["fondo"])
            pane.pane.set_edgecolor(C["borde"])
        ax2.grid(True, color=C["grilla"])

    # --- la trayectoria del descenso ---
    if trayectoria is not None and len(trayectoria) > 0:
        tray = _a_numpy(trayectoria)
        ta, tb = tray[:, 0], tray[:, 1]
        if ax1 is not None:
            ax1.plot(ta, tb, color=C["parametro"], linewidth=1.6, alpha=0.9, zorder=5)
            ax1.scatter(ta, tb, s=16, color=C["parametro"], zorder=6,
                        edgecolors=C["fondo"], linewidths=0.5)
            ax1.scatter([ta[0]], [tb[0]], s=110, color=C["parametro"], zorder=7,
                        marker="o", edgecolors=C["fondo"], linewidths=1.6,
                        label="dónde soltamos la pelota")
            ax1.scatter([ta[-1]], [tb[-1]], s=150, color=C["acento"], zorder=7,
                        marker="X", edgecolors=C["fondo"], linewidths=1.4,
                        label=f"dónde terminó ({len(tray)} pasos)")
            ax1.legend(loc="best")
        if ax2 is not None:
            tz = np.array([float(loss_fn(a, b)) for a, b in zip(ta, tb)])
            if escala_log:
                tz = np.log10(np.maximum(tz, 1e-12))
            ax2.plot(ta, tb, tz, color=C["parametro"], linewidth=2.2, zorder=10)

    if optimo is not None and ax1 is not None:
        ax1.scatter([optimo[0]], [optimo[1]], s=200, marker="*",
                    color=C["ok"], edgecolors=C["tinta"], linewidths=0.8,
                    zorder=8, label="el fondo del valle")
        ax1.legend(loc="best")

    if titulo:
        fig.suptitle(titulo)
    return fig, ejes


def plot_loss_1d(loss_fn, rango=(-3, 5), n=300, punto=None, paso_de_prueba=0.5,
                 ax=None, titulo=None, nombre_parametro="a"):
    """
    La versión unidimensional del paisaje: una parábola, un punto, y la recta
    que pasa por el punto y por el punto de al lado.

    Existe para que nadie tenga que haber estudiado cálculo. Achicá
    `paso_de_prueba` y mirá cómo la secante se va pegando a la curva: eso, y
    nada más que eso, es una derivada.
    """
    ax = _ejes(ax, titulo=titulo, xlabel=f"perilla «{nombre_parametro}»",
               ylabel="loss")
    xs = np.linspace(rango[0], rango[1], n)
    ys = np.array([float(loss_fn(v)) for v in xs])
    ax.plot(xs, ys, color=C["error"], linewidth=2.4, zorder=3, label="loss")

    if punto is not None:
        p = float(punto)
        lp = float(loss_fn(p))
        h = float(paso_de_prueba)
        # La pendiente medida con una resta. Todavía no la llamamos derivada.
        pendiente = (float(loss_fn(p + h)) - float(loss_fn(p - h))) / (2 * h)

        ancho = (rango[1] - rango[0]) * 0.22
        xr = np.array([p - ancho, p + ancho])
        ax.plot(xr, lp + pendiente * (xr - p), color=C["parametro"],
                linewidth=2.0, linestyle="--", zorder=4,
                label=f"pendiente medida = {pendiente:+.3f}")
        # los dos puntos de prueba
        ax.scatter([p - h, p + h], [loss_fn(p - h), loss_fn(p + h)], s=55,
                   color=C["val"], zorder=5, edgecolors=C["fondo"], linewidths=1.0,
                   label=f"pasitos de prueba (±{h:g})")
        ax.scatter([p], [lp], s=150, color=C["parametro"], zorder=6,
                   edgecolors=C["fondo"], linewidths=1.5, label="dónde estoy")
        # La flecha de hacia dónde conviene moverse. Arranca separada del punto
        # y el cartel va POR ENCIMA de la flecha, para no taparle la bolita.
        alto = (max(ys) - min(ys))
        largo = ancho * 0.55 * (-1 if pendiente > 0 else 1)
        desde = p + largo * 0.18
        y_flecha = lp + alto * 0.09          # arriba del punto: ahí no hay nada
        ax.annotate("", xy=(p + largo, y_flecha), xytext=(desde, y_flecha),
                    arrowprops=dict(arrowstyle="-|>", color=C["acento"], lw=2.4))
        ax.text((desde + p + largo) / 2, y_flecha + alto * 0.03, "cuesta abajo",
                color=C["acento"], va="bottom", ha="center", fontweight="bold")
        ax.legend(loc="best")
    return ax


# ===========================================================================
# CLASE 4: entrenamiento
# ===========================================================================

def curvas_de_entrenamiento(historial=None, train=None, val=None, ax=None,
                            titulo="Cómo fue bajando la loss",
                            xlabel="época", ylabel="loss",
                            escala_log=False, marcar_mejor=True,
                            etiqueta_train="entrenamiento (lo que el modelo vio)",
                            etiqueta_val="validación (lo que NUNCA vio)"):
    """
    Las dos curvas de la clase 4. Azul lo que el modelo vio; NARANJA lo que no.

    Cuando la naranja deja de bajar y empieza a subir mientras la azul sigue
    bajando, eso tiene nombre: sobreajuste. El modelo dejó de dibujar la forma
    y empezó a calcar las manchitas de tu muestra.

        g.curvas_de_entrenamiento(historial)          # objeto Historial
        g.curvas_de_entrenamiento(train=[...], val=[...])
    """
    if historial is not None:
        train = getattr(historial, "train", None) or historial.get("train")
        val = getattr(historial, "val", None)
        if val is None and isinstance(historial, dict):
            val = historial.get("val")
    train = _a_numpy(train)
    val = _a_numpy(val) if val is not None and len(val) else None

    ax = _ejes(ax, titulo=titulo, xlabel=xlabel, ylabel=ylabel)
    epocas = np.arange(1, len(train) + 1)
    ax.plot(epocas, train, color=C["modelo"], linewidth=2.4,
            label=etiqueta_train, zorder=4)
    if val is not None:
        ax.plot(np.arange(1, len(val) + 1), val, color=C["val"], linewidth=2.4,
                label=etiqueta_val, zorder=4)
        if marcar_mejor and len(val) > 1:
            i = int(np.argmin(val))
            ax.scatter([i + 1], [val[i]], s=150, marker="v", color=C["ok"],
                       zorder=6, edgecolors=C["fondo"], linewidths=1.2,
                       label=f"mejor validación (época {i + 1})")
            ax.axvline(i + 1, color=C["ok"], linestyle=":", linewidth=1.6, zorder=2)
    if escala_log:
        ax.set_yscale("log")
    ax.legend(loc="best")
    return ax


# ===========================================================================
# CLASE 9-10: evaluación
# ===========================================================================

def matriz_de_confusion(y_true, y_pred, etiquetas=None, ax=None,
                        titulo="Matriz de confusión", normalizar=False,
                        nombre_positivo=None):
    """
    La matriz de confusión, con los números Y su traducción al castellano.

    Regla de la casa: prohibido reportar una métrica sin poder decirla en voz
    alta. Si es binaria, esta función imprime debajo las frases del tipo
    "de cada 100 que el modelo llamó X, N lo eran de verdad".

        g.matriz_de_confusion(y_true, y_pred,
                              etiquetas=["no menciona protesta", "menciona protesta"])

    Devuelve el `ax`. Las métricas en texto las conseguís con `frase_de_metricas`.
    """
    y_true = _a_numpy(y_true).astype(int).ravel()
    y_pred = _a_numpy(y_pred).astype(int).ravel()
    clases = np.unique(np.concatenate([y_true, y_pred]))
    k = len(clases)
    if etiquetas is None:
        etiquetas = [str(c) for c in clases]

    M = np.zeros((k, k), dtype=int)
    for verdadero, predicho in zip(y_true, y_pred):
        M[np.searchsorted(clases, verdadero), np.searchsorted(clases, predicho)] += 1

    mostrar = M / np.maximum(M.sum(axis=1, keepdims=True), 1) if normalizar else M

    # El ancho tiene que contemplar las etiquetas: los casilleros se rotulan EN EL
    # PROBLEMA SUSTANTIVO ("menciona protesta"), no con 0 y 1, así que son largas.
    largo_etiqueta = max(len(str(e)) for e in etiquetas)
    ax = _ejes(ax, ancho=2.6 + 1.5 * k + 0.085 * largo_etiqueta,
               alto=2.4 + 1.35 * k + 0.03 * largo_etiqueta, titulo=titulo)
    im = ax.imshow(mostrar, cmap=CMAPS["conteo"], vmin=0,
                   vmax=mostrar.max() if mostrar.max() > 0 else 1)
    ax.set_xticks(range(k), etiquetas, rotation=18, ha="right")
    ax.set_yticks(range(k), etiquetas)
    ax.set_xlabel("lo que dijo el modelo", labelpad=8)
    ax.set_ylabel("lo que era en realidad", labelpad=8)
    ax.grid(False)

    umbral = mostrar.max() * 0.55 if mostrar.max() > 0 else 1
    for i in range(k):
        for j in range(k):
            valor = f"{mostrar[i, j]:.0%}" if normalizar else f"{M[i, j]:,}"
            correcto = (i == j)
            ax.text(j, i, valor, ha="center", va="center",
                    fontsize=matplotlib.rcParams["font.size"] * 1.25,
                    fontweight="bold",
                    color=(C["fondo"] if mostrar[i, j] > umbral
                           else (C["ok"] if correcto else C["error"])))

    # bordes verdes en la diagonal (aciertos)
    for i in range(k):
        ax.add_patch(plt.Rectangle((i - 0.5, i - 0.5), 1, 1, fill=False,
                                   edgecolor=C["ok"], linewidth=2.2, zorder=5))
    ax.figure.colorbar(im, ax=ax, shrink=0.62, pad=0.04, aspect=16,
                       label="casos" if not normalizar else "proporción de la fila")

    # Las métricas van DEBAJO del eje, no adentro: un cartel encima de la matriz
    # siempre termina tapando justo el casillero del que estás hablando.
    if k == 2 and nombre_positivo:
        m = metricas_binarias(y_true, y_pred)
        ax.set_xlabel(f"lo que dijo el modelo\n\n"
                      f"precisión {m['precision']:.0%}  ·  recall {m['recall']:.0%}"
                      f"  ·  F1 {m['f1']:.2f}", labelpad=8)
    return ax


def metricas_binarias(y_true, y_pred) -> dict:
    """
    Las cuatro métricas de siempre, calculadas a mano para que se vea de dónde
    salen. Devuelve un diccionario con vp, fp, vn, fn, accuracy, precision,
    recall, f1 y prevalencia.

    >>> m = metricas_binarias([1, 1, 0, 0], [1, 0, 0, 0])
    >>> m["vp"], m["fn"], round(m["recall"], 2)
    (1, 1, 0.5)
    """
    y_true = _a_numpy(y_true).astype(int).ravel()
    y_pred = _a_numpy(y_pred).astype(int).ravel()
    vp = int(np.sum((y_true == 1) & (y_pred == 1)))   # verdaderos positivos
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))   # falsos positivos
    vn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    n = max(vp + fp + vn + fn, 1)
    precision = vp / (vp + fp) if (vp + fp) else 0.0
    recall = vp / (vp + fn) if (vp + fn) else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
    return {"vp": vp, "fp": fp, "vn": vn, "fn": fn,
            "accuracy": (vp + vn) / n, "precision": precision,
            "recall": recall, "f1": f1, "prevalencia": (vp + fn) / n}


def frase_de_metricas(y_true, y_pred, fenomeno="casos que mencionan protesta",
                      imprimir: bool = True) -> str:
    """
    Traduce las métricas a castellano llano. Si no podés decir esto en voz alta,
    no entendiste tu propio resultado (y el revisor 2 lo va a notar).

        g.frase_de_metricas(y_true, y_pred, fenomeno="titulares con protesta")
    """
    m = metricas_binarias(y_true, y_pred)
    lineas = [
        f"De cada 100 casos que el modelo marcó como «{fenomeno}», "
        f"{m['precision'] * 100:.0f} lo eran de verdad.  (precisión = {m['precision']:.2f})",
        f"De cada 100 casos que realmente eran «{fenomeno}», el modelo encontró "
        f"{m['recall'] * 100:.0f}.  (recall = {m['recall']:.2f})",
        f"F1 = {m['f1']:.2f} (el promedio armónico de las dos de arriba).",
        f"Acertó {m['accuracy'] * 100:.0f}% de las veces, pero ojo: el fenómeno "
        f"aparece en el {m['prevalencia'] * 100:.0f}% de los casos, así que "
        f"decir siempre «no» ya acertaría el {(1 - m['prevalencia']) * 100:.0f}%.",
    ]
    texto = "\n".join(lineas)
    if imprimir:
        print(texto)
    return texto


# ===========================================================================
# CLASE 6: embeddings
# ===========================================================================

def proyeccion_de_embeddings(vectores, palabras, ax=None,
                             titulo="El mapa donde viven las palabras",
                             resaltar=None, colores=None, grupos=None,
                             max_etiquetas=70, anotar_todo=False):
    """
    Proyecta vectores de muchas dimensiones a un plano y los dibuja con su
    palabra al lado. Si los vectores ya son 2D, no los toca.

    La reducción es un PCA hecho a mano con numpy (tres líneas: centrar, SVD,
    proyectar). Sin sklearn, para que se pueda leer.

    ADVERTENCIA PEDAGÓGICA que conviene decir en el aula: esto es una SOMBRA.
    El espacio real tiene 300 dimensiones y estamos mirando 2. Dos palabras
    pueden verse pegadas acá y estar lejísimos en el espacio de verdad.

    Parámetros
    ----------
    vectores : (n, d) array o tensor
    palabras : lista de n strings
    resaltar : lista de palabras a pintar con el color de acento y etiqueta grande
    grupos : lista de n etiquetas de grupo (ej. el partido), para colorear
    """
    V = _a_numpy(vectores).astype(float)
    palabras = list(palabras)

    if V.shape[1] > 2:
        centrado = V - V.mean(axis=0)
        # SVD: las dos primeras direcciones de máxima variación.
        _, s, Vt = np.linalg.svd(centrado, full_matrices=False)
        P = centrado @ Vt[:2].T
        var = (s ** 2) / np.sum(s ** 2)
        subtitulo = (f"proyección PCA · estas 2 dimensiones muestran el "
                     f"{(var[0] + var[1]) * 100:.0f}% de la variación")
    else:
        P = V[:, :2]
        subtitulo = None

    ax = _ejes(ax, ancho=9, alto=6.5, titulo=titulo)
    resaltar = set(resaltar or [])

    if grupos is not None:
        nombres = list(dict.fromkeys(grupos))
        paleta_grupos = colores or [C["modelo"], C["error"], C["ok"], C["val"],
                                    C["parametro"], C["acento"], C["tinta_3"]]
        for i, nombre in enumerate(nombres):
            m = np.array([gr == nombre for gr in grupos])
            ax.scatter(P[m, 0], P[m, 1], s=44, label=str(nombre), zorder=3,
                       color=paleta_grupos[i % len(paleta_grupos)],
                       edgecolors=C["fondo"], linewidths=0.7, alpha=0.9)
        ax.legend(loc="best")
    else:
        ax.scatter(P[:, 0], P[:, 1], s=40, color=C["datos"], zorder=3,
                   alpha=0.75, edgecolors=C["fondo"], linewidths=0.6)

    if resaltar:
        m = np.array([p in resaltar for p in palabras])
        if m.any():
            ax.scatter(P[m, 0], P[m, 1], s=160, color=C["acento"], zorder=6,
                       edgecolors=C["fondo"], linewidths=1.6)

    # --- etiquetas sin encimarse: greedy, salteando las que caen muy cerca ---
    # Una etiqueta de texto es MUCHO más ancha que alta, así que la zona de
    # exclusión también: si la medimos con un círculo, "diputado" y "banca"
    # terminan encimadas aunque sus puntos estén "lejos".
    rango = max(float(np.ptp(P[:, 0])), float(np.ptp(P[:, 1])), 1e-9)
    sep_x = rango * (0.0 if anotar_todo else 0.09)
    sep_y = rango * (0.0 if anotar_todo else 0.038)
    puestas = []
    orden = sorted(range(len(palabras)),
                   key=lambda i: (palabras[i] not in resaltar))  # primero las resaltadas
    for i in orden:
        if len(puestas) >= max_etiquetas and palabras[i] not in resaltar:
            break
        p = P[i]
        if any(abs(p[0] - q[0]) < sep_x and abs(p[1] - q[1]) < sep_y
               for q in puestas):
            continue
        es_clave = palabras[i] in resaltar
        ax.annotate(
            palabras[i], (p[0], p[1]), textcoords="offset points", xytext=(6, 5),
            fontsize=matplotlib.rcParams["font.size"] * (1.05 if es_clave else 0.85),
            color=C["acento"] if es_clave else C["tinta_2"],
            fontweight="bold" if es_clave else "normal", zorder=7,
        )
        puestas.append(p)

    ax.set_xlabel("dimensión 1" + (f"\n{subtitulo}" if subtitulo else ""))
    ax.set_ylabel("dimensión 2")
    ax.margins(0.13, 0.09)   # aire, para que las etiquetas del borde no se corten
    return ax


# ===========================================================================
# CLASE 7: atención
# ===========================================================================

def mapa_de_atencion(pesos, tokens, tokens_columna=None, ax=None,
                     titulo="Quién mira a quién", mascara_causal=False,
                     anotar=None, cabeza=None):
    """
    La matriz de atención como mapa de calor. Cada FILA es una palabra
    preguntando; cada COLUMNA, una palabra siendo mirada.

    La confusión número uno al leer estos gráficos, y la razón de que esta
    función imprima las sumas: LAS FILAS SUMAN 1, LAS COLUMNAS NO SUMAN NADA.
    Que una palabra reparta todo su 100% no dice nada sobre cuánta atención
    recibe ella.

        g.mapa_de_atencion(pesos, tokens, mascara_causal=True)

    Parámetros
    ----------
    pesos : matriz (n, m) con los pesos de atención
    tokens : las n palabras de las filas
    tokens_columna : las m de las columnas (por defecto, las mismas)
    mascara_causal : dibuja en gris el triángulo del futuro (lo que no se puede mirar)
    anotar : mostrar el número en cada celda (por defecto sí si la matriz es chica)
    """
    W = _a_numpy(pesos).astype(float)
    if W.ndim == 3:  # (cabezas, n, m) -> elegimos una
        W = W[cabeza or 0]
    tokens = list(tokens)
    tokens_columna = list(tokens_columna) if tokens_columna is not None else tokens
    n, m = W.shape

    ax = _ejes(ax, ancho=max(5.5, 0.52 * m + 3.2), alto=max(4.6, 0.46 * n + 2.6),
               titulo=titulo)
    im = ax.imshow(W, cmap=CMAPS["atencion"], vmin=0, vmax=max(W.max(), 1e-9),
                   aspect="auto")

    if mascara_causal:
        futuro = np.triu(np.ones((n, m)), k=1)
        ax.imshow(np.ma.masked_where(futuro == 0, futuro), cmap="Greys",
                  vmin=0, vmax=1.6, alpha=0.5, aspect="auto", zorder=2)

    ax.set_xticks(range(m), tokens_columna, rotation=52, ha="right")
    ax.set_yticks(range(n), tokens)
    # La aclaración va en el eje, NO adentro del mapa: un cartel flotando encima
    # de un heatmap siempre termina tapando justo la celda que querías mostrar.
    ax.set_xlabel("...mira a esta palabra\n"
                  "(cada fila suma 1,00 · las columnas no suman nada)", labelpad=8)
    ax.set_ylabel("esta palabra...", labelpad=8)
    ax.grid(False)

    if anotar is None:
        anotar = (n * m) <= 144
    if anotar:
        for i in range(n):
            for j in range(m):
                if mascara_causal and j > i:
                    continue
                if W[i, j] < 0.005:
                    continue
                ax.text(j, i, f"{W[i, j]:.2f}".lstrip("0"), ha="center", va="center",
                        fontsize=matplotlib.rcParams["font.size"] * 0.72,
                        color=C["fondo"] if W[i, j] > W.max() * 0.55 else C["tinta_2"])

    cb = ax.figure.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
    cb.set_label("cuánta atención le presta", color=C["tinta_2"])
    return ax


# ===========================================================================
# CLASE 5: imágenes y filtros
# ===========================================================================

def grilla_de_filtros(filtros, ncols=8, titulo="Lo que aprendió a buscar cada filtro",
                      titulos=None, fig=None, escala=1.0):
    """
    La grilla de filtros de una CNN. Azul = negativo, blanco = cero,
    rojo = positivo, con la escala centrada en cero y compartida por todos, que
    es la única forma de poder compararlos entre sí.

    Mismo criterio de color que la viz kernel-deslizante.html de la clase 5.

        g.grilla_de_filtros(modelo.conv1.weight)     # (n, canales, alto, ancho)

    Acepta (n, h, w) o (n, c, h, w) (en cuyo caso promedia los canales) o
    directamente un tensor de PyTorch.
    """
    W = _a_numpy(filtros).astype(float)
    if W.ndim == 4:
        W = W.mean(axis=1)   # promediamos los canales de entrada para poder dibujarlo
    if W.ndim == 2:
        W = W[None, ...]
    n = W.shape[0]
    ncols = min(ncols, n)
    nfilas = int(np.ceil(n / ncols))

    lim = float(np.abs(W).max()) or 1.0
    fig = fig or plt.figure(figsize=(1.35 * ncols * escala + 1.2,
                                     1.45 * nfilas * escala + 1.1))
    ejes = fig.subplots(nfilas, ncols, squeeze=False)
    for k in range(nfilas * ncols):
        ax = ejes[k // ncols][k % ncols]
        ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
        if k >= n:
            ax.set_visible(False)
            continue
        im = ax.imshow(W[k], cmap=CMAPS["filtro"], vmin=-lim, vmax=lim)
        ax.set_title(titulos[k] if titulos else f"#{k}",
                     fontsize=matplotlib.rcParams["font.size"] * 0.8,
                     color=C["tinta_2"], pad=4)
        for lado in ax.spines.values():
            lado.set_visible(True)
            lado.set_color(C["borde"])

    cb = fig.colorbar(im, ax=ejes, shrink=0.7, pad=0.02, aspect=18)
    cb.set_label("peso del filtro  (azul −  ·  blanco 0  ·  rojo +)",
                 color=C["tinta_2"])
    if titulo:
        fig.suptitle(titulo)
    return fig, ejes


def mostrar_imagenes(imagenes, etiquetas=None, ncols=8, titulo=None,
                     cmap="gray", predicciones=None, fig=None):
    """
    Una grilla de imágenes con su etiqueta. Si le pasás `predicciones`, pinta el
    título de VERDE cuando acertó y de ROJO cuando erró: el análisis de errores
    de la clase 5 se hace mirando, no leyendo una tabla.
    """
    X = _a_numpy(imagenes).astype(float)
    if X.ndim == 4:                     # (n, c, h, w) -> (n, h, w)
        X = X[:, 0] if X.shape[1] in (1, 3) and X.shape[1] != 3 else X.mean(axis=1)
    n = X.shape[0]
    ncols = min(ncols, n)
    nfilas = int(np.ceil(n / ncols))

    fig = fig or plt.figure(figsize=(1.35 * ncols + 0.6, 1.55 * nfilas + 0.8))
    ejes = fig.subplots(nfilas, ncols, squeeze=False)
    for k in range(nfilas * ncols):
        ax = ejes[k // ncols][k % ncols]
        ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
        if k >= n:
            ax.set_visible(False)
            continue
        ax.imshow(X[k], cmap=cmap)
        if etiquetas is not None:
            if predicciones is not None:
                bien = etiquetas[k] == predicciones[k]
                texto = (f"{etiquetas[k]}" if bien
                         else f"{predicciones[k]}\n(era {etiquetas[k]})")
                color = C["ok"] if bien else C["error"]
            else:
                texto, color = str(etiquetas[k]), C["tinta_2"]
            ax.set_title(texto, fontsize=matplotlib.rcParams["font.size"] * 0.78,
                         color=color, pad=4)
        for lado in ax.spines.values():
            lado.set_visible(True)
            lado.set_color(C["borde"])
    if titulo:
        fig.suptitle(titulo)
    return fig, ejes


if __name__ == "__main__":
    import doctest
    fallas, corridos = doctest.testmod()
    print(f"doctests: {corridos - fallas}/{corridos} OK")
