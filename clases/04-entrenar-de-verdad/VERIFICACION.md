# Verificación adversarial — Clase 4

**El ciclo de entrenamiento, y la diferencia entre dibujar y calcar**
Segunda pasada, hecha por un equipo distinto del que la construyó, con la consigna
de no creerle nada al informe anterior. Todo lo que dice acá se comprobó **corriendo**:
`nbconvert --execute`, `nbformat.validate`, Chromium por Playwright con `context.route`
abortando cualquier `http(s)`, `curl` contra cada URL, `md5sum` sobre los archivos del
corpus, y **mirando los PNG con los ojos** (48 capturas de slides, 14 de las viz,
6 figuras del notebook).

---

## 0. Tercera pasada (2026-09-29): los arreglos de la revisión

La revisión de septiembre de 2026 encontró afirmaciones que este mismo informe daba por
buenas y no lo eran. Se corrigieron en el material y **también acá**: las secciones 1 a 6
quedan como registro de la segunda pasada, con las correcciones marcadas **[corregido]**.

**Qué se cambió, en una línea cada cosa:**

- «La loss de entrenamiento **siempre** baja con más capacidad» → **tiende** a bajar (no sube
  de forma sistemática). Medido: con torch 2.14 el TODO 2 da 64 → 0.00612 y 256 → 0.00628. El
  notebook ahora lee los números y dice «baja / casi igual / SUBE» en vez de imprimir «Mejora.
  Mejora. Mejora.»; la slide 24 cambió las opciones (B = «tiende a bajar, hasta quedar cerca
  de cero»); la slide 38, el cierre del notebook y las notas, igual.
- `viz/sobreajuste.html`: los codos ahora están **anidados** (van der Corput), así que cada
  modelo contiene al anterior. Antes (codos en j/(K+1)) la curva azul subía 25 veces entre K=1
  y 60, con saltos de hasta 0.0012; ahora sube a lo sumo en el quinto decimal (2·10⁻⁵, por la
  regularización). La cifra «perillas / casos» (K+2) pasó a «números ajustados / casos», con
  la aclaración de que es una red con los codos clavados (con codos libres serían 3K+1). La
  curva naranja va punteada (antes sólo el color la distinguía).
- `viz/particion.html`: la partición por grupo dejaba el **test vacío** en 51 de 200 sorteos y
  lo declaraba «un test de verdad». Ahora el último grupo del sorteo va siempre a test (y el
  anteúltimo a validación si hace falta): en 500 sorteos el test tiene 2, 4, 6, 8 o 10
  discursos, nunca 0. Hay además un cartel para test vacío (se llega con los sliders), una
  letra E/V/T en cada cuadradito (el montón no se dice sólo con color), el checkbox se llama
  «agrupar por presidente o diario», y «por tiempo» explica por qué con 60/20/20 los gemelos
  quedan partidos y en el notebook (corte 2008/2014) no.
- `viz/anatomia-del-loop.html`: el eje de la loss se agranda cuando la loss sube (con lr arriba
  de ~0.68, el umbral 2/λ_máx de estos 8 puntos) y un cartel lo dice; el slider se llama
  «learning rate», «el número que multiplica a la pendiente».
- La escena de la fuga (sección 6) estaba contada como si el modelo leyera el texto. Sólo ve
  el año. Ahora el notebook lo dice, mide la predicción para 2005 (0.137 contra 0.1645 real,
  error² 0.0008: cerca, no perfecto) y agrega una celda con un «vecino más parecido» por perfil
  de temas, que encuentra a 2006 a distancia 0 y acierta con error cero: la fuga con un modelo
  de texto.
- Validez interna/externa → «ajuste perfecto dentro de la muestra y capacidad predictiva nula
  fuera de ella» (slide 22, notas, soluciones 3b). «No existe un test estadístico» → AIC, BIC y
  validación cruzada nombrados (slide 23, notebook §5).
- Autograd: «misma cuenta» → «mismo resultado, otra cuenta» (la resta mide, la regla de la
  cadena calcula). Adam: adapta el paso de cada perilla, igual necesita lr; se sacó el «90 %».
  Tensor: se acuerda de las cuentas «si se lo pedís». Sin `zero_grad`: oscila, no «pasos
  enormes»; hay una celda opcional nueva que lo muestra.
