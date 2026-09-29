"""Genera los números REALES que se dibujan en las figuras de slides.html.

Ninguna figura de esta clase está dibujada "a ojo": todas salen de correr acá el
mismo código que corre el notebook, con la misma semilla. (La única excepción, y
está declarada en `referencias.md`, son los dos parámetros de la recta «a ojo»
de la slide 18: esos sí van a mano, porque representan un ajuste humano.) Este script escribe
`datos-figuras.js`, que las slides cargan por ruta relativa (nada de fetch: el
material tiene que abrir con file://).

    PYTHONPATH=_shared python3 clases/04-entrenar-de-verdad/medir-figuras.py

Si cambiás un número del notebook, volvé a correr esto. Si no, las slides y el
notebook empiezan a contar cosas distintas, que es exactamente lo que este curso
le pide a los demás que no haga.

Reproducibilidad: el resultado es determinista EN LA MISMA MÁQUINA Y CON LAS
MISMAS VERSIONES de las librerías (semilla fija). Con otra versión de torch o de
numpy los números cambian un poco (en el tercer o cuarto decimal; justo el par
64/256 rampas es de los más sensibles). Por eso el archivo que sale guarda las
versiones con que se generó (`versiones`), y las slides leen de acá en vez de
tener números escritos a mano.
"""
import json
import platform
import numpy as np
import torch
import torch.nn as nn
import os
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "_shared"))
os.environ.setdefault("DLSS_RAIZ", str(RAIZ))
from ssdl import datos, utils

utils.fijar_semilla(1983)
anios, seg = datos.serie_menciones("seguridad")
X = torch.tensor((anios - 2001) / 10, dtype=torch.float32).reshape(-1, 1)
Y = torch.tensor(seg, dtype=torch.float32).reshape(-1, 1)
grilla = np.linspace(1983.5, 2019.5, 160)
Xg = torch.tensor((grilla - 2001) / 10, dtype=torch.float32).reshape(-1, 1)


def entrenar(xt, yt, h, epocas=3000, lr=0.01, semilla=1983, xv=None, yv=None):
    torch.manual_seed(semilla)
    m = nn.Sequential(nn.Linear(1, h), nn.ReLU(), nn.Linear(h, 1))
    crit, opt = nn.MSELoss(), torch.optim.Adam(m.parameters(), lr=lr)
    lt, lv = [], []
    for _ in range(epocas):
        p = crit(m(xt), yt)
        opt.zero_grad(); p.backward(); opt.step()
        lt.append(p.item())
        if xv is not None:
            with torch.no_grad():
                lv.append(crit(m(xv), yv).item())
    return m, lt, lv


out = {"versiones": {"python": platform.python_version(), "torch": torch.__version__,
                     "numpy": np.__version__},
       "anios": anios.tolist(), "seguridad": [round(v, 4) for v in seg.tolist()],
       "grilla": [round(v, 3) for v in grilla.tolist()]}

# --- la mejor recta posible (clase 1) ---------------------------------------
A = np.vstack([(anios - 2001) / 10, np.ones(len(anios))]).T
coef, *_ = np.linalg.lstsq(A, seg, rcond=None)
out["recta"] = {"a": float(coef[0]), "b": float(coef[1]),
                "mse": round(float(np.mean((A @ coef - seg) ** 2)), 5)}
# Una recta "a ojo" plausible, de las que salían en la clase 1. OJO: estos dos
# números están ELEGIDOS A MANO, no medidos — es el único par de la clase que no
# sale de una corrida. El MSE sí se mide sobre los datos reales. Está declarado
# en referencias.md; si lo cambiás, cambiá también la nota de ahí.
a_ojo, b_ojo = 0.02, 0.22
out["ojo"] = {"a": a_ojo, "b": b_ojo,
              "mse": round(float(np.mean((a_ojo * (anios - 2001) / 10 + b_ojo - seg) ** 2)), 5)}

# --- las capacidades (4, 16, 64; y 256 sin dibujo) -------------------------
# Es el TODO 2 del notebook. La slide 19 dibuja las tres primeras y menciona el
# número de 256 (lo lee de `cap256`, no está escrito a mano en el HTML).
out["capacidades"] = []
for h in [4, 16, 64]:
    m, lt, _ = entrenar(X, Y, h)
    with torch.no_grad():
        curva = m(Xg).numpy().ravel()
    out["capacidades"].append({"h": h, "perillas": utils.contar_parametros(m),
                               "mse": round(lt[-1], 5),
                               "curva": [round(float(v), 4) for v in curva]})
m256, lt256, _ = entrenar(X, Y, 256)
out["cap256"] = {"h": 256, "perillas": utils.contar_parametros(m256),
                 "mse": round(lt256[-1], 5)}

# --- el calco: 200 rampas sobre 31 años, con 5 años apartados ---------------
apartados = [1987, 1995, 2003, 2010, 2017]   # cinco años repartidos parejo
mask = ~np.isin(anios, apartados)
Xc, Yc = X[mask], Y[mask]
m_calco, lt_calco, _ = entrenar(Xc, Yc, 200, epocas=12000, lr=0.005)
with torch.no_grad():
    curva_calco = m_calco(Xg).numpy().ravel()
    pred_apartados = m_calco(X[~mask]).numpy().ravel()
out["calco"] = {
    "h": 200, "perillas": utils.contar_parametros(m_calco),
    "mse_train": round(lt_calco[-1], 6),
    "curva": [round(float(v), 4) for v in curva_calco],
    "apartados": [{"anio": int(a), "y": round(float(v), 4), "pred": round(float(p), 4)}
                  for a, v, p in zip(anios[~mask], seg[~mask], pred_apartados)],
    "mse_apartados": round(float(np.mean((pred_apartados - seg[~mask]) ** 2)), 5),
}
# y la red sana (16 rampas) sobre los mismos 31, para comparar en los 5 apartados
m_sana, lt_sana, _ = entrenar(Xc, Yc, 16, epocas=3000, lr=0.01)
with torch.no_grad():
    pred_sana = m_sana(X[~mask]).numpy().ravel()
    curva_sana = m_sana(Xg).numpy().ravel()
