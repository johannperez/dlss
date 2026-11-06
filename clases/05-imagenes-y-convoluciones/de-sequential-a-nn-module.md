# De `nn.Sequential` a `nn.Module`

**En la clase 4 escribimos los modelos con `nn.Sequential`. En la clase 5 los
escribimos como una clase con `__init__` y `forward`. Es la misma red: cambia
cómo se escribe, no qué calcula.**

---

## La misma red, de las dos maneras

```python
# Clase 4: una lista de capas. El dato pasa por ellas en ese orden.
modelo = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 64),
    nn.ReLU(),
    nn.Linear(64, 10),
)
```

```python
# Clase 5: una clase. Decís qué capas hay y, aparte, por dónde pasa el dato.
class RedDensa(nn.Module):

    def __init__(self, n_clases=10):
        super().__init__()                     # siempre, antes de crear capas
        self.aplanar = nn.Flatten()
        self.capa1 = nn.Linear(28 * 28, 64)
        self.capa2 = nn.Linear(64, n_clases)

    def forward(self, x):
        x = self.aplanar(x)
        x = torch.relu(self.capa1(x))
        return self.capa2(x)


modelo = RedDensa()
```

Las dos tienen 50.890 perillas. Si les ponés los mismos pesos, dan la misma
salida (lo probamos).

- **`__init__` son las perillas:** qué capas tiene la máquina.
- **`forward` es el dibujo:** por dónde pasa el dato, y en qué orden.

La idea que ordena todo: **`nn.Sequential` también es un `nn.Module`**, uno que
ya trae escrito un `forward` que pasa el dato por cada capa, en fila. Al heredar
de `nn.Module`, ese `forward` lo escribís vos.

---

## Qué cambia

| | `nn.Sequential` | clase que hereda de `nn.Module` |
|---|---|---|
| **El recorrido del dato** | siempre en fila, una capa tras otra | el que escribas: es código Python |
| **Cómo llegás a una capa** | por posición: `modelo[1]` | por nombre: `modelo.capa1` |
| **Nombres en `state_dict()`** | `1.weight`, `3.weight` | `capa1.weight`, `capa2.weight` |
| **Entradas y salidas** | un tensor entra, un tensor sale | las que quieras |
| **Métodos propios** | no | sí, como `por_dentro` en la CNN |

**Lo que no cambia:** se llama igual (`modelo(x)`), se entrena con el mismo loop
y `modelo.parameters()` devuelve las perillas igual.

---

## Cuándo usar cada una

**`nn.Sequential` alcanza** si el dato pasa en fila por las capas y no necesitás
nada más. Es más corto y se lee de un vistazo.

**Hace falta una clase** cuando la red no es una fila, o cuando querés hacer algo
más con ella. En este curso:

- **Mirar adentro.** `RedConvolucional.por_dentro` devuelve los mapas de las tres
  capas (clase 5, sección 5).
- **Repetir capas con un `for`.** `MiniTransformer` recorre sus bloques en un loop
  (clase 7).
- **Recibir más de una entrada.** `MiniGPT.forward(idx, objetivos)` recibe las
  fichas y, si se las das, las respuestas correctas (clase 8).

---

## Cuatro cosas que confunden

1. **Se llama `modelo(x)`, no `modelo.forward(x)`.** Nunca vas a ver una línea que
   llame a `forward` desde afuera: `nn.Module` lo llama por vos cuando usás
   `modelo(x)`, y de paso hace otros trámites internos.
2. **Las capas tienen que colgar de `self`, y las listas son `nn.ModuleList`.** Si
   guardás las capas en una lista común de Python, PyTorch no las ve: el modelo
   queda con 0 perillas y no da error. Por eso la clase 7 usa `nn.ModuleList`.
3. **`print(modelo)` no muestra el recorrido.** Lista las capas en el orden en que
   las creaste en `__init__`, no el orden en que las usa `forward`. Y no muestra
   lo que no es una capa: en `RedDensa`, el `torch.relu` no aparece en el `print`.
   El recorrido real está en `forward`.
4. **`super().__init__()` no se puede saltear.** Sin esa línea, Python frena con
   `cannot assign module before Module.__init__() call`.

---

## Para leer más

- Tutorial: [*Build the Neural Network*](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html)
- Documentación: [`nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html) y [`nn.Sequential`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Sequential.html)
