# Glosario vivo

Cada término técnico que aparece en el curso, qué quiere decir en castellano, la
analogía que usamos en clase y **en qué clase se introdujo**. Tenelo abierto
mientras cursás: la mitad de la sensación de "no entiendo nada" en deep learning
es vocabulario, no conceptos.

> **Para el equipo que construye una clase:** cuando introduzcas un término nuevo,
> agregalo acá **en la clase en que aparece por primera vez**. Si ya está, no lo
> repitas: enlazá. La regla del curso es que ningún término en inglés se usa sin
> haberlo explicado en castellano la primera vez.

**Cómo leer la tabla.** *Término* es como se dice (en inglés si así se usa en la
práctica). *En castellano* es la traducción que usamos cuando queremos ser
claros. *La analogía* es la imagen mental con la que lo presentamos en clase: si
te acordás de la analogía, te acordás del concepto.

---

## Clase 1 — Una función es una máquina con perillas

| Término | En castellano | La analogía de clase |
|---|---|---|
| **función** | función | Una máquina: le metés un número por un lado y sale otro por el otro. |
| **variable** | variable, entrada | La bolita que recorre la figura. Cambia dentro de un mismo dibujo. |
| **parámetro** | parámetro, perilla | La perilla que deforma la figura entera. No cambia mientras dibujás. |
| **ajustar** (*to fit*) | ajustar | Mover las perillas hasta que la figura se parezca a los datos. |
| **optimización** | optimización | Mover perillas para minimizar un número. Nada más místico que eso. |
| **desajuste** | desajuste | El número que dice qué tan mal está tu dibujo. En la clase 3 va a tener nombre propio: *loss*. |

## Clase 2 — Componer funciones: dibujar lo imposible

| Término | En castellano | La analogía de clase |
|---|---|---|
| **composición** | composición | Encadenar máquinas: la salida de una es la entrada de la siguiente. |
| **no linealidad** | no linealidad | El doblez. Sin un doblez en el medio, apilar máquinas rectas te vuelve a dar una recta. |
| **ReLU** | rampa | `max(0, x)`: plancha lo negativo, deja pasar lo positivo. La pieza de Lego del curso. |
| **activación** (*activation*) | función de activación | El nombre técnico del doblez. ReLU, sigmoide y tanh son activaciones. |
| **peso** (*weight*) | peso | Un parámetro que multiplica. Cuánto pesa esa entrada en la cuenta. |
| **sesgo** (*bias*) | sesgo, ordenada | Un parámetro que suma. Corre la figura para arriba o para abajo. **Ojo:** no es el "sesgo" de la clase 10, que es otra cosa entera. |
| **neurona** | neurona | Una rampa con sus perillas. El nombre viene de una analogía biológica de 1943 que hoy confunde más de lo que ayuda. |
| **capa** (*layer*) | capa | Un montón de rampas trabajando en paralelo sobre la misma entrada. |
| **capa oculta** (*hidden layer*) | capa oculta | Una capa que no es ni la entrada ni la salida. "Oculta" sólo quiere decir "del medio". |
| **profundo** (*deep*) | profundo | Muchas capas apiladas. De ahí sale *deep learning*, y no de nada más profundo que eso. |
| **aproximación universal** | aproximación universal | El teorema que dice que con suficientes rampas dibujás cualquier figura. Dice que *existe*; no dice que la vayas a encontrar. |

## Clase 3 — Estar equivocado es un número, y ese número tiene pendiente

