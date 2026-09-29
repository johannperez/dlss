# Notas para quien da la clase 2

**Componer funciones: dibujar lo imposible** · 120 minutos · 35 slides

> Si sólo vas a leer una cosa de este archivo antes de entrar al aula, leé el
> **arco narrativo** de acá abajo y el **plan de tiempos**. Todo lo demás son
> muletas para cuando pase algo.

---

## 1. El arco narrativo, en diez líneas

1. Se proyecta una curva real (menciones a *inflación*, 1984-2019) y se les pide
   que le ajusten una recta. El aula tira valores; vos los ponés.
2. Fracasan. Y no por torpes: **la mejor recta posible explica el 0,5 % de la
   variación**. Casi lo mismo que dibujar una raya en el promedio.
3. «¿Y si le agrego perillas?» — se prueba en vivo y se descubre que cinco
   perillas se colapsan a dos. *Más parámetros no es más flexibilidad.* Ese
   golpe vale la clase entera aunque no llegues a nada más.
4. La idea de albañil: **encadenar**. Si una máquina no alcanza, poné dos. Se
   sigue un número por la cadena y se descubre que el orden importa.
5. Segundo fracaso, más profundo: encadenar rectas **da una recta**, siempre, y
   se demuestra apretando «randomizar» quince veces. Ahora el aula quiere la
   solución.
6. El doblez: `max(0, x)`. Ridículamente simple, y con eso alcanza.
7. **El momento de la clase**: sumar rampas. Una, dos, cuatro, ocho. La curva
   imposible aparece. Silencio de cinco segundos.
8. Recién ahí se le pone el nombre: esto es una red neuronal, y el diagrama de
   circulitos que vieron mil veces es un plano de cableado, no un ícono místico.
9. El desinflado saludable: no hay cerebro, no hay pensamiento, hay rampas
   sumadas. Y la advertencia del teorema: *existe* la combinación; no dice que
   la vayas a encontrar ni que generalice.
10. La puerta que queda abierta: los pesos los pusimos a mano y fue un suplicio.
    Con ocho ya cuesta; con ocho millones es imposible. Clase 3.

---

## 2. Plan de tiempos real (con el minuto de inicio)

| Min | Slides | Bloque | Qué pasa |
|---|---|---|---|
| **0** | 1-2 | Apertura + callback | Una frase de apertura. Recap de la clase 1 preguntando, no contando. |
| **3** | 3-4 | **El gancho** | La curva proyectada. El aula grita valores. `viz/la-recta-imposible.html`. |
| **9** | 5-6 | Más perillas | Los botones 3 y 5 perillas. El límite es de vocabulario, no de precisión. |
| **14** | 7-10 | Componer | Dos cajas, seguir el número, la notación, la cadena de mediciones. |
| **21** | 11 | Viz lego | `viz/lego-de-funciones.html` con el botón del intercambio. |
| **25** | 12-13 | **Apuesta + baldazo** | Se vota. Después `viz/sin-no-linealidad.html` y quince randomizaciones. |
| **31** | 14-17 | El doblez | La goma, la hoja, ReLU, la rampa con sus dos números (tres perillas en la red de verdad). |
| **38** | 18 | **Manos 1** | Notebook hasta el TODO 3. Recorré el aula. |
| **55** | 19 | **PAUSA** | **No se toca.** |
| **65** | 20-21 | Volvimos + la pregunta | Se muestra la solución de alguien. Diez segundos de silencio. |
| **70** | 22-24 | **El momento fuerte** | `viz/rampas.html`: 1 → 2 → 4 → 8. Silencio. El teorema. |
| **82** | 25-28 | El nombre y el vocabulario | El diagrama, `viz/red-como-dibujante.html`, las siete palabras, ancho vs profundo. |
| **90** | 29 | **Manos 2** | De a dos, 17 minutos. TODO 4 y la versión matricial. |
| **107** | 30-32 | Lo que no es + la siembra | El desinflado. El botón «32». `[EN TU INVESTIGACIÓN]`. |
| **115** | 33-35 | Cierre | Las tres cosas, el glosario, el puente a la clase 3. |

Suma exacta: **120 minutos**. La pausa está a los 55 y dura 10.

