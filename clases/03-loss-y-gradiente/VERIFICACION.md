# Verificación — Clase 3

**«Estar equivocado es un número, y ese número tiene pendiente»** ·
`clases/03-loss-y-gradiente/`

Este archivo tiene dos capas:

- **§0, la revisión de septiembre de 2026.** Es la vigente. Dice qué se corrigió, qué se
  volvió a comprobar y cómo.
- **§1 a §6, la verificación original** (agosto). Se conserva como registro, con notas
  donde algo quedó desactualizado o afirmaba de más. Lo que dice sobre Playwright, `curl` y
  el proxy se hizo en el contenedor donde se construyó el curso y **no se repitió** en esta
  revisión.

**Estado: apta para dictarse**, con lo que queda abierto en §5.

---

## 0. Revisión de septiembre de 2026

### 0.1 Qué se corrigió

| # | Problema | Dónde estaba | Qué se hizo |
|---|---|---|---|
| 1 | «La red de 8 rampas de la clase 2» con **8** perillas y «115 días». La clase 2 cuenta 3 perillas por rampa: son **25** (24 en las rampas + la altura final). | slide 17 y su nota, slide 2, notebook §3, solución 7 | La fila de 8 perillas pasa a ser «una regresión con 7 variables» (115 días, se conserva la muerte en la tercera línea). La red de 8 rampas va en la cuarta fila, con 25 perillas: 10⁵⁰ pruebas, **10²³ edades del universo**. Sale la fila «una red chiquita, 100 perillas» (10¹⁷³). |
| 2 | El learning rate definido como «el tamaño del paso», que choca con «el paso se achica solo». | slides 20, 22, 23, 32, 33; notebook §5 y glosario; cuestionario 8b; viz `valle-de-loss` y `tasa-de-aprendizaje` | Ahora es **el número que multiplica a la pendiente** (paso = lr × pendiente) en todos esos lugares. |
| 3 | Cuestionario 1d («porcentaje mal clasificado») era defendible como correcta. | `cuestionario.md`, soluciones 1 | La d) pasa a ser un distractor claro (sacar casos extremos). La solución explica por qué la exactitud es una métrica y no una loss. La 12c suma el mismo matiz. |
| 4 | «Si sube, aunque sea un poquito, el paso es demasiado grande» no vale con mini-batches. | solución 4, slide 23 y su nota, slide 32, notebook §6 y §8, notas §4.7, viz `tasa` | «Si la **tendencia** sube», con la advertencia del temblor de los mini-batches. La solución 4 suma el tercer resultado (oscila pero converge). |
| 5 | Solución 7a: «la fuerza bruta es más confiable», contra lo que muestra el notebook (grilla 0,0387, descenso 0,0424). | solución 7, notebook §5 | La solución dice que la grilla es tan precisa como fina la hagas. El notebook explica la diferencia: la grilla va de a 0,0076. |
| 6 | Escenario (b): «caso central → MSE» como receta; faltaba media/mediana. | slide 8 y su nota, notebook §1 y TODO 1, referencias 10, solución 11, notas §4.5 | «→ MSE, o mejor: modelalo aparte». Se agrega «MSE = recta de las medias; MAE = recta de las medianas». Se moderó el «literalmente» sobre Lipset y Ragin. |
| 7 | «El MSE se impuso porque tenía solución cerrada» (historia a medias). | nota de slide 8, notas §4.5, referencias 8, comentario de `comparador` | Comodidad de cálculo **y** justificación estadística con errores normales (Gauss, Laplace). |
| 8 | El cero de 2002, presentado como «el caso que más tironea» la recta. Con los datos del comparador, el que más pesa es 1998. Además, el léxico de seguridad tiene 24 palabras, no 23. | notas §6 | «Uno de los casos que más tironean»; se nombra 1998; 24 palabras. |
| 9 | La redondez del valle atribuida sólo a «centrar»; el orden de las operaciones, al revés. | notebook §1, TODO 2 y la última sección | Centrar **y** pasar a décadas («casi estandarizar»); primero se resta y después se divide. |
| 10 | «Con MÁS pasos se estaciona»: ya se estaciona en el paso 37, dentro de los 40. | notebook TODO 3 y la nota que sigue | «Ya dejó de crecer antes del paso 40». |
| 11 | `loss-1d`: la viz usa la resta hacia adelante, pero el rótulo decía «entre los dos puntos» y la nota describía la centrada. Con h = 0,005 el panel seguía diciendo «achicalo». | viz `loss-1d`, slide 19 y su nota, notebook §4 | Rótulo y pie: «el atajo hasta el pasito de la derecha». La nota de la slide y la docstring del notebook explican las dos restas. El umbral de «prácticamente exacta» pasa a 0,01: con h = 0,005 el error es 0,0054. |
| 12 | `tasa-de-aprendizaje`: el «chiquito» por defecto (0,005) bajaba el 72 % del camino en 60 pasos y no era «una raya». | viz | Por defecto 0,0005 (baja el 12 %). En el quiz, C pasa de 0,004 a 0,0004. Texto: «le faltarían miles» (≈4.000 pasos para quedar a 2 % del fondo). |
| 13 | «El 95 % de los papers», «el 99 % de los papers»: cifras inventadas. | slides 5 y 30 (nota) | «El nombre que más vas a leer»; «casi cualquier paper». |
| 14 | «Cargó 15 donde iba 1,5». | slide 8 | «Cargó 1,5 donde iba 0,15», en línea con el notebook. |
| 15 | MAE: «trata a todos los errores igual de mal». | notebook §1 (docstring) | «Cada caso empuja con la misma fuerza». |
| 16 | «En 2001 valían»: x = 0 es 2001,5. | notebook §2, slide 13, viz `valle` | «A mitad de la serie (entre 2001 y 2002)». |
| 17 | Los `revisar()` de los TODO 2 a 5 aprobaban solos. | notebook | Cada TODO pide completar algo: `zoom_a`/`zoom_b`/`forma_del_valle`, `signo_de_a`, `llego`/`iteraciones_estimadas`, `a0_lejos`/`b0_lejos`/`pasos_lejos`. Con `None` o `""`, la celda dice ✱ y explica qué falta. Las respuestas modelo están en un anexo de `cuestionario-soluciones.md`. |
| 18 | El bloque `[EL LUNES]` y los plazos por día o por semana. | slide 31 (reveal), notebook §8, notas §2, referencias | `[EN TU INVESTIGACIÓN]`, «Qué te llevás a tu investigación», «En tu propia investigación, desde ya». Los plazos se dicen por número de clase. El cuestionario y el TODO 4 se hacen «antes de la clase 4». |
| 19 | Dos versiones de la pausa: las notas del orador ponían la niebla a los 58-60 y `loss-1d` a los 60-64. | notas del orador, slides 16-19 | Se alinearon con `notas-docente.md` §2: 54 / 55 / 56 / 57-60, pausa 60-70 (ahora con su nota), y se aclaró la numeración. |
| 20 | Referencias internas: «slide 25» por la 26, «celda 3» por la sección 3, «tres palabras» contra «dos palabras», «tarda dos segundos» contra lo que se mide. | slides 17, 29, 36 y JS | Corregidas. En la clase 4 son cinco líneas de PyTorch, y el gradiente son dos palabras, `loss.backward()`. |
| 21 | «Lock-in, la analogía es exacta» contra el glosario, que dice que los mínimos locales casi nunca son el problema. | slide 29, notas §7 | Las dos cosas juntas: exacta como mecanismo, no como frecuencia. |
| 22 | Accesibilidad: canvas sin `aria-label`; en el gancho, azul y naranja se distinguían sólo por el color. | slides y las 4 viz | Todos los canvas tienen `role="img"` y `aria-label` (14 en las slides, 1 + 7 + 3 + 3 en las viz). La recta del MAE es punteada, en el gancho, en el comparador y en su leyenda. Las rectas se rotulan «A · azul» y «B · naranja». El rastro de la muestra en «censo o muestra» también es punteado. |
| 23 | La muestra de la slide «censo o muestra» se sacaba **con** reposición; en el notebook, **sin**. | JS de slides | Sin reposición, como en el notebook. |
| 24 | `en_castellano()` decía «menos de 6 segundos» para 10⁻⁵ s y 0,1 s. | notebook §3 | «Menos de un parpadeo» y «0,1 segundos», como la tabla de la slide 17. |
| 25 | El zigzag de la zanja se afirmaba pero no se veía. | notebook, última sección | Se suelta la pelota en la zanja (lr = 2,3·10⁻⁷, apenas debajo del máximo, 2,5·10⁻⁷). Rebota de pared a pared, se acomoda en el piso y en 1000 pasos `b` se mueve 0,000003, con el fondo en b ≈ −8,3. |

