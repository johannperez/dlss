# Verificación — Clase 2

**Componer funciones: dibujar lo imposible** · `clases/02-componer-funciones/`

Este archivo dice qué se comprobó, cómo, y qué **no** se comprobó. Tiene tres
pasadas: la de construcción, una verificación adversarial (la «segunda
pasada», resumida en la §6) y una revisión posterior que encontró errores que
la segunda pasada había dado por buenos (la «tercera pasada», §1 a §5). Donde
la segunda pasada afirmaba algo que resultó falso, acá se corrige.

---

## 1. Estado actual

**La clase se puede dictar.** El notebook corre de punta a punta sin errores y
todos los números que citan las slides, las notas, el notebook y las viz salen
del script de `notas-docente.md` §10, corrido sobre los datos actuales.

La tercera pasada encontró cuatro problemas de fondo, que ahora están
arreglados:

1. **La «localidad» de la rampa era falsa.** El material decía que cada rampa
   «se hace cargo de un tramo y no se entera de lo que pasa en los otros»
   (notebook, `rampas.html`, `red-como-dibujante.html`, slide 22, notas). Una
   rampa vale cero antes de su codo, pero **después sigue creciendo hasta el
   final**. Ahora todo dice lo correcto: cada rampa dobla la curva en su codo,
   todo lo de la derecha hereda el doblez, lo de la izquierda no se entera. La
   actividad «si vas adelantado» de las notas hacía una predicción numérica
   falsa («la de 2014 duele muchísimo, la de 1990 casi nada»); se reescribió
   con números medidos (§3) para enseñar justamente la no-localidad.
2. **Los números de inflación estaban calculados con un error de borde en los
   datos.** La media móvil de 1984 promediaba con 1975 (el dato anterior de la
   serie, nueve años antes). Con el borde corregido en `ssdl.datos`, el primer
   valor de la serie pasa de 0.0762 a 0.1143 y **cambian todos los
   desajustes** (la recta: 0.00150 → 0.00156; su R²: 1,3 % → 0,5 %). Se
   volvieron a medir y se propagaron a slides, notas, notebook, viz y
   cuestionario. La serie copiada en las 3 viz y en las slides es la nueva.
3. **La cuenta de perillas no cerraba.** Las slides y `rampas.html` contaban 3
   por rampa (el «sube/baja» contado como perilla), el notebook 2 por rampa más
   la base, el cuestionario 3 por neurona. Ahora hay una sola regla, explicada
   donde aparece: la rampa del notebook y de la viz usa **2 números** (codo y
   pendiente con signo); escrita como red de verdad, cada neurona tiene **3
   perillas** (peso de entrada, sesgo, peso de salida) y la red **3n + 1**. Ocho
   rampas: 25 perillas; 32 rampas: 97 (la viz ajusta 33 con los codos fijos, y
   lo dice).
4. **Citas y promesas rotas.** Cybenko (1989) y Hornik (1991) no cubren la
   ReLU; se agregó Leshno, Lin, Pinkus y Schocken (1993) en la slide 24 y en
   `referencias.md`. «Softmax en la clase 4» pasó a la clase 7, donde está.
   «Por qué ReLU y no sigmoide, en serio, en la clase 3/4» no existía en
   ninguna clase: se sacó la promesa y se manda al capítulo 5 de Nielsen.

---

## 2. Qué se arregló en la tercera pasada, archivo por archivo

**`notebook.ipynb`** (sin tocar la celda de bootstrap)
- Celda 21: la no-localidad, la pieza local armada con varias rampas
  («sombrerito» de Nielsen) y la red como **composición** (correr → doblar →
  sumar).
- Celda 22: las alturas y la base de las 4 rampas no estaban «puestas a dedo»:
  eran la solución de mínimos cuadrados. Ahora lo dice, con los valores para
  los datos corregidos (desajuste 0.00060).
- TODO 4: avisa que tocando sólo alturas o base no se mejora (hay que mover o
  agregar codos); pista 3 reescrita según la no-localidad; umbrales nuevos.
