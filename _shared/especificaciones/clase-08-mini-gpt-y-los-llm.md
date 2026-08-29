# Clase 8 — Un mini-GPT propio, y la traducción a ChatGPT
**Directorio:** `clases/08-mini-gpt-y-los-llm/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-7 · **Cierre del módulo 2**
**GPU:** opcional (T4 acelera el entrenamiento de ~8 min a ~2 min; **el notebook debe funcionar en
CPU sí o sí**, con un modelo reducido si hace falta)

---

## 1. Narrativa de la clase

Esta es la clase que justifica el curso ante un cientista social escéptico. Todo el mundo usa
LLMs; casi nadie sabe qué son. Al final de hoy, esta audiencia va a poder explicar el
comportamiento de ChatGPT **desde el mecanismo**, no desde la analogía. Ese es el producto.

La clase tiene una estructura de dos actos con un intervalo técnico:

**Acto 1 (0-50 min): lo construimos y lo vemos aprender.** El entrenamiento en vivo es teatro y hay
que tratarlo como teatro. Cada 500 pasos el modelo imprime una muestra, y la progresión —sopa de
letras → sílabas → palabras → sintaxis → cadencia parlamentaria— es genuinamente emocionante. Hay
que dejar que corra mientras se hacen otras cosas y volver a mirarlo tres o cuatro veces. **El
entrenamiento tiene que arrancar en el minuto 20 como máximo** para que esté listo cuando se lo
necesite.

**Acto 2 (50-100 min): la traducción.** El bloque que paga todo. Cada pieza del modelo que
acaban de entrenar se conecta con un comportamiento observable de ChatGPT que ya vivieron. No es
una lista de curiosidades: es una demostración sistemática de que **todo lo raro que hace un LLM se
sigue del mecanismo, y nada de eso es un bug misterioso**.

**Cierre (100-120 min): qué le falta a esto para ser ChatGPT, y qué no cambia con la escala.**
Honestidad sobre la diferencia (escala, datos, instruction tuning, RLHF) y sobre lo que la escala
**no** arregla (la ausencia de un mecanismo de verdad, la tokenización, el contexto finito).

**La ventaja del corpus sintético.** Como Aguasclaras fue generado por nosotros, conocemos la
verdad del proceso generador. Eso permite, en el bloque de alucinación, **poner la verdad al lado
de la invención** y mostrar exactamente en qué momento el modelo se inventó un diputado que no
existe. Es una demostración imposible con un corpus real y hay que explotarla al máximo.

`[CALLBACK DIBUJO — el grande del curso]` — Slide obligatoria: en la clase 1 dibujábamos una recta
con 2 perillas contra 40 puntos. Hoy dibujamos, para cada posición del texto, **una distribución de
probabilidad sobre 5.000 fichas posibles**, con un millón y medio de perillas. **Es la misma máquina.**
Misma loss (clase 3), mismo descenso (clase 3), mismo ciclo (clase 4), mismo riesgo de calcar
(clase 4), mismos embeddings (clase 6), mismo bloque (clase 7). No hay ninguna pieza nueva hoy.
Decirlo así, explícitamente, es el cierre intelectual del curso.

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-4 | ¿Real o generado? Lo escribió esto. La promesa del día. |
| 10-20 | El objetivo más tonto del mundo | 5-11 | El dataset se arma solo, el bigrama, la arquitectura y la cross-entropy. |
| 20-40 | Manos 1: entrenar | 12 | **El entrenamiento arranca acá, minuto 20 como máximo**, y queda corriendo toda la clase. |
| 40-50 | **PAUSA** | — | **En serio, pausa.** El modelo entrena solo. Slide propia después de la 12. |
| 50-75 | **La traducción**: el modelo → ChatGPT | 13-33 | Siete comportamientos de ChatGPT explicados desde el modelo que acaban de entrenar. |
| 75-100 | Manos 2 | 34 | **25 minutos.** Temperatura, romper el contexto, hacerlo alucinar, contar letras. |
| 100-120 | Cierre | 35-38 | Qué le falta para ser ChatGPT, qué no cambia con la escala, `[EL LUNES]`, el puente. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (38 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Un GPT propio | portada | | |
| 2 | **¿Real o generado?** | figura | Un párrafo de debate parlamentario, con cadencia y fórmulas de cortesía. | "Voten: ¿lo dijo alguien o lo escribió una máquina?" |
| 3 | Lo escribió esto | figura | Foto del notebook con la celda de entrenamiento. "~1,5 millones de parámetros. 10 minutos de entrenamiento. En la compu de ustedes." | "Y hoy lo van a entrenar, y van a poder mirar cada pieza." |
| 4 | La promesa del día | texto | Lista de lo que van a poder explicar al final: por qué alucina, por qué importa el prompt, qué es la ventana de contexto, qué es la temperatura, por qué cuenta mal las letras, por qué a veces se contradice. | "Todo esto, explicado desde adentro. No con metáforas." |
| 5 | El objetivo más tonto del mundo | figura | Una ventana de texto y la próxima ficha resaltada: "El señor diputado pidió la ___". | "Predecir la próxima ficha. Eso es todo lo que hace. Todo lo demás sale de acá." |
| 6 | El dataset se arma solo | figura | Un texto largo cortado en ventanas superpuestas, cada una con su "respuesta correcta" (la ficha siguiente). | "No hay que etiquetar nada. El texto **es** su propia etiqueta. Por eso se puede entrenar con internet entero." |
| 7 | El modelo tonto: bigrama | figura | Tabla de "después de esta palabra, ¿qué viene?" con conteos. Y una muestra generada: sintaxis rota pero palabras reales. | "Con sólo mirar la palabra anterior ya se escribe algo. Malo, pero algo." |
| 8 | Por qué no alcanza | texto | El bigrama no puede saber de qué se estaba hablando hace 10 palabras. | "Necesita contexto. Y para eso ya tenemos la herramienta: la clase pasada." |
| 9 | La arquitectura completa | figura | Diagrama: fichas → embeddings (clase 6) → + posición (clase 7) → 6 bloques transformer (clase 7) → capa final → **distribución sobre el vocabulario**. | "No hay ni una pieza nueva. Todas las vimos. Hoy las apilamos." |
| 10 | La salida es una distribución | figura | Un gráfico de barras con las 10 fichas más probables después de un prompt, sumando ~100%. | `[CALLBACK DIBUJO]` "Miren esta figura. **Esto es lo que el modelo dibuja.** En la clase 1 dibujábamos una recta. Hoy, esto, en cada posición." |
| 11 | La loss: cross-entropy | figura | En castellano: "qué probabilidad le diste a la respuesta correcta". Alta probabilidad = poca pérdida. | "Es la loss de la clase 3 con otra fórmula. Castiga estar confiadamente equivocado más que estar dudando." |
| 12 | Bloque práctico 1: a entrenar | texto | Consignas y advertencia de tiempo. | "Arranquen el entrenamiento AHORA y déjenlo corriendo. Vamos a estar mirándolo toda la clase." |
| 13 | Paso 0 | figura | Muestra generada antes de entrenar: ruido puro. | |
| 14 | Paso 500 | figura | Sopa de letras con espacios en lugares plausibles. | "Ya aprendió que existen los espacios y que las palabras tienen cierto largo." |
| 15 | Paso 2000 | figura | Palabras reales, sintaxis rota. | "Ahora hay palabras del castellano. Nadie le dio un diccionario." |
| 16 | Paso 5000 | figura | Frases con estructura, cadencia parlamentaria, fórmulas de cortesía. | "Y ahí está el tono. Aprendió el **género discursivo**." |
| 17 | La curva de loss | figura | La curva bajando, con los cuatro puntos anteriores marcados. | "Es la misma curva de la clase 4. Mismo gráfico, misma lectura." |
| 18 | **La traducción** | portada de sección | En grande: "Todo lo que te vuelve loco de ChatGPT, explicado". | "Este es el bloque por el que hicimos las siete clases anteriores." |
| 19 | 1. Por qué **alucina** | texto+figura | La salida es **siempre** una distribución. No hay casillero "no sé". No hay base de datos que consultar. El modelo produce lo **plausible**, y lo verdadero y lo plausible coinciden la mayoría de las veces, que es lo que hace tan peligrosa la excepción. | "No miente: mentir requiere saber la verdad. Produce texto plausible, y eso es todo lo que hace siempre, también cuando acierta." |
| 20 | **Hacelo alucinar** | VIZ | `viz/por-que-alucina.html`. | Le pregunta al mini-GPT por un diputado que no existe en Aguasclaras. Responde con total soltura. **Al lado, la lista real de diputados del corpus.** "Miren: se lo inventó. Y miren la distribución: estaba **segurísimo**." |
| 21 | La confianza no es conocimiento | figura | Dos distribuciones: una afilada sobre una respuesta correcta, otra afilada sobre una inventada. Visualmente **idénticas**. | "No hay manera de distinguirlas mirando la salida. Por eso no podés usar la seguridad del modelo como señal de verdad." |
| 22 | 2. Por qué le importa tanto el **prompt** | texto+figura | El prompt es literalmente el condicionante de la distribución. Cambiar el prompt cambia la región del espacio de texto en la que el modelo se mueve. | "No es que 'entienda mejor la instrucción'. Es que le cambiaste el punto de partida a la máquina de completar." |
| 23 | Demostración | figura | El mismo mini-GPT con dos prompts distintos ("Señor presidente," vs "El diario informó que") produciendo dos registros completamente distintos. | "Mismo modelo, mismos parámetros. El prompt eligió el género." |
| 24 | 3. Qué es la **ventana de contexto** | texto+figura | La atención mira a todo lo que está en la ventana, y a **nada** de lo que quedó afuera. No hay memoria fuera de la ventana. | "Lo que se cayó de la ventana no existe. No es que 'se olvidó': nunca estuvo." |
| 25 | **Perdé el contexto** | VIZ | `viz/ventana-de-contexto.html`. | Va corriendo la ventana sobre un texto largo. Cuando el sujeto queda afuera, la predicción se rompe. "Esto es por qué tu prompt larguísimo se olvidó de la primera instrucción." |
| 26 | Por qué la ventana no es infinita | texto | El costo de attention crece con el **cuadrado** de la longitud: el doble de texto, cuatro veces el cómputo. | "Este es el problema nuevo que introdujo attention, el que quedó anotado en el cuestionario de la clase pasada." |
| 27 | 4. Qué hace la **temperatura** | texto+figura | La distribución se afila (T baja) o se aplana (T alta) antes de sortear. La temperatura **no cambia lo que el modelo sabe**: cambia cuánto se arriesga al elegir. | "T=0: siempre lo más probable, repetitivo y aburrido. T=1.5: creativo y delirante. No hay una 'buena': depende de la tarea." |
| 28 | **Movela** | VIZ | `viz/temperatura.html`. | Mueve el slider y genera. "Miren las barras aplastarse. Y miren el texto que sale." |
| 29 | Por qué el mismo prompt da respuestas distintas | texto | Porque hay un **sorteo**. Si querés reproducibilidad: T=0 y semilla fija. Y eso hay que reportarlo en un paper. | "Si en tu metodología usaste un LLM y no reportaste temperatura ni semilla, tu análisis no es reproducible. Anotenlo, va en la clase 10." |
| 30 | 5. Por qué **cuenta mal las letras** | VIZ | `viz/contar-letras.html`, con `viz/tokenizador.html` de la clase 6 reabierta al lado. | "¿Se acuerdan de la siembra de la clase 6? Acá está la cosecha. El modelo nunca vio letras: vio fichas. Preguntarle cuántas R tiene 'ferrocarril' es como preguntarle a alguien que lee en bloques cuántas curvas tiene la tinta." |
| 31 | Y por qué es malo con la aritmética | texto | Los números también se parten en fichas de maneras raras ("1.234" puede ser 3 fichas). No hay una unidad aritmética adentro: hay predicción de texto. | "Cuando acierta una cuenta es porque la vio escrita muchas veces, no porque la calculó." |
| 32 | 6. Por qué a veces se **contradice** | texto | No hay un estado interno de creencias que se mantenga. Cada ficha se genera condicionada al texto anterior; si el texto anterior lo lleva para otro lado, va para otro lado. Y una vez que dijo algo, ese algo condiciona lo que sigue (por eso se "va" por un camino equivocado y no vuelve). | "No tiene opiniones que sostener. Tiene una distribución que actualizar." |
| 33 | 7. Por qué **repite** con T baja | texto | Bucles de alta probabilidad: la ficha más probable después de X es Y, y después de Y es X. | "Es un pozo de probabilidad. Como un mínimo local, pero de texto." |
| 34 | Bloque práctico 2 | texto | Consignas: jugar con temperatura, romper el contexto, hacerlo alucinar, contar letras. Y el desafío: **escribí el prompt que rompe el modelo**. | "25 minutos. Rómpanlo y expliquen por qué se rompió." |
| 35 | Qué le falta para ser ChatGPT | texto | Tres cosas: (1) **escala** (~1,5M vs cientos de miles de millones de parámetros; 1 MB vs billones de fichas); (2) **instruction tuning** (enseñarle a responder consignas en vez de sólo completar); (3) **RLHF** (ajustarlo con preferencias humanas para que sea útil e inofensivo). Cada una en dos líneas. | "El paso 2 y 3 son los que lo convierten de 'autocompletar' en 'asistente'. Y son los que introducen otras cosas: la adulación, por ejemplo, sale de ahí." |
| 36 | Qué **no** cambia con la escala | texto | Sigue sin haber casillero de "no sé". Sigue habiendo tokenización. Sigue habiendo ventana finita. Sigue siendo un sorteo. La escala mejora la calidad, no cambia la naturaleza. | "Esto es lo más importante de la clase. Los modelos de 2030 van a ser mucho mejores y van a seguir teniendo estas propiedades." |
| 37 | `[EL LUNES]` | texto | **Para qué sí**: primer pase de codificación con validación humana obligatoria; generar variantes de instrumentos; resumir con el texto fuente a la vista; explorar un corpus. **Para qué no**: como fuente de hechos, citas o referencias bibliográficas; para codificar sin validar; como sustituto de leer. Y: siempre reportar modelo, versión, fecha, temperatura, prompt exacto. | "El prompt exacto va en el apéndice del paper. Es su instrumento de medición." |
| 38 | El puente | texto | "Entrenar uno desde cero cuesta una fortuna y casi nunca es lo que necesitás. Lo que vas a hacer de verdad es agarrar uno que ya entrenó otro y adaptarlo a tu problema. Clases 9 y 10." | |

**Tabla de traducción (versión de referencia para el equipo — debe quedar también en
`notas-docente.md` y como slide de resumen imprimible):**

| Pieza del mini-GPT | Comportamiento de ChatGPT que explica |
|---|---|
| La salida es una distribución de probabilidad, siempre | Alucina; nunca dice "no sé" espontáneamente; suena igual de seguro cuando acierta que cuando inventa |
| Está condicionada por el texto previo | El prompt cambia todo; el rol asignado ("sos un experto en...") cambia el registro; el prompt es un instrumento de medición |
| La ventana de atención es finita | Se olvida del principio de una conversación larga; ignora instrucciones lejanas; hay que repetir lo importante al final |
| Costo cuadrático de attention | Por qué la ventana tiene límite y por qué cuesta más caro un prompt largo |
| Hay un sorteo al elegir la ficha (temperatura) | El mismo prompt da respuestas distintas; T=0 lo hace repetitivo; T alta lo hace delirante; sin semilla no hay reproducibilidad |
| Trabaja con fichas, no con letras | Cuenta mal las letras, falla con rimas y anagramas, se equivoca con aritmética, tiene problemas con idiomas poco representados |
| No hay estado de creencias, sólo condicionamiento | Se contradice; una vez que arrancó por un camino equivocado, sigue por ahí; se le puede "convencer" de cualquier cosa |
| Entrenado para predecir texto plausible | Produce referencias bibliográficas con el formato perfecto y los datos inventados: el formato es lo más predecible que hay |
| Instruction tuning + RLHF encima | Responde consignas en vez de completar; es amable; a veces adula y te da la razón |
| Aprendió del corpus | Reproduce los sesgos del corpus; sabe mucho de lo que abunda en internet y poco de lo que no |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/temperatura.html`
- **Qué se ve.** Arriba, un prompt (elegible). Debajo, un **gráfico de barras horizontales** con las
  15 fichas más probables y sus porcentajes, ordenadas. Abajo, un panel de texto generado.
