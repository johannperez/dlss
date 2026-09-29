"""Corre DE VERDAD los experimentos de la clase 5 y escribe `datos-experimentos.js`.

Ninguno de los numeros que muestran las slides ni las visualizaciones de esta
clase esta inventado ni "estimado": todos salen de correr aca el mismo codigo
que corre el notebook, con la misma semilla (1983) y la misma configuracion.

    PYTHONPATH=_shared python3 clases/05-imagenes-y-convoluciones/medir-experimentos.py
    (agrega --rapido para saltear la parte E, la de las otras semillas)

Si tocas el notebook, volve a correr esto. Si no, las slides y el notebook
empiezan a contar cosas distintas -- que es exactamente lo que este curso le
pide a los demas que no hagan.

SOBRE LA REPRODUCIBILIDAD, dicho con cuidado: con la semilla fija, la corrida
es determinista EN LA MISMA MAQUINA Y CON LAS MISMAS VERSIONES de las
librerias. Con otra version de torch/numpy (u otro procesador) los numeros
cambian un poco: unas decimas en FashionMNIST, un par de puntos en los casos
mas sensibles (la CNN con la foto corrida 6 pixeles, el mini-caso del
archivo). Por eso el JSON guarda las versiones con que se midio ("entorno") y
la parte E mide cuanto se mueven los numeros si solo cambia la semilla.

Que mide:
  A) EL BARAJADO (se vuelve a entrenar con los pixeles permutados)
     1. red densa sobre las imagenes normales   -> exactitud
     2. red densa sobre los pixeles BARAJADOS   -> exactitud (sale igual)
     3. CNN sobre las imagenes normales         -> exactitud
     4. CNN sobre los pixeles BARAJADOS         -> exactitud (baja)
  B) EL CORRIMIENTO (se entrena con imagenes centradas y se prueba con la foto
     corrida unos pixeles: NO se vuelve a entrenar). Es el gancho de la clase.
     la densa se desploma; la CNN aguanta.
  C) EL ARCHIVO VISUAL sintetico (multitud / no multitud) y el analisis de
     errores: la exactitud global y la exactitud por subgrupo.
  D) LOS EXPERIMENTOS DEL CUESTIONARIO (6 pasadas, para que no tarde): una
     permutacion DISTINTA por imagen (pregunta 3c), la foto centrada en un
     lienzo de 56x56 y probada en la esquina (4a) y la foto rotada 90 grados
     (4b, sin reentrenar).
  E) LA MISMA CUENTA CON OTRAS SEMILLAS: cuanto se mueven los numeros de A y
     B (semillas 1984-1987) y los de C (semillas 1983-1994, que es barato) si
     solo cambia el azar del entrenamiento. Los datos y la permutacion quedan
     fijos.

Que exporta ademas, para que las viz dibujen datos reales y no dibujitos:
  - un punado de imagenes de muestra (28x28, 0-255)
  - la permutacion exacta que usa el barajado
  - los filtros de 3x3 que la CNN aprendio sola
  - unas imagenes esquematicas sinteticas (afiche, diario, multitud, reja)
    generadas con numpy, para la viz del filtro deslizante
"""
import datetime
import json
import os
import pathlib
import platform
import sys
import time

import numpy as np
import torch
import torch.nn as nn

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(RAIZ / "_shared"))
sys.path.insert(0, str(RAIZ / "datos"))
os.environ.setdefault("DLSS_RAIZ", str(RAIZ))

from ssdl import utils  # noqa: E402

SEMILLA = 1983
N_TRAIN, N_TEST, EPOCAS, LR, LOTE = 12000, 4000, 12, 2e-3, 64

# el archivo visual sintetico de la segunda mitad del notebook
LADO_ARCHIVO = 32
ARCH_TRAIN, ARCH_TEST, ARCH_EPOCAS = 400, 400, 10


# ---------------------------------------------------------------------------
# 0. Los datos. Con red o sin red, la clase corre igual.
# ---------------------------------------------------------------------------