| Término | En castellano | La analogía de clase |
|---|---|---|
| **loss** | función de pérdida, costo | El medidor de desajuste de la clase 1, con nombre. Un número: más chico es mejor. |
| **MSE** (*mean squared error*) | error cuadrático medio | El promedio de los palitos al cuadrado. Al elevar al cuadrado, los casos extremos pesan muchísimo. |
| **MAE** (*mean absolute error*) | error absoluto medio | El promedio de los palitos sin elevar. Los casos extremos pesan igual que el resto. |
| **gradiente** (*gradient*) | gradiente | La flecha que apunta para dónde sube más rápido el terreno. Vos vas al revés. |
| **descenso por gradiente** (*gradient descent*) | descenso por gradiente | Soltar una pelota en un valle con niebla: mirás la pendiente bajo tus pies y das un paso cuesta abajo. |
| **learning rate** | tasa de aprendizaje | El largo del paso. Chico: tardás una eternidad. Enorme: salís despedido. |
| **batch** | lote | Cuántos casos mirás antes de mover las perillas una vez. |
| **mini-batch** | lote chico | Un puñado de casos en vez de todo el conjunto. Es lo que se usa siempre. |
| **SGD** (*stochastic gradient descent*) | descenso estocástico | Descenso por gradiente mirando un lote chico por vez. "Estocástico" = con azar en qué casos mirás. |
| **backpropagation** | retropropagación | La contabilidad que reparte la culpa del error hacia atrás, capa por capa. No hace falta saber derivarla para usarla. |
| **Adam** | Adam | Un optimizador que ajusta solo el largo del paso. Es el que usa todo el mundo por defecto. |
| **mínimo local** | mínimo local | Un pozo que no es el pozo más hondo. Se sale menos seguido de lo que uno teme. |

## Clase 4 — El ciclo de entrenamiento, y la diferencia entre dibujar y calcar

| Término | En castellano | La analogía de clase |
|---|---|---|
| **training loop** | el ciclo de entrenamiento | Las cinco líneas que se repiten: predecir, comparar, borrar, anotar, mover. |
| **época** (*epoch*) | época, pasada | Una pasada completa por todos los datos de entrenamiento. |
| **batch** | lote | El puñado de casos que el modelo mira por vez. Con 1200 casos y lotes de 200, una época son 6 iteraciones. |
| **iteración** | iteración, paso | Una vuelta al ciclo: una actualización de las perillas. No es lo mismo que una época, salvo que los datos entren en un solo lote. |
| **tensor** | tensor | Una tabla de números con la cantidad de dimensiones que haga falta. Un número es un tensor; una foto también. |
| **autograd** | derivación automática | La maquinaria de PyTorch que calcula todas las pendientes sola. Es la resta de la clase 3, hecha exacta y para millones de perillas. |
| **forward** | paso hacia adelante | Meter el dato y sacar la predicción. |
| **backward** | paso hacia atrás | Calcular de quién es la culpa del error. |
| **optimizador** | optimizador | El que efectivamente mueve las perillas con lo que dijo el `backward`. |
| **overfitting** | sobreajuste | Calcar en vez de dibujar: el modelo se aprendió tu muestra de memoria, ruido incluido. |
| **underfitting** | subajuste | El modelo es demasiado rígido para la figura. Ni siquiera ajusta lo que vio. |
| **train / val / test** | entrenamiento / validación / prueba | Lo que el modelo ve para aprender, lo que ve para que vos decidas cuándo parar, y lo que **nunca** ve hasta el final. |
| **early stopping** | parada temprana | Parar cuando la validación empieza a empeorar, aunque el entrenamiento siga mejorando. |
| **fuga de datos** (*data leakage*) | fuga | Cuando algo del test se coló en el train. La causa número uno de resultados demasiado buenos para ser ciertos. |
| **regularización** | regularización | Cualquier cosa que le ate las manos al modelo para que no calque. |
| **capacidad** | capacidad | Cuánta libertad tiene el modelo para deformarse. Más capacidad = más riesgo de calcar. |
| **dropout** | apagado al azar | Apagar neuronas al azar mientras se entrena, para que el modelo no dependa de ninguna en particular. |
| **baseline** | línea de base | El modelo tonto contra el que hay que ganar (predecir siempre el promedio, o siempre la clase mayoritaria). Sin baseline, un número no significa nada. |
| **partición temporal** | partir por tiempo | Entrenar con el pasado y testear con el futuro. La partición honesta cuando la pregunta es predictiva. |
| **partición por grupo** | partir por grupo | Que cada unidad repetida (persona, medio, provincia) caiga entera de un solo lado. La defensa contra la fuga más común en ciencias sociales. |

