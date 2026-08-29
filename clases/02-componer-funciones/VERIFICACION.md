# Verificación adversarial — Clase 2

**Componer funciones: dibujar lo imposible** · `clases/02-componer-funciones/`
Segunda pasada, hecha por otro agente que no construyó el material y que **no le
creyó nada al informe de construcción**. Todo lo que dice acá se comprobó
corriendo el código: `nbconvert --execute`, `nbformat.validate`, Chromium por
Playwright con `context.route` abortando cualquier `http(s)`, `curl` contra cada
host, y **mirando los PNG con los ojos** (35 slides barridas, 5 viz en tema claro
y oscuro, antes y después de mover cada control, y las 9 figuras del notebook).

---

## 1. Veredicto

**La clase se puede dictar.** La base que dejó el equipo de construcción era
buena y los números eran reales. Se encontraron **11 problemas** y **se
arreglaron los 11**. Dos eran de los que arruinan un momento en el aula:

- **`red-como-dibujante.html` mostraba un gráfico vacío al randomizar.** El guion
  del docente dice «apretá randomizar dos veces: sale cualquier cosa». Lo que
  salía era **nada**: con las alturas al azar la salida se iba a ±5 mientras los
  datos viven entre 0 y 0,2, así que la curva azul quedaba fuera del cuadro. En
  el aula eso se lee «se rompió», no «una red sin entrenar dibuja porquería».
- **Cualquier viz abierta con el tema oscuro ya guardado se dibujaba con la
  paleta clara.** Es un bug de `_shared/js/viz.js` que afecta a las diez clases
  (ver sección 5). Parcheado localmente en los cinco archivos de esta clase.

Y uno de rigor, que es de la peor categoría porque *enseña algo falso*:
**`la-recta-imposible.html` afirmaba que al mover las perillas de más «el
desajuste no baja ni un poquito» y «la forma no cambia».** Las dos cosas son
falsas y la pantalla las desmiente en el acto: la recta se mueve. Lo verdadero,
y lo que ahora dice, es que **cualquiera sea el juego de perillas siempre queda
una recta y el desajuste nunca baja del piso de 0.00150**.

| Chequeo | Resultado |
|---|---|
| Entregables | 6 de 6, más 5 viz. Ninguno vacío ni a medias |
| `nbformat.validate` | válido, 32 celdas |
| `nbconvert --execute` | **0 errores**, 9 figuras · **8,9 s** de reloj |
| Notebook **sin red y sin `datos/cache/`** | 0 errores y **salida idéntica byte a byte** a la corrida con cache |
| Consola del navegador (slides + 5 viz, claro y oscuro) | **0 errores**, 12 combinaciones |
| Requests externas (`route` abortando `http(s)`) | **0** |
| Barrido de las 35 slides | 0 errores, ninguna se sale de cuadro |
| Ventana angosta (420 px) en las 5 viz | 0 scroll horizontal |
| Números de las slides y las viz contra el código | **todos coinciden** (sección 3) |
| Citas de `referencias.md` | 10 de 10 reales y bien citadas; 0 URLs inventadas |
| Presupuesto de tiempo | continuo, 0 → 120, sin huecos ni solapes |

---

## 2. Lo que se arregló

### Rompía un momento de la clase

**1. `viz/red-como-dibujante.html` — «randomizar» dejaba el cuadro vacío.**
`w2` al azar en ±2 sobre activaciones de hasta ~5 da salidas del orden de ±10;
el eje va de −0,03 a 0,21. Medido: desajuste **23,75** y curva invisible.
*Arreglado:* después de sortear, las alturas y la base se **reescalan** para que
la curva entre en el cuadro (`salida' = k·(salida − mín) + 0,02`). La **forma
sigue siendo la que salió al azar**, no se corrige nada, y el panel lo dice con
todas las letras. Ahora el desajuste típico queda en **0.00348** — peor que la
mejor recta (0.00150), que es exactamente la lección — y la porquería **se ve**.

**2. Tema oscuro guardado = dibujo claro.** Ver sección 5. Parcheado en los cinco
archivos con `Viz.recargarColores()` después de `Viz.botonTema()`.

### Rigor (enseñaban algo falso)

**3. «El desajuste no baja ni un poquito» / «la forma no cambia»** al agregar
perillas, en el `aha` y en el panel de `la-recta-imposible.html`, y en las notas
del docente de la slide 5. Reescrito a lo que efectivamente pasa: la recta se
mueve, pero sigue siendo una recta y **nunca baja del piso de 0.00150**.

