# Clase 6 — Notas para quien da la clase

**La forma de los datos manda: texto, secuencias y embeddings**
120 minutos · apertura del módulo de texto · prerrequisitos: clases 1 a 5

> **Esta es la clase más apretada del curso.** 40 slides, cinco visualizaciones y un
> bloque de contenido nuevo *después* del segundo práctico. Leé la sección 6 antes
> de entrar al aula: dice qué se recorta y qué no se recorta nunca.

---

## 1. El arco narrativo en diez líneas

1. Dos frases con las mismas palabras y sentido opuesto. Se cuentan las palabras:
   **la tabla es idéntica**. Golpe seco, y el aula se ríe.
2. Se aclara enseguida que no venimos a despreciar la bolsa de palabras. Media
   sala publicó con diccionarios y con LDA: si arrancás despreciando eso, perdiste.
3. Se arma el *pipeline*: tokenizar → vocabulario → índices. Y la primera sorpresa
   incómoda: **el modelo no ve palabras, ve pedazos**. Se planta la semilla de la clase 8.
4. One-hot, y su absurdo: **todas las palabras están igual de lejos de todas**.
   `diputados` está tan lejos de `senadores` como de `trigo`.
5. La idea del mapa. `[CALLBACK DIBUJO]`: hasta ahora dibujábamos curvas; hoy
   dibujamos **el mapa donde viven las palabras**.
6. Firth y la hipótesis distribucional. **Acá se pregunta y se escucha**: es la
   discusión que esta audiencia puede llevar mejor que un ingeniero.
7. Práctico 1: cuentan a mano. Descubren que **el 45,6 % del vocabulario aparece
   una sola vez** y que las coocurrencias ya cuentan una historia sin ningún modelo.
8. Pausa. Vuelven, y el mapa. Los vecinos de `pobreza` son *indigencia, desocupación,
   inflación, hambre*: **eso ya es un hallazgo, y no lo produjo una teoría**.
9. **La escena de la clase**: modo eje, `mujeres ←→ hombres`. Las palabras se
   ordenan solas. Silencio. Y la frase: *el sesgo estaba en el corpus, o sea, en nosotros*.
10. El orden vuelve a romper todo: promediar da el **mismo vector exacto**, la
    mochila de la RNN (de tamaño fijo) va pisando lo viejo, y queda la pregunta que
    abre la clase 7.

**Si te llevás una sola frase para repetir**: *cerca en el mapa quiere decir que se
usan parecido, no que signifiquen lo mismo.*

---

## 2. Plan de tiempos real, bloque por bloque

