# Soluciones comentadas — Clase 8

**Para quien da la clase.** Cada ítem trae la respuesta correcta, **por qué cada distractor
es tentador**, y **qué confusión revela elegirlo**. Esa última parte es la que sirve: si en
un grupo de treinta hay ocho que eligen el mismo distractor, no es distracción, es una
explicación que no funcionó, y ya sabés cuál.

> **Todos los números de este archivo están medidos**, no estimados. Salen de correr
> `clases/08-mini-gpt-y-los-llm/entrenar-mini-gpt.py` en el contenedor de construcción.
> Los del ítem 6 salen de una corrida aparte del mismo modelo sobre los primeros 25 KB
> del corpus; está documentada en `notas-docente.md` §9.

---

## 1. El objetivo de entrenamiento

**Correcta: B** — *ponerle una probabilidad a cada ficha posible de ser la que sigue.*

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** (aprender definiciones de un diccionario) | Es el modelo mental por defecto de «la computadora entiende palabras»: que adentro hay significados guardados. | Creen que el significado está **almacenado**. Se desarma volviendo a la clase 6: el significado que el modelo maneja sale de **la compañía** (con qué otras palabras aparece) y del contexto. No hay definiciones adentro. Se paga en el ítem 2: si creés que adentro hay un diccionario, no podés entender por qué alucina. |
| **C** (comprimir el corpus para recuperarlo) | Es media verdad, y de las peligrosas: entrenar **sí** es una forma de compresión. | El problema es el «para recuperarlo». Es compresión **con pérdida**, y sin índice: no hay manera de consultar ni de recuperar el original. La demostración de tres segundos: el corpus pesa 1,1 MB, el modelo 6,2 MB, y en la clase 9 aparecen modelos entrenados con terabytes que pesan gigabytes. **No entra.** Lo que se perdió es exactamente lo que después se inventa. |
| **D** (clasificar oraciones por tema) | Es la tarea de ML que esta audiencia ya conoce (clases 4 y 9), así que es la plantilla que tienen a mano. | Confunden **modelo de lenguaje** con **clasificador**. Vale la pena señalar la diferencia económica: el clasificador necesita etiquetas humanas, el modelo de lenguaje no necesita ninguna. Ésa asimetría es por qué existen los LLM. |

**Bandera roja:** si más de un tercio elige A, la segunda mitad de la clase no se entendió.
Volvé a la slide 21 («por qué alucina») antes de seguir con la clase 9.

---

## 2. Por qué alucina

**Correcta: C** — *la salida es siempre una distribución, no hay verificador de verdad y
no existe la opción «no sé».*

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** (le faltan datos) | **Es el distractor fuerte y hay que esperarlo.** Es lo que dice la prensa, es intuitivo, y además es *parcialmente cierto*: con más datos alucina menos seguido. | Creen que es un problema de **cobertura**, que se arregla con escala. No: alucina **por diseño**. Con más datos alucina *menos seguido*, no *cualitativamente distinto*. Es exactamente la slide 36 («qué no cambia con la escala») y por eso esa slide es la más importante de la clase. Si eligieron A, la consecuencia práctica es grave: van a confiar en modelos grandes «porque ya no alucinan». |
| **B** (es un bug) | Le da a la gente la esperanza de que alguien lo va a arreglar. | No entienden que es una **propiedad del mecanismo**, no un defecto de implementación. Desarmalo con la viz: se les puede mostrar el mecanismo funcionando *correctamente* y produciendo una diputada inventada. |
| **D** (la temperatura está alta) | Confunde dos cosas que **sí** existen las dos, y por eso es el más difícil de descartar. | Confusión entre **qué se elige** y **de dónde se elige**. La temperatura cambia el riesgo del sorteo; la alucinación pasa igual a T=0. Es más: los cuatro ejemplos de `viz/por-que-alucina.html` están generados **a temperatura 0**, sin sorteo. Decilo: es la mejor refutación. |

---

## 3. Temperatura 0

**a)** El texto se vuelve **determinista** (misma entrada, misma salida siempre) y
**repetitivo**: siempre gana la ficha más probable, y eso lo mete con facilidad en bucles
de alta probabilidad.

