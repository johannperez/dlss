# Verificación — Clase 9

**Usar modelos que ya existen, sin creerles** · `clases/09-modelos-preentrenados/`

Este archivo tiene dos partes: **el estado actual** (revisión del 28/29-09-2026, que es la
que vale) y, más abajo, **el historial** de la verificación anterior (29-08-2026), con sus
afirmaciones corregidas donde la revisión encontró que decían de más.

---

## 1. Estado actual (29-09-2026)

**Se puede dar.** La revisión del 28-09 encontró errores conceptuales (el más serio:
presentar TF-IDF desde cero como si fuera el fine-tuning) y textos que sólo valían para el
camino sin red. Están corregidos; el detalle, en la sección 2.

Qué se comprobó en esta pasada, y cómo:

| Chequeo | Resultado |
|---|---|
| `nbformat` | válido · 58 celdas (25 de código, 33 de markdown) · guardado **sin salidas** |
| Celda de bootstrap | intacta: idéntica a la de los otros nueve notebooks (md5 del `source` `4c9c6d9d…`) |
| Notebook, **camino B** forzado (`FORZAR_CAMINO_B = True`), `nbconvert --execute` en una copia | **0 errores**, 3 corridas, 6-8 s de pared con la máquina libre |
| Notebook tal cual, **camino A** (con red, modelos ya en caché) | **0 errores**, 21 s de pared |
| Camino A con la celda opcional de fine-tuning prendida | **0 errores**, 30 s de pared (el fine-tuning con 200 etiquetas, 12 s) |
| Camino A sin caché | no se volvió a medir en esta pasada; la revisión del 28-09 lo corrió: 66 s y ~0,9 GB de descarga |
| Números de las slides (camino B) | se reproducen todos en la corrida de hoy: piso 0,72 · diccionario 0,75 / 0,40 · A 0,78 / 0,65 (P 0,59, R 0,72) · desde cero 0,83 / 0,67 · matriz 74/51/29/214 · trampa 0,73/0,68 contra 0,44/0,22 · pisos 0,53 y 0,60 · 332 de 346 medios · kappa 0,46, acuerdo 0,73, F1 humano 0,71 |
| `medir-clase09.py` | corrido dos veces en la misma máquina: salida **idéntica** entre las dos (md5). Contra la versión anterior del archivo, tres valores de la curva difieren en el 4.º decimal (0,5624 → 0,5628; 0,5864 → 0,5868; sd 0,0238 → 0,0237): otra versión de numpy/scikit-learn. Ningún número redondeado a 2 decimales cambió. Ahora el JSON guarda las versiones (`meta.versiones`) y el script chequea que aparezcan los momentos de las slides 16 y 32 (los cuatro dieron ok) |
| Figuras | `umbral.png` y `curva-de-etiquetas.png` regeneradas desde la corrida del camino B (la primera ahora es de validación; la segunda distingue las curvas por forma además de color). `matriz-de-confusion.png` no se tocó |
| Las 3 viz | abiertas con Chrome headless por `file://` y capturadas; se probaron a mano los estados nuevos (consultas revisadas, sin revisar, «futbol» sin tilde). No se registraron los errores de consola con una herramienta: se verificó que dibujan y responden |
| Slides | capturas de las slides que cambiaron de tamaño (4, 9, 11, 29, 32, 35) a 1280×760 |
| Verificación independiente (29-09, otra copia del repo) | camino B forzado y camino A con fine-tuning prendido: **0 errores**, mismos números (fine-tuning con 200: F1 0,64 en 10 s). `medir-clase09.py`: JSON y JS con el **mismo md5** que los del repo, los 4 chequeos ok. Slides y viz: HTML bien anidado, JS sin errores de sintaxis (`node --check`), y las 3 viz cargadas en Chrome headless sin errores de consola. Rankings de la viz de similitud simulados en node para las 6 consultas revisadas y «futbol»: las marcas coinciden con el texto |
| URL `[VERIFICADA]` | **no** se volvieron a probar en esta pasada |
| Colab real | **no** se probó |

### Reproducibilidad: qué se puede prometer

Los resultados son **deterministas en la misma máquina y con las mismas versiones de las
librerías**. Con otras versiones algún número cambia un poco (se vio en el 4.º decimal).
Las figuras **no** son reproducibles byte a byte entre máquinas: cambian los metadatos. Y
correr el notebook adentro del repo las pisa: por eso las instrucciones dicen de correrlo
sobre una copia.

