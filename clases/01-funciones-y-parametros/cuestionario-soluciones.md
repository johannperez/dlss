# Clase 1 — Soluciones del cuestionario

**Para quien da la clase.** Acá no está sólo cuál es la correcta: está **por qué cada
distractor es tentador y qué confusión revela elegirlo**. Eso es lo que sirve cuando
alguien te muestra su respuesta y hay que decidir en diez segundos qué decirle.

Si en tu aula un distractor se lleva más del 30 % de las respuestas, esa confusión no
se desarmó en clase y conviene volver sobre ella al arrancar la clase 2.

---

## 1. ¿Cuál es un parámetro? — **Correcta: B**

**B (`a`).** Es el mismo número para los 36 años de la base. Esa es la definición
operativa que usamos toda la clase.

| Distractor | Por qué es tentador | Qué confusión revela |
|---|---|---|
| **A (`x`)** | `x` es lo que uno «mueve» cuando juega con la función, y «mover» se siente como «ajustar». | Confunde *lo que yo manipulo en la pantalla* con *lo que el modelo trata como fijo*. Es **la** confusión de la clase. Antídoto: la regla del dedo y la viz `variable-vs-parametro.html`. |
| **C (`f(x)`)** | Es lo que «sale» y por eso parece el resultado importante. | Confunde la salida con la perilla. Suele venir de gente que nunca vio una función escrita así y está agarrándose de lo único con nombre. Es una confusión fácil de desarmar señalando el dibujo de la caja. |
| **D («depende»)** | Es la respuesta prudente, y en muchos contextos la prudencia paga. | Acá **no** depende, y vale decirlo claro: dentro de un modelo dado, `a` es parámetro y `x` es variable, punto. Ahora bien: la persona que elige D suele estar pensando en algo real y más profundo —que un mismo número puede ser parámetro en un modelo y variable en otro— y eso merece un «tenés razón en otro nivel» antes del «pero acá no». |

---

## 2. Parámetro vs variable — **Correcta: C**

**C.** El parámetro es el mismo para todos los casos de la base; la variable cambia de
un caso a otro.

| Distractor | Por qué es tentador | Qué confusión revela |
|---|---|---|
| **A (decimal vs entero)** | En los ejemplos de clase `a` suele ser 0,004 y `x` suele ser 1998. El patrón visual existe. | Confunde una **coincidencia de formato** con una **diferencia de rol**. Es un buen momento para decir que el año podría escribirse 1998,0 y no cambiaría nada. |
| **B (letras del alfabeto)** | Es cierto que la convención existe: `a, b, c` para parámetros, `x, y, z` para variables. | Confunde la convención tipográfica con la definición. Peligroso porque **funciona** casi siempre y falla justo cuando importa (en la clase 2 los parámetros se van a llamar `w`, y en la 6 los datos se van a llamar `V`). |
| **D (quién lo calcula)** | Tiene algo de verdad: los parámetros muchas veces los estima la computadora. | Confunde **quién produce el número** con **qué papel juega**. Hoy los parámetros los movieron a mano, y no dejaron de ser parámetros por eso. |

---

## 3. Qué pasa si… — respuestas

**(a)** La recta **gira**. Se hace más empinada. Gira alrededor del punto donde `x`
vale 0, o sea alrededor de `(0, b)` = `(0, 10)`, que es el único punto que no se
mueve.

**(b)** La recta **se traslada entera hacia arriba**, sin girar: la inclinación no
cambió. Todas las alturas suben 10.

**(c)** Sólo el cambio de `b`. `f(0) = a·0 + b = b`, así que `a` no puede afectar
ese valor.

**Errores típicos y qué revelan:**

- *«Las dos cosas suben la recta»*: es verdad que subir `a` levanta la recta **a la
  derecha del cero**, así que la respuesta no es absurda. Lo que falta es notar que a
  la **izquierda** del cero la baja. Buen momento para dibujar el punto fijo.
- *«Gira alrededor del centro del gráfico»*: confunde el centro visual del encuadre
  con el origen. Si en la viz el eje empieza en 1983 y no en 0, esta confusión aparece
  casi garantizada. Por eso el notebook reparametriza a «años desde 1984».
