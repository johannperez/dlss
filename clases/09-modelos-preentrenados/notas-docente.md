# Clase 9 — Notas para quien da la clase

> **Lo primero, antes de cualquier otra cosa.** Esta clase se puede arruinar de una sola
> manera: dedicándole 90 minutos a Hugging Face y 20 a evaluación. Es al revés. La
> biblioteca es el medio; el criterio es el contenido. Si tenés que recortar, recortá
> biblioteca.

---

## 1. El arco narrativo, en diez líneas

1. Ocho clases construyendo la máquina desde adentro. Se terminó lo que podemos entrenar.
2. Tres líneas de código bajan un modelo que costó millones y clasifican tu corpus.
3. Asombro genuino y merecido. **Y de inmediato: ¿cómo sabés que está bien?** Nadie tiene
   la respuesta. Ese hueco es la clase.
4. Por qué funciona: alguien ya le enseñó castellano; vos le enseñás tu distinción.
   Es la jerarquía de la clase 5 con texto.
5. Tres estrategias, y la regla de decisión no es "cuál es mejor" sino
   **"cuántas etiquetas puedo producir"**.
6. La curva lo demuestra con datos medidos: con pocas etiquetas, lo simple gana.
7. Pausa. Cambio de registro.
8. Evaluar de verdad: etiquetar a mano, la matriz con palabras, precisión y recall,
   el umbral, el piso, el techo humano.
9. La trampa: el detector de desinformación que era un detector de chistes. Con los datos
   del curso, medido, no inventado.
10. Tenemos un número bueno. ¿Prueba algo? No. Clase 10.

**La frase que se llevan:** *si dos codificadores no se ponen de acuerdo, no tenés un
problema de modelo: tenés un problema de concepto.*

---

## 2. Plan de tiempos real

**Son 120 minutos y este plan suma 120 exactos**, con las mismas seis casillas del
presupuesto de `PROGRAMA.md`. Las casillas grandes son las que mandan: si un bloque se te
va, lo recortás adentro de su casilla, **no le comés minutos a la siguiente**.

