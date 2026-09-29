# Clase 3 — Cuestionario, soluciones comentadas

**Para quien corrige.** Lo que importa acá no es la letra correcta: es **qué revela cada
distractor**. Cada pregunta trae, además de la respuesta, qué confusión tiene alguien que
eligió cada una de las otras opciones y qué decirle. Si una opción equivocada se repite en
más de tres personas, es una señal de que hay que volver sobre esa slide antes de la clase 4.

---

## 1. ¿Qué es una función de pérdida? — **b)**

**Correcta:** *«un número que resume, en una sola cifra, qué tan mal está el modelo sobre
todos los datos, según un criterio que elige quien modela».*
Las dos mitades importan: **resume todos los casos en un número** y **el criterio lo elige
una persona**. Si en la respuesta falta la segunda mitad, la clase se entendió a medias.

| Si eligió | Qué confusión revela | Qué decirle |
|---|---|---|
| **a)** el error de un caso | Confunde el error individual (un palito rojo) con el resumen de todos. Es la confusión más benigna y la más común. | «Eso es *un* error. La loss es lo que hacés con los treinta y seis palitos para que quede un solo número.» |
| **c)** información que se pierde | Se enganchó con la palabra «pérdida» y la leyó en su sentido cotidiano. Pasa siempre con la traducción. | Es un buen momento para insistir en que *loss* acá no tiene nada que ver con perder información: es «qué tan mal». |
| **d)** los casos extremos que conviene sacar | Mezcla la loss con la limpieza de datos: piensa que «manejar los outliers» es algo que se hace *antes* y no *con* la loss. Es la confusión que la slide 8 quiere desarmar. | «Sacar casos también es una decisión, y ésa sí hay que justificarla. La loss es otra cosa: el criterio con el que el modelo resume *todos* los errores, incluidos los de los casos raros. Elegir MAE es una manera de que un caso extremo no mande, sin sacarlo.» |

*Nota para quien corrige.* Una versión anterior de este cuestionario tenía como d) «el
porcentaje de casos que el modelo clasifica mal». Se cambió porque era defendible como
correcta. Si alguien lo pregunta, la respuesta es útil igual: ese porcentaje es una
**métrica** para evaluar, no la loss que se optimiza en clasificación. No se puede bajar con
gradiente (es plano casi en todas partes y salta de golpe), y por eso para clasificar se
entrena con entropía cruzada y se *reporta* el porcentaje de aciertos. Vuelve en la clase 9.

---

## 2. ¿Qué representa cada punto del mapa? — **c)**

**Correcta:** *una recta completa: un par de valores de las dos perillas.*

| Si eligió | Qué confusión revela | Qué decirle |
|---|---|---|
| **a)** un caso de la base | **Es LA confusión de la clase**: espacio de datos contra espacio de parámetros. Si más de un tercio del aula la eligió, hay que rehacer la slide 12 antes de la clase 4, sin excepción. | Volvé a la viz `valle-de-loss.html` y arrastrá el punto delante de ellos. «Mirá: la nube de la derecha no se mueve. Se mueve la recta.» |
| **b)** un año de la serie | La misma confusión que a), un poco más específica. | Igual que a). Frase: «en este mapa no hay ningún año. Buscá el eje de los años: no está». |
| **d)** la loss en una iteración | Confunde el **mapa** (dónde estás) con la **curva de loss** (cómo bajó con el tiempo). Es una confusión sutil y vale la pena tratarla con respeto: son dos gráficos que efectivamente aparecen juntos. | «El mapa no tiene tiempo adentro; existe antes de que empieces a entrenar. La curva sí: es el diario de viaje.» |

---

## 3. El caso extremo mal cargado

**a)** El **MSE se dispara**: el error de ese municipio es enorme y se eleva al cuadrado, así
que ese único caso pasa a aportar una fracción gigantesca del total. El **MAE también sube**,
pero de manera proporcional al error, no a su cuadrado: sube muchísimo menos.
Números del notebook, con un solo caso extremo sobre 36: el MSE creció **4,0×** y el MAE
**1,4×**, y ese año pasó a explicar el **75 %** de todo el MSE. Ojo: esos números son con
una recta **fija** (la que se puso a ojo en la sección 1), sin reajustarla. En la viz
`comparador-de-losses.html`, donde la recta del MSE **sí** se reajusta para ir a buscar al
caso, la cuota de ese año queda en **47 %**: la recta reajustada le achica el error, y aun
así ese año explica casi la mitad.

