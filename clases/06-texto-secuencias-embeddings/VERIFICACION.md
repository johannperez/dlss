# Verificación adversarial — Clase 6

**La forma de los datos manda: texto, secuencias y embeddings**
Fecha: 2026-08-29 · Todo lo que dice acá se comprobó **corriendo el código y mirando los
píxeles**, no leyendo el HTML.

---

## 1. Veredicto

**La clase se puede dar.** Estaba bien construida y con los números medidos de verdad, que
es lo difícil. Se encontraron **25 problemas** y **se arreglaron los 25**. Cuatro eran
graves —uno rompía una slide entera, uno era una afirmación **falsa** sobre el corpus, uno
prometía un momento aha que la viz **no** producía, y uno hacía que el gancho de la clase
no cerrara con la slide siguiente—. El resto son de rigor fino, de tipografía y de
legibilidad en proyector.

| Chequeo | Resultado |
|---|---|
| `nbformat.validate` | **válido** · 45 celdas (23 md, 22 código) |
| `nbconvert --execute` | **0 errores**, tres corridas: **19,0 · 17,3 · 17,5 s** de pared |
| Notebook sin red y sin cache | **idéntico**: se movió `datos/cache/` entero y la salida sale byte a byte igual salvo la línea que imprime el tiempo medido |
| Consola del navegador (slides, 40 slides, una por una) | **0 errores** |
| Requests externas (todo `http(s)` abortado con `context.route`) | **0** en slides y en las 5 viz |
| Las 5 viz sueltas | **0 errores** de consola, tema claro y oscuro |
| Los 6 `<iframe>` adentro de las slides | **cargan**, los 6 con `body class="curso embebido"` |
| KaTeX | **renderiza** desde el vendor, sin red (verificado inyectando una fórmula y mirando el `.katex` en pantalla) |
| Ventana angosta (720 px) | 0 errores, **0 scroll horizontal** (había 4 px, arreglado) |
| Reproducibilidad de `medir-embeddings.py` | borré los `.npz`, regeneré de cero: los **1,42 MB** de JSON salen **idénticos** salvo `meta.segundos` |
| Colores hardcodeados / CDNs / rutas absolutas | **ninguno** |
| Presupuesto de tiempo | los bloques de `notas-docente.md` §2 son continuos y suman **120 min exactos** |

---

## 2. Lo que estaba mal, y cómo quedó

### Graves

**1. El gancho no cerraba con la slide siguiente.**
La slide 3 mostraba *«La comisión rechazó al ministro» / «El ministro rechazó a la
comisión»* (las frases que piden `PROGRAMA.md` y la spec) y la slide 4, titulada **«Las
mismas, contadas»**, mostraba las bolsas de **otro par** (`el gobierno criticó al
congreso`). No eran «las mismas». Y hay un motivo real por el que el constructor cambió de
par: en castellano **«al» es «a» + «el»**, así que el par del gancho **no** da bolsas
idénticas con un tokenizador ingenuo. El ejemplo de la especificación es, literalmente,
falso para el pipeline de la clase.
*Arreglado sin tirar el gancho:* la slide 4 muestra ahora las bolsas **reales** del par del
gancho, señala que lo único que cambia son los artículos, y muestra abajo las dos bolsas
**sin palabras vacías** —idénticas—, que es lo que hace cualquier pipeline de análisis de
contenido. El caso sin asterisco (`gobierno`/`congreso`) sigue estando en el notebook y en
`viz/bolsa-vs-orden.html`, y ahora está anotado en las notas del docente. **La moraleja
quedó mejor que el ejemplo limpio**: qué tan idénticos son dos textos depende de las
decisiones de preprocesamiento que tomaste vos.

**2. La slide 26 («Todo lo de hoy, en tres líneas») era ilegible.**
El bloque de código se desbordaba de su caja por arriba y por abajo, con las líneas
pisándose. Causa: `curso.css` estiliza `.reveal pre code` pero **no le pone
`display:block`**, y el `reveal.css` vendorizado tampoco lo trae (el `dist` que hay en
`_shared/vendor` está recortado). Los equipos de las clases **1 y 4 ya se toparon con
esto** y lo parchearon a mano en su propio `<style>`, con un comentario.
*Arreglado* con el mismo parche local (`.reveal pre code { display:block; overflow-x:auto }`)
y reescribiendo el snippet en cuatro líneas más cortas. **Ver §4: las clases 7 y 10 siguen
rotas por lo mismo.**