| Min | Casilla | Slides | Qué hacés |
|---|---|---|---|
| **0-10** | **Gancho** | 1-6 | |
| 0-1 | Portada | 1 | El título y nada más. No leas el temario. |
| 1-3 | Dónde quedamos | 2 | Puente desde la clase 8. Que digan ellos qué hicieron. |
| 3-4 | El presupuesto | 3 | Tu mini-GPT contra un modelo grande. Un minuto, no más. |
| 4-7 | **Las tres líneas** | 4 | **Corrélo en vivo si tenés red.** Si no, mostrá la salida guardada. |
| 7-9 | Los resultados | 5 | La tabla de titulares reales. "¿Estos dos están bien?" |
| 9-10 | **La pregunta** | 6 | Votación a mano alzada. No la contestes vos. |
| **10-25** | **Transfer learning** | 7-17 | **La casilla más apretada de la clase. Cronometrala.** |
| 10-12 | Por qué funciona | 7 | El diagrama, con la analogía. |
| 12-13 | Callback clase 5 | 8 | Una frase mientras avanzás. Ya lo vieron. |
| 13-15 | Qué se congela | 9 | Menos perillas = menos datos. Cobra la clase 4. |
| 15-16 | El informante clave | 10 | La metáfora que se llevan. |
| 16-19 | **Las tres estrategias** | 11 | **La tabla de decisión. Pedí que le saquen foto.** |
| 19-21 | A, B y C | 12-14 | Cuarenta segundos cada una. El detalle está en el notebook. |
| 21-22 | **Apuesta** | 15 | Votación. **No la saltees: sin esto la viz que sigue es decoración.** |
| 22-24 | Viz de la curva | 16 | Movela vos, despacio, y leé el cartel de recomendación. |
| 24-25 | Modelos en castellano | 17 | 70, no 95. Una frase. |
| **25-45** | **Manos 1** | 18-19 | |
| 25-26 | Las consignas | 18 | Leelas en voz alta y arrancan. |
| 26-42 | Notebook, secciones 1 a 4 | — | Caminá por el aula. No resuelvas: preguntá. |
| 42-45 | Puesta en común + viz | 19 | La búsqueda semántica **y el botón de falsos positivos**. |
| **45-55** | **PAUSA** | 20 | **En serio. No se toca. Nunca.** |
| **55-75** | **Evaluar de verdad** | 21-29 | |
| 55-56 | Segunda parte | 21 | Cambio de tono. Decí que esta mitad es la que importa. |
| 56-58 | Etiquetá a mano | 22 | Va a haber resistencia. Bancala. |
| 58-61 | La matriz con palabras | 23 | Pizarrón, con un corpus del aula. |
| 61-62 | **Apuesta del umbral** | 24 | Votación. |
| 62-69 | **Viz de la matriz** | 25 | **La viz central de la clase. Siete minutos y no la apures.** |
| 69-71 | Precisión y recall | 26 | Que digan las frases en voz alta, ellos. |
| 71-72 | ¿Cuál te importa? | 27 | Treinta segundos para que escriban su caso. |
| 72-73 | El modelo bobo | 28 | Números reales del notebook. |
| 73-75 | El techo humano | 29 | Acá ellos saben más que el ingeniero. Aprovechalo. |
| **75-100** | **Manos 2 — el proyecto chico** | 30 | |
| 75-77 | Las consignas | 30 | De a dos. Repartí quién hace qué. |
| 77-100 | Notebook, secciones 5 a 11 | — | El grueso: comparación honesta y los 30 errores. (La 12, el kappa, la hacés vos en la slide 29; si a alguna pareja le sobra tiempo, que la corra.) |
| **100-120** | **Cierre** | 31-40 | |
| 100-104 | Resultados del aula | 31 | Que hablen ellos. Manos arriba. |
| 104-109 | **La trampa del corpus** | 32 | **Lo más importante de la segunda mitad.** |
| 109-111 | Mirá los errores | 33 | |
| 111-113 | Qué reportar | 34 | Foto. |
| 113-115 | `[EL LUNES]` | 35 | Foto también. Es lo único que se llevan escrito. |
| 115-116 | Cuándo NO | 36 | El mejor consejo de la clase, en una frase. |
| 116-118 | Qué te llevás | 37 | Tres ideas. Tres, no más. |
| 118-119 | Glosario | 38 | Pasala. Está en `recursos/glosario.md`. |
| 119-120 | Lo que falta + puente | 39-40 | Dejalo incómodo. No lo resuelvas. |

> **Los dos bloques prácticos suman 45 minutos y la exposición 65.** Es la proporción que
> pide la clase: la parte de hacerlo andar es corta, la de saber si anda es larga. Si al
> minuto 25 seguís hablando de Hugging Face, ya te comiste el bloque práctico.

---

## 3. Qué preguntar al aula, y cuándo

| Cuándo | La pregunta | Para qué |
|---|---|---|
| Slide 2 | "¿Alguien se acuerda de la primera muestra que escupió el mini-GPT?" | Medir la distancia recorrida. Levanta el ánimo. |
| Slide 5 | "Si entreno un modelo con estas etiquetas, ¿qué le estoy enseñando a detectar?" | Que descubran solos que la etiqueta mezcla constructos. |
| Slide 6 | **Votación A/B/C.** "¿Cómo sabés que está bien?" | El error productivo. Casi todos votan A o B. |
| Slide 9 | "Si dejo todas las capas libres y tengo 200 ejemplos, ¿qué pasa?" | Que digan *sobreajuste*. Cobra la clase 4. |
| Slide 13 | "¿Quién usó alguna vez un diccionario de términos o LIWC?" | Reconocimiento. Les da autoridad. |
| Slide 15 | **Votación.** "Con 25 ejemplos, ¿cuál gana?" | Sin esta apuesta, la viz siguiente es decoración. |
| Slide 23 | "Alguien con un corpus: ¿qué sería un falso positivo en su caso?" | Traducir la matriz a su dominio. |
| Slide 24 | **Votación.** "Si bajo el umbral, ¿qué pasa?" y "si el fenómeno pasa a ser el 5 %, ¿qué le pasa a la accuracy?" | La segunda es el aha central de la clase. |
| Slide 27 | "Escribí en una línea cuál de los tres casos es el tuyo." | Treinta segundos, mucho rédito. |
| Slide 31 | "¿A quién le ganó la regresión logística?" (manos) | Validar públicamente el resultado "aburrido". |