- **Controles.**
  - Slider de **temperatura** de 0 a 2.0. Las barras se redistribuyen en vivo: a T→0 una barra se
    come todo; a T=2 quedan casi todas iguales.
  - Botón **"generar 50 fichas"**, que produce texto con la temperatura actual.
  - Botón **"generar 5 veces con el mismo prompt"**: muestra cinco salidas en paralelo. A T=0 son
    idénticas; a T=1 son distintas. **Este botón es el que explica la irreproducibilidad.**
  - Selector de prompt (4 prompts del dominio).
  - Toggle "top-k / top-p" con una explicación de una línea (opcional, para los curiosos).
- **Qué tiene que hacer clic.** Que la temperatura **no cambia el conocimiento del modelo**: las
  barras mantienen su orden, sólo cambian sus alturas relativas. Lo que cambia es el riesgo del
  sorteo.
- **Momento aha.** "El orden de las barras no cambia nunca. Entonces la temperatura no lo hace más
  inteligente ni más tonto: lo hace más o menos arriesgado."
- **Implementación.** Se exportan las logits reales del mini-GPT entrenado para ~6 prompts, a JSON.
  El softmax con temperatura se calcula en JavaScript. La generación de 50 fichas puede ser un
  muestreo real usando una tabla de transición precalculada, o texto precalculado para varias
  temperaturas. **Preferible lo primero si el tamaño lo permite.**

