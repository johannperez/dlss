# Clase 2 — Componer funciones: dibujar lo imposible
**Directorio:** `clases/02-componer-funciones/`
**Duración:** 120 min · **Prerrequisitos:** clase 1 (variable vs parámetro, el zoo)

---

## 1. Narrativa de la clase

Esta es la clase donde se revela **qué es** una red neuronal, y hay que llegar a esa revelación por
necesidad, no por anuncio. La secuencia emocional es: frustración → una idea tonta → asombro.

1. **Frustración (el gancho).** Se les da la mejor herramienta de la clase 1 —la recta con sus dos
   perillas— contra un problema que no puede resolver. Se intenta en serio, en vivo, con el aula
   gritando valores. Se fracasa. Se prueba "darle más perillas a la recta" y se descubre que
   `a·x + b + c` es la misma recta con otro nombre: **más parámetros no es más expresividad**. Esa
   sub-lección es valiosa por sí sola y desarma la idea de que "más grande = mejor".
2. **La idea tonta: encadenar.** Si una máquina no alcanza, ponemos la salida de una en la entrada
   de otra. Se hace a mano, con números, siguiendo un valor por tres cajas. Analogía social directa:
   una cadena de mediaciones (dato bruto → codificación → índice → interpretación).
3. **El descubrimiento incómodo.** Encadenar rectas da... una recta. Se demuestra visualmente y con
   números, no con álgebra. Segundo fracaso, más profundo. Ahora sí el aula quiere la solución.
4. **El doblez.** ReLU: `max(0, x)`. La función más tonta imaginable — "si es negativo, poné cero".
   No hay nada que entender. Y con eso alcanza.
5. **El asombro.** Sumar rampas. Una, dos, cuatro, ocho. La curva imposible aparece. Este es **el
   momento del curso** en el que la audiencia entiende de qué se trata todo. Hay que darle aire:
   silencio, dejar que la vean, no explicar por encima.
6. **El nombre.** Recién ahora se dice "esto es una red neuronal con una capa oculta" y se muestra
   el diagrama de círculos y flechas, mapeando cada círculo a una rampa que ya vieron. El diagrama
   deja de ser un ícono místico y pasa a ser una notación.
7. **El desinflado saludable.** No hay neuronas, no hay cerebro, no hay pensamiento. Hay rampas
   sumadas. Y la puerta que queda abierta: los pesos los pusimos a mano y fue un suplicio.