**Los números de slide de esta tabla son los que muestra reveal abajo a la
derecha** (`n / 35`), o sea contando la pausa como la 19. Todas las referencias
a slides de este archivo y de las notas del docente usan esa misma numeración.

Los dos bloques prácticos duran **17 minutos** cada uno, no 20: son los que
quedan después de descontar lo que efectivamente ocupa la exposición, y es lo
que dice la slide. Si querés los 20, lo que se recorta está en la sección 6.

> **Diferencia con `PROGRAMA.md`.** El plan del curso pone «Manos 2» en 85-105 y
> el cierre en 105-120. Medido slide por slide, el tramo del nombre y el
> vocabulario (25-28) no entra en el reloj del programa: son cuatro slides y una viz. Así que
> acá el práctico 2 va **90-107** y el cierre **107-120**. Suma lo mismo, la pausa
> no se movió, y ningún bloque quedó por debajo de lo que necesita. Si preferís
> respetar el reloj del programa al pie de la letra, recortá la slide 28 (ancho vs
> profundo) y acortá la 26 (`red-como-dibujante`) a dos minutos: con eso arrancás
> el práctico a los 87.

---

## 3. Qué preguntar al aula, y cuándo

| Momento | La pregunta | Para qué |
|---|---|---|
| Slide 2 | «¿Cuál es la diferencia entre variable y parámetro?» | Reactiva la clase 1. Esperá la respuesta; no la des vos. |
| Slide 3 | «¿Qué forma tiene esto?» | Las respuestas *son* los codos que vas a poner después. Anotalas. |
| Slide 3 | «Ajustale una recta. Denme valores.» | Que el fracaso sea de ellos, no una afirmación tuya. |
| Slide 5 | «¿Por qué no cambia nada al agregar perillas?» | Si alguien contesta bien, descubrió solo la no linealidad. |
| Slide 8 | «Si invierto el orden, ¿da lo mismo?» | Desarma "componer es sumar" antes de que se instale. |
| **Slide 12** | **«Si encadeno dos rectas, ¿qué sale?» — se vota** | Sin esta apuesta, la viz siguiente es decoración. |
| Slide 16 | (la que van a hacer ellos) «¿Por qué justo esa función?» | Preparate la respuesta honesta. Está abajo. |
| Slide 21 | «¿Cuántas rampas creen que hacen falta?» | Anotá los números. Después se comparan. |
| Slide 24 | «¿Qué le criticarías a una teoría que explica cualquier resultado?» | Puente a Popper. Contestan bien solos. |
| Slide 29 | «¿Por qué pusiste el codo ahí?» (recorriendo) | Buscás: «porque ahí cambia de dirección» o «ahí el palito era más largo». |

---

## 4. Las respuestas típicas y cómo usarlas

**«Sube»** (slide 3). Contestá: «¿sube todo el tiempo?». Casi siempre alguien
corrige: «sube, baja y vuelve a subir». Esa frase es literalmente la que la
recta no puede decir, y la vas a citar en la slide 6.

**«Una curva»** (la apuesta de la slide 12). Es la mayoría. Perfecto: contá las
manos en voz alta y **anotá el número en el pizarrón**. Cuando salga la recta,
señalá el número. La predicción fallida es el aprendizaje; el número anotado es
lo que la hace visible.

**«Porque son todas lo mismo»** (slide 5). Si alguien dice esto, pará todo y
felicitalo delante del aula: acaba de deducir el argumento de la slide 14 veinte
minutos antes. Después pedile que lo explique con sus palabras.

**«¿Y si en vez de una recta usamos una parábola?»** Muy buena, y aparece
seguido. Respuesta: «podés, y a veces alcanza. Pero entonces tenés que adivinar
*qué* fórmula rara sirve para cada problema, y eso es exactamente el trabajo que
queremos que haga la máquina. La gracia de las rampas es que **no hay que
adivinar la forma**: se ponen muchas y ellas se acomodan».

**«Tres rampas» / «cuatro rampas»** (la meseta del TODO 3). Las dos están bien y
la discusión es buena: con tres sube, se aplana y baja; con cuatro además
termina plana. Que lo dibujen en el pizarrón.

---

## 5. Las confusiones de principiante que van a aparecer

