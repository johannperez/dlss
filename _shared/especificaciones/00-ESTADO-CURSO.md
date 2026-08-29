# Estado del curso — verificación final del conjunto

**Las diez clases se construyeron y verificaron una por una. Esto es la revisión
del conjunto: lo que sólo se ve mirando las diez juntas.** Fecha: **2026-08-29**.

Todo lo que dice acá se comprobó **corriendo el código**, no leyéndolo:
`nbconvert --execute` sobre los diez notebooks, Chromium por Playwright
interceptando la red sobre las 50 páginas HTML, `curl` contra cada URL de la
bibliografía, `unittest` y `doctest` sobre el paquete de Python, y mirando los
PNG con los ojos.

> **Este documento reemplaza a `00-ESTADO-ESPINA.md` como estado vigente.** Ese
> otro se deja como registro histórico de la base compartida; su **sección 5 —las
> trampas del entorno y de los datos— sigue siendo lectura obligatoria** y no
> cambió.

---

## 1. Veredicto

**El curso está completo y es apto para dictarse.**

| Chequeo | Resultado |
|---|---|
| Los 10 notebooks con `nbconvert --execute` | **10 de 10 en verde**, 0 errores, sin red |
| Tiempo total de los 10 notebooks | **8 min 51 s** en CPU (el 62 % es la clase 8) |
| Las 50 páginas HTML por `file://`, con la red abortada | **0 errores de consola, 0 requests externas** |
| Scroll horizontal a 1280 px (proyector) y a 760 px | **0 páginas** de 50 |
| Enlaces internos (`src`/`href` de HTML, links de los `.md`) | **0 rotos** de 42 en `index.html` y 0 en los `.md` |
| `python3 _shared/ssdl/test_ssdl.py` | **119 tests, todos pasan** |
| `python3 datos/preparar_corpus.py` | **28 doctests, todos pasan** + informe |
| URLs de la bibliografía probadas con `curl` | **58 probadas**: 52 dieron 200 |
| Portadas de las 10 clases, miradas una al lado de la otra | **consistentes**: misma tipografía, misma franja, misma jerarquía |
| Puentes clase N → N+1 | **9 de 9 cierran**, textualmente |
| Metáfora del dibujo con callback explícito | **10 de 10** (dos se agregaron acá) |
| Slide de pausa · slide de glosario · bloque `[EL LUNES]` | **10, 10 y 10** |

**Inventario:** 10 `slides.html` (**381 slides**), **39 visualizaciones**, 10
notebooks, 10 `notas-docente.md`, 10 cuestionarios con solución, 10
`referencias.md`, 9 scripts de medición, 5 corpus. 82 MB en total (13 MB son los
dos checkpoints del mini-GPT de la clase 8).

---

## 2. Los tiempos de los notebooks (medidos, uno detrás de otro)

`python3 -m nbconvert --to notebook --execute`, CPU, sin GPU, sin red externa:

| Clase | Segundos | | Clase | Segundos |
|---|---:|---|---|---:|
| 01 funciones y parámetros | 8,0 | | 06 texto y embeddings | 18,8 |
| 02 componer funciones | 9,3 | | 07 attention | 15,5 |
| 03 loss y gradiente | 8,7 | | **08 mini-GPT** | **329,0** |
| 04 entrenar de verdad | 28,8 | | 09 pre-entrenados | 17,3 |
| 05 imágenes | 81,1 | | 10 criterio | 14,6 |

**Total: 531 s (8 min 51 s).** En Colab gratis (2 vCPU compartidas) contá entre
una y dos veces eso. Estos números están publicados en `index.html`, en
`README.md` y en `recursos/GUIA-DEL-DOCENTE.md` §3.

**Lo que sigue sin medir:** el tiempo del notebook de la clase 8 en **GPU T4**.
Este contenedor no tiene GPU (`torch.cuda.is_available()` es `False`). El pedido
está escrito en el propio notebook y en las notas de la clase 8, dirigido a quien
lo corra por primera vez en Colab. **No se inventó ningún número.**

---

## 3. Qué se arregló en esta pasada

### 3.1 Tres defectos de la base compartida que golpeaban a varias clases

Los diez equipos los encontraron por separado y los parchearon localmente para no
pisarse entre ellos. **Ahora están arreglados una sola vez, en la espina, y los
parches locales se sacaron.**

