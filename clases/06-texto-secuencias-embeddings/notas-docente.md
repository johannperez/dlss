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
    mochila de la RNN se vacía, y queda la pregunta que abre la clase 7.

**Si te llevás una sola frase para repetir**: *cerca en el mapa quiere decir que se
usan parecido, no que signifiquen lo mismo.*

---

## 2. Plan de tiempos real, bloque por bloque

| Min | Slides | Bloque | Qué hacés |
|---|---|---|---|
| **0-1** | 1 | Portada | Una frase y pasás. |
| **1-3** | 2 | Dónde quedamos | Dos minutos. Preguntá qué supone una CNN sobre el mundo. |
| **3-5** | 3 | **Las dos frases** | Leelas en voz alta con énfasis distinto. Preguntá y esperá. |
| **5-8** | 4 | La misma bolsa | **Callate cinco segundos** después de mostrar las dos tablas. |
| **8-10** | 5-6 | No despreciar / el problema | La 5 se dice en serio, no como concesión. |
| **10-13** | 7 | Tokenizar | «¿qué se perdió acá?». Salen mayúsculas y puntuación. |
| **13-16** | 8 | Tres estrategias | Preguntá cuál usarían. Casi todos dicen «por palabras». |
| **16-21** | 9 | **VIZ tokenizador** | Escribís vos «inconstitucionalidad», letra por letra. **Sembrás la clase 8.** |
| **21-23** | 10 | Ficha → número | El «ese número no significa nada» es lo importante. |
| **23-27** | 11-12 | One-hot y su problema | Estirá los brazos para el largo del vector. Funciona. |
| **27-30** | 13 | **VIZ one-hot vs embedding** | Alternás vos las tres palabras, despacio y en silencio. |
| **30-50** | 17 | **Práctico 1** | Notebook, secciones 1-4. Pasás por las mesas. |
| **50-60** | 18 | **PAUSA** | Diez minutos. **No se toca.** |
| **60-63** | 19 | Volvimos | Anotás en el pizarrón dos listas que sacaron ellos. |
| **63-69** | 20 | **VIZ el mapa** | Buscás «reforma», después «pobreza», después una que te tiren. |
| **69-72** | 21 | Los vecinos cuentan | Detenete en `docentes`. |
| **72-75** | 22 | Aritmética | Dos de diez aciertan. Que «niñas» no exista es un dato. |
| **75-77** | 23 | **LA APUESTA** | Votación a mano alzada, contando los votos en voz alta. |
| **77-83** | 24 | **VIZ modo eje** | **La escena central.** Silencio de cinco segundos. |
| **83-86** | 25-26 | Problema o instrumento + código | La 26 se pasa rápido: es referencia. |
| **86-88** | 27-28 | El lunes + la advertencia | |
| **88-105** | 29 | **Práctico 2** | Notebook, secciones 5-10, de a dos. |
| **105-112** | 30-32 | El orden vuelve | La 32 (VIZ bolsa vs orden) es la que engancha. |
| **112-117** | 33-35 | RNN y su falla | **La 35 es lo primero que se recorta.** |
| **117-120** | 36-40 | Cierre | La pregunta, tres ideas, glosario, puente. |

> Los bloques prácticos tienen 20 y 17 minutos en este plan (el presupuesto del
> programa dice 20 y 25). La diferencia se mueve al bloque «el orden importa», que
> es contenido nuevo y va **después** del segundo práctico. El notebook está armado
> para que la segunda mitad se pueda terminar en casa sin perderse nada.

---

## 3. Qué preguntar al aula, y cuándo

| Momento | La pregunta | Para qué |
|---|---|---|
| Slide 3 | **«¿Significan lo mismo?»** | Que alguien use la palabra *quién*. Anotala en el pizarrón: vuelve en la slide 31. |
| Slide 5 | «¿Quién de acá publicó con diccionarios o con LDA?» | Manos arriba. La clase deja de ser una amenaza a lo que ya saben. |
| Slide 7 | «¿Qué se perdió al partir así?» | Que vean que tokenizar es un libro de códigos, no un automatismo. |
| Slide 8 | «¿Cuál usarían ustedes?» | Casi todos dicen «por palabras». Anotalo: la viz que sigue lo desarma. |
| Slide 12 | «¿Alguien ve el problema del one-hot?» | La carencia hay que **sentirla** antes de mostrar el embedding. |
| **Slide 15** | **«¿El significado de una palabra es su uso?»** | **Dos o tres minutos de discusión abierta.** Es donde esta audiencia brilla. |
| Slide 19 | «¿Qué les salió a ustedes?» | Que el hallazgo salga de ellos y no de la pantalla. |
| Slide 20 | «¿Les llama la atención algún vecino?» | Y después: «tírenme una palabra». Buscala en vivo, sin preparar. |
| Slide 21 | «¿Qué les dice que `docentes` esté al lado de `salario` y de `piso`?» | Sale solo, y es lectura sustantiva pura. |
| **Slide 23** | **«¿Dónde cae cada palabra? A, B o C. Voten.»** | Sin esta apuesta, la viz del eje es un dibujito lindo. |
| Slide 24 | *(nada)* | **No preguntes. Callate.** Dejá que hablen ellos primero. |
| Slide 28 | «¿Por qué `importaciones` y `exportaciones` quedan cerca?» | La respuesta la dice el aula, no vos. |
| Slide 32 | «¿Quién tiene una variable que depende de una negación?» | Se levantan manos. Es el puente al lunes. |