`[CALLBACK DIBUJO]` — hoy la metáfora se vuelve literal: **componemos funciones para dibujar figuras
que ninguna función simple podía dibujar.** Frase textual para la slide: "en la clase 1 teníamos un
pincel; hoy tenemos una caja de pinceles y la posibilidad de pasarlos uno encima del otro."

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-4 | La figura que una recta no puede dibujar, por más perillas que le pongas. |
| 10-25 | Exposición: componer | 5-11 | Encadenar funciones y seguir el número por la cadena. |
| 25-35 | Viz + apuesta: el doblez | 12-17 | El baldazo: componer lineales da lineal. Hace falta ReLU. |
| 35-55 | Manos 1 | 18 | Notebook: componer a mano y ver la figura cambiar. |
| 55-65 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 18. |
| 65-85 | El momento fuerte: sumar rampas | 19-29 | 1 → 2 → 4 → 8 rampas. La viz más importante del curso. |
| 85-105 | Manos 2 | 30 | De a dos: dibujar la figura objetivo apilando rampas. |
| 105-120 | Cierre | 31-35 | Lo que NO es, `[EN TU INVESTIGACIÓN]`, el puente a la clase 3, el glosario. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (35 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Componer funciones | portada | Título + una curva compleja dibujada con trazo grueso. | "Al final de hoy van a saber exactamente qué es una red neuronal. Sin metáforas de cerebros." |
| 2 | Dónde quedamos | texto | Recap en 4 viñetas de la clase 1. La caja con perillas de nuevo. | "Función = caja con perillas. Variable recorre, parámetro deforma. ¿Alguien quiere agregar algo?" |
| 3 | **El desafío** | figura | La serie de menciones a *inflación*, 40 años, dos picos y un valle. | "Esto es real (o: esto es Aguasclaras, y es realista). Ajústenle una recta. Denme valores, yo los pongo." |
| 4 | Intento 1 | VIZ | `viz/maquina-de-perillas.html` (reusada de la clase 1) con los datos nuevos cargados. | Prueba 4-5 valores que grita el aula. El desajuste no baja de un piso. "No es que lo hagamos mal. **No se puede**." |
| 5 | ¿Y si le agrego perillas? | texto+figura | `f(x) = a·x + b + c` y `f(x) = a·x + b·1 + c·2`. Al lado, el gráfico: idéntico. | "Le puse tres perillas. Sigue siendo la misma recta. **Más parámetros no es más flexibilidad.** Acordate de esto cuando alguien te venda un modelo por su tamaño." |
| 6 | El problema real | texto | La forma de la función limita lo que podés afirmar. Callback al desafío 3 del zoo. | "El límite no es de precisión. Es de vocabulario: la recta no tiene cómo decir 'subió, bajó y volvió a subir'." |
| 7 | Una idea de albañil | figura | Dos cajas en serie: la salida de la primera entra a la segunda. | "Si una máquina no alcanza... poné dos." |
| 8 | Seguí el número | figura | Un `3` entrando a la primera caja, saliendo como `7`, entrando a la segunda, saliendo como `52`. Con los números grandes y el recorrido animado. | Lo recorre en voz alta. "Nada más que esto. La salida de una es la entrada de la otra." |
| 9 | Se escribe así | texto | `g(f(x))` y `h(g(f(x)))`, con colores y flechas que muestran el orden de adentro hacia afuera. | "Se lee de adentro para afuera, que es lo más incómodo de la notación matemática y lo lamento." |
| 10 | Ustedes ya componen | texto | Cadena de mediciones: respuestas crudas → recodificación → índice sumado → estandarización → tipología. Cada paso es una función. | "Tu pipeline de construcción de un índice **es** una composición de funciones. Ya sabés hacer esto, en papel." |
| 11 | **Jugá con la cadena** | VIZ | `viz/lego-de-funciones.html`. | "Miren los gráficos intermedios. La curva se transforma en cada etapa." |
| 12 | Apuesta | discusión | "Si encadeno dos rectas, ¿qué sale?" Tres opciones: una curva, una recta, un escalón. Se vota. | "Voten, no piensen mucho. Mayoría dice curva." |
| 13 | **El baldazo** | VIZ | `viz/sin-no-linealidad.html`. | "Recta. Sale una recta. Y con diez rectas encadenadas también. Puedo poner mil capas y sigue siendo una recta." |
| 14 | Por qué | figura | Sin álgebra: dos "estiramientos" seguidos es un estiramiento. Con una imagen de una goma que se estira dos veces. | "Estirar y volver a estirar es estirar. No hay forma de que aparezca un codo." |
| 15 | Falta un doblez | figura | Una hoja de papel plana, y la misma hoja doblada una vez. | "Necesitamos algo que **doble**. Y va a ser ridículamente simple." |
| 16 | **ReLU: la rampa** | figura | `relu(x) = max(0, x)` con su gráfico: plano en cero, después sube a 45°. En grande. | "Si es negativo, cero. Si es positivo, lo dejo pasar. Eso es todo. Esto es la función de activación más usada del planeta." |
| 17 | Una rampa con perillas | VIZ | Mini-viz embebida: una ReLU con 3 sliders (dónde está el codo, qué tan empinada, hacia arriba o hacia abajo). | "Tres perillas y puedo poner el codo donde quiera, con la inclinación que quiera, para arriba o para abajo." |
| 18 | Bloque práctico 1 | texto | Consignas del notebook, parte 1. | "35 minutos. Componer funciones y hacer una V invertida con dos rampas." |
| 19 | Volvimos | discusión | ¿Cómo les fue con la V invertida? | Alguien lo hizo distinto: se muestra. |
| 20 | Y ahora, el truco | texto | "¿Qué pasa si sumo muchas rampas, cada una con su codo en un lugar distinto?" | "Piensen antes de que lo muestre." |
| 21 | **1 rampa** | VIZ | `viz/rampas.html`, estado inicial: 1 rampa contra la curva objetivo. | "Mal, obviamente." |
| 22 | **2 rampas** | VIZ | Misma viz, botón "agregar rampa". | "Un poquito mejor." |
| 23 | **4 rampas** | VIZ | | "Uy." |
| 24 | **8 rampas** | VIZ | La curva objetivo prácticamente reproducida. | **Silencio de 5 segundos.** "Esto es una red neuronal. Ya está. Eso es todo lo que hay." |
| 25 | Lo que acaban de ver tiene nombre | texto | *Teorema de aproximación universal* (Cybenko 1989, Hornik 1991; para la rampa, Leshno et al. 1993), enunciado en castellano llano: con suficientes rampas se aproxima cualquier función continua tan bien como quieras. | "No lo vamos a demostrar porque lo acaban de ver. Y ojo: el teorema dice que **existe** la combinación. No dice que la vayas a encontrar, ni con cuántos datos. Esa distinción va a importar en la clase 4." |
| 26 | Lo mismo, dibujado como red | figura | Diagrama clásico de círculos y flechas (1 entrada → 8 ocultas → 1 salida), con **cada círculo oculto pintado del color de su rampa** en el gráfico de al lado. | "Cada bolita es una rampa. Cada flecha es una perilla. El diagrama no tiene nada místico: es la misma suma de rampas con otra notación." |
| 27 | **Tocá una perilla, mirá la curva** | VIZ | `viz/red-como-dibujante.html`. | "Muevo este peso... y se movió **esta parte** de la curva. Cada perilla tiene su territorio." |
| 28 | El vocabulario mínimo | texto | Tabla: *peso* = perilla multiplicativa; *sesgo/bias* = perilla que desplaza; *neurona* = una rampa; *capa* = un grupo de rampas en paralelo; *capa oculta* = las del medio; *activación* = el doblez; *profunda* = muchas capas. | "Siete palabras. Con estas siete entendés el 90% del vocabulario de cualquier paper." |
| 29 | ¿Por qué "profundo"? | figura | Comparación: una capa ancha (muchas rampas) vs varias capas angostas. La segunda arma "partes de partes". | "Ancho: muchas piezas simples. Profundo: piezas hechas de piezas. Lo segundo es más eficiente y es de donde sale la palabra *deep*. Lo vamos a ver muy claro con imágenes en la clase 5." |
| 30 | Bloque práctico 2 | texto | Consignas parte 2: la red a mano con 4 neuronas. | "Van a escribir una red neuronal en 6 líneas, sin PyTorch, sin nada." |
| 31 | Lo que NO es | texto | No es un cerebro. No piensa. No entiende. Es una suma de rampas con las perillas bien puestas. | "Y esto no lo digo por humildad: lo digo porque si creés que piensa, vas a interpretar mal sus errores. Vas a ver en la clase 8." |
| 32 | `[EN TU INVESTIGACIÓN]` | texto | Cuando leas "usamos una red neuronal", traducí: "usamos una función muy flexible con muchísimas perillas". Y hacé las dos preguntas de revisor: ¿cuántas perillas? ¿cuántos datos? | "Un modelo con más perillas que datos puede dibujar cualquier cosa, incluido el ruido. Ese es el tema de la clase 4 y es el error más común en los papers que van a revisar." |
| 33 | El problema que queda | figura | El panel de la viz de 8 rampas con sus 24 sliders, todos desordenados. | "Yo puse estos 24 números a mano y me llevó una tarde. Un modelo de verdad tiene millones. ¿Cómo se encuentran?" |
| 34 | El puente | texto | "Clase 3: la máquina busca sola. Necesitamos dos cosas: un número que mida qué tan mal está, y una brújula que diga para dónde ir." | "Y las dos ya las vieron sin saberlo: el número es el 'desajuste' del ajuste a ojo." |
| 35 | Glosario de hoy | texto | composición, no linealidad, ReLU, activación, peso, sesgo, neurona, capa, capa oculta, profundo, aproximación universal. | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/lego-de-funciones.html`
- **Qué se ve.** Tres bloques en fila horizontal, tipo cadena de montaje. Cada bloque tiene: un
  nombre elegible por dropdown (duplicar, elevar al cuadrado, rampa/ReLU, sigmoide, sumar), un
  slider de parámetro, y **debajo de cada bloque un mini-gráfico** que muestra la curva acumulada
  hasta ese punto de la cadena.
- **Controles.** Los 3 dropdowns, los 3 sliders, y un **valor de entrada `x` arrastrable** que se
  ve viajar por la cadena como una bolita, mostrando su valor numérico en cada etapa.
- **Qué tiene que hacer clic.** Que la composición es literalmente secuencial y que **el orden
  importa**: intercambiar el bloque 1 y el 2 cambia el resultado.
- **Momento aha.** "Cambié el orden de los dos bloques y me dio otra cosa. Componer no es sumar."
- **Detalle.** Botón "intercambiar bloque 1 y 2" que hace el swap de golpe y muestra las dos curvas
  superpuestas. Ese botón es el que produce el aha; sin él la viz es sólo linda.

### 3.2 `viz/sin-no-linealidad.html`
- **Qué se ve.** Dos columnas. **Izquierda, "sin doblez":** N cajas lineales encadenadas
  (slider de N, 1 a 6), cada una con sus dos perillas al azar (botón "randomizar"); el gráfico
  final: siempre una recta, con un cartel que dice **"sigue siendo una recta"** en rojo.
  **Derecha, "con doblez":** las mismas N cajas pero con una ReLU entre cada par; el gráfico final:
  una poligonal con N-1 codos, con el cartel **"N-1 codos"**.
- **Controles.** Slider de N, botón "randomizar perillas" (que se puede apretar 20 veces; la
  izquierda siempre da una recta), toggle "poner los dobleces".
- **Qué tiene que hacer clic.** La **imposibilidad**: por más que randomices, la columna izquierda
  nunca deja de ser una recta. La evidencia se construye por repetición, no por argumento.
- **Momento aha.** "Aprieto randomizar veinte veces y siempre sale una recta. Ah: **es imposible**,
  no es que tengo mala suerte."
- **Detalle clave.** Un contador "randomizaste 14 veces, salieron 14 rectas". Ese contador es el
  argumento.

### 3.3 `viz/rampas.html` — **la visualización más importante del curso**
- **Qué se ve.** Un panel grande. En gris grueso, la **curva objetivo** (menciones a *inflación*,
  40 años, dos picos y un valle). En azul, la **suma de rampas actual**. Abajo, un panel de rampas:
  cada rampa es una fila con 3 sliders (posición del codo, altura/pendiente, signo) y un mini-gráfico
  propio de 60px mostrando esa rampa sola, **pintada en su color**. La curva azul se dibuja como
  suma, y opcionalmente se muestran las rampas individuales en colores tenues por debajo.
- **Controles.**
  - Botón grande **"+ agregar rampa"** y "− quitar rampa".
  - Los 3 sliders por rampa.
  - Botón **"acomodar automáticamente"** (hace un ajuste rápido por mínimos cuadrados sobre las
    alturas, con los codos donde estén) — *se usa recién al final, y el docente aclara: "esto que
    acabo de apretar es lo que vamos a aprender a hacer la clase que viene".*
  - Toggle "mostrar las rampas por separado".
  - Indicador de desajuste con barra, igual al de la clase 1 (continuidad visual deliberada).
- **Qué tiene que hacer clic.** Que cada rampa se hace cargo de **un tramo** de la curva, y que
  agregando rampas se puede seguir mejorando indefinidamente.
- **Momento aha.** Con 8 rampas la curva azul tapa a la gris. "Con ocho cosas tontas dibujé algo que
  ninguna fórmula que conozco dibuja."
- **Segundo aha (deliberado, para la clase 4).** Botón **"32 rampas"**: la curva azul empieza a
  pasar por *todos* los puntos, incluidos los que claramente son ruido. El docente no lo explica
  hoy; sólo dice: "guarden esta imagen, en la clase 4 vamos a hablar de esto". Sembrar el
  overfitting visualmente dos clases antes de nombrarlo.
- **Rendimiento.** Todo en canvas, redibujo completo en cada `input`. Con 32 rampas y 400 puntos de
  grilla es trivial; nada de requestAnimationFrame complicado.

### 3.4 `viz/red-como-dibujante.html`
- **Qué se ve.** Dos paneles sincronizados. **Izquierda:** el diagrama de red (1 entrada, 6 ocultas,
  1 salida) con las flechas dibujadas con **grosor proporcional al valor absoluto del peso** y color
  según el signo (azul positivo, rojo negativo). **Derecha:** la curva que la red dibuja.
- **Controles.** Hacés **clic en una flecha** y aparece un slider para ese peso; al moverlo, la
  flecha cambia de grosor y **la parte de la curva afectada se resalta con un halo**.
  Botón "randomizar toda la red". Botón "volver a la configuración buena".
- **Qué tiene que hacer clic.** Que el diagrama de circulitos —el ícono que vieron mil veces en
  notas de divulgación— **es** la máquina de dibujar, y que cada flecha es una perilla con un efecto
  visible y localizable.
- **Momento aha.** "Toqué esta flecha de acá y se movió esa parte de la curva de allá. El diagrama
  no es un adorno, es un plano de cableado."
- **Detalle.** Al hacer hover sobre una neurona oculta, se resalta **su rampa** dentro de la curva
  de la derecha. Ese hover conecta directo con `viz/rampas.html`: es la misma cosa en dos notaciones.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** < 90 segundos, CPU. **Dependencias:** numpy, matplotlib.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Recap de la clase 1 en 4 líneas + qué vamos a hacer hoy. | |
| 2 | code | Imports + carga de la serie de *inflación* (patrón try/except). Scatter. | |
| 3 | code | **El fracaso reproducible.** Ajuste de la mejor recta posible (con `np.polyfit`, presentado como "la fórmula cerrada que existe para las rectas"), gráfico, desajuste impreso. | Que vean el fracaso en su propia pantalla, no sólo en la slide. |
| 4 | md | **Componer.** | |
| 5 | code | `def doble(x): return 2*x` / `def mas_diez(x): return x+10` y las cuatro combinaciones: `doble(mas_diez(3))` vs `mas_diez(doble(3))`. Con `print` de los dos. | El orden importa: 26 vs 16. |
| 6 | md | `TODO 1` — Escribí una tercera función y componé las tres. Predecí el resultado **antes** de correr la celda y anotalo en un comentario. *Pista: resolvé de adentro hacia afuera, como paréntesis.* | La predicción escrita es obligatoria. |
| 7 | code | Esqueleto para el TODO 1. | |
| 8 | md | **La rampa.** | |
| 9 | code | `def rampa(x, codo=0, altura=1): return altura * np.maximum(0, x - codo)` + gráfico de tres rampas con codos distintos. | Una línea. Se subraya que es una línea. |
| 10 | md | `TODO 2` — Sumá dos rampas para dibujar una **V invertida** (sube y baja). *Pista: la segunda rampa tiene que tener altura negativa y el doble de pendiente que la primera. Probá y mirá.* | Se resuelve por prueba y error; está bien. |
| 11 | code | Esqueleto + celda de verificación gráfica. | |
| 12 | md | `TODO 3` — Ahora una **meseta** (sube, se queda plana, baja). ¿Cuántas rampas necesitás? | Respuesta: 3. |
| 13 | md | **Sumar muchas rampas.** | |
| 14 | code | Función `red_a_mano(x, codos, alturas)` que suma N rampas en un `for`, y la grafica contra los datos. Se llama con 4 rampas y valores pre-elegidos que quedan decentes. | 6 líneas. Se subraya: "esto es una red neuronal". |
| 15 | code | Celda de juego: los arrays `codos` y `alturas` bien visibles arriba con `# ← toqueteá`. | |
| 16 | md | `TODO 4` — Bajá el desajuste a menos de X agregando y moviendo rampas. Anotá cuántas necesitaste. *Pista: poné un codo cerca de cada "quiebre" que veas en la curva gris.* | Enseña la estrategia de mirar la forma. |
| 17 | md | **Lo mismo con matrices** (opcional, marcado como "si te interesa cómo se escribe de verdad"). | |
| 18 | code | La misma red escrita con producto matricial: `W2 @ relu(W1 * x + b1) + b2`. Se verifica con un `assert` que da **exactamente lo mismo** que el `for`. | Momento importante: la notación matricial no es otra cosa, es la misma cosa escrita corta. Prepara PyTorch en la clase 4. |
| 19 | md | `TODO 5 (opcional)` — Cambiá `relu` por la sigmoide de la clase 1 y mirá qué pasa con la curva. ¿Se ve más suave o más angulosa? ¿Por qué? | Conecta el zoo con las activaciones. |
| 20 | md | **Para llevarte** + el problema abierto: "pusimos todos estos números a mano". | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Más parámetros = más flexible"** | Creen que la recta con 5 parámetros puede hacer curvas. | Slide 5, explícita. Y la viz 3.2 con su contador de randomizaciones. Es una creencia fuerte: hay que atacarla dos veces. |
| **"La composición es la suma"** | `g(f(x))` se lee como `g(x) + f(x)`. | El bloque de la bolita viajando (slide 8) y el botón "intercambiar bloques" de la viz 3.1. Si la suma fuera, el orden no importaría. |
| **"ReLU debe tener algo profundo adentro"** | Buscan complejidad donde no hay. Preguntan "¿pero por qué justo esa?". | Respuesta honesta: "porque es la más barata de calcular y anda. Se probaron otras más elegantes y andan parecido. Gran parte del deep learning es así, y está bien saberlo." La honestidad acá genera confianza. |
| **La analogía del cerebro** | Alguien pregunta si las neuronas artificiales imitan neuronas reales. | "El nombre es de 1943 y es marketing histórico. Una neurona artificial es una rampa. Una neurona real es una célula viva de una complejidad brutal. La analogía te va a hacer sobreestimar el modelo." Slide 31. |
| **"Entonces con suficientes rampas puedo predecir cualquier cosa"** | Confunden aproximación con predicción. | El teorema dice que la función **existe**, no que la vayas a encontrar, ni que generalice, ni que tengas datos suficientes. Se dice hoy (slide 25) y se demuestra en la clase 4. Es la confusión más peligrosa de la clase. |
| **Perderse en el `for` del notebook** | El acumulador `total += rampa(...)` no se entiende. | Se ejecuta a mano en el pizarrón con 3 iteraciones y valores concretos, escribiendo el estado de `total` en cada paso. |
| **"¿Cuántas capas hay que poner?"** | Buscan una regla. | "No hay regla. Se prueba. En serio: se prueba, se mide en validación, y se elige. La clase 4 es sobre cómo se prueba sin engañarse." |

---

## 6. Analogías y metáforas de ciencias sociales

- **La cadena de mediaciones.** Encuesta cruda → recodificación de categorías → construcción del
  índice → estandarización → tipología. Cinco funciones compuestas. Y como en la red: si una etapa
  distorsiona, todo lo de abajo hereda la distorsión.
- **La burocracia como composición.** Un trámite pasa por ventanilla, mesa de entradas, dictamen,
  resolución. Cada oficina transforma el expediente y se lo pasa a la siguiente. Y —el chiste que
  sirve— **la no linealidad es la ventanilla que dice "si no cumple el requisito, cero"**: sin
  alguna ventanilla que corte, todo el circuito sería una sola operación trivial.
- **El teorema de aproximación universal como el problema de la sobreajustabilidad teórica.** Toda
  ciencia social conoce esto: una teoría que puede explicar cualquier resultado no explica nada
  (Popper). Una función que puede dibujar cualquier curva no dice nada sobre el mundo **hasta que
  la restringimos con datos**. Esta analogía es potentísima con esta audiencia y hay que usarla
  explícitamente en la slide 25 y retomarla en la clase 4.
- **Ancho vs profundo.** Un equipo de 100 codificadores que leen todos lo mismo (ancho) vs una
  cadena de 5 analistas donde cada uno trabaja sobre la síntesis del anterior (profundo). El segundo
  construye abstracciones; el primero, cobertura.
- **El ecualizador, ahora con 25 perillas** (8 rampas × 3, más el sesgo final). Callback a la clase 1: nadie ecualiza 25 bandas a mano,
  por eso existen los presets. El descenso por gradiente es la máquina que fabrica presets.

---

## 7. Cuestionario: temas a evaluar (11 ítems)

1. **[MC conceptual]** ¿Qué significa componer dos funciones?
2. **[MC conceptual]** ¿Por qué apilar capas lineales sin activación no aporta nada?
3. **[Qué pasa si]** Dadas `f(x)=2x` y `g(x)=x+3`, calculá `f(g(1))` y `g(f(1))`. ¿Por qué difieren?
4. **[Qué pasa si]** Tenés una red con 5 rampas y la curva objetivo tiene 9 quiebres claros. ¿Qué
   esperás que pase? ¿Y si tenés 500 rampas y 12 puntos de datos?
5. **[Leer un gráfico]** Se muestran cuatro curvas dibujadas con rampas y se pide decir cuántas
   rampas tiene cada una (contar codos).
6. **[Leer un gráfico]** Se muestra un diagrama de red (2 entradas, 3 ocultas, 1 salida) y se pide
   contar **cuántos parámetros** tiene en total, contando los sesgos. *(Respuesta: 2·3 + 3 + 3·1 + 1 = 13.)*
7. **[MC]** ¿Qué es una función de activación y qué pasaría si la sacamos?
8. **[Vocabulario]** Aparear: peso / sesgo / neurona / capa oculta / activación con sus cinco
   definiciones en castellano llano.
9. **[Interpretación de teorema]** El teorema de aproximación universal dice que con suficientes
   neuronas se puede aproximar cualquier función continua. ¿Cuál de estas conclusiones **no** se
   sigue? (opciones que incluyan "entonces siempre va a predecir bien datos nuevos" — la incorrecta).
10. **[Código]** Se da la función `red_a_mano` con un bug (el acumulador se reinicia adentro del
    `for`) y se pide encontrarlo y decir qué curva saldría.
11. **[Criterio / ética aplicada]** Un colega te dice: "usé una red neuronal con 2 millones de
    parámetros para modelar la trayectoria de 80 municipios; ajusta perfecto". Escribí las **dos**
    preguntas que le harías y explicá por qué. *(Se busca: relación parámetros/datos; qué pasó con
    datos que el modelo no vio; y por qué "ajusta perfecto" es una señal de alarma, no de éxito.)*

---

## 8. Referencias

**Para el estudiante:**
- 3Blue1Brown, *But what is a neural network?* — **ahora sí**: mirarlo después de esta clase.
  Se le avisa que él usa sigmoides donde nosotros usamos rampas; es lo mismo con otro doblez.
  `[VERIFICAR URL]`
- Nielsen, Michael, *Neural Networks and Deep Learning*, capítulo 4: *A visual proof that neural
  nets can compute any function*. **Es exactamente la clase de hoy, con visualizaciones.** Libro
  gratuito online. `[VERIFICAR URL]`
- TensorFlow Playground — juguete en el navegador para poner capas y ver la figura que dibuja.
  Advertencia para el docente: usa un problema 2D de clasificación, así que hay que introducirlo
  con cuidado para que no confunda. `[VERIFICAR URL]`

**Para el docente:**
- Cybenko, G. (1989), *Approximation by superpositions of a sigmoidal function*. Sólo la referencia,
  no se asigna. `[VERIFICAR]`
- Hornik, K. (1991), *Approximation capabilities of multilayer feedforward networks*. `[VERIFICAR]`
- Sobre el nombre "neurona": McCulloch & Pitts (1943). Útil para contar la anécdota histórica en la
  slide 31 con precisión. `[VERIFICAR]`