- `medir-figuras.py` calcula también 256 rampas (`cap256`), el TODO 4 y la sección 6 (`fuga`),
  y guarda las versiones (`versiones`). Las slides 19 y 35 leen esos números en vez de tenerlos
  escritos a mano (el 0.00509 de 256 estaba fijo en el HTML).
- Accesibilidad: los 7 canvas de las slides y los 5 de las viz tienen `role="img"` y un
  `aria-label` que dice en palabras lo que dibujan (en las viz se actualiza con los controles).
- Calendario: «[EL LUNES]» → «en tu investigación»; las tres preguntas del cierre y la pregunta
  13 del cuestionario tienen el mismo plazo (la clase 5). Los tiempos se rehicieron: el cierre
  tenía 2 minutos y ahora tiene 6 (114-120); el práctico 2 tiene 12 y el experimento de a dos
  se termina antes de la clase 5.
- Cuestionario: el gráfico ASCII del ítem 3 se rehízo con los datos de la corrida (el ▼ cae en
  la época 42, el recorte del eje está declarado y la frase del colega usa 0.36 → 0.006).
  Soluciones: 6D (el ruido no explica la brecha), 8b-c (oscila), 4-IV (la cita es de la slide
  20, no del notebook), 11a (`meses` numérico).
- Números de otras clases: el pie de la slide 21 usa los de la clase 2 después del arreglo del
  borde de la media móvil (32 rampas 0.0000076 contra 0.001561 de la recta; 97 perillas, 3 por
  rampa más el sesgo final).

**Qué se verificó en esta pasada, y cómo:**

| Chequeo | Resultado |
|---|---|
| `nbconvert --execute` sobre una copia del repo | **0 errores**, 51 celdas, 7 figuras, ~7 s en la máquina de la revisión (Python 3.12.13, torch 2.14.0, numpy 2.5.3) |
| Notebook guardado | sin salidas, `execution_count` nulo; la celda de bootstrap no se tocó |
| `medir-figuras.py` | regenerado con torch 2.14.0; coincide con lo que imprime el notebook en esa misma máquina |
| Slides en Chrome headless (1280×760, todos los fragmentos abiertos) | 0 errores de JS; ninguna slide pasa de 745 px de contenido (las más altas, 25, 28 y 34, con iframe); los 7 canvas con `aria-label` |
| Las 3 viz en Chrome headless, manejadas por script | 0 errores de JS; anatomía con lr 0.3 converge a a=0.0775, b=0.1970, MSE 0.00884; con lr 1.0 el eje sube y aparece el cartel; sobreajuste y partición dan los números de la tabla de arriba |
| Lógica de las viz en node (sobreajuste, partición) | ver los números de arriba |
| Re-verificación independiente (otra copia del repo, mismas versiones) | notebook: 0 errores, mismos números impresos; `medir-figuras.py` reproduce `datos-figuras.js` idéntico; sobreajuste: 13 subidas de la azul, la mayor de 2·10⁻⁵, mejor K = 8; partición por grupo en 500 sorteos: test de 2, 4, 6, 8 o 10 discursos (24/8/4 con la semilla 2019). La tijera de `datos-figuras.js` guarda una época de cada cinco: su último punto es la 1496 (val 0.02239), no la 1500 que imprime el notebook (0.02247) |

**Lo que NO se verificó en esta pasada:** el tema oscuro, la ventana angosta, el notebook en
Colab, las URLs de `referencias.md` y una recorrida visual completa de las 40 slides (se
miraron dos capturas: la 20 y la 24).

---

## 1. Veredicto

**Apta para dictarse.** Se encontraron **11 problemas** y se arreglaron **11**.
Ninguno era una bomba, pero dos habrían dado vergüenza en el aula (texto tapado en
tres slides con viz embebida) y dos eran errores de **rigor** — que en esta clase,
que trata justamente de no mentir con números, pesan más que en cualquier otra.

