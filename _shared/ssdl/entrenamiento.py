"""
ssdl.entrenamiento — el loop de entrenamiento, escrito para ser leído.

Regla de la casa número 3: una abstracción sólo se permite después de haber
hecho a mano lo que esconde. Así que este módulo NO es un `Trainer` opaco.
Es el mismo loop de cinco líneas de la clase 4, con barra de progreso y un poco
de contabilidad alrededor. Abrilo, leelo: son doscientas líneas y no hay magia.

    from ssdl import entrenamiento as ent

    historial = ent.entrenar(modelo, x, y, x_val=xv, y_val=yv,
                             perdida=torch.nn.MSELoss(), lr=0.05, epocas=200)
    historial.graficar()

Y para la clase 4, el modo que narra lo que pasa en cada estación del ciclo:

    ent.entrenar(modelo, x, y, epocas=50, explicar=2)
"""

from __future__ import annotations

import copy
import sys
import time

import numpy as np

from .utils import formatear_duracion

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


# ===========================================================================
# La contabilidad
# ===========================================================================

class Historial:
    """
    La libreta del entrenamiento: qué loss hubo en cada época, en train y en
    validación, más las métricas que quieras agregar.

        historial.train        -> lista de loss de entrenamiento
        historial.val          -> lista de loss de validación
        historial.mejor()      -> (época, valor) de la mejor validación
        historial.graficar()   -> las dos curvas de la clase 4
    """

    def __init__(self):
        self.epocas: list[int] = []
        self.train: list[float] = []
        self.val: list[float] = []
        self.metricas: dict[str, list[float]] = {}
        self.segundos: float = 0.0
        self.detenido_temprano: bool = False

    def registrar(self, epoca: int, train: float, val: float | None = None,
                  **metricas) -> None:
        """Anota una época."""
        self.epocas.append(epoca)
        self.train.append(float(train))
        if val is not None:
            self.val.append(float(val))
        for nombre, valor in metricas.items():
            self.metricas.setdefault(nombre, []).append(float(valor))

    def mejor(self, cual: str = "val") -> tuple[int, float]:
        """
        Devuelve (época, valor) del mejor momento. Por defecto, la época donde
        la loss de validación tocó su mínimo: ese es el modelo que te querés
        quedar, no el de la última época.
        """
        serie = self.val if (cual == "val" and self.val) else self.train
        if not serie:
            return (0, float("nan"))
        i = int(np.argmin(serie))
        return (self.epocas[i], serie[i])

    def como_dict(self) -> dict:
        """Todo el historial como diccionario, para guardarlo en un JSON."""
        d = {"epocas": self.epocas, "train": self.train, "val": self.val,
             "segundos": self.segundos, "detenido_temprano": self.detenido_temprano}
        d.update(self.metricas)
        return d

    def graficar(self, **kwargs):
        """Dibuja las curvas de train y validación (ver ssdl.graficos)."""
        from . import graficos
        return graficos.curvas_de_entrenamiento(self, **kwargs)

    def __len__(self) -> int:
        return len(self.epocas)

    def __repr__(self) -> str:
        if not self.epocas:
            return "<Historial vacío>"
        partes = [f"{len(self)} épocas", f"train {self.train[-1]:.4g}"]
        if self.val:
            epoca, valor = self.mejor()
            partes.append(f"val {self.val[-1]:.4g}")
            partes.append(f"mejor val {valor:.4g} en la época {epoca}")
        return "<Historial: " + " · ".join(partes) + ">"