**1. `.reveal pre code` sin `display:block` — el código se veía cortado en el
proyector.** `curso.css` estilizaba el bloque pero el `<code>` quedaba
`display:inline`, así que el padding se le iba para arriba y el bloque se salía
de su caja. Afectaba a **16 bloques de código en siete clases**; las clases 7 y
10 lo tenían roto en ese momento, y las 1, 4, 6, 8 y 9 lo habían parcheado a mano.
*Arreglado en `_shared/css/curso.css`*: `display:block; overflow:auto;
box-sizing:border-box; width:100%`. Verificado por screenshot en las clases 2, 7,
9 y 10.

**2. `Viz.botonTema()` aplicaba el tema oscuro guardado pero dibujaba con la
paleta clara.** Leía `localStorage`, ponía `data-tema="oscuro"` en el `<html>`… y
no llamaba a `recargarColores()` ni redibujaba. Cualquier viz abierta después de
haber puesto el tema oscuro en otra salía con el fondo oscuro y los colores
claros encima. Afectaba a **las 39 visualizaciones**.
*Arreglado en `_shared/js/viz.js`*: dos líneas adentro de `botonTema()`, y los
cinco parches locales de la clase 2 se reemplazaron por un comentario correcto.
Verificado abriendo dos viz con `localStorage['dlss-tema']='oscuro'` precargado.

**3. Faltaba `box-sizing: border-box` en las cuatro cajas con padding propio.**
Cualquier `.viz-frame`, `.panel`, `.viz-pagina` o `.viz-con-panel` con padding se
volvía más ancha que su columna y se montaba encima de lo de al lado, o generaba
scroll horizontal en ventana angosta. Parcheado a mano en **más de 20 archivos**
de seis clases. *Arreglado en `curso.css`*, con dos reglas más de la misma
familia que también estaban sueltas: `.reveal pre { position: relative }` (sin
eso, los pasos de `data-line-numbers="1-2|3-4"` clonan el `<code>` en
`position:absolute` y se comen el título de la slide — le pasaba a la clase 9) y
`.reveal sup / sub` (el reset de reveal los aplana, y `10`<sup>`16`</sup> se leía
"1016" — le pasaba a la clase 3). Y una cuarta: el botón flotante **TEMA** se
montaba encima de la última línea de cualquier viz suelta larga; ahora la página
le deja su lugar.

Resultado medido: **0 de 50 páginas con scroll horizontal a 760 px** (antes eran
al menos cinco) y **0 a 1280 px**.

### 3.2 Incoherencias entre clases

**4. El mini-GPT tardaba diez minutos en la clase 9 y siete en la clase 8.** La
clase 8 mide y declara **4 a 7 minutos**; la clase 9 lo citaba como "diez
minutos" en dos lugares y "1 MB de texto" donde la 8 dice 1,1 MB. *Arreglado en
la clase 9 y en el gancho de la clase 8 dentro de `PROGRAMA.md`.* El tamaño del
modelo —**~1,5 millones de perillas, 1.541.056 exactas**— sí era consistente en
las diez clases.

**5. La clase 7 declaraba un modelo que su propio notebook no arma.** La tarjeta
decía *"2 bloques, 4 cabezas, ~0,5 M de perillas"* mientras el diagrama de al
lado mostraba **seis** bloques y el notebook construye
`MiniTransformer(vocab=3000, dim=96, cabezas=4, capas=6, ctx=24)` = **1.249.536
perillas**. *Arreglado*: la tarjeta dice ahora "6 bloques, 4 cabezas, ~1,25 M de
perillas. Armado y apagado: lo entrenamos la clase que viene", que además cose
mejor el puente a la clase 8.

**6. El desajuste de las 32 rampas se escribía distinto en la clase 2 y en la 4.**
`0.00001` contra `0.000014`. Es la siembra del sobreajuste y se cobra
textualmente. *Arreglado*: la clase 2 usa el número medido, `0.000014`.

**7. El zoo de la clase 1 tenía seis formas en la slide y otras seis en la viz.**
La slide 19 mostraba **escalón** como sexta forma y no lo explicaba en ninguna
parte (las slides 20-24 cubren cinco); la viz muestra **la rampa** en ese lugar, a
propósito, como siembra de la clase 2. *Arreglado*: el escalón se explica en una
línea en el pie de la slide 19 (con su nota para el docente sobre por qué no se
usa como pieza: no tiene pendiente), y la slide de la viz avisa con todas las
letras que ahí hay una forma que no estaba en la lista y que es la protagonista
de la clase que viene.