- Celda 26: «números que moviste: 2n+1» y, al lado, «como red: 3n+1».
- Celdas 27-28: se sacaron «al lado, la figura» (no había figura) y «el mismo
  número, bit por bit» (la propia celda muestra una diferencia de ~1e-17); el
  comentario ya no afirma un dígito concreto. Se explica la diferencia 2 vs 3
  perillas.
- TODO 5: ya no venía resuelto. Ahora el estudiante toca `suavidad` y predice
  si la sigmoide se parece a una rampa o a un escalón.
- Celdas 8-10: «puntos porcentuales por año»; la recta de 5 perillas usa años
  desde 1984, así los valores quedan en la escala de los datos.
- Celda 15-16: `altura` es una pendiente; se aclara una vez y en las leyendas.
- Celda 31: «En tu propia investigación, desde ya» (antes «Para el lunes»);
  «cualquier figura continua, en el rango de los datos»; sesgo según dónde esté.

**`slides.html`**: números nuevos (slides 4, 22, 29, 31), perillas (17, 31, 35),
localidad (22, 26), teorema con Leshno 1993 y «en un rango acotado» (24, 33,
34), sesgo (27, 34), composición (25), bloque `en tu investigación` (32, con la
tercera pregunta de revisor como anticipo de la clase 4), TODO 5 (29). Los tres
canvas de la presentación tienen `role="img"` y `aria-label`.

**Viz**
- `rampas.html`: serie y números nuevos; atajo de 2 rampas en (1985, 2012), que
  es el óptimo con los datos corregidos; la cabecera ya no dice «el mejor juego»
  para 8 (es el mejor de una búsqueda local); cartel «n rampas · como red: 3n+1
  perillas»; se sacó la anécdota inventada «me llevó una tarde»; el desajuste de
  32 rampas se muestra con 6 decimales (0.000008, no «0.00001»). Accesibilidad:
  `aria-label` en el lienzo y en cada mini-gráfico, y la pendiente **con signo,
  en texto** en cada tarjeta (el signo ya no depende sólo del color).
- `red-como-dibujante.html`: pesos de salida reajustados a los datos corregidos
  (MSE 0.000200, los codos no cambian); el mensaje de la bolita resaltada depende
  del signo del peso de entrada (con w1 < 0 la rampa vive a la izquierda); pie
  sin «cada una se ocupa de un tramo» ni «las seis rampas de la viz anterior»
  (esa viz no tiene atajo de 6); se sacó una promesa sobre normalización en la
  clase 3 que no se cumple. Accesibilidad: los pesos negativos van
  **punteados** además de rojos; `aria-label` en el SVG y en el lienzo.
- `sin-no-linealidad.html`: el contador de rectas era tautológico (copiaba el de
  randomizaciones); ahora cuenta una recta sólo si la cadena, medida, se desvía
  de una recta menos de 1e-9 relativo a su tamaño. Arranca con N = 5 cajas, como
  dice el pie. *Dying ReLU* se nombra como pariente del fenómeno de
  entrenamiento, no como el mismo. `aria-label` en los dos lienzos.
- `la-recta-imposible.html`: números nuevos; el umbral de «ya llegaste al piso»
  bajó de ×1,02 a ×1,003 (con los datos nuevos, ×1,02 ya aceptaba la raya en el
  promedio). `aria-label` dinámico en el lienzo.
- `lego-de-funciones.html`: `aria-label` en los tres mini-gráficos, en los
  selects y en los sliders.

**`notas-docente.md`**: arco y tiempos con los números nuevos; confusión nueva
«cada rampa se ocupa de un tramo»; pregunta difícil 5 reescrita (polinomio
global contra base lineal por tramos, extrapolación lineal, *splines*);
«si vas adelantado» con números medidos; ecualizador de 25 perillas; sección 5
del notebook como tarea con tope de 1 h; soluciones del TODO 4 y TODO 5
recalculadas; §10 con el script completo (atajos, óptimos exhaustivos, 32
rampas, red buena, sacar rampas) y la nota sobre el cambio de datos.