---

## 4. Las respuestas típicas, y cómo usarlas

**"Leí unos cuantos y tenían sentido."** (Slide 6, opción A — la más votada.)
No la ridiculices: es lo que hace todo el mundo, incluida gente que publica.
Preguntá: *"¿cuáles leíste?"*. La respuesta siempre es "los primeros" o "unos que me
llamaron la atención". Ahí está: **no es una muestra al azar y ya sabías lo que buscabas.**
Es el mismo error que ellos ya saben detectar en una encuesta mal muestreada. Decilo así.

**"El paper del modelo reporta 0,92."** (Opción B.)
Preguntá tres cosas: ¿en qué corpus?, ¿en qué idioma?, ¿para qué tarea? La respuesta es
"otro, inglés, otra". Esa métrica es un dato sobre *ese* experimento, no sobre el tuyo.
Analogía que funciona: *"un test diagnóstico validado en una población no está validado en
otra. Ustedes ya saben esto."*

**"Sobreajusta."** (Slide 9.) Perfecto, seguí: "¿y cómo lo evito con 200 ejemplos?".
Van a llegar solos a "usar menos parámetros". Congelar es exactamente eso.

**"La sofisticada."** (Slide 15, la apuesta.) Es la respuesta mayoritaria y es la
equivocada, y por eso la viz funciona. Cuando vean 0,14 contra 0,45, dejá tres segundos de
silencio antes de explicar.

**"Baja."** (Slide 24, ¿qué le pasa a la accuracy con prevalencia 5 %?) También mayoritaria
y también equivocada. Sube, o se queda igual mientras la precisión se derrumba. Es el
momento más rentable de la clase entera.

**"¿Entonces para qué sirve la accuracy?"** (Aparece siempre después de la viz.)
Respuesta honesta: para clases balanceadas y para nada más. En el 90 % de los problemas de
ciencias sociales las clases están desbalanceadas. Por eso el curso mira F1 y, sobre todo,
precisión y recall por separado.

---

## 5. Las confusiones de principiante, y cómo desarmarlas

**"Anda porque la salida tiene sentido."**
Desarme: mostrá que cinco casos elegidos por uno mismo no son una muestra. Exigí la
muestra al azar etiquetada a ciegas. Si insisten, preguntá cuántos casos harían falta para
distinguir un modelo del 70 % de uno del 85 % — nadie lo sabe de memoria, y eso ya prueba
el punto.

**Accuracy = desempeño.**
Desarme: la viz de la matriz con el slider de prevalencia. Es la lección más transferible
de la clase, y funciona porque el número *sube* mientras el modelo empeora para su
propósito.

**Confundir precisión con recall.**
Desarme: prohibido decir el número sin la frase. Hacelos hablar. Si no pueden decir
*"de cada 100 que el modelo llamó X, N lo eran"*, no lo entendieron. La función
`g.frase_de_metricas()` del paquete del curso las escribe sola; mostrala.

**"El modelo es mejor que los codificadores humanos."**
Desarme: el techo del acuerdo humano. Un modelo que supera claramente el kappa
inter-codificador está midiendo otra cosa, o hay fuga. Casi siempre es fuga.

**Modelos en inglés sobre texto en castellano.**
Es frecuentísimo porque son los que aparecen primero en los tutoriales. Si tenés red,
la demo en vivo (misma oración, dos modelos) es la manera más rápida de terminar la
discusión.

