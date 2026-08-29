# `ssdl` — Social Science Deep Learning

El paquete de plomería del curso **Deep Learning para Cientistas Sociales**.

Acá **no** está el contenido del curso. El contenido está en los notebooks, en
las slides y en las visualizaciones. Acá está lo aburrido que si no habría que
copiar y pegar en diez notebooks: cargar los datos, fijar la semilla, dibujar
con los colores de siempre, correr el loop de entrenamiento.

**Regla de diseño.** Este paquete tiene permitido ahorrar tipeo. No tiene
permitido esconder ideas. Por eso `entrenar()` es el loop de cinco líneas de la
clase 4 con contabilidad alrededor, y no un `Trainer` opaco; por eso el PCA de
`proyeccion_de_embeddings` son tres líneas de numpy y no una importación de
sklearn. Si alguna vez te encontrás escribiendo una función de `ssdl` que
esconde algo que el estudiante todavía no hizo a mano, esa función va en el
notebook, no acá.

```
_shared/ssdl/
  __init__.py        los atajos de siempre
  datos.py           traer datos, tokenizar, partir en train/val/test
  graficos.py        figuras con la identidad visual y la semántica de color
  entrenamiento.py   el loop de la clase 4, explícito, con barra de progreso
  utils.py           semillas, device, contar perillas, medir tiempo
  test_ssdl.py       los tests (corrélos si tocás algo)
```

---

## Arranque

En un notebook, después de la celda de bootstrap (ver
`_shared/plantillas/notebook-plantilla.ipynb`):

```python
from ssdl import datos, entrenamiento as ent, graficos as g, utils

utils.fijar_semilla(1983)
utils.resumen_del_entorno()

anios, seguridad = datos.serie_menciones("seguridad")
g.plot_serie(anios, seguridad, titulo="Menciones a seguridad")
```

Desde la terminal, parado en la raíz del repo:

```bash
PYTHONPATH=_shared python3 -c "import ssdl; ssdl.hola()"
python3 _shared/ssdl/test_ssdl.py                       # los tests
python3 _shared/ssdl/test_ssdl.py --figuras /tmp/check   # figuras de muestra
```

---

## `ssdl.utils` — plomería

| función | qué hace |
|---|---|
| `fijar_semilla(semilla=1983, verboso=False)` | Fija `random`, `numpy` y `torch` de una. Devuelve la semilla. |
| `elegir_device(preferir_gpu=True, verboso=False)` | Devuelve un `torch.device`: cuda / mps / cpu. |
| `contar_parametros(modelo, solo_entrenables=True, detallado=False)` | Cuántas perillas tiene el modelo. Con `detallado=True` imprime la tabla capa por capa. |
| `medir_tiempo(que, verboso=True)` | Context manager. `with utils.medir_tiempo("entrenar"): ...` |
| `estamos_en_colab()` | `True`/`False`, preguntándole a Python (no adivinando por la ruta). |
| `estamos_en_notebook()` | Idem, para Jupyter o Colab. |
| `raiz_del_repo(desde=None)` | La carpeta del repo, buscándola por `DLSS_RAIZ` o subiendo carpetas. |
| `resumen_del_entorno(imprimir=True)` | Versiones, GPU, dónde encontró los datos. **La primera celda que conviene correr cuando algo no anda.** |
| `formatear_cantidad(n)` | `3141592` → `'3,1 M'`. |
| `formatear_duracion(s)` | `125.4` → `'2 min 5 s'`. |
| `SEMILLA_DEL_CURSO` | `1983`. |

```python
modelo = torch.nn.Linear(1, 1)
print(utils.contar_parametros(modelo))            # 2

with utils.medir_tiempo("entrenar el mini-GPT"):
    ent.entrenar(modelo, x, y, epocas=500)
# -> entrenar el mini-GPT: 4,2 s
```

---

## `ssdl.datos` — traer los datos

### Carga

