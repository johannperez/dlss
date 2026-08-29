# Verificación adversarial — Clase 3

**«Estar equivocado es un número, y ese número tiene pendiente»** ·
`clases/03-loss-y-gradiente/`

Todo lo que dice acá se comprobó **corriendo el código y mirando las imágenes**, no
leyendo los archivos: `nbconvert --execute` cronometrado, `nbformat.validate`,
Chromium por Playwright con `context.route` abortando **cualquier** URL `http(s)`,
`curl` contra cada enlace, y las cuentas rehechas en numpy/scipy aparte para
contrastar con lo que dicen las slides.

**Veredicto: apta para dictarse.** Se encontraron **17 problemas** y se
**arreglaron los 17**. Tres eran de los que arruinan una clase en vivo (una tabla
que mentía en pantalla y dos botones que no hacían nada la segunda vez que se
apretaban). Lo que queda abierto está en la sección 5 y **nada de eso frena la
clase**.

---

## 1. Chequeo mecánico

| Chequeo | Resultado |
|---|---|
| Los 6 entregables existen y están completos | sí (slides, notebook, 4 viz, notas, cuestionario + soluciones, referencias) |
| `nbformat.validate` | **válido**, 40 celdas |
| `nbconvert --to notebook --execute` | **0 errores**, 8 figuras · 3 corridas: **8,97 s / 9,47 s / 9,04 s** |
| El notebook **sin red** (`HTTPS_PROXY` a un puerto muerto) | **0 errores**, mismos 36 años y mismos números |
| Consola del navegador · slides + las 4 viz **en su ubicación real** | **0 errores** (las 36 slides recorridas una por una) |
| Requests externas (`context.route` abortando `http(s)`) | **0** en los 5 archivos |
| KaTeX | renderiza desde `_shared/vendor` — verificado **por screenshot** (slide 6, MSE y MAE) |
| Los 5 `<iframe>` de viz cargan adentro de las slides | sí, verificado por screenshot de cada una |
| Tema oscuro (`prefers-color-scheme: dark`) | slides y las 4 viz, sin errores y legibles |
| Ventana angosta (900×640) | la slide 14 sigue entera |
| Ninguna slide se pasa del alto del canvas de reveal (760 px) | **0 de 36** (antes de esta revisión se pasaba una) |

---

## 2. Chequeo de rigor: cada número, rehecho aparte

Todos estos se recalcularon con numpy/scipy sobre `ssdl.datos.serie_menciones("seguridad", 1984, 2019)`,
sin usar el código de la clase.

| Número que aparece | Dónde | Comprobado |
|---|---|---|
| la serie (36 años, 1984-2019) | slides, notebook y las 4 viz | los arrays hardcodeados de `slides.html`, `valle-de-loss.html` y `comparador-de-losses.html` coinciden con `serie_menciones` **con diferencia máxima 0,0** |
| 0,0146 / 0,0152 / 0,0880 / 0,0921 | slide 4 | recta MSE-óptima (0,042427; 0,154908) → MSE 0,014547 · MAE 0,092050. Recta MAE-óptima (0,061261; 0,138093) → MAE 0,087966 · MSE 0,015213. **Los cuatro, exactos** |
| 0,033 vs 0,092 puntos por década | `comparador-de-losses` | subconjunto de 15 años: 0,0328 y 0,0925. **Exacto** |
| 20 % / 17 % (peso del año 1998) | `comparador-de-losses` | 20 % y 17 %. **Exacto** |
| 47 % del MSE, tras plantar el caso extremo | viz + slide 7 | 47 %. **Exacto** |
| «la azul se mueve N veces más» | `comparador-de-losses` | medido: 0,092 contra 0,011 → **8,4×**. La viz decía «cinco veces»: corregido |
| 4,0× (MSE) contra 1,4× (MAE), y 75 % del MSE | notebook + soluciones 3 | salida real del notebook |
| 0,014547 (el fondo del valle) | notebook, slides, viz | `lstsq` da 0,0145471504. **Exacto** |
| 115 días para 10¹⁶ pruebas | slide 17 + notebook | 10¹⁶/10⁹ = 10⁷ s = 115,7 días. **Correcto**, con el supuesto (10⁹ pruebas/s) escrito en el código |
| 10¹⁷³ edades del universo, 10⁸⁰ átomos | slide 17 | consistentes con los mismos supuestos |
| 0,93 = el paso más grande que todavía converge | pie de `tasa-de-aprendizaje` | Hessiano = 2·diag(⟨x²⟩, 1) con ⟨x²⟩ = 1,07917 → 2/λmax = **0,9267**. **Correcto**, y explica por qué 0,3 converge y 1,3 explota |
| loss = 2,67e+25 y «después se congela» | notebook, notas §4.10, slide 25 | corrido a 300 pasos: se estaciona en 2,67e+25 desde el paso ~40. **Correcto** |
| 0,106 y 0,065 (los dos pozos) | notas §4.3 | mínimos locales del paisaje inventado: **0,10581** y **0,06503**, y el descenso llega a los dos según de dónde arranque (verificado en el navegador, 6 arranques) |
| −0,6905 (resta) vs −0,6959 (exacta) con h = 0,005 | `loss-1d`, slide 19 | leído del panel en vivo. **Correcto** |
| pendiente +0,0042 puntos **por año** | `datos/README.md` | 0,042427 por década = 0,00424 por año. **Coherente** |

