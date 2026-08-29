"""Corre DE VERDAD los experimentos de la clase 5 y escribe `datos-experimentos.js`.

Ninguno de los números que muestran las slides ni las visualizaciones de esta
clase está inventado ni "estimado": todos salen de correr acá el mismo código
que corre el notebook, con la misma semilla (1983).

    PYTHONPATH=_shared python3 clases/05-imagenes-y-convoluciones/medir-experimentos.py

Si tocás el notebook, volvé a correr esto. Si no, las slides y el notebook
empiezan a contar cosas distintas — que es exactamente lo que este curso le
pide a los demás que no hagan.

Qué mide:
  A) EL BARAJADO (se vuelve a entrenar con los píxeles permutados)
     1. red densa sobre las imágenes normales   -> exactitud
     2. red densa sobre los píxeles BARAJADOS   -> exactitud (sale igual)
     3. CNN sobre las imágenes normales         -> exactitud
     4. CNN sobre los píxeles BARAJADOS         -> exactitud (baja)
  B) EL CORRIMIENTO (se entrena con imágenes centradas y se prueba con la foto
     corrida unos píxeles: NO se vuelve a entrenar)
     la densa se desploma; la CNN aguanta mucho mejor.

Qué exporta además, para que las viz dibujen datos reales y no dibujitos:
  - un puñado de imágenes de muestra (28x28, 0-255)
  - la permutación exacta que usa el barajado
  - los filtros de 3x3 que la CNN aprendió sola
  - unas imágenes esquemáticas sintéticas (afiche, diario, multitud, reja)
    generadas con numpy, para la viz del filtro deslizante
"""
import json
import os
import pathlib
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
N_TRAIN, N_TEST, EPOCAS = 20000, 5000, 12


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
    """FashionMNIST si se puede; si no, las figuras sintéticas."""
    try:
        import descargar
        tr = descargar.fashion_mnist("train")
        te = descargar.fashion_mnist("t10k")
        if tr is not None and te is not None:
            nombres = descargar.ETIQUETAS_FASHION
            return tr, te, nombres, "FashionMNIST"
    except Exception as e:                              # noqa: BLE001
        print(f"  [!] FashionMNIST no disponible ({type(e).__name__}). Voy a lo sintético.")
    nombres = ["barras verticales", "barras horizontales", "bloque", "marco"]
    return (imagenes_sinteticas(N_TRAIN, 1), imagenes_sinteticas(N_TEST, 2),
            nombres, "figuras sintéticas")


# ---------------------------------------------------------------------------
# 1. Los dos modelos
# ---------------------------------------------------------------------------

def red_densa(n_clases):
    """La red de la clase 4, tal cual: aplanar y dos capas."""
    return nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 64), nn.ReLU(),
        nn.Linear(64, n_clases),
    )