**b)** Se mueve más **la recta que minimiza el MSE**, y bastante más. Al MSE le «conviene»
girar la recta para acercarse a ese caso, porque bajar un error grande le baja mucho la
cuenta; al MAE le da casi lo mismo: para el MAE cada caso empuja con la misma fuerza, esté
cerca o lejos. (Es la diferencia entre la recta de las medias y la de las medianas.) En la
viz, plantando un caso extremo, la azul se mueve 0,092 puntos por década y la naranja 0,011.

**c)** Se busca algo del estilo de: *«mientras estoy limpiando datos y todavía no sé si los
casos raros son reales o son errores de carga, me conviene el MAE, porque un error de carga
no me va a dar vuelta el modelo entero».*

**Cómo puntuar.** El **a)** y el **b)** son de conocimiento y se puntúan como correcto o
incorrecto. El **c)** es de criterio: aceptá cualquier respuesta que conecte «no sé si es un
error» con «prefiero una loss que no persiga al caso raro». **Rechazá** las respuestas que
digan «hay que sacar el outlier» sin más: sacarlo también es una decisión, y ahí no la
justificaron; una respuesta que diga «lo saco *y* lo reporto *y* corro las dos versiones»
es mejor que la esperada.

---

## 4. El learning rate por diez

Se piden **dos resultados posibles**, y esto es lo importante: la respuesta «va a ir más
rápido» es incompleta, no incorrecta.

1. **Anda mejor.** Si `0.01` era conservador, con `0.1` la loss baja más rápido y llega al
   mismo lugar en menos iteraciones. La curva cae más empinada y se aplana antes.
2. **Se rompe.** Si `0.1` se pasa del límite del valle, cada paso salta al otro lado, más
   arriba que antes. La loss **sube**, a veces oscilando, y termina en `inf` o `nan`.

Hay un tercer resultado, intermedio, que vale como bonus: **oscila pero converge**. Cada
paso salta al otro lado del valle, pero cada vez un poco más abajo. La curva baja con
serrucho y termina aplanándose.

**Cómo distinguirlos mirando sólo la curva:** si baja y se aplana, anduvo; **si la
tendencia sube** (o la curva sube y explota), el learning rate es demasiado grande. Regla
práctica: si la tendencia sube, dividí por diez.
Hoy, que cada paso usa todos los datos, cualquier subida es una señal. Pero desde la clase 4
se entrena con **mini-batches** y la curva siempre tiembla un poco por el ruido de la
muestra (lo vieron en el bonus del notebook). **Un temblor no es una subida**: hay que mirar
la tendencia. Si alguien escribe «si sube aunque sea un poquito, está mal», vale, pero
agregale ese matiz.

*Respuesta parcial frecuente:* «va a ir más rápido». Vale la mitad: hay que preguntar «¿y si
no?». La otra parcial frecuente es «se va a romper», sin la posibilidad de que ande, y también
vale la mitad: **el aula tiende a quedarse con el fracaso espectacular** porque es lo más
visual de la clase.

---

## 5. Las tres curvas

- learning rate **bien elegido** → curva **B**. *Qué hacer:* nada. Es lo que querés ver.
- learning rate **demasiado chico** → curva **A**. *Qué hacer:* subirlo, por diez.
- learning rate **demasiado grande** → curva **C**. *Qué hacer:* bajarlo, por diez.

**El error clásico acá es confundir A con B**: alguien ve que A «está planita» y lo lee como
«convergió». La diferencia no es la forma, es **la altura**: B se aplana *abajo*, pegada al
piso; A se aplana *arriba*, lejísimos del piso. Si aparece esta confusión, es una buena señal
de que en el próximo curso conviene dibujar siempre la línea del mínimo alcanzable como
referencia (en la clase la dibujamos verde punteada, justamente por esto).

*Se descuenta si no escribieron qué harían con el learning rate:* la pregunta pide el
diagnóstico **y** la acción, porque en la clase 4 van a necesitar la acción.

---

## 6. La flecha en el mapa

**a)** Es el **gradiente**: la dirección en la que la loss **sube** más rápido, medida en ese
punto.

**b)** **Hacia abajo a la derecha**, o sea exactamente al revés de la flecha. Porque el paso
del descenso es `parámetros − lr × gradiente`, y ese signo menos es lo que da vuelta la
dirección.