| Chequeo | Resultado |
|---|---|
| Los 6 entregables + extras | **11 archivos**, ninguno vacío ni a medias |
| `nbconvert --execute` | **0 errores**, 46 celdas, 6 figuras (hoy: 51 celdas, 7 figuras, ver §0) |
| Tiempo del notebook (mediana de 3 corridas, CPU) | **28,9 s** (28,6 / 28,9 / 29,5) |
| `nbformat.validate` | válido |
| ¿El notebook necesita red? | **No.** `ssdl.datos` lee sólo `datos/muestras/`, nunca `datos/cache/`. Verificado leyendo `datos.py`: las 36 observaciones salen del CSV versionado |
| Consola del navegador (slides + 3 viz, en su ruta real) | **0 errores, 0 pageerrors** |
| Requests externas (todo `http(s)` abortado) | **0** |
| Desborde de slides (48 estados, con fragmentos abiertos) | **0** después de los arreglos (había 0 antes, y 2 que introduje yo y corregí) |
| Tema oscuro, las 3 viz | 0 errores, legible |
| Proyector 1280×720 y ventana angosta 1024×640 | bien en las dos |
| Código de las slides = código del notebook | **idéntico** (7 bloques comparados uno por uno) |
| Números de las slides = corrida real | **todos**, ver §3 — **[corregido]** en la misma versión de torch; con otra, el TODO 2 y el calco cambiaban (ver §3) |
| `medir-figuras.py` reproducible | ~~vuelve a escribir un `datos-figuras.js` byte por byte idéntico~~ **[corregido]**: determinista en la misma máquina y con las mismas versiones. Con torch 2.14 cambiaron el 64 del TODO 2 (0.00584 → 0.00612), el calco (0.000805 → 0.000613; 0.00753 → 0.00807) y la red sana (0.00496 → 0.00472). Ahora el archivo guarda las versiones |
| URLs de `referencias.md` | 2 responden (200) y están marcadas `[VERIFICADA]`; 5 no responden y están marcadas `[VERIFICAR URL]`. Ninguna cita inventada |
| Presupuesto de tiempo | 0-120, continuo, sin huecos ni solapes |

KaTeX carga sin error, pero **la clase no tiene ni una fórmula**: no había nada que
renderizar. Es deliberado y está bien para esta audiencia (la intuición alcanza y
sobra acá). Se deja el vendor cargado por consistencia con las otras nueve.

---

## 2. Lo que se arregló

### Grave — se veía en el aula

**1. El texto de las tres viz embebidas quedaba cortado.**
`_shared/css/curso.css` **no declara `box-sizing: border-box` en ninguna parte**, y
`reveal/reset.css` tampoco. Como `.viz-frame` lleva `width: 100%` **más** su padding
**más** su borde, cada recuadro se le iba ~26 px por la derecha a su columna del grid
y se montaba encima del panel de controles. Suelta la página casi no se nota; embebida
en una slide (donde el panel mide 268 px y no 300) el dibujo le comía la primera letra
a cada rótulo: se leía **«L CICLO»**, **«L TAMAÑO DEL PASO»**, **«OS DATOS»**.
Medido en el navegador: la caja de números terminaba en x=1019 y el panel empezaba en
x=1004.
*Arreglado* con `.viz-frame, .panel { box-sizing: border-box; }` en el `<style>` local
de las tres viz, con el comentario explicando por qué. **Es un defecto de la base y
conviene subirlo a `curso.css`** (ver §5).

**2. `viz/particion.html` decía «tu test no es un test» cuando el test estaba limpio.**
Con la estrategia **por tiempo**, 2005 cae en entrenamiento y 2006 en validación: el
par idéntico cruza, pero **no toca el test**. El veredicto sólo tenía dos estados y
tiraba igual el cartel rojo «⚠ Hay fuga. Tu test no es un test», que es **falso** — y
encima contradice al notebook, que dice que la partición por tiempo deja el test limpio.
Un estudiante atento se lleva la idea de que partir por tiempo no sirve.
*Arreglado:* tres estados. Verde = sin fugas · **naranja = «el test está limpio; la que
se ensució es la validación»**, explicando que eso contamina la *decisión* y no el
número que reportás · rojo = fuga de verdad en el test. Comprobado a mano en las tres
estrategias y en los dos datasets.

### Rigor — números y afirmaciones

**3. El «2,2 veces mejor» estaba contado como si todo fuera la fuga.**
Los dos test **no son el mismo conjunto de años**: el honesto es 2014-2019, un tramo
más difícil, y se ve en que **hasta el baseline tonto empeora** (0.0133 → 0.0255).
Contra su propio baseline, la red al azar queda en 1,07 y la honesta en 1,25.
Atribuirle el factor 2,2 entero a la fuga es enseñar algo que después hay que desaprender.
*Arreglado* en los tres lugares: el notebook ahora **imprime** los dos cocientes contra
su propio baseline, la celda de markdown que sigue lo explica, la slide 35 lo dice en
una línea y las notas del docente traen la respuesta larga por si alguien pregunta.
La formulación que queda: *«la fuga garantiza la dirección, no el tamaño: el 0.0142 está
inflado y no hay manera de medir cuánto — y esa imposibilidad es el problema».*

