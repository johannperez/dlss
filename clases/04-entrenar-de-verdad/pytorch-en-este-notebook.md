# PyTorch (y algo de numpy) en el notebook de la clase 4

**Un machete: cada función que aparece en el código, qué hace en castellano y
dónde está su documentación.**

> No hace falta leerlo de corrido. Está para cuando una línea del notebook te
> frena y querés saber qué hace ese `.detach()` o ese `.reshape(-1, 1)` antes de
> seguir. Va en el orden en que aparece cada cosa en el notebook.
>
> Los enlaces van a la documentación oficial, que está en inglés. Si querés una
> sola puerta de entrada, es el tutorial
> [*Learn the Basics*](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)
> de PyTorch: cubre casi todo lo de esta página, en el mismo orden.

---

## 1. Tensores: crearlos, mirarlos, sacar números afuera

| en el notebook | qué hace | docs |
|---|---|---|
| `torch.tensor([1.0, 2.0, 3.0])` | Crea un tensor a partir de una lista (o de un array de numpy). Copia los datos. | [torch.tensor](https://docs.pytorch.org/docs/stable/generated/torch.tensor.html) |
| `torch.tensor(a, dtype=torch.float32)` | Lo mismo, diciendo el tipo de número. Usamos `float32` porque es lo que esperan las capas de `nn`; numpy, en cambio, crea `float64` por defecto. | [tipos de tensor](https://docs.pytorch.org/docs/stable/tensor_attributes.html) |
| `t.shape` | La forma: cuántas filas, cuántas columnas. `(36, 1)` quiere decir 36 casos y 1 variable. | [Tensor.size](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.size.html) (`shape` es lo mismo) |
| `.reshape(-1, 1)` | Reacomoda los mismos números en otra forma. El `-1` quiere decir "calculalo vos": con 36 años y `(-1, 1)` sale `(36, 1)`. Lo hacemos porque `nn.Linear` quiere una **tabla** de casos × variables, no una lista suelta. | [Tensor.reshape](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.reshape.html) |
| `t * 2`, `t.sum()`, `.mean()` | Cuentas de toda la vida, elemento por elemento o sobre todo el tensor. | [Tensor.sum](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.sum.html), [Tensor.mean](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.mean.html) |
| `x[indices_train]` | Elegir filas con una lista de índices. Así partimos en train / val / test. | [indexado, en el tutorial de tensores](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html) |
| `.item()` | Saca **un** número de un tensor de un solo elemento y te lo da como número común de Python. Lo usamos para guardar la loss en una lista o imprimirla. Con más de un elemento, explota. | [Tensor.item](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.item.html) |
| `.numpy()` | Convierte el tensor en un array de numpy, para graficarlo o compararlo. Comparte la memoria: no copia. | [Tensor.numpy](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.numpy.html) |
| `.detach()` | Devuelve el mismo tensor pero "desenganchado" de la historia de cuentas. Hace falta antes de `.numpy()` cuando el tensor salió de un modelo: PyTorch no te deja pasar a numpy algo que todavía se acuerda de cómo se calculó. | [Tensor.detach](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.detach.html) |
| `.clone()` | Una copia de verdad, independiente del original. En el early stopping la usamos para guardar los pesos del mejor momento: sin `clone`, la "foto" se seguiría moviendo con el entrenamiento. | [Tensor.clone](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.clone.html) |

**La cadena que más se repite:** `modelo(entrada).detach().numpy().ravel().round(5)`.
Leída de izquierda a derecha: predecí, desenganchá de la historia, pasá a
numpy, aplaná la tabla `(n, 1)` a una lista de `n`, redondeá. Las dos últimas
son de numpy (ver la sección 5).

---

## 2. Autograd: las pendientes

| en el notebook | qué hace | docs |
|---|---|---|
| `torch.tensor(3.0, requires_grad=True)` | "Acordate de las cuentas que te hagan." Sin esto no hay pendiente que calcular. Los parámetros de un `nn.Linear` ya vienen con esto puesto. | [cómo funciona autograd](https://docs.pytorch.org/docs/stable/notes/autograd.html) |
| `y.backward()` | Recorre las cuentas de la última a la primera aplicando la regla de la cadena y **anota** la pendiente en cada tensor que la pedía. No mueve nada. | [Tensor.backward](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.backward.html) |
| `x.grad` | Donde quedó anotada la pendiente. Ojo: cada `backward()` **suma** encima de lo que había (lo que se ve en la celda opcional sin `zero_grad`). | [Tensor.grad](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.grad.html) |
| `with torch.no_grad():` | "Lo que venga ahora no lo anotes." Para predecir o medir la validación, donde no vamos a entrenar: es más rápido y no ensucia los `.grad`. | [torch.no_grad](https://docs.pytorch.org/docs/stable/generated/torch.no_grad.html) |
| `torch.sin(x)` | El seno. Aparece como sugerencia en el TODO 1: autograd sabe derivar todas las funciones de `torch`. | [torch.sin](https://docs.pytorch.org/docs/stable/generated/torch.sin.html) |

Tutorial: [*Automatic Differentiation with torch.autograd*](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html).

**`detach()` y `no_grad()`, ¿no son lo mismo?** Casi. `no_grad` es un bloque:
nada de lo que pase adentro se anota. `detach` es sobre un tensor que ya existe:
te da una versión sin historia. En el notebook usamos `no_grad` cuando vamos a
hacer cuentas y `detach` cuando ya tenemos el resultado y lo queremos pasar a
numpy.

---

## 3. El modelo

| en el notebook | qué hace | docs |
|---|---|---|
| `nn.Linear(1, 16)` | Una capa que hace `x @ W.T + b`. Entra 1 número, salen 16. Trae sus pesos (`.weight`, forma `(16, 1)`) y sesgos (`.bias`, forma `(16,)`) inicializados al azar. | [nn.Linear](https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html) |
| `nn.ReLU()` | El doblez: `max(0, x)`, elemento por elemento. La rampa de la clase 2, como capa. | [nn.ReLU](https://docs.pytorch.org/docs/stable/generated/torch.nn.ReLU.html) |
| `torch.relu(...)` | La misma rampa, como función suelta. La usamos en la versión "a mano". | [torch.nn.functional.relu](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.relu.html) |
| `nn.Sequential(a, b, c)` | Encadena capas: la salida de una es la entrada de la siguiente. `modelo[0]` es la primera capa, `modelo[2]` la tercera. | [nn.Sequential](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sequential.html) |
| `modelo(x)` | Hacer pasar los datos por el modelo: la predicción. | [nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html) |
| `modelo.parameters()` | Todas las perillas del modelo, para dárselas al optimizador. | [Module.parameters](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.parameters) |
| `modelo.state_dict()` | Un diccionario con todas las perillas y sus valores actuales: la "foto" del modelo. | [Module.state_dict](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.state_dict) |
| `modelo.load_state_dict(foto)` | Volver a poner las perillas como estaban en la foto. Así vuelve el early stopping al mejor momento. | [Module.load_state_dict](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.load_state_dict) |
| `A @ B` | Multiplicación de matrices. Es la suma ponderada de la clase 2, para todos los casos y todas las rampas de una. | [torch.matmul](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html) |
| `W1.T` | La transpuesta: filas por columnas. Hace falta porque PyTorch guarda los pesos como `(salidas, entradas)`. | [Tensor.T](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor.T) |
| `torch.allclose(a, b, atol=1e-6)` | ¿Son iguales salvo por diferencias de redondeo? Así comprobamos que `nn.Sequential` y la fórmula a mano dan lo mismo. | [torch.allclose](https://docs.pytorch.org/docs/stable/generated/torch.allclose.html) |

Tutorial: [*Build the Neural Network*](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html).

---

## 4. El loop: loss, optimizador, semilla

| en el notebook | qué hace | docs |
|---|---|---|
| `nn.MSELoss()` | La loss de la clase 3: el promedio de los errores al cuadrado. `criterio(prediccion, y)` devuelve un tensor de un solo número. | [nn.MSELoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.MSELoss.html) |
| `torch.optim.SGD(modelo.parameters(), lr=0.15)` | El descenso por gradiente de la clase 3: cada perilla se mueve `lr × pendiente` en contra de la pendiente. | [optim.SGD](https://docs.pytorch.org/docs/stable/generated/torch.optim.SGD.html) |
| `torch.optim.Adam(..., lr=0.01)` | Descenso por gradiente con el paso ajustado perilla por perilla. Es el que usamos desde el TODO 2. | [optim.Adam](https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam.html) |
| `optimizador.zero_grad()` | BORRAR: pone en cero los `.grad` de todas las perillas. | [Optimizer.zero_grad](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.zero_grad.html) |
| `perdida.backward()` | ANOTAR: las pendientes de la loss respecto de cada perilla. | [Tensor.backward](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.backward.html) |
| `optimizador.step()` | MOVER: recién acá cambian las perillas. | [Optimizer.step](https://docs.pytorch.org/docs/stable/generated/torch.optim.Optimizer.step.html) |
| `torch.manual_seed(1983)` | Fija la semilla del azar de PyTorch: mismos pesos iniciales, mismos resultados. (`utils.fijar_semilla` hace esto y lo mismo para numpy.) | [torch.manual_seed](https://docs.pytorch.org/docs/stable/generated/torch.manual_seed.html) |

Tutorial: [*Optimizing Model Parameters*](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html),
que es el loop de las cinco líneas con otras palabras.

---

## 5. Lo de numpy que aparece en el medio

Una vez que el resultado pasó por `.numpy()`, lo que sigue es numpy.

| en el notebook | qué hace | docs |
|---|---|---|
| `.ravel()` | Aplana: de una tabla `(36, 1)` a una lista de 36. Es lo que piden los gráficos. | [numpy.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html) |
| `.round(5)` | Redondea a 5 decimales, para que se pueda leer al imprimir. | [numpy.round](https://numpy.org/doc/stable/reference/generated/numpy.round.html) |
| `.astype(int)` | Cambia el tipo: de `2005.0` a `2005`. | [ndarray.astype](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html) |
| `.tolist()` | De array a lista común de Python, para imprimirla linda. | [ndarray.tolist](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tolist.html) |
| `np.argmin(l_val)`, `.argmax()` | En qué **posición** está el mínimo (o el máximo), no cuánto vale. Así encontramos la mejor época. | [numpy.argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html) |
| `np.isfinite(...)` | ¿Es un número de verdad? Da `False` para `nan` e infinito: así detectamos el entrenamiento que explotó en el TODO 3. | [numpy.isfinite](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html) |
| `np.vstack`, `np.column_stack`, `np.ones` | Armar una tabla pegando columnas. Con eso armamos la matriz de la mejor recta. | [numpy.column_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html) |
| `np.linalg.lstsq(A, y)` | Mínimos cuadrados: la mejor recta, calculada de una, sin descenso. | [numpy.linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) |

---

## 6. Para dibujar la red

| en el notebook | qué hace | docs |
|---|---|---|
| `g.diagrama_de_red(modelo)` | Del curso, no de PyTorch: un círculo por neurona, una línea por peso. | `_shared/ssdl/README.md` |
| `draw_graph(modelo, input_size=(36, 1))` | De `torchview`: una caja por capa, con la forma de lo que entra y sale. Necesita Graphviz instalado. | [torchview](https://github.com/mert-kurttutan/torchview) |
