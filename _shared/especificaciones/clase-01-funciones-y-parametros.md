# Clase 1 — Una función es una máquina con perillas
**Directorio:** `clases/01-funciones-y-parametros/`
**Duración:** 120 min · **Prerrequisitos:** ninguno · **Nivel de código:** cero previo

---

## 1. Narrativa de la clase (el hilo argumental)

El problema que abre el curso es el problema más viejo de las ciencias sociales cuantitativas:
**tengo unos puntos y quiero decir algo general sobre ellos.** Nadie en el aula se siente ajeno a
eso. Lo que hacemos hoy es mostrar que decir "algo general" es, operativamente, **elegir una figura
y ubicarla**; que ubicar una figura es mover un puñado de números; y que ese puñado de números
—los parámetros— es una categoría distinta de los datos, aunque ambos sean números y aunque el
lenguaje de la estadística los mezcle todo el tiempo.

El hilo, en orden:

1. **Unos puntos misteriosos** → todos quieren trazar una línea. La intención de modelar aparece
   sola, antes de cualquier definición. No la definimos: la usamos.
2. **La función como máquina** → una caja con una boca de entrada, una boca de salida y perillas
   al costado. Se dibuja literalmente esa caja. Todo el curso vuelve a esta imagen.
3. **La distinción que vale la clase entera** → variable vs parámetro. La misma fórmula, dos tipos
   de movimiento incompatibles: mover `x` te *recorre* la figura, mover `a` *deforma* la figura.
   Es una distinción que la audiencia ya tiene sin saberlo (una tasa de crecimiento es un
   parámetro; un año es una variable) y hay que hacérsela consciente.
4. **Primer contacto con el código** → Python como forma de escribir la caja. Nada de sintaxis por
   la sintaxis: se escribe una función, se grafica, se cambia un número, se vuelve a graficar.
5. **El zoo** → cinco formas básicas y para qué sirve cada una. Se siembra la sigmoide ("guardala").
6. **El ajuste a ojo** → ellos mueven las perillas contra datos reales, y aparece la necesidad de
   un número que diga qué tan mal están. Se lo llama "medidor de desajuste" y **no** se lo llama
   loss todavía: el nombre técnico se gana en la clase 3, cuando ya duela no tenerlo.
7. **La frustración productiva** → la recta no alcanza. Fin de clase con la puerta abierta.

**Tono.** Esta es la clase donde se decide si la gente vuelve. Mucho humor, cero solemnidad, cero
disculpas por la matemática ("no se asusten" es contraproducente: no se anuncia el susto). Nadie
tiene que sentir que hay un examen. La palabra "derivada" no se pronuncia hoy.

`[CALLBACK DIBUJO]` — **se instala hoy**: "una función es una máquina de dibujar figuras. Las
perillas eligen qué figura. Todo el curso es esto, con máquinas cada vez más grandes."

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-4 | La nube de puntos misteriosa. Se vota qué línea la resume. No se resuelve. |
| 10-25 | Exposición: máquina con perillas | 5-10 | `f(x)=a·x+b` con la viz proyectada. Se nombra el «medidor de desajuste», todavía no se lo llama *loss*. |
| 25-40 | Viz + apuesta: variable vs parámetro | 11-14 | **Primero se pregunta y se vota**, recién después se mueve la perilla. |
| 40-60 | Manos 1: notebook | 15 | Colab. Definir funciones, graficarlas, TODO 1. |
| 60-70 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 15. |
| 70-85 | Exposición: el zoo de funciones | 16-24 | Recta, parábola, exponencial, sigmoide, seno. «Guardá la sigmoide». |
| 85-105 | Manos 2: ajuste a ojo | 25 | De a dos, con datos reales de discurso político. |
| 105-120 | Cierre | 26-32 | El ranking, `[EL LUNES]`, el puente a la clase 2, el glosario. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (32 slides)