- *«`b` también la inclina un poco»*: no. Vale mostrarlo moviendo sólo `b` en la viz.

---

## 4. `a = 0` — respuestas

**(a)** Queda una **recta horizontal** a la altura `b`.

**(b)** Una oración posible: *«El tema ocupó siempre la misma proporción del
discurso, todos los años, sin ninguna tendencia».* O más corto: *«acá no pasó nada».*

**(c)** **No es tonta en absoluto.** Es el modelo «no hay tendencia», que en
estadística es la hipótesis nula y en una investigación es un resultado perfectamente
publicable. Y hay más: sobre estos datos, la recta horizontal en el promedio da un
desajuste de **0.0165**, contra **0.0146** de la mejor recta posible. O sea que **el
modelo "no pasó nada" casi empata con el mejor modelo lineal que existe**. Eso es un
hallazgo sobre el fenómeno, no una limitación del método.

**Qué revela cada tipo de respuesta:**

- Quien dice «queda un punto» está pensando en `f(x) = 0`, no en `a = 0`: confundió
  anular el parámetro con anular la función.
- Quien dice «es un modelo inútil» todavía no entiende que **un modelo sin efecto es
  un resultado**. Es una excelente puerta de entrada a la conversación sobre por qué
  los papers con resultados nulos casi no se publican.
- Quien escribe la oración usando la palabra «pendiente» aunque se lo pediste sin
  jerga: no está mal, pero es exactamente el hábito que el `[EL LUNES]` quiere romper.
  Pedile la versión para su abuela.

---

## 5. Ordenar tres rectas — **Correcta: R, P, Q**

De menor a mayor desajuste: **R** (la que sube), después **P** (horizontal en el
promedio), y muy lejos **Q** (horizontal en 0,40).

Justificación sin cuentas: R sigue la nube y encima capta que sube; P pasa por el
medio pero ignora la tendencia; Q está por encima de casi todos los puntos, así que
casi todos los errores son grandes y del mismo signo.

Los números medidos, por si los querés dar: R = **0.0146**, P = **0.0165**,
Q ≈ 0.076.

**Errores típicos:**

- *«Q es la mejor porque pasa cerca de los picos»*: mirar los cuatro puntos altos y
  olvidar los treinta y dos bajos. Es una lectura selectiva y muy común; conviene
  nombrarla, porque es la versión de bolsillo de sobreajustar a los casos llamativos.
- *«P y R están igual de bien»*: **es casi cierto** y quien lo dice está leyendo bien
  el gráfico. La respuesta correcta es «tenés razón en que la diferencia es chica, y
  eso es justamente el hallazgo». No lo marques como error.
- Quien invierte P y Q no está mirando la escala del eje: vale la pena preguntarle
  dónde está el 0,40 en el gráfico.

---

## 6. Familia de curvas — respuestas

**(a)** Se movió un **parámetro**. Si se hubiera movido una variable, tendrías una
sola curva con una bolita corriéndose sobre ella, no ocho curvas.

**(b)** La que controla **dónde está el salto** (el punto de mitad de camino). Se
sabe porque todas tienen la misma inclinación en el salto y el mismo techo: lo único
que cambió fue el año en que ocurre.

**(c)** Las ocho curvas juntas son **la familia de todas las teorías que ese modelo
puede sostener**. Elegir el parámetro es elegir una de esa familia. Es literalmente
el rastro violeta de `variable-vs-parametro.html`.

**Qué revela contestar «se movió `x`»:** que la distinción no quedó, y que la viz 2
hay que volver a mostrarla. Es la pregunta más diagnóstica del cuestionario: si más
del 30 % del aula contesta «variable», arrancá la clase 2 con esa viz.

---

## 7. Reconocer la forma — **1-D, 2-E, 3-A, 4-B, 5-C**

| # | Forma | Por qué |
|---|---|---|
| 1 | **D, sigmoide** | «arrancó despacio, se aceleró, ya casi no crece» son las tres zonas de la S: arranque, explosión y **techo**. La palabra clave es la saturación. |
| 2 | **E, seno** | «cada cuatro años, sin falta» = periodicidad. |
| 3 | **A, recta** | «siempre lo mismo por año» = cambio constante por unidad. |
| 4 | **B, parábola** | «subió, llegó a un máximo, ahora baja» = un punto de giro. |
| 5 | **C, exponencial** | «casi no se notó y después se disparó sin freno» = crecimiento que se acelera **y no tiene techo**. |