| función | devuelve | real o sintético |
|---|---|---|
| `serie_menciones(tema, desde=1984, hasta=2019, suavizada=False)` | `(anios, valores)` numpy | **real** |
| `serie_completa(desde, hasta)` | dict con todos los temas + presidente | **real** |
| `discursos_apertura(anios=None)` | `{anio: texto}` | **real** |
| `corpus_mini_gpt(max_caracteres=None)` | un string | **real** |
| `discursos_casarosada(n=None)` | lista de dicts (orador, fecha, discurso) | **real** |
| `titulares_prensa(n=None, con_texto=False)` | lista de dicts | **real** |
| `debates_aguasclaras(max_caracteres=None)` | un string (~1 MB) | ⚠ **SINTÉTICO** |
| `prensa_aguasclaras()` | lista de dicts con `menciona_protesta` | ⚠ **SINTÉTICO** |
| `verdad_aguasclaras()` | dict: el padrón de la verdad | ⚠ **SINTÉTICO** |

`TEMAS_DISPONIBLES` es `["seguridad", "inflacion", "educacion", "trabajo", "salud"]`.
Los valores **ya vienen en porcentaje**: `0.42` quiere decir "el 0,42% de las
palabras del discurso".

```python
# la serie de las clases 1, 3 y 4
anios, seguridad = datos.serie_menciones("seguridad")

# la de la clase 2: dos picos y un valle, imposible para una recta
anios, inflacion = datos.serie_menciones("inflacion")

# el corpus del mini-GPT (clase 8), con la verdad al lado
corpus = datos.debates_aguasclaras()
verdad = datos.verdad_aguasclaras()
print([p["sigla"] for p in verdad["partidos"]])
```

**Aguasclaras se rotula siempre como sintético.** No es una formalidad: es la
diferencia entre una demostración didáctica y poner frases inventadas en boca
de gente real. La ventaja pedagógica es que conocemos el proceso generador, y
por eso en la clase 8 podemos poner la verdad al lado de la alucinación.

### Tokenizar

```python
tok = datos.TokenizadorCaracteres(corpus)     # o .ajustar(corpus) después
ids = tok.codificar("hola presidente")
tok.decodificar(ids)
len(tok)                                       # tamaño del vocabulario

tok = datos.TokenizadorPalabras(corpus, minimo=2)
tok.cobertura("la sesion berenjena")           # 0.667 -> una de cada tres es <desc>
tok.partir("hola, mundo")                      # ['hola', ',', 'mundo']

datos.vocabulario(corpus, top=20).most_common(5)
```

Los dos tienen `.fichas`, `.a_id`, `.a_ficha`, `.codificar`, `.decodificar` y
`len()`. El de palabras además tiene `.frecuencias` y reserva el id `0` para
`<desc>` (desconocida).

### Embeddings propios, sin red y sin Hugging Face

Coocurrencia → PPMI → SVD, con numpy y nada más. Es lo que hace andar el mapa de
palabras de la **clase 6** con el corpus real, y es el **plan B de la clase 9**
si Hugging Face no está disponible el día de la clase.

```python
texto = datos.corpus_mini_gpt()                 # 2,2 MB de discursos reales
V, palabras = datos.embeddings_ppmi_svd(texto)  # (4000, 100) en ~25 s en CPU

datos.vecinos("provincias", V, palabras, k=6)
# [('todas', .71), ('misiones', .69), ('provincia', .68), ('santiago', .66), ...]

M, pal = datos.matriz_de_coocurrencia(texto, top=4000, ventana=5)   # el paso 1 solo
```

Los vectores vienen **normalizados a norma 1**, así que `V @ V[i]` ya es la
similitud coseno y `graficos.proyeccion_de_embeddings(V, palabras)` los dibuja
directamente.

Tres cosas para tener a mano:

- **Tarda ~25 s** con el corpus completo (`top=4000`). Para probar rápido en
  clase, `datos.corpus_mini_gpt(400_000)` con `top=1200` baja a un par de
  segundos y los vecinos siguen teniendo sentido.