Formato: `NN. TÍTULO — [tipo] — contenido — <docente dice>`
Tipos: `[texto]` `[figura]` `[VIZ]` (embebida en iframe) `[código]` `[discusión]`

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Deep Learning para Cientistas Sociales | portada | Título, clase 1, nombre del docente. Fondo: una nube de puntos tenue. | "Antes de que empecemos: nadie acá va a tener que derivar nada. Si en algún momento sentís que se puso matemático de más, es culpa mía y quiero que me lo digas." |
| 2 | ¿Qué le pasó a este país? | figura | 40 puntos, sin ejes rotulados, patrón claro pero con ruido. | "Tómense un minuto. ¿Qué historia cuenta esto?" Deja hablar. No corrige nada. |
| 3 | (los mismos puntos, con ejes) | figura | Eje X: año 1983-2023. Eje Y: % de palabras del discurso de apertura dedicadas a *seguridad*. Fuente rotulada. | "Ah. Bueno. ¿Cambia lo que dijeron? ¿Alguien mantiene su historia?" |
| 4 | La pregunta del curso | texto | "Si tuvieras que resumir esto con **una línea**, ¿cuál dibujarías?" | "No con palabras: con una línea. Con el dedo en el aire." Que lo hagan. |
| 5 | Tres candidatas | figura | La misma nube con tres líneas: una recta, una curva suave, una que pasa por todos los puntos. | "Tres personas dibujaron esto. Guarden cuál les gusta más: en la clase 4 vamos a descubrir que una de las tres es una trampa." |
| 6 | Para dibujar la recta hacen falta 2 números | figura | La recta con `a` (pendiente) y `b` (altura) señalados con flechas. | "Dos. Nada más. Toda la información de esa línea infinita cabe en dos números." |
| 7 | **La caja con perillas** | figura | Dibujo grande: caja, flecha que entra (x), flecha que sale (y), dos perillas arriba rotuladas a y b. | "Esta imagen la vamos a usar durante diez clases. Una función es esto: entra algo, sale algo, y tiene perillas." |
| 8 | Lo mismo, escrito | texto+fórmula | `f(x) = a·x + b` con colores: `x` en un color, `a` y `b` en otro. Debajo, la caja de la slide 7 con los mismos colores. | "Esta es la única fórmula de la clase de hoy, y ya la entendieron mirando el dibujo." |
| 9 | Dos tipos de números | texto | Tabla de dos columnas. **Variable**: lo que entra, cambia con cada caso, la elige el mundo (el año, la edad, la cantidad de palabras). **Parámetro**: la perilla, es la misma para todos los casos, la elegís vos (o la aprende la máquina). | "Esta distinción es el 80% de la clase. Si se la llevan, ganamos." |
| 10 | Ustedes ya usan parámetros | texto | Ejemplos de su mundo: "creció 3% por año" (3% es un parámetro); "por cada año de educación, +X de ingreso" (X es un parámetro, es *el* coeficiente); una tasa, un coeficiente de regresión, un peso muestral. | "Cuando reportás un coeficiente en una tabla de regresión, estás reportando una perilla. Ya venís haciendo esto." |
| 11 | **Movelas vos** | VIZ | `viz/maquina-de-perillas.html` embebida. | El docente mueve `a` y `b`. "¿Qué pasa si subo la pendiente? ¿Y si la bajo a cero?" |
| 12 | Apuesta | discusión | Pregunta a pantalla completa: "Si muevo **x**, ¿se mueve la curva o se mueve un punto sobre la curva?" con dos opciones para votar a mano alzada. | "Voten. En serio, levanten la mano. Es importante que se equivoquen ahora y no en la clase 4." |
| 13 | **La respuesta** | VIZ | `viz/variable-vs-parametro.html`. | "Izquierda: muevo x, la bolita corre, la curva quieta. Derecha: muevo a, la bolita quieta, la curva se retuerce. Dos movimientos completamente distintos." |
| 14 | El medidor de desajuste | figura | La nube, una recta mal puesta, y segmentos verticales rojos de cada punto a la recta. Al costado, un número grande. | "Cada palito rojo es un error. Si los sumo, tengo un número que dice qué tan mal está. Ese número va a ser la estrella de la clase 3." |
| 15 | Bloque práctico 1 | texto | Instrucciones: abrir el notebook en Colab, link corto, qué hacer si no anda. | "Cuarenta minutos. Yo doy vueltas. Si algo no corre, levanten la mano y no se peleen con la compu." |
| 16 | Volvimos | texto | Repaso en 3 viñetas de lo que hicieron en el notebook. | "¿Qué encontraron? ¿A alguien le pasó algo raro?" |
| 17 | El zoo de funciones | figura | Grilla 2x3: recta, parábola, exponencial, sigmoide, seno, escalón. Cada una con su nombre y una frase de para qué sirve. | "Estas son las formas básicas. Como los ladrillos de un Lego." |
| 18 | La recta | figura | Con su fórmula y su interpretación social: "cambio constante por unidad". | "Cuando decís 'creció linealmente' estás diciendo esto." |
| 19 | La parábola | figura | "Sube y después baja" — la curva de Kuznets, la U invertida, el ciclo. | "Toda ciencia social tiene su U invertida favorita." |
| 20 | La exponencial | figura | Crecimiento explosivo. Ejemplo: difusión de una noticia en redes. | "Nuestro cerebro es malísimo para lo exponencial. Por eso nos sorprende siempre." |
| 21 | **La sigmoide** (guardá esta) | figura | La S. Rotulada: "empieza lento, se acelera, se satura". Ejemplos: adopción de una innovación, saturación de un tema en la agenda mediática. | "Márquenla. Esta función vuelve en la clase 2, en la 3 y en la 9. Es la más importante del curso después de la recta." |
| 22 | El seno | figura | Periodicidad: ciclo electoral, estacionalidad de las noticias. | "Todo lo que se repite." |
| 23 | **Jugá con el zoo** | VIZ | `viz/zoo-de-funciones.html`. | "Cada una tiene dos perillas. El desafío: reproducir la figura gris." |
| 24 | La misma fórmula, otra historia | texto | La sigmoide con parámetros distintos y las tres lecturas sustantivas correspondientes. | "El parámetro no es un detalle técnico: es la afirmación sustantiva. Cuando cambiás el parámetro, cambiás la teoría." |
| 25 | Bloque práctico 2: ajuste a ojo | texto | Consignas del desafío en parejas. | "De a dos. Uno mueve, el otro mira el número. Quien llegue más bajo gana el prestigio eterno." |
| 26 | El ranking | discusión | Espacio en blanco para anotar los mejores resultados del aula. | "¿Cuánto sacaron? ¿Cómo hicieron para bajar? Escuchen lo que acaban de describir: una estrategia de búsqueda." |
| 27 | Lo que acaban de hacer tiene nombre | texto | "Mover perillas para minimizar un número" = **optimización**. Y hacerlo a mano = insoportable. | "Ustedes acaban de hacer a mano, con dos perillas y en diez minutos, lo que una computadora hace con mil millones de perillas en dos semanas. La idea es la misma." |
| 28 | `[EL LUNES]` | texto | Tres pasos concretos: 1) tomá una serie de tu investigación; 2) graficala; 3) ajustale una recta y decí **en castellano sustantivo** qué significa cada parámetro. | "Si tu pendiente es 0.4, no digas 'la pendiente es 0.4'. Decí 'cada año sube 0.4 puntos'. Esa traducción es tu trabajo, no el del modelo." |
| 29 | Pero... | figura | La curva de menciones a "inflación": dos picos y un valle. Con la mejor recta posible encima, fracasando gloriosamente. | "Esto es lo que nos espera la clase que viene. Miren qué mal le va a la recta." |
| 30 | Dos caminos | texto | Camino A: buscar una fórmula más complicada para cada caso. Camino B: **combinar** funciones simples. | "El camino A es lo que hizo la estadística durante un siglo, y funciona. El camino B es lo que hace el deep learning. Vamos por B." |
| 31 | El puente | texto | "Clase 2: componer funciones para dibujar figuras imposibles con una sola máquina." | "Van a ver algo que a mí todavía me parece magia, y no lo es." |
| 32 | Glosario de hoy | texto | función, variable, parámetro, ajustar, optimización. Link a `recursos/glosario.md`. | "Todo término nuevo va al glosario. Está online y crece con nosotros." |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/maquina-de-perillas.html`
- **Qué se ve.** Panel único. Un scatter de 40 puntos (año vs % menciones a *seguridad*, corpus
  Aguasclaras). Encima, una recta azul gruesa. A la derecha, un dibujo esquemático de la caja con
  dos perillas que **giran de verdad** cuando movés los sliders (feedback redundante: el slider y
  la perilla dibujada se mueven juntos).
- **Controles.** Slider `a` (pendiente, -2 a 2, paso 0.05) y slider `b` (ordenada, -20 a 60, paso 1).
  Botón "reset". Checkbox "mostrar errores" que dibuja los segmentos verticales rojos.
- **Números en pantalla.** La fórmula `f(x) = a·x + b` con los valores actuales sustituidos y
  resaltados en el mismo color que su slider. Un "desajuste" grande (suma de cuadrados normalizada),
  con una barra horizontal que se llena de verde a rojo. **No se lo llama loss.**
- **Qué tiene que hacer clic.** Que `a` y `b` hacen cosas **cualitativamente distintas** (una gira,
  la otra traslada), y que el número de desajuste responde a los dos.
- **Momento aha.** "El número de abajo baja cuando la línea se acerca a los puntos. Entonces si yo
  supiera cómo bajar ese número automáticamente, no necesitaría los sliders."
- **Detalle de implementación.** Canvas 2D. Sin dependencias. Redibujado en `input` de los sliders,
  no en `change` (tiene que sentirse continuo). Ejes rotulados en castellano.

### 3.2 `viz/variable-vs-parametro.html`
- **Qué se ve.** Dos paneles lado a lado, con la **misma** función `f(x) = a·x²` dibujada en ambos.
  - Panel izquierdo, título "**Movés la variable x**": la curva está **fija y en gris claro**; una
    bolita naranja corre sobre ella; líneas punteadas bajan al eje x y al eje y mostrando el par.
  - Panel derecho, título "**Movés el parámetro a**": la bolita está **fija** en `x=2` (marcada con
    una línea vertical), y la curva se deforma; se dibujan en gris fantasma las curvas anteriores
    (rastro de las últimas 8 posiciones), así queda una familia de curvas.
- **Controles.** Slider `x` (sólo afecta al panel izquierdo). Slider `a` (sólo afecta al derecho).
  Botón "animar los dos" que los barre automáticamente, para verlos en contraste.
- **Qué tiene que hacer clic.** Que son dos movimientos que no se parecen en nada, aunque en la
  fórmula `a` y `x` estén escritos igual, uno al lado del otro.
- **Momento aha.** "Ah, el rastro de la derecha son *todas las funciones posibles*. Elegir el
  parámetro es elegir una de esa familia. Aprender es elegir."
- **Refuerzo textual.** Debajo de cada panel, una frase que cambia en vivo: izquierda, "estoy
  mirando **otro caso** de la misma teoría"; derecha, "estoy proponiendo **otra teoría**".
  Esta frase es la mitad del valor de la viz.

### 3.3 `viz/zoo-de-funciones.html`
- **Qué se ve.** Grilla de 6 tarjetas: recta, parábola, exponencial, sigmoide, seno, ReLU
  (la ReLU aparece rotulada como "la rampa" y con un cartelito "esta es la protagonista de la
  clase que viene", sin explicarla).
- **Controles.** Cada tarjeta tiene 2 sliders con nombres **en castellano y sustantivos**
  ("qué tan empinada", "dónde está el codo", "qué tan rápido se satura"), no `a` y `b`.
- **Modo desafío.** Botón "desafío": aparece una curva gris objetivo dentro de una tarjeta al azar y
  hay que reproducirla con los sliders; cuando el error baja de un umbral, la tarjeta se pone verde
  y aparece "¡esa es!". Tres niveles.
- **Qué tiene que hacer clic.** Que cada forma tiene un repertorio limitado: por más que muevas los
  sliders de la recta, nunca vas a hacer una S.
- **Momento aha.** "Con la recta no puedo hacer la curva del desafío 3 ni loco. La forma de la
  función es una restricción sobre lo que puedo afirmar."
- **Nota de diseño.** Este aha es **el gancho de la clase 2**, así que tiene que quedar frustrado a
  propósito: el desafío 3 debe ser imposible para la tarjeta de la recta e imposible para todas las
  demás individualmente.

---

## 4. Especificación del notebook (`notebook.ipynb`)

**Tiempo total de ejecución:** < 60 segundos, CPU. **Dependencias:** numpy, matplotlib
(preinstaladas en Colab; la celda 1 igual las importa y avisa si falta algo).

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | **Bienvenida.** Qué es un notebook, qué es una celda, cómo se corre (Shift+Enter), qué pasa si rompés algo (nada: se reinicia y listo). Con captura de pantalla del botón de play. | Explícitamente tranquilizador. |
| 2 | code | Imports y configuración de gráficos. Imprime "Todo listo ✓". | Que la primera celda que corren dé una recompensa. |
| 3 | md | **Tu primera función.** La caja con perillas, en Python. | |
| 4 | code | `def recta(x, a, b): return a*x + b` y tres llamadas con `print`. | Se lee línea por línea en clase. |
| 5 | md | Explicación de qué es `def`, qué son los argumentos, qué hace `return`. Con la caja dibujada al lado en ASCII o como imagen. | |
| 6 | code | Graficar la recta: `xs = np.linspace(...)`, `plt.plot(xs, recta(xs, 2, 5))`. | Primer gráfico propio: momento importante. |
| 7 | code | **Celda de juego.** La misma recta con `a` y `b` en variables al principio, bien visibles, con comentarios `# ← cambiá este número`. | Se les pide correrla 5 veces cambiando números. |
| 8 | md | `TODO 1` — Dibujá una recta que pase por (0, 10) y baje 2 por cada unidad de x. *Pista: uno de los dos números te lo dice directamente el enunciado.* | |
| 9 | code | Celda vacía con el esqueleto y un `assert` suave que valida la respuesta con un mensaje amable. | |
| 10 | md | **Los datos de verdad.** Presentación del corpus (rotulado: sintético Aguasclaras / real si se consiguió). Qué se midió, cómo, y las salvedades. | Momento de honestidad metodológica, breve. |
| 11 | code | Carga de datos con el patrón try/except obligatorio. Muestra `df.head()` y el scatter. | |
| 12 | md | **Ajuste a ojo.** Consigna del desafío. | |
| 13 | code | Función `desajuste(a, b)` que calcula el error cuadrático medio y una función `probar(a, b)` que grafica la recta sobre los datos, dibuja los errores y **imprime el número en grande**. | La función `probar` es el corazón del bloque práctico. |
| 14 | code | Celda de juego con `probar(1.0, 0.0)`. Comentario: `# ← cambiá los dos números y volvé a correr. ¿Cuánto podés bajar?` | Se corre 20 veces. Está bien que se corra 20 veces. |
| 15 | md | `TODO 2` — Bajá el desajuste de 1.0 y 0.0 a menos de la mitad. Anotá los valores que encontraste. *Pista: mirá primero si la recta está muy arriba o muy abajo (eso es `b`), y después si está muy inclinada (eso es `a`).* | La pista enseña una **estrategia de búsqueda coordinada**, que es descenso por coordenadas: se lo va a nombrar en la clase 3. |
| 16 | md | `TODO 3 (opcional, para los que van rápido)` — Escribí un `for` que pruebe 20 valores de `a` y se quede con el mejor. *Pista: guardá el mejor en una variable y comparalo con cada nuevo.* | Prefigura la búsqueda por grilla de la clase 3. |
| 17 | code | Esqueleto del `for` con huecos. | |
| 18 | md | **El zoo, en código.** | |
| 19 | code | Definición de las 5 funciones del zoo y una grilla de subplots con las 5. | |
| 20 | code | Celda de juego: elegí una función del zoo y cambiale los parámetros. | |
| 21 | md | `TODO 4` — ¿Podés hacer que la sigmoide parezca casi un escalón? ¿Qué parámetro tuviste que exagerar? *Pista: uno de los dos controla lo empinado.* | Prefigura saturación y, mucho después, la temperatura de la clase 8. |
| 22 | md | **Para llevarte.** Resumen en 5 viñetas + la pregunta abierta de la clase 2 + link al glosario. | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"`x` y `a` son lo mismo, son letras"** | El estudiante mueve el slider equivocado buscando un efecto. | La viz 3.2 existe para esto. Además: la regla del dedo — "¿este número cambia de un caso a otro de mi base? Entonces es variable. ¿Es el mismo para toda la base? Es parámetro." |
| **"Entonces la máquina descubre la fórmula"** | Esperan que el modelo les diga *qué* función es la correcta. | Se aclara ya en la clase 1: **vos elegís la familia de figuras** (recta, S, red neuronal) y la máquina elige el miembro de la familia. La elección de familia es tuya y es teórica. Se retoma en las clases 5 y 10. |
| **Miedo al `def`** | Se traban en la sintaxis y no llegan al contenido. | La celda 4 se lee en voz alta palabra por palabra, incluidos los dos puntos y la indentación. Se les dice explícitamente: "Python es maniático con los espacios y no es culpa tuya." |
| **"Si toco algo, rompo todo"** | No experimentan; sólo corren las celdas en orden y en silencio. | Se rompe algo a propósito adelante de todos (un error rojo enorme), y se muestra que reiniciar el entorno no tiene consecuencias. "El error rojo no es un reto, es información." |
| **Confundir "ajustar bien" con "estar en lo cierto"** | "Bajé el número, entonces mi modelo es verdadero." | Se planta la duda hoy y se cosecha en la clase 4 (slide 5: la línea que pasa por todos los puntos es una trampa). |
| **Leer `f(x)` como "f por x"** | Error clásico de quien viene de aritmética escolar. | Se dice explícitamente una vez: "no es una multiplicación, son los paréntesis de 'aplicá f a x'. Es notación desafortunada y la sufrimos todos." |
| **Creer que hay que memorizar las fórmulas del zoo** | Toman apuntes de las fórmulas en vez de mirar las formas. | "No hay nada que memorizar. Quiero que reconozcan la **forma**. Si ven una S, piensan 'sigmoide' y buscan la fórmula en Google." |

