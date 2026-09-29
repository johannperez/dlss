# Clase 6 — Soluciones comentadas

**Para quien da la clase.** Cada ítem trae la respuesta correcta **y qué confusión
revela cada distractor**. Eso es lo que sirve para devolver la corrección: no alcanza
con marcar la cruz.

Si al corregir ves que un distractor concreto se llevó media clase, está anotado abajo
qué slide y qué visualización lo desarman.

---

## 1. Qué es un token → **B**

Cada uno de los pedacitos en que se parte el texto.

| distractor | por qué tienta | qué confusión revela |
|---|---|---|
| **A** (siempre una palabra) | Es lo que uno supone antes de ver un tokenizador funcionando, y en muchos ejemplos simples es cierto. | **La confusión más común de la clase**, y tiene consecuencias prácticas: si contás fichas y reportás «palabras», tu número está inflado entre 1,3 y 2 veces en castellano. Desarme: `viz/tokenizador.html`, «inconstitucionalidad» → 5 fichas. |
| **C** (un número entre 0 y 1) | Confunde token con **peso**: se están acordando de TF-IDF o de una probabilidad. | Mezcla la *unidad* con la *medida*. Vale la pena aclararlo: un token es una cosa, no un número. |
| **D** (una palabra desconocida) | Confunde *token* con *OOV*. | Los dos términos aparecieron en la misma slide (10). Si eligieron D, la slide 10 pasó demasiado rápido. |

---

## 2. El problema del one-hot → **C**

Todas las palabras quedan exactamente igual de lejos entre sí.

| distractor | por qué tienta | qué confusión revela |
|---|---|---|
| **A** (ocupa mucha memoria) | **Es verdad**, y por eso es el distractor más peligroso del cuestionario. Un vector de 50.000 posiciones es un despilfarro. | Que se quedaron con el problema *de ingeniería* y no vieron el problema *conceptual*. Si la memoria fuera el único problema, con computadoras más grandes one-hot serviría — y no serviría. Desarme: `viz/one-hot-vs-embedding.html`, la tabla donde todos los pares dan 0,000. |
| **B** (los números no son enteros) | Suena técnico. | Confusión sobre qué le molesta a una red. Los one-hot **sí** son enteros; el problema no está ahí. |
| **D** (no sirve para textos largos) | Mezcla el problema de la representación de *palabra* con el de la ventana de contexto (clase 8). | Vale aclarar que son dos problemas distintos y que el de hoy es el de la palabra. |

---

## 3. Qué captura un embedding → **B**

Aparecen en contextos parecidos **dentro del corpus con el que se entrenó**.

| distractor | por qué tienta | qué confusión revela |
|---|---|---|
| **A** (significan lo mismo) | **Es el distractor fuerte y el error número uno con embeddings**, y aparece en papers publicados. La divulgación lo repite. | Que no se llevaron la advertencia de validez. Desarme inmediato y sin discusión: `importaciones` y `exportaciones` dan **0,78**. Slide 28 y celda de antónimos del notebook. Si más de un tercio del aula eligió A, **volvé sobre esto la clase siguiente**: es la confusión que más caro les va a salir. |
| **C** (misma frecuencia) | Se acuerdan de que la frecuencia juega en el cálculo (PPMI, Zipf). | Confunde una **variable de control** con lo que se mide. PPMI existe justamente para *descontar* la frecuencia. |
| **D** (misma categoría gramatical) | Es parcialmente cierto en los hechos: los verbos tienden a agruparse. | Confunde un **efecto colateral** con el criterio. El espacio no sabe qué es un verbo; agrupa por contexto, y los verbos comparten contextos. |

> **Fijate en la parte que se olvidan aun cuando eligen B:** *«dentro del corpus con el
> que se entrenó»*. Si alguien contestó B pero sin esa cláusula, la respuesta está a
> medias. Todo lo que se mide con un embedding es una afirmación sobre **ese** corpus.

---

## 4. Dos corpus, dos épocas

**(a)** No. Casi seguro que no.

**(b)** **Cambio semántico**: cómo cambió el uso —y con él, el sentido operativo— de la
palabra. Es una medición legítima y publicable. En nuestro corpus lo tenemos medido:
las vecinas de `seguridad` pasan de *social · justicia · ministerio · salud* (1984-1999)
a *policía · fuerzas · defensa · federal* (2004-2019). **De ocho vecinas, siguen dos.**
Y con la vara al lado: partiendo el mismo corpus en dos mitades alternadas, sin corte
de época, siguen **cuatro**. Hay una pista de cambio, no una prueba.

**(c)** Lo que buscamos acá. Al menos una de estas:

- **Los corpus no son comparables.** Distintos oradores, distintos géneros
  discursivos, distinta extensión. Parte de la diferencia es de corpus, no de época.
