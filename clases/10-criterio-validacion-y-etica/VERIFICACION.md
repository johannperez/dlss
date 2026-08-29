# Verificación adversarial — Clase 10

**Criterio: validez, sesgo, reproducibilidad y el revisor 2** · verificada el **2026-08-29**

> Segunda pasada, hecha con la consigna de **no creerle nada** a quien construyó la clase.
> Todo lo que dice acá se comprobó **corriendo el código y mirando las imágenes**, no leyendo:
> `nbconvert --execute` cronometrado cuatro veces, `nbformat.validate`, Chromium por Playwright
> con `context.route` **abortando toda URL http(s)**, 44 capturas de pantalla miradas una por
> una, `curl` contra cada URL, y los cinco PNG abiertos con los ojos.

---

## 1. Veredicto

**La clase es apta para dictarse.** Estaba bien construida y bien medida. Se encontraron y se
arreglaron **siete** problemas: **uno grave de rigor** (números inventados adentro de la propia
clase que enseña a no inventarlos), **uno de reproducibilidad**, **uno de semántica de color**,
**un plan de tiempos que no cerraba por 53 minutos**, **un entregable que no existía**, y dos
menores. Lo que queda abierto está en la sección 5 y **nada de eso frena una clase**.

| Chequeo | Resultado |
|---|---|
| Entregables (6 obligatorios + extras) | **todos presentes**, ninguno vacío ni a medias · +1 escrito acá |
| `nbformat.validate(notebook.ipynb)` | **válido**, 57 celdas |
| `nbconvert --execute`, sin red | **0 errores, 0 stderr, 5 figuras** |
| Tiempo del notebook (4 corridas) | **14,4 · 18,2 · 18,3 · 18,8 s** de punta a punta |
| Consola del navegador (slides + 3 viz, en su ubicación real) | **0 errores, 0 `pageerror`, 0 requests fallidos** |
| Requests externos con `route` abortando `http(s)` | **0**, en las cuatro páginas |
| Desborde vertical de las 40 slides (medido con rectángulos reales) | **0 slides desbordadas** |
| Reproducibilidad de `medir-clase10.py` | `datos-clase10.json`, `.js` y `pesos-clase10.js` **bit a bit idénticos** |
| Reproducibilidad de `exportar-figuras.py` | los 5 PNG **bit a bit idénticos** en corridas sucesivas |
| Números de las slides contra la corrida real | **todos verificados** (ver §3) |
| Código de las slides contra el notebook | **idéntico**, las dos veces que aparece |
| URLs de `referencias.md` | 4 marcadas VERIFICADA dan **200**; la única que no responde está marcada `[VERIFICAR URL]` |
| Plan de tiempos | **120,0 min exactos**, slide por slide y en `notas-docente.md` |

---

## 2. Lo que estaba mal y se arregló

### Grave

**1. Números inventados adentro de la clase que enseña a no inventar números.**
`viz/checklist-revisor.html` decía, al pie: *«el ejemplo precargado es la auditoría real de
esta clase, con los números que salen de `medir-clase10.py`»*. **Cuatro de sus respuestas no
salían de ningún lado:**

| campo | lo que decía | lo que pasa de verdad |
|---|---|---|
| exclusiones | «se excluyeron 72 notas sin titular» | **no se excluyó ninguna**: entran las 1471 |
| validación manual | «150 casos leídos a ciegas, estratificados» | **cero**: la codificación es heredada del corpus fuente |
| acuerdo entre codificadores | «kappa de Cohen = 0,46 sobre 100 casos» | **no hubo doble codificación** |
| falsos positivos | «leímos 30 … la mayoría son notas de Covid» | hay **25** en el test, el notebook imprime **20**, y de esos 20 **uno solo** es de Covid |

Es exactamente el pecado del que habla la clase, cometido por su entregable estrella.
*Arreglado:* los cuatro campos dicen ahora lo que efectivamente pasó —incluido **«0 en este
ejercicio»** para la validación manual, declarado como la limitación principal— y el pie
explica que el ejemplo es la auditoría real **agujeros incluidos**, y que declararlos es la
jugada correcta. El párrafo de métodos que genera la viz sigue siendo completo; ahora además
es cierto.

### Importante