out["sana"] = {"h": 16, "mse_train": round(lt_sana[-1], 5),
               "curva": [round(float(v), 4) for v in curva_sana],
               "mse_apartados": round(float(np.mean((pred_sana - seg[~mask]) ** 2)), 5)}

# --- la red de 16 rampas sobre TODO (el reencuentro) ------------------------
torch.manual_seed(1983)
m16 = nn.Sequential(nn.Linear(1, 16), nn.ReLU(), nn.Linear(16, 1))
crit, opt = nn.MSELoss(), torch.optim.SGD(m16.parameters(), lr=0.15)
for _ in range(4000):
    p = crit(m16(X), Y); opt.zero_grad(); p.backward(); opt.step()
with torch.no_grad():
    out["reencuentro"] = {"mse": round(p.item(), 5),
                          "curva": [round(float(v), 4) for v in m16(Xg).numpy().ravel()]}

# --- la tijera (los mismos números del notebook) ----------------------------
idx_tr, idx_va, idx_te = datos.particion(len(anios), 0.6, 0.2)
_, lt, lv = entrenar(X[idx_tr], Y[idx_tr], 16, epocas=1500,
                     xv=X[idx_va], yv=Y[idx_va])
paso = 5
out["tijera"] = {"epocas": list(range(1, 1501, paso)),
                 "train": [round(v, 5) for v in lt[::paso]],
                 "val": [round(v, 5) for v in lv[::paso]],
                 "mejor": int(np.argmin(lv)) + 1,
                 "mejor_val": round(min(lv), 5)}

# --- la partición al azar: qué años caen dónde ------------------------------
out["particion"] = {
    "train": sorted(anios[idx_tr].astype(int).tolist()),
    "val": sorted(anios[idx_va].astype(int).tolist()),
    "test": sorted(anios[idx_te].astype(int).tolist()),
}

# --- el TODO 4: 256 rampas sobre 15 casos (para las notas de la slide 30) ----
_, lt4, lv4 = entrenar(X[idx_tr][:15], Y[idx_tr][:15], 256, epocas=1500,
                       xv=X[idx_va], yv=Y[idx_va])
out["todo4"] = {"train": round(lt4[-1], 5), "val": round(lv4[-1], 5),
                "veces": round(lv4[-1] / lt4[-1], 1), "mejor": int(np.argmin(lv4)) + 1}


# --- la sección 6: al azar contra por tiempo (slide 35) ---------------------
def entrenar_y_testear(i_tr, i_va, i_te, h=16):
    """Lo mismo que la función del notebook: early stopping y test UNA vez."""
    _, _, lv_ = entrenar(X[i_tr], Y[i_tr], h, epocas=1500, xv=X[i_va], yv=Y[i_va])
    frenar = int(np.argmin(lv_)) + 1
    m_, _, _ = entrenar(X[i_tr], Y[i_tr], h, epocas=frenar)
    with torch.no_grad():
        test = float(((m_(X[i_te]) - Y[i_te]) ** 2).mean())
        base = float(((Y[i_te] - Y[i_tr].mean()) ** 2).mean())
    return m_, test, base


m_azar, test_azar, base_azar = entrenar_y_testear(idx_tr, idx_va, idx_te)
tr_t, va_t, te_t = datos.particion_temporal(anios, 2008, 2014)
_, test_tiempo, base_tiempo = entrenar_y_testear(tr_t, va_t, te_t)
i05 = int(np.where(anios == 2005)[0][0])
with torch.no_grad():
    pred05 = float(m_azar(X[i05:i05 + 1]).item())
out["fuga"] = {"test_azar": round(test_azar, 5), "base_azar": round(base_azar, 5),
               "test_tiempo": round(test_tiempo, 5), "base_tiempo": round(base_tiempo, 5),
               "veces": round(test_tiempo / test_azar, 1),
               "pred_2005": round(pred05, 4), "real_2005": round(float(seg[i05]), 4)}

ruta = pathlib.Path(__file__).resolve().parent / "datos-figuras.js"
ruta.write_text(
    "/* GENERADO por medir-figuras.py — no lo edites a mano.\n"
    "   Son los números reales de la corrida del notebook (semilla 1983). */\n"
    "const DATOS_FIG = " + json.dumps(out, ensure_ascii=False) + ";\n",
    encoding="utf-8")
print("escrito", ruta)
print("recta   MSE", out["recta"]["mse"], " a ojo", out["ojo"]["mse"])
print("reencuentro MSE", out["reencuentro"]["mse"])
for c in out["capacidades"]:
    print("  h", c["h"], "perillas", c["perillas"], "mse", c["mse"])
print("calco: train", out["calco"]["mse_train"], "en los 5 apartados",
      out["calco"]["mse_apartados"], "| sana:", out["sana"]["mse_train"],
      out["sana"]["mse_apartados"])
print("apartados", out["calco"]["apartados"])
print("  h 256 perillas", out["cap256"]["perillas"], "mse", out["cap256"]["mse"])
print("tijera mejor", out["tijera"]["mejor"], out["tijera"]["mejor_val"],
      "final train", out["tijera"]["train"][-1], "val", out["tijera"]["val"][-1])
print("todo4", out["todo4"])
print("fuga", out["fuga"])
print("versiones", out["versiones"])
print("test años", out["particion"]["test"])