| Min | Slides | Bloque | Qué hacés |
|---|---|---|---|
| **0-1** | 1 | Portada | Una frase y pasás. |
| **1-3** | 2 | Dónde quedamos | Dos minutos. Preguntá qué supone una CNN sobre el mundo. |
| **3-5** | 3 | **Las dos frases** | Leelas en voz alta con énfasis distinto. Preguntá y esperá. |
| **5-8** | 4 | La misma bolsa | **Callate cinco segundos** después de mostrar las dos tablas de abajo (las podadas). Si alguien objeta que arriba no son idénticas, tiene razón: ver §4. |
| **8-10** | 5-6 | No despreciar / el problema | La 5 se dice en serio, no como concesión. |
| **10-12** | 7 | Tokenizar | «¿qué se perdió acá?». Salen mayúsculas y puntuación. |
| **12-14** | 8 | Tres estrategias | Preguntá cuál usarían. Casi todos dicen «por palabras». |
| **14-18** | 9 | **VIZ tokenizador** | Escribís vos «inconstitucionalidad», letra por letra. **Sembrás la clase 8.** |
| **18-19** | 10 | Ficha → número | El «ese número no significa nada» es lo importante. |
| **19-22** | 11-12 | One-hot y su problema | Estirá los brazos para el largo del vector. Funciona. |
| **22-25** | 13 | **VIZ one-hot vs embedding** | Alternás vos las tres palabras, despacio y en silencio. |
| **25-31** | 14-16 | **El mapa y Firth** | La 14 en un minuto (callback del dibujo). **La 15 es discusión: tres minutos**, se pregunta y se escucha. La 16 (contar, descontar, comprimir) en dos. |
| **31-51** | 17 | **Práctico 1** | Notebook, secciones 1-4. Pasás por las mesas. |
| **51-61** | 18 | **PAUSA** | Diez minutos. **No se toca.** |
| **61-63** | 19 | Volvimos | Anotás en el pizarrón dos listas que sacaron ellos. |
| **63-69** | 20 | **VIZ el mapa** | Buscás «reforma», después «pobreza», después una que te tiren. |
| **69-71** | 21 | Los vecinos cuentan | Detenete en `docentes`. |
| **71-73** | 22 | Aritmética | Cinco de diez aciertan, una sola sale primera, y el orden de la resta importa. Que «niñas» no entre al vocabulario es un dato. |
| **73-75** | 23 | **LA APUESTA** | Votación a mano alzada, contando los votos en voz alta. |
| **75-80** | 24 | **VIZ modo eje** | **La escena central.** Silencio de cinco segundos. |
| **80-83** | 25-26 | Problema o instrumento + código | La 26 se pasa rápido: es referencia. |
| **83-87** | 27-28 | En tu investigación + la advertencia | En la 27, la vara del ruido al lado del «de 8 siguen 2». |
| **87-104** | 29 | **Práctico 2** | Notebook, secciones 5-10, de a dos. |
| **104-109** | 30-32 | El orden vuelve | La 32 (VIZ bolsa vs orden) es la que engancha. |
| **109-114** | 33-35 | RNN y su falla | **La 35 es lo primero que se recorta.** |
| **114-120** | 36-40 | Cierre | La pregunta, tres ideas, herramientas, glosario, puente. |

> Los minutos de esta tabla son **los mismos que dicen las notas del orador** de cada
> slide en `slides.html`: sumadas, dan 120. Los dos bloques prácticos duran 20 y 17
> minutos, y `PROGRAMA.md` usa los mismos minutos (el segundo práctico en 87-104,
> porque antes entran la apuesta, la viz del eje y la advertencia de validez, que
> no se recortan). No sobra ningún minuto: si una
> discusión se estira (la 15 o la 24, y está bien que pase), recortá según §6.
> El notebook está armado para que la segunda mitad (secciones 8 a 10, una media
> hora) se pueda terminar en casa antes de la clase 7 sin perderse nada.

---

## 3. Qué preguntar al aula, y cuándo

| Momento | La pregunta | Para qué |
|---|---|---|
| Slide 3 | **«¿Significan lo mismo?»** | Que alguien use la palabra *quién*. Anotala en el pizarrón: vuelve en la slide 31. |
| Slide 5 | «¿Quién de acá publicó con diccionarios o con LDA?» | Manos arriba. La clase deja de ser una amenaza a lo que ya saben. |
| Slide 7 | «¿Qué se perdió al partir así?» | Que vean que tokenizar es un libro de códigos, no un automatismo. |
| Slide 8 | «¿Cuál usarían ustedes?» | Casi todos dicen «por palabras». Anotalo: la viz que sigue lo desarma. |
| Slide 12 | «¿Alguien ve el problema del one-hot?» | La carencia hay que **sentirla** antes de mostrar el embedding. |
| **Slide 15** | **«¿El significado de una palabra es su uso?»** | **Un par de minutos de discusión abierta** (la slide tiene tres). Es donde esta audiencia brilla. |
| Slide 19 | «¿Qué les salió a ustedes?» | Que el hallazgo salga de ellos y no de la pantalla. |
| Slide 20 | «¿Les llama la atención algún vecino?» | Y después: «tírenme una palabra». Buscala en vivo, sin preparar. |
| Slide 21 | «¿Qué les dice que `docentes` esté al lado de `salario` y de `piso`?» | Sale solo, y es lectura sustantiva pura. |
| Slide 22 | «¿Qué pasa si invierto la resta?» | Que lo prueben en la viz (botón «la trampa»). Es una decisión de medición: un error de planteo hace que un método parezca peor de lo que es. |
| **Slide 23** | **«¿Dónde cae cada palabra? A, B o C. Voten.»** | Sin esta apuesta, la viz del eje es un dibujito lindo. |
| Slide 24 | *(nada)* | **No preguntes. Callate.** Dejá que hablen ellos primero. |
| Slide 28 | «¿Por qué `importaciones` y `exportaciones` quedan cerca?» | La respuesta la dice el aula, no vos. |
| Slide 32 | «¿Quién tiene una variable que depende de una negación?» | Se levantan manos. Es el puente a su propia investigación. |