def imagenes_sinteticas(n, semilla=0):
    """Plan B sin red: cuatro clases de figuras de 28x28, hechas con numpy."""
    rng = np.random.default_rng(semilla)
    X = np.zeros((n, 28, 28), dtype=np.uint8)
    y = rng.integers(0, 4, size=n).astype(np.int64)
    for i in range(n):
        f, c = rng.integers(4, 12), rng.integers(4, 12)
        alto, ancho = rng.integers(9, 16), rng.integers(9, 16)
        img = np.zeros((28, 28))
        if y[i] == 0:                                   # barras verticales
            img[f:f + alto, c:c + ancho:3] = 1.0
        elif y[i] == 1:                                 # barras horizontales
            img[f:f + alto:3, c:c + ancho] = 1.0
        elif y[i] == 2:                                 # bloque lleno
            img[f:f + alto, c:c + ancho] = 1.0
        else:                                           # marco hueco
            img[f:f + alto, c:c + ancho] = 1.0
            img[f + 2:f + alto - 2, c + 2:c + ancho - 2] = 0.0
        img = np.clip(img * 200 + rng.normal(0, 12, (28, 28)) + 20, 0, 255)
        X[i] = img.astype(np.uint8)
    return X, y


def traer_datos():
    """FashionMNIST si se puede; si no, las figuras sinteticas."""
    try:
        import descargar
        tr = descargar.fashion_mnist("train")
        te = descargar.fashion_mnist("t10k")
        if tr is not None and te is not None:
            nombres = descargar.ETIQUETAS_FASHION
            return tr, te, nombres, "FashionMNIST"
    except Exception as e:                              # noqa: BLE001
        print(f"  [!] FashionMNIST no disponible ({type(e).__name__}). Voy a lo sintetico.")
    nombres = ["barras verticales", "barras horizontales", "bloque", "marco"]
    return (imagenes_sinteticas(N_TRAIN, 1), imagenes_sinteticas(N_TEST, 2),
            nombres, "figuras sinteticas")


# ---------------------------------------------------------------------------
# 1. Los dos modelos
# ---------------------------------------------------------------------------

def red_densa(n_clases):
    """La misma FORMA de maquina que la de la clase 4 (dos capas densas con un
    doblez en el medio), comiendo pixeles: primero se aplana la grilla."""
    return nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 64), nn.ReLU(),
        nn.Linear(64, n_clases),
    )


def red_convolucional(n_clases):
    """Mira de a 3x3 tres veces; al final se queda con el maximo de cada mapa
    (";aparecio esta pieza en algun lado?") y recien ahi decide."""
    return nn.Sequential(
        nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(),
        nn.AdaptiveMaxPool2d(1), nn.Flatten(),
        nn.Linear(64, n_clases),
    )


def correr(X, d):
    """La misma imagen, corrida `d` pixeles a la derecha. Lo que entra por la
    izquierda es fondo (negro), no el otro borde: una foto corrida no da la
    vuelta."""
    if d == 0:
        return X
    Y = torch.zeros_like(X)
    Y[:, :, :, d:] = X[:, :, :, :-d]
    return Y


def entrenar(modelo, Xtr, ytr, Xte, yte, epocas=EPOCAS, lr=LR, lote=LOTE,
             semilla=SEMILLA):
    torch.manual_seed(semilla)
    crit = nn.CrossEntropyLoss()
    opt = torch.optim.Adam(modelo.parameters(), lr=lr)
    n = len(Xtr)
    g = torch.Generator().manual_seed(semilla)
    t0 = time.time()
    for _ in range(epocas):
        orden = torch.randperm(n, generator=g)
        for i in range(0, n, lote):
            idx = orden[i:i + lote]
            opt.zero_grad()
            crit(modelo(Xtr[idx]), ytr[idx]).backward()
            opt.step()
    modelo.eval()
    with torch.no_grad():
        acc = (modelo(Xte).argmax(1) == yte).float().mean().item()
    return acc, time.time() - t0