**4. La tarjeta del baseline en la slide 35 no decía de qué partición era.**
Mostraba `0.0142 · 0.0319 · 0.0255` con el tercero rotulado «el baseline tonto», sin
más. Leído de izquierda a derecha da a entender que la red al azar (0.0142) le gana al
baseline (0.0255), cuando el baseline de *esa* partición es 0.0133 y **tampoco le gana**.
*Arreglado:* el rótulo ahora dice «el baseline tonto **en la partición honesta**».

**5. Un número construido que no estaba declarado.**
`medir-figuras.py` fija a mano `a_ojo, b_ojo = 0.02, 0.22` para la línea «a ojo, con dos
sliders (clase 1)» de la slide 18 (MSE 0.0195). El MSE sí se mide sobre los datos reales,
pero **los dos parámetros están elegidos a dedo** y `referencias.md` declaraba como único
número construido el del gancho.
*Arreglado:* declarado en `referencias.md`, comentado en `medir-figuras.py` y corregido
el docstring del script, que empezaba diciendo «ninguna figura está dibujada a ojo».

**6. Error numérico en las soluciones del cuestionario.**
El ítem 3.c decía que sobre datos nuevos el modelo pasó de **«~0.018 (época 42)»** a
~0.022. El mínimo real de validación en la época 42 es **0.01331** (medido, y es el mismo
número que imprime el notebook y que dibuja la slide 26).
*Arreglado:* «de **0.0133** (época 42) a **0.0225** (época 1500)». Se agregó también el
valor al pie del gráfico ASCII del enunciado, para que enunciado y solución coincidan.

### Pedagógicos

**7. La siembra de la clase 2 estaba sin cobrar.**
La espec (§1, punto 4) y `GUIA-CONSTRUCCION.md` §6 son explícitas: el botón **«32 rampas»**
de `clases/02-componer-funciones/viz/rampas.html` se cobra en la clase 4, y la clase 2
cerró prometiéndolo por escrito («guardá esa imagen, en la clase 4 va a tener nombre»).
En las 40 slides no aparecía por ningún lado.
*Arreglado:* pie nuevo en la **slide 21**, con los números que midió el equipo de la clase 2
(32 rampas → MSE **0.0000076** sobre 36 puntos, contra 0.001561 de la mejor recta) y el cierre
«el nombre es *overfitting*». En las notas del docente va además el aviso que dejó ese equipo
en su propia verificación: **la serie de la clase 2 está suavizada, así que la imagen de 32
rampas se ve prolija, no grotesca — hay que cobrarla con los números (97 perillas para 36
datos), no con la foto.**

**8. La semántica de color rota en la slide 18.**
El «ajuste a ojo de la clase 1» se dibujaba en **gris punteado**, que en las tres capas del
curso (`curso.css` = `viz.js` = `graficos.py`) significa **la verdad subyacente** — y acá los
datos son **reales**, así que verdad no hay. Y «la mejor recta posible» iba en **violeta**,
que es el color de las **perillas**. Diez clases enseñando un código de color y esta lo
contradecía dos veces en la misma figura.
*Arreglado:* las tres líneas son cosas que un modelo dibuja → azul (`modelo`), la mejor recta
punteada y más finita; el ajuste humano en gris neutro (`tinta3`), que no es un token con
significado técnico. Comentado en el archivo para que no vuelva.

**9. El sorteo por defecto de `viz/particion.html` no era el que cuenta la clase.**
Con la semilla 1983 el sorteo mandaba 2005 a entrenamiento y 2006 a **validación**: el caso
flojo, y **distinto del que dicen el notebook y la slide 35** («2005 cayó en test y 2006 en
entrenamiento»). La escena central de la clase mostraba una cosa en la slide y otra en la viz.
*Arreglado:* semilla **2019** (buscada por barrido, con el motivo escrito en el archivo).
Ahora el sorteo por defecto reproduce exactamente la escena del notebook: **2005 en test,
2006 en entrenamiento**, 7 de 7 casos del test con fuga de presidente, 6 presidentes cruzados.
El botón «otro sorteo» sigue funcionando igual.