**`cuestionario.md` / `cuestionario-soluciones.md`**: pregunta 8 (sesgo según
dónde esté), pregunta 9 C («pueden representarla»), pregunta 11 alineada con las
dos preguntas de revisor de la clase (la que falta + una tercera), 4(b) «puede
pasar», fila «contar las neuronas» = 4, se sacó «Python 2», softmax → clase 7,
`[EN TU INVESTIGACIÓN]` y «al empezar la clase 3». El cuestionario dice que se
hace en casa antes de la clase 3.

**`referencias.md`**: Leshno et al. 1993 (6b), Hornik con la salvedad de
«acotadas», Nielsen con la aclaración de piezas locales, lectura prioritaria
sólo la 1 (media hora) y el resto sin plazo, sin «esta semana», promesas
corregidas.

---

## 3. Los números, verificados uno por uno

Medidos con el script de `notas-docente.md` §10 sobre
`datos.serie_menciones("inflacion", 1984, 2019, suavizada=True)` (n = 36, de
0,021 a 0,184 % de las palabras), con la versión corregida de `ssdl.datos`.

| Afirmación | Dónde aparece | Medido |
|---|---|---|
| mejor recta = `0.00156` | slides 4, 22, 29 · 4 viz · notebook | 0.001561 |
| raya en el promedio = `0.00157` | slide 4 · 2 viz · notebook | 0.001568 |
| la recta explica el **0,5 %**, sube 0,00026 por año | slide 4 · notas §1 · notebook · viz | R² = 0.0046; pendiente 0.000260 |
| 1 rampa = `0.00092` (codo 2013) | slide 22 · `rampas.html` | 0.000916 (óptimo exhaustivo) |
| 2 rampas = `0.00065` (1985, 2012) | slide 22 · `rampas.html` | 0.000648 (óptimo exhaustivo) |
| 4 rampas = `0.00034` | slide 22 · `rampas.html` | 0.000339 (óptimo exhaustivo) |
| 8 rampas = `0.00016` | slides 22, 31 · `rampas.html` · notebook | 0.000164 (mejor de 60 búsquedas locales) |
| 32 rampas = `0.000008` | slide 31 · `rampas.html` | 0.0000076 |
| 25 perillas (8 rampas) / 97 (32) / 33 ajustados / **36 datos** | slides 17, 31, 35 · `rampas.html` | 3·8+1, 3·32+1, 32+1, n = 36 |
| red buena de 6 rampas = `0.00020` | `red-como-dibujante.html` | 0.000200 |
| la red `[1,6,1]` tiene **19 perillas** | `red-como-dibujante.html` | 6+6+6+1 |
| 4 rampas del notebook = `0.00060`, «2.6 veces mejor» | slide 29 · notebook | 0.000598 |
| soluciones del TODO 4: `0.00039` y `0.00029` | `notas-docente.md` §9 | 0.000392 / 0.000292 |
| TODO 5: sigmoide `0.00066` con suavidad 0,25 (0,05 → `0.00074`; 1 → `0.00052`; 5 → `0.00050`) | notebook · notas §9 | ídem |
| sacar la rampa de 1992 sin reacomodar = 0,29; la de 2017 = 0,0011; reacomodando, la de 1990 = 0,00019 y la de 1999 = 0,00042 | notas §6 y §10 | ídem |
| `for` contra matrices | notebook celda 28 | 6,94e-18 en esta máquina (< 1e-12, que es lo que chequea el `assert`) |
| red `[1,4,1]` = **13** parámetros | notebook · cuestionario 6 | 4+4+4+1 |
| `doble(mas_diez(3))=26`, al revés `16`; TODO 1 da 18 y 13 | slides 8-9 · lego · notebook · notas | ídem |

El tope de altura de `rampas.html` (`MAX_ALTURA = 0.15`) no altera ningún atajo:
el peso más grande que sale de mínimos cuadrados es 0,091 (con 32 rampas).

Los números son deterministas en la misma máquina y con las mismas versiones de
las librerías; con otras versiones pueden cambiar en los últimos decimales (el
6,94e-18 de la celda 28 es el más sensible, y puede dar 0).

---