**2. Dos definiciones del mismo experimento, con dos resultados distintos.**
`medir-clase10.py` ablacionaba **14** nombres propios y el notebook **18**. Consecuencia
visible en el aula: la VIZ 1 decía *«sin los 14 nombres propios · 0,677»* y el notebook, en la
pantalla de al lado, imprimía *«los nombres propios · 18 · 0,670»* para el mismo test. Lo mismo
con la auditoría de sesgo: `medir` tenía **18** filas (con «los empresarios» repetido en dos
dimensiones) y el notebook **17**, y la VIZ 3 reportaba «18 sujetos».
*Arreglado:* las dos listas de `medir-clase10.py` son ahora **idénticas a las del notebook**
(18 nombres propios, 17 sujetos sin repetir), con un comentario en cada una diciendo por qué
tienen que quedar iguales. Los literales `14` y `18` de las dos viz se reemplazaron por
`D.ablacion[4].n_quitados` y `D.sesgo.filas.length`, para que **no puedan volver a divergir**.
Se regeneraron `datos-clase10.json` y `.js`; `pesos-clase10.js` y las cinco figuras no cambian.

**3. El plan de tiempos sumaba 173 minutos para una clase de 120.**
La nota del docente lo admitía como «suma más de 120», sin decir cuánto: eran **53 minutos de
más**, un 44 %. Un docente que leyera «más de 120» iba a preparar 130 y llegar a la mitad de la
segunda parte con la campana sonando. Y el bloque práctico 1 decía **30 minutos** en la slide
contra los **20** del presupuesto de `PROGRAMA.md`.
*Arreglado:* la sección 2 de `notas-docente.md` es ahora **un plan que suma 120 exactos**, con
los recortes ya aplicados y explicados (VIZ 1 de 8 a 5, los procedimientos 13-17 a un minuto,
el práctico 1 a 20, el juicio a 20, la ética a 7). Los rótulos de minutos de las 40
`<aside class="notes">` se reescribieron uno por uno para que coincidan con esa tabla —suman
**119,7**, con dos transiciones de 20 segundos—, y la sección 5 («si vas atrasado») recosteó
cada recorte, que ahora dan **12 minutos** de colchón real.

**4. Faltaba el material del bloque práctico 2.** El juicio son 20-25 minutos de clase y **no
había paper para repartir**: estaban las consignas, los roles y la rúbrica, pero el objeto
físico no existía. La spec autoriza explícitamente construirlo *ad hoc* y rotularlo como
material didáctico (§8).
*Arreglado:* escrito **`material-el-juicio.md`**, con los dos papers que pide la spec —el A
defendible con reparos menores, el B con un problema fatal de validez escondido en una nota al
pie— más la clave de corrección para el docente, objeción por objeción y con su gravedad. Los
dos son **ficticios, sin autores y sin revista**, y así lo dicen en su primera línea y en
`referencias.md`: no citan datos reales y no se pueden citar. Los números de adentro son
internamente coherentes, para que un grupo que los revise en serio encuentre lo que tiene que
encontrar y no un descuido.

### Menores

**5. Semántica de color al revés en la slide 16.** La fila de la negación tenía su Δ en
**verde** (`c-ok` = «correcto, aceptado») mientras el cartel de abajo explica que *la negación
no mueva nada es el problema*. Un estudiante que mirara la tabla y no el cartel leía la
conclusión contraria. *Arreglado:* va en `c-error`, como las otras tres; las cuatro filas son
señales del mismo problema y el cartel ya lo dice («las dos cosas dicen lo mismo»).

**6. Una figura del repo no era la que produce el notebook.** `figuras/02-terminos-influyentes.png`
en el árbol de trabajo no coincidía con la salida de `exportar-figuras.py` (sí coincidía la
versión de HEAD: había quedado una copia vieja encima). *Arreglado:* regenerada. Ahora las
cinco salen bit a bit iguales en corridas sucesivas.

**7. La slide 23 no entraba en la pantalla** después de agregarle la línea de prioridades
(768 px sobre 760). *Arreglado:* la pista se plegó adentro del recuadro `.manos compacta` y se
sacó la coletilla redundante del `TODO 6`. Verificado midiendo los rectángulos reales: **0
slides desbordadas de 40**.

---

## 3. Lo que se verificó y **no** se tocó

**Los números.** Cada cifra concreta de las slides se comparó contra la salida real:

- Panel del gancho: `0,83 / 0,73 / 0,64 / 0,68`, piso `0,72`, ganancia `+0,11`, `1471` notas,
  `368` de test, `1103` de train, vocabulario `6.534`. ✔ todos.
- Slide 4: los **16** pesos de la tabla son el top-16 exacto (`presidencial +1,10` …
  `gobernador +0,62`), y el conteo de nombres propios —**5 de 16** en la tabla, **6 de 20** en
  el top completo, «uno de cada tres»— se contó sobre la salida. ✔