---

## 4. Las respuestas típicas, y cómo usarlas

**Slide 3, «¿significan lo mismo?»**
Dicen «no, cambia quién rechaza». Perfecto: escribí **QUIÉN** en el pizarrón y dejalo
ahí toda la clase. En la slide 31, cuando el promedio dé 1,000 exacto, señalalo.

**Slide 4, «pero arriba las dos bolsas no son idénticas»**
Si sale, es el mejor comentario de los primeros diez minutos, y hay que agradecerlo.
En castellano, «al» es «a» + «el», así que el par del gancho difiere en dos artículos.
Ninguna palabra con contenido cambia, y sacar las palabras vacías es lo primero que
hace cualquier pipeline: por eso la slide muestra las dos bolsas podadas, y ahí sí
son idénticas. Si querés el caso sin ningún asterisco, en el notebook (celda de la
sección 3) y en la viz `bolsa-vs-orden` está *«el gobierno criticó al congreso»* /
*«el congreso criticó al gobierno»*: dos sustantivos masculinos, y las bolsas salen
iguales tal cual. **La moraleja es mejor que el ejemplo limpio**: qué tan idénticos
son dos textos depende de las decisiones de preprocesamiento que tomaste vos.

**Slide 15, «¿el significado es el uso?»**
Va a salir alguien que dice que sí (Wittgenstein), alguien que dice que no (hay
referencia, hay intención) y alguien que dice «depende del contexto de enunciación».
**Las tres son buenas y ninguna hay que corregirla.** Cerrá así: *«la máquina ya
decidió que sí, sin preguntarle a nadie. Veamos qué le sale con esa decisión —y
después discutimos qué se le escapa».* Eso convierte la discusión filosófica en el
marco crítico de todo lo que viene.

**Slide 21, «docentes»**
Suele salir: «porque el Estado habla de docentes cuando hay conflicto salarial».
Exactamente. Y ahí metés la vuelta metodológica: *eso es una hipótesis, y ahora
tenés una manera de medirla en un corpus grande. Lo que no tenés todavía es una
manera de validarla, y eso es la clase 10.* Un primer chequeo ya está en el notebook:
entrenando con la mitad del corpus, de las vecinas de `docentes` sobrevive sólo
`mínimo`. La lista es una pista, no un resultado.

**Slide 23, la votación**
Casi siempre gana B. Los que votan A («son palabras neutras») son los que más
aprenden: preguntales, después de la viz, qué los sorprendió. Los que votan C
(«el corpus es oficial y cuidado») te regalan el mejor comentario de la clase:
*el corpus es oficial y cuidado, y el orden sale igual. Justamente por eso.*

**Slide 24, después del silencio**
La primera reacción suele ser incomodidad, y a veces enojo. No la apures y no la
resuelvas. Si alguien dice «entonces el modelo es machista», reformulá sin
corregir: *el modelo aprendió cómo se habló. Si querés, el machista es el corpus.
Y el corpus son treinta y cinco discursos de Estado.* Eso abre la slide 25 sola.

---

## 5. Confusiones de principiante, y cómo desarmarlas

