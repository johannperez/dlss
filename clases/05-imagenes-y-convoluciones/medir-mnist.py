"""Corre el notebook de la clase 5 (MNIST) y escribe `datos-mnist.js` y `.json`.

Las slides y el solucionario citan los números que salen de acá, y acá no hay
una segunda copia del código: el script **ejecuta las celdas del notebook tal
cual**, en orden, y después lee las variables que quedaron. Si cambiás el
notebook, volvé a correr esto y los números de las slides se actualizan solos.

    python3 clases/05-imagenes-y-convoluciones/medir-mnist.py

(Necesita torch, numpy y matplotlib. Tarda dos o tres minutos en CPU.)

Dos cosas que el notebook deja como TODO se completan acá para poder medirlas:
  - el TODO 3 se corre con final="aplanar" (es el resultado que las slides
    muestran en la tabla de los tres modelos);
  - las apuestas y las frases de los TODO quedan vacías: no se miden.

Y dos experimentos que el notebook NO corre, para las preguntas 4a y 4b del
cuestionario:
  - la esquina: densa y CNN entrenadas con dígitos centrados en un lienzo de
    56x56 y probadas con el dígito en una esquina (12.000 fotos, 4 épocas);
  - la rotación: los modelos del notebook, probados con las fotos de
    validación rotadas 90 grados (no se reentrena nada).

SOBRE LA REPRODUCIBILIDAD: con la semilla fija la corrida es determinista en
la misma máquina y con las mismas versiones de las librerías. Con otras, los
números cambian unas décimas. El JSON guarda el entorno con que se midió.
"""
import datetime
import json
import os
import pathlib
import platform

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

AQUI = pathlib.Path(__file__).resolve().parent
NOTEBOOK = AQUI / "notebook.ipynb"


def correr_notebook():
    """Ejecuta las celdas de código del notebook en un mismo espacio de nombres."""
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    ns = {"__name__": "__main__"}
    os.chdir(AQUI)                       # el bootstrap busca el repo desde acá
    plt.show = lambda *a, **k: plt.close("all")
    for i, celda in enumerate(nb["cells"]):
        if celda["cell_type"] != "code":
            continue
        fuente = "".join(celda["source"])
        if 'mi_variante = "maximo"' in fuente:
            fuente = fuente.replace('mi_variante = "maximo"', 'mi_variante = "aplanar"')
        exec(compile(fuente, f"notebook.ipynb[{i}]", "exec"), ns)
        plt.close("all")
    return ns


def r1(v):
    return round(float(v), 1)