**No se encontró ningún número inventado.** Tampoco ninguna analogía que enseñe algo
que después haya que desaprender: las tres más riesgosas (el gradiente «apunta al
mínimo», la fuerza bruta «da un mínimo local», backprop «reemplaza al descenso») están
explícitamente desarmadas en las slides 21 y 29, en `notas-docente.md` §4.2, §4.9 y en
las soluciones 6c, 7d y 10.

---

## 3. Los 17 problemas que se encontraron y se arreglaron

### Graves (se ven en el aula)

**1. La tabla de la fuerza bruta mentía en pantalla.**
`reset.css` de reveal aplana `sup` y `sub` (les pone `font-size:100%; vertical-align:baseline`),
así que `10<sup>16</sup>` se **leía «1016»** en el proyector. Los siete números de la
slide 17 estaban mal: «10200» en vez de 10²⁰⁰, «1080 átomos» en vez de 10⁸⁰. Era la
slide que mata la fuerza bruta y decía cualquier cosa.
*Arreglado:* regla `.reveal sup/sub` en el `<style>` de `slides.html`. Verificado por
screenshot en tema claro y oscuro.
**Para la base:** es un bug de `reset.css` que va a golpear a cualquier clase que use
`<sup>`. Hoy la 3 es la única que lo usa; convendría subir la regla a `curso.css`.

**2. «Soltar la pelota» no hacía nada la segunda vez.**
`Viz.animacion` no reinicia su contador interno `i`, y `valle-de-loss.html` frenaba con
`return i < 45`. Consecuencia real: el docente suelta la pelota (anda), aprieta
**«uno con dos pozos»** o **«Soltarla desde otro lugar»**, vuelve a apretar soltar…
**y la pelota da un paso y se queda quieta.** Justo el momento de la slide 29.
*Arreglado:* contador propio (`pasosDados`) que se pone en cero en cada `play` vía
`anim.on(...)`. Verificado: seis corridas seguidas, y el modo «dos pozos» llegando
alternadamente a 0,1058 y 0,0650.

**3. «Soltar las tres» tampoco animaba la segunda vez.**
Mismo bug en `tasa-de-aprendizaje.html` (`estado.hasta = i + 1`): la segunda corrida
mostraba el resultado final de un cuadro, sin animación. Y la animación *es* el
contenido de esa viz.
*Arreglado:* `estado.hasta += 1`. Medido: 1ª corrida a 1,2 s → paso 20; 2ª corrida a
1,2 s → paso 18. Las dos animan.

**4. Los botones de la animación quedaban fuera de pantalla en las slides 14 y 22.**
En el marco embebido el panel de `valle-de-loss` medía 799 px contra 589 disponibles, y
los botones estaban **al final**: «Soltar la pelota», «Un paso», «Volver arriba» y
«Soltarla desde otro lugar» **no se veían**. La slide 22 se llama «Soltá la pelota».
*Arreglado:* se reordenó el panel (los botones arriba, los textos largos al final), se
compactó y se ensanchó a 330 px en modo embebido, y el marco pasó de 610 a 614 px con el
título y el pie apretados. Medido: comparador **601 → entra entero**, loss-1d
**616 → entra entero**, valle 689 (se corta sólo el cartel de lectura del final),
tasa 950 (se corta el quiz, que ya estaba pensado como opcional y ahora el pie lo dice).

### Rigor y coherencia

**5.** Slide 25 citaba a un estudiante: *«puse 1.5 y en el paso cuatro ya tenía un número
con nueve dígitos»*. Medido: en el paso 4 la loss vale 94,89 (dos dígitos); nueve dígitos
llegan en el **paso 13**. Corregido a «paso trece».

**6.** «Una recta con 2 variables → 4 perillas» (slide 17 y notebook): con dos predictoras
son **tres** parámetros, no cuatro. Para una audiencia que sabe regresión, es un error
visible. Cambiado a «una regresión con 3 variables», que sí tiene 4 perillas.

**7.** `notas-docente.md` §5 mandaba recortar «la slide 29 (optimizadores)» y tres párrafos
más abajo decía que la slide 29 (la honestidad) **nunca** se recorta. Optimizadores es la
**30**. Un docente atrasado se comía justo la slide que la spec marca como irrecortable.