**Lo que no se tocó a propósito:** la celda de bootstrap de Colab (la mantiene la base del
curso). Tampoco los números de C3, que **no dependen** del arreglo de la media móvil en
`_shared/ssdl/datos.py`: la clase usa la serie **cruda** de seguridad (sin suavizar).
Verificado: los arrays de `slides.html` y de las viz coinciden con
`serie_menciones("seguridad", 1984, 2019)` de la versión corregida, con diferencia máxima 0,0.

### 0.2 Qué se volvió a comprobar, y cómo

| Chequeo | Resultado |
|---|---|
| `nbformat.validate` | válido, 40 celdas; celda de bootstrap idéntica a la de la base (md5 del source `4c9c6d9d…`) |
| `nbconvert --execute` en una copia del repo, notebook tal como se entrega (TODO sin completar) | 0 errores, ~3,6 s de reloj. Los TODO 2 a 5 dicen ✱ y explican qué falta; nada explota |
| Lo mismo con los TODO completados con las respuestas modelo | 0 errores; todos los `revisar()` dan ✔ |
| Números del notebook | MSE 4,0× y MAE 1,4× con el caso extremo; 75 % del MSE; grilla a = 0,0387, b = 0,1534 (paso de la grilla 0,0076); descenso a = 0,0424, b = 0,1549, loss 0,014547; lr = 1,5: 2,67e+25, congelado desde el paso 37; lr = 1e-6: regla de tres ≈ 237.000, cuenta exacta ≈ 1,5 millones para quedar a 2 % del fondo; desde (−5; 50) en 400 pasos llega a (0,0424; 0,1549) |
| El notebook se guarda sin salidas | sí: `outputs` vacíos y `execution_count` null en las 21 celdas de código |
| JS de `slides.html` y de las 4 viz | `node --check` sin errores de sintaxis |
| Slides en Chrome headless (1280×800, CDP), por `file://` a la profundidad real | 0 errores de consola; **las 36 slides entran** en los 760 px de reveal (la más alta: 760, la pausa); screenshots de las slides 3, 8 y 17 revisados |
| Las 4 viz en Chrome headless | 0 errores de consola. `loss-1d` con h = 0,005 dice «prácticamente la respuesta exacta». En el quiz de `tasa`, A llega a 0,0145, B explota y C queda en 0,183. `comparador`, al plantar el caso: 47 %, azul 0,092 contra naranja 0,011 |
| Cuentas aparte (numpy) | 25 perillas → 10⁵⁰ pruebas → 10⁴¹ s → 10^23,4 edades del universo. «Chiquito» 0,0005: baja el 12 % en 60 pasos (0,005 bajaba el 72 %). Error de la resta de un lado = 1,079·h |