# ---------------------------------------------------------------------------
# 2. Las imagenes esquematicas para la viz del filtro
# ---------------------------------------------------------------------------

def esquemas_sinteticos():
    """Cuatro escenas de 28x28 dibujadas con numpy. Sinteticas y rotuladas."""
    rng = np.random.default_rng(7)
    out = {}

    # --- afiche de campana: fondo claro, letras (palotes verticales), franja ---
    a = np.full((28, 28), 40.0)
    a[3:25, 3:25] = 215.0                       # el papel
    for c in (6, 9, 12, 16, 19, 22):            # los palotes de las letras
        a[7:14, c:c + 2] = 45.0
    a[17:21, 5:23] = 90.0                       # la franja de abajo
    out["afiche"] = a

    # --- fragmento de pagina de diario: titulo + dos columnas de renglones ---
    d = np.full((28, 28), 230.0)
    d[2:5, 3:25] = 40.0                         # el titulo
    for f in range(8, 26, 3):
        d[f:f + 1, 3:12] = 55.0                 # columna izquierda
        d[f:f + 1, 15:25] = 55.0                # columna derecha
    out["diario"] = d

    # --- multitud: cabecitas sobre un fondo con degrade ---
    m = np.tile(np.linspace(200, 120, 28), (28, 1))
    yy, xx = np.mgrid[0:28, 0:28]
    for _ in range(38):
        cy, cx = rng.integers(6, 27), rng.integers(1, 27)
        m[(yy - cy) ** 2 + (xx - cx) ** 2 <= 1.6] = rng.integers(25, 70)
    out["multitud"] = m

    # --- reja / ventana: una grilla, el caso donde todo son bordes ------------
    r = np.full((28, 28), 190.0)
    r[:, 4:6] = r[:, 12:14] = r[:, 20:22] = 35.0
    r[4:6, :] = r[13:15, :] = r[22:24, :] = 35.0
    out["reja"] = r

    # OJO CON LA CONVENCION. Arriba dibujamos "en papel": numero alto = claro.
    # FashionMNIST viene al reves (fondo 0 = negro, prenda 255 = clara) y todo el
    # material de la clase pinta con `Viz.paleta('grises')`, que va de papel a
    # tinta: numero ALTO = TINTA. Asi que invertimos aca, una sola vez, y todos
    # los consumidores (viz y slides) usan la misma regla sin excepciones.
    return {k: (255 - np.clip(v, 0, 255)).astype(np.uint8).tolist()
            for k, v in out.items()}


# ---------------------------------------------------------------------------
# 3. El archivo visual sintetico: multitud / no multitud
#    IDENTICO al del notebook (misma funcion, mismas semillas).
# ---------------------------------------------------------------------------

def _suavizar(img):
    """Un desenfoque 3x3. Las fotos de archivo no tienen bordes de bisturi."""
    L = img.shape[0]
    k = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], float)
    k /= k.sum()
    p = np.pad(img, 1, mode="edge")
    out = np.zeros_like(img)
    for j in range(3):
        for i in range(3):
            out += k[j, i] * p[j:j + L, i:i + L]
    return out