**3. Una afirmación falsa sobre el corpus, en la slide 22.**
Decía *«niñas» ni siquiera está en el corpus*. **Es falso**: `niñas` aparece **11 veces**
en los 35 discursos. Lo que pasa es que no entra al **vocabulario de las 2.000 más
frecuentes**. (El `datos-texto.js` que genera el script dice bien «no está en el
vocabulario»; la slide se comió las dos palabras que importaban.)
*Arreglado*, y de paso mejorado: las notas del docente traen ahora los conteos medidos —
**niños 78 · niñas 11 · chicos 69 · chicas 2**— que son un hallazgo mucho más fuerte que
la afirmación falsa que reemplazan.

**4. La viz de la memoria prometía un aha que no producía.**
La slide 32 y el propio cartel de la viz decían *«agrandá la mochila al máximo: el olvido
se hace más lento y **igual llega abajo**»*. Lo medí: con la mochila al máximo (512
dimensiones) de la palabra clave queda **40 %**, y el modelo **acierta** (70/30). La barra
**no** llega abajo. Un docente que dijera esa frase en el aula quedaría desmentido por su
propia pantalla.
*Arreglado* diciendo lo que efectivamente pasa, que además enseña lo mismo y mejor: con la
mochila chica queda **0 %** y es moneda al aire; con **64 veces más memoria** llega con
**40 %**; agrandar la memoria **posterga** el problema (y con una oración el doble de larga
volvés a cero).

### De rigor

**5. Un vecino que no era el vecino.** La tabla de la slide 21 daba `pobreza → … exclusión
0,57` como sexta vecina. La sexta real es **`lucha` 0,57** (`exclusión` es la octava). Y las
listas estaban podadas en silencio (se sacaron `de`, `entre`, `provincia`, `docente`).
*Arreglado:* el valor real, y **un pie que declara la poda**. En una clase que repite que
toda decisión de medición hay que declararla, esconderla era un autogol.

**6. «Aciertan dos de diez» sin decir con qué criterio.** El criterio del generador es
generoso (la palabra esperada entre las **cinco** primeras). Con el criterio estricto
—que salga primera— acierta **una** de diez. Ahora lo dicen la slide 22 **y** el panel
«¿acertó?» de la viz, que antes cantaba «acertó» mientras en pantalla la primera respuesta
era otra palabra.

**7. Los antónimos, en el notebook, arrancaban con el contraejemplo.** La celda que
demuestra *«los antónimos quedan cerquísima»* imprimía primero **`guerra`/`paz` = 0,364**,
que no es alto, sin ningún comentario. Peor: no había vara para saber si 0,78 es mucho.
*Arreglado y medido:* la celda ordena los pares de mayor a menor, calcula la **distribución
de similitudes entre todos los pares del vocabulario** (mediana **0,226**, p90 **0,364**,
p99 **0,516**) y dice explícitamente que `guerra`/`paz` —el ejemplo clásico— **no funciona
en este corpus** y por qué (`guerra` aparece 33 veces con *armas, muerte, dolor*; `paz` 112
con *operaciones, naciones, derechos humanos*). La slide 28 lleva ahora la misma vara.
Esto convirtió una celda que vendía humo en la celda más honesta del notebook.

**8. Una URL marcada `[VERIFICADA]` que da 404.**
`raw.githubusercontent.com/lucariel/discursos_presidenciales/` → **404**. *Arreglado:*
ahora figuran las dos rutas que **sí** probé con `curl` (`…/master/README.md` → 200 y
`…/master/data/sesiones_ordinarias/1984-raul_alfonsin.txt` → 200) y la portada del repo
queda marcada `[VERIFICAR URL]` porque `github.com` en HTML da 403 desde acá.