- **Las tildes cuentan.** `"educación"` está en el vocabulario; `"educacion"`
  no. `vecinos()` levanta `KeyError` con un mensaje que lo explica.
- Sólo entran palabras alfabéticas con al menos `minimo=5` apariciones. Las muy
  frecuentes (`de`, `que`) siguen adentro y a veces se cuelan como vecinas: es
  una buena oportunidad para discutir en clase por qué PPMI no las elimina del
  todo.

### Partir

```python
tr, va, te = datos.particion(len(X))                       # al azar 70/15/15
tr, va, te = datos.particion_temporal(anios, 2010, 2015)   # pasado -> futuro
tr, va, te = datos.particion_por_grupo([n["diario"] for n in notas])

datos.diagnostico_de_fuga(tr, te, grupos=diarios, textos=titulares)
# ✓ Sin fugas detectadas: train y test no comparten casos, grupos ni textos.
```

`diagnostico_de_fuga` imprime el veredicto en castellano y devuelve el dict.
Corrélo siempre: partir al azar datos de panel es hacer trampa sin darse cuenta.

### Datasets de juguete

Todos devuelven `(X, y)` con `X` de forma `(n, 2)` e `y` binaria, y todos
aceptan `n`, `ruido` y `semilla`.

```python
X, y = datos.espiral(300, clases=2)          # el imposible para una recta
X, y = datos.dos_lunas(300)
X, y = datos.circulos_concentricos(300)
X, y = datos.xor(300)                        # el que hundió a los perceptrones

x, y = datos.recta_con_ruido(40, a=2.0, b=1.0, ruido=1.0)
x, y, verdad = datos.curva_de_dos_picos(60)  # la curva objetivo de la clase 2

X_t, y_t = datos.a_tensores(X, y)            # a torch: floats y etiquetas long
```

---

## `ssdl.graficos` — las figuras

Se importa como `g` por convención. **El estilo se aplica solo al importar.**

### La semántica de color (esto no es decoración)

| constante | color | qué significa |
|---|---|---|
| `g.DATOS` | tinta | lo observado: la nube, el corpus |
| `g.VERDAD` | gris punteado | la verdad subyacente (sólo con datos sintéticos) |
| `g.MODELO` | azul | lo que el modelo dibuja |
| `g.PARAMETRO` | violeta | las perillas, los gradientes, el punto en el mapa |
| `g.ERROR` | rojo | el desajuste, la loss, los falsos positivos |
| `g.VAL` | naranja | lo que el modelo **no** vio: validación, test |
| `g.OK` | verde | aciertos |
| `g.ACENTO` | turquesa | "mirá acá" (sin significado técnico) |

Son los mismos de `_shared/css/curso.css`, y hay un test que falla si divergen.
`g.paleta()` te da el dict completo.

### Base

```python
fig, ax = g.figura(ancho=8, alto=5, titulo="...", xlabel="...", ylabel="...")
fig, ejes = g.figura(13, 4, filas=1, columnas=3, titulo="...")   # grilla
g.guardar(fig, "salida/figura.png")
g.estilo_curso(escala=1.4)          # letra más grande, para proyectar
g.estilo_curso(oscuro=True)         # paleta oscura, mismos roles
```

Todas las funciones aceptan `ax=` para dibujar dentro de una grilla, y todas
aceptan `titulo`/`xlabel`/`ylabel` **también** cuando les pasás un `ax`.

### Clases 1-2 — funciones y parámetros

```python
# la misma función con distintos valores de UN parámetro
g.plot_familia(lambda x, a: a * x**2, valores=[0.2, 0.5, 1, 2, 4],
               nombre_parametro="a", destacar=1)

g.plot_funcion(lambda x: np.maximum(0, x - 2), x=(0, 10))

g.plot_serie(anios, valores, etiqueta="menciones a seguridad")

# LA figura del curso: datos + curva + errores como segmentos rojos
g.plot_ajuste(x, y, modelo=lambda t: 2*t + 1,
              verdad=lambda t: 1.8*t + 2,     # gris punteado, opcional
              mostrar_errores=True, loss=None)  # loss=None -> calcula el MSE
```