**b)** **No cambia nada de lo que el modelo sabe.** La distribución que produce es
exactamente la misma; sólo cambia cómo se elige adentro de ella. El **orden** de las
opciones no se mueve nunca: es lo que muestra `viz/temperatura.html`.

**c)** Mejora: la **reproducibilidad** (condición para poder afirmar algo en un paper).
Empeora: la **variedad** — se vuelve monótono, repite, y en tareas creativas es peor.

> **Lo que revela una respuesta floja.** Si contestan «con T=0 es más preciso» o «sabe
> más», la antropomorfización del parámetro sigue intacta. Volvé a la viz y mostrá que el
> orden de las barras no cambia. Es la confusión más común de todo el bloque.

---

## 4. El prompt de 10.000 palabras

**a)** Las instrucciones del principio **quedan fuera de la ventana** y directamente no se
le pasan al modelo. No las ve.

**b)** **No «se olvidó»**: nunca las tuvo. La diferencia importa y no es una sutileza
semántica. «Olvidarse» supone que estuvieron adentro y se degradaron — que es lo que hacía
la RNN de la clase 6. El transformer tiene un **corte duro**: lo que quedó afuera no está
borroso, no está.

**c)** Tres mitigaciones aceptables, en orden de calidad:
1. **Poner las instrucciones al final**, pegadas a los datos.
2. **Procesar por lotes**: repetir las instrucciones en cada tanda de 20 titulares en vez
   de mandar los 200 juntos. Es lo que hay que hacer de verdad.
3. **Repetir** lo más importante al principio y al final.

> **Media respuesta que hay que corregir:** «uso un modelo con ventana más grande».
> Sirve, pero no resuelve: en modelos grandes existe el *lost in the middle* — lo que
> queda en el medio de un contexto largo se atiende peor aunque esté adentro. Y eso lo
> vieron medido: el caso «lejos» de `viz/ventana-de-contexto.html` tiene la curva **plana
> aun con la pista adentro de la ventana**. Ventana más grande no es lo mismo que
> atención efectiva.

---

## 5. Las dos distribuciones

**a)** La **B** es la de temperatura más alta: está más **aplanada** (la primera se lleva
58,6% en vez de 89,1%, y las «otras 66» pasan de 0,3% a 14,4%).

**b)** **A** produce texto conservador y previsible; si la usás para generar varias veces,
las salidas van a parecerse mucho entre sí, y hay riesgo de bucles. **B** produce texto
variado, con más riesgo de que se descarrile: cada tanto va a elegir una de esas 66 fichas
raras, y en castellano una letra rara arruina la palabra.

**c)** **Se parecen en el orden**: «s» primero, «y» segundo, «l» tercero, «p», «c». En las
dos. Y eso dice lo que la temperatura **no** hace: **no cambia lo que el modelo cree que
es más probable.** No lo hace más inteligente ni más tonto: lo hace más o menos arriesgado
al sortear.

> Los números son reales: es la distribución del mini-GPT de la clase después de
> «Señor presidente, », con **T = 1,0** (columna A) y **T = 1,9** (columna B), calculada
> sobre las 71 logits que exportó `entrenar-mini-gpt.py`.
>
> **La respuesta que importa es la (c).** Si contestan bien a) y b) pero no ven la (c), la
> viz no funcionó: volvé a abrirla y movés el slider vos, señalando la primera barra con
> el dedo.

---

## 6. La curva de loss con tijera

**a)** **Sobreajuste** (*overfitting*): está **calcando** el corpus en vez de aprender la
forma. La señal de libro de la clase 4: la loss de train sigue bajando (0,56 → 0,10)
mientras la de validación **toca fondo y empieza a subir** (0,70 en el paso 900 → 0,79 en
el 1200).

**b)** Alrededor del **paso 900**, donde la validación toca su mínimo. Eso es exactamente
lo que hace la **parada temprana** (`ent.ParadaTemprana`, clase 4).