**Las dos confusiones que hay que esperar:**

- **1 con 5** (sigmoide con exponencial). Las dos «arrancan despacio y se disparan».
  La diferencia está en el final: la sigmoide **se satura**, la exponencial no tiene
  techo. Si alguien las cambia, la pregunta que lo desatasca es: *«¿y después qué
  pasa?»*. Vale la pena decir además que en el mundo real **casi nada es
  exponencial por mucho tiempo**: todo lo que parece exponencial suele ser la primera
  mitad de una sigmoide que todavía no encontró su techo. Es una idea que se paga
  sola en cualquier discusión sobre difusión.
- **4 con 2** (parábola con seno). «Sube y baja» describe las dos. La diferencia es
  si **vuelve a subir**. La parábola tiene un solo giro; el seno, infinitos.

---

## 8. Traducción sustantiva — no hay respuesta única

**(a) Una respuesta buena:** *«Según este modelo, en 1984 alrededor del 0,21 % de las
palabras del discurso de apertura estaban dedicadas al léxico de educación, y esa
proporción viene subiendo unos 0,0037 puntos por año, o sea unos 0,13 puntos a lo
largo de los 35 años del período».*

Lo que tiene que estar para darla por buena:
1. Que `b` se traduzca a **un valor en un año concreto** (1984), no a «la ordenada».
2. Que `a` se traduzca a **cuánto cambia por año**, con el signo bien leído (sube).
3. Que se mencione la unidad: **porcentaje de palabras del discurso**, no
   «menciones» ni «importancia».

Dato de contexto por si preguntan: la serie de educación va de 0,03 % a 0,69 %, con un
promedio de 0,27 %, y esa recta deja un desajuste de **0.0175** — o sea que también
acá la tendencia lineal es débil y ruidosa. Los números salen de
`medir-referencias.py`.

**(b) Respuestas buenas para lo que el modelo NO dice** (cualquiera de estas):

- No dice que a los gobiernos les haya importado **más** la educación: dice que le
  dedicaron más palabras en **ese** discurso.
- No dice que la suba haya sido pareja. Un modelo lineal **impone** que sea pareja;
  la serie real puede haber saltado de golpe en un año y quedarse quieta después.
  (Y de hecho no es pareja: la serie va de 0,03 % a 0,69 % dando tumbos.)
- No dice nada sobre 2025: extrapolar fuera del rango de los datos es una decisión
  tuya, no del modelo.
- No dice que la educación haya mejorado, ni empeorado. No mide política educativa:
  mide palabras.

**Errores típicos de (a) y (b):**

- *«Cada año hay un 0,37 % más de educación»*: confunde el porcentaje de palabras con
  un porcentaje de otra cosa, y confunde 0,0037 con 0,37. Es un error de escala y hay
  que corregirlo con firmeza, porque es el mismo error que la trampa de
  `serie_menciones` (los valores **ya vienen en porcentaje**: 0,21 quiere decir
  «el 0,21 % de las palabras», no «el 21 %»).
- *«A la educación se le dio más importancia»*: el salto ilegítimo del indicador al
  constructo. Es exactamente el tema de la clase 10 y conviene celebrarlo como una
  buena oportunidad, no como un error.
- Contestar (b) con «no dice si es significativo»: es una respuesta correcta pero de
  otra caja de herramientas. Aceptala y pedile una segunda que no use jerga
  estadística.

**(c)** Cambiaría el verbo —«baja» en vez de «sube»— y el signo del total del período.
**No** cambiaría nada de lo demás: ni la unidad, ni el punto de partida en 1984, ni la
advertencia de que el modelo **impone** que el cambio sea parejo año a año. Quien
conteste sólo «cambiaría el signo» tiene razón pero se quedó en la aritmética; lo que
buscamos es que note que la **forma de la afirmación** es la misma.

---

## 9. El error en el código — respuestas

**Primera función.** Le falta el `return`. Calcula `resultado` y no lo devuelve
nunca, así que la función devuelve `None`. La línea que falta:

```python
    return resultado
```