**Fine-tuning como opción por defecto.**
Desarme: la viz de la curva y la tabla del notebook. Con pocos datos pierde, y siempre
cuesta más. Que lo vean medido, no dicho.

**"Zero-shot no necesita validación porque no entrené nada."**
Desarme: hay que validar **más**, no menos. Y probar cinco prompts y quedarse con el mejor
*en el test* **es** ajustar contra el test. Es exactamente el pecado de la clase 4 con
otra ropa.

**Etiquetar mirando la predicción del modelo.**
Desarme: es el mismo principio del doble ciego, y por el mismo motivo. Contamina el patrón
de referencia hacia el acuerdo. Regla explícita, dicha en voz alta: **se etiqueta antes de
ver nada.**

**"Usamos BERT."**
Desarme: los modelos se actualizan y se despublican. Citar un modelo sin versión es citar
un libro sin edición. Hay que fijar el identificador exacto y la revisión (el hash del
commit). Se retoma en la clase 10.

---

## 6. Si vas atrasado/a

Se recorta **en este orden**, y no se improvisa:

1. **Slide 8 (callback clase 5).** Se dice en una frase mientras avanzás: "es la misma
   jerarquía que vieron con imágenes". −2 min.
2. **Slide 27 (¿cuál te importa más?).** Se menciona sin desarrollar. −3 min.
3. **Slide 12 (el código de la estrategia A).** Ya está en el notebook y lo van a correr.
   −3 min.
4. **Bloque práctico 2: sacá el punto 2 (la curva).** Ya la vieron en la viz. −6 min.
5. **Slide 31 (resultados del aula).** Doloroso, pero se puede pasar a un mensaje escrito
   después de clase. −4 min.

**Lo que NUNCA se recorta, pase lo que pase:**

- **La pausa.** Diez minutos. La segunda mitad es la importante y necesitan cabeza.
- **La viz de la matriz de confusión con el slider de prevalencia** (slide 25). Si sólo
  te queda tiempo para una cosa de toda la segunda mitad, es esta.
- **La trampa del corpus** (slide 32). Es la clase entera condensada, con datos reales.
- **Las dos apuestas** (slides 15 y 24). Sin la predicción fallida, las viz son decoración.
- **El `[EL LUNES]`** (slide 35). Es lo único que se llevan escrito.

---

## 7. Si vas adelantado/a

- **Corré el pipeline en vivo** sobre los cuatro titulares de la slide 5 y comparalo con
  la tabla. Diez minutos de oro, si tenés red.
- **La demo inglés vs castellano**: la misma oración por un modelo en cada idioma.
- **Abrí la viz de la matriz en el fenómeno "protesta"** y rehacé el ejercicio con otra
  prevalencia. Cambian todas las frases y se ve que la matriz se lee distinto según qué
  medís.
- **En la viz de la curva, cambiá la tarea a Covid-19** y dejá que discutan cinco minutos
  por qué ahí el diccionario gana. Es una discusión buenísima sobre operacionalización.
- **Pedí que alguien lea en voz alta sus 30 errores del TODO 6.** Suele salir algo que
  vale más que media clase.

---

## 8. Chistes y analogías que funcionan

- **El informante clave.** Sabe muchísimo, te ahorra meses, y tiene su posición y sus
  puntos ciegos. Se lo usa, se lo cita con precisión y se lo triangula. *"Nadie publicaría
  una etnografía diciendo «me lo contó un tipo». Tampoco publiques «usamos BERT»."*
- **El equipo de codificadores.** El fine-tuning es entrenar un codificador: le mostrás
  ejemplos, aprende tu libro de códigos, y codifica el resto. Todo lo que ya saben sobre
  codificación humana aplica tal cual.