**c)** Cualquiera de estas, y conviene que nombren dos de familias distintas:
- **Más datos.** Es la causa directa acá: 22.500 fichas de train para 1.541.056 perillas.
  Con el corpus entero (988.385 fichas) la tijera desaparece.
- **Un modelo más chico** (menos bloques, menos dimensión): menos capacidad para memorizar.
- **Parada temprana** en el mínimo de validación.
- **Regularización** (*dropout*, *weight decay*).

**d)** Que el modelo **es buenísimo**: 0,10 es una loss preciosa. Y estaría completamente
equivocada. **Ése es todo el argumento de por qué existe el conjunto de validación**, y es
por qué la clase 4 va antes que ésta.

> **Contexto para el docente.** Estos números salen de entrenar el mismo mini-GPT sobre
> los primeros 25 KB del corpus (1200 pasos, 224 s). Con el corpus entero, train y val
> terminan en 0,185 y 0,186: **una diferencia de 0,001**. La comparación entre las dos
> corridas es lo que hace la pregunta.
>
> **Bandera roja:** si alguien contesta «se rompió el entrenamiento» o «la loss de
> validación está mal calculada», el concepto de la clase 4 no está. No sigas a la clase 9
> sin recuperarlo: toda la evaluación de la 9 depende de esto.

---

## 7. Por qué cuenta mal las letras

**Lo que tiene que aparecer:** el modelo no ve letras, ve **fichas** (*tokens*) de
sub-palabra. «ferrocarril» no son once letras: son tres o cuatro números. Contar las erres
es contar algo que **no está en su representación**. Es como pedirle a alguien que sólo
escuchó una palabra que te diga cómo se escribe.

**Segunda parte — por qué a veces acierta:** porque **vio la respuesta escrita** muchas
veces en el corpus (las palabras muy frecuentes, o los casos que aparecen en tutoriales y
foros), o porque la palabra es **una sola ficha frecuente** y su respuesta quedó
memorizada junto a ella. Acierta **por recuperación, no por conteo** — y eso explica por
qué acierta con «arroz» y falla con una palabra rara de la misma longitud.

| respuesta parcial frecuente | qué le falta |
|---|---|
| «porque es un modelo de lenguaje, no una calculadora» | Es verdad y no explica nada. Preguntá: *¿por qué no puede simplemente contar?* Ahí aparece la tokenización o no aparece. |
| «porque no sabe contar» | Circular. Un modelo de caracteres tampoco sabe contar, pero por otro motivo. Repreguntá: *¿qué es lo que el modelo tiene delante cuando le hacés la pregunta?* |

> **Honestidad obligatoria en esta pregunta.** El mini-GPT de la clase es **de
> caracteres**: él sí ve las letras. No sufre este problema (sufre otro: nunca vio a nadie
> contar nada en el corpus). Si algún estudiante lo señala, **festejalo**: leyó el aviso
> del notebook y entendió la diferencia entre las dos tokenizaciones. Es la mejor
> respuesta posible a esta pregunta.

---

## 8. El mismo prompt, dos respuestas

**a)** Porque al elegir cada ficha hay un **sorteo** sobre la distribución. Con
temperatura mayor que cero, dos corridas sortean distinto. **El modelo no cambió de
opinión: la distribución fue la misma y salió otro número.**

**b)** **Temperatura 0** (o lo más cerca que te deje el proveedor) y **semilla fija**, si
te la deja fijar. Y reportarlo.

**c)** Porque no alcanza, y hay que saber por qué:
- **La versión del modelo cambia sin aviso.** «GPT-4» no es una versión: es una familia.
  El modelo que te contestó en marzo puede no existir en septiembre.
- **El hardware y la infraestructura** introducen no determinismo (orden de operaciones en
  punto flotante, batching del servidor): aun a T=0 podés obtener salidas distintas.
- **El proveedor puede cambiar el sistema alrededor del modelo** (el *system prompt*, los
  filtros) sin cambiarle el nombre.

> La consecuencia metodológica —**un modelo cerrado no es del todo reproducible**— se
> retoma entera en la clase 10. La mitigación seria es usar un modelo abierto con pesos
> fijados y versión anotada, y decir en el paper qué no pudiste controlar.

---