def main():
    ns = correr_notebook()
    torch = ns["torch"]
    nn = ns["nn"]
    if ns["FUENTE"] != "MNIST":
        raise SystemExit("No hay MNIST (el notebook cayó al plan B): no mido nada.")

    X_val, y_val = ns["X_val"], ns["y_val"]
    predecir, entrenar = ns["predecir"], ns["entrenar"]
    densa, cnn, aplanada = ns["densa"], ns["cnn"], ns["cnn_variante"]
    contar = ns["utils"].contar_parametros
    n_val = len(y_val)

    def resumen(modelo, hist, corr):
        pred = predecir(modelo, X_val)
        errores = int((pred != y_val).sum())
        _, test = ns["evaluar"](modelo, ns["cargador_test"])
        return {"parametros": contar(modelo),
                "val": r1(hist["exactitud"][-1]),
                "val_por_epoca": [r1(v) for v in hist["exactitud"]],
                "test": r1(test),
                "errores_cada_1000": round(1000 * errores / n_val),
                "corrimiento": [r1(v) for v in corr]}

    datos = {
        "fuente": "MNIST",
        "semilla": ns["SEMILLA"],
        "n_train": len(ns["datos_train"]), "n_val": n_val, "n_test": len(ns["datos_test"]),
        "epocas": len(ns["hist_cnn"]["exactitud"]),
        "desplazamientos": ns["DESPLAZAMIENTOS"],
        "densa": resumen(densa, ns["hist_densa"], ns["corr_densa"]),
        "cnn": resumen(cnn, ns["hist_cnn"], ns["corr_cnn"]),
        "aplanada": resumen(aplanada, ns["hist_variante"], ns["corr_variante"]),
    }

    # --- el archivo sintético ------------------------------------------------
    pred_a, y_a, tipo_a = ns["prediccion"], ns["y_arch_val"], ns["tipo_arch_val"]
    datos["archivo"] = {
        "n_train": len(ns["y_arch"]), "n_val": len(y_a),
        "exactitud": r1(100 * (pred_a == y_a).mean()),
        "por_tipo": {t: {"n": int((tipo_a == t).sum()),
                         "exactitud": r1(100 * (pred_a[tipo_a == t] == y_a[tipo_a == t]).mean()),
                         "errores": int((pred_a[tipo_a == t] != y_a[tipo_a == t]).sum())}
                     for t in ["multitud", "follaje", "edificio"]},
    }

    # --- material para las figuras de las slides -----------------------------
    datos["muestra"] = np.asarray(ns["X_train_todo"][0]).astype(int).tolist()
    datos["plantillas"] = (densa.capa1.weight.detach().reshape(-1, 28, 28)[:8]
                           .numpy().round(3).tolist())
    oclusion = []
    for i in [0, 2, 3, 5]:
        x, clase = X_val[i], int(y_val[i])
        oclusion.append({
            "digito": clase,
            "px": (x[0].numpy() * 255).round().astype(int).tolist(),
            "densa": ns["mapa_de_oclusion"](densa, x, clase).round(3).tolist(),
            "cnn": ns["mapa_de_oclusion"](cnn, x, clase).round(3).tolist(),
        })
    datos["oclusion"] = oclusion

    # los errores de follaje del archivo, con el mapa de lo que los convenció
    # (la misma celda del notebook: tapar con el gris medio de cada foto, lado 8)
    errores_follaje = [k for k in np.where(pred_a != y_a)[0] if tipo_a[k] == "follaje"]
    oclusion_archivo = []
    for k in errores_follaje[:3]:
        x, dijo = ns["X_arch_val_t"][k], int(pred_a[k])
        mapa = ns["mapa_de_oclusion"](ns["modelo_archivo"], x, dijo, lado=8,
                                      relleno=float(x.mean()))
        oclusion_archivo.append({"dijo": dijo,
                                 "px": (x[0].numpy() * 255).round().astype(int).tolist(),
                                 "mapa": mapa.round(3).tolist()})
    datos["oclusion_archivo"] = oclusion_archivo

    # --- pregunta 4b: rotar 90 grados, sin reentrenar ------------------------
    rotadas = torch.rot90(X_val, 1, dims=(2, 3))
    datos["rotada"] = {
        nombre: r1(100 * (predecir(m, rotadas) == y_val).float().mean())
        for nombre, m in [("densa", densa), ("cnn", cnn)]}

    # --- pregunta 4a: entrenar centrado en 56x56, probar en una esquina ------
    def lienzo(X, f, c):
        Y = torch.zeros(len(X), 1, 56, 56)
        Y[:, :, f:f + 28, c:c + 28] = X
        return Y

    Xtr = torch.stack([ns["datos_train"][i][0] for i in range(12000)])
    ytr = torch.stack([ns["datos_train"][i][1] for i in range(12000)])
    cargador = ns["DataLoader"](ns["TensorDataset"](lienzo(Xtr, 14, 14), ytr),
                                batch_size=64, shuffle=True,
                                generator=torch.Generator().manual_seed(ns["SEMILLA"]))

    class DensaGrande(nn.Module):
        def __init__(self):
            super().__init__()
            self.red = nn.Sequential(nn.Flatten(), nn.Linear(56 * 56, 64), nn.ReLU(),
                                     nn.Linear(64, 10))

        def forward(self, x):
            return self.red(x)

    esquina = {}
    for nombre, constructor in [("densa", DensaGrande), ("cnn", ns["RedConvolucional"])]:
        torch.manual_seed(ns["SEMILLA"])
        m = constructor()
        opt = torch.optim.Adam(m.parameters(), lr=1e-3)
        for _ in range(4):
            ns["entrenar_una_epoca"](m, cargador, opt)
        esquina[nombre] = {
            lugar: r1(100 * (predecir(m, lienzo(X_val, f, c)) == y_val).float().mean())
            for lugar, (f, c) in [("centro", (14, 14)), ("arriba_izq", (0, 0)),
                                  ("abajo_der", (28, 28))]}
    datos["esquina"] = esquina

    datos["entorno"] = {
        "python": platform.python_version(), "torch": torch.__version__,
        "numpy": np.__version__, "plataforma": platform.platform(),
        "fecha": datetime.date.today().isoformat(),
    }

    (AQUI / "datos-mnist.json").write_text(
        json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    cabecera = (
        "/* GENERADO por medir-mnist.py -- no lo edites a mano.\n"
        "   Son los numeros REALES de correr notebook.ipynb (MNIST, semilla 1983).\n"
        f"   Medido con python {datos['entorno']['python']}, torch {datos['entorno']['torch']}, "
        f"numpy {datos['entorno']['numpy']}.\n"
        "   Determinista en la misma maquina y con las mismas versiones. */\n")
    (AQUI / "datos-mnist.js").write_text(
        cabecera + "const DATOS_MNIST = " + json.dumps(datos, ensure_ascii=False) + ";\n",
        encoding="utf-8")

    d, c, a = datos["densa"], datos["cnn"], datos["aplanada"]
    print(f"densa    {d['parametros']:6d} perillas · val {d['val']} · test {d['test']} · 4px {d['corrimiento'][4]}")
    print(f"cnn      {c['parametros']:6d} perillas · val {c['val']} · test {c['test']} · 4px {c['corrimiento'][4]}")
    print(f"aplanada {a['parametros']:6d} perillas · val {a['val']} · test {a['test']} · 4px {a['corrimiento'][4]}")
    print("archivo", datos["archivo"])
    print("rotada", datos["rotada"], "· esquina", datos["esquina"])


if __name__ == "__main__":
    main()