**4. «Los que son *claramente* ruido de medición»** (slide 31 y pie de
`rampas.html`). La serie es una media móvil de 3 años: el ruido año a año ya
está parcialmente alisado. Ahora dice «los que casi seguro son ruido —el léxico
lo escribimos nosotros—», que es lo que `datos/README.md` §1.2(a) y (b)
sostienen. El argumento fuerte, que no cambió, es **96 perillas para 36 datos**.

**5. La slide 3 no decía que la serie está suavizada.** En un curso que insiste
en que el instrumento se declara, eso no podía faltar. La bajada ahora dice
«suavizados con una media móvil de 3 años», y las notas traen la frase para
cuando alguien pregunte («la serie contesta *en qué parte del período el tema
estuvo en agenda*, no *cuánto habló ese año*»).

**6. El notebook tenía tres umbrales distintos para el mismo TODO 4.** El texto
decía «bajá de 0.00056», el `print` decía «objetivo: menos de 0.00050» y el
premio estaba en 0.00040. Ahora el `print` dice lo mismo que la consigna:
*bajar de 0.00056; abajo de 0.00040 es excelente*.

**7. La slide 26 prometía un efecto local para *cualquier* flecha.** Sólo los
**pesos de salida** mueven un tramo dejando el resto quieto; los pesos de entrada
y los sesgos **mueven el codo de lugar**. Comprobado moviendo las 19 flechas. El
pie ahora distingue las dos cosas y manda a probar las dos.

### Coherencia y aula

**8. La numeración de slides estaba corrida en uno después de la pausa.** Reveal
muestra `n / 35` **contando la pausa** (verificado por screenshot: «Y ahora, el
truco» es la 21, no la 20), pero los comentarios del HTML, las notas del docente
y `notas-docente.md` §3, §5, §6 y §7 numeraban sin contarla. Un docente que
buscaba «la slide 30» encontraba otra. *Arreglado:* **todo** usa ahora la
numeración de reveal; la pausa es la 19.

**9. El bloque práctico 2 tenía la duración de emergencia metida en el plan
normal.** La slide decía «Veinte minutos», el minutado del docente le daba 12, y
la sección «si vas atrasado» ofrecía *achicarlo a 12* como recorte. *Arreglado:*
retimado el tramo post-pausa; los **dos** prácticos duran 17 minutos, que es lo
que realmente queda, y las slides dicen 17. La pausa no se movió (55-65) y el
total sigue siendo 120 exactos. La diferencia de 5 minutos contra `PROGRAMA.md`
está declarada en `notas-docente.md` §2, con la instrucción de qué recortar si
se quiere respetar el reloj del programa al pie de la letra.

**10. Dos errores de concordancia que se proyectan en pantalla.**
`rampas.html` decía «Con **1 rampa** bien **puestas**…» en el panel, justo en el
momento fuerte; `sin-no-linealidad.html`, «Las **1 caja es** una sola recta».

**11. En la slide, las tarjetas de rampa quedaban cortadas al medio.** Con
`max-height: 186px` y tarjetas de 245 px, los botones «sube/baja» quedaban fuera.
Subido a 252 px, que entra sin agrandar la página (el alto lo manda el panel, no
el taller). Verificado por screenshot dentro del iframe con 8 rampas.

**Además** (mejoras chicas, no defectos): los mini-gráficos del taller ahora se
repintan al cambiar de tema; la slide 17 muestra la línea de `rampa()` **tal cual
la van a escribir en el notebook**; y las notas de la slide 22 explican cómo
dejar la imagen más limpia posible («qué mostrar debajo» → «nada, sólo el
resultado») para el silencio de los cinco segundos, porque con 8 rampas las
sumas parciales cruzan el cuadro y ensucian justo el momento aha.

---

## 3. Los números, verificados uno por uno

Reproducidos con el script de `notas-docente.md` §10 sobre
`datos.serie_menciones("inflacion", 1984, 2019, suavizada=True)` (n = 36, la
serie va de **0,021 a 0,184 % de las palabras** — la escala es porcentaje, como
manda la trampa 3 de la espina, y ningún eje la multiplica de nuevo).