## 9. Tu mini-GPT y ChatGPT

**a)** Tres diferencias (se aceptan otras si son correctas):
1. **Escala.** 1.541.056 parámetros contra cientos de miles de millones; 1,1 MB de corpus
   contra billones de fichas.
2. **Instruction tuning.** ChatGPT fue ajustado con ejemplos de instrucción-respuesta para
   **responder consignas**; el mini-GPT sólo completa texto.
3. **RLHF.** Ajuste con preferencias humanas, para que sea útil, amable e inofensivo.
4. *(También válidas:)* tokenización por sub-palabras en vez de caracteres; ventana de
   contexto de miles o cientos de miles de fichas en vez de 128; corpus multilingüe y
   general en vez de un corpus sintético de un dominio.

**b)** **Instruction tuning y RLHF** — sobre todo el primero. La **escala sola no lo
convierte en asistente**: un modelo enorme entrenado sólo para completar texto, si le
escribís una pregunta, te contesta con **más preguntas parecidas**, porque eso es lo que
sigue en un texto lleno de preguntas. Es el punto de la slide 35 y sorprende a todo el
mundo.

**c)** Dos propiedades que ChatGPT sigue teniendo igual (cualquiera de la tabla de
traducción): la salida es siempre una distribución sin casillero de «no sé»; hay un sorteo
al elegir la ficha; la ventana es finita; trabaja con fichas y no con letras; no hay un
estado de creencias que se sostenga.

> **Bandera roja al revés:** si alguien contesta que la diferencia principal es la escala
> y que con escala aparece el resto, mostrale que GPT-3 base (175 mil millones de
> parámetros, sin instruction tuning) **no** se comportaba como un asistente. La escala y
> la instrucción son dos cosas distintas.

---

## 10. Clasificar 3.000 titulares

**Lo que tiene que aparecer** (una lista, no un párrafo):

1. **Definir la categoría por escrito antes de tocar nada.** Qué cuenta como «protesta
   social» y qué no, con casos límite. Ese documento es tu **libro de códigos**.
2. **Escribir el prompt en un archivo y no tocarlo más.** El prompt *es* el libro de
   códigos operacionalizado. Va en el apéndice, literal.
3. **Temperatura 0** y semilla fija, si el proveedor la ofrece.
4. **Codificar a mano una muestra al azar** de al menos 100-200 titulares, sin mirar lo
   que dijo el modelo. Si podés, que dos personas codifiquen un subconjunto y reportás el
   acuerdo entre humanos: **ése es tu techo realista**, no el 100%.
5. **Comparar el modelo contra esa muestra** y reportar **precisión, recall, F1 y matriz
   de confusión**, cada uno con su frase en castellano llano
   («de cada 100 que el modelo llamó protesta, 78 lo eran»).
6. **Comparar contra un baseline tonto**: la clase mayoritaria y un diccionario de
   palabras clave. Si el diccionario da lo mismo, usá el diccionario.
7. **Mirar los errores a mano**, no sólo el número. Los errores tienen estructura y la
   estructura te dice qué aprendió el modelo en vez de tu categoría.
8. **Reportar** modelo, versión exacta, fecha de las consultas, temperatura, prompt
   completo, y qué hiciste con los casos donde el modelo no contestó en el formato pedido.

**Lo que vale como respuesta completa:** los puntos 2, 4, 5, 6 y 8. Sin el 4 no hay
trabajo publicable, y ése es el que más se olvida.

> **Error frecuente y caro:** validar sobre los mismos casos que usaron para ajustar el
> prompt. Es fuga (clase 4) con otro disfraz: si mirás los errores y cambiás el prompt,
> ese conjunto ya no es válido para medir. Hace falta un conjunto de test que no se toque.

---

## 11. Las diez referencias

**Lo que le decís, y tiene que incluir el mecanismo:**

