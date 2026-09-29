# Clase 6 — La forma de los datos manda (II): texto, secuencias y embeddings
**Directorio:** `clases/06-texto-secuencias-embeddings/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-5

---

## 1. Narrativa de la clase

Esta es la clase donde el curso llega al material con el que la mayoría de esta audiencia realmente
trabaja: **texto**. Y hay que aprovechar que llegan con una ventaja: ya saben analizar texto. Saben
de codificación, de análisis de contenido, de análisis del discurso, de las trampas de contar
palabras. Lo que no saben es cómo se le da texto a una máquina sin que se pierda todo lo que a
ellos les importa.

Hay dos ideas grandes, y conviene no mezclarlas:

**Idea A: para que una máquina lea, cada palabra necesita un lugar en el espacio.** Y ese lugar no
es arbitrario: se lo gana por la compañía que frecuenta. La hipótesis distribucional de Firth
("conocerás una palabra por la compañía que mantiene") es una tesis sobre el significado que esta
audiencia puede discutir con criterio propio —y debe discutirla, porque de ahí salen tanto la
potencia como los sesgos de todo lo que viene después.

**Idea B: el orden es información, y las técnicas viejas lo tiran a la basura.** Bag-of-words fue
la herramienta dominante en text-as-data por décadas y sigue siendo útil; pero no puede distinguir
quién le hizo qué a quién. Se muestra la limitación sin despreciar la herramienta: LDA y
diccionarios siguen sirviendo, y a veces son mejor elección que un transformer (eso se dice hoy y
se retoma en la clase 10).

El hilo:

1. **La comisión y el ministro.** Dos frases opuestas, un mismo vector. Golpe seco.
2. **De texto a números: el pipeline.** Tokenizar → vocabulario → índices. Y la primera sorpresa
   incómoda: el modelo no ve palabras, ve **pedazos de palabras**. Se muestra con
   "inconstitucionalidad" y con "desfinanciamiento". **Se planta la semilla de la clase 8** (por qué
   no sabe contar letras) sin cobrarla todavía.
3. **One-hot: el absurdo necesario.** Un vector de 50.000 posiciones con un 1. Todas las palabras
   equidistantes: "diputado" está tan lejos de "senador" como de "berenjena". Se ve por qué eso es
   insostenible.
4. **El mapa.** Embeddings: pocas dimensiones, densos, aprendidos. Las palabras que se usan parecido
   quedan cerca. `[CALLBACK DIBUJO]`: hoy dibujamos **el mapa donde viven las palabras**.
5. **La aritmética y el sesgo, juntos.** Los vectores permiten operaciones análogas; y esas mismas
   operaciones revelan sesgos del corpus. **No se presentan como dos cosas separadas: son la misma
   propiedad.** Si el mapa captura regularidades de uso, captura *todas* las regularidades de uso,
   incluidas las que no nos gustan. Y para un cientista social eso puede ser un **hallazgo**: el
   embedding como instrumento de medición de estereotipos en un corpus (Garg et al. 2018,
   Kozlowski et al. 2019). Este es el `[EN TU INVESTIGACIÓN]` más fuerte del curso.
6. **El orden, de nuevo.** Una vez que tenemos vectores por palabra, ¿cómo combinamos una secuencia?
   Promediar (= bolsa de palabras con embeddings: mejor, pero sigue sin orden). Leer en orden
   acumulando memoria (RNN). Y la falla de la RNN: se olvida.
7. **La puerta.** Una oración larga donde el sujeto está a 30 palabras del verbo. La memoria no
   llega. Y la pregunta que abre la clase 7: ¿y si en vez de recordar, **miramos directamente**?

**Advertencia de diseño.** La RNN se cuenta en **10 minutos y no se implementa**. Está en el curso
sólo como motivación del attention. Si el equipo que construye la clase se entusiasma con LSTM y
compuertas, está arruinando la clase.

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-6 | Dos frases con las mismas palabras y sentido opuesto. |
| 10-30 | De texto a números | 7-16 | Tokenizar, one-hot, y por qué hace falta el embedding. |
| 30-50 | Manos 1 | 17 | Notebook: tokenizar el corpus real y construir el vocabulario. |
| 50-60 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 17. |
| 60-78 | El mapa de palabras | 18-25 | Vecinos reales del corpus, aritmética de palabras, el sesgo como instrumento. |
| 78-95 | Manos 2 | 26 | De a dos: buscar vecinos en el corpus propio y anotar lo que sorprende. |
| 95-110 | El orden importa | 27-32 | Bolsa vs secuencia, leer en orden, y la memoria que se olvida. |
| 110-120 | Cierre | 33-36 | El puente a la clase 7, herramientas usables ya, el glosario. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (36 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Texto, secuencias y embeddings | portada | | |
| 2 | Dónde quedamos | texto | La arquitectura como teoría. Imágenes → convoluciones. | "Hoy: ¿qué forma tiene el texto?" |
| 3 | **Dos frases** | figura | "La comisión rechazó al ministro." / "El ministro rechazó a la comisión." | "¿Significan lo mismo?" |
| 4 | Las mismas, en bolsa de palabras | figura | Las dos tablas de frecuencias: **idénticas**. | "Este es el método más usado en análisis cuantitativo de texto en ciencias sociales durante treinta años. Y no puede distinguir quién rechazó a quién." |
| 5 | No es para despreciarlo | texto | Bag-of-words, diccionarios, LDA: qué siguen resolviendo bien y por qué a veces son la elección correcta. | "Nada de lo que viene invalida esas herramientas. Si tu pregunta es 'de qué se habla', contar palabras anda bárbaro. Si tu pregunta es 'quién le hizo qué a quién', no." |
| 6 | El problema del día | texto | Cómo darle texto a una máquina sin tirar el orden ni el significado. | |
| 7 | Paso 1: partir el texto | figura | Una oración partida en tokens con cajitas. | "Se llama tokenizar. Suena técnico y es 'partir en pedacitos'." |
| 8 | ¿En qué pedacitos? | figura | Tres opciones sobre la misma frase: por caracteres, por palabras, por sub-palabras. Con sus vocabularios y sus problemas. | "Por palabras: el vocabulario del español es enorme y siempre aparece una que no viste. Por caracteres: vocabulario chiquito pero secuencias larguísimas. Por sub-palabras: el compromiso que ganó." |
| 9 | **Tokenizá vos** | VIZ | `viz/tokenizador.html`. | Escribe "inconstitucionalidad" y sale partido en 5 pedazos. "El modelo **nunca ve la palabra entera**. Guarden esto: en la clase 8 vamos a explicar con esto por qué ChatGPT cuenta mal las letras." |
| 10 | Paso 2: cada token es un número | figura | Vocabulario con índices. La frase convertida en `[45, 1203, 8, 77]`. | "Ahora es una lista de números. Ya podemos empezar." |
| 11 | Paso 3 (primer intento): one-hot | figura | Un vector de 50.000 ceros con un 1. Dibujado a escala, absurdamente largo. | "Un vector por palabra, del tamaño del vocabulario." |
| 12 | El problema del one-hot | figura | Distancias: "diputado"↔"senador" = √2. "diputado"↔"berenjena" = √2. Todas iguales. | "Para este esquema, todas las palabras son igual de distintas entre sí. No hay ninguna noción de parecido." |
| 13 | **Comparación visual** | VIZ | `viz/one-hot-vs-embedding.html`. | "Izquierda: 50.000 números, casi todos cero. Derecha: 300 números, todos con información." |
| 14 | La idea: darle a cada palabra un lugar | figura | Un mapa 2D con palabras políticas ubicadas: los verbos de acción legislativa juntos, los actores institucionales juntos, los temas económicos juntos. | `[CALLBACK DIBUJO]` "Hasta ahora dibujábamos curvas. Hoy dibujamos un mapa, y las posiciones en ese mapa **son** lo que el modelo sabe del significado." |
| 15 | ¿De dónde salen las posiciones? | texto | La hipótesis distribucional: *conocerás una palabra por la compañía que mantiene* (Firth, 1957). | "Es una tesis fuerte sobre el significado y es discutible. Discutámosla: ¿el significado de una palabra es su uso? Wittgenstein diría que sí. Un semiólogo tal vez matice." |
| 16 | Cómo se aprende | figura | Esquema simple de la tarea: tapar una palabra y hacer que el modelo la adivine desde sus vecinas. Las posiciones son los parámetros que se ajustan. | "Y se ajustan con... el descenso por gradiente de la clase 3. Otra vez. Siempre es lo mismo." |
| 17 | Bloque práctico 1 | texto | Consignas: tokenizar el corpus, vocabulario, coocurrencias. | "25 minutos." |
| 18 | Volvimos | discusión | ¿Qué palabras aparecen juntas en el corpus? | |
| 19 | **El mapa de palabras** | VIZ | `viz/espacio-de-embeddings.html`. | Busca "reforma" y muestra sus vecinos. "Miren quiénes son los vecinos. ¿Les llama la atención alguno?" |
| 20 | Los vecinos cuentan una historia | figura | Tres palabras del corpus con sus 10 vecinos más cercanos, y una lectura sustantiva de cada lista. | "Esto ya es un hallazgo. 'Seguridad' está rodeada de un vocabulario y no de otro, y eso es un dato sobre cómo se habla del tema en este corpus." |
| 21 | Aritmética de palabras | figura | El clásico rey − hombre + mujer ≈ reina, y una versión del dominio: presidente − ejecutivo + legislativo ≈ ... | "No siempre funciona y se exageró muchísimo en la divulgación. Pero cuando funciona, dice algo sobre la estructura del corpus." |
| 22 | **La misma propiedad, el otro lado** | VIZ | `viz/espacio-de-embeddings.html`, panel de sesgo. | Muestra ocupaciones proyectadas sobre el eje género. "Esto no es un error del modelo. El modelo aprendió cómo se usa el lenguaje en el corpus. El sesgo estaba en el corpus, es decir, en nosotros." |
| 23 | Problema... o instrumento | texto | Dos lecturas: (a) si usás el embedding para decidir sobre personas, el sesgo es un daño; (b) si lo usás para **medir**, el sesgo es tu variable dependiente. Garg et al. 2018: 100 años de estereotipos medidos en embeddings entrenados década por década. | "Este es uno de los usos más lindos de esta tecnología en ciencias sociales, y es exactamente lo contrario de lo que la industria considera un problema." |
| 24 | `[EN TU INVESTIGACIÓN]` | texto | Tres cosas concretas: medir similitud entre documentos de tu corpus; encontrar el vocabulario asociado a un concepto; medir cambio semántico entre dos períodos entrenando dos embeddings. | "Con lo de hoy, ya podés medir si el vocabulario de 'seguridad' se acercó al de 'inmigración' entre 2005 y 2020. Eso es una tesis." |
| 25 | Advertencia de validez | texto | Cercanía en el mapa = uso parecido, **no** significado parecido. Los antónimos suelen quedar cerquísima ("guerra" y "paz" aparecen en los mismos contextos). | "Este es el error de interpretación número uno con embeddings, y aparece en papers publicados." |
| 26 | Bloque práctico 2 | texto | Consignas: entrenar embeddings, explorar, medir similitud entre discursos. | "30 minutos." |
| 27 | Y ahora, el orden | texto | Tenemos vectores por palabra. ¿Cómo armamos el vector de una **frase**? | |
| 28 | Opción 1: promediar | figura | El promedio de los vectores de las palabras. Y las dos frases del inicio dando **el mismo promedio**. | "Volvimos al mismo problema. Mejor que contar palabras, pero sigue sin orden." |
| 29 | **Bolsa vs orden** | VIZ | `viz/bolsa-vs-orden.html`. | |
| 30 | Opción 2: leer en orden | figura | Una persona leyendo palabra por palabra con una mochila en la espalda donde va metiendo lo que va entendiendo. | "Esto es una RNN. Lee en orden y arrastra un resumen de todo lo anterior." |
| 31 | **Y se olvida** | VIZ | `viz/memoria-que-se-olvida.html`. | Frase larga, el sujeto a 30 palabras del verbo. "Miren cómo se desvanece la información del principio. La mochila tiene tamaño fijo y se va sobrescribiendo: cada palabra nueva pisa algo de lo viejo." |
| 32 | Las RNN en 30 segundos | texto | LSTM y GRU: variantes con compuertas para olvidar mejor. Fueron el estado del arte hasta 2017. | "No las vamos a implementar. Están acá para que entiendan qué problema vino a resolver lo de la clase que viene." |
| 33 | La pregunta que abre la clase 7 | texto | En grande: **"¿Y si en vez de recordar, miramos directamente?"** | "Cuando ustedes leen 'lo' al final de un párrafo largo, no recuerdan todo el párrafo: **saltan** al sustantivo. Eso es lo que vamos a construir." |
| 34 | El puente | texto | "Clase 7: attention." | |
| 35 | Herramientas que ya podés usar | texto | Mención honesta y breve: spaCy para procesamiento en español, gensim para embeddings, y los modelos preentrenados que vienen en la clase 9. | "No reinventen la rueda en su investigación. Lo de hoy es para entender qué hace la rueda." |
| 36 | Glosario de hoy | texto | token, tokenización, vocabulario, OOV, one-hot, embedding, dimensión, similitud coseno, hipótesis distribucional, bag-of-words, RNN, LSTM, secuencia. | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/tokenizador.html`
- **Qué se ve.** Un campo de texto grande arriba. Debajo, el texto partido en tokens, cada uno en
  una cajita de color (colores alternados para que se vea el corte), con su **ID numérico** debajo.
  Un contador: "23 caracteres → 7 tokens".