**c)** **No necesariamente.** La flecha señala la subida más empinada *ahí nomás*: es local
y es ciega. En un valle redondo como el de la clase, ir en contra del gradiente apunta
bastante bien al fondo; en un valle alargado y torcido (el de la última figura del notebook,
con el año sin centrar) apunta **a la pared de enfrente**, y el descenso zigzaguea.

| Si contestó | Qué revela | Qué decirle |
|---|---|---|
| «P se mueve hacia arriba a la izquierda» | **Se perdió el signo menos.** Es la confusión más frecuente de toda la clase y no es conceptual: es de lectura. | Hacelo con un número en el pizarrón: «la pendiente da +3, entonces resto». Una vez alcanza. |
| «Sí, la flecha apunta al mínimo» | Está sobreestimando lo que el gradiente sabe. Es la puerta de entrada a confiar de más en el método. | Mostrale la zanja diagonal del notebook. La imagen convence más rápido que el argumento. |

---

## 7. ¿Por qué no probar todas las combinaciones? — **b)**

**Correcta:** la cantidad de combinaciones crece exponencialmente con la cantidad de
parámetros. Con 100 valores por perilla y mil millones de pruebas por segundo: 2 perillas
son 10⁴ pruebas (instantáneo); **8 perillas (una regresión con siete variables) son 10¹⁶,
que son 115 días de computadora**; la red de 8 rampas de la clase 2 tiene 25 perillas (3 por
rampa, más la altura final), o sea 10⁵⁰ pruebas y unas 10²³ edades del universo; y el
mini-GPT de la clase 8 tiene 1,5 millones de perillas.

| Si eligió | Qué confusión revela | Qué decirle |
|---|---|---|
| **a)** sería menos preciso | Tiene algo de razón, pero no es el motivo. La grilla es tan precisa como fina la hagas: en el notebook, la de 120×120 da a = 0,0387 contra el 0,0424 exacto del descenso, porque sus puntos van de a 0,0076. Afinarla arregla la precisión y empeora la factura. | «La precisión se compra con una grilla más fina. Lo que no se puede comprar es el tiempo: el problema es la factura, no la calidad.» |
| **c)** no se sabe qué valores toman | Confunde el problema del rango con el de la escala. Es una objeción razonable pero no es la razón. | «Podrías acotar el rango a ojo y probar igual. Ese no es el cuello de botella.» |
| **d)** daría un mínimo local | **Al revés**, y esta confusión importa: la fuerza bruta es justamente el único método que **sí** encontraría el mínimo global. El que se queda en mínimos locales es el descenso. | «Se te dieron vuelta los dos. Probar todo encuentra el global; bajar tanteando es lo que se puede quedar en un pozo.» |

---

## 8. ¿Qué es el learning rate? — **b)**

**Correcta:** cuánto se mueven los parámetros en cada paso, en proporción a la pendiente.
El learning rate **no** es el largo del paso: es el número que multiplica a la pendiente
(paso = lr × pendiente). Por eso, con el mismo lr, los pasos se achican solos cerca del
fondo. Si alguien contesta b) pero en la justificación dice «el largo fijo de cada paso»,
vale, pero corregile la definición: es lo que hace que «la pelota frena sola» tenga
sentido.

| Si eligió | Qué confusión revela | Qué decirle |
|---|---|---|
| **a)** velocidad de la computadora | Leyó «rate» como velocidad de máquina. Es una confusión de traducción, no conceptual. | «Es la velocidad *del aprendizaje*, no la del procesador: cuánto te movés por cada unidad de pendiente.» |
| **c)** cuántos datos mira | Confundió learning rate con **batch size**. Es una confusión razonable: los dos son perillas que uno elige y los dos afectan el ruido de la curva. | Vale la pena separar los dos explícitamente antes de la clase 4, donde aparecen juntos: «uno dice *cuánto me muevo*, el otro *con cuánta información decido para dónde*». |
| **d)** porcentaje de datos de entrenamiento | Se lo llevó a train/test. Es la clase 4. | Anotalo: significa que están anticipando el tema siguiente, lo cual no está mal. |

---

## 9. La niebla — abierta

**Qué tiene que aparecer** (no hace falta que aparezca todo, pero sí lo primero):

1. Que **no hace falta ver el paisaje entero** para decidir el próximo paso.
2. Que localmente **sí** podés medir si el suelo sube o baja: te movés un poquito y comparás.
3. Que repitiendo esa decisión local muchas veces se llega abajo.
4. **Bonus:** que eso no garantiza llegar al punto más bajo del mundo, sino a uno bajo cerca.