**No se repitió:** el recorrido con Playwright de los paneles embebidos (recortes de §5.1 y
§5.2), el tema oscuro, la ventana angosta y los `curl` de §4. Las viz se abrieron sueltas,
no adentro del iframe de la slide.

Números: el notebook es **determinista en la misma máquina y con las mismas versiones de
las librerías** (semilla 1983). Con otras versiones algún decimal puede cambiar.

---

## 1. Chequeo mecánico (verificación original, agosto)

| Chequeo | Resultado |
|---|---|
| Los 6 entregables existen y están completos | sí (slides, notebook, 4 viz, notas, cuestionario + soluciones, referencias) |
| `nbformat.validate` | **válido**, 40 celdas |
| `nbconvert --to notebook --execute` | **0 errores**, 8 figuras · 3 corridas: 8,97 s / 9,47 s / 9,04 s en aquel contenedor (en la revisión de septiembre, en otra máquina: ~3,6 s; la revisión anterior midió ~20 s con la caché de fuentes de matplotlib vacía) |
| El notebook **sin red** (`HTTPS_PROXY` a un puerto muerto) | **0 errores**, mismos 36 años y mismos números |
| Consola del navegador · slides + las 4 viz **en su ubicación real** | **0 errores** (las 36 slides recorridas una por una) |
| Requests externas (`context.route` abortando `http(s)`) | **0** en los 5 archivos |
| KaTeX | renderiza desde `_shared/vendor`, verificado **por screenshot** (slide 6, MSE y MAE) |
| Los 5 `<iframe>` de viz cargan adentro de las slides | sí, verificado por screenshot de cada una |
| Tema oscuro (`prefers-color-scheme: dark`) | slides y las 4 viz, sin errores y legibles |
| Ventana angosta (900×640) | la slide 14 sigue entera |
| Ninguna slide se pasa del alto del canvas de reveal (760 px) | **0 de 36** (vuelto a medir en septiembre, ver §0.2) |