**8.** El plan de tiempos de `notas-docente.md` tenía dos filas en «0:60»: la viz `loss-1d`
quedaba con **cero minutos** y el texto de abajo decía que había que darle aire.
Corregido a 0:57 → 1:00.

**9.** `loss-1d.html`: al llegar al fondo del valle el panel seguía diciendo «para bajar
tenés que ir **a la derecha**» con una pendiente de ~0 (el signo salía de un redondeo).
Ahora, cuando los dos pasitos suben, dice **«llegaste al fondo»**.

**10.** El «momento aha» de `comparador-de-losses` decía «la azul se mueve unas cinco veces
más que la naranja»; medido son 8,4×. Reemplazado por los dos números reales
(0,092 y 0,011).

**11.** «La **flecha negra**» (panel de `valle-de-loss` y notebook): en tema oscuro esa
flecha es blanca. Cambiado a «la flecha gruesa» en los dos lados.

**12.** El notebook decía «estas diez líneas se van a convertir en **tres** palabras de
PyTorch» y, seis celdas más abajo, «son **dos** palabras: `loss.backward()`». Unificado
en dos.

**13.** El título del gráfico de la slide 16 decía «diez mil rectas, probadas una por una»
sobre una grilla dibujada de 40×26. Ahora el título dice que el dibujo es más ralo y el
pie da los dos números.

### Legibilidad

**14.** La flecha roja del gradiente (slide 21) era corta y roja **sobre fondo naranja**:
no se leía de lejos. Se alargó y el rótulo se movió a la punta.

**15.** «Volver arriba» en `valle-de-loss` devolvía siempre al arranque del paisaje de los
datos, incluso estando en el paisaje de dos pozos. Ahora respeta el paisaje activo.

**16.** El quiz de firmas de la slide 23 quedaba abajo del pliegue del panel sin que nada
lo dijera. El pie de la slide ahora lo aclara.

**17.** Después de agrandar los marcos, seis slides se pasaban del alto del canvas de
reveal. Se ajustó el alto a 614 px y se comprobó **slide por slide** que las 36 entran.
De paso se arregló la **slide 21**, que ya se pasaba por 5 px **antes** de esta revisión.

---

## 4. Lo que se revisó y estaba bien

- **Coherencia con la spec.** Están los 34 bloques del guion, más la slide de pausa y la
  de «qué te llevás» que pedía el encargo: **36 secciones**. No falta ningún bloque y no
  sobra nada que no estuviera pedido.
- **Presupuesto de tiempo.** El plan de `notas-docente.md` §2 suma 120 minutos exactos, es
  continuo, y sus rangos de slides coinciden **uno por uno** con la numeración que muestra
  reveal (verificado contra los screenshots, no contra los comentarios del HTML).
- **Las cuatro decisiones de diseño que declaró quien la construyó** (azul/naranja en vez
  de rojo, la paleta `loss` con claro = hondo, los mapas angostos, lr 0,15 por defecto)
  **están bien tomadas** y son coherentes con `GUIA-CONSTRUCCION.md` §2 y con las clases 4
  y 8.
- **Puentes.** Hacia atrás: slide 2 (`[CALLBACK DIBUJO]`, las 8 perillas a mano) y slide 17
  («la red de 8 rampas de la clase 2»). Hacia adelante: slide 24 (los dos síntomas → clase 4),
  slide 28 (`loss.backward()`), slide 36, y el cierre del notebook. Todos explícitos.
- **Tono.** Voseo, humor, cero solemnidad, sin «no se asusten» y sin «esto es fácil».
  No se encontró ningún tramo académico ni condescendiente. Cada slide tiene imagen,
  ejemplo o pregunta.
- **Cuestionario.** Las 12 preguntas se contestan con lo que se da en clase. Los
  distractores son tentadores, no absurdos (2a/2b son *la* confusión de la clase; 7d
  invierte fuerza bruta y descenso; 8c confunde learning rate con batch size). Las
  soluciones son correctas, incluidos los números que citan (4,0× / 1,4× / 75 % / 115 días)
  y las referencias a slides.
- **Las 4 viz, control por control.** Arrastre en vivo (comparador y valle), plantar y
  volver, los tres learning rates, el quiz de firmas (probado respondiendo bien: «3 de 3»;
  y mal: corrige con la pista de la firma), el pasito de prueba de 0,25 a 0,005, el paso
  cuesta abajo, los dos paisajes, y el cartel «se fue del mapa» con lr = 1,5
  (loss 1,91e+31). Todo responde.
- **Figuras del notebook.** Las 8 se guardaron y se miraron: ejes rotulados, leyendas,
  barra de color, y las tres firmas con el aviso «ojo: otra escala» en el panel que la
  cambia. Se entienden sin el texto.