**Respuestas que valen aunque no usen el vocabulario:** «es como bajar una escalera a oscuras
tanteando con el pie», «como buscar la salida de un laberinto pegado a la pared derecha»,
«es prueba y error pero ordenada». Todas capturan la idea.

**Respuestas que NO valen:** cualquiera que diga «el gradiente sabe dónde está el mínimo».
Eso es exactamente lo que la pregunta quiere descartar. Si aparece, es la señal más clara de
que hay que repetir la slide 29 (la honestidad) al empezar la clase 4.

---

## 10. Descenso por gradiente contra backpropagation

**Corrección esperada, en dos oraciones:**
*«No son alternativas: son dos piezas del mismo mecanismo. El **descenso por gradiente**
decide hacia dónde moverse y cuánto; **backpropagation** es la manera eficiente de calcular
el gradiente que el descenso necesita, todas las derivadas de una sola pasada.»*

**Analogía que suele cerrar la idea:** backprop es el contador que te dice cuánto gastaste en
cada rubro; el descenso es vos decidiendo qué recortar y cuánto. Sin el contador no podés
decidir; pero el contador no decide nada.

*Error frecuente:* decir que backprop «es el algoritmo que entrena la red». Es media verdad y
conviene precisarla, porque en la clase 4 van a ver `loss.backward()` y `opt.step()` en dos
líneas seguidas y tienen que saber cuál hace qué: **`backward` anota, `step` mueve**.

---

## 11. Protestas por mes — aplicación sustantiva

**No hay una respuesta correcta.** Se puntúa la coherencia entre el objetivo declarado y la
loss elegida, y que estén **las dos** justificaciones.

**Justificación válida para MSE** (el caso extremo importa):
> «Mi pregunta es qué explica los estallidos. Si el modelo aplana los tres meses excepcionales,
> me quedo con un modelo que describe la rutina y me pierde justamente el fenómeno que quiero
> estudiar. Quiero que esos tres meses pesen.»

Aceptala, pero con una salvedad que conviene devolver por escrito: que los tres meses pesen
no quiere decir que el modelo los *explique*. Una recta por MSE sólo inclina la tendencia de
los otros ciento diecisiete meses hacia ellos. Por eso la respuesta de nota máxima (abajo)
es la que propone modelarlos aparte.

**Justificación válida para MAE** (el caso extremo distorsiona):
> «Mi pregunta es cuál es el nivel habitual de conflictividad y cómo evoluciona. Los tres
> estallidos son eventos de otra naturaleza; si los dejo pesar, la tendencia que reporte va a
> estar tironeada por tres puntos de doce meses por diez años y no va a describir a ninguno de
> los otros ciento diecisiete.»

**Qué NO alcanza:** «uso MSE porque es el estándar», «uso MAE porque hay outliers». Las dos
son afirmaciones sobre la técnica y no sobre la investigación. **La consigna pide el objetivo
de investigación explícito**, y es la mitad del puntaje.

**Respuesta que merece nota máxima aunque no se haya pedido:** la que propone modelar los
estallidos aparte, o agregar una variable que los marque, y dice que la elección de loss no
resuelve un problema de especificación. Eso es exactamente el criterio que el curso quiere
producir.

---

## 12. La beca — criterio y ética aplicada

**Lo que se busca**, en orden de importancia:

1. **Que identifiquen que la pregunta no es técnica.** Los dos errores tienen costos de
   naturaleza distinta y a quienes los pagan no son las mismas personas: el falso negativo lo
   paga quien deserta; el falso positivo lo paga el presupuesto (y, indirectamente, quien se
   quedó sin la beca que se llevó otro).
2. **Que noten que igual hay que decidir**, y que no decidir *también es decidir*: si nadie
   discute nada, el default de la biblioteca decide por todos.
3. **Que ubiquen dónde queda escrita la decisión**: en la función de pérdida (los pesos por
   clase) y en el **umbral** de corte. Son dos líneas de código.
4. **Que digan que no la debería tomar quien programa, en soledad**, sino el equipo con el
   área de política educativa, y que debería quedar documentada.