## Clase 5 — La forma de los datos manda: imágenes

| Término | En castellano | La analogía de clase |
|---|---|---|
| **píxel** | píxel | Una celda de la grilla. Un número (o tres, si hay color). |
| **canal** (*channel*) | canal | Cada capa de color de la imagen: rojo, verde, azul. |
| **filtro / kernel** | filtro, pincel | Una plantillita chica que se desliza por la imagen buscando un patrón. |
| **convolución** | convolución | Deslizar el filtro por toda la imagen y anotar dónde encajó. |
| **mapa de activación** (*feature map*) | mapa de activación | El resultado de pasar un filtro: dónde apareció eso que el filtro busca. |
| **pooling** | agrupamiento | Achicar la imagen quedándose con lo más fuerte de cada vecindario. |
| **CNN** (*convolutional neural network*) | red convolucional | La arquitectura que supone que lo que importa es local y se repite. |
| **invariancia traslacional** | invariancia a la traslación | Un gato sigue siendo un gato aunque esté corrido tres píxeles. |
| **sesgo inductivo** (*inductive bias*) | sesgo inductivo | Los supuestos que la arquitectura trae de fábrica sobre cómo es el mundo. **Es una teoría, y puede ser falsa.** |
| **jerarquía de representaciones** | jerarquía | Bordes → texturas → partes → objetos. Cada capa arma sobre la anterior. |
| **aplanar** (*flatten*) | aplanar | Estirar la grilla de 28×28 en una fila de 784 números. Es lo que hacía la red de la clase 4, y es donde se pierde la vecindad. |
| **compartir parámetros** (*parameter sharing*) | compartir parámetros | Los **mismos** nueve números recorren toda la imagen. Es de dónde sale que una capa convolucional tenga 170 veces menos perillas que una densa. |
| **campo receptivo** (*receptive field*) | campo receptivo | Qué pedazo de la foto original influye sobre una unidad. Crece al apilar capas, no al agrandar el filtro. |

## Clase 6 — La forma de los datos manda: texto, secuencias y embeddings

| Término | En castellano | La analogía de clase |
|---|---|---|
| **token** | ficha, pedacito | La unidad mínima en que se parte el texto. No siempre es una palabra. |
| **tokenización** | tokenización | Partir el texto en fichas. "Inconstitucionalidad" puede salir en cuatro pedazos. |
| **vocabulario** | vocabulario | La lista de todas las fichas que el modelo conoce. |
| **OOV** (*out of vocabulary*) | fuera de vocabulario | Una palabra que el modelo nunca vio. Suele terminar en un cajón llamado `<unk>`. |
| **one-hot** | uno-caliente | Un vector larguísimo de ceros con un solo uno. Todas las palabras quedan igual de lejos entre sí, que es justo lo que no queremos. |
| **embedding** | representación vectorial | Darle a cada palabra un lugar en un espacio, de manera que las que se usan parecido queden cerca. |
| **dimensión** | dimensión | Cuántos números tiene el vector de cada palabra. No corresponden a conceptos interpretables, por más que dé ganas. |
| **similitud coseno** | similitud coseno | Qué tan alineadas apuntan dos flechas. 1 = misma dirección, 0 = perpendiculares. |
| **hipótesis distribucional** | hipótesis distribucional | "Sabrás una palabra por la compañía que tiene." Es el supuesto sustantivo detrás de todos los embeddings. |
| **bag-of-words** | bolsa de palabras | Contar palabras y tirar el orden. Funciona sorprendentemente bien, y por eso hay que saber qué se pierde. |
| **RNN** (*recurrent neural network*) | red recurrente | Leer palabra por palabra arrastrando una mochila de memoria. |
| **LSTM** | LSTM | Una RNN con una mochila más grande y con candados. Mejora la memoria; no la arregla. |
| **secuencia** | secuencia | Datos donde el orden es información, no un detalle de presentación. |
| **BPE** (*byte pair encoding*) | fusión de pares frecuentes | El algoritmo que arma las sub-palabras: arranca por letras y va pegando el par que más aparece. El de GPT es éste, en grande. |
| **coocurrencia** | coocurrencia | Cuántas veces dos palabras aparecen cerca. Es la materia prima de todo embedding. |
| **PPMI** (*positive pointwise mutual information*) | información mutua positiva | ¿Estas dos palabras aparecen juntas más de lo esperable por azar? Descuenta que «de» esté cerca de todo. Es el residuo de una tabla de contingencia. |
| **ley de Zipf** | ley de Zipf | Un puñado de palabras se lleva casi todo el texto y la mayoría del vocabulario aparece poquísimo. Pasa en todos los idiomas y nadie lo diseñó. |
| **hapax legomenon** | dicho una sola vez | Una palabra que aparece exactamente una vez en el corpus. En los discursos de apertura son el **45,6 %** del vocabulario. |
| **cambio semántico** | cambio semántico | Que las vecinas de una palabra sean otras en dos períodos distintos. Se mide entrenando un embedding por época. |

