# Cuestionario — Clase 2 · Soluciones comentadas

> **Para quien corrige.** Lo que importa no es cuál marcaron: es **cuál
> distractor eligieron**. Cada uno de los que están abajo está puesto a
> propósito porque corresponde a una confusión real que aparece todos los años.
> Si media clase eligió el mismo distractor, eso es un dato sobre la clase que
> diste, no sobre ellos.

---

## 1. Qué significa componer

**Correcta: B** — meter `x` en `f`, y lo que sale de `f` meterlo en `g`.

| Distractor | Por qué es tentador | Qué confusión revela |
|---|---|---|
| **A** (sumar) | Es la lectura "natural" de dos funciones puestas juntas, y en la notación las dos aparecen en la misma línea. | **La confusión número uno de la clase.** Quien elige A todavía no vio la cadena: cree que las dos máquinas trabajan *en paralelo* sobre la misma entrada, no *en serie*. Se desarma volviendo a la slide 8 y siguiendo el 3 con el dedo. |
| **C** (multiplicar) | Misma raíz que A: dos cosas juntas, alguna operación aritmética entre ellas. | Igual que A. Si alguien eligió C, casi seguro también dudó entre A y C: el problema no es qué operación, es que **no hay operación aritmética**, hay un encadenamiento. |
| **D** (la más chica) | Suena a "optimizar", que es una palabra que ya escucharon. | Mezcla componer con elegir. Vale aclarar que elegir el mejor de varios modelos es otra cosa, y que la vamos a ver en la clase 4. |

**Cómo verificar que entendieron de verdad:** que digan en voz alta el resultado
de `doble(mas_diez(3))` y de `mas_diez(doble(3))`. Si dan lo mismo, no entendieron.

---

## 2. Por qué no alcanza con apilar

**Correcta: B** — encadenar rectas da otra recta; se colapsa a dos números.

| Distractor | Por qué es tentador | Qué confusión revela |
|---|---|---|
| **A** (limitación de las computadoras) | Hay una intuición difusa de que "las máquinas tienen un límite". | Cree que el problema es **técnico** cuando es **matemático**. Es un error importante de desarmar: acá no hay nada que un procesador más rápido pueda arreglar. |
| **C** (faltan datos) | Es una respuesta que suele ser correcta en otros contextos, así que se elige por costumbre. | Confunde **expresividad** (qué formas puede dibujar el modelo) con **estimación** (si tenés datos para encontrarlas). Es una distinción central del curso y conviene nombrarla: acá el problema es de vocabulario, no de evidencia. |
| **D** (se cancelan y da cero) | Suena plausible si uno imagina que "se anulan". | Confusión con el caso particular en que los pesos son opuestos. Basta mostrar la viz: da una recta con pendiente cualquiera, casi nunca cero. |

---

## 3. Seguir el número

**(a)** `f(g(1)) = f(4) = 8`
**(b)** `g(f(1)) = g(2) = 5`

**(c)** Respuesta esperada: *porque en el primer caso el `+3` se aplica antes de
multiplicar (y entonces el 3 también se duplica), y en el segundo se aplica
después (y el 3 queda tal cual)*. Cualquier formulación que muestre **que el
resultado de la primera es lo que entra a la segunda** está bien.

**Respuestas que hay que corregir:**
- *"Porque la multiplicación va antes que la suma"* → está mezclando el orden de
  las operaciones dentro de una expresión con el orden de las funciones en una
  cadena. No es lo mismo.
- *"Porque una da par y la otra impar"* → describe el resultado, no el mecanismo.
  Pedile que lo cuente siguiendo el número paso por paso.

---

## 4. Cuántas rampas

**(a) 5 rampas, 9 quiebres.** El modelo se va a quedar corto: va a capturar la
forma gruesa —los quiebres más grandes— y a alisar los demás. En el gráfico se
ve como una curva que "sigue la idea" pero se corta las esquinas, con los
segmentos rojos del error concentrados justo en los quiebres que no llegó a
representar. **Es exactamente lo que pasó en el notebook con 4 rampas.**
El nombre técnico —*underfitting*, subajuste— todavía no se dio; si alguien lo
usa, bárbaro, y se aclara en la clase 4.

**(b) 500 rampas, 12 datos.** Va a pasar por **todos** los puntos, exactamente.
El desajuste va a dar prácticamente cero. **Y no, eso no es bueno**: con 500
perillas y 12 casos, el modelo tiene margen de sobra para copiar cada punto,
incluidos los que son error de medición. Entre punto y punto puede hacer
cualquier cosa. Es la imagen del botón «32 rampas» de la viz, llevada al extremo.

*Respuesta que revela la confusión peligrosa:* «va a andar buenísimo porque
ajusta perfecto». Quien conteste eso está confundiendo **aproximar lo que ya
viste** con **predecir lo que no viste**, que es la confusión más cara del curso.
Anotalo: esa persona necesita que la clase 4 le pegue fuerte.

---

## 5. Contar codos