**8. La metáfora del dibujo se cortaba en las clases 7 y 9.** `PROGRAMA.md` pide
un `[CALLBACK DIBUJO]` explícito en las diez y estaba en ocho: la clase 7 sólo lo
tenía en un comentario de código y la 9 no lo tenía. *Arreglado*: la clase 7 lo
dice en el pie de su viz central (*"seguimos dibujando: en la clase 1 la máquina
dibujaba una curva; en la 6, el mapa donde viven las palabras; hoy cada palabra
dibuja su propio mapa de a quién mira"*) y la clase 9 en la slide del informante
clave (*"hoy no dibujamos desde cero: agarramos a alguien que ya sabe dibujar"*),
las dos con la marca `callback dibujo` y la instrucción en las notas del docente.
Verificado que las dos entran enteras en la slide a 1280×720.

**9. Dos contradicciones entre documentos que nadie tenía autoridad para
resolver.** Las resolví como cierre del curso, y la regla quedó escrita en
`PROGRAMA.md`:
- **Cuando los minutos de `PROGRAMA.md` y los de `notas-docente.md` no
  coinciden, manda el de la clase.** El programa es el presupuesto de diseño; las
  notas son el plan operativo medido contra las slides que existen. Hoy difieren
  en dos clases (el práctico 2 de la 2 y el juicio de la 10) y las dos declaran y
  justifican la desviación. Las diez siguen sumando 120 minutos y la pausa de 10
  no se toca en ninguna.
- **El cuestionario de la clase 10 declara 50 minutos y el programa dice 15.**
  Manda el archivo de la clase, con la instrucción explícita de usar sus cinco
  preguntas mínimas para los 15 minutos de rutina y dejar el resto como
  integrador o como parte del proyecto final.

### 3.3 Un defecto de figura y un desborde

**10. Faltaba `set_aspect("equal")` en el panel del medio de la figura del
descenso** (celda 25 del notebook de la clase 3): el mismo valle se veía redondo
en la celda 15 y elíptico en la 25. *Arreglado y el notebook re-corrido* (8,5 s).

**11. `viz/sesgo-en-el-espejo.html` de la clase 10 desbordaba 7 px a 760 px.**
Última página del curso con scroll horizontal. *Arreglada* con `box-sizing` y
`min-width:0`.

### 3.4 Los cuatro entregables transversales

**12. `recursos/glosario.md`, rehecho.** **169 entradas** organizadas por la clase
donde el término aparece **por primera vez**, más 11 falsos amigos y un índice
alfabético de 171 términos. Cada entrada trae ahora cuatro cosas: el término
como se dice en la práctica, cómo lo decimos en castellano, **qué es en una línea
sin jerga**, y **la analogía que se usa en clase**. Los términos se sacaron por
`grep` sobre las diez `slides.html`, los diez `notebook.ipynb` y las diez
`notas-docente.md`, no de memoria: se agregaron unos 40 que se usaban en el aula
y no estaban (p-hacking, preregistro, validación cruzada, stride/padding,
sandbox, MLP, logits, checkpoint, TF-IDF, muestra estratificada, scraping,
consentimiento, interpretabilidad, hiperparámetro, spaCy, gensim, word2vec,
Hugging Face, BETO, RoBERTuito, accuracy, dying ReLU, proxy, modelo, familia de
funciones…).

**13. `recursos/bibliografia.md`, consolidado y con las URLs probadas.** **85
obras**, sin repetir, con la clase donde se usa cada una. Se corrió `curl` sobre
**58 URLs**: 52 dieron 200. Se agregaron 11 **espejos verificados** —repositorios
oficiales que sí abren de obras cuyo enlace canónico está bloqueado— con la marca
`[ESPEJO VERIFICADO]`, que **no** hace pasar el espejo por el enlace de la obra.
Se agregaron siete obras que estaban en un `referencias.md` de clase y faltaban
acá (Krizhevsky 2012, LeCun 1998, Reimers & Gurevych 2019, Gómez-Adorno et al.
2021, la guía de `scikit-learn`, el tutorial *Training a Classifier* de PyTorch y
`minbpe`). Y se arregló una URL que daba 404 en la clase 6 (una ruta de
directorio: `raw.githubusercontent.com` no lista directorios; lo que se verifica
es cada archivo).

> **No se eliminó ninguna cita por sospecha de invención.** Se auditaron las 85 y
> las 85 tienen autores, año y publicación completos y plausibles. **Una sola
> quedó marcada `[VERIFICAR — cita no confirmada]`**: Bercholc & Bercholc (2012),
> *Los discursos presidenciales en la Argentina democrática*, que se cita en tres
> clases como inspiración de la serie de menciones y de la que no se pudo
> confirmar título, editorial ni año desde acá. **Ninguna afirmación del curso
> depende de ella; si quien tenga red no la encuentra, se saca.**

**14. `index.html`, actualizado.** Los 42 enlaces se comprobaron **uno por uno
contra el disco** y se abrió la página con Playwright: todos existen. Se agregó
una columna con **cuánto tarda el notebook de cada clase** (medido), la cantidad
de visualizaciones por clase, una caja hacia la guía del docente, y se sacó el
aviso de "los enlaces van a dar 404 hasta que esa clase esté construida", que ya
no corresponde.

**15. `README.md`, reescrito como puerta de entrada.** Qué es el curso y para
quién, la filosofía en un párrafo, el mapa de las diez clases con los tiempos
medidos, cómo se usa (docente: por dónde empezar; estudiante: por dónde empezar),
cómo se abren slides, viz y notebooks, la estructura del repo, de dónde salen los
datos y con qué licencia, y cómo reproducir la verificación entera.

**16. `recursos/GUIA-DEL-DOCENTE.md`, nuevo.** Qué leer y con cuánta
anticipación, el equipamiento mínimo con su plan B sin wifi, cómo manejar un aula
con tres niveles de programación, qué hacer la primera clase para que nadie se
asuste, cómo evaluar (los cuestionarios formativos **más una consigna de proyecto
final de seis puntos** con su rúbrica y su criterio de corrección), **los diez
momentos del curso donde el aula se pierde** con síntoma, causa y rescate, las
cinco siembras que no se pueden tocar, y las adaptaciones a **5 × 4 h** y a
**20 × 1 h** con lo que se gana y lo que se pierde en cada una.

---

## 4. Coherencia transversal: lo que se revisó y cerró bien

### Los nueve puentes

Se leyeron el cierre de cada clase y el arranque de la siguiente. **Los nueve
cierran textualmente**, y en varios casos la clase N+1 retoma la frase exacta:

| Puente | Cierre de N | Arranque de N+1 |
|---|---|---|
| 1 → 2 | *"la recta no alcanza; la salida no es una fórmula más complicada, es apilar"* | el fracaso de la recta contra la curva de inflación |
| 2 → 3 | *"pusimos los pesos a mano; con ocho ya es un suplicio"* | *"quedó una bronca: las perillas las pusimos a mano"* |
| 3 → 4 | *"entrenamos de verdad y descubrimos que un 99 % puede ser un desastre"* | modelo A 99 % / modelo B 84 % |
| 4 → 5 | *"el dato era un número; tus datos son fotos y discursos"* | la foto corrida 20 píxeles |
| 5 → 6 | *"la estructura espacial pide convoluciones; el texto tiene otra"* | *"barajamos los píxeles y la red ni se enteró. Hoy: ¿qué forma tiene el texto?"* |
| 6 → 7 | *"¿y si en vez de recordar, miramos directamente?"* | *"la clase 6 terminó con una bronca. Hoy la resolvemos."* |
| 7 → 8 | *"tenemos la máquina construida y apagada"* | *"lo apilamos cuatro veces, lo prendemos y lo miramos aprender"* |
| 8 → 9 | *"entrenar uno desde cero es carísimo"* | *"y ahí terminó lo que podemos entrenar nosotros"* |
| 9 → 10 | *"tenemos un número bueno. ¿Eso prueba algo?"* | *"ahí terminamos: con un F1 lindo y una sospecha. Hoy la sospecha se convierte en método."* |

### Las cinco siembras

Todas están puestas **y todas se cobran**:

| Se planta en | Se cobra en | Estado |
|---|---|---|
| clase 1, la rampa sin explicar en la viz del zoo | clase 2 | ✅ (y ahora la slide lo dice) |
| clase 2, botón "32 rampas" | clase 4, slide 21, *"prometido en la clase 2, cumplido"* | ✅ |
| clase 5, dos filas grises de `supuestos-de-arquitectura` | clase 7, slide 32, *"prometido en la clase 5, cumplido"* | ✅ |
| clase 6, panel "¿cuántas erres tiene?" | clase 8, la viz de contar letras | ✅ |
| clase 6, slide 36, el puente a attention | clase 7, slide 2 | ✅ |

### Vocabulario y notación

- **"desajuste" en la clase 1 → "loss" en la clase 3**: el hilo está y las dos
  clases usan las mismas palabras. La clase 3 lo nombra explícitamente como *"el
  medidor de desajuste de la clase 1, con nombre"*.
- **"ficha" para *token***: consistente en las cinco clases donde aparece (4, 6,
  7, 8, 10), 63 usos contra 4 de "token" (todos con su glosa).
- **`bias`**: se usa con los dos sentidos —el parámetro que suma (clase 2) y el
  sesgo social (clase 10)— y **las dos clases avisan explícitamente que no es lo
  mismo**. Está además en la tabla de falsos amigos del glosario.
- **Números que se repiten entre clases y coinciden**: 1.541.056 perillas del
  mini-GPT (≈1,5 M en las clases 1, 3, 8 y 9), 71 fichas de vocabulario,
  1.471 titulares (clases 9 y 10), 36 datos de la serie (clases 1 a 4), 0,0146 de
  piso de la recta (clases 1 y 3), 0,00150 vs 0,00152 de la serie suavizada
  (clases 1 y 2), 96 % de la fuente que predice la etiqueta (clases 9 y 10),
  1,1 MB de Aguasclaras y 2,2 MB del corpus real (clases 8 y 9).
- **Repetición**: los repasos de arranque ("dónde quedamos") están en las diez y
  ninguno reexplica desde cero: son cuatro o cinco viñetas de una línea. No se
  encontró ningún concepto explicado tres veces desde el principio, ni ninguno
  dado por sabido sin haberse explicado antes.

### Consistencia visual

Se sacó un screenshot de la portada de las diez clases a 1280×720 y se miraron
las diez juntas. **Ninguna desentona.** Misma tipografía, misma franja de cinco
colores, misma jerarquía (`CLASE N` / título / franja / bajada en itálica), mismo
papel. La única variación es deliberada: la clase 10 dice `CLASE 10 — LA ÚLTIMA`.
Las alturas de bloque varían con el largo del título, como corresponde.

---

## 5. Lo que se sabe y no se puede arreglar desde acá

Ninguna de estas cosas frena un dictado. Todas necesitan algo que este contenedor
no tiene.

1. **Las marcas `[VERIFICAR URL]`.** Quedan **77** en `recursos/bibliografia.md`
   y **97** repartidas en los diez `referencias.md` de clase. Las citas están
   completas y son correctas; **faltan sólo los enlaces**, y desde acá
   `arxiv.org`, `doi.org`, `huggingface.co`, YouTube, `distill.pub`,
   `deeplearningbook.org` y los sitios de las editoriales no responden. **Media
   hora de alguien con red cierra el archivo entero.** Ver la última sección de
   `recursos/bibliografia.md`, que tiene la tarea escrita en tres pasos.
2. **Hugging Face nunca se probó.** Las clases 9 y 10 tienen su camino "con red"
   escrito y sus tres identificadores de modelo confirmados contra la
   documentación oficial de cada repositorio, pero **bajar los pesos no se pudo
   probar**: `huggingface.co` da 403 acá. El camino sin red (PPMI+SVD y TF-IDF
   con regresión logística) sí corre, y es el que produjo los números que están
   en las slides. Quien dé la clase 9 en Colab tiene que anotar el hash de
   revisión de cada modelo y volver a correr `medir-clase09.py`.
3. **El tiempo en GPU T4 del notebook de la clase 8.** Sin medir, y pedido
   explícitamente en el notebook.
4. **La licencia de los dos corpus de discursos.** Ninguno de los dos declara
   licencia en su repositorio. Los textos son actos oficiales del Estado
   argentino y el uso educativo es defendible, pero **si el curso se publica hay
   que escribirles a los recopiladores**. Es la trampa 13 de
   `00-ESTADO-ESPINA.md`, sigue abierta, y ahora está dicha en `README.md`,
   `datos/README.md`, `recursos/bibliografia.md` y `GUIA-DEL-DOCENTE.md` §10.
5. **La URL del repositorio es un marcador de posición.**
   `https://github.com/johannperez/dlss` está en la celda de bootstrap de los
   diez notebooks, en `notebook-plantilla.ipynb` y en `recursos/setup.md`. **Los
   diez notebooks corren igual sin ella** (caen a `datos/muestras/`, probado),
   pero hay que reemplazarla por la real en los **12 lugares** antes de publicar,
   y ponerle a la slide 16 de la clase 1 el enlace corto de Colab. Anotado en
   `setup.md` y en `GUIA-DEL-DOCENTE.md` §10.
6. **Nadie dio este curso con estudiantes.** Los repartos de 120 minutos son
   estimaciones de diseño, no mediciones. Las adaptaciones a 5 × 4 h y 20 × 1 h
   son razonadas, no probadas. **La primera cohorte es también la prueba**: la
   guía del docente pide anotar los minutos reales y corregir las tablas.
7. **Viz que no entran enteras embebidas en la slide.** Se midieron las 39: **22
   son más altas que su iframe**, la peor es `checklist-revisor` de la clase 10
   con 2.596 px. **Es a propósito y no es un defecto**: la viz embebida muestra
   lo que el aula necesita ver desde el asiento, el iframe scrollea, y las notas
   del docente piden proyectarlas sueltas —que es donde tienen el título, el pie
   y los textos completos—. Está dicho en `GUIA-DEL-DOCENTE.md` §2 y §10.
8. **Detalles menores anotados por los verificadores de clase, que se dejan como
   están y con su justificación:** el modelo de las viz de la clase 7 tiene la
   atención muy afilada (entrenar más lo empeora pedagógicamente); en `qkv.html`
   dos barras empatan al redondeo (los números son los que son); el modo por
   defecto de `rampas.html` dibuja las sumas parciales (informativo con 2 y 4
   rampas; las notas piden cambiarlo para el silencio de los cinco segundos); el
   ítem 6 del cuestionario de la clase 8 tiene un mínimo que se mueve ±200 pasos
   por ruido (documentado en la solución); la slide 3 de la clase 5 usa un
   esquema sintético de multitud en vez de una foto real (**es lo primero que
   conviene reemplazar** si aparece una foto con licencia libre); y el juicio de
   la clase 10 nunca se corrió con un aula.
9. **Las slides cargan KaTeX y casi no lo usan.** Las clases 1 y 10 no tienen una
   sola fórmula con delimitadores. **Es la decisión correcta para esta
   audiencia** —la regla de la casa es que la fórmula se gana el lugar— y se
   anota sólo para que nadie busque un renderizado que no existe.

---

## 6. Estado de los seis ítems que dejó abiertos `00-ESTADO-ESPINA.md` §6

| # | Qué era | Hoy |
|---|---|---|
| 1 | Las marcas `[VERIFICAR]` de la bibliografía | **abierto**, y es lo único que le falta al archivo (§5.1) |
| 2 | Las clases 4, 8 y 10 sin slide "Glosario de hoy" | **cerrado**: las diez la tienen |
| 3 | Nadie probó el flujo real de Hugging Face | **abierto** (§5.2) |
| 4 | El entrenamiento del mini-GPT sin medir | **cerrado**: 4 a 7 minutos, medido ocho veces |
| 5 | La clase 6, la más apretada del curso | **cerrado**: entra en su presupuesto y el puente está marcado como lo único que nunca se recorta |
| 6 | La licencia de los corpus de discursos | **abierto** (§5.4) |

---

## 7. Cómo reproducir esta verificación

```bash
# Python: 119 tests + 28 doctests + el informe sobre los datos reales
python3 _shared/ssdl/test_ssdl.py
python3 datos/preparar_corpus.py
python3 datos/descargar.py --solo-muestras        # ni intenta la red

# los diez notebooks, cronometrados (unos 9 minutos en total)
for d in clases/*/; do
  s=$(date +%s)
  python3 -m nbconvert --to notebook --execute --output /tmp/out.ipynb "$d/notebook.ipynb"
  echo "$(basename $d) $(( $(date +%s) - s ))s"
done
```

Para el HTML, Chromium por Playwright:

```
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
NODE_PATH=/opt/node22/lib/node_modules
import pw from '/opt/node22/lib/node_modules/playwright/index.js';
chromium.launch({executablePath:'/opt/pw-browsers/chromium'})
```

Se abre cada uno de los 50 `.html` por `file://` con un
`context.route('**/*')` que **aborta cualquier URL `http(s)`** y cuenta los
errores de consola, los `pageerror` y las requests abortadas. Después, la misma
recorrida a 1280 y a 760 px comparando `document.documentElement.scrollWidth`
contra `clientWidth`. Los scripts quedaron fuera del repo a propósito (son de
verificación, no material de curso); están descritos con el detalle suficiente
para rehacerlos en veinte líneas.

Para las URLs:

```bash
while read u; do
  echo "$(curl -sS -o /dev/null -w '%{http_code}' -m 25 -L "$u")  $u"
done < urls.txt
```