- **Los dos espacios no están alineados.** Son dos entrenamientos independientes: las
  dimensiones no significan lo mismo en uno y en otro. Comparar *listas de vecinas*
  es legítimo; comparar coordenadas o hacer aritmética entre los dos espacios, no,
  salvo que los alinees explícitamente (procrustes).
- **Corpus chicos = mucho ruido.** Con 16 y 15 discursos, parte del cambio de vecinas
  es azar: en nuestro corpus, dos mitades de la *misma* época ya comparten sólo la mitad
  de las vecinas de `seguridad`. Un paper serio lo repite con remuestreo y reporta la
  variabilidad.
- **Cambió el mundo, no la palabra.** Si entre las dos épocas hubo una pandemia o una
  crisis, el vocabulario de coyuntura arrastra a todo.

*Con una de estas alcanza para el punto completo. Si escriben las cuatro, eso es una
sección de limitaciones ya escrita.*

---

## 5. Corpus chico

**(a)** 80.000 palabras es **poquísimo**. Concretamente:

- La ley de Zipf no perdona: casi todo el vocabulario va a aparecer una o dos veces, y
  de esas palabras no se puede estimar nada. En nuestro corpus, que es **cuatro veces
  más grande**, el 45,6 % del vocabulario aparece una sola vez.
- Con `minimo=8` te quedan unos pocos cientos de palabras útiles; si bajás el mínimo,
  entran palabras con vectores que son ruido.
- Los vecinos van a ser inestables: cambiás la semilla o sacás cinco documentos y la
  lista cambia. **Y eso no se nota si no lo probás.**

**(b)** Usar **modelos pre-entrenados**: alguien ya entrenó sobre miles de millones de
palabras en castellano y vos usás esos vectores. Es la clase 9. El precio es que el
modelo trae el sesgo y el vocabulario de *su* corpus, no del tuyo, y eso hay que
declararlo y validarlo.

> *Respuesta parcial frecuente:* «voy a usar más dimensiones para compensar».
> Es exactamente al revés, y es la clase 4 otra vez: menos datos pide **menos**
> capacidad, no más.

---

## 6. Leer el gráfico

**(a)** Educación · economía · salud · instituciones legislativas.
(Aceptar cualquier nombre razonable: lo que se evalúa es que agrupen bien.)

**(b)** **`licitación`**, que aparece en el medio del grupo de educación, entre
*docentes* y *alumnos*. Uno la esperaría con economía (o con obra pública e
infraestructura), no con escuelas y maestros. Es una sola palabra a propósito: en un
embedding de palabras, cada punto es **una** palabra, y una expresión de dos
(«obra pública») no tendría un punto propio.

**(c)** Hipótesis aceptables (cualquiera, si está argumentada):

- En estos debates se habla de licitaciones **cuando se habla de construir escuelas**
  (o de comprar computadoras o guardapolvos): comparte contexto con el vocabulario
  educativo.
- La proyección 2D aplasta: en las 100 dimensiones reales puede estar lejos, y sólo
  *parece* cerca en la sombra.
- Es una palabra de baja frecuencia y su vector es pobre.

**(d)** El recaudo: **el dibujo es una sombra**. Con el 15 % de la variación, el 85 % de
lo que distingue a estas palabras **no está en la pantalla**. Dos palabras pueden verse
pegadas y estar lejísimos. Corolario práctico: **la proyección sirve para explorar y
para ilustrar, no para medir**. Si vas a afirmar que dos palabras están cerca, medí la
similitud coseno en el espacio completo, no la distancia en el gráfico.

> Este es el ítem que más separa a quien entendió de quien memorizó. El punto (d) vale
> tanto como (a), (b) y (c) juntos.

---

## 7. Leer la salida de código

**(a)** `de` y `la` son **palabras de función**, y aparecen cerca de todo. **No es un
error del código**: PPMI descuenta la frecuencia pero no la elimina, y esas palabras
tienen contextos tan variados que terminan en el medio del espacio, cerca de todo.
(Se ve igual en nuestro corpus: `seguridad → social, de, la, salud, fuerzas…`)

**(b)** Se filtran con una lista de palabras vacías (*stopwords*). Y **lo que hay que
declarar es la lista**: cuál usaste, de dónde salió, y si la editaste a mano. Es
exactamente el mismo problema que el léxico de la clase 1: **el instrumento de medición
lo escribiste vos, un martes**, y cambiarlo cambia el resultado.