## Clase 7 — Attention: cada palabra arma su propio resumen del contexto

| Término | En castellano | La analogía de clase |
|---|---|---|
| **attention** | atención | Cada palabra mira a todas las demás y decide a cuál prestarle atención. Sin releer, sin acordarse: mirando directo. |
| **self-attention** | auto-atención | Attention de una frase sobre sí misma. |
| **query** | consulta | El aviso clasificado: "busco un sustantivo masculino singular". |
| **key** | clave | El cartel que cada palabra levanta: "soy un sustantivo masculino singular". |
| **value** | valor | Lo que la palabra efectivamente aporta si la mirás. |
| **producto punto** (*dot product*) | producto punto | La cuenta que mide qué tan bien el aviso y el cartel se corresponden. |
| **softmax** | softmax | Convertir puntajes cualesquiera en porcentajes que suman 1. |
| **máscara causal** | máscara causal | Taparle el futuro al modelo, para que al predecir la palabra 5 no pueda espiar la 6. |
| **cabeza** (*head*) | cabeza | Una copia del mecanismo de atención mirando una relación distinta. |
| **multi-head** | atención de varias cabezas | Varias cabezas en paralelo: una sigue la sintaxis, otra la correferencia, otra vaya a saber qué. |
| **positional encoding** | codificación de posición | Ponerle a cada palabra una marca de en qué lugar de la frase está. Sin eso, attention no distingue el orden. |
| **conexión residual** (*residual / skip connection*) | conexión residual | Un atajo que deja pasar la entrada sin tocar, sumada a la salida. Hace entrenables las redes profundas. |
| **normalización** (*layer norm*) | normalización | Reescalar los números para que no se disparen entre capa y capa. Plomería, pero plomería necesaria. |
| **bloque transformer** | bloque transformer | Attention + MLP + residuales + normalización. La pieza que se apila. |

## Clase 8 — Un mini-GPT propio, y la traducción a ChatGPT