class BarraDeProgreso:
    """
    Barra de progreso de texto, sin dependencias. Funciona igual en Colab, en
    Jupyter y en una terminal.

        barra = BarraDeProgreso(total=100, etiqueta="entrenando")
        for i in range(100):
            barra.actualizar(i + 1, "loss 0.031")
        barra.cerrar()
    """

    def __init__(self, total: int, ancho: int = 26, etiqueta: str = "",
                 salida=None):
        self.total = max(int(total), 1)
        self.ancho = ancho
        self.etiqueta = etiqueta
        self.salida = salida or sys.stdout
        self.arranque = time.perf_counter()
        self._ultimo_dibujo = 0.0

    def actualizar(self, i: int, sufijo: str = "", forzar: bool = False) -> None:
        """Redibuja la barra. Se autolimita a ~20 dibujos por segundo."""
        ahora = time.perf_counter()
        if not forzar and i < self.total and (ahora - self._ultimo_dibujo) < 0.05:
            return
        self._ultimo_dibujo = ahora

        fraccion = min(i / self.total, 1.0)
        llenas = int(self.ancho * fraccion)
        barra = "█" * llenas + "·" * (self.ancho - llenas)
        transcurrido = ahora - self.arranque
        resto = (transcurrido / fraccion - transcurrido) if fraccion > 0.02 else 0.0
        linea = (f"\r{self.etiqueta} |{barra}| {i}/{self.total} "
                 f"[{formatear_duracion(transcurrido)}"
                 f"{' · faltan ' + formatear_duracion(resto) if resto > 1 else ''}]"
                 f"  {sufijo}")
        self.salida.write(linea.ljust(96)[:110])
        self.salida.flush()

    def cerrar(self, mensaje: str = "") -> None:
        """Cierra la línea. Siempre llamala, o el próximo print sale pegado."""
        self.salida.write("\n" + (mensaje + "\n" if mensaje else ""))
        self.salida.flush()


class ParadaTemprana:
    """
    Early stopping: si la validación deja de mejorar durante `paciencia` épocas,
    frenamos y nos quedamos con el mejor modelo, no con el último.

    Es la defensa operativa contra el sobreajuste de la clase 4: en vez de
    adivinar cuántas épocas entrenar, entrenás de más y volvés al mejor punto.

        parada = ParadaTemprana(paciencia=15)
        if parada(loss_val, modelo):
            break
        parada.restaurar_mejor(modelo)
    """

    def __init__(self, paciencia: int = 15, minima_mejora: float = 1e-5,
                 verboso: bool = True):
        self.paciencia = paciencia
        self.minima_mejora = minima_mejora
        self.verboso = verboso
        self.mejor_valor = float("inf")
        self.mejor_epoca = 0
        self.sin_mejorar = 0
        self._mejor_estado = None

    def __call__(self, valor: float, modelo=None, epoca: int | None = None) -> bool:
        """Devuelve True si hay que frenar."""
        if valor < self.mejor_valor - self.minima_mejora:
            self.mejor_valor = float(valor)
            self.mejor_epoca = epoca if epoca is not None else self.mejor_epoca + 1
            self.sin_mejorar = 0
            if modelo is not None:
                self._mejor_estado = copy.deepcopy(modelo.state_dict())
            return False

        self.sin_mejorar += 1
        if self.sin_mejorar >= self.paciencia:
            if self.verboso:
                print(f"\nParada temprana: la validación no mejora hace "
                      f"{self.paciencia} épocas. La mejor fue {self.mejor_valor:.4g} "
                      f"(época {self.mejor_epoca}).")
            return True
        return False

    def restaurar_mejor(self, modelo) -> bool:
        """Devuelve el modelo al estado de su mejor época. True si pudo."""
        if self._mejor_estado is not None:
            modelo.load_state_dict(self._mejor_estado)
            return True
        return False


# ===========================================================================
# Lotes
# ===========================================================================

def _lotes(x, y, tam_lote: int | None, barajar: bool, generador=None):
    """
    Corta los datos en lotes (batches). Si `tam_lote` es None, un solo lote con
    todo (que es lo que se hace en las clases 1 a 4, donde hay 36 puntos).

    Devuelve un iterador de pares (x_lote, y_lote).
    """
    n = len(x)
    if tam_lote is None or tam_lote >= n:
        yield x, y
        return
    indices = (torch.randperm(n, generator=generador) if barajar
               else torch.arange(n))
    for i in range(0, n, tam_lote):
        idx = indices[i:i + tam_lote]
        yield x[idx], y[idx]