## 4. Qué se ejecutó en la tercera pasada, y qué no

**Se ejecutó:**
- El notebook entero con `nbconvert --execute` sobre una copia del repo
  (`scratchpad/runs2/02-componer-funciones`): 0 errores, unos 4 s. Salidas
  cotejadas con el texto: 36 años; máximo 2017 (0,1837); mínimo 2000 (0,0211);
  0.00156 / 0.00157 / 0,5 %; `True` en las 5 perillas; 26/16; 18/13; 4 rampas
  0.00060 y «2.6 veces»; 13 parámetros; rampas 0.00060 contra sigmoides 0.00066.
  Los TODO 2, 3 y 4 muestran «✗ todavía no» a propósito. Además se comprobó
  que las soluciones de las notas pasan los chequeos del TODO 4.
- El script de `notas-docente.md` §10, extraído tal cual del Markdown.
- Las 5 viz y las slides en Chrome sin interfaz (`--headless`), con captura de
  pantalla y la consola del navegador. Y una copia de cada viz con un script
  agregado al final que aprieta los atajos y botones y escribe en la consola lo
  que resulta (desajustes de cada atajo, sacar rampas, 15 randomizaciones del
  contador, el mensaje de la bolita con peso de entrada negativo, los
  `aria-label`). Resultados en la §5.

**No se ejecutó:**
- No se probaron las viz a mano con el mouse (arrastrar codos, hover), ni el
  tema oscuro, ni la ventana angosta: eso lo hizo la segunda pasada (§6) y no
  se repitió.
- No se abrieron las URLs de `referencias.md`: siguen `[VERIFICAR URL]`.
- No se corrió en Colab.

**Verificación independiente (después de la tercera pasada).** Se volvió a
correr todo sobre otra copia (`scratchpad/runs3`): notebook sin errores, script
de §10 con la misma salida que la tabla, búsqueda local de 8 codos (200
arranques) que vuelve a dar los codos actuales, JS de las 6 páginas con
`node --check` y Chrome sin interfaz sin errores de consola. Se corrigió una
cosa: con las alturas redondeadas a 4 decimales, poner las óptimas exactas
bajaba el desajuste unas 4 diezmillonésimas y el chequeo del TODO 4 (margen
`1e-7`) lo daba por bueno, contra lo que dice la consigna. El margen pasó a
`1e-6` (hay que ganar en el quinto decimal) y la consigna dice ahora «no vas a
mejorar nada que se note». Con las alturas óptimas exactas: ✗; con la solución
1 de las notas: ✓ y ★ (0.00039).

---

## 5. Resultados del navegador (tercera pasada)

Chrome sin interfaz, abriendo los archivos con `file://` desde la copia del
repo. **0 mensajes de error en la consola** en las 5 viz y en `slides.html`, y
las 6 capturas de pantalla se miraron: todo se dibuja, nada queda cortado en el
ancho de 1280 px.

Lo que devolvieron las copias instrumentadas:

| Viz | Qué se hizo | Resultado |
|---|---|---|
| `rampas.html` | atajos 1, 2, 4, 8 y 32 | 0.0009164, 0.0006477, 0.0003387, 0.0001635, 0.0000076: los mismos del script de Python |
| | 8 rampas, sacar la de 1992 / la de 2017 con la ×, sin reacomodar | 0.29180 / 0.00107 |
| | 8 rampas, sacar la de 1990 y apretar «acomodar» | 0.000192 |
| | tarjetas y aviso de 32 | la tarjeta 1 dice «−0.015/año» y su mini-gráfico tiene `aria-label`; el aviso dice «32 rampas: como red, 97 perillas. (Acá se ajustaron 33 números…)»; el medidor muestra 0.000008 |
| `sin-no-linealidad.html` | abrir y apretar «randomizar» 15 veces | arranca con N = 5 y contador 1/1; después, 16 cadenas y 16 rectas **medidas** (desviación del orden de 1e-15) |
| `red-como-dibujante.html` | configuración buena | desajuste 0.000200 |
| | bolita 5 con peso de entrada positivo / negativo | «sólo puede tocar la curva de ahí en adelante» / «está viva antes del codo: sólo toca la curva de ahí para atrás» |
| | randomizar | desajuste 0.00362; 8 de las 19 flechas punteadas (pesos negativos) |
| `la-recta-imposible.html` | «poner la mejor recta» / raya en el promedio | 0.001561 con «Ya llegaste al piso» / 0.001568 **sin** ese mensaje |
| `lego-de-funciones.html` | intercambiar los bloques | la caja 3 pasa de sacar 16 a sacar 26, y su `aria-label` lo dice |