- Control positivo: `600` fragmentos, `64` contra `21` de cada 100 (recall 0,641 y 0,208). ✔
- Banda de ruido: `0,68` medio, desvío `0,026`, `0,626–0,733`, rango `0,107`, ablación
  «como mucho 0,033». ✔
- Falsos positivos de la slide 14: los cinco titulares y sus scores están en la salida. ✔
- Pares mínimos de la slide 16: `0,800/0,759`, `0,773/0,516`, `0,546/0,392`, `0,713/0,317`. ✔
- Slide 22: los cuatro `0,265`, y los pesos `−0,339` («los») y `−0,1355` («las»). ✔
- Nota del docente de la slide 21: `0,346` vs `0,257` en género y `0,344` vs `0,183` en origen
  — comprobado **en la pantalla**, moviendo el selector. ✔

**El código de las slides es el del notebook.** Los dos bloques `<pre><code>` (el control
positivo de la slide 15 y el `bloque_de_reproducibilidad` de la slide 27) son literalmente las
líneas de las celdas 30 y 49. ✔

**El motor JS de la VIZ 2 coincide con el modelo de Python.** La viz reconstruye la regresión
logística sumando pesos en el navegador; da `0,346` para «las médicas», el mismo número que
`predict_proba` en el notebook. ✔

**Las tres viz cumplen su momento aha, comprobado moviendo los controles:**

| viz | qué se hizo | qué pasó |
|---|---|---|
| `validez-de-constructo` | los 3 casos × 2 vistas | Caso 1: 64 de cada 100 → **21** de cada 100, y las tres ablaciones caen adentro de la banda gris. Caso 2: **0 casos** en años compartidos, el arreglo no existe. Caso 3: dos foros con tono idéntico y estructuras opuestas. |
| `sesgo-en-el-espejo` | las 4 dimensiones, el checkbox, y una plantilla escrita a mano | Con «marcar los que no conoce», 4 de 8 sujetos se pintan gris y varios comparten el número **hasta el último decimal**. La plantilla propia («marcharon contra el aumento de tarifas») recalcula todo en vivo. «los adultos mayores» ya no se corta. |
| `checklist-revisor` | modo revisor vacío → completar → párrafo → vaciar | Vacío: **22 objeciones, 13 fatales** en rojo. Completo: `22 de 22` y el párrafo de métodos armado. El `localStorage` está envuelto en `try/catch` y hay botón *Vaciar*. |

**Las cinco figuras, miradas.** Ejes rotulados, leyendas, y se entienden sin el texto de al
lado. La 03 (ablación contra ruido) es la mejor de la clase: se ve de un vistazo que las tres
intervenciones caen adentro de la banda.

**Las URLs.** `curl` a las cinco de `referencias.md` que tienen enlace: las cuatro marcadas
`[VERIFICADA 2026-08-29]` responden **200**; `scikit-learn.org` no responde desde este
contenedor y está correctamente marcada `[VERIFICAR URL]`. **No hay ninguna URL inventada** y
ninguna cita sospechosa: las diez obras existen, con autor, año, publicación y páginas.

**El cuestionario.** Las 12 preguntas se contestan con lo que se dio en clase, y las soluciones
son correctas (se rehizo la cuenta del ítem 5: `0,412 − 0,357 = 0,055` ✔). Los distractores de
los dos *multiple choice* son **tentadores, no absurdos**: el A del ítem 1 («detecta con 91 % de
eficacia») es la traducción que hace la literatura publicada, y el B del ítem 2 («generaliza
bien») es *otra* validez de verdad. Cada distractor viene con la confusión que revela elegirlo,
que es lo que sirve en el aula.

**Cero red, cero CDN, todo relativo.** Ni un `https://` en un `src` o un `href`, ni un color
hexadecimal escrito a mano, ni una ruta absoluta, en las cuatro páginas.

**Los puentes.** Hacia atrás: la slide 2 retoma textualmente el cierre de la clase 9 («la
fuente predecía la etiqueta al 96 %»). Hacia adelante —es la última clase— la 39 lo cruza al
proyecto propio del estudiante. El `[CALLBACK DIBUJO]` está en la 36, con el mapa de las diez
clases al lado.

**El tono.** Rioplatense, con voseo, sin solemnidad. No quedaron imperativos peninsulares ni
párrafos-muro: todas las slides largas tienen tabla, tarjetas o recuadro. Los términos en
inglés se explican la primera vez y los siete de hoy están en `recursos/glosario.md`,
coherentes con la slide 37.