### 3.2 `viz/ventana-de-contexto.html`
- **Qué se ve.** Un texto largo (~200 palabras) en pantalla. Una **ventana resaltada** que abarca N
  palabras; lo que queda fuera se muestra en gris muy tenue. En el borde derecho de la ventana, la
  predicción del modelo para la próxima palabra, con sus 5 candidatos.
- **Controles.** Slider de **tamaño de ventana** (8 a 128 fichas). Slider de **posición**. Botón
  "avanzar" que corre la ventana una palabra a la vez.
- **Qué tiene que hacer clic.** Que hay una dependencia concreta (por ejemplo, el género del sujeto
  mencionado al principio determina un adjetivo al final) y que **al achicar la ventana hasta que el
  sujeto queda afuera, la predicción se rompe visiblemente**.
- **Momento aha.** El texto en gris. "Eso que está gris, para el modelo no existe. No es que le
  presta poca atención: no está."
- **Detalle.** Un cartel que aparece cuando la palabra clave sale de la ventana: **"acabás de perder
  la información que hacía falta"**, y las 5 predicciones cambian a la vista.
- **Aplicación práctica explícita.** Un panel al costado que traduce a la práctica: "por eso, en un
  prompt largo, poné las instrucciones importantes **al final**" — con la aclaración honesta de que
  en modelos grandes el fenómeno es más sutil (el famoso *lost in the middle*) pero de la misma
  naturaleza.