def archivo_visual(n, semilla, lado=LADO_ARCHIVO, prop_follaje=0.34):
    """Un archivo fotografico SINTETICO de 32x32 en escala de grises.

    Tres tipos de escena, dos etiquetas:
      - 'multitud'  (etiqueta 1): muchas cabecitas repartidas bajo el horizonte
      - 'edificio'  (etiqueta 0): un bloque grande con ventanas
      - 'follaje'   (etiqueta 0): racimos de manchitas -- copas de arboles

    'follaje' esta puesto A PROPOSITO: tiene la misma *textura* que una
    multitud y ninguna persona. Es el confundidor que hace que el analisis de
    errores del notebook diga algo. Pais ficticio, proceso generador conocido.
    """
    rng = np.random.default_rng(semilla)
    X = np.zeros((n, lado, lado))
    y = np.zeros(n, dtype=np.int64)
    tipo = []
    yy, xx = np.mgrid[0:lado, 0:lado]
    for k in range(n):
        base = rng.uniform(140, 205)
        img = np.tile(np.linspace(base, base - 40, lado), (lado, 1)).T
        r = rng.random()
        if k % 2 == 0:                                     # ---- multitud
            y[k] = 1
            tipo.append("multitud")
            hor = rng.integers(3, 18)
            img[hor:, :] = rng.uniform(110, 175)
            for _ in range(rng.integers(45, 120)):
                cy, cx = rng.integers(hor, lado - 1), rng.integers(0, lado)
                img[(yy - cy) ** 2 + (xx - cx) ** 2
                    <= rng.uniform(0.8, 2.0) ** 2] = rng.uniform(20, 90)
        elif r < prop_follaje:                             # ---- follaje
            y[k] = 0
            tipo.append("follaje")
            hor = rng.integers(3, 18)
            img[hor:, :] = rng.uniform(110, 175)
            for _ in range(rng.integers(2, 6)):
                by, bx = rng.integers(2, lado - 4), rng.integers(2, lado - 4)
                for _ in range(rng.integers(15, 40)):
                    cy = int(np.clip(by + rng.normal(0, 3.5), 0, lado - 1))
                    cx = int(np.clip(bx + rng.normal(0, 3.5), 0, lado - 1))
                    img[(yy - cy) ** 2 + (xx - cx) ** 2
                        <= rng.uniform(0.8, 2.0) ** 2] = rng.uniform(20, 90)
        else:                                              # ---- edificio
            y[k] = 0
            tipo.append("edificio")
            a, an = rng.integers(10, 20), rng.integers(12, 24)
            f0 = lado - a - rng.integers(0, 5)
            c0 = rng.integers(0, lado - an)
            img[f0:f0 + a, c0:c0 + an] = rng.uniform(60, 110)
            for fv in range(f0 + 2, f0 + a - 2, 4):
                for cv in range(c0 + 2, c0 + an - 2, 5):
                    img[fv:fv + 2, cv:cv + 3] = rng.uniform(170, 215)
        X[k] = np.clip(_suavizar(img) + rng.normal(0, 7, (lado, lado)), 0, 255)
    return X.astype(np.uint8), y, np.array(tipo)


# ---------------------------------------------------------------------------
# 4. Correrlo todo
# ---------------------------------------------------------------------------

def entorno():
    """Con que se midio. La semilla fija la corrida en ESTA combinacion."""
    return {"python": platform.python_version(), "torch": torch.__version__,
            "numpy": np.__version__, "plataforma": platform.platform(),
            "procesador": platform.machine(),
            "fecha": datetime.date.today().isoformat()}


def barajado_y_corrimiento(Xtr, ytr, Xte, yte, Xtr_b, Xte_b, n_clases, semilla,
                           verboso=True):
    """Partes A y B con una semilla dada (la del entrenamiento: inicializacion
    y orden de los lotes). Devuelve (res, corrimiento, entrenados)."""
    res, entrenados = {}, {}
    for nombre, constructor, datos_tr, datos_te in [
        ("densa_normal", red_densa, Xtr, Xte),
        ("densa_barajada", red_densa, Xtr_b, Xte_b),
        ("cnn_normal", red_convolucional, Xtr, Xte),
        ("cnn_barajada", red_convolucional, Xtr_b, Xte_b),
    ]:
        torch.manual_seed(semilla)
        modelo = constructor(n_clases)
        acc, seg = entrenar(modelo, datos_tr, ytr, datos_te, yte, semilla=semilla)
        params = utils.contar_parametros(modelo)
        res[nombre] = {"exactitud": round(acc * 100, 1), "parametros": params,
                       "segundos": round(seg, 1)}
        entrenados[nombre] = modelo
        if verboso:
            print(f"  {nombre:16s}  {acc*100:5.1f} %   ({params} perillas, {seg:.0f} s)")

    desplazamientos = [0, 1, 2, 3, 4, 6]
    corrimiento = {"pixeles": desplazamientos, "densa": [], "cnn": []}
    for clave, mod in [("densa", entrenados["densa_normal"]),
                       ("cnn", entrenados["cnn_normal"])]:
        mod.eval()
        for d in desplazamientos:
            with torch.no_grad():
                a = (mod(correr(Xte, d)).argmax(1) == yte).float().mean().item()
            corrimiento[clave].append(round(a * 100, 1))
    return res, corrimiento, entrenados