| Afirmación | Dónde aparece | Medido | ¿Coincide? |
|---|---|---|---|
| mejor recta = `0.00150` | slides 4, 22, 31 · 4 viz · notebook | 0.001496 | ✅ |
| raya en el promedio = `0.00152` | slide 4 · 2 viz | 0.001516 | ✅ |
| la recta explica el **1,3 %** | slides 4 · notas §1 · notebook | 0.01326 | ✅ |
| 1 rampa = `0.00084` | slide 22 · `rampas.html` | 0.000843 | ✅ |
| 2 rampas = `0.00062` | slide 22 · `rampas.html` | 0.000624 | ✅ |
| 4 rampas = `0.00032` | slide 22 · `rampas.html` | 0.000318 | ✅ |
| 8 rampas = `0.00014` | slides 22, 31 · `rampas.html` | 0.000144 | ✅ |
| 32 rampas = `0.00001` | slide 31 · `rampas.html` | 0.000014 | ✅ |
| 24 perillas (8 rampas) / 96 (32) / **36 datos** | slide 31 | 3·8, 3·32, n=36 | ✅ |
| red buena de 6 rampas = `0.00018` | `red-como-dibujante.html` | 0.000178 | ✅ |
| la red `[1,6,1]` tiene **19 perillas** | `red-como-dibujante.html` | 6+6+6+1 | ✅ |
| 4 rampas del notebook = `0.00056` | slide 29 · notebook | 0.00056 | ✅ |
| soluciones del TODO 4: `0.00044` y `0.00027` | `notas-docente.md` §9 | 0.00044 / 0.00027 | ✅ |
| `for` vs matrices difieren `6.94e-18` | notebook celda 28 | 6.94e-18 | ✅ |
| red `[1,4,1]` = **13** parámetros | notebook · cuestionario 6 | 4+4+4+1 | ✅ |
| `doble(mas_diez(3))=26`, al revés `16` | slides 8 y 9 · lego · notebook | ✅ | ✅ |
| TODO 1 da `18` y `13` | `notas-docente.md` §9 | 18 / 13 | ✅ |

**Ningún número inventado.** El *clamp* de altura (`MAX_ALTURA = 0.15`) de
`rampas.html` no altera ninguno de los atajos: el peso más grande que sale de
mínimos cuadrados es 0,091.

---

## 4. Lo que se miró con los ojos

- **35 slides** barridas una por una a 1280×720 con los `fragment` revelados.
  Ninguna se corta, ninguna se encima, ninguna es un muro de texto sin imagen,
  ejemplo o pregunta. La más cargada (la 5, «¿y si le agrego perillas?») no tiene
  figura pero sí el ejemplo algebraico concreto: pasa la regla de oro.
- **Los 5 iframes cargan de verdad** dentro de las slides (screenshot de las
  slides 4, 13, 22 y 26 con la viz viva adentro), y se puede interactuar con
  `rampas.html` **desde la slide** (apretados «8» y «32» dentro del iframe).
- **Cada viz, control por control:** los cinco atajos de `rampas.html` con su
  desajuste leído del DOM; el select de tres modos; el checkbox de errores;
  «+ agregar», «acomodar», «empezar de nuevo»; el arrastre del codo; 15
  randomizaciones seguidas en `sin-no-linealidad.html` (contador: **16/16
  rectas**, desviación `0.000000` en todas); el intercambio de bloques del lego
  (**16 → 26**, con el fantasma gris y «mismas cajas, mismas perillas, otro
  resultado»); las 19 flechas de `red-como-dibujante.html`, el hover de las
  bolitas, randomizar y volver; y el 2/3/5 perillas de `la-recta-imposible.html`.
- **Los aha se ven.** Con 8 rampas la curva azul tapa a la negra; con 32 pasa por
  todos los puntos y el panel se niega a mostrar 96 sliders con el argumento que
  hace de pie para la clase 3.
- **Las 9 figuras del notebook**: todas con ejes rotulados en castellano
  (`año`, `% de palabras`), título, leyenda y el MSE anotado. Se entienden solas.
- **KaTeX**: las slides **no tienen ni una fórmula** (la única del material está
  en el markdown del notebook, que Jupyter renderiza). El plugin queda cargado y
  configurado, sin nada que hacer. No es un defecto: es coherente con «nada de
  matemática sin una imagen al lado».

---

## 5. Lo que queda abierto

