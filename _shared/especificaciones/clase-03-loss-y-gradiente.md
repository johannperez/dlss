# Clase 3 — Estar equivocado es un número, y ese número tiene pendiente
**Directorio:** `clases/03-loss-y-gradiente/`
**Duración:** 120 min · **Prerrequisitos:** clases 1 y 2

---

## 1. Narrativa de la clase

Hoy se cierra el mecanismo. La clase 2 dejó una máquina capaz de dibujar cualquier cosa y un
problema práctico insoportable: las perillas hay que ponerlas a mano. Hoy la máquina las busca sola.

Hay una trampa pedagógica a evitar: **el gradiente no es el tema de la clase**. El tema es la
*loss*, y el gradiente es el instrumento. Si se invierte el orden de importancia, la clase se
vuelve una clase de cálculo y se pierde a la audiencia. La loss, en cambio, es un tema profundamente
sociológico: **es donde se escribe qué error te importa**, y esa es una decisión metodológica y
política que ellos ya saben discutir.

El hilo:

1. **Dos rectas, ¿cuál es mejor?** El aula se divide. Y se divide **con razón**: sin un criterio
   explícito, la pregunta no tiene respuesta. Que la máquina elija sola exige escribir el criterio.
2. **El desajuste tiene nombre.** Lo que en la clase 1 fue un número gris ahora se llama *loss* y
   se muestran dos formas de escribirlo: error cuadrático (MSE) y error absoluto (MAE).
3. **La loss es una decisión, no un default.** Se arrastra un outlier y se ve cómo el MSE persigue
   al caso extremo y el MAE lo ignora. Traducción sustantiva inmediata: si tu caso extremo es un
   error de codificación, querés MAE; si es *el* caso que te interesa explicar, querés MSE. Nadie
   puede decidir eso por vos, ni el paquete estadístico. **Este es el bloque más importante de la
   clase para esta audiencia.**
4. **El paisaje.** Salto conceptual clave: cada punto del plano de parámetros es *una recta posible*,
   y su altura es qué tan mal está. El problema "encontrar la mejor recta" se convierte en el
   problema "encontrar el fondo del valle". Hay que hacer este salto **despacio y con la viz
   sincronizada**, porque es el más difícil de la clase.
5. **La búsqueda por fuerza bruta y su muerte.** Probamos una grilla. Anda. Después se cuenta:
   con 2 parámetros y 100 valores cada uno son 10.000 pruebas; con 8 parámetros son 10^16; con un
   modelo real, más pruebas que átomos. La fuerza bruta muere en pantalla y hace falta otra cosa.
6. **La brújula.** El gradiente, contado como *pendiente bajo el pie en la niebla*. Sin límites, sin
   epsilon, sin notación de derivada parcial en la primera pasada: es "si me muevo un poquito para
   allá, ¿sube o baja?". Se calcula numéricamente en el notebook, que es honesto y suficiente.
7. **Soltar la pelota.** Descenso por gradiente en vivo, con rastro. Y el learning rate como la
   longitud del paso: chiquito (llegás para la próxima década), justo, gigante (te caés del mapa).
8. **La honestidad del final.** Los valles reales no son este valle lindo: tienen mesetas, valles
   laterales y ruido. Y aun así funciona. Nadie sabe del todo bien por qué. Decirlo genera confianza
   y vacuna contra la mistificación.