def red_convolucional(n_clases):
    """Mira de a 3x3, dos veces, y recién al final decide."""
    return nn.Sequential(
        nn.Conv2d(1, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(16, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Flatten(),
        nn.Linear(32 * 7 * 7, n_clases),
    )


def correr(X, d):
    """La misma imagen, corrida `d` píxeles a la derecha. Lo que entra por la
    izquierda es fondo (negro), no el otro borde: una foto corrida no da la vuelta."""
    if d == 0:
        return X
    Y = torch.zeros_like(X)
    Y[:, :, :, d:] = X[:, :, :, :-d]
    return Y


def entrenar(modelo, Xtr, ytr, Xte, yte, epocas=EPOCAS, lr=1e-3, lote=64,
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
    with torch.no_grad():
        acc = (modelo(Xte).argmax(1) == yte).float().mean().item()
    return acc, time.time() - t0


# ---------------------------------------------------------------------------
# 2. Las imágenes esquemáticas para la viz del filtro
# ---------------------------------------------------------------------------

def esquemas_sinteticos():
    """Cuatro escenas de 28x28 dibujadas con numpy. Sintéticas y rotuladas."""
    rng = np.random.default_rng(7)
    out = {}

    # --- afiche de campaña: fondo claro, letras (palotes verticales), franja ---
    a = np.full((28, 28), 40.0)
    a[3:25, 3:25] = 215.0                       # el papel
    for c in (6, 9, 12, 16, 19, 22):            # los palotes de las letras
        a[7:14, c:c + 2] = 45.0
    a[17:21, 5:23] = 90.0                       # la franja de abajo
    out["afiche"] = a

    # --- fragmento de página de diario: título + dos columnas de renglones ---
    d = np.full((28, 28), 230.0)
    d[2:5, 3:25] = 40.0                         # el título
    for f in range(8, 26, 3):
        d[f:f + 1, 3:12] = 55.0                 # columna izquierda
        d[f:f + 1, 15:25] = 55.0                # columna derecha
    out["diario"] = d

    # --- multitud: cabecitas sobre un fondo con degradé ---
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

    return {k: np.clip(v, 0, 255).astype(np.uint8).tolist() for k, v in out.items()}


# ---------------------------------------------------------------------------
# 3. Correrlo todo
# ---------------------------------------------------------------------------

def main():
    utils.fijar_semilla(SEMILLA)
    (Xtr_raw, ytr_raw), (Xte_raw, yte_raw), nombres, fuente = traer_datos()
    print(f"Datos: {fuente}  ·  train {Xtr_raw.shape}  test {Xte_raw.shape}")

    rng = np.random.default_rng(SEMILLA)
    itr = rng.choice(len(Xtr_raw), size=min(N_TRAIN, len(Xtr_raw)), replace=False)
    ite = rng.choice(len(Xte_raw), size=min(N_TEST, len(Xte_raw)), replace=False)

    Xtr = torch.tensor(Xtr_raw[itr] / 255.0, dtype=torch.float32).unsqueeze(1)
    ytr = torch.tensor(np.asarray(ytr_raw)[itr], dtype=torch.long)
    Xte = torch.tensor(Xte_raw[ite] / 255.0, dtype=torch.float32).unsqueeze(1)
    yte = torch.tensor(np.asarray(yte_raw)[ite], dtype=torch.long)
    n_clases = int(max(ytr.max().item(), yte.max().item())) + 1

    # LA permutación: una sola, la misma para todas las imágenes.
    perm = np.random.default_rng(SEMILLA).permutation(28 * 28)
    tperm = torch.tensor(perm, dtype=torch.long)

    def barajar(X):
        return X.reshape(len(X), 1, -1)[:, :, tperm].reshape(len(X), 1, 28, 28)

    Xtr_b, Xte_b = barajar(Xtr), barajar(Xte)

    res, filtros, entrenados = {}, None, {}
    print("\nA) EL BARAJADO — se vuelve a entrenar con los píxeles permutados")
    for nombre, constructor, datos_tr, datos_te in [
        ("densa_normal", red_densa, Xtr, Xte),
        ("densa_barajada", red_densa, Xtr_b, Xte_b),
        ("cnn_normal", red_convolucional, Xtr, Xte),
        ("cnn_barajada", red_convolucional, Xtr_b, Xte_b),
    ]:
        torch.manual_seed(SEMILLA)
        modelo = constructor(n_clases)
        acc, seg = entrenar(modelo, datos_tr, ytr, datos_te, yte)
        params = utils.contar_parametros(modelo)
        res[nombre] = {"exactitud": round(acc * 100, 1), "parametros": params,
                       "segundos": round(seg, 1)}
        entrenados[nombre] = modelo
        print(f"  {nombre:16s}  {acc*100:5.1f} %   ({params} perillas, {seg:.0f} s)")
        if nombre == "cnn_normal":
            filtros = modelo[0].weight.detach().numpy()[:, 0]   # (16,3,3)

    # --- B) el corrimiento: mismos modelos, la foto movida ------------------
    print("\nB) EL CORRIMIENTO — mismos modelos, la foto corrida (sin reentrenar)")
    desplazamientos = [0, 1, 2, 3, 4, 6]
    corrimiento = {"pixeles": desplazamientos, "densa": [], "cnn": []}
    for clave, mod in [("densa", entrenados["densa_normal"]),
                       ("cnn", entrenados["cnn_normal"])]:
        mod.eval()
        for d in desplazamientos:
            with torch.no_grad():
                a = (mod(correr(Xte, d)).argmax(1) == yte).float().mean().item()
            corrimiento[clave].append(round(a * 100, 1))
        print(f"  {clave:6s}  " + "  ".join(
            f"{d}px:{v:5.1f}%" for d, v in zip(desplazamientos, corrimiento[clave])))

    # --- imágenes de muestra para las viz -----------------------------------
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
        "resultados": res,
        "corrimiento": corrimiento,
        "permutacion": perm.tolist(),
        "filtros_aprendidos": [[[round(float(v), 3) for v in fila] for fila in f]
                               for f in filtros],
        "muestras": muestras,
        "esquemas": esquemas_sinteticos(),
    }

    destino = AQUI / "datos-experimentos.js"
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write("/* GENERADO por medir-experimentos.py — no lo edites a mano.\n"
                 "   Son los números REALES de la corrida del notebook (semilla 1983).\n"
                 f"   Datos: {fuente}. {len(Xtr)} imágenes de entrenamiento, "
                 f"{EPOCAS} pasadas. */\n")
        fh.write("const DATOS_EXP = " + json.dumps(salida, ensure_ascii=False) + ";\n")
    print(f"\nEscrito: {destino}  ({destino.stat().st_size/1024:.0f} KB)")

    with open(AQUI / "datos-experimentos.json", "w", encoding="utf-8") as fh:
        json.dump({k: v for k, v in salida.items()
                   if k not in ("permutacion", "muestras", "esquemas")},
                  fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