---

## 2. Chequeo de rigor: cada número, rehecho aparte

Todos se recalcularon con numpy/scipy sobre `ssdl.datos.serie_menciones("seguridad", 1984, 2019)`,
sin usar el código de la clase.

| Número que aparece | Dónde | Comprobado |
|---|---|---|
| la serie (36 años, 1984-2019) | slides, notebook y las 4 viz | los arrays de `slides.html`, `valle-de-loss.html` y `comparador-de-losses.html` coinciden con `serie_menciones` **con diferencia máxima 0,0** (vuelto a comprobar en septiembre, con el `datos.py` corregido) |
| 0,0146 / 0,0152 / 0,0880 / 0,0921 | slide 4 | recta MSE-óptima (0,042427; 0,154908) → MSE 0,014547 · MAE 0,092050. Recta MAE-óptima (0,061261; 0,138093) → MAE 0,087966 · MSE 0,015213. **Los cuatro, exactos** |
| 0,033 vs 0,092 puntos por década | `comparador-de-losses` | subconjunto de 15 años: 0,0328 y 0,0925. **Exacto** |
| 20 % / 17 % (peso del año 1998) | `comparador-de-losses` | 20 % y 17 %. **Exacto** |
| 47 % del MSE, tras plantar el caso extremo | viz + slide 7 + solución 3 | 47 %. **Exacto** (con la recta reajustada; el 75 % del notebook es con la recta fija) |
| «la azul se mueve N veces más» | `comparador-de-losses` | 0,092 contra 0,011 → **8,4×** |
| 4,0× (MSE) contra 1,4× (MAE), y 75 % del MSE | notebook + solución 3 | salida real del notebook |
| 0,014547 (el fondo del valle) | notebook, slides, viz | `lstsq` da 0,0145471504. **Exacto** |
| 115 días para 10¹⁶ pruebas | slide 17 + notebook | 10¹⁶/10⁹ = 10⁷ s = 115,7 días. Ahora rotulado como **8 perillas, una regresión con 7 variables** (antes decía, mal, «la red de 8 rampas») |
| 10²³ edades del universo (red de 8 rampas, 25 perillas) y 10⁸⁰ átomos | slide 17 + notebook | 10⁵⁰/10⁹ = 10⁴¹ s; 10⁴¹/10^17,64 = 10^23,4. Consistente con los mismos supuestos |
| 0,93 = el lr más grande que todavía converge | pie de `tasa-de-aprendizaje` | Hessiano = 2·diag(⟨x²⟩, 1) con ⟨x²⟩ = 1,07917 → 2/λmax = **0,9267** |
| loss = 2,67e+25 «y se congela» | notebook, notas §4.10 | se estaciona **desde el paso 37**, dentro de los 40 que corre la celda (la versión original decía «~40» y el notebook «con más pasos») |
| 0,106 y 0,065 (los dos pozos) | notas §4.3 | mínimos locales del paisaje inventado: **0,10581** y **0,06503** |
| la resta contra la exacta, con h = 0,005 | `loss-1d`, slide 19 | −0,6905 contra −0,6959: el error (0,0054 ≈ 1,08·h) es el de la resta de un solo lado. Antes chocaba con el umbral de 0,005 y el panel decía «achicalo»; ahora el umbral es 0,01 |
| pendiente +0,0042 puntos **por año** | `datos/README.md` | 0,042427 por década = 0,00424 por año. **Coherente** |