| Curva | Quiebres | Rampas |
|---|---|---|
| **A** | 2 (donde arranca a subir, donde se aplana) | **2** |
| **B** | 3 (sube, dobla en el pico, se aplana) | **3** |
| **C** | 5 (sube, baja, sube, baja, se aplana) | **5** |
| **D** | 3 (sube, dobla en el pico, se aplana) | **3** |

**El punto de la pregunta no es contar, es que B y D tienen la misma cantidad.**
Dos figuras que se ven distintas necesitan la misma cantidad de piezas: lo que
cambia es *dónde* están los codos y *cuánto* valen las alturas, no cuántas
rampas hay. Si alguien contó 4 en D porque "tiene una parte plana más larga",
ahí está la confusión: la longitud del tramo no cuesta perillas.

*Error típico:* contar el arranque y el final del gráfico como quiebres. No lo
son: la curva ya venía plana.

---

## 6. Contar perillas

**Correcta: 13.**

```
pesos entrada -> ocultas :  2 × 3 = 6
sesgos de las ocultas    :        3
pesos ocultas -> salida  :  3 × 1 = 3
sesgo de la salida       :        1
                           --------
                                 13
```

| Error típico | Cuánto da | Qué confusión revela |
|---|---|---|
| Contar sólo las flechas | 9 | **Se olvidaron los sesgos.** Es el error más frecuente y no es trivial: el sesgo es la perilla que *desplaza*, y sin ella la rampa tendría el codo clavado en cero. Mostrales la viz `red-como-dibujante.html`: los sesgos están dibujados como cabitos que entran a cada bolita. |
| Contar las neuronas | 6 | Confunden "neurona" con "parámetro". Una neurona **tiene** parámetros, no **es** un parámetro. |
| 2 + 3 + 1 = 6 | 6 | Sumaron el tamaño de las capas. Es el error de quien todavía no ve que lo que se aprende está en las **conexiones**, no en las bolitas. |
| 12 | 12 | Contaron los sesgos de las ocultas pero se olvidaron el de la salida. Casi bien: vale medio punto y una sonrisa. |

**Regla general que conviene que se lleven:** para una red `[a, b, c]` los
parámetros son `a·b + b + b·c + c`. Para la del notebook, `[1, 4, 1]`:
`4 + 4 + 4 + 1 = 13`. (Sí, la misma cuenta da 13 en los dos casos. Coincidencia,
y sirve para chequear.)

---

## 7. La función de activación

**Correcta: B** — es el doblez entre capa y capa; sin ella, la red entera
equivale a una sola recta.

| Distractor | Por qué es tentador | Qué confusión revela |
|---|---|---|
| **A** ("prende o apaga la neurona") | Es la explicación que circula en toda la divulgación, y la palabra *activación* la invita. Además es *casi* cierta para ReLU, que efectivamente deja pasar o pone cero. | La metáfora del interruptor biológico. El problema no es que sea falsa, es que hace pensar que la activación es una **decisión** de la neurona, cuando es simplemente una cuenta. Y sobre todo: no explica **para qué está**. Preguntales "¿y qué pasa si la saco?" — si no saben, eligieron A. |
| **C** (convierte en probabilidad) | Confusión con *softmax*, que sí hace eso y que van a ver en la clase 4. | Mezcla la activación **de la capa oculta** (el doblez) con la **de la salida** (que a veces sí convierte a probabilidad). Vale aclararlo: son dos cosas con el mismo nombre y distinta función. |
| **D** (evita el sobreajuste) | "Sobreajuste" es una palabra que ya escucharon y que suena a problema serio. | Al revés: la activación es lo que le da al modelo **más** flexibilidad, no menos. Quien elige D está asociando cualquier componente técnico con "algo que controla el modelo". |

---

## 8. Vocabulario

**1-c** (peso = la perilla que multiplica) · **2-e** (sesgo = la perilla que suma)
· **3-b** (neurona = una rampa) · **4-a** (capa oculta) · **5-d** (activación = el doblez)

*El par que más se confunde es 1-2.* Si intercambiaron peso y sesgo, la frase que
lo arregla es: **el peso multiplica, el sesgo suma**. Y el recordatorio que
importa para el resto del curso: *bias* acá **no** quiere decir sesgo social. Es
un número que corre la figura para arriba o para abajo. Cuando en la clase 10 se
hable de sesgo de verdad, va a ser otra cosa completamente distinta con el mismo
nombre en inglés.

---

## 9. Leer el teorema

**La que NO se sigue: B** — "va a predecir bien los casos que todavía no vio".

Ésta es **la pregunta más importante del cuestionario**. El teorema es una
afirmación de *existencia*: dice que la combinación de pesos existe. No dice:

- que la vayas a **encontrar** (ese es el problema de la clase 3),
- con **cuántos datos** (ese es el problema de la clase 4),
- ni que sirva para casos **nuevos** (ese es el problema de todo el curso).

