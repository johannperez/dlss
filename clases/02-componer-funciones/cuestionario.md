# Cuestionario — Clase 2

**Componer funciones: dibujar lo imposible**

> Once preguntas. No hay que estudiar nada de memoria: todas se contestan con lo
> que viste moverse en clase. Las que piden escribir, escribilas de verdad — son
> las que más te van a servir el día que tengas que revisar un paper.
>
> Tiempo estimado: 25-30 minutos. Se hace en casa, antes de la clase 3.

---

## 1. Qué significa componer *(múltiple choice)*

Tenés dos funciones, `f` y `g`. ¿Qué quiere decir «componerlas», o sea escribir
`g(f(x))`?

- **A)** Sumar los dos resultados: primero calculás `f(x)`, después `g(x)`, y los sumás.
- **B)** Meter `x` en `f`, y lo que sale de `f` meterlo en `g`.
- **C)** Multiplicar las dos funciones entre sí.
- **D)** Elegir la que dé el resultado más chico de las dos.

---

## 2. Por qué no alcanza con apilar *(múltiple choice)*

¿Por qué apilar capas lineales, una atrás de la otra, **sin nada en el medio**,
no aporta ninguna flexibilidad?

- **A)** Porque las computadoras no pueden calcular más de dos capas seguidas.
- **B)** Porque el resultado de encadenar rectas es siempre otra recta: se colapsa a dos números, por más capas que pongas.
- **C)** Porque hacen falta más datos para entrenar tantas capas.
- **D)** Porque las capas lineales se cancelan entre sí y el resultado da cero.

---

## 3. Seguir el número *(qué pasa si…)*

Tenés `f(x) = 2x` y `g(x) = x + 3`.

**(a)** Calculá `f(g(1))`.
**(b)** Calculá `g(f(1))`.
**(c)** ¿Por qué dan distinto? Explicalo en una oración, sin usar la palabra «porque sí».

---

## 4. Cuántas rampas *(qué pasa si…)*

**(a)** Tenés una red con **5 rampas** y la curva que querés dibujar tiene
**9 quiebres claros**. ¿Qué esperás que pase? ¿Qué vas a ver en el gráfico?

**(b)** Ahora al revés: tenés **500 rampas** y **12 puntos de datos**.
¿Qué esperás que pase? ¿Y eso es bueno?

---

## 5. Contar codos *(leer un gráfico)*

Las cuatro curvas de abajo se dibujaron sumando rampas (y una base). Cada rampa
agrega **un** quiebre. Decí cuántas rampas tiene cada una.

```
(A)                          (B)
      ____                          /\
     /                             /  \
____/                        _____/    \____


(C)                          (D)
        /\                            /\
   /\  /  \                          /  \____
__/  \/    \___                _____/
```

*(Contá los puntos donde la pendiente cambia. Si querés, dibujalas en el
notebook con `red_a_mano` y comprobá.)*

---

## 6. Contar perillas *(leer un diagrama)*

Un diagrama de red con **2 entradas → 3 neuronas ocultas → 1 salida**.
Cada flecha es un **peso** y cada neurona (oculta o de salida) tiene además su
propio **sesgo**.

**¿Cuántos parámetros tiene la red en total?** Mostrá la cuenta, no sólo el número.

---

## 7. La función de activación *(múltiple choice)*

¿Qué es una función de activación y qué pasaría si la sacáramos de una red de
tres capas?

- **A)** Es lo que decide si una neurona "se prende" o "se apaga"; sin ella la red no arrancaría.
- **B)** Es el doblez que va entre capa y capa; sin ella, las tres capas juntas serían equivalentes a una sola recta.
- **C)** Es lo que convierte la salida en una probabilidad; sin ella los resultados no sumarían 1.
- **D)** Es lo que evita que el modelo sobreajuste; sin ella el modelo memorizaría los datos.

---

## 8. Vocabulario *(aparear)*

Uní cada término con su definición en castellano llano.

| | Término | | Definición |
|---|---|---|---|
| 1 | peso (*weight*) | a | Un grupo de rampas trabajando en paralelo, que no es ni la entrada ni la salida. |
| 2 | sesgo (*bias*) | b | Una rampa con sus perillas. |
| 3 | neurona | c | La perilla que multiplica. |
| 4 | capa oculta | d | El doblez que va entre capa y capa. |
| 5 | activación | e | La perilla que suma y desplaza la figura: en la salida la sube o la baja; en una rampa, le corre el codo. |

---

## 9. Leer el teorema *(múltiple choice, la difícil)*

El **teorema de aproximación universal** dice, más o menos: *con suficientes
neuronas en una capa oculta se puede aproximar cualquier función continua tan
bien como se quiera.*

¿Cuál de estas conclusiones **NO** se sigue del teorema?

- **A)** Existe alguna combinación de pesos que dibuja casi exactamente la curva que tengo.
- **B)** Si le doy suficientes neuronas, el modelo va a predecir bien los casos que todavía no vio.
- **C)** En principio, no hace falta una fórmula especial para cada curva: muchas piezas simples pueden representarla.
- **D)** El teorema no dice nada sobre **cuántos datos** hacen falta.

---

## 10. Encontrar el bug *(leer código)*

Esta versión de `red_a_mano` tiene un error. La original decía:

```python
def red_a_mano(x, codos, alturas, base=0.0):
    total = np.full_like(np.asarray(x, dtype=float), base)
    for codo, altura in zip(codos, alturas):
        total = total + rampa(x, codo, altura)
    return total
```

y alguien la reescribió así:

```python
def red_a_mano(x, codos, alturas, base=0.0):
    for codo, altura in zip(codos, alturas):
        total = np.full_like(np.asarray(x, dtype=float), base)
        total = total + rampa(x, codo, altura)
    return total
```

**(a)** ¿Cuál es el error?
**(b)** Si la llamás con cuatro rampas, ¿qué curva va a dibujar?
**(c)** ¿Se rompería con un mensaje de error, o andaría y daría mal? ¿Por qué eso
es peor?

---

## 11. Criterio aplicado *(escribí de verdad)*

Un colega te dice, en un pasillo:

> «Usé una red neuronal con 2 millones de parámetros para modelar la trayectoria
> de 80 municipios. Ajusta perfecto: el R² da 0,99.»

**(a)** De las dos preguntas de revisor de la clase (*¿cuántas perillas?* y
*¿cuántos datos?*), tu colega ya te contestó una sin que se la hicieras. ¿Cuál?
Escribí **la que falta** y **una tercera** que le agregarías.

**(b)** Explicá, para cada una de las dos que escribiste, **qué información te
da** la respuesta.

**(c)** ¿Por qué «ajusta perfecto» es, en este caso, una señal de alarma y no un
resultado? Contestá en tres o cuatro oraciones.

**(d)** *(La que importa.)* Pensá en un modelo o una medida que hayas usado en tu
propia investigación —una regresión, un índice, una escala—. ¿Cuántas «perillas»
tenía y cuántos casos? ¿Le harías a tu propio trabajo las mismas preguntas?