### Menores

**10. Slide 37 («Glosario de hoy»): `backpropagation` pisaba su definición.**
La columna del término era angosta y el término más largo se comía el `gap`.
*Arreglado* ensanchando la columna y bajando un punto la letra (y verificado que la slide
sigue sin desbordar: ensanchar sin bajar la letra la hacía desbordar 30 px, lo probé).

**11. Dos inconsistencias de texto.**
`cuestionario.md` decía «Doce preguntas» y traía trece ítems, y el ítem 4 decía «sobra un
diagnóstico y falta ninguno» cuando son cuatro y cuatro. Y el pie de `viz/sobreajuste.html`
decía que la serie sintética es «por trimestre» cuando el muestreo es a tiempos al azar
sobre 24 años. Los tres arreglados.

---

## 3. Los números, verificados uno por uno

Todos se comprobaron **contra la corrida**, no contra el informe. La columna «medido» sale
de `nbconvert --execute` sobre `notebook.ipynb` y de `medir-figuras.py`, las dos con semilla 1983.

| Dónde | Afirmación | Medido | |
|---|---|---|---|
| slide 18 · nb §4 | mejor recta MSE **0.0146** | 0.01455 | ✅ |
| slide 18 · nb §4 | red de 16 rampas **0.0100** | 0.00996 | ✅ |
| slide 18 | «a ojo» **0.0195** | 0.01946 · **parámetros elegidos a mano** (declarado) | ⚠→✅ |
| slide 19 · nb TODO 2 | 4/16/64/256 → **0.01193 / 0.00900 / 0.00584 / 0.00509** | idénticos **[corregido]**: con torch 2.14, 0.01193 / 0.00899 / 0.00612 / **0.00628** (256 no mejora a 64). Hoy la slide lee `cap256` y el notebook no afirma «mejora» | ⚠→✅ |
| slide 19 | perillas 13 / 49 / 193 | idénticos | ✅ |
| slide 20 | calco: **601** perillas, train **0.00081**, en los 5 apartados **0.00753** | 601 · 0.000805 · 0.00753 **[corregido]**: con torch 2.14, 0.000613 · 0.00807 (lo lee la slide) | ✅ |
| slide 20 | la red de 16 rampas en esos 5: **0.00496** | 0.00496 **[corregido]**: con torch 2.14, 0.00472 | ✅ |
| slide 20 (notas) | «nueve veces peor» | 0.00753 / 0.00081 = **9,3×** **[corregido]**: con torch 2.14, 13×; las notas dicen «más de diez veces» | ⚠→✅ |
| slide 30 (notas) · nb TODO 4 | ~~«la brecha típica es de 50 veces»~~ **[corregido]** | 0.04665 / 0.00319 = **14,6×**, fondo en la época 34 | ✅ |
| slide 26 · nb §5 | tijera: mejor época **42**, después **1458** épocas peor | 42 y 1458 | ✅ |
| slide 35 · nb §6 | test al azar **0.0142** · honesto **0.0319** · baseline **0.0255** | 0.01423 · 0.03194 · 0.02551 | ✅ |
| slide 35 · nb §6 | **2,2 veces mejor** | 0.03194/0.01423 = 2,24 | ✅ (con el matiz del §2.3) |
| slide 35 · nb §6 | **7 presidentes**, Menem **10**, C. Fernández **8** | contado sobre `serie_completa`: 7 · 10 · 8 (y Alfonsín 6) | ✅ |
| slide 35 · nb §6 | 2005 y 2006 son **el mismo archivo** | `md5sum` sobre el corpus: `2a6a1fae…` en los dos | ✅ |
| nb §6 | fuga al azar: **4 presidentes** cruzados, **1** texto idéntico | idéntico | ✅ |
| viz anatomía | converge a **a = 0.0775, b = 0.1970** | óptimo exacto de mínimos cuadrados sobre esos 8 puntos: **0.077507 / 0.197017**, MSE 0.008844 (la viz muestra 0.00884) | ✅ |
| viz anatomía | los 8 valores de la serie | coinciden con `serie_menciones('seguridad')` año por año | ✅ |
| viz sobreajuste | capacidad 60, 5 muestras: train **0.0002**, val **0.0324**, **×3,56** | idéntico, apretando el botón 5 veces **[corregido]**: con los codos anidados, 0.0002 / 0.0250, ×2,85. Por defecto (n=25): el mejor es K=8, y K=60 da 0.0003 / 0.0157, ×1,43 | ✅ |
| viz sobreajuste | capacidad 60 + 300 casos: la tijera se cierra | 0.0059 / 0.0080, brecha 0.0021, «en el punto justo» **[corregido]**: con codos anidados, 0.0061 / 0.0088 (×1,08), «en el punto justo» | ✅ |
| viz partición | 7 de 7 del test con fuga, 6 presidentes | idéntico (con la semilla nueva) | ✅ |
| viz partición | por grupo | **[nuevo]** antes: test de 0 casos en 51 de 200 sorteos. Ahora: 4 casos por defecto, entre 2 y 10 en 500 sorteos, nunca 0 | ✅ |
| nb §6 (nuevo) | predicción para 2005 con la partición al azar | 0.1366 contra 0.1645 (error² 0.0008); el vecino por perfil de temas es 2006, distancia 0 | ✅ |
| gancho slides 2-3 | 99 / 61 vs 84 / 82 | **construido, y declarado** en `referencias.md` y en las notas | ⚠ declarado |
| slide 21 (nuevo) | 32 rampas → 0.000014 vs recta 0.001496 | tomado de la verificación de la **clase 2**, no re-medido acá **[corregido]**: después del arreglo del borde de la media móvil, 0.0000076 contra 0.001561 (números que midió el equipo de fundaciones para la clase 2) | ⚠ ver §5 |