- **Controles.** Escribir libremente. Un selector de estrategia: **por caracteres / por palabras /
  por sub-palabras (BPE)**. Botones con ejemplos precargados: una frase corta, "inconstitucionalidad",
  "desfinanciamiento", un párrafo de discurso, una frase con emoji y con números, una palabra en
  guaraní o en inglés (para mostrar cómo se fragmenta lo que el tokenizador no conoce bien).
- **Qué tiene que hacer clic.** Que la unidad del modelo **no es la palabra**, y que palabras largas
  o infrecuentes se parten en pedazos arbitrarios que no coinciden con morfemas.
- **Momento aha.** "'Inconstitucionalidad' son 5 tokens y ninguno es 'constitución'. El modelo no
  ve la palabra: ve pedazos."
- **Detalle crítico.** Debajo, un panel permanente: **"¿Cuántas veces aparece la letra R en esta
  palabra?"** con la palabra tokenizada al lado. La pregunta queda planteada sin responder, con un
  cartel: *"volvemos a esto en la clase 8"*. Es una siembra deliberada, y en la clase 8 esta misma
  viz se reabre para cobrarla.
- **Implementación.** No hace falta un BPE real: se puede implementar un BPE chiquito entrenado
  sobre el corpus del curso y embeber el vocabulario resultante en el HTML como JSON. Debe ser
  **el mismo tokenizador que usa el notebook de la clase 8**, o la demostración pierde fuerza.