---

## 4. Cómo reproducir esta verificación

```bash
cd clases/10-criterio-validacion-y-etica
python3 -c "import nbformat; nbformat.validate(nbformat.read('notebook.ipynb', as_version=4))"
time PYTHONPATH=../../_shared python3 -m nbconvert --to notebook --execute \
     --output /tmp/out.ipynb notebook.ipynb          # ~14-19 s, 0 errores, 0 stderr
md5sum datos-clase10.json datos-clase10.js pesos-clase10.js figuras/*.png > /tmp/a.md5
python3 medir-clase10.py && python3 exportar-figuras.py && md5sum -c /tmp/a.md5   # todo OK
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`), abriendo
por `file://` **desde la ubicación real de los archivos**, con
`context.route('**/*', r => /^https?:/.test(r.request().url()) ? r.abort() : r.continue())`
y escuchando `console`, `pageerror` y `requestfailed`. Para el desborde: recorrer las 40
`section`, forzarles `display:block` y comparar el `bottom` real de cada hijo contra los 760 px
de alto de la slide.

---

## 5. Lo que queda abierto

| # | Qué | Para quién | Frena la clase? |
|---|---|---|---|
| 1 | **El juicio dura 20 minutos, no los 25 de `PROGRAMA.md`.** Es la única desviación del presupuesto oficial, y es deliberada: el mazo entero son ~150 min y había que sacar 30 de algún lado. `notas-docente.md` §5 dice cómo devolverle los 5 minutos si el aula va holgada. | quien dé la clase | no |
| 2 | **Nadie lo probó con estudiantes.** El reparto de 120 minutos es una estimación de diseño, no una medición. Conviene anotar los minutos reales la primera vez y ajustar la tabla. | quien dé la clase | no |
| 3 | Las **66 marcas `[VERIFICAR URL]`** (56 de `recursos/bibliografia.md` + 10 de este `referencias.md`). `doi.org`, `arxiv.org` y los sitios de las editoriales están bloqueados acá. Las citas están completas y correctas; faltan los enlaces. **Si una obra no aparece, se saca la cita: no se le inventa un enlace.** | quien tenga red | no |
| 4 | La **licencia de los dos corpus de discursos** sigue sin declarar (trampa 13 de la espina). Está dicho en `referencias.md` y en las notas. Si el curso se publica, hay que escribirle a los recopiladores. | el docente | no |
| 5 | El cuestionario declara **50 minutos**; `PROGRAMA.md` §3.4 dice que los cuestionarios se resuelven en 15. La contradicción viene de la propia spec, que en su §7 pide para esta clase tres ítems de diseño y uno «de una página». Se dejó en 50 y con la lista de las cinco preguntas mínimas para media hora. **Alguien tiene que decidir cuál de los dos documentos manda.** | el equipo del curso | no |
| 6 | Las slides cargan **KaTeX y no lo usan**: esta clase no tiene una sola fórmula. Es coherente con la regla de la casa («y a veces la fórmula no va») y con la plantilla, pero son dos `<script>` de más. | opcional | no |
| 7 | `material-el-juicio.md` **nunca se usó en un aula**. Los dos papers son nuevos: la primera cohorte es también su prueba. Si el B resulta demasiado obvio, la clave de corrección dice qué objeción esconder. | quien dé la clase | no |

---

## 6. Los archivos de la clase

```
clases/10-criterio-validacion-y-etica/
  slides.html                 40 slides · 0 errores de consola · 0 desbordes
  notebook.ipynb              57 celdas · 0 errores · 5 figuras · 14-19 s
  viz/validez-de-constructo.html   3 casos × 2 vistas
  viz/sesgo-en-el-espejo.html      4 dimensiones + plantilla editable + tabla markdown
  viz/checklist-revisor.html       22 preguntas · 13 fatales · párrafo de métodos
  notas-docente.md            plan de 120 min exactos + qué recortar
  cuestionario.md · cuestionario-soluciones.md      12 ítems
  referencias.md              10 lecturas · 4 URLs verificadas
  material-el-juicio.md       NUEVO — los dos papers del práctico 2 (ficticios, rotulados)
  medir-clase10.py            de acá sale cada número de las slides y las viz
  exportar-figuras.py         corre el notebook y guarda sus 5 figuras
  datos-clase10.json · datos-clase10.js · pesos-clase10.js
  figuras/                    5 PNG + README
  VERIFICACION.md             este archivo
```