| Confusión | Cómo se manifiesta | Cómo la desarmás |
|---|---|---|
| **«Cerca = significa lo mismo»** | Interpretan la similitud coseno como sinonimia, o peor, como *acuerdo* entre documentos. | Slide 28 y celda de antónimos del notebook: `importaciones`/`exportaciones` da **0,78**. El espacio codifica **contextos de uso**, y los antónimos comparten contexto. **Es la confusión más consecuente de la clase.** |
| **«El modelo entiende»** | Antropomorfización, sobre todo después de ver buenos vecinos. | *El modelo sabe con quién sale cada palabra. Eso es mucho, y no es entender.* |
| **«El sesgo es un bug»** | Piden «el modelo sin sesgo». | Slide 25. Un embedding sin sesgo es un embedding que no refleja el corpus: un termómetro roto. La corrección tiene sentido en aplicaciones de **decisión**, y aun ahí es difícil y parcial. |
| **«Los tokens son palabras»** | Reportan «cantidad de palabras» contando fichas. | Viz del tokenizador. Regla práctica para castellano: **1,3 a 2 fichas por palabra**, según el tokenizador. Importa para el costo de una API y para el límite de contexto (clase 8). |
| **«Más dimensiones es mejor»** | Piden 300 o 1000 dimensiones. | Es la clase 4 otra vez: más dimensiones = más perillas, y con poco texto las dimensiones de más tienden a capturar ruido. Acá no lo medimos: 100 es un valor habitual para un corpus de este tamaño. Si alguien lo quiere defender en su tesis, que pruebe 50, 100 y 300 y mire si cambian las vecinas de sus palabras clave. |
| **Embedding de palabra ≠ de oración** | Promedian y esperan que capture la oración. | Slides 31-32, con el número medido: 1,000 exacto. Los embeddings de oración de verdad llegan en la clase 9 y usan un transformer. |
| **«La aritmética funciona»** (o «no funciona nunca») | Prueban analogías y se frustran, o invierten la resta sin darse cuenta. | Slide 22 y los botones de la viz. De diez, cinco aciertan entre las cinco primeras y una sola sale primera. **Y el orden de la resta importa**: `a − b + c` le aplica a `c` la relación que va de `b` a `a`. Planteadas al revés, seis de esas relaciones aciertan cero. **Decilo antes de que lo descubran solos.** |
| **«Hay que abandonar bag-of-words»** | Descartan sus herramientas previas. | Slide 5, dicha en serio. Para muchas preguntas un diccionario validado es mejor, más barato y más interpretable. Se retoma en la clase 10. |
| **«Todos los discursos son iguales»** | Les da 0,98 de similitud entre todos y concluyen que no hay variación. | Es el momento más pedagógico del notebook. **Es un problema de instrumento, no un hallazgo**: el promedio está dominado por el fondo común. Restás la media y aparece la estructura. |

---

## 6. Si vas atrasado (y vas a ir atrasado)

**Se recorta, en este orden:**

1. **Slide 35, «las RNN en treinta segundos».** Se dice de pie, en dos oraciones,
   sin proyectar. Es contenido de contexto, no de examen.
2. **Slide 22, la aritmética.** Se muestra una sola fila de la tabla
   (`senado − senadores + diputados`, que acierta, y al revés no) y se dice «de diez,
   aciertan cinco, y una sola sale primera». Treinta segundos.
3. **Slide 26, el código.** Es referencia; está en el notebook.
4. **Slide 38, herramientas.** Se menciona de palabra al cerrar.
5. **El práctico 2 baja de 17 a 12 minutos**, y el notebook se termina en casa.
   Avisalo explícitamente: *«las secciones 8, 9 y 10 se terminan en casa antes de la
   clase 7; es una media hora»*. El TODO 5 no tiene minutos en la clase 7: si querés
   discutirlo, usá la puesta en común opcional de diez minutos al abrir la clase 7
   (`recursos/GUIA-DEL-DOCENTE.md` §3); si no, que quede escrito en el notebook.

**NUNCA se recorta:**

- **La pausa** (slide 18). Diez minutos. No es negociable.
- **La apuesta (23) y la viz del eje (24).** Es la escena central de la clase y el
  momento de mayor empoderamiento del curso. Si sólo te queda tiempo para una cosa
  en la segunda mitad, es ésta.
- **La pregunta que abre la clase 7 (slide 36).** Sin ese puente, la clase 7 arranca
  sin motivación y se convierte en una clase de álgebra.
- **La advertencia de validez (28).** Es lo que les evita publicar una barbaridad.

---

## 7. Si vas adelantado

- **Buscá palabras que te tire el aula** en la viz del mapa, modo explorar. Es el
  mejor uso posible de cinco minutos libres, porque nadie lo preparó.