### 3.2 `viz/one-hot-vs-embedding.html`
- **Qué se ve.** Izquierda: una barra vertical larguísima de 50.000 celdas (representada
  comprimida, con una lupa que muestra el único 1). Derecha: 300 celdas coloreadas con valores
  continuos. Abajo, la comparación de "cuánta memoria ocupa" y "qué información tiene".
- **Controles.** Selector de palabra (5 palabras del dominio). Al cambiar de palabra: en one-hot
  sólo se mueve el 1; en el embedding **cambia todo el patrón de colores**, y palabras relacionadas
  tienen patrones visiblemente parecidos.
- **Qué tiene que hacer clic.** Que en one-hot no hay información **entre** palabras; en el
  embedding, el parecido es visible a simple vista como parecido de patrón.
- **Momento aha.** Alternar entre "diputado" y "senador": los patrones de la derecha son casi
  iguales. Alternar con "berenjena": es completamente distinto. En la izquierda, los tres cambios se
  ven exactamente igual.

> **De dónde salen los vectores.** No de Hugging Face y no de un archivo bajado:
> de `ssdl.datos.embeddings_ppmi_svd()`, que hace coocurrencia → PPMI → SVD con
> numpy sobre el corpus real de discursos y tarda ~25 s en CPU. Los vecinos ya
> están verificados (`provincias` → misiones, santiago, formosa; `mujeres` →
> hombres, jóvenes, niños; `docentes` → salario, cargos, investigadores). Para la
> viz standalone, **precalculá los vectores y embebelos como JSON adentro del
> HTML**: la viz no puede depender de Python. Ojo con las tildes: el vocabulario
> tiene `educación`, no `educacion`.