**«Componer es sumar»** — `g(f(x))` leído como `g(x) + f(x)`.
*Cómo se desarma:* la slide 8 (seguir el número) y el botón de intercambio de la
viz del lego. Si fuera una suma, el orden no importaría, y el orden importa: 16
contra 26.

**«Más parámetros = más flexible»** — es una creencia fuerte y hay que atacarla
**dos veces**: en la slide 5 con el álgebra de juguete, y en la slide 13 con el
contador de randomizaciones. Si sólo la atacás una vez, vuelve.

**«ReLU tiene que tener algo profundo adentro»** — buscan complejidad donde no
hay. La respuesta honesta (abajo, sección 8) genera más confianza que cualquier
explicación elaborada.

**El acumulador del `for`** — `total = total + rampa(...)` es donde se pierden en
el notebook. *Cómo se desarma:* ejecutalo a mano en el pizarrón con tres
iteraciones y valores concretos, escribiendo el estado de `total` en cada paso.
Tres minutos, y no vuelve a pasar en toda la cursada.

**Codo vs altura** — mezclan las dos perillas de la rampa. Frase corta: **el codo
es *dónde*, la altura es *cuánto sube por cada unidad* después del codo.** (En
el notebook se llama `altura`, pero es una pendiente: con altura 2 y el codo en
5, en x = 10 la rampa ya vale 10. La slide 17 la llama bien: «qué tan empinada».)

**«Cada rampa se ocupa de un tramo»** — la confusión que el material mismo puede
sembrar si uno se descuida. Una rampa vale cero antes de su codo, pero después
**sigue subiendo o bajando hasta el final**. Cada rampa dobla la curva en su codo
y todo lo de la derecha hereda el doblez; lo de la izquierda ni se entera. Por
eso, al agregar una rampa, hay que reacomodar las otras (el botón «acomodar» de
`rampas.html`, o la pista 3 del TODO 4). Si alguien quiere una pieza que sí sea
local, se arma con varias rampas: sube, frena, baja y frena (el «sombrerito» de
Nielsen).

**«Con suficientes rampas puedo predecir cualquier cosa»** — la más peligrosa.
Aproximar lo que ya viste no es predecir lo que no viste. Se dice en la slide 24
y se cobra en la clase 4. Si aparece antes, no la resuelvas del todo: decí
«guardá esa pregunta, es la clase 4 entera» y anotala en el pizarrón.

**«Bias = sesgo social»** — falso amigo. Clavarlo en la slide 27 ahorra
malentendidos durante ocho clases.

---

## 6. Si vas atrasado (y si vas adelantado)

### Qué se recorta, en este orden

1. **Slide 28 (ancho vs profundo).** Se reemplaza por una frase: «profundo quiere
   decir varias capas, cada una trabajando sobre lo que armó la anterior; lo
   vemos en la clase 5».
2. **Slide 9 (la notación `g(f(x))`).** Se puede dejar para el notebook, que la
   tiene igual.
3. **Slide 14 (la cuenta algebraica del "por qué").** Si el aula tiene alergia al
   álgebra, quedate sólo con la goma que se estira: la viz ya lo demostró por
   repetición.
4. **Slide 10 (la cadena de mediciones).** Duele recortarla porque es la que
   conecta con su oficio, pero se puede decir en una frase mientras mostrás la
   viz del lego.
5. **Bloque práctico 2**, achicándolo de 17 a 12 minutos y dejando la sección 5
   del notebook (matrices) como tarea para antes de la clase 3. Son unos 15
   minutos; con el cuestionario (25-30) no pasa de una hora, que es el tope de
   tarea entre clases.

### Qué NUNCA se recorta

- **La pausa.** Diez minutos, en el minuto 55. Si la comés, la segunda mitad se
  atropella y el momento fuerte de la clase se arruina.
- **La apuesta de la slide 12.** Sin la votación, `sin-no-linealidad.html` es un
  dibujito lindo.
- **El silencio de cinco segundos en las 8 rampas.** Es tentador seguir hablando.
  No lo hagas.
- **La advertencia del teorema (slide 24).** Sin ella, la clase enseña
  entusiasmo mágico, que es exactamente lo contrario de lo que este curso quiere.
- **El botón «32» de la slide 31.** Es la siembra del sobreajuste, y el equipo de
  la clase 4 cuenta con que esté puesta.