def mini_archivo(Xa_t, ya_t, Xv_t, yv, tv, semilla):
    """Parte C con una semilla dada: entrena la CNN y cuenta errores por tipo."""
    yv_t = torch.tensor(yv, dtype=torch.long)
    torch.manual_seed(semilla)
    mod_arch = red_convolucional(2)
    acc_a, seg_a = entrenar(mod_arch, Xa_t, ya_t, Xv_t, yv_t,
                            epocas=ARCH_EPOCAS, lote=32, semilla=semilla)
    with torch.no_grad():
        pred = mod_arch(Xv_t).argmax(1).numpy()
    por_tipo = {t: {"n": int((tv == t).sum()),
                    "exactitud": round(float((pred[tv == t] == yv[tv == t]).mean()) * 100, 1),
                    "errores": int(((pred != yv) & (tv == t)).sum())}
                for t in ["multitud", "follaje", "edificio"]}
    return {
        "n_train": ARCH_TRAIN, "n_test": ARCH_TEST, "epocas": ARCH_EPOCAS,
        "lado": LADO_ARCHIVO,
        "exactitud": round(acc_a * 100, 1), "segundos": round(seg_a, 1),
        "parametros": utils.contar_parametros(mod_arch),
        "por_tipo": por_tipo,
        "errores_totales": int((pred != yv).sum()),
    }


def exactitud(modelo, X, y):
    modelo.eval()
    with torch.no_grad():
        return round((modelo(X).argmax(1) == y).float().mean().item() * 100, 1)