### 3.3 `viz/espacio-de-embeddings.html` — **la viz central de la clase**
- **Qué se ve.** Una nube 2D de ~400 palabras del corpus político (proyección precalculada con PCA
  o t-SNE, guardada como JSON en el HTML), con las palabras escritas. Zoom y paneo con el mouse.
  Los clusters se ven a simple vista.
- **Controles y modos:**
  - **Buscador**: escribís una palabra, se resalta y se dibujan líneas a sus 10 vecinos más
    cercanos, con la distancia coseno anotada.
  - **Modo "aritmética"**: tres campos (A − B + C) y se muestra el resultado y sus 5 candidatos más
    cercanos, **con honestidad**: si el resultado es malo, se muestra igual. Un botón "ejemplos que
    funcionan" y otro **"ejemplos que no funcionan"**. Mostrar los fracasos es tan importante como
    los aciertos y protege contra el entusiasmo mágico.
  - **Modo "eje"**: elegís dos palabras que definen un eje (por ejemplo *él*—*ella*, u
      *oficialismo*—*oposición*) y la nube se reordena proyectando todas las palabras sobre ese eje,
      como un ranking horizontal. **Este modo es el que produce el análisis de sesgo y es el más
      valioso para la audiencia.**
  - **Modo "dos épocas"**: dos nubes lado a lado, embeddings entrenados sobre 1990-2000 y sobre
    2010-2020, con una palabra seleccionada y sus vecinos en cada una. Muestra **cambio semántico**.
  - Toggle "mostrar sólo sustantivos / verbos / todo".