`[CALLBACK DIBUJO]` — "hasta ahora nosotros movíamos la mano para dibujar. Hoy le enseñamos a la
máquina a mover la mano sola. La figura la sigue eligiendo el que arma el modelo; el pulso lo pone
el gradiente."

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-4 | «Roja o azul»: se vota antes de saber la respuesta. |
| 10-25 | Exposición: la loss | 5-9 | MSE vs MAE. La elección de la loss como decisión metodológica y política. |
| 25-40 | Manos 1a: arrastrá el outlier | 10 | Bloque corto: se arrastra el caso influyente y se mira qué recta se mueve. |
| 40-60 | El paisaje y la niebla | 11-19 | El mapa de la loss, por qué la fuerza bruta muere, la pendiente sin cálculo. |
| 60-70 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 19. |
| 70-90 | El gradiente y el learning rate | 20-23 | Soltá la pelota. Los dos síntomas de una lr mal elegida. |
| 90-110 | Manos 1b / 2 | 24 | De a dos: romper el learning rate a propósito y explicar el síntoma. |
| 110-120 | Cierre | 25-34 | Mini-batch, optimizadores, `[EN TU INVESTIGACIÓN]`, el puente a la clase 4. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (34 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Loss y gradiente | portada | Una superficie de contorno con una pelotita. | |
| 2 | Dónde quedamos | texto | 24 sliders puestos a mano. La imagen de la clase 2. | "Esto es insostenible y ustedes lo saben." |
| 3 | **Roja o azul** | figura | Nube de puntos, dos rectas distintas. Sin más datos. | "¿Cuál es mejor? Voten. Levanten la mano." Se divide el aula. |
| 4 | Están todos en lo cierto | texto | La pregunta está mal formulada: *mejor según qué*. | "No hay 'mejor' hasta que alguien escribe qué le importa. Y ese alguien sos vos, no el software." |
| 5 | El número gris de la clase 1 | figura | La imagen de los segmentos rojos, otra vez. Ahora rotulada: **loss / función de pérdida / función de costo**. | "Tres nombres para la misma cosa, porque este campo no se pone de acuerdo en nada." |
| 6 | Dos maneras de sumar errores | figura | Lado a lado: MSE (cuadrado) y MAE (valor absoluto). Con las dos fórmulas chiquitas abajo y **los dos gráficos de la penalización en grande**: la parábola y la V. | "Miren las formas: el cuadrado castiga muchísimo los errores grandes. El absoluto los trata a todos igual de mal." |
| 7 | **Arrastrá el outlier** | VIZ | `viz/comparador-de-losses.html`. | Arrastra un punto lejos. La recta del MSE lo persigue; la del MAE ni se inmuta. |
| 8 | Esto es una decisión metodológica | texto | Tres escenarios: (a) el outlier es un error de tipeo; (b) el outlier es el caso desviado que motivó tu investigación; (c) no sabés. Qué loss corresponde a cada uno. | "El paquete estadístico tiene un default. El default es una posición teórica que alguien tomó por vos." |
| 9 | Y a veces es una decisión política | texto | Un modelo que asigna un recurso: ¿te duele más dejar afuera a quien lo necesita (falso negativo) o dárselo a quien no (falso positivo)? La loss es donde eso se escribe. | "Guarden esto. En la clase 9 lo vamos a ver con números y en la 10 con consecuencias." |
| 10 | Bloque práctico 1a | texto | Consignas: calcular la loss a mano. | "20 minutos." |
| 11 | Ahora: ¿cómo la minimizamos? | texto | Reformulación del problema: buscar los parámetros que hacen la loss más chica. | |
| 12 | **El salto conceptual** | figura | Tres paneles: (1) una recta sobre datos; (2) una flecha; (3) **un punto** en un plano `(a,b)`. Con la leyenda: "cada recta posible es un punto en este mapa". | Lo dice tres veces con distintas palabras. "Un punto acá **es** una recta allá." |
| 13 | El mapa completo | figura | El plano `(a,b)` pintado con colores según la loss: contornos tipo mapa topográfico. | "Es un mapa de altura, como los de senderismo. Lo oscuro es hondo. Queremos el fondo." |
| 14 | **Movete por el mapa** | VIZ | `viz/valle-de-loss.html`, modo "arrastrar". | Arrastra el punto y muestra cómo cambia la recta al lado, en vivo. "Miren los dos paneles a la vez." |
| 15 | Apuesta | discusión | "Si me muevo en esta dirección, ¿la loss sube o baja?" con una flecha dibujada en el mapa. | Votan antes de mover. |
| 16 | Fuerza bruta | figura | La grilla de 100x100 puntos evaluados, con el mínimo marcado. | "Probamos 10.000 rectas y nos quedamos con la mejor. Funciona." |
| 17 | Fuerza bruta, muerta | texto | Tabla: 2 params → 10⁴ pruebas; 4 → 10⁸; 8 → 10¹⁶; un modelo chico como el de la clase 8 (~1,5M params) → un número absurdo con nota "más que átomos en el universo observable". | "Se acabó la fuerza bruta en la línea 3 de esta tabla." |
| 18 | La niebla | figura | Ilustración: alguien en una colina, con niebla, que no ve nada más allá de sus pies. | "No podés ver el valle entero. Pero sí podés sentir con el pie para qué lado baja. Eso alcanza." |
| 19 | La pendiente, sin cálculo | VIZ | `viz/loss-1d.html`. | "Me muevo un poquito a la derecha: ¿subió o bajó? Esa comparación **es** la derivada. No hay más." |
| 20 | El gradiente | figura | El mapa con una flecha en un punto. Definición en castellano: "la dirección en la que la loss sube más rápido". Y abajo, en grande: **"por eso vamos para el lado contrario"**. | "Todo el nombre pomposo es: para dónde sube. Y nosotros vamos al revés." |
| 21 | **Soltá la pelota** | VIZ | `viz/valle-de-loss.html`, botón "soltar" con rastro. | La suelta desde tres lugares distintos. "Miren el rastro: primero pasos largos, después cortitos. ¿Por qué se van acortando?" (Porque la pendiente se aplana.) |
| 22 | El paso: learning rate | VIZ | `viz/tasa-de-aprendizaje.html`, tres pelotas en paralelo. | "Izquierda: paso microscópico, no llega nunca. Centro: bien. Derecha: se va del mapa." |
| 23 | Los dos síntomas | figura | Dos curvas de loss vs iteración: una que baja lentísimo y casi plana; otra que oscila y explota a NaN. | "Cuando entrenen y vean una de estas dos formas, ya saben qué perilla tocar. Esto lo van a usar en la clase 4 y en la 8." |
| 24 | Bloque práctico 1b / 2 | texto | Consignas del descenso a mano. | |
| 25 | Volvimos: ¿quién lo rompió? | discusión | Se piden las curvas de loss rotas con lr grande. | Se proyecta una del aula. |
| 26 | Batch, mini-batch, estocástico | figura | Tres rastros sobre el mismo mapa: uno suave (todos los datos), uno tembloroso (mini-batches), uno muy tembloroso (de a un dato). Todos llegan más o menos al mismo lugar. | "El temblor no es un defecto: es más barato y encima ayuda a escaparse de pozos malos. De ahí sale la palabra *estocástico*." |
| 27 | Lo que hace la computadora de verdad | texto | Se nombra **backpropagation** en una sola slide: es la regla de la cadena aplicada con inteligencia para calcular todas las derivadas de una pasada. **No se deriva.** | "Es el truco que hace que esto sea factible. Es importante que exista y no es importante que lo sepas hacer a mano. PyTorch lo hace y en la clase 4 vas a ver que son dos palabras: `loss.backward()`." |
| 28 | La honestidad | texto | Los paisajes reales tienen mesetas, valles laterales, sillas de montar. El descenso no garantiza el mínimo global. Y funciona igual. | "Nadie tiene una teoría completa de por qué esto anda tan bien. Es un campo con más ingeniería que teoría, y eso hay que saberlo cuando leés un paper que suena muy seguro de sí mismo." |
| 29 | Optimizadores | texto | Adam, SGD con momento, en una línea cada uno: variantes de cómo dar el paso (con inercia, con paso adaptativo). | "Van a ver `Adam` en todos lados. Es 'la pelota con inercia y con paso que se autorregula'. Con eso alcanza." |
| 30 | `[EN TU INVESTIGACIÓN]` | texto | Cuando leas "el modelo fue optimizado", preguntá: ¿optimizado para minimizar **qué**? Y si la respuesta es "el default", ahí hay una decisión escondida que alguien no discutió. | "Esta es una pregunta de revisor que casi nadie hace y que casi siempre encuentra algo." |
| 31 | La escalera de la clase | figura | Resumen visual: función → loss → paisaje → gradiente → paso → repetir. | |
| 32 | Ya tenemos todo | texto | Clase 1: la máquina. Clase 2: la máquina flexible. Clase 3: cómo se ajusta sola. | "Falta una sola cosa: hacerlo bien, sin engañarnos." |
| 33 | El puente | texto | "Clase 4: entrenamos de verdad con PyTorch. Y descubrimos que un modelo puede sacarse un 99% y ser un desastre." | |
| 34 | Glosario de hoy | texto | loss, MSE, MAE, optimización, gradiente, descenso por gradiente, learning rate, batch, SGD, backpropagation, Adam, mínimo local. | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/comparador-de-losses.html`
- **Qué se ve.** Una nube de 15 puntos. Dos rectas superpuestas: la que minimiza **MSE** (azul) y la
  que minimiza **MAE** (naranja), ambas recalculadas en vivo. Panel lateral con los dos valores de
  loss y, debajo, los dos gráficos de penalización (parábola vs V) con el error de cada punto
  marcado sobre ellos.
- **Controles.** **Podés arrastrar cualquier punto con el mouse.** Botón "agregar un caso extremo"
  que planta un outlier bien lejos. Botón "reset".
- **Qué tiene que hacer clic.** Que la elección de loss cambia **la conclusión sustantiva**, no la
  precisión decimal: con el outlier arrastrado, la recta azul cambia de pendiente y la naranja no.
  Dos investigadores con los mismos datos publican tendencias distintas por una decisión que ninguno
  de los dos discutió.
- **Momento aha.** "Moví **un** punto y la recta azul giró. La naranja ni se enteró. La diferencia
  no es técnica: es qué caso decidís que importa."
- **Detalle.** Un cartel de texto que cambia en vivo: "el MSE está mirando principalmente al caso
  #7" (el de mayor error), con ese punto resaltado. Hace visible **a quién le hace caso el modelo**.

### 3.2 `viz/valle-de-loss.html` — **la viz central de la clase**
- **Qué se ve.** Dos paneles sincronizados, lado a lado.
  - **Izquierda: el mapa.** Plano `(a, b)` con la loss dibujada como **contornos rellenos** (mapa
    topográfico, escala de color secuencial oscura=baja). Un punto rojo arrastrable. Una **flecha
    negra** que sale del punto mostrando −gradiente, con largo proporcional a la magnitud.
  - **Derecha: el mundo real.** La nube de datos con la recta correspondiente al punto actual, y los
    segmentos de error dibujados. Arriba, el valor de la loss en grande.
- **Controles.**
  - Arrastrar el punto rojo con el mouse (los dos paneles se actualizan en tiempo real).
  - Botón **"un paso"**: avanza una iteración de descenso y deja marca.
  - Botón **"soltar la pelota"**: anima el descenso completo dejando **rastro con puntitos**,
    ~40 iteraciones, con velocidad de animación visible (no instantáneo: la animación *es* el
    contenido).
  - Slider de **learning rate** (escala logarítmica, 0.0001 a 2.0).
  - Botón "reiniciar desde un lugar al azar".
  - Toggle "mostrar la flecha del gradiente".
  - Toggle **"mostrar la curva de loss"**: agrega abajo un tercer panel con loss vs iteración,
    que es exactamente el gráfico que van a ver en todos los entrenamientos del resto del curso.
- **Qué tiene que hacer clic.** Tres cosas, en orden: (1) un punto acá es una recta allá; (2) la
  flecha siempre apunta para arriba en el mapa y por eso vamos al revés; (3) los pasos se van
  acortando solos cuando el terreno se aplana.
- **Momento aha.** Al soltar la pelota con lr adecuado: "va sola al fondo, y frena sola". Al subir
  el lr a 1.5: "se fue a la mierda" (sí, alguien lo va a decir en voz alta, y está bien).
- **Detalle crítico de implementación.** El panel derecho **tiene que actualizarse mientras se
  arrastra**, no al soltar. La sincronización en vivo es toda la viz. Precalcular la grilla de loss
  una vez (200x200) y dibujarla como imagen de fondo; sólo redibujar punto, flecha y rastro.

### 3.3 `viz/loss-1d.html`
- **Qué se ve.** Una parábola (loss en función de **un solo** parámetro). Un punto sobre ella. Una
  recta tangente dibujada en el punto. Debajo, dos números grandes: "si me muevo +0.1, la loss
  cambia en ___" y "si me muevo −0.1, la loss cambia en ___".
- **Controles.** Slider de posición del parámetro. Slider del **tamaño del pasito de prueba**
  (de 1.0 a 0.001): al achicarlo, la recta secante que se dibuja se va pegando a la tangente.
  Botón "dar un paso cuesta abajo".
- **Qué tiene que hacer clic.** Que la derivada no es una entidad mística: es "probé moverme un
  poquito y comparé". Y que la tangente es el límite de esa comparación cuando el pasito se achica.
- **Momento aha.** "Ah, la derivada es literalmente 'cuánto cambia si me muevo un toque'. Eso lo
  puedo calcular con una resta."
- **Nota pedagógica.** Esta viz existe para que **nadie tenga que haber estudiado cálculo**. Se hace
  antes de la flecha en 2D. Si el aula viene lenta, esta viz es más importante que la 3.2 y se le
  da más tiempo.

### 3.4 `viz/tasa-de-aprendizaje.html`
- **Qué se ve.** Tres copias del mismo mapa de contornos, en fila, rotuladas "paso chiquito",
  "paso justo", "paso enorme". Tres pelotas soltadas **desde el mismo punto** simultáneamente,
  con sus rastros. Debajo de cada una, su curva de loss vs iteración.
- **Controles.** Botón único "soltar las tres". Sliders individuales para los tres learning rates
  (con valores por defecto que producen los tres comportamientos canónicos). Slider de "cantidad de
  pasos".
- **Qué tiene que hacer clic.** Que los tres fracasos/éxitos tienen **firmas visuales distintas en
  la curva de loss**, y que esa firma es diagnosticable sin ver el mapa (que es lo único que vas a
  tener cuando entrenes de verdad).
- **Momento aha.** "La curva de la derecha se va para arriba. Entonces cuando en la clase 4 vea una
  curva que sube, ya sé que tengo que bajar el learning rate."
- **Detalle.** Un panel "¿qué firma es esta?" con tres curvas de loss sin etiquetar y un quiz de
  aparear. Convierte la viz en evaluación formativa.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** < 2 minutos, CPU.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Recap + objetivo del día. | |
| 2 | code | Imports + carga de datos (mismos de la clase 1: menciones a *seguridad* por año). | Continuidad deliberada. |
| 3 | md | **La loss, en código.** | |
| 4 | code | `def mse(y_real, y_pred): return np.mean((y_real - y_pred)**2)` y `def mae(...)`. Se calculan las dos para una recta cualquiera. | Dos líneas. |
| 5 | code | Se agrega un outlier a los datos y se recalculan las dos. Se imprime la comparación. | |
| 6 | md | `TODO 1` — ¿Cuál de las dos loss subió proporcionalmente más al agregar el outlier? Escribí en un comentario por qué, y cuál elegirías si ese caso extremo fuera un error de carga. *Pista: mirá qué le hace el cuadrado a un error de 20.* | |
| 7 | md | **El paisaje.** | |
| 8 | code | Doble `for` sobre una grilla de `a` y `b`, calculando la loss en cada punto. Guardado en una matriz. | Se corre en 2 segundos y es tangible. |
| 9 | code | `plt.contourf` del paisaje + marca del mínimo encontrado con `np.argmin`. | Su propio mapa topográfico. |
| 10 | md | `TODO 2` — Cambiá el rango de la grilla para hacer zoom cerca del mínimo. ¿Qué forma tiene el valle de cerca? *Pista: achicá los límites de `np.linspace`.* | Descubren que es un valle alargado y torcido: prepara la intuición de por qué el descenso zigzaguea. |
| 11 | md | **La fuerza bruta no escala.** | |
| 12 | code | Celda que calcula e imprime cuántas evaluaciones harían falta para 2, 4, 8, 100 y 3.000.000 de parámetros con 100 valores cada uno. Formateado en notación científica, con un comentario comparando con la edad del universo en segundos. | Un chiste que es un argumento. |
| 13 | md | **La pendiente, con una resta.** | |
| 14 | code | `def derivada_numerica(f, x, h=1e-4): return (f(x+h) - f(x-h)) / (2*h)`. Se prueba con una función conocida. | Una línea. Nada de cálculo simbólico. |
| 15 | code | `def gradiente(a, b)` que devuelve las dos derivadas parciales numéricas. Se imprime el gradiente en un punto y se compara con la flecha que vieron en la viz. | |
| 16 | md | **El descenso, en 10 líneas.** | |
| 17 | code | El loop: inicializar `a, b`; `for i in range(200)`: calcular gradiente, restar `lr * grad`, guardar la loss en una lista. Imprime cada 20 iteraciones. | **La celda más importante del curso hasta acá.** Comentada línea por línea. |
| 18 | code | Gráfico de la curva de loss + gráfico del rastro sobre el contorno + la recta final sobre los datos. | Los tres gráficos que van a ver el resto de sus vidas. |
| 19 | md | `TODO 3` — Poné `lr = 1.5` y corré. Pegá el gráfico y explicá en una oración qué pasó. *Pista: mirá los valores de `a` en las primeras 5 iteraciones.* | Van a ver `nan`. Hay que anticiparlo en el texto: "si ves `nan`, felicitaciones, lo rompiste bien." |
| 20 | md | `TODO 4` — Poné `lr = 0.000001`. ¿Llegó? ¿Cuántas iteraciones harían falta? *Pista: mirá cuánto bajó la loss en 200 pasos y hacé una regla de tres.* | |
| 21 | md | `TODO 5` — Arrancá desde `a=-5, b=50` (bien lejos). ¿Llega al mismo lugar? | Introduce la pregunta del mínimo global sin nombrarla. |
| 22 | md | **Bonus: mini-batches** (opcional). | |
| 23 | code | El mismo loop pero calculando el gradiente sobre 5 puntos al azar por iteración. Se grafican los dos rastros superpuestos. | Se ve el temblor. |
| 24 | md | **Para llevarte** + puente a PyTorch: "en la clase 4, las líneas 14 a 17 de este notebook se van a convertir en tres palabras". | Que sientan que se ganaron la abstracción. |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **Confundir el espacio de datos con el espacio de parámetros** | Miran el mapa de contornos y creen que los ejes son las variables del estudio. | **Es la confusión número uno de la clase.** Se ataca con la viz 3.2 y sus dos paneles sincronizados, y con la slide 12 repetida tres veces. Frase útil: "en este mapa no hay ningún año ni ningún porcentaje: hay **rectas**. Cada punto es una recta entera." |
| **"El gradiente apunta al mínimo"** | Creen que la flecha señala el fondo del valle. | La flecha señala la **subida más empinada acá nomás**, es local y ciega. En un valle torcido, ir en contra del gradiente te hace zigzaguear y **no** apunta al fondo. Se muestra con el zoom del TODO 2. |
| **"Entonces siempre encuentra la mejor solución"** | Confían de más. | Se sueltan tres pelotas desde puntos distintos en un paisaje con dos pozos (agregar un modo "paisaje difícil" a la viz 3.2) y terminan en lugares distintos. Slide 28. |
| **Pánico ante la palabra "derivada"** | Se desconectan al escucharla. | Estrategia: la palabra **no se dice** hasta la slide 19, después de que ya la calcularon con una resta. Se la presenta como "el nombre elegante de la resta que acabamos de hacer". |
| **"MSE es el correcto, MAE es una alternativa rara"** | Toman el default como verdad. | Viz 3.1 + los tres escenarios de la slide 8. Y el dato histórico: el MSE se popularizó en buena medida porque tiene solución cerrada y es fácil de derivar, no porque represente mejor el error que te importa. |
| **Creer que el learning rate se calcula** | Piden la fórmula del lr óptimo. | "Se prueba. Se mira la curva. Se ajusta. Es artesanía y todos la hacemos." Se les da el rango práctico (0.1 a 0.0001) y la heurística: si explota, dividí por 10. |
| **Perderse en el signo menos** | `a = a - lr*grad`: no entienden por qué menos. | Se hace en el pizarrón con un número: si el gradiente es +3 (sube hacia la derecha), tengo que ir a la izquierda, entonces resto. Una vez, con números, alcanza. |
| **Pensar que backprop es otro algoritmo distinto** | Creen que backprop reemplaza al descenso. | Se aclara: el descenso decide *hacia dónde y cuánto*; backprop es sólo la manera eficiente de **calcular** el gradiente. Son dos piezas distintas del mismo mecanismo. |

---

## 6. Analogías y metáforas de ciencias sociales

- **La loss como operacionalización del fracaso.** Toda evaluación de política pública tiene que
  definir qué cuenta como error. ¿Una política de vivienda fracasa por dejar gente afuera o por
  darle a quien no lo necesitaba? Elegir la loss es exactamente esa discusión, escrita en una línea.
- **El outlier como caso desviado.** La tradición del *case study* del caso desviado (Lipset,
  Ragin) es literalmente una decisión de darle peso al outlier. MSE es "el caso raro me importa
  mucho"; MAE es "quiero la tendencia general". El curso no toma partido: exige que se elija a
  conciencia.
- **La niebla y el conocimiento situado.** No ves el paisaje completo; ves tu entorno inmediato y
  decidís con eso. La analogía con el conocimiento situado y con la racionalidad limitada
  (Simon: *satisficing*) es directa y le gusta a esta audiencia: el descenso por gradiente es un
  agente de racionalidad limitada que igual llega a buen puerto.
- **Mínimo local = equilibrio subóptimo estable.** Path dependence, *lock-in* institucional: el
  sistema se estabiliza en una configuración que nadie elegiría de cero, y salir cuesta. Es
  literalmente un mínimo local. La analogía es exacta, no decorativa.
- **El learning rate como velocidad de reforma.** Cambios muy chicos: no pasa nada en una
  generación. Cambios enormes de golpe: el sistema se desestabiliza y termina peor. Se puede hacer
  el chiste, y funciona.
- **Batch vs estocástico como muestreo.** Calcular el gradiente con todos los datos es un censo;
  con un mini-batch es una muestra. La muestra es ruidosa pero muchísimo más barata, y con
  suficientes iteraciones llegás igual. Esta analogía es perfecta para esta audiencia y hay que
  usarla en la slide 26.

---

## 7. Cuestionario: temas a evaluar (12 ítems)

1. **[MC conceptual]** ¿Qué es una función de pérdida?
2. **[MC conceptual]** En el mapa de contornos de la loss, ¿qué representa cada punto?
   *(Distractor fuerte: "un dato".)*
3. **[Qué pasa si]** Agregás a tu base un caso con un error enorme. ¿Qué le pasa al MSE? ¿Y al MAE?
   ¿Qué recta cambia más?
4. **[Qué pasa si]** Ponés un learning rate diez veces más grande. Describí los dos resultados
   posibles.
5. **[Leer un gráfico]** Tres curvas de loss vs iteración (una que baja y se aplana, una casi plana,
   una que oscila hacia arriba). Aparear con: "learning rate bien", "learning rate muy chico",
   "learning rate muy grande".
6. **[Leer un gráfico]** Un mapa de contornos con una flecha dibujada en un punto. Marcar hacia
   dónde se va a mover el próximo paso del descenso. *(Se evalúa el signo menos.)*
7. **[MC]** ¿Por qué no se busca el mínimo probando todas las combinaciones posibles?
8. **[MC]** ¿Qué es el learning rate?
9. **[Conceptual abierta]** Explicá con tus palabras, sin fórmulas, por qué el gradiente sirve
   aunque no veas el paisaje completo.
10. **[Distinción]** ¿Cuál es la diferencia entre el descenso por gradiente y backpropagation?
    *(Uno decide el paso, el otro calcula el gradiente eficientemente.)*
11. **[Aplicación sustantiva]** Estás modelando cantidad de protestas por mes. Hay tres meses de
    conflictividad excepcional. ¿Elegís MSE o MAE? Justificá según **dos** objetivos de
    investigación distintos, uno para cada respuesta.
12. **[Criterio / ética aplicada]** Un modelo predice riesgo de deserción escolar para asignar becas.
    ¿Qué error es más costoso: dejar afuera a alguien que iba a desertar, o darle beca a alguien que
    no la necesitaba? ¿Quién debería decidir eso y en qué parte del código queda escrito?
    *(Se busca: que identifiquen que la loss/umbral es donde se escribe una decisión política, y que
    no la debería tomar quien programa en soledad. Enlaza directo con las clases 9 y 10.)*

---

## 8. Referencias

**Para el estudiante:**
- 3Blue1Brown, *Gradient descent, how neural networks learn* (capítulo 2 de la serie). Es
  exactamente esta clase. `[VERIFICAR URL]`
- Distill.pub, *Why Momentum Really Works* — visualmente hermoso; recomendarlo sólo a los muy
  entusiastas, avisando que va más allá de lo que necesitan. `[VERIFICAR URL]`

**Para el docente:**
- Goodfellow, Bengio & Courville, *Deep Learning* (MIT Press, disponible gratis online),
  capítulo 4 (optimización numérica) y 8. Para consulta, no para asignar. `[VERIFICAR URL]`
- Sobre el peso histórico del MSE y su relación con la solución cerrada de mínimos cuadrados:
  cualquier historia de la estadística (Stigler, *The History of Statistics*) sirve para la anécdota
  de la slide 8. `[VERIFICAR]`
- Simon, H. (1955), *A Behavioral Model of Rational Choice* — para quien quiera fundamentar bien la
  analogía del *satisficing* con la optimización local. `[VERIFICAR]`