### Clases 2-4 — clasificación en el plano

```python
g.scatter_clases(X, y, etiquetas=["no menciona", "menciona"])

g.frontera_de_decision(predecir, X, y)
```

`predecir` recibe una matriz `(n, 2)` de numpy y devuelve `(n,)`. Con un modelo
de PyTorch, envolvelo:

```python
def predecir(XX):
    with torch.no_grad():
        return torch.softmax(modelo(torch.tensor(XX, dtype=torch.float32)), -1)[:, 1].numpy()

g.frontera_de_decision(predecir, X, y)
```

### Clase 3 — el paisaje de la loss

```python
def loss_ab(a, b):
    return float(np.mean((y - (a*x + b))**2))

trayectoria, losses = ent.descenso_a_mano(
    lambda p: loss_ab(p[0], p[1]), [0.0, 0.0], lr=0.05, pasos=60)

fig, ejes = g.superficie_de_loss(loss_ab, rango_a=(-1, 5), rango_b=(-3, 6),
                                 trayectoria=trayectoria, optimo=(2.0, 1.0),
                                 modo="ambos")   # "contorno" | "3d" | "ambos"

# la versión 1D: la pendiente medida con una resta, sin nombrar la derivada
g.plot_loss_1d(lambda a: loss_ab(a, 1.0), rango=(-1, 5),
               punto=0.2, paso_de_prueba=0.4)
```

**Ojo con la escala de x.** Si `x` no está centrada, `a` y `b` quedan
correlacionadas, el valle es una zanja diagonal y el descenso zigzaguea
eternamente. Centrá `x` antes de dibujar el paisaje, salvo que el zigzagueo sea
justamente lo que querés mostrar.

### Clase 4 — entrenamiento

```python
g.curvas_de_entrenamiento(historial)                 # objeto Historial
g.curvas_de_entrenamiento(train=[...], val=[...])    # o listas sueltas
```

Azul lo que el modelo vio, naranja lo que no, y una marca verde en la mejor
época de validación.

### Clase 5 — imágenes

```python
g.grilla_de_filtros(modelo.conv1.weight, ncols=8)   # azul − · blanco 0 · rojo +
g.mostrar_imagenes(imgs, etiquetas=nombres, predicciones=predichos, ncols=8)
```

En `mostrar_imagenes`, si pasás `predicciones` los títulos salen verdes cuando
acertó y rojos cuando erró: el análisis de errores se hace mirando.

### Clase 6 — embeddings

```python
g.proyeccion_de_embeddings(vectores, palabras,
                           grupos=temas,              # colorea por grupo
                           resaltar=["diputado", "protesta"])
```

Si los vectores tienen más de 2 dimensiones, hace PCA (SVD de numpy, tres
líneas) y dice en el eje qué porcentaje de la variación estás viendo. **Decilo
en el aula:** esto es una sombra; dos palabras pueden verse pegadas acá y estar
lejísimos en las 300 dimensiones reales.

### Clase 7 — atención

```python
g.mapa_de_atencion(pesos, tokens, mascara_causal=True, cabeza=0)
```

Acepta `(n, m)` o `(cabezas, n, m)`. La aclaración de que **las filas suman 1 y
las columnas no suman nada** va impresa en el eje: es la confusión número uno al
leer estos heatmaps.

### Clases 9-10 — evaluación

```python
g.matriz_de_confusion(y_true, y_pred,
                      etiquetas=["no menciona protesta", "menciona protesta"],
                      nombre_positivo="menciona protesta")

m = g.metricas_binarias(y_true, y_pred)
# {'vp':.., 'fp':.., 'vn':.., 'fn':.., 'accuracy':.., 'precision':..,
#  'recall':.., 'f1':.., 'prevalencia':..}

g.frase_de_metricas(y_true, y_pred, fenomeno="titulares que mencionan protesta")
# De cada 100 casos que el modelo marcó como «...», 73 lo eran de verdad.
# De cada 100 casos que realmente eran «...», el modelo encontró 74.
# ...
```