### Si vas adelantado

- En `viz/rampas.html`, apretá **«8»** y pediles que **apuesten** qué rampa va a
  doler más si la sacás. Después sacala con la **×** de su tarjeta, que **no
  reacomoda** las demás. Medido: sacar la de 1992 lleva el desajuste a 0.29 y la
  de 1994 a 0.28 —peor que no hacer nada—, mientras que sacar la de 2017 lo deja
  en 0.0011. ¿Por qué? Porque una rampa no es local: la de 1992 arrastra toda la
  curva desde 1992 hasta 2019, y la de 2017 sólo los dos últimos años. Después
  apretá **«acomodar»**: ahora sacar la de 1990 casi no duele (0.00019, contra
  0.00016 con las ocho) y las que más duelen son la de 1999 (0.00042) y la de
  2017 (0.00038). Buena discusión sobre qué quiere decir que una pieza
  «importa». (Números en §10.)
- En `viz/lego-de-funciones.html`, poné `sigmoide` en la caja 1 y mostrá cómo
  aplasta todo entre 0 y 1: cualquier cosa que venga después trabaja sobre un
  rango minúsculo. Es una pista de por qué las redes profundas con sigmoides
  eran difíciles de entrenar. En este curso no se desarrolla; si alguien quiere
  seguir, está en el capítulo 5 de Nielsen (el 1 de `referencias.md`).
- En `viz/red-como-dibujante.html`, apretá «randomizar toda la red» cinco veces y
  preguntá: «¿cuánto tardarías en encontrar la buena a mano?». Es el mejor pie
  posible para la clase 3.
- Pediles que abran el notebook y prueben `codos` con dos valores **iguales**.
  ¿Qué pasa? (Se suman las dos rampas en el mismo lugar: es como tener una sola
  con el doble de altura. Dos perillas que hacen lo mismo. Volvemos a la lección
  de la slide 5, ahora del otro lado.)

---

## 7. Los chistes y analogías que funcionan

- **La burocracia como composición.** Un trámite pasa por ventanilla, mesa de
  entradas, dictamen, resolución. Cada oficina transforma el expediente y se lo
  pasa a la siguiente. Y el remate: **la no linealidad es la ventanilla que dice
  «si no cumple el requisito, cero»**. Sin alguna ventanilla que corte, todo el
  circuito sería una sola operación trivial. Este chiste funciona *siempre*.
- **El ecualizador con 25 perillas.** Callback a la clase 1: la red de ocho
  rampas tiene 25 perillas (3 por rampa, más la base), y nadie ecualiza 25
  bandas a mano: por eso existen los presets. El descenso por gradiente es la
  máquina que fabrica presets. Guardalo para la slide 31.
- **La goma que se estira dos veces.** Para el "por qué apilar lineales no sirve".
  Si tenés una banda elástica en el bolsillo, mejor.
- **La hoja de papel.** Doblala en vivo. El gesto físico se recuerda más que la
  slide.
- **«Marketing histórico de 1943».** Para desactivar la analogía del cerebro sin
  ser antipático con quien la trajo.
- **Popper.** «Una teoría que puede explicar cualquier resultado no explica nada.»
  Es la analogía más potente de la clase con esta audiencia y hay que decirla
  con todas las letras en la slide 24.

---

## 8. «Si te preguntan X» — las cinco preguntas difíciles

**1. «¿Por qué justo `max(0, x)`? ¿Qué tiene de especial?»**
Nada. Y hay que decirlo así. *«Porque es la más barata de calcular y porque anda.
Se probaron otras más elegantes —la sigmoide, la tangente hiperbólica, y una
docena de variantes con nombres raros— y andan parecido o un poco peor. Gran
parte del deep learning es así: se probó, funcionó, se quedó. Está bien
saberlo.»* La honestidad acá compra confianza para toda la cursada. Si querés
agregar una razón técnica: con la sigmoide, las redes profundas se entrenaban
muy mal porque la señal para ajustar las perillas se achicaba capa a capa; con
ReLU ese problema es mucho menor. **En este curso no se desarrolla** (no lo
prometas para otra clase); quien quiera seguir lo tiene en el capítulo 5 de
Nielsen.