**(c)** Lo que **no** podés concluir: que en tu corpus la protesta *cause* represión,
ni que la represión sea una *consecuencia* de la protesta, ni que quien escribe apruebe
o desapruebe ninguna de las dos. Lo único que dice el número es que **las dos palabras
aparecen en contextos parecidos**: en las mismas notas, en las mismas oraciones.
Podría ser causalidad, podría ser co-tematización periodística, podría ser una fórmula
fija («la protesta terminó con represión») repetida en 200 titulares.

---

## 8. Los antónimos

**(a)** Porque el embedding codifica **contextos de uso**, y los antónimos comparten
contexto casi perfectamente: son justamente las palabras que uno puede intercambiar en
una oración sin que la oración deje de tener sentido. *«Aumentaron las importaciones
este año»* / *«Aumentaron las exportaciones este año»*. Las dos oraciones existen, las
dos son gramaticales, las dos aparecen en el mismo tipo de párrafo. Para un método que
sólo mira compañía, **son casi la misma palabra**.

**(b)** Respuesta esperada, en una oración: *«estarías midiendo si los dos discursos
hablan de los mismos temas, no si están de acuerdo — dos discursos que dicen lo
contrario sobre exactamente el mismo tema te van a dar la similitud más alta de todo
tu corpus»*.

> Si alguien contesta «depende», pedile que complete. La única versión aceptable del
> «depende» es: *sirve como medida de solapamiento temático, y hay que llamarla así.*

---

## 9. Los cuatro pasos

Una respuesta completa se parece a esto. **Lo que se evalúa es la segunda columna**, no
la primera: cualquiera puede listar los pasos, lo difícil es ver dónde está la
discusión.

| paso | la decisión que estás tomando, y por qué se puede discutir |
|---|---|
| **1. Partir el corpus en dos períodos** (2000-2005 y 2015-2020) y tokenizar cada uno igual. | ¿Dónde corta el período, y por qué ahí? ¿Los dos tramos tienen medios comparables, extensión comparable? Si un diario cerró en el medio, cambiaste el corpus y no la época. |
| **2. Entrenar un embedding por período**, con la misma configuración y la misma semilla. | Los dos espacios son independientes: **no se pueden comparar coordenadas**, sólo listas de vecinas o proyecciones sobre ejes definidos dentro de cada espacio. |
| **3. Definir el eje «securitario»** con dos palabras o dos listas de palabras (por ejemplo *delito · policía · frontera* contra *trabajo · derechos · familia*), y proyectar `inmigración` sobre él en cada período. | **Esta es la decisión fuerte y es tuya**: esas listas son el instrumento de medición. Cambialas y cambia el resultado. Hay que publicarlas, y conviene reportar el resultado con dos o tres listas alternativas. |
| **4. Comparar las dos proyecciones y validar**: leer 30 notas de cada extremo a mano y ver si el número dice lo que parece. | Sin este paso no tenés una medición, tenés un número. Y hay que reportar la variabilidad: repetí el entrenamiento con varias semillas y con submuestras, porque parte de la diferencia va a ser ruido. |

*Respuestas que se quedan cortas:* las que listan los cuatro pasos técnicos y no
mencionan **ni una sola** decisión discutible. Devolvelas pidiendo la segunda columna.

---

## 10. La RNN → **B**

Arrastra un estado de tamaño fijo que se va sobrescribiendo.

> **Para quien quiera la razón técnica:** al entrenar, la señal de error que tiene que
> viajar hacia atrás hasta las primeras palabras se multiplica una vez por cada paso,
> y se achica hasta casi desaparecer: es el *gradiente que se desvanece* (Hochreiter,
> 1991; Bengio, Simard & Frasconi, 1994). La mochila de tamaño fijo es la imagen; el
> gradiente que se desvanece es el mecanismo. Las compuertas de la LSTM se inventaron
> para eso. No hace falta pedirlo en la respuesta.

| distractor | por qué tienta | qué confusión revela |
|---|---|---|
| **A** (pocos parámetros) | Es la explicación por defecto para todo lo que no anda. | Que no vieron que el problema es **estructural, no de tamaño**. La viz lo muestra: con la mochila al máximo (128 veces el mínimo) el olvido se hace más lento y llega con un 40 %, pero con el doble de distancia volvería a quedar casi nada. Agrandar posterga, no arregla. Desarme: `viz/memoria-que-se-olvida.html`, slider al máximo. |
| **C** (promedia y el promedio no tiene orden) | **Es el distractor más peligroso del ítem**, porque describe algo que sí vimos hoy y que sí es verdad… de *otra* cosa. | Confunde las dos maneras de armar el vector de una frase. **Promediar** (slides 31-32) tira el orden de entrada; **la RNN no promedia**: lee en orden, y por eso el orden sí le llega. Su problema es otro y es posterior: lo que leyó primero se le degrada. Si alguien elige C, la mitad final de la clase se le mezcló, y conviene volver sobre la slide 33 («leer en orden, con una mochila»). |
| **D** (las palabras lejanas quedan fuera del vocabulario) | Mezcla el problema de **memoria** con el de **vocabulario**, y los dos aparecieron hoy. | Estar fuera de vocabulario no tiene nada que ver con estar lejos en la oración: `<desc>` depende de la frecuencia de la palabra en el corpus, no de su posición. Son dos límites distintos y se arreglan con cosas distintas. |