**9. `viz/tokenizador.html` tenía dos bytes NUL (`0x00`) literales** metidos en un string
de JavaScript como separador de claves. El archivo era **binario** para `grep`, `diff` y
media herramienta de texto. *Arreglado* escribiendo el separador como `'\u0000'`: mismo comportamiento en
el navegador, archivo de texto para las herramientas.

**10. La siembra de la clase 8 preguntaba por erres donde no había ninguna.** El panel
*«¿cuántas veces aparece la letra R?»* caía sobre `inconstitucionalidad` (cero erres) o
sobre `índice` (cero erres). *Arreglado:* el panel prefiere una palabra que **tenga**
erres, y se agregó el ejemplo **`irreprochable`** —tres erres, y el BPE la parte en cinco
fichas (`ir · re · proc · hab · le`), ninguna de ellas una letra suelta—. La siembra ahora
se planta de verdad.

**11. `notas-docente.md` decía que el programa pide «20 y 25» minutos de práctico.**
`PROGRAMA.md` pide **20 y 17**, que es exactamente lo que la clase hace. *Corregido*, y
aclarado que lo único que se movió es **dónde** cae el segundo práctico, no cuánto dura.

**12. `recursos/glosario.md`:** decía que «inconstitucionalidad» sale en **cuatro** pedazos
(la clase entera dice **cinco**), citaba a Firth con otra traducción que la de las slides, y
mandaba el OOV a un cajón `<unk>` cuando las viz del curso lo llaman `<desc>`. Los tres
corregidos.

**13. El ítem 10 del cuestionario no medía nada.** Dos de sus tres distractores eran
descartables sin pensar («porque lee de derecha a izquierda», «porque no usa embeddings»).
*Reemplazados* por dos que sí tientan y sí diagnostican: **«porque promedia y un promedio
no tiene orden»** (es verdad… de *otra* cosa vista hoy, y separa a quien entendió las dos
mitades de la clase) y **«porque las palabras lejanas quedan fuera del vocabulario»**
(mezcla memoria con vocabulario). Las soluciones explican las dos confusiones.

### De legibilidad en proyector

**14.** La slide 39 («Glosario de hoy») **cortaba las dos últimas filas** de diez. Arreglado
con una variante compacta de `.glosario-lista`.
**15.** En `viz/espacio-de-embeddings.html` **embebida**, las listas de vecinas quedaban
cortadas por el borde del `<iframe>` (se veían 8 de 10 en la slide 20 y 3 de 4 en la 24).
Arreglado: el mapa embebido baja de 300 a **250 px** y el modo eje muestra **3** en vez de 4
cuando está adentro de una slide. Ahora entra todo.
**16.** El botón flotante **«TEMA»** (`position:fixed`, abajo a la derecha) **se le montaba
encima a la última línea** del cartel «MOMENTO AHA» en las cinco viz sueltas. Arreglado con
aire abajo. *Es un problema de la base, no de esta clase* — ver §4.
**17.** `viz/memoria-que-se-olvida.html` provocaba **4 px de scroll horizontal** a 720 px de
ancho. Arreglado (`box-sizing:border-box`).
**18.** `viz/tokenizador.html` mostraba **«5.00 fichas por palabra»** (punto decimal, contra
la coma que usa toda la clase) y **«1 palabras»**. Arreglados los dos.

### Menores

**19.** `viz/one-hot-vs-embedding.html` decía *«la posición 1714, que es el orden alfabético
de nada»*. Se lee como un error de tipeo. Reescrito: *«y ese número no significa nada: no es
un orden alfabético ni una medida de nada»*.
**20.** El notebook decía **«Son cuatro segundos»**; lo medí tres veces y da **4,3 · 5,1 ·
4,3**. Ahora dice «unos cuatro segundos (lo medimos: entre 4 y 5)».
**21.** El notebook usaba un par de frases distinto del gancho de la clase sin explicar por
qué. Ahora lo explica en dos líneas (es el mismo problema del punto 1).
**22.** La configuración de KaTeX incluía el delimitador de **un solo `$`** en un deck que
**no tiene una sola fórmula**. Un `$5.000 millones` en una slide futura se habría comido el
texto en silencio. Sacado (queda `$$…$$` y `\(…\)`, como en la clase 1).
**23-25.** Tres arreglos de coherencia interna que salieron de los anteriores: el pie de la
tabla de vecinas, la nota del docente sobre la objeción del alumno en la slide 4, y la
referencia de slide en las soluciones del ítem 10.

