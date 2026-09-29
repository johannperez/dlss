# Glosario vivo

Cada término técnico que aparece en el curso: cómo lo decimos en castellano, qué
es en una línea sin jerga, la analogía con la que lo contamos en clase, y **en
qué clase aparece por primera vez**. Tenelo abierto mientras cursás: la mitad de
la sensación de "no entiendo nada" en deep learning es vocabulario, no conceptos.

**Cómo leer las tablas.** *Término* es como se dice en la práctica (en inglés
cuando así se usa). *Cómo lo decimos* es la traducción que usamos cuando queremos
ser claros. *Qué es* es la definición corta, sin jerga. *La analogía* es la imagen
mental con la que lo presentamos: si te acordás de la analogía, te acordás del
concepto.

Cada término está en la clase **donde aparece por primera vez**. Si volvés a
verlo en la clase 8, buscalo en la 3.
Al final hay un [índice alfabético](#índice-alfabético) y una tabla de
[falsos amigos](#falsos-amigos-y-confusiones-que-valen-oro) que valen oro.

> **Para el equipo que mantiene el curso:** todos los términos de acá se
> verificaron por `grep` contra las diez `slides.html`, los diez `notebook.ipynb`
> y las diez `notas-docente.md`. Si agregás un término a una clase, agregalo acá,
> **en la clase donde aparece por primera vez**, y no lo repitas en las
> siguientes.

---

## Clase 1 — Una función es una máquina con perillas

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **function** | función | Una regla que a cada número de entrada le hace corresponder uno de salida. | Una máquina: le metés un número por un lado y sale otro por el otro. |
| **variable** | variable, entrada | El número que cambia de un caso a otro de tu base. | La bolita que recorre la figura. Te mueve *a lo largo* del dibujo. |
| **parameter** | parámetro, perilla | El número que es el mismo para toda la base y que decide qué figura se dibuja. | La perilla al costado de la máquina. Te *deforma* el dibujo. |
| **model** | modelo | La figura elegida más los valores de sus perillas. | El dibujo que la máquina hace hoy, con las perillas donde están. |
| **to fit** | ajustar | Mover las perillas hasta que la figura se parezca a los datos. | Probar posiciones de las perillas hasta que la curva "abrace" la nube. |
| **optimization** | optimización | Buscar los valores de las perillas que hacen mínimo un número. | Mover perillas para minimizar un número. Nada más místico que eso. |
| **desajuste** | desajuste | Un número que resume qué tan lejos está tu figura de los datos. | El medidor del tablero: cuanto más chico, mejor dibujás. En la clase 3 va a tener nombre propio (*loss*). |
| **familia de funciones** | familia | El conjunto de todas las figuras que una misma fórmula puede dibujar. | Elegir la familia es tuyo; elegir el miembro de la familia lo hace el ajuste. |
| **notebook / Colab** | cuaderno | Una página web donde se escribe y se corre código de a pedacitos. | Un cuaderno de laboratorio que además ejecuta lo que anotás. |
| **numpy / matplotlib** | — | Las dos bibliotecas de Python con las que hacemos cuentas y gráficos. | La calculadora y el papel milimetrado. |

## Clase 2 — Componer funciones: dibujar lo imposible

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **composition** | composición | Encadenar funciones: lo que sale de una entra en la siguiente. | Una cadena de mediaciones: dato bruto → codificación → índice → interpretación. |
| **non-linearity** | no linealidad | Cualquier operación que doble una línea recta. | El doblez. Sin un doblez en el medio, apilar máquinas rectas te devuelve una recta. |
| **ReLU** (*rectified linear unit*) | la rampa | `max(0, x)`: si el número es negativo devuelve cero, si no lo deja pasar. | Una rampa: plancha hasta cierto punto y después sube. La pieza de Lego del curso. |
| **activation function** | función de activación | El nombre técnico del doblez que va entre capa y capa. | ReLU, sigmoide y tanh son tres dobleces distintos. |
| **weight** | peso | Un parámetro que multiplica a lo que entra. | Cuánto pesa esa entrada en la cuenta. |
| **bias** | sesgo, ordenada | Un parámetro que suma, sin multiplicar nada. | Desplaza la figura: el de la salida la corre entera para arriba o para abajo; el de una neurona oculta corre su codo a izquierda o derecha. **Ojo:** no es el "sesgo" social de la clase 10. |
| **neuron** | neurona | Una rampa con sus perillas: multiplicar, sumar y doblar. | Ni una célula ni algo que piense. El nombre viene de una analogía de 1943 que hoy confunde más de lo que ayuda. |
| **layer** | capa | Un grupo de neuronas que miran la misma entrada en paralelo. | Cien codificadores leyendo todos el mismo documento. |
| **hidden layer** | capa oculta | Una capa que no es ni la entrada ni la salida. | "Oculta" sólo quiere decir "del medio". No hay misterio. |
| **deep** | profundo | Muchas capas, una atrás de la otra. | Cinco analistas donde cada uno trabaja sobre la síntesis del anterior. De ahí sale *deep learning*, y de nada más profundo que eso. |
| **universal approximation** | aproximación universal | El teorema que dice que con suficientes rampas se dibuja cualquier figura continua, dentro de un rango acotado (para la rampa, Leshno et al. 1993). | Dice que la figura *existe*; no dice que la vayas a encontrar, ni que sirva para predecir. |
| **dying ReLU** | rampa muerta | Una rampa cuyo codo queda fuera del rango de los datos: nunca se activa y no aporta nada. | Un codificador al que le tocó una parte del corpus que está vacía. |

## Clase 3 — Estar equivocado es un número, y ese número tiene pendiente

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **loss** | pérdida | El número que mide qué tan mal está el dibujo. Más chico es mejor. | El medidor de desajuste de la clase 1, con nombre propio. |
| **loss function / cost function** | función de pérdida, de costo | La receta con la que se calcula ese número. | El criterio. **Y el criterio no viene con los datos: lo escribe alguien.** |
| **MSE** (*mean squared error*) | error cuadrático medio | El promedio de los errores elevados al cuadrado. | Al elevar al cuadrado, un caso extremo pesa muchísimo: la recta se le va atrás. |
| **MAE** (*mean absolute error*) | error absoluto medio | El promedio de los errores sin signo, sin elevar. | Cada caso empuja la recta con la misma fuerza, esté cerca o lejos: un caso extremo no la arrastra. El MSE persigue el promedio; el MAE, la mediana. |
| **gradient** | gradiente | Para qué lado sube la loss si movés un poquito cada perilla. | La flecha que apunta cuesta arriba. Vos vas exactamente al revés. |
| **gradient descent** | descenso por gradiente | Mover las perillas de a pasitos en la dirección contraria al gradiente. | Bajar una colina con niebla: tanteás la pendiente con el pie y das un paso. |
| **learning rate** | tasa de aprendizaje | El número que multiplica a la pendiente para decidir cuánto moverse: paso = tasa × pendiente. | Chico: tardás una eternidad. Enorme: salís despedido de la ladera. Y como multiplica a la pendiente, el paso se achica solo cerca del fondo. |
| **batch** | lote | Cuántos casos mira el modelo antes de mover las perillas una vez. | Censo (todos) contra muestra (un puñado). |
| **mini-batch** | lote chico | Un puñado de casos en vez del conjunto entero. Es lo que se usa siempre. | Encuestar a 400 personas en vez de al país. |
| **SGD** (*stochastic gradient descent*) | descenso estocástico | Descenso por gradiente mirando un lote chico por vez. | "Estocástico" quiere decir "con azar en qué casos mirás". |
| **backpropagation** | retropropagación | El procedimiento que calcula todas las pendientes de una sola pasada hacia atrás. | La contabilidad que reparte la culpa del error, capa por capa. No hace falta saber derivarla para usarla. |
| **Adam** | Adam | Un optimizador que adapta el paso de cada perilla por separado, con algo de inercia. Igual hay que darle un learning rate. | Una pelota con peso: no se frena en cada pocito y acelera en las bajadas largas. |
| **local minimum** | mínimo local | Un pozo del paisaje que no es el pozo más hondo. | Se sale menos seguido de lo que uno teme, y con muchas perillas casi nunca es el problema. |
| **hyperparameter** | hiperparámetro | Un número que elegís vos antes de entrenar, y que el modelo no aprende. | La tasa de aprendizaje y la cantidad de rampas son hiperparámetros; los pesos, no. |
| **proxy** | proxy, medida indirecta | Una variable que usás en lugar de la que te importa, porque la que te importa no se mide. | Menciones en el discurso como proxy de agenda de gobierno. Toda la validez del análisis cuelga de ahí. |

## Clase 4 — El ciclo de entrenamiento, y la diferencia entre dibujar y calcar

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **training loop** | el ciclo de entrenamiento | Las cinco líneas que se repiten miles de veces. | Predecir, comparar, borrar, anotar, mover. `backward()` anota; `step()` mueve. |
| **epoch** | época, pasada | Una pasada completa por todos los datos de entrenamiento. | Leer el corpus entero de punta a punta, una vez. |
| **iteration / step** | iteración, paso | Una vuelta del ciclo: una actualización de las perillas. | Con 1.200 casos y lotes de 200, una época son 6 pasos. No es lo mismo época que paso. |
| **tensor** | tensor | Una tabla de números con las dimensiones que haga falta. | Un número es un tensor; una foto también; un lote de fotos también. |
| **autograd** | derivación automática | La maquinaria de PyTorch que calcula sola todas las pendientes. | Mismo resultado que la resta de la clase 3, otra cuenta: la resta *mide* la pendiente; autograd la *calcula* exacta con la regla de la cadena, para millones de perillas a la vez. |
| **forward** | paso hacia adelante | Meter el dato y sacar la predicción. | La ida. |
| **backward** | paso hacia atrás | Calcular de quién es la culpa del error. | La vuelta. Anota; no mueve nada. |
| **optimizer** | optimizador | El objeto que efectivamente mueve las perillas con lo que anotó el `backward`. | El que gira las perillas después de que el contador dijo cuánto. |
| **overfitting** | sobreajuste | Que el modelo reproduzca tu muestra, ruido incluido, en vez del patrón. | Calcar en vez de dibujar. El codificador que se aprendió las manías del corpus piloto. |
| **underfitting** | subajuste | Que el modelo sea demasiado rígido para la figura. | Ni siquiera ajusta lo que ya vio. |
| **train / validation / test** | entrenamiento / validación / prueba | Lo que el modelo ve para aprender, lo que ves vos para decidir cuándo parar, y lo que nadie toca hasta el final. | El test es el preregistro del aprendizaje automático: se mira **una sola vez**. |
| **early stopping** | parada temprana | Frenar cuando la validación deja de mejorar, aunque el entrenamiento siga bajando. | Levantarse de la mesa cuando ya no aprendés nada nuevo. |
| **data leakage** | fuga de datos | Que algo del test se haya colado en el entrenamiento. | La causa número uno de resultados demasiado buenos para ser ciertos. |
| **regularization** | regularización | Cualquier cosa que le ate las manos al modelo para que no calque. | Menos libertad a propósito. |
| **capacity** | capacidad | Cuánta libertad tiene el modelo para deformarse. | Más capacidad = puede dibujar más figuras = más riesgo de calcar. |
| **dropout** | apagado al azar | Apagar neuronas al azar durante el entrenamiento. | Que ningún codificador del equipo sea imprescindible. |
| **baseline** | línea de base, el piso | El modelo tonto contra el que hay que ganar. | Predecir siempre el promedio, o siempre la clase mayoritaria. Sin baseline, un 0,85 no significa nada. |
| **partición temporal** | partir por tiempo | Entrenar con el pasado y evaluar con el futuro. | La partición honesta cuando la pregunta es predictiva. |
| **partición por grupo** | partir por grupo | Que cada unidad repetida (persona, medio, provincia) caiga entera de un solo lado. | La defensa contra la fuga más común en ciencias sociales. |
| **cross-validation** | validación cruzada | Partir varias veces y promediar, para no depender de una partición con suerte. | Repetir la encuesta con otras muestras y mirar cuánto se mueve el número. |
| **p-hacking** | p-hacking | Probar variantes hasta que el resultado dé, y reportar sólo la que dio. | Mirar el test veinte veces es p-hacking artesanal: más lento y con más pasos. |
| **preregistro** | preregistro | Escribir qué vas a hacer antes de mirar los datos. | El conjunto de test hace de preregistro: lo apartás antes y no lo tocás. |
| **varianza** | varianza | Cuánto se mueve el resultado si cambiás la muestra o la semilla. | Si tu efecto es más chico que ese movimiento, no tenés un efecto. |

## Clase 5 — La forma de los datos manda: imágenes

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **pixel** | píxel | Una casilla de la grilla, con un número de 0 a 255. | La unidad mínima de la foto. Y su vecino de al lado no es un dato cualquiera: es su vecino. |
| **channel** | canal | Cada tabla apilada de la imagen: gris tiene 1, color tiene 3. | Tres calcos superpuestos: rojo, verde y azul. |
| **filter / kernel** | filtro | Una plantillita chica (9 números en un 3×3) que se desliza por la imagen. | El pincel. Y la red aprende sus pinceles. |
| **convolution** | convolución | Deslizar el filtro por toda la imagen, multiplicando de a nueve y sumando. | Pasar una plantilla por toda la foto y anotar dónde encajó. |
| **feature map** | mapa de activación | El dibujo que produce un filtro: dónde apareció eso que busca. | El calco que deja el pincel. |
| **pooling** | submuestreo | Achicar el mapa quedándose con lo más fuerte de cada vecindario. | Resumir cada barrio por su valor más alto. |
| **CNN** (*convolutional neural network*) | red convolucional | La arquitectura que supone que lo importante es local y se repite. | Una teoría sobre el mundo, escrita en forma de red. |
| **translation invariance** | invariancia traslacional | Que el resultado no cambie si el objeto se corre unos píxeles. | Un gato sigue siendo un gato tres píxeles más a la derecha. **Técnicamente:** la convolución *acompaña* el corrimiento (el mapa se corre con la imagen: equivariancia); el que lo *ignora* es el máximo final (invariancia). |
| **inductive bias** | sesgo inductivo | Lo que el modelo supone por diseño, antes de ver un solo dato. | Es una teoría, y puede ser falsa. Igual que un marco teórico. |
| **feature hierarchy** | jerarquía de representaciones | Que cada capa arme sobre lo que armó la anterior. | Bordes → texturas → partes → objetos. |
| **flatten** | aplanar | Estirar la grilla de 28×28 en una fila de 784 números. | Es lo que hace la red densa de esta clase antes de mirar la foto, y es exactamente donde se pierde la vecindad. |
| **parameter sharing** | compartir parámetros | Usar los **mismos** nueve números en toda la imagen. | De ahí sale que una capa convolucional tenga muchísimas menos perillas que una densa. |
| **receptive field** | campo receptivo | Qué pedazo de la foto original influye sobre una unidad. | Crece al apilar capas, no al agrandar el filtro. |
| **stride / padding** | paso / relleno | Cada cuántos píxeles salta el filtro, y cuánto borde se agrega para que entre. | Detalles de plomería: se googlean el día que armes una red. No los estudies. |
| **sandbox** | sandbox, banco de pruebas | Un conjunto de datos neutro que se usa sólo para ver funcionar la técnica. | FashionMNIST es el sandbox de la clase 5. Se rotula como tal y se vuelve al dominio antes de cerrar. |

## Clase 6 — La forma de los datos manda: texto, secuencias y embeddings

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **token** | ficha | El pedacito mínimo en que se parte el texto. Casi siempre una palabra, a veces un pedazo. | "Inconstitucionalidad" sale en varios pedazos, y ninguno es "constitución". |
| **tokenization** | tokenización | Partir el texto en fichas. | Es la primera decisión metodológica del análisis de texto, y casi nadie la reporta. |
| **vocabulary** | vocabulario | La lista de todas las fichas que el modelo conoce. | Si no está en la lista, para el modelo no existe. |
| **OOV** (*out of vocabulary*) | fuera de vocabulario | Una palabra que no está en la lista. | Va a un cajón llamado `<unk>` y **desaparece sin avisar**. |
| **one-hot** | un casillero por palabra | Un vector larguísimo de ceros con un solo uno. | Todas las palabras quedan a la misma distancia entre sí, que es justo lo que no queremos. |
| **embedding** | representación vectorial | Los pocos números que le dan a cada palabra un lugar en un mapa. | Las palabras que se usan parecido quedan cerca. La geometría del mapa *es* el significado que el modelo maneja. |
| **dimension** | dimensión | Cuántos números tiene el vector de cada palabra. | No corresponden a conceptos interpretables, por más ganas que dé. |
| **cosine similarity** | similitud coseno | Qué tan parecido apuntan dos vectores, de −1 a 1. | Dos flechas: importa el ángulo, no el largo. |
| **distributional hypothesis** | hipótesis distribucional | Que el significado de una palabra se deduce de la compañía que frecuenta. | "Conocerás una palabra por la compañía que mantiene" (Firth, 1957). Es el supuesto sustantivo detrás de todos los embeddings. |
| **bag-of-words** | bolsa de palabras | Representar un texto por sus conteos, tirando el orden. | "La comisión rechazó al ministro" y "el ministro rechazó a la comisión" dan el **mismo** vector (una vez que sacás las palabras vacías: «al» contra «a» + «el» cambian un conteo). |
| **RNN** (*recurrent neural network*) | red recurrente | Un modelo que lee palabra por palabra arrastrando una memoria. | Una mochila de tamaño fijo que se va sobrescribiendo: cada palabra nueva entra pisando algo, y lo del principio se va perdiendo. |
| **LSTM** | LSTM | Una RNN con compuertas que deciden qué guardar y qué olvidar. | La misma mochila, con alguien en la puerta que elige qué entra y qué sale. Mejora la memoria; no la arregla. |
| **secuencia** | secuencia | Datos donde el orden es información, no un detalle de presentación. | El texto tiene forma, igual que la imagen. Su forma es el orden. |
| **BPE** (*byte pair encoding*) | fusión de pares frecuentes | El algoritmo que arma las sub-palabras pegando el par de letras que más aparece. | Empieza por letras sueltas y va pegando. El de GPT es éste, en grande. |
| **coocurrencia** | coocurrencia | Cuántas veces dos palabras aparecen cerca en el corpus. | La materia prima de todo embedding. Es una tabla de contingencia. |
| **PPMI** (*positive pointwise mutual information*) | información mutua positiva | ¿Estas dos palabras aparecen juntas más de lo esperable por azar? | Descuenta que "de" esté cerca de todo. Es el residuo de la tabla de contingencia. |
| **SVD** (*singular value decomposition*) | descomposición en valores singulares | Comprimir una tabla enorme a unas pocas dimensiones que conservan lo más importante. | El primo mayor del análisis factorial y del análisis de correspondencias. Ya lo conocés. |
| **word2vec** | word2vec | El método clásico (2013) para entrenar embeddings de palabras. | Lo que hacemos a mano con PPMI+SVD, hecho con una red y en grande. |
| **ley de Zipf** | ley de Zipf | Un puñado de palabras se lleva casi todo el texto. | Pasa en todos los idiomas, y nadie lo diseñó. |
| **hapax legomenon** | dicho una sola vez | Una palabra que aparece exactamente una vez en el corpus. | En los discursos de apertura son casi la mitad del vocabulario. |
| **cambio semántico** | cambio semántico | Que las vecinas de una palabra sean otras en dos períodos distintos. | Se mide entrenando un embedding por época y comparando vecindarios. |
| **spaCy / gensim** | — | Las dos bibliotecas que vas a usar de verdad en tu investigación para texto en castellano. | Lo de hoy es para entender qué hace la rueda cuando te dé un número raro. |

## Clase 7 — Attention: cada palabra arma su propio resumen del contexto

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **attention** | atención | Un promedio ponderado: cada elemento reparte su 100 % entre los demás y se arma un resumen. | Cuando leés "lo" al final de una oración larga, saltás a la palabra que importa. No releíste: miraste directo. |
| **self-attention** | autoatención | Attention de una frase sobre sí misma. | No hay dos textos: la oración se mira a sí misma. |
| **query** | consulta | Lo que una palabra busca. | El aviso clasificado: "busco un sustantivo masculino singular". |
| **key** | clave | El aviso que cada palabra publica. | El cartel: "soy un sustantivo masculino singular". |
| **value** | valor | Lo que una palabra aporta cuando la miran. | Lo que efectivamente te llevás si la mirás, que no es lo mismo que su cartel. |
| **dot product** | producto punto | La cuenta que mide cuánto apuntan dos flechas para el mismo lado. | Mide qué tan bien el aviso y el cartel se corresponden. |
| **softmax** | softmax | Convertir puntajes cualesquiera en porcentajes que suman 100. | Reparte, no inventa: si le da más a una, le da menos a otra. |
| **causal mask** | máscara causal | Taparle el futuro al modelo mientras aprende a generar. | Al predecir la palabra 5 no puede espiar la 6. Sin esto, hace trampa y no aprende nada. |
| **head / multi-head** | cabeza | Una copia del mecanismo de atención con su propio juego de perillas Q, K y V. | Varias cabezas en paralelo, cada una mirando una relación distinta — aunque la mayoría no se deja resumir en un rol lingüístico prolijo, y la clase 7 lo muestra midiendo. |
| **positional encoding** | codificación posicional | Marcarle a cada palabra en qué lugar de la frase está. | El sellito con el número de orden. Sin él (y sin máscara), el transformer también sería una bolsa de palabras. Hoy lo más usado son las posiciones rotatorias (RoPE); el GPT original las aprendía. |
| **residual connection** | conexión residual | Un atajo que suma la entrada sin tocar a la salida de la capa. | El original del expediente, siempre adjunto. Hace entrenables las redes profundas. |
| **layer norm** | normalización | Reescalar los números de cada palabra para que no se disparen entre capa y capa. | Plomería honesta: no aporta ninguna idea, y sin ella no entrena. |
| **transformer block** | bloque transformer | Attention + MLP + dos residuales + dos normalizaciones. | La pieza que se apila. No hay una idea nueva por piso: es el mismo piso, repetido. |
| **MLP** (*multi-layer perceptron*) | red densa, el MLP | La red de capas de la clase 2, metida adentro del bloque. | Attention decide de dónde traer información; el MLP decide qué hacer con lo que trajo. Es la suma de rampas de la clase 2: nunca se fue. |
| **logits** | logits | Los puntajes crudos, antes de convertirlos en probabilidades. | Lo que sale de la última capa y todavía no suma 1. |

## Clase 8 — Un mini-GPT propio, y la traducción a ChatGPT

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **LLM** (*large language model*) | modelo de lenguaje grande | Una máquina que dibuja la distribución de probabilidad de la próxima ficha. | Es la máquina de la clase 1 con un millón y medio de perillas. La misma máquina. |
| **autoregressive** | autorregresivo | Genera de a una ficha: la agrega al texto y vuelve a empezar. | Y por eso, si arrancó mal, sigue por ahí. |
| **bigrama** | bigrama | El modelo de lenguaje más tonto: mirar sólo la ficha anterior y contar qué vino después. | Cero perillas aprendidas, son conteos. Y ya escribe algo. Es la línea de base de la clase. |
| **cross-entropy** | entropía cruzada | La loss de los modelos que predicen una categoría: qué probabilidad le diste a la respuesta que efectivamente vino. | Castiga muchísimo más estar confiadamente equivocado que estar dudando. |
| **sampling** | sorteo, muestreo | Elegir la próxima ficha sorteando sobre la distribución en vez de tomar siempre la más probable. | De acá sale que el mismo prompt dé respuestas distintas. |
| **temperature** | temperatura | La perilla del riesgo al sortear la próxima ficha. | Baja: elige lo más probable y se repite. Alta: arriesga y desbarranca. **No lo hace más inteligente.** |
| **context window** | ventana de contexto | Cuántas fichas puede mirar hacia atrás. | Lo que queda afuera, para el modelo **no existe**. Y en los modelos grandes, lo de adentro tampoco se usa parejo: lo del principio y lo del final se aprovechan mejor que lo del medio (*lost in the middle*, una U). |
| **prompt** | consigna, prompt | El texto con el que arranca la generación. | Elige el género y el registro de lo que sigue. **Es tu instrumento de medición**, y va en el apéndice. |
| **hallucination** | alucinación | Generar algo bien formado y falso, con total confianza. | No es una falla del sistema: es exactamente lo que el sistema hace. Nada adentro detecta que no sabe; si contesta "no sé", es una continuación aprendida, no un chequeo. |
| **instruction tuning** | ajuste por instrucciones | Un segundo entrenamiento que lo convierte de autocompletador en asistente. | Lo que separa a tu mini-GPT de ChatGPT, más que la escala. |
| **RLHF** (*reinforcement learning from human feedback*) | ajuste con preferencias humanas | Afinarlo con juicios de personas sobre qué respuesta es mejor. | La adulación ya asoma sin RLHF y crece con la escala; el RLHF la refuerza (Perez et al. 2022; Sharma et al. 2023). |
| **checkpoint** | punto de guardado | El archivo con los pesos del modelo en un momento dado. | Guardar el checkpoint es guardar el millón y medio de números que *son* el modelo. |
| **emergente** | emergente | Una capacidad que aparece sola al crecer la escala, sin que nadie la programara. | Ojo con la palabra: mucho de lo que se cuenta como emergente en realidad fue **entrenado**. |

## Clase 9 — Usar modelos que ya existen, sin creerles

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **transfer learning** | aprendizaje por transferencia | Aprovechar lo que otro modelo ya aprendió en vez de empezar de cero. | Alguien ya le enseñó castellano; vos sólo le enseñás tu distinción. |
| **modelo pre-entrenado** | modelo pre-entrenado | Un modelo que otro entrenó y publicó, listo para usar o adaptar. | Un informante clave: sabe muchísimo, te ahorra meses, y tiene su posición y sus puntos ciegos. |
| **fine-tuning** | ajuste fino | Seguir entrenando ese modelo con tus ejemplos y tu tarea. | Enseñarle tu campo a alguien que ya sabe el idioma. |
| **freezing** | congelar capas | Dejar quietas las capas de abajo y mover sólo las de arriba. | No es una optimización técnica: es **bajar la capacidad a propósito** para que 200 ejemplos alcancen. |
| **zero-shot** | sin ejemplos | Pedirle la tarea describiéndola con palabras, sin entrenarlo para eso. | Cero etiquetas para entrenarlo, pero igual 200 o 300 para evaluarlo, como todo. Sin esas, no tenés con qué saber si anda. |
| **few-shot** | con poquitos ejemplos | Darle tres o cuatro ejemplos en el prompt y que siga el patrón. | Mostrarle cómo se codifica, en vez de explicárselo. |
| **pipeline** | la cañería | La cadena completa: texto crudo entra, etiqueta sale. | Muy cómoda, y por eso hay que abrirla y mirar qué hace adentro. |
| **sentence embedding** | representación de oración | Un vector para un texto entero, no para una palabra. | Sirve para medir parecido entre documentos de tu corpus. |
| **Hugging Face** | — | El repositorio donde vive la mayoría de los modelos abiertos. | La biblioteca pública de modelos. Se cita como se cita una fuente: con versión. |
| **BETO / RoBERTuito / pysentimiento** | — | Modelos entrenados en castellano (y en castellano rioplatense de redes). | Los informantes que hablan tu idioma. |
| **TF-IDF** | — | Contar palabras dándole más peso a las que son raras en el corpus. | El piso barato del análisis de texto. Muchas veces le gana a algo mucho más caro. |
| **matriz de confusión** | matriz de confusión | La tabla de en qué acertó y en qué se equivocó, discriminando **cómo** se equivocó. | Cuatro casilleros. La diagonal es lo que salió bien; los otros dos son distintos entre sí. |
| **accuracy** | exactitud | De todos los casos, en cuántos acertó. | Con clases desbalanceadas engaña: si el 90 % es "no", decir siempre "no" da 0,90. |
| **precision** | precisión | De lo que marcaste, cuánto era de verdad. | "De cada 100 notas que el modelo llamó protesta, 73 lo eran." |
| **recall** | exhaustividad, cobertura | De lo que había, cuánto encontraste. | "De cada 100 que lo eran, encontró 64." |
| **F1** | F1 | El promedio armónico de precisión y recall. | Un número que esconde dos. Nunca lo reportes solo. |
| **threshold** | umbral | El corte a partir del cual una probabilidad se vuelve un "sí". | Bajarlo sube el recall (o lo deja igual); la precisión tiende a bajar, aunque puede dar saltitos. No hay un umbral que mejore las dos de forma sostenida. La decisión es tuya, no del modelo. |
| **kappa** (*Cohen's kappa*) | kappa de Cohen | Cuánto coinciden dos codificadores, descontando el acuerdo por azar. | Sirve para reportar el acuerdo entre humanos, pero no es el techo del F1: está en otra escala. El techo realista es el acuerdo entre dos humanos medido con **la misma métrica** que el modelo (el F1 de un codificador contra el otro). |
| **muestra estratificada** | muestra estratificada | Elegir al azar pero garantizando casos de cada grupo que te importa. | Que la muestra que leés a mano no sea todo lo fácil. |
| **intervalo de confianza / bootstrap** | banda de incertidumbre | Cuánto se movería tu número con otra muestra. Se estima remuestreando. | Un F1 sin banda es un número sin escala. |

## Clase 10 — Criterio: validez, sesgo, reproducibilidad y el revisor 2

| Término | Cómo lo decimos | Qué es | La analogía de clase |
|---|---|---|---|
| **construct validity** | validez de constructo | ¿Lo que el modelo mide es la cosa de la que estás hablando? | Dos círculos y la brecha entre ellos. Hunde más papers que cualquier métrica. |
| **content validity** | validez de contenido | ¿Tu medida cubre todo el concepto, o sólo la parte fácil de medir? | Medir "participación política" contando marchas. |
| **external validity** | validez externa | ¿Anda fuera de tu muestra, tu período y tu país? | El modelo entrenado con prensa de 2019 aplicado a 2024. |
| **bias** (el de la clase 10) | sesgo | Sesgo social, de muestreo o de medición. | **No** es el parámetro que suma de la clase 2. Mismo inglés, dos cosas completamente distintas. |
| **sesgo de muestreo** | sesgo de muestreo | Tu corpus no representa a la población de la que querés hablar. | Twitter no es la opinión pública. |
| **sesgo de medición** | sesgo de medición | El instrumento mide distinto según a quién. | El mismo texto puntúa distinto si el sujeto cambia de género o de nacionalidad. |
| **sesgo de representación** | sesgo de representación | Lo que el modelo aprendió del mundo tal como está escrito, prejuicios incluidos. | El sesgo del modelo es un dato sobre el corpus. Puede ser un hallazgo, no sólo un problema. |
| **shortcut learning** | atajo | Algo que separa las clases pero **no es el concepto**. | El clasificador de "política" de la clase 10: anda bien en su test y en oraciones de discursos presidenciales (824 oraciones) encuentra 22 de cada 100. Aprendió algo que separa sus dos montones, no el concepto. |
| **spurious correlation** | correlación espuria | Una asociación real en tus datos que no es la relación que te interesa. | La fuente predice la etiqueta al 96 %: tu modelo detecta el medio, no el fenómeno. |
| **ground truth** | verdad de referencia | Lo que tomás como correcto para evaluar. | **Casi nunca es la verdad: es lo que alguien codificó**, con sus instrucciones y su cansancio. |
| **ablation** | ablación | Sacarle algo al corpus o al modelo, reentrenar, y mirar cuánto cae el número. | Ojo: si casi no cae, puede ser que no hubiera atajo o que haya varios que se reemplazan entre sí. Hay que distinguirlo, y medir la caída contra su propio error. |
| **placebo test** | test de placebo | Aplicar el modelo donde el fenómeno **no debería** aparecer. | Si aparece igual, tenés un problema. |
| **invariance test** | test de invariancia | Cambiarle al texto algo que no debería importar (por ejemplo, barajar las palabras) y mirar si la predicción cambia. | No es un placebo: el placebo mira dónde el fenómeno no está; este mira si el modelo es sordo a algo. Con una bolsa de palabras da idéntico por construcción, y eso ya dice qué modelo tenés. |
| **control positivo** | control positivo | El hermano del placebo: aplicarlo donde el fenómeno **tiene que** aparecer. | Si ahí no lo encuentra, tampoco lo encontraba antes. |
| **minimal pair** | par mínimo | Dos textos idénticos salvo por **una** cosa, escritos a mano. | Es un experimento, no una observación. Tres pares mínimos valen más que una métrica. |
| **banda de ruido** | banda de ruido | Cuánto se mueve tu métrica sólo por cambiar la semilla. | Para comparar dos versiones, mirá la *diferencia pareada* entre ellas, semilla por semilla (o partición por partición), con su desvío o su intervalo, no el rango de cada una. Si las particiones comparten casos, el intervalo ingenuo es optimista: corregilo (Nadeau y Bengio 2003). Una diferencia más chica que su propio error no es una diferencia. |
| **out-of-distribution** (OOD) | fuera de dominio | Datos que no se parecen a los del entrenamiento. | Donde todo modelo se rompe, y donde casi nadie lo mide. |
| **MNAR** (*missing not at random*) | faltante no aleatorio | Los agujeros de tus datos tienen una causa, y la causa suele ser sustantiva. | En el corpus de discursos, los años que faltan son los golpes de Estado. |
| **reproducibilidad** | reproducibilidad | Que otro —o vos en seis meses— corra lo mismo y obtenga lo mismo. | Semilla, versiones, datos y código. Con la misma máquina y las mismas versiones, da lo mismo; con otras versiones de las librerías, los números cambian un poco, y por eso se reportan. |
| **seed** | semilla | El número que hace repetible el azar. | En este curso siempre es **1983**. |
| **model card** | ficha del modelo | La media página que dice con qué se entrenó, para qué sirve y para qué **no**. | El prospecto del instrumento. Si publicás el número, publicás la ficha. |
| **datasheet** | ficha de datos | Lo mismo, pero para el corpus: cómo se recolectó, quién etiquetó, con qué instrucciones, qué se excluyó. | Es la sección de fuentes que ya escribías, con más disciplina. |
| **scraping** | scraping | Bajar datos de la web de manera automática. | Que sea público no quiere decir que sea tuyo, ni que la gente haya consentido a este uso. |
| **consentimiento** | consentimiento | Que la gente haya aceptado **este** uso, no un uso parecido de hace ocho años. | La pregunta no es "¿es legal?", es "¿habría dado consentimiento para esto?". |
| **interpretabilidad** | interpretabilidad | Cuánto podés explicar por qué el modelo dijo lo que dijo. | Es lo que se paga por la flexibilidad. A veces una regresión te sirve más. |

---

## Falsos amigos y confusiones que valen oro

| Se parecen | Pero | Dónde se aclara |
|---|---|---|
| **bias** (parámetro) vs **bias** (sesgo social) | El primero es un número que suma; el segundo es un problema de validez. Mismo inglés, cosas distintas. | Clases 2 y 10 |
| **parámetro** vs **hiperparámetro** | El parámetro lo aprende el modelo; el hiperparámetro lo elegís vos (tasa de aprendizaje, cantidad de capas). | Clase 3 |
| **época** vs **paso** | Una época son todos los datos una vez; un paso es una actualización de las perillas. Con lotes chicos, una época son muchos pasos. | Clase 4 |
| **validación** vs **prueba** (*test*) | Con validación decidís cuándo parar. El test se toca **una sola vez**. Si lo mirás dos veces, ya es validación. | Clase 4 |
| **precisión** (*precision*) vs **exactitud** (*accuracy*) | Precisión es "de lo que marqué, cuánto acerté". Exactitud es "de todo, cuánto acerté". Con clases desbalanceadas se separan muchísimo. | Clase 9 |
| **desempeño** vs **validez** | ¿Acierta? y ¿mide lo que digo que mide? son dos preguntas distintas, y la segunda no se contesta con métricas. | Clases 9 y 10 |
| **attention** vs atención en el sentido corriente | El mapa de atención dice por dónde pasó la información, **no** por qué el modelo decidió. No es una explicación. | Clase 7 |
| **deep** (profundo) vs profundo (interesante) | Quiere decir "con muchas capas". Nada más. | Clase 2 |
| **token** (ficha) vs palabra | Una ficha puede ser media palabra. Por eso el modelo no sabe contar letras. | Clases 6 y 8 |
| **loss** vs error de medición | La loss es un criterio que elegís vos para entrenar; el error de medición es una propiedad de tus datos. | Clase 3 |
| **ReLU** (la rampa) vs escalón | La rampa tiene pendiente; el escalón no. Sin pendiente no hay gradiente, y sin gradiente no se aprende. | Clases 1 y 2 |

---

## Índice alfabético

El número es **la clase donde el término aparece por primera vez**.

ablation 10 · accuracy 9 · activation function 2 · Adam 3 · aplanar (*flatten*) 5 ·
aproximación universal 2 · attention 7 · autograd 4 · autoregressive 8 ·
backpropagation 3 · backward 4 · bag-of-words 6 · banda de ruido 10 · baseline 4 ·
batch 3 · BETO 9 · bias (parámetro) 2 · bias (sesgo) 10 · bigrama 8 · BPE 6 ·
cabeza (*head*) 7 · cambio semántico 6 · campo receptivo 5 · canal 5 · capa 2 ·
capa oculta 2 · capacidad 4 · checkpoint 8 · CNN 5 · Colab 1 · composición 2 ·
conexión residual 7 · congelar (*freezing*) 9 · consentimiento 10 ·
context window 8 · control positivo 10 · convolución 5 · coocurrencia 6 ·
correlación espuria 10 · cosine similarity 6 · cross-entropy 8 ·
cross-validation 4 · datasheet 10 · deep 2 · desajuste 1 · descenso por gradiente 3 ·
dimensión 6 · dot product 7 · dropout 4 · dying ReLU 2 · early stopping 4 ·
embedding 6 · emergente 8 · época (*epoch*) 4 · F1 9 · familia de funciones 1 ·
feature map 5 · few-shot 9 · filtro (*kernel*) 5 · fine-tuning 9 · forward 4 ·
fuga de datos 4 · función 1 · gensim 6 · gradiente 3 · ground truth 10 ·
hapax legomenon 6 · hiperparámetro 3 · hipótesis distribucional 6 ·
Hugging Face 9 · instruction tuning 8 · interpretabilidad 10 ·
intervalo de confianza 9 · invariancia traslacional 5 · iteración 4 ·
jerarquía de representaciones 5 · kappa 9 · key 7 · layer norm 7 ·
learning rate 3 · ley de Zipf 6 · LLM 8 · local minimum 3 · logits 7 · loss 3 ·
LSTM 6 · MAE 3 · máscara causal 7 · matriz de confusión 9 · matplotlib 1 ·
minimal pair 10 · mini-batch 3 · MLP 7 · MNAR 10 · model card 10 · modelo 1 ·
modelo pre-entrenado 9 · MSE 3 · muestra estratificada 9 · neurona 2 ·
no linealidad 2 · notebook 1 · numpy 1 · one-hot 6 · OOV 6 ·
optimización 1 · optimizador 4 · out-of-distribution 10 · overfitting 4 ·
p-hacking 4 · par mínimo 10 · parámetro 1 · partición por grupo 4 ·
partición temporal 4 · peso (*weight*) 2 · pipeline 9 · píxel 5 · pooling 5 ·
positional encoding 7 · PPMI 6 · precision 9 · preregistro 4 · prompt 8 ·
proxy 3 · query 7 · recall 9 · regularización 4 · ReLU 2 · reproducibilidad 10 ·
RLHF 8 · RNN 6 · RoBERTuito 9 · sampling 8 · sandbox 5 · secuencia 6 ·
self-attention 7 · semilla (*seed*) 10 · sentence embedding 9 ·
sesgo de medición 10 · sesgo de muestreo 10 · sesgo de representación 10 ·
sesgo inductivo 5 · SGD 3 · shortcut learning 10 · softmax 7 · spaCy 6 ·
stride / padding 5 · subajuste 4 · SVD 6 · temperature 8 · tensor 4 ·
test de invariancia 10 · test de placebo 10 · TF-IDF 9 · threshold 9 · to fit 1 · token 6 ·
tokenización 6 · train / validation / test 4 · training loop 4 ·
transfer learning 9 · transformer block 7 · validez de constructo 10 ·
validez de contenido 10 · validez externa 10 · value 7 · variable 1 ·
varianza 4 · ventana de contexto 8 · vocabulario 6 · word2vec 6 · zero-shot 9