**Regla de la casa:** prohibido reportar una métrica sin su frase en castellano
llano. Para eso está `frase_de_metricas`. Si no podés decirla en voz alta, no
entendiste tu propio resultado.

---

## `ssdl.entrenamiento` — el loop

```python
historial = ent.entrenar(
    modelo, x, y,
    x_val=x_val, y_val=y_val,
    perdida=torch.nn.MSELoss(),        # o CrossEntropyLoss() para clasificar
    optimizador=None,                  # None -> SGD con la lr de abajo
    lr=0.01,
    epocas=200,
    tam_lote=None,                     # None -> todos los datos en un lote
    paciencia=None,                    # un número -> parada temprana
    metrica=ent.exactitud,
    verboso=1,                         # 0 mudo · 1 barra · 2 una línea por época
    explicar=0,                        # narra las 5 estaciones N pasos
    semilla=1983,
)
```

Adentro pasa exactamente esto y nada más:

```python
prediccion = modelo(x)                          # 1. PREDECIR
perdida    = funcion_de_perdida(prediccion, y)  # 2. COMPARAR
optimizador.zero_grad()                         # 3. BORRAR
perdida.backward()                              # 4. ANOTAR
optimizador.step()                              # 5. MOVER
```

### El modo pedagógico (clase 4)

```python
ent.entrenar(modelo, x, y, epocas=50, explicar=1)
```

Narra las cinco estaciones del primer paso con los números de verdad: la loss,
los gradientes recién calculados, y los valores de cada perilla antes y después
del `step`. Sirve para que se vea que **`backward` no mueve nada, sólo anota
para dónde habría que moverse; recién `step` mueve.** Poné `explicar=1` o `2`,
no más: son 30 líneas por paso.

### `Historial`

```python
historial.train          # lista de loss de entrenamiento
historial.val            # lista de loss de validación
historial.metricas       # {"métrica": [...]}
historial.mejor()        # (época, valor) del mínimo de validación
historial.segundos
historial.detenido_temprano
historial.como_dict()    # serializable a JSON
historial.graficar()     # las dos curvas
```

### El resto

```python
loss, metrica = ent.evaluar(modelo, x_val, y_val, perdida, metrica=ent.exactitud)
y_hat = ent.predecir(modelo, x_test, como_numpy=True)

ent.exactitud(prediccion, y)             # proporción de aciertos
ent.error_absoluto_medio(prediccion, y)  # MAE, en las unidades de tus datos
ent.r_cuadrado(prediccion, y)            # el R² que ya conocés

parada = ent.ParadaTemprana(paciencia=15)
barra  = ent.BarraDeProgreso(total=100, etiqueta="entrenando")
```

### `descenso_a_mano` (clase 3)

Descenso por gradiente **sin torch y sin autograd**, con las pendientes
calculadas con una resta. Es la clase donde la palabra "derivada" todavía no se
pronunció.

```python
trayectoria, losses = ent.descenso_a_mano(
    lambda p: loss_ab(p[0], p[1]),   # loss(vector de parámetros) -> número
    parametros_iniciales=[0.0, 0.0],
    lr=0.05, pasos=60)
```

La idea entera son dos líneas:

```python
pendiente = (loss(p + h) - loss(p - h)) / (2*h)   # ¿para dónde sube?
p = p - lr * pendiente                            # entonces voy al revés
```

---

## Si tocás algo

```bash
python3 _shared/ssdl/test_ssdl.py                        # 114 tests
python3 _shared/ssdl/test_ssdl.py --figuras /tmp/check    # y mirá las figuras
```

Los tests incluyen los doctests de los módulos y uno que compara los colores
contra `curso.css`. Las figuras **hay que mirarlas**: un gráfico puede pasar
todos los `assert` y ser ilegible.