---

## 2. Qué se arregló en la revisión del 28/29-09-2026

**Conceptuales**
1. **TF-IDF no es fine-tuning.** La viz de la curva, el notebook (sección 7 y tabla), las
   notas y las soluciones (1c, 6a) decían que TF-IDF "ocupa el lugar del fine-tuning" y
   sacaban de ahí conclusiones sobre el fine-tuning. Ahora se llama "aprender desde cero
   (nada prestado)", se dice que la curva no mide fine-tuning y que TF-IDF es barato en
   cómputo. Se agregó una **celda opcional y medida** de fine-tuning a mano (MiniLM
   multilingüe, las cinco estaciones de la clase 4). Con tres semillas por tamaño dio F1
   0,53 (25 etiquetas), 0,39 (50, de 0,22 a 0,57), 0,58 (100), 0,59 (200), 0,66 (400) y
   0,67 (800). Los números están en el notebook y en `notas-docente.md` §10.
2. **El "nunca" del umbral.** Al bajar el umbral el recall no baja nunca, pero la
   precisión no es monótona. Ahora lo dicen así el notebook (que cuenta los tramos donde
   suben las dos), la slide 25, las notas de la slide 24, la viz y la solución 5, donde
   "depende del modelo" pasa a ser parcialmente correcta.
3. **El "sube" de la accuracy.** En la viz la accuracy no se mueve (0,882 → 0,875). Se
   cambió en las notas de la slide 24, en `notas-docente.md` §4 y §5 y en el comentario
   de la viz.
4. **El kappa como techo.** Ahora se compara F1 con F1: el notebook calcula el F1 de un
   codificador contra el otro (0,71). Se cambió en la slide 29, las notas y el TODO 7, y
   se bajó el absoluto ("no hay modelo que pueda...").
5. **La época del corpus.** Son 971 notas de 2018 y 500 de 2020-21. Se corrigió en el
   notebook, `medir-clase09.py` (meta), la viz de similitud y referencias. Se agregó en la
   sección 11 la trampa tema/época: Covid-19 está 0 contra 192. Al armarla apareció otro
   detalle del CSV: el `id` se repite entre particiones, así que el notebook no lo usa
   como llave.
6. Escala de kappa según Landis y Koch (con cita), "rioplatense", "1471 titulares",
   "meses y millones", "nueve clases", el espectro de congelar (A y C en la slide 9),
   "Nada" del zero-shot (ahora "0 para entrenar, 200-300 para evaluar"), P11 (accuracy
   0,89), referencias cruzadas a secciones y comentarios de `medir-clase09.py` y de la
   viz de similitud.

**Ejecución y camino A**
7. Las celdas del camino A fijan la revisión exacta (`revision=`), atrapan fallas de
   descarga y caen al camino B. Además hay un interruptor `FORZAR_CAMINO_B`.
8. Los textos fijos que sólo valían para el camino B ahora van condicionados
   (`if not HAY_HF`): la búsqueda semántica, la pista del TODO 2 y el cierre de la sección 13.
9. La búsqueda semántica avisa cuando la consulta cae fuera del vocabulario, en vez de
   devolver un ranking arbitrario.
10. La sección 9 elige el umbral en **validación** (validación cruzada sobre train) y
    mira el test una sola vez.
11. La tabla de la sección 11 y la slide 32 muestran el piso de cada test (0,53 y 0,60).
12. "Mejores" pasa a "otros" para los números del camino A, con la tabla medida.

**Calendario y carga**
13. `[EL LUNES]` pasa a `[EN TU INVESTIGACIÓN]` en la slide 35, el notebook y las notas.
    La receta de siete pasos se presenta como proyecto de mediano plazo; antes de la
    clase 10, a lo sumo el paso 1.
14. Los botones de la viz de la curva decían "una semana (200)", que en realidad son
    1,7 h. Ahora dicen media hora (50), una tarde (200) y un día entero (800).

**Accesibilidad**
15. Los canvas de las viz de la curva y de la matriz tienen `role="img"` y un
    `aria-label` que se actualiza con el estado. En la matriz, acierto y error ya no
    dependen sólo del color: los aciertos son puntos llenos, los errores anillos huecos,
    y las celdas dicen "✓ acierto" y "✗ error". En la curva, las dos estrategias se
    distinguen además por la forma del punto y por un rótulo. En la búsqueda, "sin la
    palabra", "dudoso" y "sin revisar" van escritos. Los emojis de la slide 9 van con
    `aria-hidden`.