| Distractor | Por qué es tentador | Qué confusión revela |
|---|---|---|
| **A** | Es lo que el teorema efectivamente dice, así que quien busca "la falsa" y no lee con cuidado puede marcarla. | Lectura apurada, no confusión conceptual. |
| **C** | Suena a exageración ("no hace falta buscar una fórmula especial") y por eso levanta sospecha. | En realidad es correcta y es justamente el valor práctico del resultado. Quien la marca suele estar aplicando bien el escepticismo, sólo que al enunciado equivocado. Vale reconocérselo. |
| **D** | Es una afirmación *negativa* sobre el teorema, y las negaciones confunden. | Igual que C: es verdadera. El teorema efectivamente no dice nada sobre cantidad de datos. |

**El paralelo que conviene dejar escrito** (y que se retoma en la clase 10): una
teoría que puede explicar cualquier resultado no explica nada. Una función que
puede dibujar cualquier curva no dice nada sobre el mundo **hasta que la
restringimos con datos**. Aproximar no es predecir.

---

## 10. Encontrar el bug

**(a) El error:** la línea que crea `total` quedó **adentro** del `for`. En cada
vuelta se pisa el acumulador, así que sólo sobrevive la última rampa.

**(b) Qué dibuja:** la base más **la última rampa sola** — o sea, una línea
horizontal que en el último codo empieza a subir (o a bajar). Las tres primeras
rampas se calculan y se tiran a la basura.

**(c)** Andaría **sin dar error**, y ése es exactamente el problema. Python no
tiene forma de saber que quisiste acumular: `total` existe, tiene el tipo
correcto, la función devuelve un array de la forma correcta. Vas a ver un
gráfico, vas a ver un número de desajuste, y los dos van a estar mal.

> **La lección que hay que subrayar, y no es sobre Python:** los errores que te
> arruinan un paper casi nunca tiran una excepción. Corren, devuelven un número
> plausible, y te dejan escribir un resultado. Por eso en este curso los
> gráficos se **miran** y los resultados se **comparan contra algo conocido**
> (acá: contra el desajuste de las cuatro rampas de la celda anterior). Si el
> número no cambia cuando debería, ahí hay algo.

*Pista para corregir:* si alguien contesta "se rompería porque `total` no está
definida", está pensando en Python 2 o en otro lenguaje. Vale la pena aclarar
que **sí** queda definida, porque el `for` corre al menos una vez.
(Y si `codos` estuviera vacío, ahí **sí** explotaría con un `NameError`: es un
buen dato extra, no un error de la respuesta.)

---

## 11. Criterio aplicado

**(a) y (b) — las dos preguntas.** Se busca, en cualquier orden y con cualquier
formulación:

1. **«¿Cuántos casos usaste para entrenar?»** — 80 municipios, quizá por unos
   años. Aunque fueran 80 × 20 años = 1.600 observaciones, sigue habiendo
   **1.250 parámetros por cada dato**. Con esa relación, el modelo puede pasar
   por todos los puntos sin haber aprendido nada sobre el fenómeno.
2. **«¿Ese 0,99 está calculado sobre datos que el modelo no vio?»** — y si la
   respuesta es "sobre los mismos datos con los que lo entrené", la conversación
   terminó ahí. Es la pregunta que separa dibujar de calcar.

Preguntas adicionales que también valen (y suman):
- «¿Cómo partiste los datos? ¿Al azar o por tiempo?» (si los municipios se
  repiten a lo largo de los años, partir al azar mete el mismo municipio de los
  dos lados: eso es fuga, y es la clase 4).
- «¿Contra qué lo comparaste?» Si un modelo lineal simple da 0,97, los 2 millones
  de parámetros no compraron nada.

**(c) Por qué «ajusta perfecto» es una alarma.** Porque con muchísimas más
perillas que datos, ajustar perfecto es lo que pasa **siempre**, tenga o no
tenga el modelo algo que decir sobre el fenómeno. Un R² de 0,99 en los datos de
entrenamiento no es evidencia de que el modelo capturó el patrón: es evidencia de
que tuvo libertad suficiente para copiar la muestra, ruido incluido. La pregunta
útil no es "¿cuánto ajusta?" sino "¿cuánto ajusta **en datos que no vio**?".

**Respuestas que hay que corregir:**
- *"Está mal porque las redes neuronales no sirven para pocos datos"* → demasiado
  categórico y no es el argumento. El problema no es la herramienta, es la
  relación entre flexibilidad y evidencia, y no reportar validación.
- *"Está bien, 0,99 es un buen resultado"* → todavía no distingue ajustar de
  predecir. Volver al botón «32 rampas».

**(d) La parte que importa.** No hay respuesta correcta, y es la que hay que
leer con más atención. Lo que se busca es que apliquen la misma vara a su propio
trabajo: *"mi índice tiene 8 ítems ponderados a mano y lo construí con 240
encuestas"*, *"mi regresión tenía 14 predictores y 90 casos"*. Una respuesta
excelente reconoce que la relación perillas/datos también aplica a métodos que
no son redes neuronales — porque **es un problema de método, no de tecnología**.

Si nadie de la clase se aplicó la vara a sí mismo, decilo en voz alta la clase
que viene: es la única forma de que el `[EL LUNES]` de esta clase deje de ser una
frase.