---

## 6. La segunda pasada (histórica), con correcciones

La segunda pasada encontró y arregló 11 problemas; siguen arreglados. En
resumen: `red-como-dibujante` quedaba vacía al randomizar (ahora se reescala la
salida, y el panel lo dice); tema oscuro guardado con paleta clara; «el
desajuste no baja ni un poquito» al agregar perillas en `la-recta-imposible`
(falso: la recta se mueve, lo que no baja es el piso); «claramente ruido»
pasó a «casi seguro ruido»; la slide 3 no decía que la serie está suavizada;
tres umbrales distintos para el TODO 4; la slide 26 prometía efecto local para
cualquier flecha; numeración de slides corrida en uno después de la pausa; los
dos prácticos duran 17 minutos; dos errores de concordancia; tarjetas de rampa
cortadas.

Lo que esa pasada afirmó y **no era cierto** (corregido acá):
- «Salida idéntica byte a byte» sin red y sin cache: la afirmación correcta es
  que el notebook es determinista en la misma máquina y con las mismas
  versiones.
- «Las 10 citas son correctas»: los datos bibliográficos sí, pero la slide 24
  usaba Cybenko y Hornik como fuente para la **rampa**, y no la cubren.
- «Contador: 16/16 rectas» en `sin-no-linealidad`: el contador era, por
  construcción, igual al de randomizaciones. No medía nada.
- «24 perillas / 96 perillas»: contaba el signo como una perilla (§1, punto 3).
- Los números de su tabla (0.00150, 1,3 %, 0.00014, etc.) estaban bien
  calculados sobre la serie con el error de borde; ya no valen (§3).
- Declaraba abierto el bug de `_shared/js/viz.js` (`botonTema()` no recargaba
  la paleta): ya está arreglado en el archivo compartido, que llama a
  `recargarColores()` y emite `viz:tema`. Las viz de esta clase conservan una
  llamada extra a `Viz.recargarColores()`, inofensiva.

---

## 7. Lo que queda abierto

| # | Qué | Para quién |
|---|---|---|
| 1 | `_shared/css/curso.css` no declara `box-sizing: border-box`. Está parcheado localmente en las 5 viz. | quien mantenga la espina |
| 2 | Las marcas `[VERIFICAR URL]` de `referencias.md` (ahora 10, con Leshno). | quien tenga red |
| 3 | La siembra del sobreajuste (botón «32», slide 31) la cobra la clase 4. Como la serie está suavizada, con 32 rampas la curva se ve prolija, no grotesca: el golpe fuerte es el numérico (97 perillas, 33 ajustados, 36 datos, desajuste 0.000008). | equipo 4 |
| 4 | ~~`recursos/GUIA-DEL-DOCENTE.md` §8 (tabla de siembras) decía «32 rampas → 96 perillas».~~ **[resuelto]**: ahora dice 97 como red (33 ajustados con los codos fijos). | — |
| 5 | El plan de esta clase corre el práctico 2 de 90 a 107 en vez de 85-105 como `PROGRAMA.md`; está declarado en `notas-docente.md` §2. | quien coordine el programa |

---

## 8. Cómo reproducir

```bash
# el notebook (en una copia del repo, no adentro del repo)
python -m jupyter nbconvert --to notebook --execute \
       --output /tmp/out.ipynb clases/02-componer-funciones/notebook.ipynb

# los números de las slides, las notas y las viz (desde la raíz del repo)
python - < <(sed -n '/^```python/,/^```/p' \
              clases/02-componer-funciones/notas-docente.md | sed '1d;$d')
```