---

## 6. Analogías y metáforas de ciencias sociales para este tema

- **La perilla y el caso.** Un cuestionario tiene preguntas (variables: cambian por persona) y tiene
  un diseño (parámetros: son iguales para toda la muestra). Nadie confunde una respuesta con el
  diseño del cuestionario. Es la misma distinción.
- **El coeficiente de regresión ya es un parámetro.** Quien haya corrido alguna vez una regresión ya
  estimó parámetros; lo único nuevo del curso es que las figuras van a ser más raras que una recta.
- **La receta y el plato.** La receta (función) es la misma; las cantidades (parámetros) definen el
  resultado; los ingredientes que le metés hoy (variables) cambian cada día.
- **El ecualizador de audio.** Cinco perillas, un sonido. Nadie sabe la fórmula del ecualizador y
  todos lo usan bien. Se puede tener criterio sobre un sistema sin conocer su interior — y ese es
  justamente el objetivo del curso.
- **La operacionalización.** "% de palabras dedicadas a seguridad" es una decisión de medición
  discutible: podría ser menciones, minutos, o posición en el discurso. Vale la pena decirlo hoy:
  **antes de cualquier modelo hay una decisión de medición, y ahí se juega la mitad de la validez.**
  Es la primera aparición del tema que cierra el curso en la clase 10.