- **Qué tiene que hacer clic.** Que la geometría del espacio codifica relaciones sustantivas, y que
  las mismas relaciones que sirven para medir también son las que producen sesgo.
- **Momento aha (doble).** (1) Al buscar una palabra del dominio y ver vecinos que cuentan una
  historia. (2) En modo eje con *él*—*ella*: ver ocupaciones ordenarse. Silencio en el aula.
- **Nota.** El modo "eje" es exactamente la metodología de Kozlowski, Taddy & Evans (2019) y de
  Garg et al. (2018). Hay que decirlo: **"esto que acaban de hacer es la metodología de un paper de
  la American Sociological Review"**. Es el momento de mayor empoderamiento del curso.

### 3.4 `viz/bolsa-vs-orden.html`
- **Qué se ve.** Dos frases con las mismas palabras y sentido opuesto. Debajo de cada una, su
  representación: la tabla de conteos (idéntica, resaltada en rojo) y el promedio de embeddings
  (también idéntico). A la derecha, un panel "lo que un humano entiende" con los roles marcados
  (quién es agente, quién es paciente).
- **Controles.** Un selector de pares de frases (5 pares del dominio político y periodístico,
  incluyendo un caso de negación: "el proyecto fue aprobado" / "el proyecto no fue aprobado", donde
  la bolsa de palabras difiere en un solo token y el sentido se invierte completamente).
- **Qué tiene que hacer clic.** Que la información perdida es **exactamente la que le importa a un
  cientista social**: agencia, atribución de responsabilidad, negación.
- **Momento aha.** El caso de la negación: "difieren en un token de 12 y significan lo opuesto. Un
  método que pesa todas las palabras igual va a decir que estos dos documentos son casi idénticos."

### 3.5 `viz/memoria-que-se-olvida.html`
- **Qué se ve.** Una oración larga (35 palabras) que se lee de izquierda a derecha con un cursor
  animado. Sobre cada palabra, una **barra de "cuánto queda de esta palabra en la memoria"** que se
  va achicando a medida que el cursor avanza. Al llegar al final, la palabra clave del principio
  tiene una barra casi invisible.
- **Controles.** Botón "leer". Slider de **tamaño de la mochila** (dimensión del estado oculto):
  con una mochila grande el olvido es más lento pero igual ocurre. Botón "mostrar qué necesita el
  modelo acá": resalta la palabra del principio de la que depende la predicción actual.
- **Qué tiene que hacer clic.** Que la información se degrada con la distancia, y que agrandar la
  memoria posterga el problema pero no lo resuelve.
- **Momento aha.** "Para saber si va 'lo' o 'la' necesito la palabra 3, y en la palabra 33 ya casi
  no queda nada de la palabra 3."