| Término | En castellano | La analogía de clase |
|---|---|---|
| **LLM** (*large language model*) | modelo de lenguaje grande | Una máquina de dibujar la distribución de la próxima ficha. Todo lo demás sale de ahí. |
| **modelo autorregresivo** | autorregresivo | Predice la ficha siguiente, la agrega, y vuelve a empezar con eso adentro. |
| **bigrama** | bigrama | El modelo de lenguaje más tonto: mirar sólo la ficha anterior y contar qué vino después. La línea de base de la clase. |
| **muestreo** (*sampling*) | sorteo | Elegir la próxima ficha sorteando sobre la distribución, en vez de tomar siempre la más probable. Es de acá que sale la irreproducibilidad. |
| **cross-entropy** | entropía cruzada | La loss de los modelos que predicen una categoría: castiga estar seguro y equivocado. |
| **logits** | logits | Los puntajes crudos, antes de convertirlos en probabilidades con softmax. |
| **temperatura** | temperatura | La perilla del riesgo. Baja: elige siempre lo más probable y repite. Alta: arriesga y desbarranca. **No lo hace más inteligente.** |
| **ventana de contexto** (*context window*) | ventana de contexto | Cuántas fichas puede mirar de una. Lo que queda afuera, para el modelo no existe. |
| **prompt** | consigna, prompt | El texto con el que arranca. Elige el género y el registro de lo que sigue. |
| **alucinación** (*hallucination*) | alucinación | Cuando genera algo bien formado y falso. No es una falla del sistema: es exactamente lo que el sistema hace. |
| **instruction tuning** | ajuste por instrucciones | Enseñarle a responder consignas en vez de sólo completar texto. |
| **RLHF** (*reinforcement learning from human feedback*) | ajuste con preferencias humanas | Afinarlo con juicios de personas sobre qué respuesta es mejor. De acá sale, entre otras cosas, la adulación. |

## Clase 9 — Usar modelos que ya existen, sin creerles