| # | Qué | Para quién |
|---|---|---|
| 1 | **Bug de `_shared/js/viz.js`, afecta a las diez clases.** `botonTema()` aplica el `data-tema` guardado en `localStorage` pero **no llama a `recargarColores()` ni redibuja**, así que una viz abierta con el tema oscuro ya guardado dibuja el canvas con la paleta **clara** sobre fondo oscuro. Verificado por screenshot en las 5 viz de esta clase antes del parche. El arreglo son dos líneas dentro de `botonTema()`, después del `setAttribute`: `recargarColores();` y `global.dispatchEvent(new Event('viz:tema'));`. **No se tocó el archivo compartido** para no pisar a los otros nueve equipos; está parcheado localmente en las 5 viz de la clase 2, con el comentario que lo explica. | quien mantenga la espina |
| 2 | `_shared/css/curso.css` no declara `box-sizing: border-box` (lo dejó anotado el equipo de construcción y **se confirma**). Parchado local en las 5 viz; a 420 px de ancho no hay scroll horizontal en ninguna. Falta arreglarlo en la hoja compartida. | quien mantenga la espina |
| 3 | **Las 9 marcas `[VERIFICAR URL]` de `referencias.md` siguen ahí.** Se corrió `curl` de nuevo: `raw.githubusercontent.com` responde **200**; `neuralnetworksanddeeplearning.com` da **403**; 3Blue1Brown, Playground y deeplearningbook dan **000**. Las 10 citas se revisaron una por una contra su referencia bibliográfica (revista, volumen, páginas, año, autores) y **las 10 son correctas**: Cybenko 1989 MCSS 2(4) 303-314, Hornik 1991 NN 4(2) 251-257, McCulloch & Pitts 1943 BMB 5 115-133, Breiman 2001 Stat Sci 16(3) 199-231, Molina & Garip 2019 ARS 45 27-45. **Ninguna URL inventada.** Falta que alguien con red las abra y las pase a `[VERIFICADA · aaaa-mm-dd]`. | quien tenga red |
| 4 | **La clase 1 ya existe** (no existía cuando se construyó ésta) y tiene `viz/maquina-de-perillas.html`, `variable-vs-parametro.html` y `zoo-de-funciones.html`. Se comprobó que **el vocabulario cierra**: el zoo de la clase 1 es recta, parábola, exponencial, sigmoide, seno y escalón, y la slide 2 de la clase 2 lista exactamente esos seis; las dos usan «medidor de desajuste»; y la slide de cierre de la clase 1 anuncia «Clase 2: componer funciones para dibujar lo imposible». **No hace falta tocar nada.** `viz/la-recta-imposible.html` se queda: usa la serie de `inflacion` y los botones 3/5 perillas, que la viz de la clase 1 no tiene. | nadie, es sólo para saber |
| 5 | **La siembra del sobreajuste está puesta y hay que cobrarla.** Botón «32» de `rampas.html`, slide **31** (ojo: 31, no 30, ver arreglo 8). Los números para cerrarla están en `notas-docente.md` §10. Aviso honesto para el equipo de la clase 4: como la serie está suavizada, con 32 rampas la curva **no se ve grotesca**, se ve prolija. El golpe visual es flojo; el que sirve es el numérico (96 perillas, 36 datos, desajuste 0.00001). Conviene cobrar la promesa con ese par de números y no sólo con la imagen. | equipo 4 |
| 6 | El TODO 3 («¿cuántas rampas para una meseta?») admite **3 y 4** y las dos son correctas (3 sube-frena-baja; 4 si además querés que termine plana). Está anotado en las notas y en la slide 20. | equipo 3 |
| 7 | En `sin-no-linealidad.html` los codos de la cadena con ReLU se sortean con la restricción de que el corte caiga adentro del rango que le llega a esa caja, para que la cadena no se apague. **Está declarado en el pie de la página** y nombrado (*dying ReLU*). Consecuencia visible: con 4-6 cajas suelen verse **2 codos**, no N−1, y el cartel cuenta los que efectivamente se ven, que es lo honesto. Si la clase 3 o la 4 quieren mostrar el fenómeno de verdad, acá está el lugar para desactivar la restricción con un toggle. | equipos 3 y 4 |
| 8 | El plan de esta clase corre el práctico 2 de **90 a 107** en vez de 85 a 105 como dice `PROGRAMA.md`. Está declarado y justificado en `notas-docente.md` §2, con qué recortar para volver al reloj del programa. | quien coordine el programa |

---

## 6. Cómo reproducir esta verificación

```bash
# el notebook, con y sin red y sin cache
python3 -m nbconvert --to notebook --execute \
        --output /tmp/out.ipynb clases/02-componer-funciones/notebook.ipynb

# los números de las slides y de las viz
python3 - < <(sed -n '/^```python/,/^```/p' \
              clases/02-componer-funciones/notas-docente.md | sed '1d;$d')
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`),
abriendo por `file://` con `context.route('**/*')` abortando toda URL `http(s)` y
contándolas, en tema claro y oscuro (sembrando `localStorage['dlss-tema']`
**antes** de cargar: es la única forma de destapar el bug 1 de la sección 5).