- **URLs.** `curl` sobre las 5 de `referencias.md`:
  `raw.githubusercontent.com/3b1b/manim` → **200**,
  `raw.githubusercontent.com/lucariel/discursos_presidenciales` → **200** (las dos marcadas
  `[VERIFICADA]`, correcto);
  `deeplearningbook.org`, `arxiv.org` y `distill.pub` → bloqueadas por el proxy, y están
  marcadas `[VERIFICAR URL]`, correcto. **Ninguna URL inventada.**
  Las citas (Goodfellow/Bengio/Courville 2016; Ruder 2016; Goh 2017 en Distill;
  Stigler 1986; Simon 1955 *QJE* 69(1) 99-118; Ragin & Becker 1992) son todas obras reales
  con autor, año y editorial correctos. **No se sacó ninguna.**
- **Glosario y bibliografía.** Los 12 términos de la clase están en `recursos/glosario.md`;
  las 4 entradas nuevas de `recursos/bibliografia.md` están bien formadas y marcadas.

---

## 5. Lo que queda abierto

| # | Qué | Gravedad | Para quién |
|---|---|---|---|
| 1 | En la slide 23, el panel de `tasa-de-aprendizaje` mide 950 px contra 593 disponibles: el **quiz de firmas** queda abajo del pliegue (se scrollea, y el pie lo avisa). Suelto se ve entero. | cosmética | quien la dé: si quiere hacer el quiz en vivo, conviene abrir la viz suelta |
| 2 | En las slides 14 y 22, el último cartel del panel de `valle-de-loss` (el texto que cambia en vivo, incluido «Se fue del mapa») queda cortado por ~96 px. Los controles, las perillas y el desajuste **sí** se ven. | cosmética | idem |
| 3 | Las 4 viz dejan espacio vacío abajo a la izquierda del marco embebido. Se achicó bastante subiendo los dibujos de 300 a 390 px en `valle-de-loss`; se podría hacer lo mismo en las otras tres. | cosmética | quien retoque |
| 4 | 5 marcas `[VERIFICAR URL]` / `[VERIFICAR]` en `referencias.md` (3Blue1Brown en YouTube, Distill, arXiv, deeplearningbook, y las fechas 1805/1809 de Legendre-Gauss). Desde este contenedor **no se pueden** abrir: el proxy las rechaza. Las citas están completas; faltan los enlaces. | abierta a propósito | quien tenga red |
| 5 | En el panel del medio de la figura del descenso (celda 25 del notebook) falta `set_aspect("equal")`, así que ahí el valle se ve elíptico mientras que en la celda 15 se ve redondo. Un ojo atento lo puede notar. | menor | quien retoque el notebook |
| 6 | El quiz de firmas **nunca se probó con un aula real**. Las tres formas son muy distintas; si resulta trivial, agregar un cuarto caso ambiguo. | menor | quien la dé primero |
| 7 | El cierre (110-120 min, 11 slides) sigue siendo el tramo más apretado. `notas-docente.md` §5 tiene el orden de recorte y ahora es coherente. **Hay que medirlo en un aula.** | menor | quien la dé primero |
| 8 | Siembras que hay que cobrar en la clase 4: la slide 24 («los dos síntomas») y la promesa de que las diez líneas del notebook se vuelven `loss.backward()`. | coordinación | equipo de la clase 4 |
| 9 | La regla `.reveal sup/sub` quedó local en `slides.html`. Si otra clase usa `<sup>` le va a pasar lo mismo: conviene subirla a `_shared/css/curso.css`. | base | quien mantenga la base |

---

## 6. Cómo reproducir esta verificación

```bash
# notebook
python3 -c "import nbformat;nbformat.validate(nbformat.read('clases/03-loss-y-gradiente/notebook.ipynb',as_version=4))"
time python3 -m nbconvert --to notebook --execute \
     --output /tmp/out.ipynb clases/03-loss-y-gradiente/notebook.ipynb
# y sin red:
env HTTPS_PROXY=http://127.0.0.1:9 HTTP_PROXY=http://127.0.0.1:9 \
    python3 -m nbconvert --to notebook --execute --output /tmp/out2.ipynb \
    clases/03-loss-y-gradiente/notebook.ipynb

# enlaces
curl -s -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/3b1b/manim/master/README.md
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
`NODE_PATH=/opt/node22/lib/node_modules`), abriendo por `file://` **a la profundidad real**
(`clases/03-loss-y-gradiente/…`) con un `context.route('**/*')` que aborta cualquier `http(s)`
y lleva la cuenta. Para las slides: recorrer las 36 con `Reveal.slide(i,0)`, comparar
`section.present.scrollHeight` contra `Reveal.getConfig().height`, y sacar screenshot de
cada una. Para las viz: `frame.evaluate` sobre `.panel` (`scrollHeight` contra
`clientHeight`) mide el recorte del panel embebido.