**Para c)**, la pregunta esperada es alguna versión de: **«¿optimizado para minimizar qué,
exactamente?»**, y si la respuesta es «exactitud», la repregunta: *«con qué prevalencia?»*.
Si sólo el 5 % de los alumnos deserta, un modelo que dice «nadie deserta» tiene 95 % de
exactitud y sirve para cero. Esa observación merece nota máxima: es la clase 9 anticipada.
Un matiz que vale como bonus: la exactitud casi nunca es lo que se *optimiza* (no se puede
bajar con gradiente: es plana casi en todas partes y salta de golpe). Se entrena con otra
loss, como la entropía cruzada, y la exactitud se *reporta*. «Optimizado para maximizar la
exactitud» suele querer decir «elegido entre varios modelos por su exactitud», y la
pregunta sigue valiendo igual.

**Cómo NO puntuar esta pregunta.** No hay una respuesta correcta entre «falso positivo» y
«falso negativo», y **no se le baja la nota a nadie por la posición que tome**. Se le baja a
quien no justifique, a quien crea que hay una respuesta técnica, y a quien no ubique dónde
queda escrita la decisión.

**Nota para el docente.** Esta pregunta es la siembra de las clases 9 y 10. Si alguien da una
respuesta especialmente buena, guardala (con permiso) y proyectala en la clase 10: cierra
el arco del curso.

---

## Resumen para el docente: qué mirar en el conjunto

| Señal | Qué significa | Qué hacer antes de la clase 4 |
|---|---|---|
| Muchos eligen **2a** o **2b** | El salto entre espacio de datos y espacio de parámetros no se dio. | Cinco minutos de `valle-de-loss.html` al empezar la clase 4. Es lo más urgente. |
| Muchos se pierden el signo menos (**6b**) | Es de lectura, no conceptual. | Un número en el pizarrón, treinta segundos. |
| Muchos eligen **7d** | Se dieron vuelta la fuerza bruta y el descenso. | Una frase: «probar todo encuentra el global; tantear se puede quedar en un pozo». |
| Muchos confunden **A** con **B** en la 5 | No están mirando la **altura** de la curva, sólo su forma. | En la clase 4, dibujá siempre la línea de referencia del mínimo alcanzable. |
| Las respuestas 11 y 12 son técnicas y no sustantivas | El mensaje central de la clase —que la loss es una decisión— no llegó. | **Es lo más grave que puede pasar.** Vale volver dos slides al empezar la clase 4. |

---

## Anexo: respuestas modelo de los `TODO` del notebook

Los números son los de una corrida del notebook: es determinista en la misma máquina y con
las mismas versiones de las librerías; con otras versiones algún decimal puede cambiar.

| TODO | Qué se completa | Respuesta modelo |
|---|---|---|
| **1** | Dos comentarios. | 1. «Creció más el MSE (4,0× contra 1,4×), porque eleva cada error al cuadrado: un error grande, al cuadrado, se come la loss entera (ese año solo aporta el 75 % del MSE).» 2. «Si es un error de carga, MAE (o corregir el dato). Si es el año que motiva la investigación, MSE deja que pese; pero una recta no lo explica, así que conviene estudiarlo aparte.» |
| **2** | `zoom_a`, `zoom_b` y `forma_del_valle`. | `np.linspace(mejor_a - 0.06, mejor_a + 0.06, 120)` y lo mismo con `mejor_b`; `forma_del_valle = "redondo"`. Sale redondo porque el año está centrado (eso despega las dos perillas) y en décadas (eso las pone en la misma escala): casi estandarizado. |
| **3** | Un comentario y `signo_de_a`. | `signo_de_a = "alterna"`. «Con lr = 1,5 cada paso salta al otro lado del valle y cae más arriba que antes: `a` rebota con el signo cambiado y cada vez unas 2,2 veces más lejos (+0,81, −1,67, +3,88, −8,54, +19,2), y la loss explota.» |
| **4** | `llego` e `iteraciones_estimadas`. | `llego = False`. Por regla de tres, unas 240.000 iteraciones (se acepta cualquier estimación desde 10.000). La cuenta exacta da más, del orden de 1,5 millones para quedar a menos de 2 % del fondo, porque el paso es lr × pendiente y la pendiente se va achicando. |
| **5** | `a0_lejos`, `b0_lejos`, `pasos_lejos`. | `-5.0`, `50.0`, `400`. Llega a a = 0,0424, b = 0,1549, el mismo fondo que desde (−0,3; 0,4) y que el descenso original. Pasa porque este paisaje tiene un solo pozo; en «uno con dos pozos» de `valle-de-loss.html`, no. |