- **Modo «dos épocas» con `seguridad`.** Está en la viz (y aparece en la slide 27):
  1984-1999 → *social, justicia, ministerio, salud*; 2004-2019 → *policía, fuerzas,
  defensa, federal*. **De ocho vecinas, siguen dos.** Y la viz trae la vara: partiendo
  el mismo corpus en dos mitades alternadas, *sin* corte de época, siguen **cuatro**
  (con la misma configuración chica de las épocas: 60 dimensiones, 1.200 palabras).
  Si alguien lo cruza con la celda de estabilidad del notebook, donde `seguridad`
  conserva 2 de 8 entre mitades, no hay contradicción: allá la configuración es la
  completa (100 dimensiones, 2.000 palabras), y la vara sólo vale contra una
  comparación hecha con la misma configuración.
  O sea: hay una pista de cambio, pero la mitad del movimiento ya lo produce el
  ruido de trabajar con 16 discursos. Mostrá las dos cosas juntas: es la lección de
  la clase 10 adelantada. Si te sobran cinco minutos, esto es lo que hacés.
- **Modo eje con `gobierno ←→ oposición`** (está como atajo). Del lado de
  «oposición» caen *senadores* y *diputados*; del lado de «gobierno», *trabajo*,
  *salud*, *derechos* y *trabajadores*. En estos discursos la oposición aparece en
  el Congreso, no en la calle ni en la gestión. Da conversación sobre quién habla y
  desde dónde. (Un eje con `oficialismo` no se puede: aparece 6 veces y no entra al
  vocabulario.)
- Pediles que armen un eje con dos palabras **de su campo**, en voz alta, y probalo
  en vivo. Muchos van a fallar porque la palabra no está en el vocabulario: eso
  también enseña (frecuencia mínima 8, y las tildes cuentan).

---

## 8. Chistes y analogías que funcionan

- **La mochila.** Caminá por el aula haciendo el gesto de meter cosas en una mochila
  chica que ya está llena mientras «leés»: para que entre lo nuevo, algo se cae. Es
  la misma metáfora del glosario (tamaño fijo, se va sobrescribiendo). Es tonto y se
  lo acuerdan seis meses después.
- **«Volvimos al mismo problema, con más decimales»** (slide 31). Se ríen, y después
  entienden que es literal.
- **El análisis de correspondencias.** *«Esto que parece de Silicon Valley lo viene
  haciendo la sociología francesa desde los setenta.»* Baja la ansiedad muchísimo.
  Si hay gente de sociología en el aula, mirala al decirlo.
- **Bourdieu, con cuidado.** El embedding es tentadoramente parecido a un espacio
  social, y la analogía sirve **si la usás con la advertencia**: en Bourdieu las
  dimensiones se interpretan sustantivamente (capital económico, capital cultural);
  en un embedding **las dimensiones individuales no significan nada**. Lo que
  significa es la geometría relativa. Hacer bien esa distinción enseña algo real
  sobre los dos lados.
- **La memoria de la entrevista.** Cuando alguien narra una historia larga, el
  detalle del principio se degrada y queda una síntesis. La RNN hace lo mismo, y por
  eso falla cuando la pregunta depende de un detalle lejano.
- **«Estirá los brazos»** para el largo del vector one-hot. Ridículo y eficaz.
- No hagas el chiste de «la máquina aprendió a ser machista». Convierte una
  discusión metodológica seria en un chiste, y la slide 25 después no entra.

---

## 9. Si te preguntan X

**«¿Esto es lo que usa ChatGPT?»**
Es *el primer paso* de lo que usa ChatGPT, y está desactualizado como técnica.
GPT también convierte cada ficha en un vector —eso no cambió— pero sus vectores no
son fijos: cambian según el contexto de la oración, y eso es lo que vamos a construir
en las clases 7 y 8. El embedding de hoy le da a `banco` un solo vector para «banco de
plaza» y «banco central». Un transformer le da uno distinto en cada oración.
**Lo de hoy no es una versión de juguete: es la pieza sobre la que se construyó todo.**