### 3.3 `viz/por-que-alucina.html`
- **Qué se ve.** Dos columnas. **Izquierda:** el prompt y la generación del modelo, con las fichas
  inventadas resaltadas en rojo. **Derecha:** **la verdad del corpus Aguasclaras** — la lista real
  de diputados, partidos y leyes que existen en el corpus generador. Abajo, la distribución de
  probabilidad en el momento de la invención, mostrando que el modelo estaba **muy seguro**.
- **Controles.** Cuatro prompts preparados: uno cuya respuesta **está** en el corpus (contesta bien y
  con confianza), uno cuya respuesta **no está** (inventa con la misma confianza), uno ambiguo, y
  uno que pide una cita textual (inventa una cita con formato perfecto).
- **Qué tiene que hacer clic.** Que **no hay diferencia observable** entre el modelo acertando y el
  modelo inventando. La confianza es idéntica.
- **Momento aha.** Alternar entre el prompt 1 y el prompt 2: las dos distribuciones se ven iguales.
  "Si no puedo distinguirlas mirando, entonces no puedo confiar en la seguridad del modelo como
  señal. Nunca."
- **Por qué esto sólo se puede hacer con Aguasclaras.** Tener la verdad del proceso generador es lo
  que permite el panel derecho. Con un corpus real habría que verificar a mano cada afirmación.
  Es el argumento decisivo a favor del corpus sintético y hay que decirlo en clase.