def _es_dataloader(objeto) -> bool:
    return hasattr(objeto, "__iter__") and hasattr(objeto, "dataset")


# ===========================================================================
# El modo pedagógico: narrar el ciclo estación por estación
# ===========================================================================

_ESTACIONES = [
    ("1. PREDECIR", "prediccion = modelo(x)",
     "El modelo dibuja con las perillas que tiene ahora. Todavía no sabe si está bien."),
    ("2. COMPARAR", "perdida = funcion_de_perdida(prediccion, y)",
     "Ponemos un número a qué tan mal la está dibujando. Un número, uno solo."),
    ("3. BORRAR", "optimizador.zero_grad()",
     "Borramos los gradientes de la vuelta anterior. Si no, se acumulan. "
     "Es el error #1 de PyTorch, y lo cometemos todos."),
    ("4. ANOTAR", "perdida.backward()",
     "Se calcula, para CADA perilla, hacia dónde habría que moverla. "
     "OJO: acá no se movió nada todavía. Sólo se anotó."),
    ("5. MOVER", "optimizador.step()",
     "Recién ACÁ se mueven las perillas, un pasito cuesta abajo. "
     "Este es el descenso de la clase 3."),
]


def _narrar(paso: int, modelo, perdida_valor: float, grad_antes, params_antes,
            params_despues) -> None:
    """Imprime las cinco estaciones del ciclo con los números de verdad."""
    print(f"\n{'═' * 74}")
    print(f"  UNA VUELTA DEL CICLO (paso {paso})")
    print("═" * 74)
    for titulo, linea, explicacion in _ESTACIONES:
        print(f"\n  {titulo}")
        print(f"      {linea}")
        print(f"      {explicacion}")
        if titulo.startswith("2."):
            print(f"      →  perdida = {perdida_valor:.6f}")
        if titulo.startswith("4."):
            for nombre, g in list(grad_antes.items())[:4]:
                print(f"      →  gradiente de {nombre}: {_resumir(g)}")
            print("      →  y las perillas siguen valiendo lo mismo que antes.")
        if titulo.startswith("5."):
            for nombre in list(params_antes.keys())[:4]:
                antes, despues = params_antes[nombre], params_despues[nombre]
                print(f"      →  {nombre}: {_resumir(antes)}  →  {_resumir(despues)}")
    print(f"\n{'═' * 74}\n")


def _resumir(tensor) -> str:
    """Un tensor en una línea corta: si tiene 1-3 valores los muestra enteros."""
    if tensor is None:
        return "None"
    plano = tensor.detach().cpu().reshape(-1)
    if plano.numel() <= 3:
        return "[" + ", ".join(f"{v:+.4f}" for v in plano.tolist()) + "]"
    return (f"{tuple(tensor.shape)}  media {plano.mean():+.4f}  "
            f"máx |{plano.abs().max():.4f}|")


# ===========================================================================
# EL LOOP
# ===========================================================================