16. La viz de similitud ya no cuenta como "hallazgos genuinos" lo que nadie revisó. Hay
    tres casos: revisado a mano (sólo los 8 primeros de las 6 consultas sugeridas),
    dudoso (con el motivo) y **sin revisar**.

---

## 3. Lo que queda abierto

1. **Colab real no se probó.** El camino A se corrió en una máquina con red y el
   bootstrap está a cargo de otra revisión (`recursos/setup.md`).
2. **Quedan marcas `[VERIFICAR URL]`** en `referencias.md`. Se agregó una nueva, Landis y
   Koch 1977. No se les inventó URL.
3. **La casilla de transfer learning (10-25 min, 11 slides) sigue siendo la más
   apretada**, y la slide 9 ganó una línea (el espectro de congelar). Conviene
   cronometrarla el primer dictado.
4. **Embebida en la slide 25, la viz de la matriz mide más que su `<iframe>`.** Lo que
   queda abajo es la caja "momento aha", que la slide ya repite en su `viz-pie`, y se
   puede scrollear adentro.
5. **La celda de fine-tuning es opcional y sólo corre con red.** La medición es de tres
   semillas: alcanza para mostrar la inestabilidad, no para afirmar diferencias finas
   contra embeddings + logística.
6. **Los codificadores del archivo de kappa son simulados** y codifican "¿es falsa?". El
   techo de 0,71 vale para esa tarea, no para la de política.

---

## 4. Historial: la verificación del 29-08-2026 (resumen, con correcciones)

Aquella pasada se hizo en un contenedor **sin acceso a `huggingface.co`**, así que sólo
corrió el camino B. Encontró y arregló 11 problemas; los más serios fueron estos:

- la viz de la matriz decía "le gana por -8 puntos" en el momento aha;
- el plugin de resaltado de reveal tapaba el título de la slide 12 (el arreglo local
  sigue en `slides.html`; el CSS compartido sigue sin `position: relative` en
  `.reveal pre`);
- la slide 23 tenía los números de "política" con el sustantivo de "protesta";
- en la slide 17, un macro-F1 presentado como accuracy (los seis números de la tabla
  coinciden con `docs/TASKS.md` de pysentimiento).

También arregló la concordancia en las viz, el tamaño del código en las slides 12 y 14,
el rótulo del eje Y de `umbral.png` y los tiempos declarados del notebook.

**Correcciones a lo que afirmaba aquella pasada:**
- *"Figuras reproducibles byte a byte" y "`medir-clase09.py` reproducible byte a byte".*
  Valía sólo en aquel contenedor. En otra máquina, `datos-clase09.json` difiere en el
  4.º decimal y las figuras cambian de md5 (ver §1).
- *"No hay corte donde suban las dos".* Falso en general (ver §2, punto 2).
- *"Nadie corrió el camino A" y "con Hugging Face los números van a ser mejores".* El
  camino A se corrió el 28-09-2026. Sus números son otros: la misma F1 y otra accuracy.
- *"La curva... dicha como es".* La viz decía que TF-IDF ocupaba el lugar del
  fine-tuning (ver §2, punto 1).

Lo que se verificó entonces y se sigue sosteniendo:
- los cuatro titulares de la slide 5 están en el CSV con la etiqueta y el medio que dice
  la slide;
- AFPFactual aparece 32 veces, todas "falsas";
- las viz no hacen requests externas;
- el plan de tiempos suma 120 minutos;
- las cuentas del cuestionario (P3: 0,67 / 0,60 / 0,86 / F1 0,63 / piso 0,80; P4: bobo 96 %).

---

## 5. Cómo reproducir esta verificación

```bash
# sobre una COPIA del repo (el notebook guarda figuras en figuras/)
cp -R dlss /tmp/dlss-copia && cd /tmp/dlss-copia/clases/09-modelos-preentrenados
export PYTHONDONTWRITEBYTECODE=1

# camino A si hay red; para forzar el B, poné FORZAR_CAMINO_B = True en la sección 1
python3 -m nbconvert --to notebook --execute --output nb-09-ejecutado.ipynb notebook.ipynb

# los datos de las viz (determinista en la misma máquina y versiones)
cd /tmp/dlss-copia && PYTHONPATH=_shared python3 clases/09-modelos-preentrenados/medir-clase09.py
```