- **Nota de honestidad.** Es una **ilustración esquemática**, no una RNN real corriendo. Debe estar
  rotulada como tal. El fenómeno es real; la animación es didáctica.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** < 6 minutos, CPU. **Dependencias:** numpy, matplotlib, torch, (opcional)
scikit-learn para PCA.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Objetivo. Presentación del corpus (rotulado sintético/real). | |
| 2 | code | Carga del corpus de discursos (try/except). Muestra 3 fragmentos y estadísticas: cuántos documentos, cuántas palabras, rango de años. | |
| 3 | md | **Tokenizar.** | |
| 4 | code | Tokenización simple por palabras con una regex, minusculizado, quitando puntuación. Muestra los primeros 30 tokens de un discurso. | Se hace a mano primero. |
| 5 | code | Construcción del vocabulario con `Counter`. Las 30 palabras más frecuentes. Gráfico de la ley de Zipf en log-log. | La curva de Zipf es un regalo: es un hallazgo lingüístico real, es bella, y explica por qué el vocabulario es un problema. |
| 6 | md | `TODO 1` — ¿Cuántas palabras del vocabulario aparecen **una sola vez**? ¿Qué porcentaje del vocabulario son? *Pista: `Counter` te da los conteos; contá cuántos valen 1.* | Suele ser ~50%. Sorprende. Motiva las sub-palabras. |
| 7 | md | **La bolsa de palabras y su límite.** | |
| 8 | code | Vectorizar las dos frases del gancho. Mostrar que los vectores son idénticos con un `assert`. | |
| 9 | md | **Coocurrencias: el mapa a mano.** | |
| 10 | code | Matriz de coocurrencia con ventana de ±4 palabras sobre el corpus. Para 5 palabras elegidas, mostrar con quién coocurren más. | Se ve la hipótesis distribucional funcionando **sin ningún modelo**. Momento importante: los embeddings no son magia, son esto comprimido. |
| 11 | md | `TODO 2` — Elegí una palabra que te interese de tu área y mirá sus coocurrencias. Escribí una oración interpretándolas. | |
| 12 | md | **Embeddings entrenados.** | |
| 13 | code | Entrenar embeddings chiquitos (skip-gram simplificado, 50 dimensiones, en PyTorch, ~2 min) sobre el corpus. **Se muestra el training loop y se señala que es idéntico al de la clase 4.** | La continuidad es el contenido: "no aprendimos nada nuevo sobre entrenamiento; cambió sólo qué predice el modelo". |
| 14 | code | Función `vecinos(palabra, k=10)` con similitud coseno. Se prueba con 5 palabras del dominio. | |
| 15 | md | `TODO 3` — Buscá los vecinos de tres palabras que te interesen. ¿Alguno te sorprendió? *Pista: probá con palabras que tengan carga política.* | |
| 16 | code | Proyección a 2D (PCA) y scatter con las 150 palabras más frecuentes rotuladas. | Su propia versión de la viz 3.3. |
| 17 | md | **Medir similitud entre documentos.** | |
| 18 | code | Vector de documento = promedio de los embeddings de sus palabras. Matriz de similitud entre 20 discursos de años distintos. Heatmap. | |
| 19 | md | `TODO 4 (el de tu investigación)` — ¿Qué dos años tienen los discursos más parecidos? ¿Y los más distintos? ¿Coincide con lo que sabés de la historia política de ese período? *Pista: mirá el heatmap y buscá el máximo fuera de la diagonal.* | Momento donde el conocimiento sustantivo del estudiante vale más que el código. Hay que decírselo. |
| 20 | md | **Sesgo, o medición.** | |
| 21 | code | Definir un eje con dos palabras (`él`/`ella`) y proyectar una lista de sustantivos sobre él. Tabla ordenada. | |
| 22 | md | `TODO 5 (criterio)` — Este resultado, ¿es un defecto del modelo o un dato sobre el corpus? Escribí tres oraciones. ¿Cómo lo reportarías en un paper? *Pista: la respuesta cambia según para qué vayas a usar el modelo.* | |
| 23 | md | **La advertencia.** | |
| 24 | code | Similitud entre pares de antónimos: `guerra`/`paz`, `aprobar`/`rechazar`. Salen altas. | La evidencia contra la sobreinterpretación, en su propia pantalla. |
| 25 | md | `TODO 6` — ¿Por qué "aprobar" y "rechazar" quedan cerca? ¿Qué implica eso para usar similitud coseno como medida de "acuerdo" entre documentos? | El ejercicio conceptual más importante del notebook. |
| 26 | md | **Para llevarte** + puente. | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Cerca en el embedding = significa lo mismo"** | Interpretan similitud coseno como sinonimia o como acuerdo. | Celda 24 del notebook: los antónimos están cerca. Explicación: el espacio codifica **contextos de uso**, y los antónimos comparten contexto. Se repite en la slide 25. Es la confusión más consecuente de la clase. |
| **"El modelo entiende el significado"** | Antropomorfización. | "El modelo sabe con quién sale cada palabra. Eso es mucho y no es entender." |
| **"El sesgo es un bug que hay que arreglar"** | Piden el modelo "sin sesgo". | Se distinguen los dos usos (decidir vs medir) y se aclara que un embedding sin sesgo sería un embedding que no refleja el corpus, es decir, un mal instrumento de medición. La corrección de sesgo tiene sentido en aplicaciones de decisión, y aun ahí es difícil y parcial. |
| **Los tokens no son palabras** | Cuentan tokens y reportan "cantidad de palabras". | Viz 3.1. Y la regla práctica: para español, ~1.3-2 tokens por palabra según el tokenizador. Importa para costos de API y para límites de contexto (clase 8). |
| **"Más dimensiones es mejor"** | Piden 1000 dimensiones. | Más dimensiones = más parámetros = clase 4 otra vez. Con corpus chico, 50-100 dimensiones andan mejor que 300. La lección de capacidad vs datos se aplica igual. |
| **Confundir embeddings de palabra con embeddings de oración** | Promedian y esperan que capture la oración. | Se muestra explícitamente que el promedio pierde el orden (viz 3.4). Los embeddings de oración de verdad llegan en la clase 9 y usan un transformer. |
| **Esperar que la aritmética funcione siempre** | Prueban analogías y se frustran. | El botón "ejemplos que no funcionan" de la viz 3.3. Se dice: la divulgación exageró este resultado; funciona para algunas relaciones frecuentes en el corpus y falla para el resto. |
| **Creer que hay que abandonar bag-of-words** | Descartan sus herramientas previas. | Slide 5, dicha en serio. Para muchas preguntas, un diccionario validado es mejor, más barato y más interpretable. Se retoma en la clase 10. |