| Término | En castellano | La analogía de clase |
|---|---|---|
| **transfer learning** | aprendizaje por transferencia | Aprovechar lo que otro modelo ya aprendió, en vez de empezar de cero. |
| **modelo pre-entrenado** | modelo pre-entrenado | Un informante clave: sabe muchísimo y tiene sus sesgos. Se lo usa y se lo valida. |
| **fine-tuning** | ajuste fino | Seguir entrenando un modelo ajeno con tus datos y tu tarea. |
| **congelar capas** (*freezing*) | congelar | Dejar quietos los parámetros de las primeras capas y mover sólo los últimos. |
| **zero-shot** | sin ejemplos | Pedirle la tarea sin entrenarlo para eso. |
| **few-shot** | con pocos ejemplos | Darle tres o cuatro ejemplos en el prompt y que siga el patrón. |
| **pipeline** | flujo, cañería | La cadena completa de pasos: texto crudo → tokens → modelo → etiqueta. |
| **embeddings de oración** | representación de oración | Un vector para un texto entero, no para una palabra. Sirve para medir parecido entre documentos. |
| **matriz de confusión** | matriz de confusión | La tabla de en qué acertó y en qué se equivocó, discriminando **cómo** se equivocó. |
| **precisión** (*precision*) | precisión | De lo que marcaste, cuánto era de verdad. |
| **recall** | exhaustividad, cobertura | De lo que había, cuánto encontraste. |
| **F1** | F1 | El promedio armónico de precisión y recall. Un número que esconde dos. |
| **baseline** | línea de base | El modelo tonto contra el que hay que comparar. Sin baseline, un 85% no significa nada. |
| **kappa** (*Cohen's kappa*) | kappa de Cohen | Acuerdo entre dos codificadores descontando el acuerdo por azar. |
| **umbral** (*threshold*) | umbral | El corte a partir del cual una probabilidad se vuelve un "sí". Moverlo cambia precisión y recall en direcciones opuestas. |

## Clase 10 — Criterio: validez, sesgo, reproducibilidad y el revisor 2

| Término | En castellano | La analogía de clase |
|---|---|---|
| **validez de constructo** | validez de constructo | ¿Lo que el modelo mide es lo que decís que mide? La pregunta que hunde más papers que cualquier métrica. |
| **validez de contenido** | validez de contenido | ¿Tu medida cubre todo el concepto, o sólo la parte fácil de medir? |
| **validez externa** | validez externa | ¿Anda fuera de tu muestra, tu período y tu país? |
| **sesgo** (*bias*, el de la clase 10) | sesgo | Aquí es sesgo social o de muestreo, **no** el parámetro que suma de la clase 2. Es el mismo inglés para dos cosas distintas. |
| **sesgo de muestreo** | sesgo de muestreo | Tu corpus no representa a la población de la que querés hablar. |
| **sesgo de medición** | sesgo de medición | El instrumento mide distinto según a quién. |
| **sesgo de representación** | sesgo de representación | Lo que el modelo aprendió del mundo tal como está escrito, incluidos sus prejuicios. |
| **ground truth** | verdad de referencia | Lo que tomás como correcto para evaluar. **Casi nunca es la verdad: es lo que alguien codificó.** |
| **reproducibilidad** | reproducibilidad | Que otro (o vos en seis meses) pueda correr lo mismo y obtener lo mismo. Semilla, versiones y datos. |
| **semilla** (*seed*) | semilla | El número que hace repetible el azar. En este curso siempre es **1983**. |
| **ficha de modelo** (*model card*) | ficha de modelo | El documento que dice con qué datos se entrenó, para qué sirve y para qué no. |
| **MNAR** (*missing not at random*) | faltante no aleatorio | Los agujeros de tus datos tienen una causa, y esa causa suele ser sustantiva. En el corpus de discursos, los años que faltan son los golpes de Estado. |
| **shortcut learning** | atajo | El modelo aprendió algo que separa las clases pero **no es el concepto**: un nombre propio, el medio, el día de la semana. Sube el F1 igual, y no sobrevive fuera del corpus. |
| **ablación** (*ablation*) | ablación | Sacarle algo al modelo o al corpus, reentrenar, y mirar cuánto cae el número. Ojo: en la clase 10 se mide que **casi no cae**, porque los atajos son redundantes. |
| **test de placebo** | test de placebo | Aplicar el modelo a un corpus donde el fenómeno **no debería** aparecer. Si aparece igual, tenés un problema. |
| **control positivo** | control positivo | Su hermano: aplicarlo donde el fenómeno **tiene que** aparecer. Si ahí no lo encuentra, tampoco lo encontraba antes. |
| **par mínimo** (*minimal pair*) | par mínimo | Dos textos idénticos salvo por **una** cosa, escritos a mano. Es un experimento, no una observación. |
| **banda de ruido** | banda de ruido | Cuánto se mueve tu métrica sólo por cambiar la semilla de la partición. Un test que se mueve menos que eso no es un test. |
| **out-of-distribution** (OOD) | fuera de dominio | Datos que no se parecen a los del entrenamiento. Es donde todo modelo se rompe y donde casi nadie lo mide. |
| **ficha de dataset** (*datasheet*) | ficha de datos | Lo mismo que la ficha de modelo, pero para el corpus: cómo se recolectó, quién etiquetó, con qué instrucciones, qué se excluyó. |

---

## Falsos amigos y confusiones que valen oro

| Se parecen | Pero | Dónde se aclara |
|---|---|---|
| **sesgo** (*bias*, parámetro) vs **sesgo** (social) | El primero es un número que suma; el segundo es un problema de validez. Mismo inglés, cosas distintas. | Clases 2 y 10 |
| **parámetro** vs **hiperparámetro** | El parámetro lo aprende el modelo; el hiperparámetro lo elegís vos (learning rate, cantidad de capas). | Clase 3 |
| **validación** vs **prueba** (*test*) | Con validación decidís cuándo parar. El test se toca **una sola vez**, al final. Si lo mirás dos veces, ya es validación. | Clase 4 |
| **precisión** (*precision*) vs **exactitud** (*accuracy*) | Precisión es "de lo que marqué, cuánto acerté". Exactitud es "de todo, cuánto acerté". Con clases desbalanceadas se separan muchísimo. | Clase 9 |
| **atención** (*attention*) vs atención en el sentido corriente | El mapa de atención dice a dónde mira el cálculo, **no** en qué "se fija" el modelo en sentido interpretativo. No es una explicación. | Clase 7 |
| **profundo** (*deep*) vs profundo (interesante) | Quiere decir "con muchas capas". Nada más. | Clase 2 |
