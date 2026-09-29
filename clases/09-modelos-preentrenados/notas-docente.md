# Clase 9 — Notas para quien da la clase

> **Lo primero, antes de cualquier otra cosa.** Esta clase se puede arruinar de una sola
> manera: dedicándole 90 minutos a Hugging Face y 20 a evaluación. Es al revés. La
> biblioteca es el medio; el criterio es el contenido. Si tenés que recortar, recortá
> biblioteca.

---

## 1. El arco narrativo, en diez líneas

1. Ocho clases construyendo la máquina desde adentro. Se terminó lo que podemos entrenar.
2. Tres líneas de código bajan un modelo que costó mucho más de lo que tenés (semanas de
   TPU para BETO; millones para los grandes) y clasifican tu corpus.
3. Asombro genuino y merecido. **Y de inmediato: ¿cómo sabés que está bien?** Nadie tiene
   la respuesta. Ese hueco es la clase.
4. Por qué funciona: alguien ya le enseñó castellano; vos le enseñás tu distinción.
   Es la jerarquía de la clase 5 con texto.
5. Tres estrategias, y la regla de decisión no es "cuál es mejor" sino
   **"cuántas etiquetas puedo producir"**.
6. La curva lo demuestra con datos medidos: con pocas etiquetas, lo prestado gana, y
   aprender desde cero (nada prestado) pierde feo. Ojo: esa curva no mide fine-tuning.
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
| 113-115 | `[EN TU INVESTIGACIÓN]` | 35 | Foto también. Es lo único que se llevan escrito. Aclarales que es un proyecto de mediano plazo, no tarea para la clase 10. |
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

**"La de más perillas."** (Slide 15, la apuesta.) Es la respuesta mayoritaria y es la
equivocada, y por eso la viz funciona. Cuando vean 0,14 contra 0,45, dejá tres segundos de
silencio antes de explicar. Y cuidá la conclusión: lo que pierde es **aprender sin nada
prestado**, no "los modelos grandes" ni el fine-tuning, que acá no se midió en la curva.

**"Baja."** (Slide 24, ¿qué le pasa a la accuracy con prevalencia 5 %?) También mayoritaria
y también equivocada: en la viz **no se mueve** (0,88; en rigor baja una pizca, de 0,882 a
0,875) mientras la precisión se derrumba de 0,88 a 0,23. Es el momento más rentable de la
clase entera. Si alguien pregunta "¿y en general?": la accuracy es especificidad más
prevalencia por (sensibilidad − especificidad). Según cuál de las dos sea mayor, al bajar la
prevalencia puede subir, bajar o quedarse; en la viz son casi iguales, por eso no se mueve.

**"D, depende del modelo."** (Slide 24, la del umbral.) No la descartes del todo: al bajar
el umbral el recall nunca baja, pero la precisión no es monótona. Tiende a bajar y puede dar
saltitos para arriba (en el notebook se ven, y el propio código los cuenta). Lo que no hay
es un umbral que mejore las dos de forma sostenida.

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
de la clase, y funciona porque el número *no se mueve* mientras el modelo se vuelve inútil
para su propósito (la precisión cae de 0,88 a 0,23).

**Confundir precisión con recall.**
Desarme: prohibido decir el número sin la frase. Hacelos hablar. Si no pueden decir
*"de cada 100 que el modelo llamó X, N lo eran"*, no lo entendieron. La función
`g.frase_de_metricas()` del paquete del curso las escribe sola; mostrala.

**"El modelo es mejor que los codificadores humanos."**
Desarme: el techo del acuerdo humano, **en la misma métrica**. Se calcula el F1 de un
codificador contra el otro (en el archivo del curso, 0,71) y se lo compara con el F1 del
modelo contra uno de ellos. El kappa (0,46) es otra escala: con la regla "si supera el
kappa, hay fuga", hasta el F1 0,65 del notebook sería sospechoso. Un modelo que supera
claramente el F1 humano casi siempre está midiendo otra cosa, o hay fuga. No es imposible
sin trampa (un modelo promedia el ruido de cada codificador), pero es raro y hay que
demostrarlo.

**Modelos en inglés sobre texto en castellano.**
Es frecuentísimo porque son los que aparecen primero en los tutoriales. Si tenés red,
la demo en vivo (misma oración, dos modelos) es la manera más rápida de terminar la
discusión.

**Fine-tuning como opción por defecto.**
Desarme: con datos, y sin exagerar. La curva de la clase **no mide fine-tuning**: compara
vectores prestados contra aprender desde cero (TF-IDF, sin nada prestado). Lo que sí se
midió en la revisión (celda opcional del notebook, MiniLM multilingüe, tres semillas):
el fine-tuning da F1 0,53 con 25 etiquetas, 0,59 con 200 y 0,67 con 800. O sea, parecido a
embeddings + logística, un poco mejor con 400-800, **más inestable** (con 50 etiquetas fue
de 0,22 a 0,57 según la semilla) y más caro de correr. El mensaje honesto: probá primero la
del medio, y si vas a hacer fine-tuning, medilo contra ella con varias semillas.

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
- **El `[EN TU INVESTIGACIÓN]`** (slide 35). Es lo único que se llevan escrito.

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
- **El equipo de codificadores.** Entrenar un clasificador es entrenar un codificador: le mostrás
  ejemplos, aprende tu libro de códigos, y codifica el resto. Todo lo que ya saben sobre
  codificación humana aplica tal cual.
- **El café.** "Tu mini-GPT costó el café que te tomaste mientras entrenaba."
- **El test diagnóstico y la enfermedad rara.** Para el slider de prevalencia: detectar
  algo raro con un instrumento imperfecto produce mayoritariamente falsos positivos. Tiene
  un siglo de epidemiología detrás y ellos ya lo conocen de otra materia. Esto no es una
  analogía: es literalmente el mismo teorema.
