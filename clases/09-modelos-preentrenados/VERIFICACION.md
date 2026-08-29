# Verificación adversarial — Clase 9

**Usar modelos que ya existen, sin creerles** · `clases/09-modelos-preentrenados/`
Fecha: **2026-08-29**. Todo lo que dice acá se comprobó **corriendo el código y mirando las
imágenes**, no leyendo los archivos. Segunda pasada: la clase ya venía construida y
"verificada"; esta revisión desconfió de ese informe y volvió a medir todo desde cero.

---

## 1. Veredicto

**Se puede dar.** Se encontraron **11 problemas** y **se arreglaron los 11**. Tres eran
serios: una viz que decía lo contrario de lo que mostraba en el momento aha, una slide de
código que se comía su propio título al avanzar, y una slide que narraba cuatro números
reales de una tarea con las palabras de **otra** tarea. El resto son precisión de
lenguaje, legibilidad en proyector y tiempos declarados que no coincidían con los medidos.

| Chequeo | Resultado |
|---|---|
| Entregables completos | 6/6 (+ `medir-clase09.py`, datos medidos y figuras) |
| `nbformat` | válido · 54 celdas (23 código, 31 markdown) |
| `nbconvert --execute`, sin red | **0 errores**, 5 corridas |
| Tiempo del notebook (medido hoy, 5 corridas) | **19 · 20 · 20 · 21 s** con la máquina libre, **65 s** con la máquina ocupada |
| Figuras del notebook | 3, reproducibles **byte a byte** (`md5sum` idéntico) |
| `medir-clase09.py` | reproducible **byte a byte**: `datos-clase09.js` y `.json` idénticos |
| Consola del navegador | **0 errores** en `slides.html` y en las 3 viz |
| Requests externas (con `context.route` abortando `http(s)`) | **0** |
| Desbordes en las 40 slides | **0** a 1280×720 y a 1024×640, con los fragments revelados |
| Tema claro y oscuro | las 3 viz, sin colores hardcodeados (`grep` de `#hex`: 0) |
| Rutas absolutas o `https://` en `src`/`href` | **0** |
| Plan de tiempos | suma **120 min exactos** y es continuo |
| URLs marcadas `[VERIFICADA]` | **10/10 dan 200** con `curl`, hoy |
| Números de las slides | todos verificados contra la corrida del notebook o del script |

---

## 2. Lo que estaba mal, y qué se hizo

### Serios

**1. La viz de la matriz decía lo contrario de su propio momento aha.**
Con prevalencia al 5 % y el modelo bobo prendido —que es *el* momento de la clase— el panel
imprimía: *"Tu modelo le gana por **-8 puntos** — o sea, prácticamente nada."* El modelo no
le gana: **pierde**, y la slide y las notas dicen "el bobo te gana por 8 puntos". El aula
iba a leer en pantalla lo contrario de lo que el docente estaba diciendo.
*Arreglado* en `viz/matriz-de-confusion.html`: ahora hay tres redacciones según el signo
(*pierde por N puntos contra algo que no mira nada* / *le gana por +N — prácticamente nada*
/ *le gana por +N*). Reverificado moviendo los cuatro controles.

**2. La slide 12 se comía su propio título al avanzar.**
Es la única slide del curso que usa pasos de resaltado (`data-line-numbers="1-2|3-4|5-6"`).
El plugin de reveal **clona el `<code>` y lo pone en `position:absolute`**; como
`.reveal pre` no está posicionado en `curso.css`, el clon se anclaba a la `<section>` y
tapaba el título y el bloque entero. Se veía perfecto en la slide quieta y se rompía al
primer avance — o sea, exactamente en el aula.
*Arreglado* con dos reglas locales en `slides.html` (`.reveal pre { position: relative }`
y ocultar el bloque base mientras se ve un paso). Verificado paso por paso, con captura.
**Ojo, equipos de otras clases:** el defecto está en `_shared/css/curso.css` y va a morder
a cualquiera que use pasos de resaltado. Hoy no lo usa nadie más, por eso el arreglo se
hizo acá y no en el archivo compartido.