**Reproducibilidad.** Se corrió `medir-figuras.py` de nuevo y `datos-figuras.js` volvió
idéntico byte por byte. El notebook se corrió cuatro veces y dio los mismos números las cuatro.
**[corregido]** Eso vale en la misma máquina y con las mismas versiones. En la revisión de
2026-09, con torch 2.14, varios números cambiaron (ver arriba). Ahora `datos-figuras.js`
guarda las versiones, y las notas del docente dicen qué hacer si no coinciden.

---

## 4. Lo que se miró y estaba bien

- **La viz de anatomía cumple su momento aha, y se comprobó paso por paso.** Se apretó
  «una estación» seis veces leyendo el DOM en cada una: en la estación 4 (ANOTAR) las filas
  de los gradientes reciben la clase `cambio` y las de `a` y `b` **no**; en la estación 5
  (MOVER) es exactamente al revés. La separación `backward` / `step`, que es la razón de ser
  de la viz, se ve de verdad.
- **La viz de sobreajuste también.** Con capacidad 60 y cinco «otra muestra» quedan cinco
  curvas fantasma completamente distintas sobre el mismo proceso generador, todas pasando por
  todos los puntos. Es la mejor demostración de varianza del material y funciona.
- **El motor de sobreajuste no hace trampa a favor de la moraleja.** Resuelve por mínimos
  cuadrados una base de K rampas con un poco de ridge, y escala las rampas por (K+1)
  justamente para que la regularización no apague sola las capacidades altas. Está comentado
  en el archivo. ~~La curva de train baja monótonamente con la capacidad, que es el punto.~~
  **[corregido]** No bajaba monótonamente: con los codos en j/(K+1) los modelos no estaban
  anidados y la azul subía 25 veces entre K=1 y 60. Ahora los codos están anidados (ver §0).
- **El notebook reporta un resultado que no le conviene** — con 36 casos la red no le gana a
  predecir el promedio — y lo explica en vez de maquillarlo. Es lo correcto y es coherente con
  lo que la clase le pide a los demás.
- **Mira el test dos veces a propósito y lo dice en voz alta**, con un recuadro explicando que
  ese test queda quemado. Bien.
- Datos sintéticos rotulados con el chip `sintético` en las dos viz que los usan.
- El presupuesto de tiempo cierra en 120 min exactos y es continuo; la pausa tiene su
  `<section class="pausa">` (slide 17).
- El puente desde la clase 3 (slide 5) y hacia la clase 5 (slides 39-40) están explícitos.
- Tono: rioplatense, voseo, con humor y sin condescendencia, de punta a punta. No se encontró
  ni un tramo solemne. Ninguna slide es un muro de texto sin figura, ejemplo o pregunta.
- El cuestionario se contesta con lo que se dio, y los distractores son tentadores de verdad
  (el A del ítem 1 —«demasiados parámetros»— es *casi* cierto, que es lo que lo hace útil).
  Las soluciones son correctas y explican qué revela cada error.