La versión original decía «no se encontró ningún número inventado». **Afirmaba de más:**
«el 95 % de los papers» (slide 5) y «el 99 % de los papers» (nota de la slide 30) eran
cifras sin fuente, y la fila de «8 rampas = 8 perillas» contradecía a la clase 2. Las tres
se corrigieron (§0.1, ítems 1 y 13).

---

## 3. Los 17 problemas que se encontraron y se arreglaron en agosto

Se conservan como registro; siguen arreglados salvo donde se indica.

### Graves (se ven en el aula)

1. **La tabla de la fuerza bruta mentía en pantalla.** `reset.css` de reveal aplana `sup` y
   `sub`, y `10<sup>16</sup>` se leía «1016». *Arreglado* con una regla `.reveal sup/sub`
   que hoy está en `_shared/css/curso.css` (ya no en el `<style>` de la slide).
2. **«Soltar la pelota» no hacía nada la segunda vez** (`Viz.animacion` no reinicia su
   contador). *Arreglado* con un contador propio (`pasosDados`).
3. **«Soltar las tres» tampoco animaba la segunda vez.** *Arreglado:* `estado.hasta += 1`.
4. **Los botones de la animación quedaban fuera de pantalla en las slides 14 y 22.**
   *Arreglado* reordenando y compactando el panel embebido.

### Rigor y coherencia

5. Cita del aula «en el paso cuatro ya tenía nueve dígitos» → paso **trece**.
6. «Una recta con 2 variables → 4 perillas» → «una regresión con 3 variables».
7. `notas-docente.md` §5 mandaba recortar la slide 29 (la honestidad) en vez de la 30.
8. Dos filas en «0:60» en el plan de tiempos. *Nota de septiembre:* las notas del orador
   seguían con otro reparto (niebla 58-60, `loss-1d` 60-64); se alinearon (§0.1, ítem 19).
9. `loss-1d` decía «andá a la derecha» en el fondo, por redondeo → ahora «llegaste al fondo».
10. «La azul se mueve unas cinco veces más» → los dos números reales (0,092 y 0,011).
11. «La flecha negra» (blanca en tema oscuro) → «la flecha gruesa».
12. «Tres palabras» contra «dos palabras». *Nota de septiembre:* la nota de la última slide
    seguía diciendo «tres palabras»; ahora dice cinco líneas de PyTorch y
    `loss.backward()`, en las slides y en el notebook.
13. El título de la grilla de la slide 16 decía diez mil rectas sobre una grilla de 40×26.

### Legibilidad

14. La flecha roja del gradiente (slide 21) era corta sobre fondo naranja → más larga.
15. «Volver arriba» en `valle-de-loss` respeta el paisaje activo.
16. El pie de la slide 23 avisa que el quiz se scrollea.
17. Seis slides se pasaban del alto de reveal → ajustadas.

---

## 4. Lo que se revisó y estaba bien (agosto, con notas de septiembre)

- **Coherencia con la spec.** 34 bloques del guion, más la pausa y «qué te llevás»: 36
  secciones.
- **Presupuesto de tiempo.** `notas-docente.md` §2 suma 120 minutos. *Septiembre:* la
  tabla estaba bien; las notas del orador no coincidían con ella en el tramo 54-70, y ahora
  sí.
- **Puentes.** Hacia atrás: slide 2 (`[CALLBACK DIBUJO]`, las perillas a mano de la clase 2)
  y slide 17 (la red de 8 rampas, ahora con sus 25 perillas). Hacia adelante: slide 24 (los
  síntomas → clase 4), slide 28 (`loss.backward()`), slide 36 y el cierre del notebook.
- **Tono.** Voseo, humor, sin «no se asusten».
- **Cuestionario.** Las 12 preguntas se contestan con lo que se da en clase. *Septiembre:*
  la versión original afirmaba que «las soluciones son correctas». **No lo eran del todo:**
  la 1d era defendible como correcta, la 4 daba una regla que falla con mini-batches y la
  7a contradecía al notebook. Están corregidas (§0.1, ítems 3 a 5).