### 3.4 `viz/contar-letras.html`
- **Qué se ve.** Un campo de texto con una palabra. Debajo, tres filas: (1) la palabra como la ve un
  humano, letra por letra, con las "r" resaltadas y contadas; (2) **la palabra como la ve el
  modelo**: las fichas, en cajitas, con sus IDs; (3) la respuesta del modelo a "¿cuántas R tiene?".
- **Controles.** Campo de texto libre. Botones con ejemplos: "ferrocarril", "arroz",
  "irresponsabilidad", "constitucionalidad", y una palabra corta donde el modelo acierta (para
  mostrar que acierta cuando la palabra es una sola ficha frecuente).
- **Qué tiene que hacer clic.** Que la pregunta es literalmente incontestable desde la representación
  que tiene el modelo, salvo que haya memorizado la respuesta.
- **Momento aha.** "Le estoy pidiendo que cuente algo que no puede ver. Es como preguntarle a
  alguien que sólo escuchó una palabra cómo se escribe."
- **Continuidad.** Reusa el mismo tokenizador de `viz/tokenizador.html` de la clase 6, y el panel
  sembrado allí ("volvemos a esto en la clase 8") se cierra acá con un cartel:
  **"prometido en la clase 6, cumplido"**. Ese guiño hace visible el arco del curso.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** ~10 min en CPU con la configuración reducida (bloques=4, d=128,
contexto=128, ~1.5M params, 3000 pasos); ~3 min en GPU T4 con la configuración completa.
**El notebook detecta si hay GPU y ajusta la configuración solo**, imprimiendo qué eligió.
**Dependencias:** torch. Nada más. Es un punto de orgullo: no se usa ninguna biblioteca de NLP.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Objetivo. Advertencia: **la celda 12 tarda; arrancala y seguí leyendo**. | |
| 2 | code | Imports, detección de GPU, elección automática de hiperparámetros, `print` de la configuración elegida y del tiempo estimado. | La estimación de tiempo baja la ansiedad. |
| 3 | code | Carga del corpus (Aguasclaras, ~1 MB de debates parlamentarios). Estadísticas: caracteres, palabras, vocabulario. Muestra un fragmento. | |
| 4 | md | **Fichas.** | |
| 5 | code | Tokenizador a nivel de caracteres (el de Karpathy) **y** el de sub-palabras de la clase 6. Se usa el de caracteres para el entrenamiento (más simple, converge más lindo con poco corpus) y se muestra el de sub-palabras para conectar con la discusión de tokenización. | **Decisión de diseño explícita**: caracteres para entrenar, sub-palabras para explicar el conteo de letras. Hay que ser transparente con esta diferencia en el texto, y explicar por qué los modelos reales usan sub-palabras. |
| 6 | code | Codificar/decodificar. `assert decode(encode(texto)) == texto`. | |
| 7 | md | **El dataset se arma solo.** | |
| 8 | code | Función `get_batch` que corta ventanas al azar y arma `x` (contexto) e `y` (la ficha siguiente en cada posición). **Se imprime un ejemplo mostrando las 8 sub-predicciones que contiene una ventana de 8.** | Momento clave: una ventana de 8 son 8 ejemplos de entrenamiento, no 1. Explica por qué esto es tan eficiente. |
| 9 | md | **El modelo tonto: bigrama.** | |
| 10 | code | Modelo bigrama (una tabla de embeddings, nada más), entrenado 300 pasos, y una generación. | Sale sopa. Es la línea de base. |
| 11 | md | **El modelo completo.** | |
| 12 | code | La clase `MiniGPT`: reusa el `BloqueTransformer` de la clase 7 **importado/copiado literalmente**, con la capa de salida al vocabulario. Conteo de parámetros. | La continuidad con el notebook de la clase 7 tiene que ser literal y señalada. |
| 13 | code | **El entrenamiento.** El mismo training loop de la clase 4, con evaluación en validación cada 500 pasos y **generación de una muestra cada 500 pasos**. | La celda estrella. Las muestras impresas son el espectáculo. |
| 14 | md | Mientras entrena: explicación de la cross-entropy con un ejemplo numérico chiquito. | Contenido para el tiempo muerto, deliberadamente ubicado acá. |
| 15 | code | Gráfico de la curva de loss (train y val). | Callback explícito a la clase 4: "¿hay tijera? ¿estamos calcando?" |
| 16 | md | `TODO 1` — Mirá las muestras de los pasos 0, 500, 2000 y 5000. Describí **qué aprendió** entre cada par. *Pista: mirá primero la longitud de las palabras, después la puntuación, después la estructura de turnos.* | El ejercicio de observación más rico del curso. |
| 17 | md | **Generar con temperatura.** | |
| 18 | code | Función `generar(prompt, max_fichas, temperatura)` con el sorteo explícito (`torch.multinomial`), comentada línea por línea. | Que vean el sorteo escrito. |
| 19 | code | Generar con T = 0.2, 0.8, 1.5 desde el mismo prompt. Imprimir los tres. | |
| 20 | md | `TODO 2` — Encontrá la temperatura más alta con la que el texto sigue siendo legible. Anotala. ¿Cambia según el prompt? | |
| 21 | md | `TODO 3` — Generá 5 veces con el mismo prompt y T=0.8. ¿Son iguales? Ahora poné T=0.01 y repetí. Explicá la diferencia en términos del sorteo. | |
| 22 | md | **La ventana de contexto.** | |
| 23 | code | Generar con el contexto truncado a 8, 32 y 128 fichas y comparar la coherencia. | Se ve degradarse. |
| 24 | md | `TODO 4` — Escribí un prompt donde la información necesaria esté a más de 128 fichas de distancia y mostrá que el modelo falla. *Pista: nombrá algo al principio y preguntá por eso al final, con relleno en el medio.* | Reproduce en su propio modelo lo que sufren con ChatGPT. |
| 25 | md | **La alucinación.** | |
| 26 | code | Prompt sobre un diputado que **sí** existe en el corpus y otro sobre uno que **no**. Se imprimen las dos salidas y **las probabilidades asignadas**, al lado de la lista verdadera. | El corazón del bloque de criterio. |
| 27 | md | `TODO 5 (criterio, el importante)` — Mirá las dos distribuciones. ¿Podrías distinguir, sin conocer el corpus, cuál es la invención? Escribí tres oraciones sobre qué implica esto para usar un LLM como fuente de información en tu investigación. | |
| 28 | md | **Contar letras.** | |
| 29 | code | Tokenizar "ferrocarril" con el tokenizador de sub-palabras y mostrar las piezas. Preguntarle al modelo. | Cierra la siembra de la clase 6. |
| 30 | md | **El desafío de a dos**: escribí el prompt que rompe el modelo de la manera más interesante. Después explicá **por qué** se rompió, en términos de las piezas que vimos. | Se ponen en común los mejores. Actividad de cierre del módulo. |
| 31 | code | Celda libre para el desafío. | |
| 32 | md | **Guardar el modelo** (`torch.save`) para poder usarlo después. Y **exportar las logits** de algunos prompts a JSON para las visualizaciones. | Conecta el notebook con las viz: coherencia total del material. |
| 33 | md | **Para llevarte** + la tabla de traducción completa + puente a la clase 9. | La tabla queda en el notebook para que se la lleven. |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Entonces tiene una base de datos adentro"** | Buscan dónde está guardada la información. | No hay tablas ni documentos: hay un millón y medio de números que definen una función. La información está **destilada** en los pesos, de una manera que no se puede consultar ni editar puntualmente. Por eso no se le puede "corregir un dato". |
| **"Alucina porque le faltan datos"** | Creen que es un problema de cobertura. | Alucina **por diseño**: siempre produce la continuación más plausible. Con más datos alucina *menos seguido*, no *cualitativamente distinto*. Slide 36. |
| **"Si le digo que no invente, no inventa"** | Sobreestiman el control por prompt. | El prompt condiciona la distribución, no instala un verificador. Puede reducir la tasa; no puede eliminar el mecanismo. Se puede demostrar en vivo con el mini-GPT. |
| **"La temperatura lo hace más inteligente/creativo"** | Antropomorfización del parámetro. | Viz 3.1: el **orden** de las barras no cambia. Sólo cambia el riesgo del sorteo. |
| **Confundir alucinación con error** | Todo error se llama alucinación. | Distinción útil: un error es equivocarse en algo que estaba en la distribución; una alucinación es **fabricar** una entidad con confianza. Para el trabajo de investigación, la segunda es mucho más peligrosa porque es verosímil. |
| **"Este modelito no tiene nada que ver con ChatGPT"** | Descreimiento por escala. | La arquitectura es la misma; las diferencias son escala, datos y las dos etapas posteriores. Se dice qué **sí** transfiere (todo lo de la tabla de traducción) y qué no (calidad, conocimiento del mundo, seguir instrucciones). |
| **"Entonces son inútiles para investigar"** | Sobrecorrección escéptica, muy común después de esta clase. | Hay que atajarla explícitamente en la slide 37: son excelentes para tareas donde **la validación es barata y el error es visible** (primer pase de codificación, exploración, reformulación) y pésimos donde la validación es cara (hechos, citas, datos). El objetivo del curso es criterio, no rechazo. |
| **Frustración porque el mini-GPT escribe cosas sin sentido** | Esperaban ChatGPT. | Se anticipa antes de entrenar: "esto va a escribir cosas que suenan a debate parlamentario y no significan nada. Eso es exactamente el punto: **la forma se aprende antes que el contenido**, y en los modelos grandes esa disociación sigue existiendo, sólo que mejor disimulada." |
| **Creer que T=0 elimina la irreproducibilidad** | Reportan T=0 como suficiente. | Ayuda mucho pero no alcanza: cambia la versión del modelo, cambia el hardware, hay no determinismo en la infraestructura. Se retoma en la clase 10. |