> «No las cites sin chequearlas una por una, y esperá que varias no existan. Y no es que
> el modelo sea malo: es que le pediste exactamente lo que peor le sale. Una referencia
> bibliográfica tiene el **formato más predecible que hay en un texto académico** —apellido,
> año, título, revista, volumen, páginas— y los **datos menos predecibles**. El modelo
> produce lo plausible: te va a devolver una estructura impecable con contenido inventado,
> con un apellido que existe, una revista que existe, un año que existe, y un artículo que
> nunca se escribió. Y va a sonar igual de seguro que cuando acierta, porque no tiene
> ninguna manera de sonar distinto.»

**Y qué SÍ puede hacer con esa lista** (esta parte es la que separa el criterio del
rechazo):
- Usarla como **lista de términos de búsqueda** para después buscar en serio, en Scopus,
  Web of Science o Google Scholar.
- Usarla para **descubrir autores o debates** que no conocía, y después ir a buscar qué
  escribieron de verdad.
- Pedirle que le **explique un paper que él ya tiene** y está leyendo (con el texto a la
  vista, que es otra cosa completamente distinta).

> **Bandera roja:** si la respuesta es sólo «no, no lo hagas», falta el mecanismo, y sin
> mecanismo no hay criterio: dentro de un año va a creer que ya se arregló. La consigna
> pedía explicar **por qué**.

---

## 12. Sos revisor

**Un comentario aceptable dice, más o menos, esto:**

**a) Qué falta:** el prompt exacto; la versión precisa del modelo y la fecha de las
consultas; la temperatura y el manejo de la variabilidad entre corridas; una validación
humana independiente sobre una muestra; métricas por clase (precisión, recall, F1) y
matriz de confusión; comparación contra un baseline; qué se hizo con las salidas mal
formateadas o vacías.

**b) Por qué importa cada cosa:**
- **El prompt** es el instrumento de medición. Sin él, el estudio **no es replicable ni en
  principio**: es como publicar una encuesta sin el cuestionario.
- **La versión y la fecha**, porque los modelos cerrados cambian sin aviso. «GPT-4» no
  identifica un modelo.
- **La temperatura**, porque si es mayor que cero el mismo prompt da resultados distintos,
  y entonces hay una fuente de variabilidad no reportada en la medición.
- **La validación humana**, porque sin ella no hay ninguna evidencia de que el
  clasificador mida el constructo. Es el punto central.
- **El baseline**, porque si un diccionario de palabras clave da 89%, el 91% no es un
  hallazgo.

**c) El mínimo para poder evaluar:** prompt completo en apéndice; modelo, versión y fecha;
temperatura; y **una muestra de al menos 200 documentos codificada a mano por humanos, con
las métricas contra esa muestra y el acuerdo entre codificadores**. Sin eso, el resultado
no es evaluable — no es que esté mal: es que no se puede saber.

**d) La trampa — y es la parte que separa una revisión buena de una lista de pedidos:**

La frase problemática es **«una tasa de acuerdo del 91% con nuestras expectativas
teóricas»**.

Eso **no es validación: es confirmación**. Están midiendo cuánto se parece la salida del
modelo a lo que ya creían, y llamando a eso evidencia. Un clasificador que reprodujera
perfectamente sus expectativas daría 100% y no aportaría **ninguna** información; uno que
las contradijera sería descartado por «no funcionar». El criterio de validación tiene que
ser **independiente de la hipótesis**: codificación humana ciega sobre una muestra al azar,
hecha por gente que no sabe qué predice la teoría.

Y hay un problema de medición encima: «tasa de acuerdo» sin la prevalencia de las clases
no dice nada. Si el 88% de los documentos son de una sola clase, un 91% de acuerdo es
apenas mejor que decir siempre lo mismo. Por eso hacen falta precisión, recall y F1 por
clase, y un kappa que corrija por el acuerdo esperado al azar.

> **Para el docente.** Este ítem es el que mejor mide si la clase funcionó, y el que mejor
> conecta con la clase 10. Si alguien encuentra el punto (d) sin ayuda, entendió la
> diferencia entre *que el modelo ande* y *que la medición sea válida*, que es el objetivo
> del curso entero.
>
> Una variante que funciona muy bien como cierre: pedir que escriban el comentario de
> revisor **en el tono con el que les gustaría recibirlo**. Cambia bastante lo que
> escriben, y es una buena conversación sobre el oficio.