**3. Slide 23: los cuatro números eran de "política" y el texto decía "protesta".**
La slide narraba *"74 notas de **protesta** que el modelo encontró…"* y aclaraba abajo que
los cuatro números salen de la tarea *"¿es una nota sobre política?"*. Los números son
correctos (74/51/29/214, test de 368, y cierran con la precisión 0,59 y el recall 0,72 de
la slide 26), pero el sustantivo era de otra tarea. Quien fuera al notebook a buscarlos no
los iba a encontrar.
*Arreglado*: los cuatro casilleros hablan de "notas sobre política", y las notas del
docente avisan que si se cambia el sustantivo hay que cambiar **también** los números.

### Rigor

**4. Slide 17: macro-F1 presentado como accuracy.**
Decía *"el mejor modelo en castellano **acierta dos de cada tres**"* sobre un macro-F1 de
70,2 — y la nota del docente remataba *"acierta 70 de cada 100"*. En **la clase que
prohíbe decir una métrica sin su frase correcta**, confundir F1 con accuracy es el peor
error posible. *Arreglado*: ahora dice **70 de macro-F1, no de accuracy**, en una tarea de
tres clases, con el desvío (70,2 ± 0,2) y la instrucción explícita de no decir "acierta".
Los seis números de la tabla se reverificaron bajando `docs/TASKS.md` de pysentimiento con
`curl`: BETO 67,2 / 52,2 / 71,5 y RoBERTuito 70,2 / 55,3 / 74,1. **Coinciden exactamente.**

**5. Slide 5: la lectura sustantiva de los titulares no estaba comprobada.**
Los cuatro titulares existen en el corpus con la etiqueta y el medio que dice la slide
(comprobado contra `titulares-prensa-es.csv`), pero la afirmación *"las dos primeras hablan
de lo mismo"* estaba tomada del material previo sin leer las notas. Se leyeron: las dos son
sobre **supuestos daños de la vacuna del covid**, una es el desmentido (`El Universo`,
etiquetada VERDADERA) y la otra es **el texto de la afirmación desmentida, guardado con el
nombre del chequeador** (`AFPFactual`, etiquetada FALSA). *Mejorado*: la slide ahora dice
eso, que es más fuerte y es verificable. Dato agregado a las notas y comprobado:
**AFPFactual aparece 32 veces en el corpus y las 32 con etiqueta "falsa"**, así que un
modelo entrenado ahí puede terminar aprendiendo "¿esto lo publicó un chequeador?".

**6. Tiempo del notebook mal declarado (otra vez).**
`notas-docente.md` y `referencias.md` decían "entre 1 y 2 minutos", citando 58 s y 1 min
49 s. Medido hoy cinco veces con `nbconvert --execute`: **19, 20, 20 y 21 segundos** con la
máquina libre, y **65 s** en la única corrida que compartió CPU con otra cosa.
También decían "el cómputo propio son ~25 s", que es el número del corpus de discursos de
la clase 6, no el de este notebook: acá **los embeddings tardan 4 s y la curva entera 3 s**
(los imprime el propio notebook). *Arreglado* con el rango real y la explicación de por qué
varía (CPU libre contra CPU ocupada).

### Lenguaje y legibilidad

**7.** `viz/zero-shot-vs-finetune.html` escribía **"Le saca 0.05 de F1 a el diccionario"**.
Ahora contrae: *"al diccionario"*.
**8.** `viz/similitud-semantica.html` escribía **"quedan 1 hallazgos genuinos"** y
**"1 no vienen al caso"**. Ahora concuerda en singular y plural en los tres lugares.
**9.** El código de las slides 12 y 14 iba al `.5em` del CSS del curso: ilegible en un
proyector, justo en las dos slides donde el código **es** el contenido. Subido a `.72em`,
igual que la slide 4. **Reverificado que no desborda ninguna de las 40 slides.**
**10.** La figura `umbral.png` no tenía rótulo en el eje Y. Se agregó (`de 0 a 1`) en el
notebook y se regeneró.
**11.** El bloque práctico 1 prometía **"20 minutos"** en pantalla cuando el plan le da 16
(del minuto 26 al 42; los otros 4 son las consignas y la puesta en común). Un docente que
lee la slide en voz alta se atrasa 4 minutos justo antes de la pausa. Alineado a **15
minutos**, y la nota del docente explica de dónde sale.