---

## 6. Analogías y metáforas de ciencias sociales

- **El género discursivo.** El modelo aprende la **forma** del debate parlamentario antes que
  cualquier contenido: las fórmulas de tratamiento, la estructura de turnos, la cadencia. Cualquiera
  que haya trabajado con análisis del discurso reconoce ahí la noción de género (Bajtín): una
  estructura relativamente estable de enunciados que precede al hablante. El modelo hace visible,
  cuantitativamente, cuánta información hay en la pura forma.
- **El informante que siempre contesta.** Todo el mundo entrevistó alguna vez a alguien que nunca
  dice "no sé": completa, redondea, arma una historia coherente. No miente por maldad: la
  conversación tiene una fuerza de completitud. El LLM es ese informante llevado al extremo, y las
  técnicas de manejo son parecidas: triangular, pedir fuentes, chequear con otro registro.
- **La cita inventada con formato perfecto.** Es el ejemplo más eficaz con esta audiencia. El
  formato de una referencia bibliográfica es **lo más predecible que existe en un texto académico**;
  los datos concretos, lo menos. El modelo produce exactamente lo que se espera: la estructura
  impecable y el contenido inventado. Es una lección sobre qué tipo de regularidad captura.
- **La ventana de contexto y la memoria de la entrevista.** Retoma la analogía de la clase 6, ahora
  con una diferencia importante: la RNN olvida gradualmente; el transformer tiene un **corte
  duro**. Lo que quedó afuera de la ventana no está degradado: no está.