- **El detector de chistes.** "Entrenamos un detector de desinformación y nos salió un
  detector de sátira mexicana. Con un F1 lindísimo."
- **La lista de palabras del martes.** "El diccionario lo escribiste vos un martes cualquiera. Sacale
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

- **Los dos caminos, y qué se corrió de cada uno.**
  - El material se construyó en un contenedor donde `huggingface.co` daba 403. Ahí se
    corrió y se verificó entero el **camino B** (embeddings PPMI+SVD propios +
    scikit-learn): sin red, en CPU. Medido en la revisión del 28-09-2026: **6 s** de
    pared con `nbconvert --execute` en una máquina libre (antes se habían medido 19-21 s
    en el contenedor, y hasta dos minutos con la máquina cargada). Contá entre medio
    minuto y dos minutos en el aula.
  - El **camino A** se corrió por primera vez en esa revisión, con red. Terminó sin
    errores. Los modelos quedaron fijados con su revisión exacta en el notebook
    (`REVISION`, sección 1) y en `referencias.md`:
    - `pysentimiento/robertuito-sentiment-analysis` @ `a2cc0f67ebd705c55191e25a05ba23d885fcc09b`
    - `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` @ `e8f8c211226b894fcb81acc59f3b34ba3efd5f42`
    - `dccuchile/bert-base-spanish-wwm-uncased` @ `d1c9c4565c9d6731e57ed7f027b802697bad861e`
      (sólo aparece en el ejemplo de `Trainer`, no se baja).
  - El camino A **baja casi 1 GB** la primera vez (435 MB el de sentimiento y 471 MB el de
    embeddings). Con treinta personas en el mismo wifi, eso pesa. Si la red del aula es
    dudosa, que pongan `FORZAR_CAMINO_B = True` en la sección 1. Con los modelos ya en
    caché, el notebook entero tarda unos 30 s (con la celda opcional de fine-tuning
    prendida).
  - Si una descarga falla a mitad de camino (límite de pedidos, modelo renombrado,
    proxy), las celdas del camino A avisan y caen solas al camino B. Hugging Face avisa
    "unauthenticated requests": es esperable y no rompe nada.
- **Los números del camino A son otros, no "mejores".** Medido en la revisión, tarea
  «¿es una nota sobre política?», el mismo test de 368:

  | | camino B (slides) | camino A |
  |---|---|---|
  | A · embeddings + logística: accuracy / precisión / recall / F1 | 0,78 / 0,59 / 0,72 / **0,65** | 0,77 / 0,56 / 0,78 / **0,65** |
  | curva con 25 / 200 / 800 etiquetas (embeddings) | 0,45 / 0,59 / 0,63 | 0,53 / 0,63 / 0,65 |
  | umbral elegido en validación → F1 en test | 0,50 → 0,65 | 0,55 → 0,67 |
  | desde cero, diccionario, trampa del corpus, kappa | iguales en los dos caminos | |

  O sea: con pocas etiquetas el modelo pre-entrenado ayuda; con las 1103, la misma F1.
  Las slides 26 y 28, la matriz de la slide 23 y las figuras son del camino B. Si das la
  clase con el camino A en vivo, decí en voz alta que los de pantalla son los del camino
  sin red (o proyectá tu corrida).
- **El fine-tuning (celda opcional, apagada).** MiniLM multilingüe, 3 épocas, lr 5e-5, en
  CPU, el mismo test. Tres semillas por tamaño: F1 0,53 (25 etiquetas), 0,39 (50: de 0,22
  a 0,57), 0,58 (100), 0,59 (200), 0,66 (400), 0,67 (800). Con 200 tarda unos 12 s y con
  800, un minuto. Es la evidencia para la discusión de la slide 14: con pocas etiquetas
  no "pierde feo" como aprender desde cero, pero es inestable.
- **Todos los números de las slides están medidos**, no estimados. Salen de
  `medir-clase09.py` (que produce `datos-clase09.js`, lo que leen las viz) y del propio
  notebook. Si cambiás el corpus o la semilla, **volvé a correr el script y actualizá las
  slides**: un número inventado en un curso sobre no inventar es el peor error posible.
  El script es determinista en la misma máquina y con las mismas versiones de las
  librerías (quedan registradas en `meta.versiones`); con otras versiones algún número
  se mueve en el 4.º decimal. Al final chequea que los momentos de las slides 16 y 32
  sigan apareciendo y avisa si no.
- **Corré el notebook sobre una copia**, no adentro del repo: guarda las tres figuras en
  `figuras/` y las pisa (aunque el contenido sea el mismo, cambian los bytes). En Colab no
  importa: es un clon.
- **Las tres viz abren con `file://`, sin internet, y sin una sola request externa.**
- **La viz de la matriz de confusión usa 600 casos simulados** con semilla fija. Está
  dicho al pie de la viz y conviene decirlo también en voz alta: sirve para ver la mecánica
  del umbral, no para afirmar nada. Los números sobre datos reales están en el notebook.
- **Los dos codificadores del archivo de kappa son SIMULADOS** y está en el nombre del
  archivo. Repetilo cada vez que aparezca el número 0,46 (o el F1 humano, 0,71).
- **El corpus son dos épocas.** 971 notas de la recolección de enero a julio de 2018 y 500
  de la de noviembre de 2020 a marzo de 2021; las 192 de Covid-19 están todas en la
  segunda (`datos/README.md` §1.3(e)). El notebook lo muestra en la sección 11.