def main():
    rapido = "--rapido" in sys.argv
    utils.fijar_semilla(SEMILLA)
    (Xtr_raw, ytr_raw), (Xte_raw, yte_raw), nombres, fuente = traer_datos()
    print(f"Datos: {fuente}  .  train {Xtr_raw.shape}  test {Xte_raw.shape}")
    ent = entorno()
    print(f"Entorno: python {ent['python']} . torch {ent['torch']} . numpy {ent['numpy']}"
          f" . {ent['plataforma']}")

    rng = np.random.default_rng(SEMILLA)
    itr = rng.choice(len(Xtr_raw), size=min(N_TRAIN, len(Xtr_raw)), replace=False)
    ite = rng.choice(len(Xte_raw), size=min(N_TEST, len(Xte_raw)), replace=False)

    Xtr = torch.tensor(Xtr_raw[itr] / 255.0, dtype=torch.float32).unsqueeze(1)
    ytr = torch.tensor(np.asarray(ytr_raw)[itr], dtype=torch.long)
    Xte = torch.tensor(Xte_raw[ite] / 255.0, dtype=torch.float32).unsqueeze(1)
    yte = torch.tensor(np.asarray(yte_raw)[ite], dtype=torch.long)
    n_clases = int(max(ytr.max().item(), yte.max().item())) + 1

    # LA permutacion: una sola, la misma para todas las imagenes.
    perm = np.random.default_rng(SEMILLA).permutation(28 * 28)
    tperm = torch.tensor(perm, dtype=torch.long)

    def barajar(X):
        return X.reshape(len(X), 1, -1)[:, :, tperm].reshape(len(X), 1, 28, 28)

    Xtr_b, Xte_b = barajar(Xtr), barajar(Xte)

    print("\nA) EL BARAJADO -- se vuelve a entrenar con los pixeles permutados")
    res, corrimiento, entrenados = barajado_y_corrimiento(
        Xtr, ytr, Xte, yte, Xtr_b, Xte_b, n_clases, SEMILLA)
    filtros = entrenados["cnn_normal"][0].weight.detach().numpy()[:, 0]   # (16,3,3)

    # --- B) el corrimiento: mismos modelos, la foto movida ------------------
    print("\nB) EL CORRIMIENTO -- mismos modelos, la foto corrida (sin reentrenar)")
    for clave in ("densa", "cnn"):
        print(f"  {clave:6s}  " + "  ".join(
            f"{d}px:{v:5.1f}%" for d, v in zip(corrimiento["pixeles"], corrimiento[clave])))

    # --- C) el archivo visual sintetico y el analisis de errores -------------
    print("\nC) EL ARCHIVO VISUAL sintetico (multitud / no multitud)")
    Xa, ya, ta = archivo_visual(ARCH_TRAIN, 11)
    Xv, yv, tv = archivo_visual(ARCH_TEST, 22)
    Xa_t = torch.tensor(Xa / 255.0, dtype=torch.float32).unsqueeze(1)
    ya_t = torch.tensor(ya, dtype=torch.long)
    Xv_t = torch.tensor(Xv / 255.0, dtype=torch.float32).unsqueeze(1)
    archivo = mini_archivo(Xa_t, ya_t, Xv_t, yv, tv, SEMILLA)
    print(f"  exactitud global {archivo['exactitud']:.1f} %  ({archivo['segundos']:.0f} s, "
          f"{archivo['errores_totales']} errores de {ARCH_TEST})")
    for t, d in archivo["por_tipo"].items():
        print(f"    {t:9s} n={d['n']:3d}  exactitud {d['exactitud']:5.1f} %  "
              f"({d['errores']} errores)")

    # --- D) los experimentos del cuestionario --------------------------------
    print("\nD) LOS EXPERIMENTOS DEL CUESTIONARIO (6 pasadas)")
    ep_c = 6

    def permutar_cada_una(X, semilla):
        """Una permutacion DISTINTA para cada imagen (pregunta 3c)."""
        g = np.random.default_rng(semilla)
        Xf = X.reshape(len(X), -1).numpy().copy()
        for k in range(len(Xf)):
            Xf[k] = Xf[k][g.permutation(28 * 28)]
        return torch.tensor(Xf).reshape(len(X), 1, 28, 28)

    Xtr_p, Xte_p = permutar_cada_una(Xtr, 1), permutar_cada_una(Xte, 2)
    torch.manual_seed(SEMILLA)
    m = red_densa(n_clases)
    acc_pd, _ = entrenar(m, Xtr_p, ytr, Xte_p, yte, epocas=ep_c)
    torch.manual_seed(SEMILLA)
    m = red_convolucional(n_clases)
    acc_pc, _ = entrenar(m, Xtr_p, ytr, Xte_p, yte, epocas=ep_c)
    print(f"  3c) permutacion distinta por imagen: densa {acc_pd*100:.1f} %  "
          f"CNN {acc_pc*100:.1f} %  (el azar es {100/n_clases:.0f} %)")

    def lienzo(X, f, c, lado=56):
        Y = torch.zeros(len(X), 1, lado, lado)
        Y[:, :, f:f + 28, c:c + 28] = X
        return Y

    Ctr, Cte = lienzo(Xtr, 14, 14), lienzo(Xte, 14, 14)
    esq_a, esq_b = lienzo(Xte, 0, 0), lienzo(Xte, 28, 28)
    torch.manual_seed(SEMILLA)
    m = red_convolucional(n_clases)
    acc_cc, _ = entrenar(m, Ctr, ytr, Cte, yte, epocas=ep_c)
    cnn_esq = [exactitud(m, esq_a, yte), exactitud(m, esq_b, yte)]
    torch.manual_seed(SEMILLA)
    m = nn.Sequential(nn.Flatten(), nn.Linear(56 * 56, 64), nn.ReLU(), nn.Linear(64, n_clases))
    acc_dc, _ = entrenar(m, Ctr, ytr, Cte, yte, epocas=ep_c)
    densa_esq = [exactitud(m, esq_a, yte), exactitud(m, esq_b, yte)]
    print(f"  4a) lienzo 56x56, centrada -> esquinas: CNN {acc_cc*100:.1f} -> "
          f"{cnn_esq[0]:.1f} / {cnn_esq[1]:.1f} ;  densa {acc_dc*100:.1f} -> "
          f"{densa_esq[0]:.1f} / {densa_esq[1]:.1f}")

    rot = exactitud(entrenados["cnn_normal"], torch.rot90(Xte, 1, (2, 3)), yte)
    print(f"  4b) la CNN de la parte A con la foto rotada 90 grados: "
          f"{res['cnn_normal']['exactitud']:.1f} -> {rot:.1f} %")
    cuestionario = {
        "epocas": ep_c,
        "permutacion_por_imagen": {"densa": round(acc_pd * 100, 1),
                                   "cnn": round(acc_pc * 100, 1),
                                   "azar": round(100 / n_clases, 1)},
        "lienzo_56": {"cnn_centrada": round(acc_cc * 100, 1),
                      "cnn_esquinas": cnn_esq,
                      "densa_centrada": round(acc_dc * 100, 1),
                      "densa_esquinas": densa_esq},
        "rotada_90": {"cnn_normal": res["cnn_normal"]["exactitud"], "cnn_rotada": rot},
    }

    # --- E) la misma cuenta con otras semillas -------------------------------
    otras = None
    if not rapido:
        print("\nE) OTRAS SEMILLAS -- mismos datos, mismo barajado; cambia solo el azar"
              " del entrenamiento")
        otras = {"semillas": [SEMILLA], "densa_normal": [res["densa_normal"]["exactitud"]],
                 "densa_barajada": [res["densa_barajada"]["exactitud"]],
                 "cnn_normal": [res["cnn_normal"]["exactitud"]],
                 "cnn_barajada": [res["cnn_barajada"]["exactitud"]],
                 "densa_3px": [corrimiento["densa"][3]], "cnn_3px": [corrimiento["cnn"][3]],
                 "densa_6px": [corrimiento["densa"][5]], "cnn_6px": [corrimiento["cnn"][5]]}
        for s in (1984, 1985, 1986, 1987):
            r, c, _ = barajado_y_corrimiento(Xtr, ytr, Xte, yte, Xtr_b, Xte_b, n_clases,
                                             s, verboso=False)
            otras["semillas"].append(s)
            for k in ("densa_normal", "densa_barajada", "cnn_normal", "cnn_barajada"):
                otras[k].append(r[k]["exactitud"])
            otras["densa_3px"].append(c["densa"][3]); otras["cnn_3px"].append(c["cnn"][3])
            otras["densa_6px"].append(c["densa"][5]); otras["cnn_6px"].append(c["cnn"][5])
            print(f"  semilla {s}: densa {r['densa_normal']['exactitud']:.1f}->"
                  f"{r['densa_barajada']['exactitud']:.1f}  CNN {r['cnn_normal']['exactitud']:.1f}->"
                  f"{r['cnn_barajada']['exactitud']:.1f}  3px densa {c['densa'][3]:.1f} "
                  f"CNN {c['cnn'][3]:.1f}")
        otras["caida_densa"] = [round(a - b, 1) for a, b in
                                zip(otras["densa_normal"], otras["densa_barajada"])]
        otras["caida_cnn"] = [round(a - b, 1) for a, b in
                              zip(otras["cnn_normal"], otras["cnn_barajada"])]
        rangos = {k: [min(v), max(v)] for k, v in otras.items() if k != "semillas"}
        otras["rango"] = rangos
        print("  rango (min, max) sobre", len(otras["semillas"]), "semillas:")
        for k, (lo, hi) in rangos.items():
            print(f"    {k:24s} {lo:6.1f} .. {hi:6.1f}")

        # el archivo es barato: doce semillas
        arch = {"semillas": [], "exactitud": [], "errores": [],
                "exactitud_multitud": [], "exactitud_follaje": [], "exactitud_edificio": [],
                "errores_multitud": [], "errores_follaje": [], "errores_edificio": []}
        print("  archivo, doce semillas (exactitud por tipo; errores entre parentesis):")
        for s in range(1983, 1995):
            a = mini_archivo(Xa_t, ya_t, Xv_t, yv, tv, s)
            arch["semillas"].append(s)
            arch["exactitud"].append(a["exactitud"])
            arch["errores"].append(a["errores_totales"])
            for t in ("multitud", "follaje", "edificio"):
                arch["exactitud_" + t].append(a["por_tipo"][t]["exactitud"])
                arch["errores_" + t].append(a["por_tipo"][t]["errores"])
            print(f"    {s}: global {a['exactitud']:.1f}  " + "  ".join(
                f"{t} {a['por_tipo'][t]['exactitud']:.1f} ({a['por_tipo'][t]['errores']})"
                for t in ("multitud", "follaje", "edificio")))
        peor = [min(("multitud", "follaje", "edificio"),
                    key=lambda t: arch["exactitud_" + t][k]) for k in range(len(arch["semillas"]))]
        arch["peor_tipo"] = peor
        otras["archivo"] = arch
        print(f"  el follaje es el tipo con menos aciertos en {peor.count('follaje')} de "
              f"{len(peor)} semillas (errores de los edificios: "
              f"{min(arch['errores_edificio'])} a {max(arch['errores_edificio'])})")

    # --- imagenes de muestra para las viz -----------------------------------
    muestras = []
    vistos = set()
    for k in range(len(Xte_raw)):
        et = int(np.asarray(yte_raw)[k])
        if et in vistos:
            continue
        vistos.add(et)
        muestras.append({"nombre": nombres[et] if et < len(nombres) else str(et),
                         "px": Xte_raw[k].astype(int).tolist()})
        if len(muestras) >= 6:
            break

    salida = {
        "fuente": fuente,
        "n_train": int(len(Xtr)), "n_test": int(len(Xte)),
        "epocas": EPOCAS, "semilla": SEMILLA, "clases": nombres[:n_clases],
        "entorno": ent,
        "resultados": res,
        "corrimiento": corrimiento,
        "archivo": archivo,
        "cuestionario": cuestionario,
        "otras_semillas": otras,
        "permutacion": perm.tolist(),
        "filtros_aprendidos": [[[round(float(v), 3) for v in fila] for fila in f]
                               for f in filtros],
        "muestras": muestras,
        "esquemas": esquemas_sinteticos(),
    }
    if otras is None:
        # con --rapido no se pisa la parte E que ya estaba medida
        previo = AQUI / "datos-experimentos.json"
        if previo.exists():
            salida["otras_semillas"] = json.loads(previo.read_text(encoding="utf-8")).get(
                "otras_semillas")

    destino = AQUI / "datos-experimentos.js"
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write("/* GENERADO por medir-experimentos.py -- no lo edites a mano.\n"
                 "   Son los numeros REALES de la corrida del notebook (semilla 1983).\n"
                 f"   Datos: {fuente}. {len(Xtr)} imagenes de entrenamiento, "
                 f"{EPOCAS} pasadas.\n"
                 f"   Medido con python {ent['python']}, torch {ent['torch']}, "
                 f"numpy {ent['numpy']} ({ent['plataforma']}).\n"
                 "   Determinista en la misma maquina y con las mismas versiones; con\n"
                 "   otras versiones los numeros cambian un poco. */\n")
        fh.write("const DATOS_EXP = " + json.dumps(salida, ensure_ascii=False) + ";\n")
    print(f"\nEscrito: {destino}  ({destino.stat().st_size/1024:.0f} KB)")

    with open(AQUI / "datos-experimentos.json", "w", encoding="utf-8") as fh:
        json.dump({k: v for k, v in salida.items()
                   if k not in ("permutacion", "muestras", "esquemas")},
                  fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