**2. «¿Entonces las neuronas artificiales imitan a las neuronas del cerebro?»**
*«El nombre es de 1943, de McCulloch y Pitts, y era una analogía razonable para
lo que se sabía entonces. Hoy confunde. Una neurona artificial es una rampa: dos
multiplicaciones y una comparación con cero. Una neurona real es una célula viva
de una complejidad brutal, con miles de sinapsis, química propia y timing. La
analogía te va a hacer **sobreestimar** el modelo, y sobreestimarlo es
exactamente el error que este curso quiere evitar.»* No lo digas con desprecio:
el entusiasmo está bien, la magia no.

**3. «Si con suficientes rampas puedo dibujar cualquier cosa, ¿entonces puedo
predecir cualquier cosa?»**
**No.** Y ésta es la pregunta que hay que contestar mejor de toda la clase.
*«El teorema dice que la combinación **existe**. Tres cosas que no dice: que la
vayas a encontrar; con cuántos datos; y que sirva para casos que el modelo no
vio. Vos dibujaste la curva de 36 años que ya conocés. Nadie te prometió que el
2020 caiga cerca de esa curva.»* Y si querés cerrarlo con una imagen: apretá
«32 rampas» y mostrá que la curva pasa por todos los puntos, incluido el ruido.
«Esto ajusta perfecto y no sirve para nada. En la clase 4 tiene nombre.»

**4. «¿Cuántas capas y cuántas neuronas hay que poner?»**
*«No hay regla. Se prueba.»* En serio: se prueba, se mide en un conjunto de
validación que el modelo no vio, y se elige. La clase 4 es sobre **cómo se prueba
sin engañarse solo**. Si alguien insiste pidiendo un número, dale la única regla
honesta que existe: empezá por el modelo más chico que podría funcionar, y crecé
sólo mientras la validación mejore.

**5. «Esto que hicimos, ¿en qué se diferencia de una regresión polinómica? Yo ya
sé meterle términos cuadráticos a una regresión.»**
Excelente pregunta y hay que tomarla en serio, porque quien la hace tiene razón
en la intuición. *«Se parece muchísimo: en los dos casos armás una función
flexible sumando piezas. Tres diferencias que importan. Primera: un polinomio es
**global** —tocar un coeficiente mueve la curva entera, y los de grado alto se
vuelven locos en los extremos—. Una suma de rampas es **lineal por tramos**:
mover la altura de una rampa cambia sólo lo que está a la derecha de su codo, y
más allá del último dato la red sigue derecho con la última recta (extrapola
lineal, que no es lo mismo que acertar). Si conocés las *splines* lineales o la
regresión segmentada, es exactamente eso. Segunda: con polinomios vos elegís el
grado; acá el modelo acomoda **dónde** poner cada quiebre, que es una forma de
flexibilidad distinta. Tercera, y es la
grande: esto **escala a muchas variables de entrada**. Con dos predictores ya
tenés que decidir a mano qué interacciones meter; con veinte, es inviable. Ahí es
donde la red gana. Y lo que **no** cambia es el riesgo: la misma advertencia que
le hacés a un polinomio de grado 12 con 30 casos vale acá, sólo que peor.»*

**Bonus, si aparece: «¿esto es lo mismo que hace ChatGPT?»**
*«Es la misma pieza. ChatGPT es esto, muchísimas veces, con una forma de conectar
las piezas que vamos a ver en la clase 7. Pero el ladrillo es el que acabás de
armar hoy. No hay un segundo ingrediente secreto.»*

---

## 9. Las soluciones de los TODO (para vos, no para ellos)

- **TODO 1.** Cualquier tercera función sirve mientras el orden cambie el
  resultado. Con `menos_cinco(x) = x - 5`: `doble(mas_diez(menos_cinco(4))) = 18`
  y `menos_cinco(mas_diez(doble(4))) = 13`.
- **TODO 2 (V invertida).** `codo_2 = 5.0`, `altura_2 = -2.0`. La clave es que
  `|altura_2| > altura_1`: con `-1.0` la curva se aplana pero no baja.
- **TODO 3 (meseta).** `alturas = [1.0, -1.0, -1.0]` con
  `codos = [2.0, 4.0, 7.0]`. La segunda cancela exactamente a la primera (tramo
  plano) y la tercera hace bajar. Tres rampas.