---

## 6. Analogías y metáforas de ciencias sociales

- **La hipótesis distribucional como teoría del significado.** Firth 1957, y su parentesco con
  Wittgenstein ("el significado es el uso") y con el análisis del discurso. Es una discusión que
  esta audiencia puede llevar mejor que un ingeniero, y hay que dejarles ese espacio: **la clase
  gana muchísimo si el docente pregunta y escucha en la slide 15**.
- **El embedding como espacio social.** La analogía con el espacio de Bourdieu es tentadora y hay
  que usarla **con una advertencia**: en Bourdieu, las dimensiones se interpretan sustantivamente
  (capital económico, capital cultural); en un embedding, las dimensiones individuales **no
  significan nada**. Lo que significa es la geometría relativa. Hacer esa distinción bien enseña
  algo real sobre los dos lados.
- **El análisis de correspondencias.** Muchos en el aula ya vieron ACM/ACP: proyectar categorías en
  un espacio de baja dimensión a partir de coocurrencias es **exactamente** el mismo gesto. Decirlo
  reduce la ansiedad enormemente: "esto que parece de Silicon Valley lo hace la sociología francesa
  desde los 70".
- **El sesgo como sedimento.** El corpus es un depósito de cómo se habló durante un período. El
  embedding es una técnica para excavarlo. Garg et al. midieron 100 años de estereotipos así.
  Es arqueología del discurso con herramienta nueva.
- **La bolsa de palabras y el análisis de contenido clásico.** Contar menciones es una tradición
  respetable con reglas claras. Su límite —la agencia, la negación, la ironía— es un límite
  conocido en la disciplina desde siempre. Lo nuevo no es el diagnóstico: es la herramienta.
- **La memoria de la RNN y la memoria de la entrevista.** Cuando alguien narra una historia larga,
  el detalle del principio se degrada y queda una síntesis. La RNN hace lo mismo, y por eso falla
  cuando la pregunta depende de un detalle lejano.