- **Las 4 viz, control por control** (agosto, con Playwright): arrastre, plantar y volver,
  los tres learning rates, el quiz de firmas, el pasito de prueba, los dos paisajes, «se fue
  del mapa». *Septiembre:* se volvió a abrir cada viz en Chrome headless y se ejercitaron
  los controles citados en §0.2, no todos.
- **Figuras del notebook.** Ejes rotulados, leyendas, barra de color. La celda de las tres
  firmas avisa «ojo: otra escala».
- **URLs.** Las de `referencias.md` quedaron como estaban: dos `[VERIFICADA]` y el resto
  `[VERIFICAR URL]`. No se volvieron a probar.

---

## 5. Lo que queda abierto

| # | Qué | Gravedad | Para quién |
|---|---|---|---|
| 1 | En la slide 23, el **quiz de firmas** de `tasa-de-aprendizaje` queda abajo del pliegue del panel embebido (se scrollea, y el pie lo avisa). Suelto se ve entero. | cosmética | quien la dé: para el quiz en vivo, abrir la viz suelta |
| 2 | En las slides 14 y 22, el último cartel del panel de `valle-de-loss` queda cortado en el marco embebido (medido en agosto; no se volvió a medir). | cosmética | idem |
| 3 | Espacio vacío abajo a la izquierda de los marcos embebidos. | cosmética | quien retoque |
| 4 | Marcas `[VERIFICAR URL]` / `[VERIFICAR]` en `referencias.md` (3Blue1Brown, Distill, arXiv, deeplearningbook, las fechas 1805/1809). | abierta a propósito | quien tenga red |
| 5 | ~~Falta `set_aspect("equal")` en el panel del medio de la figura del descenso.~~ **Ya estaba resuelto:** la celda tiene `set_aspect("equal")`. | — | — |
| 6 | El quiz de firmas **nunca se probó con un aula real**. Con el «chiquito» en 0,0004, C es una raya casi plana y alta; si resulta trivial, agregar un cuarto caso ambiguo. | menor | quien la dé primero |
| 7 | El cierre (110-120 min, 11 slides) es el tramo más apretado. **Hay que medirlo en un aula.** | menor | quien la dé primero |
| 8 | Siembras que hay que cobrar en la clase 4: la slide 24 («los síntomas», ahora con «si la tendencia sube») y las cinco líneas de PyTorch con `loss.backward()`. | coordinación | equipo de la clase 4 |
| 9 | ~~La regla `.reveal sup/sub` quedó local.~~ **Ya está en `_shared/css/curso.css`.** | — | — |
| 10 | Los TODO 2 a 5 ahora exigen completar variables. No se probó con estudiantes si la consigna del TODO 4 (`llego`, `iteraciones_estimadas`: correr, contestar y volver a correr) se entiende sin ayuda. | menor | quien la dé primero |
| 11 | La celda de bootstrap apunta a la rama `main` de `github.com/johannperez/dlss`. Funciona en Colab sólo si estos arreglos están en `main` y el repo es público; si no, hay que subir el .zip (ver `recursos/setup.md`). | infraestructura | base del curso |

---

## 6. Cómo reproducir

```bash
export PYTHONDONTWRITEBYTECODE=1
# siempre sobre una COPIA del repo, nunca adentro del repo
cp -R dlss /tmp/copia && cd /tmp/copia/clases/03-loss-y-gradiente
python -c "import nbformat;nbformat.validate(nbformat.read('notebook.ipynb',as_version=4))"
python -m nbconvert --to notebook --execute --output /tmp/out.ipynb notebook.ipynb
```

Para el HTML (septiembre): Chrome headless con `--remote-debugging-port` y un script de
Node 22 que habla CDP (`Runtime.evaluate`): abrir `slides.html` por `file://`, recorrer las
36 slides con `Reveal.slide(i, 0)`, comparar `section.present.scrollHeight` con
`Reveal.getConfig().height` y juntar los errores de consola. Las viz se abren sueltas y se
leen sus paneles con `document.body.innerText`.