- **TODO 4.** Partiendo de las cuatro rampas de `0.00060`. Ojo: para esos cuatro
  codos las alturas y la base **ya son las óptimas** (salen de mínimos
  cuadrados), así que tocando sólo alturas o base no se mejora; el notebook lo
  avisa. Hay que mover o agregar codos. Dos soluciones verificadas (alturas
  redondeadas a 4 decimales, que es lo que se tipea a mano):

  | codos | base | alturas | desajuste |
  |---|---|---|---|
  | 1996, 2002, 2007, 2012, 2016 | `0.0806` | `-0.0101, 0.0222, -0.0282, 0.0531, -0.0415` | **0.00039** |
  | 1996, 2002, 2007, 2010, 2014, 2017 | `0.0807` | `-0.0103, 0.0238, -0.0369, 0.0308, 0.0390, -0.0804` | **0.00029** |

  Siguiendo la pista (agregar un codo en 2007, o en 2006 y 2014, y reacomodar)
  se llega a 0.00039 y 0.00031 con las alturas óptimas.

  Ojo: **no les des estos números.** Lo importante no es el valor al que lleguen
  sino que **descubran que es un suplicio** encontrarlos: ése es el motor de la
  clase 3. La estrategia que sí conviene darles es la de la pista: mirar el
  palito rojo más largo y poner un codo ahí.
- **TODO 5.** La curva con sigmoides queda redondeada; con rampas, angulosa. La
  respuesta buena a «¿por qué?» es: cada pieza dobla suave en vez de doblar de
  golpe. La parte de tocar `suavidad`, medida con los mismos cuatro codos
  (rampas: `0.00060`): `0.05` → `0.00074`, `0.25` → `0.00066`, `1` → `0.00052`,
  `5` → `0.00050`. Con `suavidad` grande cada sigmoide es casi un **escalón**
  (la pieza de Nielsen) y, con estos codos, le gana a las rampas. Es un buen
  momento para decir que no hay un doblez «mejor» en general: depende de la
  curva y de dónde están los codos.

---

## 10. Los números de la viz (medidos, no estimados)

Todos los números que aparecen en `viz/rampas.html`,
`viz/la-recta-imposible.html`, `viz/red-como-dibujante.html` y las slides salen
de este script (se corre desde la raíz del repo). Si cambiás los datos o los
codos, **volvé a correrlo**: un número inventado en un curso sobre no inventar
es el peor error posible.

> **Estos números cambiaron.** La primera versión de la clase usaba una media
> móvil que, en 1984, promediaba con el dato de 1975 (el anterior que hay en la
> serie, nueve años antes). Con el borde corregido en `ssdl.datos`, el valor de
> 1984 pasa de 0.0762 a 0.1143 y cambian todos los desajustes: la recta pasa de
> 0.00150 a 0.00156 y su R² de 1,3 % a 0,5 %. Los otros 35 valores de la serie no
> cambiaron.