- **El café.** "Tu mini-GPT costó el café que te tomaste mientras entrenaba."
- **El test diagnóstico y la enfermedad rara.** Para el slider de prevalencia: detectar
  algo raro con un instrumento imperfecto produce mayoritariamente falsos positivos. Tiene
  un siglo de epidemiología detrás y ellos ya lo conocen de otra materia. Esto no es una
  analogía: es literalmente el mismo teorema.
- **El detector de chistes.** "Entrenamos un detector de desinformación y nos salió un
  detector de sátira mexicana. Con un F1 lindísimo."
- **La lista de palabras del martes.** "El diccionario lo escribiste vos un martes. Sacale
  «gobierno» y volvé a correr: la conclusión se mueve." Es la clase 1, sembrada, cobrada.
- Cuidado con uno: **no digas "esto es fácil"**. El que no lo logre la va a pasar peor.

---

## 9. Si te preguntan X

**(1) "¿Esto no es hacer trampa? Que el modelo ya sepa castellano, ¿no contamina mi
análisis?"**
Pregunta excelente y hay que tomarla en serio. Sí contamina, y hay que decirlo en el
paper. El modelo trae supuestos sobre el idioma que aprendió de un corpus que no elegiste
vos —mayoritariamente web, mayoritariamente de ciertos países, de cierta época. Eso
condiciona qué distinciones le resultan fáciles. La respuesta honesta no es "no pasa
nada": es **"pasa, y por eso la validación se hace contra etiquetas humanas propias, no
contra la reputación del modelo"**. Y por eso se cita el modelo con su versión: para que
otro pueda auditar de dónde vino ese supuesto.

**(2) "¿Cuántos casos tengo que etiquetar? Decime un número."**
Para *evaluar*: 200-300 al azar. Con menos de 100, el intervalo de confianza de tu F1 es
tan ancho que no distinguís 0,70 de 0,85, y entonces no podés afirmar nada.
Para *entrenar*: la curva del notebook lo contesta con tus datos, y en el corpus del curso
la mejora se aplana bastante antes de las 400. Regla práctica: **300 para evaluar, y
después mirá la curva para decidir cuántas más para entrenar.**

**(3) "¿Puedo usar ChatGPT para etiquetar mis datos y ahorrarme la codificación?"**
Podés, y mucha gente lo hace. Tres condiciones, no negociables:
(a) igual tenés que etiquetar a mano una muestra para *evaluar* al LLM — no te ahorra la
validación, te ahorra el volumen;
(b) el LLM es un codificador con sesgos desconocidos y no reproducibles entre versiones,
así que fijás modelo, versión y prompt y los publicás;
(c) lo reportás como lo que es —"las etiquetas las produjo un modelo"— y no como si fueran
codificación humana. El caso ejemplar está en `datos/README.md` §1.4(d): un corpus del
curso trae columnas de sentimiento que **son la salida de un modelo**, y si alguien las usa
como variable dependiente sin decirlo, cometió justo el error que la clase 10 intenta
evitar.

**(4) "Mi corpus tiene 800 documentos. ¿Vale la pena todo esto?"**
Probablemente no, y decirlo es parte de tu trabajo. Con 800 documentos, leerlos toma unas
veinte horas y vas a entender muchísimo más. El clasificador se justifica cuando el corpus
es tan grande que leerlo es imposible **y** cuando la categoría es lo bastante nítida para
que dos personas coincidan. Si te falta cualquiera de las dos, la herramienta no es la
respuesta. (Slide 36.)

**(5) "¿Cómo le explico esto a un revisor que no sabe nada de deep learning?"**
Con la sección de métodos de la slide 34 y una tabla de tres filas: el piso, tu modelo, y
el acuerdo entre codificadores humanos. Un revisor que no sabe de redes entiende
perfectamente "el modelo bobo saca 0,72 y el nuestro 0,78" y "nuestros dos codificadores
coincidieron en el 73 % de los casos". La clave es que **ninguna de las tres filas requiere
saber qué es un transformer.** Y si el revisor pregunta por qué usaste esto y no un
diccionario, tenés la curva medida para contestarle.