---

## 3. Lo que verifiqué y estaba bien (para que no se vuelva a mirar)

- **Cada número concreto de las slides sale de los datos.** Recalculé desde el corpus:
  `347.714` fichas · `21.289` tipos · `9.712` hapax (**45,6 %**) · `cos(diputados,senadores)
  = 0,863` · `cos(diputados,trigo) = 0,031` · el eje `mujeres↔hombres` (`niños +0,322` …
  `derechos −0,124`) · los antónimos (`0,779 · 0,672 · 0,538 · 0,476`) · las vecinas de las
  cuatro palabras de la slide 21 · **2 de 10** analogías · el cambio semántico de
  `seguridad` (de 8 vecinas siguen 2, y son `nacional` y `consejo`) · la matriz de
  documentos (`0,971` a `1,000` en crudo, `−0,933` a `0,988` centrada). **Todos coinciden.**
- **El notebook no depende de la red ni del cache.** `corpus_mini_gpt()` lee directo de
  `datos/muestras/`, así que la trampa 8 de la espina está respetada: ningún número de la
  clase depende de haber bajado el corpus completo. Lo probé moviendo `datos/cache/` entero.
- **El código de la slide 26 es idéntico al del notebook**, argumento por argumento, y la
  salida que muestra como comentario es la que efectivamente imprime la celda 27.
- **`embeddings_ppmi_svd` hace exactamente lo que el notebook hizo a mano.** Comparé las dos
  implementaciones: `log((M/total)/(p_fila·p_col))` y `log((M·total)/(fila·col))` son la
  misma cuenta, y el SVD es el mismo recorte. El «exactamente los tres pasos de recién» del
  notebook es cierto.
- **Las 11 citas de `referencias.md` existen y están bien atribuidas** (autores, año, revista
  y volumen). Ninguna inventada. Lo que falta son los enlaces, no las obras.
- **Los cinco momentos aha se ven.** Moví cada control de cada viz y miré la pantalla: el
  patrón de colores que casi no cambia entre `diputados` y `senadores` y sí con `trigo`; las
  vecinas de `pobreza` que nadie escribió; el eje que ordena las ocupaciones solo; el
  `1,000` exacto del par de agencia y el `0,984` de la negación; y el 50/50 de la mochila
  chica. Los cinco pasan.
- **Tono.** Voseo parejo, humor sin payasada, cero condescendencia, ninguna slide sin imagen,
  ejemplo o pregunta. Las secciones más largas (`notas-docente.md` §9, las soluciones del
  cuestionario) son densas **a propósito**: son material del docente, no de proyección.
- **La pausa está** (slide 18), dura 10 minutos y tiene slide propia.
- **Los puentes están explícitos**: el de la clase 5 en la slide 2 (barajar los píxeles) y el
  de la clase 7 en la 36, marcado en las notas como lo único que nunca se recorta.

---

## 4. Lo que queda abierto