**«¿Cuántos textos necesito para entrenar mis propios embeddings?»**
Respuesta honesta y con números: acá usamos **350.000 palabras** y los vecinos salen
legibles, pero **la aritmética funciona a medias**, las palabras que aparecen menos de
ocho veces hay que tirarlas, y **con la mitad del corpus las vecinas cambian mucho**
(la celda de estabilidad del notebook lo muestra). Word2vec original se entrenó con 100.000 millones. Regla
práctica: por debajo del millón de palabras, entrenar propios te sirve para
*explorar* tu corpus, no para *medir* con precisión. Si tenés 200 documentos cortos,
no entrenes: usá pre-entrenados (clase 9). Rodriguez & Spirling (2022) es
exactamente el paper que responde esta pregunta con evidencia.

**«¿Cómo justifico esto ante un revisor que no sabe qué es un embedding?»**
Tres cosas, y las tres las tenés hoy. (1) **Decí de dónde salió el mapa**: qué corpus,
qué ventana, qué vocabulario mínimo, qué dimensiones, qué semilla. Es la sección de
métodos y es corta. (2) **Validá contra algo que se pueda leer**: mostrá las listas
de vecinos de cinco palabras clave y dejá que el revisor juzgue si tienen sentido.
Es validación de contenido, y es la más convincente. (3) **Reportá lo que no
funcionó**: si probaste tres ejes y sólo uno dio algo interpretable, decilo.
El revisor 2 quiere saber que no elegiste el resultado después de verlo.

**«Si el sesgo está en el corpus, ¿no habría que limpiar el corpus?»**
Depende de para qué. Si estás construyendo un sistema que **decide** sobre personas,
sí, y aun así es difícil: el género queda codificado en decenas de proxies (nombres,
ocupaciones, verbos) y sacar la palabra explícita no alcanza. Si estás **midiendo**
cómo habló una institución, limpiar el corpus es destruir el dato. Es la misma
diferencia que entre corregir un termómetro y borrar la fiebre del paciente.

**«¿No es circular usar el mismo corpus para entrenar el embedding y para medir?»**
Es una excelente pregunta y la respuesta es: **sí, en parte, y hay que decirlo.**
El embedding es un resumen del corpus; medir sobre él es describir el corpus con
otra herramienta, no testear una hipótesis contra evidencia independiente. Sirve
para **describir** («así se estructuró este vocabulario») y para **comparar**
(dos corpus, dos épocas, dos medios). No sirve para inferir sobre una población
que no está en el corpus. Garg et al. lo resuelven comparando el embedding de cada
década contra datos censales externos: eso sí es validación. Es el modelo a imitar.

**«¿Por qué 100 dimensiones y no 50 o 300?»**
Respuesta honesta: no lo optimizamos. 100 es un valor habitual para un corpus de este
tamaño, y con 100 los vecinos salen legibles; no hay una razón profunda. Es
un hiperparámetro, como la cantidad de rampas de la clase 4, y se elige igual: con
un criterio explícito y validando (por ejemplo, probando 50, 100 y 300 y mirando si
cambian las vecinas de las palabras clave). Lo importante es que **sea una decisión declarada
y no un default heredado**. Con corpus chico, menos dimensiones suele ser mejor: es
exactamente la lección de capacidad contra datos de la clase 4.

---

## 10. Antes de entrar al aula

- [ ] Abrí `viz/espacio-de-embeddings.html` suelta y probá el modo **eje** una vez.
      Es la escena central y no querés descubrir en vivo dónde está el botón.
- [ ] Tené a mano dos o tres palabras del corpus para buscar en vivo si el aula no
      tira ninguna: `reforma`, `pobreza`, `derechos`.
- [ ] Corré la primera celda del notebook en la máquina del aula **antes** de empezar.
- [ ] Acordate de la siembra: en la viz del tokenizador se plantea *«¿cuántas erres
      tiene?»* y **no se responde**. La clase 8 la cobra. El botón
      *«irreprochable (contá las erres)»* es el que mejor la planta: tiene tres
      erres y sale en cinco fichas, ninguna de las cuales es una letra suelta.
- [ ] Y de la que ya se cobró: `viz/supuestos-de-arquitectura.html` de la clase 5
      tiene una fila para texto. Si la mostraste allá, referila hoy: abrila como
      `../05-imagenes-y-convoluciones/viz/supuestos-de-arquitectura.html?hasta=6`
      y se desbloquea sólo la fila de la RNN (la del Transformer queda gris para la 7).