Además, un ajuste de puesta en página: embebida en la slide 25, la viz de la matriz dejaba
el botón **"Copiar la oración"** —que es un entregable de la spec— 30 px por debajo del
borde del `<iframe>`. Ahora, sólo en modo embebido, el botón va al costado del título del
panel y **entra entero sin scrollear**, sin achicar el gráfico.

---

## 3. Lo que se verificó y estaba bien (no se tocó)

- **El notebook corre de punta a punta sin red y sin errores**, detectando solo que no hay
  Hugging Face (prueba la biblioteca **y** hace un `urlopen` a huggingface.co con timeout)
  y cayendo al camino B. Cinco corridas, 0 celdas con error, 3 figuras.
- **Todos los números de las slides salen de corridas reales y coinciden**:
  piso 0,72 · diccionario 0,75 / F1 0,40 · A 0,78 / 0,65 · C 0,83 / 0,67 · 1103 etiquetas ·
  test 368 · 28 % de positivos · precisión 59 y recall 72 · matriz 74/51/29/214 ·
  trampa del corpus 0,73/0,68 contra 0,44/0,22 · 332 de 346 medios con una sola clase ·
  kappa 0,46 con acuerdo 0,73. **Cada uno se leyó en la salida del notebook ejecutado hoy.**
- **`medir-clase09.py` es reproducible byte a byte**: se corrió de nuevo y `datos-clase09.js`
  y `datos-clase09.json` salieron idénticos a los versionados (`diff` limpio).
- **Los tres momentos aha ocurren de verdad**, comprobados moviendo los controles con
  Playwright y leyendo el DOM resultante:
  - *matriz*: prevalencia 50 % → 5 % sin tocar nada más: precisión **0,88 → 0,23**,
    accuracy **queda en 0,88**, el bobo saca **0,96**. Y con el umbral en 0,80 la precisión
    va a 0,99 y el recall se hunde a 0,42: **no hay corte donde suban las dos**.
  - *similitud*: `fútbol` → 1 por palabra clave, **7 por significado sin la palabra**
    (FIFA, Chivas, Cruz Azul), y el botón de falsos positivos marca 1. Contrapunto
    obligatorio verificado: con `vacuna`, **4 de 8 son basura y quedan 0 hallazgos
    genuinos**. Misma técnica, resultado opuesto.
  - *curva*: con 25 etiquetas la sofisticada saca **0,14** contra **0,45**; el cruce está
    cerca de las 680; y en la tarea Covid-19 el diccionario de **cero etiquetas** saca
    **0,87** y le gana a las dos con 800 encima. Todo coincide con `datos-clase09.json`.
- **Las 10 URLs `[VERIFICADA 2026-08-29]` devuelven 200** (probadas con `curl` hoy: los
  README de HF course, BETO, pysentimiento, sentence-transformers y FakeNewsCorpusSpanish;
  `docs/TASKS.md`; los tres paquetes de PyPI; y `chapters/es` del curso de HF).
  **Ninguna URL inventada.** Las 12 citas se revisaron una por una: autores, año, revista,
  volumen y páginas son plausibles y consistentes; ninguna parece fabricada.
- **Los datos sintéticos están rotulados donde corresponde**: la viz de la matriz dice al
  pie que sus 600 casos son simulados, y el kappa 0,46 lleva su chip *codificadores
  simulados* en la slide 29, en el notebook (sección 12) y en las notas.
- **La trampa central del corpus** (el detector de sátira) está dicha con todas las letras
  en la slide 32, en la sección 11 del notebook y en las notas, con los números medidos.
- **El cuestionario cierra**: las 12 preguntas cubren los 12 ítems de la spec, se pueden
  contestar con lo que se dio, los distractores son los errores reales (no absurdos), y
  **las cuentas de las soluciones son correctas** (rehechas a mano: precisión 0,67, recall
  0,60, accuracy 0,86, F1 0,63, piso 0,80).
- **El glosario de la clase 9 está completo** en `recursos/glosario.md` y coincide con la
  slide 38, término por término.