---

## 7. Cuestionario: temas a evaluar (12 ítems)

1. **[MC conceptual]** ¿Qué es un token y por qué no siempre coincide con una palabra?
2. **[MC conceptual]** ¿Cuál es el problema principal de la representación one-hot?
3. **[MC conceptual]** ¿Qué captura un embedding? *(Distractor fuerte: "el significado del
   diccionario".)*
4. **[Qué pasa si]** Entrenás embeddings sobre discursos de 1950 y sobre discursos de 2020. ¿Esperás
   que "familia" tenga los mismos vecinos? ¿Qué medirías con esa diferencia?
5. **[Qué pasa si]** Tu corpus tiene 200 documentos cortos. ¿Qué problema vas a tener al entrenar
   embeddings propios y qué alternativa tenés? *(Usar preentrenados: se anticipa la clase 9.)*
6. **[Leer un gráfico]** Una proyección 2D de embeddings con cuatro clusters. Nombrar cada cluster
   e identificar **una** palabra mal ubicada, explicando una hipótesis de por qué.
7. **[Leer una tabla]** Una tabla de similitudes coseno entre 5 documentos. Identificar el par más
   parecido y decir qué **no** se puede concluir de esa similitud.
8. **[Interpretación]** "Guerra" y "paz" tienen similitud coseno 0.82. Explicá por qué, y qué
   implica para usar la similitud como medida de acuerdo político entre documentos.
9. **[Aplicación]** Querés medir si el discurso sobre inmigración se volvió más securitario entre
   2000 y 2020. Describí en cuatro pasos cómo lo harías con lo de hoy.
10. **[MC]** ¿Por qué una RNN tiene problemas con dependencias largas?
11. **[Conceptual]** ¿Qué información pierde el promedio de embeddings de una frase, y por qué esa
    información le importa a un cientista social? Dar un ejemplo propio.
12. **[Criterio / ética aplicada]** Una empresa usa embeddings entrenados sobre CVs para rankear
    candidatos. Un embedding muestra que ciertas ocupaciones están más cerca de nombres masculinos.
    (a) ¿De dónde viene ese sesgo? (b) ¿Alcanza con "quitarle el género" a los datos? (c) ¿Cambia tu
    respuesta si en vez de rankear candidatos, el objetivo fuera **estudiar** la segregación
    ocupacional? Justificá. *(Se busca: el sesgo viene del corpus; quitar el género explícito no
    alcanza porque queda codificado en proxies; y el mismo instrumento es dañino para decidir y
    valioso para medir.)*

---

## 8. Referencias

**Para el estudiante:**
- Kozlowski, A., Taddy, M. & Evans, J. (2019), *The Geometry of Culture: Analyzing the Meanings of
  Class through Word Embeddings*, American Sociological Review 84(5). **Lectura central de la
  clase**: es literalmente el modo "eje" de la viz 3.3, hecho investigación. `[VERIFICAR]`
- Garg, N., Schiebinger, L., Jurafsky, D. & Zou, J. (2018), *Word embeddings quantify 100 years of
  gender and ethnic stereotypes*, PNAS. `[VERIFICAR]`
- Jay Alammar, *The Illustrated Word2vec* — el mejor material visual disponible sobre embeddings.
  `[VERIFICAR URL]`

**Para el docente:**
- Grimmer, J., Roberts, M. & Stewart, B. (2022), *Text as Data*. Capítulos sobre representación de
  texto y sobre validación de medidas. **Es el libro de cabecera de este módulo.** `[VERIFICAR]`
- Bolukbasi, T. et al. (2016), *Man is to Computer Programmer as Woman is to Homemaker?* —
  el paper que abrió la discusión de sesgo en embeddings. `[VERIFICAR]`
- Firth, J.R. (1957) para la cita de la hipótesis distribucional. `[VERIFICAR]`
- Rodriguez, P. & Spirling, A. (2022), *Word Embeddings: What Works, What Doesn't, and How to Tell
  the Difference for Applied Research*, Journal of Politics. **Es la mejor guía práctica existente
  para esta audiencia exacta**, incluida la pregunta de cuándo entrenar propios vs usar
  preentrenados. `[VERIFICAR]`