---

## 11. Lo que pierde el promedio

**(a)** **El orden**, y con él todo lo que depende del orden: quién es agente y quién
paciente, el alcance de la negación, la estructura de la subordinación. El promedio de
un conjunto no depende del orden de sus elementos: es una propiedad matemática, no una
limitación de implementación. Por eso «el gobierno criticó al congreso» y «el congreso
criticó al gobierno» dan **1,000 exacto**.

**(b)** Porque las variables que un cientista social codifica a mano **son** esas:

- *atribución de responsabilidad* (¿quién reprimió a quién?);
- *agencia* (¿el sujeto actúa o le pasan cosas?);
- *negación* («el proyecto **no** fue aprobado» difiere en un token de ocho);
- *modalidad* («va a haber» contra «podría haber»).

Ejemplos propios aceptables: cualquiera donde el sentido se invierta sin que cambien
las palabras. *«La policía reprimió a los manifestantes»* / *«Los manifestantes
reprimieron a la policía»*. *«El aumento no alcanza»* / *«El aumento alcanza»*.

> **Ojo con una respuesta que parece buena y está incompleta:** «se pierde el contexto».
> Es demasiado vaga. Pedí que nombren *qué* del contexto, y que den el ejemplo.

---

## 12. Criterio y ética aplicada

**(a) De los datos, y del algoritmo sólo en tanto los refleja fielmente.** El embedding
aprendió las regularidades de uso del corpus de currículums, y en ese corpus ciertas
ocupaciones aparecen sistemáticamente con nombres de un género. El algoritmo no
introdujo el patrón: lo **encontró, lo comprimió y lo dejó disponible para usar**.
Decir «es culpa del algoritmo» es cómodo y es falso; decir «el algoritmo es neutral»
también, porque **elegir usarlo para decidir es una decisión de alguien**.

**(b) No alcanza, y esta es la parte importante.** El género queda codificado en decenas
de *proxies*: la ocupación misma, el nombre del colegio, el club, el deporte, los verbos
usados para describir logros, los años sin empleo. Sacar la variable explícita elimina
la evidencia del sesgo, no el sesgo — y encima **hace más difícil auditarlo**, porque ya
no tenés la variable con la que medirías la disparidad. Esto tiene un nombre en la
literatura de *fairness* y una discusión larga; lo mínimo que hay que decir es que
«no mirar la variable» y «no usar la variable» son cosas distintas.

**(c) Sí, cambia por completo, y ese es el corazón de la clase.**

- Para **decidir** sobre personas, el sesgo es **daño**: se reproduce a escala, con
  apariencia de objetividad y sin nadie a quien reclamarle.
- Para **estudiar** la segregación ocupacional, el sesgo del embedding **es la
  medición**. Un embedding «corregido» sería un termómetro al que le borraron la fiebre:
  ya no te sirve para el diagnóstico. Es exactamente lo que hacen Garg et al. (2018)
  midiendo cien años de estereotipos, y Kozlowski, Taddy & Evans (2019) midiendo la
  estructura de clase.

**El mismo instrumento es dañino para decidir y valioso para medir.** Y la diferencia
no está en el modelo: está en para qué lo usás y sobre quién.

> **Cómo corregir esto.** Si alguien contesta bien (a) y (b) pero en (c) dice «es lo
> mismo, el sesgo siempre es malo», no está mal informado: está aplicando bien una
> regla que en este caso no aplica. Devolvéselo con la analogía del termómetro. Es la
> idea que más cuesta y la que más vale de la clase.

---

## Cómo pesarlo

Si tenés que poner una nota, un reparto que funciona:

| ítems | qué evalúan | peso sugerido |
|---|---|---|
| 1, 2, 3, 10 | vocabulario y mecanismo (opción múltiple) | 20 % |
| 6, 7 | **leer** un gráfico y una salida con desconfianza | 25 % |
| 4, 5, 8, 11 | criterio metodológico | 30 % |
| 9, 12 | aplicación y ética: transferir a su propio trabajo | 25 % |

Y una regla de la casa: **el ítem 3 y el ítem 8 miden la misma cosa**. Si alguien
acierta el 3 y falla el 8, marcó la opción correcta sin entenderla. Vale la pena
señalárselo por escrito.