---

## 4. Las respuestas típicas, y cómo usarlas

**Slide 3, «¿significan lo mismo?»**
Dicen «no, cambia quién rechaza». Perfecto: escribí **QUIÉN** en el pizarrón y dejalo
ahí toda la clase. En la slide 31, cuando el promedio dé 1,000 exacto, señalalo.

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
manera de validarla, y eso es la clase 10.*

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
| **«Más dimensiones es mejor»** | Piden 300 o 1000 dimensiones. | Es la clase 4 otra vez: más dimensiones = más perillas. Con 350.000 tokens de corpus, 100 dimensiones andan mejor que 300. |
| **Embedding de palabra ≠ de oración** | Promedian y esperan que capture la oración. | Slides 31-32, con el número medido: 1,000 exacto. Los embeddings de oración de verdad llegan en la clase 9 y usan un transformer. |
| **«La aritmética funciona»** | Prueban analogías y se frustran. | Slide 22 y el botón *«los 8 que NO funcionan»*. Dos de diez aciertan. **Decilo antes de que lo descubran solos.** |
| **«Hay que abandonar bag-of-words»** | Descartan sus herramientas previas. | Slide 5, dicha en serio. Para muchas preguntas un diccionario validado es mejor, más barato y más interpretable. Se retoma en la clase 10. |
| **«Todos los discursos son iguales»** | Les da 0,98 de similitud entre todos y concluyen que no hay variación. | Es el momento más pedagógico del notebook. **Es un problema de instrumento, no un hallazgo**: el promedio está dominado por el fondo común. Restás la media y aparece la estructura. |

---

## 6. Si vas atrasado (y vas a ir atrasado)

**Se recorta, en este orden:**

1. **Slide 35, «las RNN en treinta segundos».** Se dice de pie, en dos oraciones,
   sin proyectar. Es contenido de contexto, no de examen.
2. **Slide 22, la aritmética.** Se muestra una sola fila de la tabla (`córdoba − provincia + salta`)
   y se dice «de diez, aciertan dos». Treinta segundos.
3. **Slide 26, el código.** Es referencia; está en el notebook.
4. **Slide 38, herramientas.** Se menciona de palabra al cerrar.
5. **El práctico 2 baja de 17 a 12 minutos**, y el notebook se termina en casa.
   Avisalo explícitamente: *«las secciones 8, 9 y 10 se terminan en casa, y el TODO 5
   lo discutimos la clase que viene»*.

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
- **Modo «dos épocas» con `seguridad`.** Está en la viz y no tiene slide propia:
  1984-1999 → *social, justicia, ministerio, salud*; 2004-2019 → *policía, fuerzas,
  defensa, federal*. **De ocho vecinas, siguen dos.** Es una tesis entera y se ve en
  diez segundos. Si te sobran cinco minutos, esto es lo que hacés.
- **Modo eje con `oficialismo ←→ oposición`** (está como atajo). Sale distinto de lo
  que la gente espera y da conversación.
- Pediles que armen un eje con dos palabras **de su campo**, en voz alta, y probalo
  en vivo. Muchos van a fallar porque la palabra no está en el vocabulario: eso
  también enseña (frecuencia mínima 8, y las tildes cuentan).

---

## 8. Chistes y analogías que funcionan

- **La mochila.** Caminá por el aula haciendo el gesto de cargar una mochila que se
  va llenando mientras «leés». Es tonto y se lo acuerdan seis meses después.
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
bien, pero **la aritmética no funciona** y las palabras que aparecen menos de ocho
veces hay que tirarlas. Word2vec original se entrenó con 100.000 millones. Regla
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
Porque las probamos y con este corpus 100 anda bien; no hay una razón profunda. Es
un hiperparámetro, como la cantidad de rampas de la clase 4, y se elige igual: con
un criterio explícito y validando. Lo importante es que **sea una decisión declarada
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
      tiene?»* y **no se responde**. La clase 8 la cobra.
- [ ] Y de la que ya se cobró: `viz/supuestos-de-arquitectura.html` de la clase 5
      tiene una fila para texto. Si la mostraste allá, referila hoy.