---

## 7. Cuestionario: temas a evaluar (10 ítems)

1. **[MC conceptual]** En `f(x) = a·x + b`, ¿cuál de estos es un parámetro? (opciones que incluyan
   un caso claro, un distractor plausible y el "depende de qué estés preguntando").
2. **[MC conceptual]** ¿Qué distingue a un parámetro de una variable? (la respuesta correcta apunta
   a "es el mismo para todos los casos de la base").
3. **[Qué pasa si]** Tenés `f(x) = a·x + b` con `a=0.5`, `b=10`. Si duplicás `a`, ¿qué le pasa al
   dibujo? ¿Y si duplicás `b`?
4. **[Qué pasa si]** Ponés `a = 0`. ¿Qué figura queda y qué está afirmando sustantivamente ese
   modelo sobre el fenómeno?
5. **[Leer un gráfico]** Tres rectas sobre una misma nube. Ordenarlas de menor a mayor desajuste
   sólo mirando, y justificar en una oración.
6. **[Leer un gráfico]** Se muestra una familia de curvas (el rastro de la viz 3.2) y se pide decir
   qué parámetro se movió para generarlas.
7. **[Reconocer la forma]** Cuatro descripciones sustantivas ("la adopción de una tecnología se
   acelera y después se satura", "el tema aparece cada 4 años", "crece a ritmo constante", "sube y
   después baja") y cuatro figuras del zoo, para aparear.
8. **[Traducción sustantiva]** Un modelo de menciones a *educación* por año da `a = -0.3`, `b = 8.2`.
   Escribí en una oración, sin jerga, qué dice ese modelo. Y escribí una oración sobre lo que ese
   modelo **no** dice.
9. **[Código]** Se da una función Python de tres líneas con un error (una variable mal nombrada o
   un `return` faltante) y se pide encontrarlo. Sin trampa: el error es visible.
10. **[Criterio / ética aplicada]** El "% de palabras dedicadas a seguridad" se propone como medida
    de "prioridad del gobierno en materia de seguridad". Dar **dos** razones por las que esa medida
    podría no capturar lo que dice capturar. *(Se busca: hablar mucho de algo puede ser reacción a
    la agenda mediática y no prioridad; un gobierno puede actuar mucho y hablar poco; el discurso de
    apertura es un género con reglas propias; cambió el largo de los discursos.)*

**Nota para quien escriba las soluciones:** el ítem 10 no tiene respuesta única y así hay que
decirlo en el solucionario. Sirve para abrir la conversación que cierra el curso en la clase 10.

---

## 8. Referencias

**Para el estudiante (breves, opcionales, en castellano cuando se pueda):**
- 3Blue1Brown, serie *Essence of Calculus*, capítulo 1 — para la intuición visual de función.
  Hay subtítulos en español. `[VERIFICAR URL]`
- 3Blue1Brown, *But what is a neural network?* — se recomienda **mirarlo recién después de la clase
  2**; se anuncia hoy para los ansiosos. `[VERIFICAR URL]`
- *Python para todos* (py4e) de Charles Severance, capítulos 1-4, versión en español, para quien
  quiera afianzar la sintaxis. `[VERIFICAR URL]`

**Para el docente:**
- Grimmer, Roberts & Stewart, *Text as Data* (Princeton UP, 2022), capítulo introductorio: la
  discusión sobre medición y validez que este curso retoma en la clase 10. `[VERIFICAR]`
- Breiman, L. (2001), *Statistical Modeling: The Two Cultures*, Statistical Science 16(3).
  **Es la lectura que fundamenta el "camino A vs camino B" de la slide 30.** `[VERIFICAR URL]`
  Muy recomendable para el docente aunque no se asigne al aula.
- Molina, M. & Garip, F. (2019), *Machine Learning for Sociology*, Annual Review of Sociology.
  Panorama del campo escrito para esta audiencia exacta. `[VERIFICAR]`

**Regla para el equipo:** ninguna URL entra a `referencias.md` sin `curl -sI` exitoso desde un
entorno con red, o sin la marca `[VERIFICAR URL]` bien visible al lado.
