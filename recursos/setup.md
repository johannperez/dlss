# Cómo poner todo a andar

> **Lo primero, porque cambia cómo leés el resto de esta página:** el camino
> recomendado es **Google Colab**, que no requiere instalar absolutamente nada.
> Abrís un link, corrés una celda y ya estás. Si elegís ese camino, con la
> sección 1 alcanza y podés saltear las demás hasta que las necesites.
>
> La sección de instalación local está para quien la quiera. No es el camino
> por defecto y no hace falta para cursar.

---

## 1. El camino recomendado: Colab (cero instalación)

Google Colab es un notebook de Python que corre en la nube, gratis, con una
cuenta de Google. La computadora que hace las cuentas es de Google, así que da
lo mismo si tu máquina es vieja.

**Los tres pasos:**

1. Andá a [colab.research.google.com](https://colab.research.google.com).
2. `Archivo` → `Abrir cuaderno` → pestaña **GitHub**. Pegá:
   `https://github.com/johannperez/dlss` y elegí la rama del curso.
   Abrí el notebook de la clase: `clases/01-funciones-y-parametros/notebook.ipynb`.
3. Corré la primera celda (la que dice **BOOTSTRAP**) con `Shift + Enter`.
   Va a tardar unos veinte segundos la primera vez: está bajando el repo del
   curso. Cuando termine imprime `Listo. Repo del curso en: /content/dlss`.

Listo. Ya podés correr el resto del notebook de arriba hacia abajo.

### Lo que conviene saber de Colab

- **`Shift + Enter`** corre la celda y pasa a la siguiente. Es el 90% de lo que
  vas a apretar.
- **Las celdas se corren en orden.** Si saltás una, las de abajo van a fallar
  porque les falta una variable. Cuando algo se pone raro:
  `Entorno de ejecución` → `Reiniciar y ejecutar todo`. Resuelve más problemas
  que cualquier otra cosa.
- **Tu copia es tuya.** Podés escribir, romper y experimentar. No estás tocando
  el repo del curso. Para guardar tus cambios: `Archivo` → `Guardar una copia
  en Drive`. Si no lo hacés, se pierden al cerrar.
- **La sesión se apaga sola** después de un rato de inactividad, y cuando eso
  pasa se borra todo lo que había en memoria. No es una falla: es cómo
  funciona. Volvé a correr desde la primera celda.
- **GPU:** sólo hace falta para el mini-GPT de la clase 8, y ni siquiera ahí es
  obligatoria (en CPU tarda unos minutos más). Si la querés:
  `Entorno de ejecución` → `Cambiar tipo de entorno de ejecución` → `T4 GPU`.
  Ojo: cambiar esto **reinicia la sesión**, así que hacelo antes de empezar.

---

## 2. El camino local (opcional)

Si preferís trabajar en tu máquina. Necesitás **Python 3.10 o más nuevo**.
Verificá qué tenés:

```bash
python3 --version
```

### 2.1 Bajar el repo

```bash
git clone https://github.com/johannperez/dlss
cd dlss
```

Si no tenés `git`, se puede bajar el ZIP desde la página de GitHub
(`Code` → `Download ZIP`) y descomprimirlo.

### 2.2 Un entorno virtual

Un *entorno virtual* (venv) es una carpeta con su propia copia de Python y sus
paquetes. Sirve para que instalar cosas para este curso no te rompa otro
proyecto que tengas andando. Es una carpeta y nada más: si algo sale mal, la
borrás y la volvés a hacer.

**En Linux o macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**En Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Vas a ver `(.venv)` al principio de la línea de tu terminal. Eso quiere decir
que está activado. **Hay que activarlo cada vez que abrís una terminal nueva.**

### 2.3 Instalar

```bash
pip install --upgrade pip
pip install torch numpy matplotlib scikit-learn pandas jupyterlab
```

`torch` es el más pesado (unos cientos de MB) y puede tardar varios minutos.
La versión de CPU alcanza para todo el curso salvo, si querés apurarlo, el
mini-GPT de la clase 8.

### 2.4 Probar que anda

Parado en la raíz del repo:

```bash
PYTHONPATH=_shared python3 -c "import ssdl; ssdl.hola()"
```

Tiene que imprimir las versiones y terminar con:

```
✓ Datos OK: la serie de menciones a seguridad tiene 36 años (1984-2019).
```

Si eso salió, tenés todo lo que hace falta.

### 2.5 Abrir los notebooks

```bash
jupyter lab
```

Se abre el navegador solo. Navegá hasta `clases/01-.../notebook.ipynb`.
La celda de bootstrap detecta que estás local y no instala ni clona nada.

---

## 3. Cómo se abren las slides

Las slides son **archivos HTML comunes**. No hace falta ningún programa
especial, ni internet:

- **Doble clic** en `clases/01-funciones-y-parametros/slides.html`. Se abren en
  tu navegador.
- Flechas `←` `→` para moverte. `Esc` te muestra el mapa de todas las slides.
  `S` abre las notas del docente. `F` pantalla completa.

Todo el curso funciona **sin internet**: reveal.js y las fórmulas están
guardadas adentro del repo, en `_shared/vendor/`. No se baja nada de ningún
lado.

## 4. Cómo se abren las visualizaciones

Igual: **doble clic** en cualquier archivo de `clases/NN-slug/viz/*.html`.

Son páginas sueltas, sin dependencias y sin internet. Movele todos los
controles: están hechas para eso. Varias tienen un botón que muestra el caso
donde la técnica **falla** — apretalo, es la mitad del contenido.

> Si abrís una viz y ves la página en blanco o sin estilos, mirá el error #10
> de acá abajo.

---

## 5. Si algo explota

No hay error acá que no haya cometido el docente. Buscá tu mensaje en esta
lista; están en orden de frecuencia real.

---

### 1. `ModuleNotFoundError: No module named 'ssdl'`

**Qué pasó.** Python no sabe dónde está el paquete del curso. Casi siempre es
porque no corriste la celda de bootstrap, o porque el kernel se reinició y se
olvidó de todo.

**Solución.** Corré la celda **BOOTSTRAP** (la primera del notebook) y después
la de imports. Si ya lo hiciste y sigue fallando:
`Entorno de ejecución` → `Reiniciar y ejecutar todo`.

Desde la terminal, el equivalente es correr parado en la raíz del repo y con:

```bash
PYTHONPATH=_shared python3 mi_script.py
```

---

### 2. `ModuleNotFoundError: No module named 'torch'`

**Qué pasó.** Falta instalar PyTorch, o estás en una terminal donde el venv no
está activado.

**Solución.**

```bash
source .venv/bin/activate      # en Windows: .venv\Scripts\Activate.ps1
pip install torch
```

Si en la terminal no ves `(.venv)` al principio de la línea, el venv **no**
está activado y `pip` está instalando en otro lado.

---

### 3. `FileNotFoundError: No encuentro .../datos/muestras/...`

**Qué pasó.** El paquete encontró el código pero no los datos. Suele ser que
abriste el notebook desde afuera del repo, o que el clon quedó a medias.

**Solución.** En Colab: volvé a correr el bootstrap. En tu máquina: fijate que
el notebook esté **adentro** de la carpeta `dlss`. Para verificar:

```python
from ssdl import utils
utils.resumen_del_entorno()
```

La línea `raiz_del_repo` te dice dónde está buscando. Si dice
`(no encontrada)`, moviste el notebook fuera del repo.

---

### 4. `NameError: name 'seguridad' is not defined`

**Qué pasó.** Corriste las celdas fuera de orden, o reiniciaste el kernel y
seguiste desde el medio. Python no recuerda nada de antes del reinicio, aunque
en pantalla sigan viéndose los resultados viejos.

**Solución.** `Entorno de ejecución` → `Reiniciar y ejecutar todo`.
Que las salidas viejas sigan en pantalla es la trampa: son un dibujo, no un
estado.

---

### 5. `RuntimeError: mat1 and mat2 shapes cannot be multiplied (36x1 and 2x1)`

**Qué pasó.** Las formas de los tensores no encajan. Es **el** error de PyTorch,
y lo vas a ver muchas veces. El mensaje te dice exactamente qué pasó: tenés algo
de 36×1 y el modelo esperaba algo de ...×2.

**Solución.** Imprimí las formas antes de la línea que falla:

```python
print(x.shape, y.shape)
```

El 99% de las veces falta un `.reshape(-1, 1)`: PyTorch quiere que los datos
sean una matriz de `(casos, características)`, aunque haya una sola
característica.

```python
x = torch.tensor(anios, dtype=torch.float32).reshape(-1, 1)
```

---

### 6. `RuntimeError: expected scalar type Long but found Float`

**Qué pasó.** Estás clasificando y `CrossEntropyLoss` quiere las etiquetas como
**enteros** (`long`), no como decimales.

**Solución.**

```python
y = y.long()                       # las etiquetas de clase van como enteros
```

`datos.a_tensores(X, y)` ya hace esto solo: deja los enteros como enteros y
pasa el resto a `float32`.

---

### 7. La loss da `nan`

**Qué pasó.** Casi siempre el `lr` (learning rate, el tamaño del paso) es
demasiado grande: el modelo pega un salto enorme, se va al infinito y de ahí no
vuelve. Es la "firma del fracaso" de la clase 3.

**Solución.** Bajá el `lr` por un factor de 10 y volvé a probar:

```python
ent.entrenar(modelo, x, y, lr=0.001, epocas=200)   # en vez de 0.1
```

Si no alcanza, fijate que tus datos no tengan valores gigantes ni `nan`:

```python
print(np.isnan(x).any(), x.min(), x.max())
```

---

### 8. La loss baja un poco y después hace cualquier cosa

**Qué pasó.** Si escribiste el loop a mano, lo más probable es que te falte
`optimizador.zero_grad()`. Sin esa línea los gradientes **se acumulan** de una
vuelta a la otra y el modelo se vuelve loco.

**Solución.** El orden es este, y las cinco líneas van siempre juntas:

```python
prediccion = modelo(x)
perdida = funcion_de_perdida(prediccion, y)
optimizador.zero_grad()      # ← la que todos nos olvidamos
perdida.backward()
optimizador.step()
```

Es el error número uno de PyTorch. Lo cometemos todos, siempre.

---

### 9. Colab dice "Tu sesión se reinició" o se desconecta

**Qué pasó.** Colab apaga las sesiones inactivas y las que llevan muchas horas.
Se pierde todo lo que estaba en memoria (variables, modelos entrenados). Los
archivos que hayas guardado en `/content` también.

**Solución.** Volvé a correr desde la primera celda. Para no perder trabajo:
`Archivo` → `Guardar una copia en Drive` cada tanto, y si entrenaste algo que
tardó, guardalo en tu Drive antes de irte a almorzar.

---

### 10. Abro una viz o unas slides y veo la página en blanco, o sin estilos

**Qué pasó.** Dos causas posibles:

**(a) Abriste una plantilla en su lugar.** Los archivos de
`_shared/plantillas/` apuntan a los estilos con rutas pensadas para su destino
final (`clases/NN-slug/viz/`). Se ven bien una vez copiados a la carpeta de una
clase, no desde `plantillas/`. Es esperable, no es una falla.

**(b) Tu navegador está bloqueando archivos locales.** Algunos navegadores son
estrictos con `file://`. La solución literal es levantar un servidor local:
parado en la raíz del repo,

```bash
python3 -m http.server 8000
```

y después abrí `http://localhost:8000/clases/01-funciones-y-parametros/slides.html`
en el navegador. Para cortarlo, `Ctrl + C` en la terminal.

---

### 11. `SyntaxError: invalid syntax` apuntando a una línea que se ve bien

**Qué pasó.** El error casi siempre está en la línea **anterior**: un paréntesis
o una comilla sin cerrar. Python se da cuenta recién en la línea siguiente.

**Solución.** Mirá la línea de arriba de la que te marca y contá paréntesis.

---

### 12. `IndentationError` / `TabError`

**Qué pasó.** En Python la sangría es sintaxis, no estética. Mezclaste tabs con
espacios, o pegaste código con una sangría distinta.

**Solución.** Usá siempre **4 espacios** y nunca tabs. En Colab, seleccioná el
bloque y `Ctrl + ]` / `Ctrl + [` para mover la sangría entera.

---

### 13. Entreno dos veces y me dan números distintos

**Qué pasó.** No es una falla: los modelos arrancan con perillas al azar. Sin
fijar la semilla, cada corrida es distinta.

**Solución.**

```python
from ssdl import utils
utils.fijar_semilla(1983)
```

Ponelo **antes** de crear el modelo, no después. Y anotá la semilla en tu
paper: de eso se trata la clase 10.

---

### 14. Tarda una eternidad

**Qué pasó.** Casi todo el curso corre en segundos en CPU. Si algo tarda
minutos, revisá que no hayas puesto un número de épocas de más (un `5000` donde
iba `500`), o un dataset entero donde iba una muestra.

**Solución.** Cortá la celda (el botón de stop, o `Ctrl + M` `I` en Colab),
bajá el número y volvé a probar. Para saber cuánto tarda algo:

```python
with utils.medir_tiempo("entrenar"):
    ent.entrenar(modelo, x, y, epocas=200)
```

---

## 6. Si nada de esto resolvió tu problema

Antes de preguntar, corré esto y pegá la salida junto con tu pregunta:

```python
from ssdl import utils
utils.resumen_del_entorno()
```

Y del error, **pegá el mensaje completo**, no sólo la última línea. La parte de
arriba del `Traceback` dice en qué línea de qué archivo se rompió, que es
justamente lo que hace falta para ayudarte.

Preguntar bien es una habilidad, y es la misma que vas a usar cuando tengas que
explicarle a un revisor por qué tu modelo hace lo que hace.