**(6) "El modelo me da 0,95 de F1. ¿Está bien o está mal?"** (Aparece siempre.)
Sospechá. En serio. Con texto real y una categoría social interesante, 0,95 es raro. Las
tres causas por orden de frecuencia: fuga de datos (algo del test se coló en el train),
una etiqueta circular (la etiqueta se derivó de las mismas palabras que el modelo ve — es
literalmente el caso del corpus Aguasclaras, `datos/README.md` §1.5(e)), o un atajo como
el de la sátira. La prueba barata: partí por grupo y mirá si se cae.

---

## 10. Cosas de producción que conviene saber

- **Hugging Face no se pudo probar** en el contenedor donde se construyó este material
  (`huggingface.co` da 403; ver `datos/README.md` §2). En consecuencia:
  - El **camino B** (embeddings PPMI+SVD propios + scikit-learn) está corrido y verificado
    entero: el notebook completo corre de punta a punta **en menos de dos minutos** en CPU
    y sin red. Cinco corridas medidas con `nbconvert --execute`: **19, 20 y 21 segundos**
    con la máquina libre, y 58 s y 1 min 49 s con la máquina cargada. O sea: **contá
    medio minuto si estás sola/o en la máquina y hasta dos minutos si el aula entera está
    corriendo cosas.** El grueso de ese tiempo es levantar el kernel e importar torch; el
    cómputo propio del notebook es poco: construir los embeddings con numpy tarda **4 s**
    y la curva de etiquetas entera, **3 s** (los dos números los imprime el propio
    notebook con `utils.medir_tiempo`).
  - El **camino A** está escrito con cuidado y **no ejecutado**. Las celdas están marcadas
    `# ── CAMINO A ──`.
  - El identificador `pysentimiento/robertuito-sentiment-analysis` está **verificado
    contra el código fuente** de la biblioteca (`pysentimiento/analyzer.py`), no contra el
    servidor de modelos. Los de BETO (`dccuchile/bert-base-spanish-wwm-uncased` y
    `-cased`) están verificados contra el README oficial del repositorio. Y el de
    embeddings de oración, `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`,
    está verificado contra la documentación oficial de `sentence-transformers`
    (`docs/sentence_transformer/pretrained_models.md`, bajado con `curl`, línea 140).
    Los tres identificadores existen y están bien escritos; lo que no se pudo probar es
    **bajar los pesos**, porque el Hub está bloqueado acá.
  - **Tarea para quien dé esta clase por primera vez:** correr el notebook en un Colab con
    red, confirmar que los tres modelos bajan, **anotar la revisión exacta de cada uno**
    (el hash del commit en el Hub, que es lo que la slide 34 pide reportar) en
    `referencias.md`, y reemplazar esta viñeta por el resultado. Ojo también con los
    números: los del camino A van a ser **otros —mejores— que los del camino B** que están
    hoy en las slides 28 y 32 y en las viz. Si vas a dar la clase por el camino A,
    volvé a correr `medir-clase09.py` y actualizá los números, o decí en voz alta que
    los de pantalla son los del camino sin red.
- **Todos los números de las slides están medidos**, no estimados. Salen de
  `medir-clase09.py` (que produce `datos-clase09.js`, lo que leen las viz) y del propio
  notebook. Si cambiás el corpus o la semilla, **volvé a correr el script y actualizá las
  slides**: un número inventado en un curso sobre no inventar es el peor error posible.
- **Las tres viz abren con `file://`, sin internet, y sin una sola request externa.**
  Verificado con Chromium interceptando y abortando cualquier `http(s)`.
- **La viz de la matriz de confusión usa 600 casos simulados** con semilla fija. Está
  dicho al pie de la viz y conviene decirlo también en voz alta: sirve para ver la mecánica
  del umbral, no para afirmar nada. Los números sobre datos reales están en el notebook.
- **Los dos codificadores del archivo de kappa son SIMULADOS** y está en el nombre del
  archivo. Repetilo cada vez que aparezca el número 0,46.