- Las ocho citas existen, están bien atribuidas y bien fechadas. No se sacó ninguna.

---

## 5. Lo que queda abierto

| # | Qué | Para quién |
|---|---|---|
| 1 | **Subir a `_shared/css/curso.css` la regla `box-sizing: border-box`** (por lo menos para `.viz-frame` y `.panel`, idealmente global). El bug del §2.1 **afecta a las diez clases**: cualquier viz con `.viz-frame` + padding embebida en una slide pisa su panel. Acá está parcheado localmente en las 3 viz para no pisar a los equipos que trabajan en paralelo. | quien cierre la base |
| 2 | **`.reveal pre code` no tiene `display: block`** en `curso.css` ni en el reveal vendoreado. Un `<code>` con padding vertical pinta su fondo encima de las líneas vecinas. Confirmado leyendo el CSS. Está parcheado en el `<style>` local de esta clase (lo dejó el equipo constructor y lo verifiqué); conviene subirlo también. | quien cierre la base |
| 3 | **Las 5 URLs `[VERIFICAR URL]` siguen sin verificar.** Se probó `curl` de nuevo contra las siete: sólo responden las dos de `raw.githubusercontent.com`, que están marcadas `[VERIFICADA]` con el código 200. `doi.org`, `pytorch.org`, `hastie.su.domains`, `deeplearningbook.org` y `github.com` (HTML) devuelven 403 en el túnel del proxy. Las obras existen y están bien citadas; falta abrir los enlaces. | quien tenga red |
| 4 | **El número de la clase 2 en la slide 21 no lo medí yo.** Hoy dice 0.0000076 contra 0.001561 (los valores después del arreglo del borde de la media móvil) y 97 perillas (3K+1). Si la clase 2 cambia esa viz o cuenta las perillas de otra manera, hay que actualizar el pie y las notas de la slide 21. | equipos 2 y 4 |
| 5 | **Coordinación con la clase 9.** Las cifras del gancho (A 99/61 vs B 84/82) están construidas y pensadas para cobrarse en la clase 9 con el corpus de prensa real (donde la fuente predice la etiqueta al 96 %). Si la 9 mide otros órdenes de magnitud, hay que ajustar la nota final de `referencias.md`. | equipo 9 |
| 6 | **Licencia del corpus de discursos.** No declara ninguna (trampa 13 de la espina). Anotado en `referencias.md`. Si el curso se publica, hay que escribirle a Lucas Ariel. | el docente |
| 7 | ~~El cierre está apretado: 5 slides (36-40) en 2 minutos.~~ **[corregido]** El plan nuevo le da 6 minutos (114-120): el práctico 2 quedó en 12 minutos (91-103), la puesta en común en 2 y la slide 29 en uno. | el docente |
| 8 | **Nadie corrió el notebook en Colab.** Acá tarda **28,9 s** en CPU (mediana de tres). En la CPU de Colab debería ser parecido, pero es una expectativa, no una medición. | el primero que lo dicte |

---

## 6. Cómo reproducir esta verificación

```bash
cd /home/user/dlss
python3 -m nbconvert --to notebook --execute --output /tmp/o.ipynb \
        clases/04-entrenar-de-verdad/notebook.ipynb
PYTHONPATH=_shared python3 clases/04-entrenar-de-verdad/medir-figuras.py
git diff --stat clases/04-entrenar-de-verdad/datos-figuras.js   # vacío sólo con las mismas
                                                               # versiones (ver "versiones")
md5sum datos/cache/discursos-apertura/200[56]-*.txt             # los dos hashes iguales
for f in datos/muestras/discursos-apertura/200[56]-*.txt; do    # en las muestras, sin las
  grep -v '^#' "$f" | md5sum; done                              # cabeceras: 89b4c032… los dos
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`),
abriendo por `file://` con un `context.route('**/*')` que **aborta cualquier URL `http(s)`**
y cuenta las que salen. Las slides se recorren con `Reveal.slide(k, 0)` **abriendo todos los
fragmentos** de cada una (si no, no ves lo que desborda) y midiendo el borde inferior del
último hijo contra el alto de la ventana. Las viz embebidas hay que mirarlas **adentro de un
iframe de 1280×610**, que es el tamaño real de `.viz-frame[data-alto="grande"]`: sueltas se
ven bien y el bug del §2.1 no aparece.