- **Los puentes están explícitos**: slide 2 hacia atrás (clases 1-8, el mini-GPT de ~1,5 M),
  slides 39-40 hacia adelante (desempeño ≠ validez, clase 10).
- **La clase no usa fórmulas**, así que KaTeX no tiene nada que renderizar; se cargó igual
  sin errores de consola.

---

## 4. Lo que queda abierto

1. **Nadie corrió el camino A (Hugging Face).** `huggingface.co` da 403 desde este
   contenedor. Los **tres identificadores de modelo existen y están bien escritos** —esta
   pasada cerró el que faltaba: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
   está en `docs/sentence_transformer/pretrained_models.md` del repositorio oficial, bajado
   con `curl`—, pero **bajar los pesos no se pudo probar**. Tarea escrita en
   `notas-docente.md` §10 para quien dé la clase por primera vez: correrlo en Colab y
   **anotar la revisión exacta (el hash del commit)** de cada modelo en `referencias.md`.
2. **Los números que están en pantalla son los del camino sin red.** Con Hugging Face van a
   ser otros —mejores— y hay que volver a correr `medir-clase09.py` y actualizar las slides
   28 y 32 y las figuras. Está dicho en `figuras/README.md`, en el pie de la viz de la
   curva y ahora también en las notas del docente.
3. **Quedan 8 marcas `[VERIFICAR URL]`** en `referencias.md` (Barberá 2021, Grimmer &
   Stewart 2013, Grimmer/Roberts/Stewart 2022, Krippendorff, Reimers & Gurevych,
   Ziems 2024, Salganik 2020, la página del curso de HF y el preprint de BETO). Las citas
   están completas y bien; faltan los enlaces porque arxiv.org, doi.org y las editoriales
   están bloqueados. **No se les inventó URL.**
4. **La casilla de transfer learning (10-25 min, 11 slides) sigue siendo la más apretada**:
   ~80 segundos por slide. Está marcada como tal en el plan y la lista de recortes ataca
   ahí. Conviene cronometrarla el primer dictado.
5. **Embebida en la slide 25, la viz de la matriz mide 806 px en un `<iframe>` de 610.**
   Todo lo importante entra (gráfico, los cuatro casilleros, las cuatro métricas con sus
   frases y el panel "traducción a tu paper" con su botón); lo que queda abajo es la caja
   "momento aha", que la slide ya repite en su `viz-pie`. Se puede scrollear adentro del
   iframe. Es la misma situación que las viz de la clase 6 (787 y 835 px), así que se dejó
   como está.
6. **`.reveal pre` no está posicionado en `_shared/css/curso.css`** (problema 2). Se arregló
   localmente en esta clase. Si otra clase agrega pasos de resaltado, va a chocar con lo
   mismo: conviene subir la regla al CSS compartido cuando no haya sesiones en paralelo
   editándolo.

---

## 5. Cómo reproducir esta verificación

```bash
# el notebook entero, sin red (medido: ~20 s con la máquina libre)
python3 -m nbconvert --to notebook --execute \
        --output /tmp/nb-09.ipynb clases/09-modelos-preentrenados/notebook.ipynb
git status --porcelain clases/09-modelos-preentrenados/figuras   # tiene que quedar limpio

# los datos de las viz, byte a byte
PYTHONPATH=_shared python3 clases/09-modelos-preentrenados/medir-clase09.py
git diff --stat clases/09-modelos-preentrenados/datos-clase09.*  # tiene que quedar limpio
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
ejecutable `/opt/pw-browsers/chromium`), abriendo por `file://` **a la profundidad real**,
con `context.route('**/*')` abortando cualquier `http(s)`, recorriendo las 40 slides con
`Reveal.slide(i)` y revelando todos los fragments antes de medir `scrollHeight`, y moviendo
los controles de las viz con `ctl.set(...)` para leer el DOM que resulta.

> **Nota de proceso.** Mientras se hacía esta verificación había otra sesión trabajando en
> la clase 7 en el mismo contenedor, que commiteó varias "Instantáneas de progreso" y se
> llevó puestos archivos de la clase 9 en el camino. **Esta verificación no hizo ningún
> commit**; los archivos en disco son los verificados.