o directamente `return a * x + b`.

**Cómo se manifiesta en la práctica:** no da error rojo. Da algo peor: `None`, y el
error explota tres celdas más abajo con un mensaje que no menciona esta función.
Vale decirlo en clase: **los errores silenciosos son peores que los ruidosos.**

**Segunda función.** Dice `a * b + b` donde debería decir `a * x + b`. Nunca usa `x`,
así que devuelve siempre el mismo número sin importar qué le metas.

**Cómo se detecta:** llamándola dos veces con `x` distinto y viendo que da lo mismo.
Es un buen momento para instalar el hábito: **probá tu función con dos valores antes
de confiar en ella**.

**Qué revela no encontrarlos:** casi siempre, que se está leyendo el código como si
fuera prosa en vez de seguirlo línea por línea. La técnica que sí funciona —y conviene
enseñarla explícitamente— es **ejecutar la función mentalmente con un número
concreto**: «si x vale 2, a vale 3 y b vale 1, ¿qué devuelve?».

---

## 10. Criterio — no hay respuesta única, y hay que decirlo

**Esto abre la conversación que cierra el curso en la clase 10.** No corrijas: pedí
que amplíen.

Objeciones que se esperan (dos bien argumentadas alcanzan):

| Objeción | Qué evidencia haría dudar menos |
|---|---|
| **Hablar mucho puede ser reacción, no prioridad.** Si el tema domina los diarios en febrero, el discurso del 1 de marzo lo va a tocar sí o sí. | Comparar la serie con la cobertura mediática del mes anterior. Si van juntas, la medida está capturando agenda mediática. |
| **Un gobierno puede actuar mucho y hablar poco** (o al revés). | Contrastar con presupuesto ejecutado, leyes enviadas al Congreso o cargos creados en el área. |
| **El discurso de apertura es un género con reglas propias.** Hay secciones obligadas; el espacio no se reparte libremente. | Ver si la proporción cambia cuando se compara con otros discursos del mismo gobierno (cadena nacional, campaña). |
| **La lista de 23 palabras la escribimos nosotros.** Sacar «policía» o agregar «orden» mueve la serie. | Repetir el análisis con dos o tres léxicos alternativos y mostrar que las conclusiones no cambian (análisis de sensibilidad). |
| **El largo de los discursos cambió por un factor de nueve.** Normalizamos por palabras, pero un discurso de 25.000 palabras cubre más temas que uno de 2.900. | Comparar las series normalizadas contra las crudas y ver si la historia es la misma. |
| **El discurso no lo escribe quien lo lee.** Lo escribe un equipo y se negocia con los ministerios. | Ninguna, y por eso hay que cambiar la afirmación: no es «lo que el presidente pensaba», es «la agenda que la Presidencia decidió mostrarle al Congreso». |

**Qué contestar a quien dice «entonces la medida no sirve».** Que no. Que **ninguna
medida social captura su constructo del todo**, y que el trabajo no es encontrar la
medida perfecta sino **escribir en el paper la afirmación que la medida sí banca**.
Esa es la diferencia entre una investigación defendible y una que se cae en el primer
comentario del revisor 2.

---

## 11. Bonus — no se corrige

No hay respuesta correcta y **no conviene evaluarla**. Lo único que importa es que la
hayan pensado antes de la clase 2, porque la clase 2 arranca exactamente ahí.

Ideas que suelen aparecer, y qué hacer con cada una:

- *«Usar una fórmula más complicada, un polinomio de grado alto»* → es el **camino A**
  de la slide 32. Funciona y es lo que hizo la estadística durante un siglo. Guardala:
  en la clase 4 vamos a ver por qué un polinomio de grado 20 sobre 36 puntos es una
  trampa.
- *«Partir el gráfico en pedazos y ponerle una recta a cada pedazo»* → **es casi
  exactamente lo que hace una red neuronal.** Quien diga esto acaba de reinventar la
  suma de rampas y merece que se lo digas en voz alta al aula.
- *«Sumar dos de las formas del zoo»* → también correcto, y es la palabra clave:
  **sumar**. Es el título de la clase 2.
- *«No se puede»* → «tenés razón con una sola forma. La semana que viene te muestro
  qué pasa con ocho.»