def entrenar(modelo, x, y, x_val=None, y_val=None, *,
             perdida=None, optimizador=None, lr: float = 0.01,
             epocas: int = 100, tam_lote: int | None = None, barajar: bool = True,
             paciencia: int | None = None, metrica=None, nombre_metrica="métrica",
             device=None, verboso: int = 1, cada: int | None = None,
             explicar: int = 0, semilla: int | None = None) -> Historial:
    """
    Entrena un modelo. Es el loop de la clase 4, con contabilidad.

    Adentro pasa exactamente esto, y nada más:

        prediccion = modelo(x)                        # 1. predecir
        perdida    = funcion_de_perdida(prediccion, y)  # 2. comparar
        optimizador.zero_grad()                       # 3. borrar
        perdida.backward()                            # 4. anotar
        optimizador.step()                            # 5. mover

    Parámetros
    ----------
    modelo : torch.nn.Module
    x, y : tensores de entrenamiento. También aceptamos numpy: los convertimos.
           Si `x` es un DataLoader, `y` se ignora y se itera el DataLoader.
    x_val, y_val : los datos que el modelo NO va a ver para entrenar. Poné algo
           acá siempre que puedas: sin validación no sabés si aprendió o memorizó.
    perdida : la función de pérdida. Por defecto MSELoss (regresión).
           Para clasificación, pasá `torch.nn.CrossEntropyLoss()`.
    optimizador : por defecto SGD con la `lr` que le pases. Podés pasarle
           `torch.optim.Adam(modelo.parameters(), lr=1e-3)` si querés.
    lr : el tamaño del paso cuesta abajo. La perilla más importante que vas a
           tocar: muy chico y no llega nunca, muy grande y sale despedido.
    epocas : cuántas veces se recorren todos los datos.
    tam_lote : de a cuántos casos. None = todos juntos (lo normal hasta la clase 4).
    paciencia : si le ponés un número, activa la parada temprana y restaura el
           mejor modelo al terminar. Necesita datos de validación.
    metrica : callable metrica(prediccion, y) -> número, por ejemplo
           `ent.exactitud`. Se calcula sobre validación.
    verboso : 0 = mudo, 1 = barra de progreso, 2 = una línea por época.
    cada : cada cuántas épocas imprimir (sólo con verboso=2). Por defecto,
           unas 10 líneas en total.
    explicar : narra el ciclo estación por estación durante los primeros N
           pasos. Es el modo de la clase 4. Poné explicar=1 o 2, no más.
    semilla : si le pasás un número, fija el barajado de los lotes.

    Devuelve un `Historial`.
    """
    if torch is None:
        raise ImportError("entrenar() necesita PyTorch. Ver recursos/setup.md.")

    # --- preparativos ---
    perdida = perdida if perdida is not None else torch.nn.MSELoss()
    optimizador = optimizador or torch.optim.SGD(modelo.parameters(), lr=lr)
    if device is not None:
        modelo = modelo.to(device)

    usa_dataloader = _es_dataloader(x)
    if not usa_dataloader:
        x, y = _asegurar_tensor(x, device), _asegurar_tensor(y, device)
        if x_val is not None:
            x_val = _asegurar_tensor(x_val, device)
            y_val = _asegurar_tensor(y_val, device)

    generador = None
    if semilla is not None:
        generador = torch.Generator().manual_seed(int(semilla))

    hay_validacion = (x_val is not None and y_val is not None)
    parada = (ParadaTemprana(paciencia, verboso=(verboso > 0))
              if (paciencia and hay_validacion) else None)
    if paciencia and not hay_validacion:
        print("Aviso: pediste parada temprana pero no pasaste datos de "
              "validación. La ignoro (no tendría contra qué parar).")

    historial = Historial()
    barra = BarraDeProgreso(epocas, etiqueta="entrenando") if verboso == 1 else None
    cada = cada or max(1, epocas // 10)
    arranque = time.perf_counter()
    pasos_narrados = 0

    # --- el loop ---
    for epoca in range(1, epocas + 1):
        modelo.train()
        suma, n_lotes = 0.0, 0

        iterador = (x if usa_dataloader
                    else _lotes(x, y, tam_lote, barajar, generador))
        for x_lote, y_lote in iterador:
            if usa_dataloader and device is not None:
                x_lote, y_lote = x_lote.to(device), y_lote.to(device)

            narrar_este = pasos_narrados < explicar
            if narrar_este:
                params_antes = {n: p.detach().clone()
                                for n, p in modelo.named_parameters()}

            # ------------- las cinco estaciones -------------
            prediccion = modelo(x_lote)                     # 1. PREDECIR
            valor = perdida(prediccion, y_lote)             # 2. COMPARAR
            optimizador.zero_grad()                         # 3. BORRAR
            valor.backward()                                # 4. ANOTAR
            if narrar_este:
                grad_antes = {n: (p.grad.detach().clone() if p.grad is not None else None)
                              for n, p in modelo.named_parameters()}
            optimizador.step()                              # 5. MOVER
            # ------------------------------------------------

            if narrar_este:
                params_despues = {n: p.detach().clone()
                                  for n, p in modelo.named_parameters()}
                _narrar(pasos_narrados + 1, modelo, float(valor.detach()),
                        grad_antes, params_antes, params_despues)
                pasos_narrados += 1

            # .detach() antes de sacar el número: si no, PyTorch avisa (con razón)
            # que estás convirtiendo a escalar algo que todavía cuelga del grafo.
            suma += float(valor.detach())
            n_lotes += 1

        loss_train = suma / max(n_lotes, 1)

        # --- validación: sin gradientes, en modo evaluación ---
        loss_val, valor_metrica = None, None
        if hay_validacion:
            loss_val, valor_metrica = evaluar(modelo, x_val, y_val, perdida,
                                              metrica=metrica)

        extras = ({nombre_metrica: valor_metrica}
                  if valor_metrica is not None else {})
        historial.registrar(epoca, loss_train, loss_val, **extras)

        # --- avisos ---
        sufijo = f"loss {loss_train:.4g}"
        if loss_val is not None:
            sufijo += f" · val {loss_val:.4g}"
        if valor_metrica is not None:
            sufijo += f" · {nombre_metrica} {valor_metrica:.3f}"

        if verboso == 1 and barra is not None:
            barra.actualizar(epoca, sufijo)
        elif verboso >= 2 and (epoca % cada == 0 or epoca == 1 or epoca == epocas):
            print(f"época {epoca:>4}/{epocas}   {sufijo}")

        # --- parada temprana ---
        if parada is not None and parada(loss_val, modelo, epoca):
            historial.detenido_temprano = True
            break

    historial.segundos = time.perf_counter() - arranque
    if barra is not None:
        barra.cerrar()

    if parada is not None and parada.restaurar_mejor(modelo):
        if verboso > 0:
            print(f"Modelo restaurado a la época {parada.mejor_epoca} "
                  f"(la de mejor validación). No te quedes con el último: "
                  f"quedate con el mejor.")

    if verboso > 0:
        print(f"Listo en {formatear_duracion(historial.segundos)}. {historial!r}")
    return historial


def _asegurar_tensor(a, device=None):
    """numpy o lista -> tensor de torch, sin romper si ya era un tensor."""
    if not isinstance(a, torch.Tensor):
        a = np.asarray(a)
        tipo = torch.long if np.issubdtype(a.dtype, np.integer) else torch.float32
        a = torch.tensor(a, dtype=tipo)
    return a.to(device) if device is not None else a


# ===========================================================================
# Evaluar y predecir
# ===========================================================================

def evaluar(modelo, x, y, perdida=None, metrica=None, tam_lote: int | None = None):
    """
    Corre el modelo sobre datos que no va a usar para aprender.

    Dos cosas importantes pasan acá y conviene saber por qué:
      · `modelo.eval()` apaga cosas como dropout, que sólo tienen sentido
        mientras entrenás.
      · `torch.no_grad()` le dice a PyTorch que no anote nada para el backward.
        Es más rápido y usa menos memoria: acá no vamos a mover ninguna perilla.

    Devuelve (loss, metrica). Si no pasás métrica, el segundo es None.
    """
    perdida = perdida if perdida is not None else torch.nn.MSELoss()
    modelo.eval()
    with torch.no_grad():
        suma, n_lotes, predicciones = 0.0, 0, []
        for x_lote, y_lote in _lotes(x, y, tam_lote, barajar=False):
            p = modelo(x_lote)
            suma += float(perdida(p, y_lote))
            n_lotes += 1
            predicciones.append(p)
        loss = suma / max(n_lotes, 1)
        valor = float(metrica(torch.cat(predicciones), y)) if metrica else None
    return loss, valor


def predecir(modelo, x, device=None, como_numpy: bool = False):
    """
    Predice, sin calcular gradientes. El atajo que vas a usar mil veces.

        y_hat = ent.predecir(modelo, x_test, como_numpy=True)
    """
    modelo.eval()
    x = _asegurar_tensor(x, device)
    with torch.no_grad():
        salida = modelo(x)
    return salida.cpu().numpy() if como_numpy else salida


# ===========================================================================
# Métricas listas para pasarle a entrenar()
# ===========================================================================

def exactitud(prediccion, y) -> float:
    """
    Proporción de aciertos. Sirve para logits de varias clases (elige el máximo)
    y para una salida única (umbral en 0).

    Recordá la clase 9: la exactitud sola miente cuando el fenómeno es raro.
    Si el 3% de los titulares menciona protesta, decir siempre "no" da 97%.
    """
    with torch.no_grad():
        if prediccion.ndim > 1 and prediccion.shape[-1] > 1:
            clases = prediccion.argmax(dim=-1)
        else:
            clases = (prediccion.reshape(-1) > 0).long()
        return float((clases.reshape(-1) == y.reshape(-1)).float().mean())


def error_absoluto_medio(prediccion, y) -> float:
    """
    MAE: el error promedio en las unidades de tus datos. Se puede decir en voz
    alta ("me equivoco en 1,2 puntos porcentuales en promedio"), cosa que con el
    MSE no se puede porque está al cuadrado.
    """
    with torch.no_grad():
        return float((prediccion.reshape(-1) - y.reshape(-1)).abs().mean())


def r_cuadrado(prediccion, y) -> float:
    """
    R²: qué proporción de la variación de y explica el modelo. El que ya conocés
    de la regresión, y por eso mismo el mejor puente al aula.
    """
    with torch.no_grad():
        y = y.reshape(-1).float()
        p = prediccion.reshape(-1).float()
        ss_res = float(((y - p) ** 2).sum())
        ss_tot = float(((y - y.mean()) ** 2).sum())
        return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")


# ===========================================================================
# El descenso a mano (clase 3): sin autograd, con restas
# ===========================================================================

def descenso_a_mano(loss_fn, parametros_iniciales, lr: float = 0.1,
                    pasos: int = 40, h: float = 1e-4, guardar_todo: bool = True):
    """
    Descenso por gradiente calculando las pendientes CON UNA RESTA, sin torch y
    sin autograd. Es la clase 3, donde la palabra "derivada" todavía no se
    pronunció.

    La idea entera está en dos líneas:
        pendiente = (loss(p + h) - loss(p - h)) / (2h)   # ¿para dónde sube?
        p = p - lr * pendiente                           # entonces voy al revés

        trayectoria, losses = ent.descenso_a_mano(
            lambda p: mse(p[0], p[1]), [0.0, 0.0], lr=0.05, pasos=60)

    Devuelve (trayectoria, losses): la lista de posiciones (para dibujar el
    rastro sobre el mapa de loss) y la lista de valores de la loss.
    """
    p = np.array(parametros_iniciales, dtype=float)
    trayectoria, losses = [p.copy()], [float(loss_fn(p))]

    for _ in range(pasos):
        gradiente = np.zeros_like(p)
        for i in range(len(p)):
            arriba, abajo = p.copy(), p.copy()
            arriba[i] += h
            abajo[i] -= h
            gradiente[i] = (float(loss_fn(arriba)) - float(loss_fn(abajo))) / (2 * h)
        p = p - lr * gradiente
        if guardar_todo:
            trayectoria.append(p.copy())
            losses.append(float(loss_fn(p)))

    return np.array(trayectoria), np.array(losses)


if __name__ == "__main__":
    import doctest
    fallas, corridos = doctest.testmod()
    print(f"doctests: {corridos - fallas}/{corridos} OK")