| # | Qué | Para quién |
|---|---|---|
| 1 | **`.reveal pre code` no trae `display:block` en la base.** No es un problema de esta clase: `curso.css` lo estiliza sin `display`, y el `reveal.css` vendorizado no lo trae. Lo comprobé abriendo las cinco clases con bloques de código: **las clases 7 y 10 tienen ahora mismo sus bloques de código desbordados e ilegibles** (las 1 y 4 lo parchearon a mano, y la 6 ahora también). La solución de una línea va en `curso.css` y arregla las cuatro de una. | equipo de la base (y avisar a los equipos 7 y 10) |
| 2 | **El botón flotante «TEMA» se monta encima del texto** al final de cualquier viz suelta larga (`position:fixed` sin aire debajo). Lo parcheé en las cinco viz de esta clase; probablemente pasa en las otras nueve. Corresponde una línea en `curso.css`. | equipo de la base |
| 3 | **11 entradas de `referencias.md` siguen `[VERIFICAR URL]`.** Desde este contenedor sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y `raw.githubusercontent.com`; las cuatro que sí se podían probar están **[VERIFICADA · 2026-08-29]** con `curl` y una de ellas estaba mal (ver §2.8). Las citas están completas y son correctas; faltan los enlaces. | quien tenga red |
| 4 | **El modo «dos épocas» entrena sobre 16 y 15 discursos.** Parte del cambio de vecinas es ruido. La viz lo dice («un paper serio repite esto con remuestreo») pero **no está cuantificado**. Ahí hay un ejercicio de bootstrap listo para la clase 10. | equipo 10 |
| 5 | **La spec pide un toggle «sólo sustantivos / verbos / todo»** en la viz central. Se entrega en su lugar «esconder las palabras de función» + «sólo el léxico político y económico», porque etiquetar categorías gramaticales sin red y sin spaCy no se puede. **Desvío consciente**, y los dos toggles hacen el trabajo que la spec quería (limpiar la nube para que se lean los clusters). | anotado, no requiere acción |
| 6 | **La spec de la slide 16 describe el aprendizaje como «tapar una palabra y adivinarla».** La clase explica en cambio contar → descontar la frecuencia → comprimir, que es **lo que el notebook efectivamente corre**. Coherencia por encima de la letra de la spec. | anotado, no requiere acción |
| 7 | **`meta.segundos` de los `datos-*.js` mide la máquina, no el algoritmo.** Está en 4,2 (que es lo que da con la máquina tranquila, y coincide con los 4,3 que mide el notebook). Regenerando con la máquina cargada me dio 17,6. **Ningún archivo lo muestra en pantalla**, así que no molesta; pero si alguien regenera los datos, que no se asuste y que **no** cambie las prosas que dicen «unos cuatro segundos». | quien regenere los datos |
| 8 | **Para el equipo de la clase 8** (sigue vigente lo que dejó el constructor): el BPE del tokenizador —600 fusiones y 660 fichas de vocabulario, entrenadas sobre el corpus real— está en `datos-texto.js` (`bpe.fusiones`, `bpe.vocabulario`). **Reusalo, no entrenes otro.** Y cobrá la siembra: el panel *«¿cuántas erres tiene?»* queda planteado y sin responder, y ahora el ejemplo que lo planta es **`irreprochable`** (3 erres → `ir · re · proc · hab · le`). | equipo 8 |
| 9 | **Para el equipo de la clase 7**: el puente está cerrado en la slide 36 («¿y si en vez de recordar, miramos directamente?») y marcado en `notas-docente.md` como lo único que nunca se recorta. Se puede cobrar textualmente. | equipo 7 |

---

## 5. Cómo reproducir esta verificación

```bash
# notebook: válido, sin errores, y sin depender de la red ni del cache
python3 -c "import nbformat; nbformat.validate(nbformat.read('clases/06-texto-secuencias-embeddings/notebook.ipynb', as_version=4))"
cd clases/06-texto-secuencias-embeddings
python3 -m nbconvert --to notebook --execute --output /tmp/out.ipynb notebook.ipynb
mv ../../datos/cache /tmp/cache && python3 -m nbconvert --to notebook --execute \
   --output /tmp/out2.ipynb notebook.ipynb && mv /tmp/cache ../../datos/cache   # misma salida

# los datos de las viz salen del corpus y son reproducibles
rm -f clases/06-texto-secuencias-embeddings/cache-*.npz
PYTHONPATH=_shared python3 clases/06-texto-secuencias-embeddings/medir-embeddings.py
# el JSON sale idéntico salvo meta.segundos. Borrá los .npz cuando termines.
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
`NODE_PATH=/opt/node22/lib/node_modules`), abriendo por `file://` **en la ubicación real**
(`clases/06-…/slides.html` y `clases/06-…/viz/*.html`) con un
`context.route('**/*')` que **aborta cualquier `http(s)`**. Se recorrieron las 40 slides
una por una desplegando los fragments, las 5 viz sueltas moviendo cada control, y todo
otra vez en **tema oscuro** y a **720 px** de ancho.