- **La temperatura y la variabilidad del codificador.** Un codificador humano cansado es de alta
  temperatura: más variable, menos predecible. Uno rígido codifica siempre igual y pierde matices.
  Ni un extremo ni el otro es "el correcto"; depende de la tarea. Y —el punto metodológico— si tu
  instrumento tiene variabilidad, tenés que **reportarla**.
- **El prompt como instrumento de medición.** El punto más importante para el `[EL LUNES]`: si
  usaste un LLM para codificar tu corpus, el prompt es tu libro de códigos y va en el apéndice.
  Cambiar el prompt es cambiar el instrumento, y por lo tanto los resultados no son comparables.

---

## 7. Cuestionario: temas a evaluar (12 ítems)

1. **[MC conceptual]** ¿Cuál es el objetivo de entrenamiento de un modelo de lenguaje?
2. **[MC conceptual]** ¿Por qué alucina un LLM? *(Distractor fuerte: "porque le faltan datos sobre
   ese tema".)*
3. **[Qué pasa si]** Ponés temperatura 0. ¿Qué cambia en el texto generado? ¿Y qué **no** cambia
   respecto de lo que el modelo sabe?
4. **[Qué pasa si]** Tu prompt tiene 10.000 palabras y la ventana de contexto es de 4.000 fichas.
   ¿Qué pasa con las primeras instrucciones? ¿Cómo lo mitigarías?
5. **[Leer un gráfico]** Dos distribuciones de próxima ficha (una afilada, una plana). Decir cuál
   corresponde a temperatura alta y qué tipo de texto va a producir cada una.
6. **[Leer un gráfico]** Una curva de loss de entrenamiento y validación de un modelo de lenguaje,
   con tijera visible. Diagnosticar. *(Aplica lo de la clase 4 a un contexto nuevo.)*
7. **[Mecanismo]** Explicá con tus palabras por qué un LLM cuenta mal las letras de una palabra.
8. **[Mecanismo]** ¿Por qué el mismo prompt puede dar dos respuestas distintas? ¿Cómo lo evitarías
   si necesitás reproducibilidad, y por qué eso no alcanza del todo?
9. **[Distinción]** ¿Qué diferencia hay entre el mini-GPT que entrenaste y ChatGPT? Nombrá tres
   diferencias e indicá cuál de ellas es la que lo convierte en "asistente" y no en
   "autocompletador".
10. **[Aplicación]** Querés usar un LLM para clasificar 3.000 titulares según si mencionan protesta
    social. Describí el procedimiento mínimo aceptable para que el resultado sea publicable.
    *(Se busca: prompt fijo y documentado, temperatura 0, muestra validada a mano, métricas de
    acuerdo, reporte de modelo y versión y fecha.)*
11. **[Criterio]** Un colega te dice que le pidió a ChatGPT las diez referencias principales sobre un
    tema y que las va a citar. ¿Qué le decís y por qué? Explicá el mecanismo, no sólo la
    recomendación.
12. **[Criterio / ética aplicada]** Una revista te pide revisar un paper cuyo método es "clasificamos
    5.000 documentos con GPT-4". El paper no reporta el prompt, ni la versión del modelo, ni la
    temperatura, ni validación humana. Escribí tu comentario de revisor: **qué falta, por qué cada
    cosa importa, y qué le pedirías como mínimo para poder evaluar el trabajo.**

---

## 8. Referencias

**Para el estudiante:**
- Karpathy, A., *Let's build GPT: from scratch, in code, spelled out* (video) y el repo `nanoGPT`.
  **Es la fuente de esta clase y hay que citarla como tal.** `[VERIFICAR URL]`
- Jay Alammar, *The Illustrated GPT-2*. `[VERIFICAR URL]`
- Wolfram, S., *What Is ChatGPT Doing... and Why Does It Work?* — largo pero muy accesible; se
  recomiendan las primeras secciones. `[VERIFICAR URL]`

**Para el docente:**
- Bender, E., Gebru, T., McMillan-Major, A. & Shmitchell, S. (2021), *On the Dangers of Stochastic
  Parrots*, FAccT. **Lectura fundamental para el bloque de criterio**, y conviene presentarla con
  matices: el argumento sobre la forma sin referencia es exactamente lo que muestra el mini-GPT.
  `[VERIFICAR]`
- Ouyang, L. et al. (2022), *Training language models to follow instructions with human feedback*
  (InstructGPT) — para la slide 35, la que explica el paso de autocompletador a asistente.
  `[VERIFICAR]`
- Liu, N. et al. (2023), *Lost in the Middle: How Language Models Use Long Contexts* — sustenta el
  panel práctico de la viz 3.2. `[VERIFICAR]`
- Ziems, C. et al. (2024), *Can Large Language Models Transform Computational Social Science?*,
  Computational Linguistics. **La mejor evaluación sistemática existente de LLMs en tareas de
  ciencias sociales**, con la conclusión matizada que este curso sostiene: sirven como asistentes de
  anotación con validación, no como reemplazo. `[VERIFICAR]`
- Sobre reproducibilidad con LLMs en investigación: Barrie, C., Palmer, A. & Spirling, A. (2024),
  sobre la irreproducibilidad de resultados con modelos cerrados y cambiantes. `[VERIFICAR]`