```python
import itertools, os, sys
import numpy as np
sys.path.insert(0, "_shared"); os.environ["DLSS_RAIZ"] = os.getcwd()
from ssdl import datos

anios, y = datos.serie_menciones("inflacion", desde=1984, hasta=2019, suavizada=True)

def ajustar(codos):
    """Mejores alturas (y base) para esos codos, por mínimos cuadrados."""
    A = np.column_stack([np.ones_like(anios)] + [np.maximum(0, anios - c) for c in codos])
    w, *_ = np.linalg.lstsq(A, y, rcond=None)
    return w, A @ w

def mse(p):
    return float(np.mean((y - p) ** 2))

print("sólo el promedio   ", mse(np.full_like(y, y.mean())))                 # 0.001568
print("la mejor recta     ", mse(np.polyval(np.polyfit(anios, y, 1), anios)))  # 0.001561
ATAJOS = {1: [2013], 2: [1985, 2012], 4: [1995, 1997, 2014, 2017],
          8: [1990, 1992, 1994, 1999, 2007, 2010, 2014, 2017],
          32: [1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1994, 1995, 1996,
               1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
               2008, 2009, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]}
for n, codos in ATAJOS.items():
    print(f"{n:2d} rampas          ", mse(ajustar(codos)[1]))

# Los atajos de 1, 2 y 4: búsqueda exhaustiva con separación mínima de 2 años.
candidatos = range(1985, 2019)
for n in (1, 2, 4):
    print("óptimo", n, min((mse(ajustar(c)[1]), c) for c in itertools.combinations(candidatos, n)
                           if all(c[i + 1] - c[i] >= 2 for i in range(n - 1))))

# La red buena de red-como-dibujante: los codos fijos (w1, b1) y las alturas
# (w2) y la base (b2) por mínimos cuadrados, con el año llevado a 0-1.
w1 = np.array([1.60, 0.90, 2.20, 1.20, 0.70, 1.90])
b1 = np.array([-0.5029, -0.3857, -1.4457, -0.8914, -0.6000, -1.7914])
H = np.maximum(0, ((anios - 1984) / 35).reshape(-1, 1) * w1 + b1)
w, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(y)), H]), y, rcond=None)
print("red buena: b2", round(w[0], 5), "w2", np.round(w[1:], 4),
      "MSE", mse(H @ np.round(w[1:], 4) + round(w[0], 5)))

# Sacar una rampa de las 8, sin reacomodar y reacomodando (§6, «si vas adelantado»).
w8, _ = ajustar(ATAJOS[8])
A8 = np.column_stack([np.ones_like(anios)] + [np.maximum(0, anios - c) for c in ATAJOS[8]])
for i, c in enumerate(ATAJOS[8]):
    sin = w8.copy(); sin[i + 1] = 0
    otros = ATAJOS[8][:i] + ATAJOS[8][i + 1:]
    print("sacar", c, "sin reacomodar", round(mse(A8 @ sin), 6),
          "reacomodando", round(mse(ajustar(otros)[1]), 6))
```

Salida esperada:

| Modelo | Desajuste (MSE) |
|---|---|
| sólo el promedio (una raya horizontal) | `0.001568` |
| la mejor recta posible | `0.001561` — **R² = 0,5 %**, pendiente +0,00026 puntos porcentuales por año |
| 1 rampa (codo en 2013) | `0.000916` |
| 2 rampas (1985, 2012) | `0.000648` |
| 4 rampas (1995, 1997, 2014, 2017) | `0.000339` |
| 8 rampas | `0.000164` |
| 32 rampas (un codo casi por año) | `0.0000076` |
| red buena de `red-como-dibujante` (6 rampas) | `0.000200` |

Los codos de 1, 2 y 4 rampas son el óptimo por búsqueda exhaustiva con
separación mínima de 2 años. Los de 8 son el mejor juego que encontró una
búsqueda local (60 arranques al azar, mismo criterio de separación): un buen
juego, no necesariamente el óptimo. Los de 32 están repartidos parejo.

La «configuración buena» de `viz/red-como-dibujante.html` son 6 rampas con codos
en 1995, 1999, 2007, 2010, 2014 y 2017, escritas como pesos de una red `[1, 6, 1]`
con la entrada normalizada a 0–1 (19 perillas: 6 + 6 + 6 + 1).

Sacar una rampa de las 8 (§6):

| rampa | sin reacomodar | reacomodando |
|---|---|---|
| 1990 | 0.052 | 0.000192 |
| 1992 | 0.292 | 0.000209 |
| 1994 | 0.276 | 0.000267 |
| 1999 | 0.055 | 0.000424 |
| 2007 | 0.015 | 0.000313 |
| 2010 | 0.0062 | 0.000239 |
| 2014 | 0.0026 | 0.000292 |
| 2017 | 0.0011 | 0.000376 |

---

## 11. Antes de entrar al aula

- [ ] Abrí `slides.html` con doble clic y pasá las 35 slides una vez. Sin
      internet: tiene que verse igual.
- [ ] Abrí las cinco viz sueltas y movelas. Especialmente `rampas.html`: es la
      que vas a proyectar más tiempo.
- [ ] Corré el notebook entero una vez, en la máquina del aula si podés.
      Tarda menos de 10 segundos.
- [ ] Tené a mano una **hoja de papel** (para la slide 15) y, si conseguís, una
      **banda elástica** (para la slide 14).
- [ ] Decidí de antemano **qué vas a recortar** si a los 55 minutos no llegaste a
      la pausa. La lista está en la sección 6.
