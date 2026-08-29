# Deep Learning para Cientistas Sociales
## Programa del curso — 10 clases de 2 horas

> **Para quién es esto.** Para gente que investiga sociedad: sociología, ciencia política,
> antropología, comunicación, economía. Gente que no programa (o programa poquito), que le tiene
> respeto a la matemática, y que no quiere convertirse en data scientist. Querés **una herramienta
> más en la caja** y querés usarla **con criterio**: saber cuándo sirve, cuándo te está mintiendo,
> y cómo demostrarle a un revisor que no te mintió.

> **Lo que NO es.** No es un curso para entrenar modelos de frontera. No vas a derivar
> backpropagation. No vas a competir en Kaggle. Si al final del curso sabés *cuándo no usar
> esto*, el curso fue un éxito.

---

## 0. Filosofía pedagógica

### 0.1 Las siete reglas de la casa

1. **La intuición va primero. La fórmula va después. Y a veces no va.**
   Ninguna ecuación entra a este curso sin haberse ganado el lugar. Si un concepto se puede
   transmitir con un dibujo que se mueve, se transmite con un dibujo que se mueve. La fórmula
   aparece después, como *resumen taquigráfico* de algo que ya entendiste, nunca como definición.

2. **Nada de matemática sin una imagen al lado.**
   Regla operativa para quien construye las clases: si escribís una fórmula en una slide y no
   tenés al lado (misma slide o la siguiente) una figura, una animación o un slider que muestre
   qué hace esa fórmula, **borrá la fórmula**. No la muevas de lugar: borrala. Si el concepto es
   imprescindible y no tiene visualización posible, es señal de que el concepto está mal contado,
   no de que la audiencia sea limitada.

3. **La metáfora conductora: aprender es aprender a dibujar.**
   Una red neuronal es una **máquina de dibujar figuras** que tiene un montón de perillas.
   Entrenarla es girar las perillas hasta que la figura que dibuja se parezca a los datos.
   Todo el curso es esa misma frase, repetida a escalas cada vez más grandes:
   - Clase 1: dibujamos una figura simple con dos perillas.
   - Clase 2: **componemos** funciones y dibujamos figuras imposibles con una sola máquina.
   - Clase 3: la máquina **encuentra sola** las perillas, bajando por un valle.
   - Clase 4: la máquina se entrena de verdad, y aprendemos a distinguir *dibujar* de *calcar*.
   - Clase 5: la CNN dibuja **sobre** una imagen (los filtros son pinceles).
   - Clase 6: el texto se convierte en un lugar del espacio para poder dibujarlo.
   - Clase 7-8: el transformer dibuja **una distribución de probabilidad de próxima palabra**.
   - Clase 9-10: usamos figuras que dibujó otro y aprendemos a auditarlas.

   Esa frase —"esto es dibujar figuras"— tiene que aparecer **explícitamente, con callback a la
   clase anterior**, en cada una de las 10 clases. Está marcado en cada especificación como
   `[CALLBACK DIBUJO]`.

4. **Todo concepto abstracto necesita un objeto concreto que se pueda manosear.**
   El estándar de una visualización no es "muestra el concepto": es "hay algo que el estudiante
   mueve con el dedo, y cuando lo mueve pasa algo que le cambia una creencia". Cada viz de este
   curso tiene declarado su **momento aha**: la frase exacta que queremos que el estudiante piense.
   Si no podés escribir esa frase, la viz no está diseñada todavía.

5. **El dominio no es decorado, es el hilo.**
   Todo ejemplo del curso vive en **discurso político** (discursos presidenciales, debates
   parlamentarios) o **prensa y noticias**. No hay ejemplos de precios de casas en Boston ni de
   flores iris. Cuando necesitamos un sandbox técnico neutro (dígitos manuscritos, por ejemplo),
   se usa explícitamente rotulado como sandbox y se vuelve al dominio antes de terminar el bloque.

6. **El lunes.**
   Cada clase tiene un bloque marcado `[EL LUNES]`: un momento explícito donde el docente muestra
   cómo lo de hoy se usa **el lunes que viene en la investigación de ellos**. No es una promesa
   futura ("cuando terminemos el curso vas a poder..."): es una cosa concreta y chiquita que ya
   pueden hacer con lo que vieron hoy. En la clase 1 es "graficá tu variable y ajustale una recta
   con una perilla que vos entendés". En la clase 8 es "ahora sabés por qué tu prompt largo se
   olvidó de la primera instrucción".

7. **El error es contenido, no accidente.**
   Cada especificación trae una sección de **confusiones típicas** con el guion de cómo desarmarlas.
   Varias visualizaciones están diseñadas para que el estudiante *se equivoque primero*: se le
   pregunta qué va a pasar, apuesta, y después mueve el slider. La predicción fallida es el
   momento de aprendizaje; sin la apuesta previa, mover el slider es un dibujito lindo.

### 0.2 Cómo está armada cada clase (estructura de 120 minutos)

Ninguna exposición dura más de 20 minutos seguidos. El ritmo base es:

| Bloque | Duración | Qué pasa |
|---|---|---|
| **Gancho** | 10 min | Una pregunta o una imagen que descoloca. Se vota, se discute, no se resuelve. |
| **Idea 1** | 20 min | Exposición corta + visualización manipulada por el docente en vivo. |
| **Manos 1** | 20 min | Notebook. Corren celdas, cambian números, resuelven un TODO. |
| **Pausa** | 10 min | En serio, pausa. |
| **Idea 2** | 20 min | La vuelta de tuerca de la clase. |
| **Manos 2** | 25 min | El ejercicio grande, de a dos. |
| **Cierre** | 15 min | `[EL LUNES]` + puente a la clase siguiente + la pregunta abierta. |

El plan minuto a minuto de cada clase respeta esta forma, con variaciones declaradas.

### 0.3 Convenciones de producción (para el equipo que construye)

- **Todo offline.** Cero CDNs. `reveal.js` y KaTeX están vendoreados en `_shared/vendor/` y se
  referencian por ruta relativa. Las slides y las viz tienen que abrir con `file://` y funcionar.
- **Las viz son HTML standalone**, un archivo, sin dependencias externas, canvas o SVG a mano.
  Tienen que poder abrirse solas (el docente las proyecta) y también embeberse en un `<iframe>`
  dentro de la slide.
- **Los notebooks abren en Colab**, instalan lo suyo en la primera celda, y corren enteros en CPU
  en menos de 10 minutos (la GPU es opcional y sólo acelera la clase 8).
- **Español rioplatense neutro-informal.** Voseo suave, humor, cero solemnidad. Términos técnicos
  en inglés se dejan en inglés (*loss*, *gradient descent*, *embedding*, *attention*, *overfitting*)
  pero **siempre** con su explicación en castellano la primera vez que aparecen, y con una entrada
  en `recursos/glosario.md`.
- **Los datos.** Ver sección 3 de este documento: usamos un corpus sintético declarado
  (**Aguasclaras**) más corpus reales de dominio público. Nunca ponemos frases inventadas en boca
  de personas reales.

---

## 1. Tabla resumen de las 10 clases

| # | Título | Intuición central (la única idea) | Metáfora del dibujo | Herramienta nueva | `[EL LUNES]` |
|---|---|---|---|---|---|
| 1 | **Una función es una máquina con perillas** | Una función tiene *entradas* que recorren la figura y *parámetros* que deforman la figura. Aprender = mover parámetros. | Dibujamos una figura simple con 2 perillas | Python, numpy, gráficos | Graficar tu serie y ajustarle una curva entendiendo qué hace cada perilla |
| 2 | **Componer funciones: dibujar lo imposible** | Apilando funciones simples con un doblez en el medio se dibuja *cualquier* figura. Eso, y no otra cosa, es una red neuronal. | Componemos funciones para dibujar figuras imposibles con una sola máquina | Composición, ReLU, la primera red a mano | Entender qué promete y qué no promete un modelo "flexible" |
| 3 | **Estar equivocado es un número, y el número tiene pendiente** | Si podés medir cuán mal dibujás, podés bajar por esa medida hasta el fondo del valle. Eso es todo el aprendizaje automático. | La máquina busca sola las perillas | Loss, gradiente, descenso | Elegir función de pérdida como decisión metodológica (y política) |
| 4 | **El ciclo de entrenamiento, y la diferencia entre dibujar y calcar** | Un modelo con demasiada libertad memoriza tu muestra en vez de aprender el patrón. Por eso existe el conjunto de validación. | Aprendemos a distinguir dibujar de calcar | PyTorch, training loop, train/val/test | Partir bien tus datos y no engañarte solo |
| 5 | **La forma de los datos manda: imágenes** | La arquitectura es un conjunto de supuestos sobre cómo es el mundo. Una CNN supone que lo que importa es local y se repite. | La CNN dibuja *sobre* la imagen: los filtros son pinceles | Convoluciones, CNN | Leer con criterio un paper que clasifica imágenes (satelitales, archivos, prensa) |
| 6 | **La forma de los datos manda: texto** | El orden es información, y para que una máquina lea hay que darle a cada palabra un lugar en el espacio. | Dibujamos el mapa donde viven las palabras | Tokenización, one-hot, embeddings | Medir similitud semántica entre documentos de tu corpus |
| 7 | **Attention: cada palabra arma su propio resumen del contexto** | En vez de leer en orden y olvidarse, cada palabra mira a todas las demás y decide a cuál prestarle atención. | Cada palabra dibuja su propio mapa de a quién mira | Self-attention, Q/K/V, máscara causal | Leer el mapa de atención de un modelo y no sobreinterpretarlo |
| 8 | **Un mini-GPT y la traducción a ChatGPT** | Un LLM es una máquina de dibujar la distribución de la próxima palabra. Todo lo raro que hace ChatGPT se explica desde ahí. | El transformer dibuja la distribución de próxima palabra | Mini-GPT completo entrenado desde cero | Prompting, temperatura, ventana de contexto, alucinación: entender por qué |
| 9 | **Usar modelos que ya existen sin creerles** | Un modelo pre-entrenado es un informante clave: sabe muchísimo y tiene sus sesgos. Se lo usa y se lo valida. | Usamos figuras que dibujó otro | Hugging Face, embeddings, zero-shot, fine-tuning | Clasificar tu corpus y reportar métricas que un revisor acepte |
| 10 | **Criterio: validez, sesgo, reproducibilidad y el revisor 2** | El modelo mide *algo*. Tu trabajo es demostrar que ese algo es lo que decís que es. | Auditamos el dibujo | Auditoría de sesgo, validación humana, ficha de modelo | Escribir la sección de métodos de tu paper |

---

## 2. Las diez clases en detalle

### Clase 1 — Una función es una máquina con perillas
`clases/01-funciones-y-parametros/` · Espec: `_shared/especificaciones/clase-01-funciones-y-parametros.md`

**Gancho (10 min).**
En pantalla, una nube de puntos sin ejes rotulados: 40 puntos que suben y bajan. Pregunta:
"¿Qué le pasó a este país?". Se discute 3 minutos. Después se revelan los ejes: es el porcentaje
de palabras del discurso presidencial de apertura de sesiones dedicadas al tema *seguridad*, año a
año. Segunda pregunta, la que importa: **"si yo quisiera resumir esto con una línea, ¿qué línea
dibujarías?"**. Alguien dice "una recta que sube". Perfecto: para dibujar esa recta hacen falta
exactamente dos números. Ese es el curso entero.

**Objetivos de aprendizaje. Al final de la clase vas a poder:**
- Explicar con tus palabras la diferencia entre una **variable** (lo que entra) y un **parámetro**
  (la perilla), y decir cuál de las dos mueve la figura y cuál te mueve *por* la figura.
- Mirar una fórmula chiquita y anticipar qué forma va a tener el dibujo, sin calcular nada.
- Leer y modificar código de Python que define una función y la grafica.
- Ajustar "a ojo" una curva a unos datos y darte cuenta de que estabas haciendo, a mano y mal, lo
  que después va a hacer una computadora.

**Intuición central.**
Una función es una máquina: le metés algo, sale algo. Y tiene perillas al costado. Cambiar lo que
metés te mueve **a lo largo** de la figura. Cambiar las perillas **deforma** la figura. Un modelo
es la figura; entrenar es girar las perillas.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | La nube de puntos misteriosa. Se vota qué línea la resume. |
| 10-25 | Exposición: máquina con perillas | Función como caja. `f(x) = a·x + b`. El docente mueve `a` y `b` en vivo en `viz/maquina-de-perillas.html`. Se nombra el "medidor de desajuste" pero todavía no se lo llama *loss*. |
| 25-40 | Viz + apuesta: variable vs parámetro | `viz/variable-vs-parametro.html`. **Primero se pregunta y se vota**: "si muevo esta perilla, ¿se mueve la bolita o se mueve la curva?". Recién después se mueve. |
| 40-60 | Manos 1: notebook, primera parte | Colab. Definir funciones en Python, graficarlas, cambiar parámetros y ver el efecto. TODO 1: reproducir una figura objetivo moviendo dos números. |
| 60-70 | Pausa | |
| 70-85 | Exposición: el zoo de funciones | Recta, parábola, sigmoide, exponencial, seno: qué forma tiene cada una y para qué sirve como pieza. `viz/zoo-de-funciones.html`. Se planta la semilla: "guardá la sigmoide, va a ser importante". |
| 85-105 | Manos 2: ajuste a ojo | De a dos. Datos reales de discurso político; ajustan a mano `a` y `b`; el notebook les muestra el número de desajuste. Competencia sana: quién llega más bajo. |
| 105-120 | Cierre | `[EL LUNES]`: tomá una serie tuya, graficala, ajustale una curva y explicá qué significa cada parámetro *sustantivamente* (una pendiente es "cuánto sube por año"). **Puente**: "hoy dibujamos con una recta. Pero los datos no son una recta. ¿Qué hacemos, buscamos una fórmula más rara? No: **componemos**. Eso es la clase que viene." |

**Conexión hacia atrás:** es la primera. **Hacia adelante:** la limitación evidente (la recta no
alcanza) es el motor de la clase 2; el "medidor de desajuste" que ajustaron a ojo es exactamente
la *loss* de la clase 3, y el hecho de que ajustarla a mano sea insoportable es el motivo de que
exista el descenso por gradiente.

---

### Clase 2 — Componer funciones: dibujar lo imposible
`clases/02-componer-funciones/` · Espec: `_shared/especificaciones/clase-02-componer-funciones.md`

**Gancho (10 min).**
Se proyecta una figura complicada: la curva real de menciones a "inflación" en 40 años de discursos,
con dos picos y un valle. Desafío en vivo, con los sliders de la clase anterior: **"ajustale una
recta. Dale, la mejor recta posible."** Es un fracaso hermoso y visible. Segundo intento: "¿y si le
damos más perillas a la recta?" — más perillas, sigue siendo una recta. El aula queda trabada. Ese
es el punto: hoy la destrabamos, y la llave no es una fórmula más complicada, es **apilar**.

**Objetivos. Vas a poder:**
- Explicar qué significa componer dos funciones (`la salida de una es la entrada de la otra`) y
  seguir a mano el recorrido de un número por una cadena de tres funciones.
- Explicar por qué apilar cosas lineales **no sirve para nada** si no hay un doblez en el medio, y
  qué es una función de activación (ReLU) en términos de dobleces.
- Construir mentalmente cualquier figura como una suma de rampas, y decir cuántas rampas hacen
  falta más o menos.
- Mirar un diagrama de red neuronal (círculos y flechas) y traducirlo a "esto es una fórmula
  compuesta con estas perillas".

**Intuición central.**
Con muchas piezas simples y un doblez entre pieza y pieza, dibujás cualquier cosa. Una red neuronal
no es un cerebro: es una **suma de rampas** con las alturas y los puntos de quiebre regulables.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | El fracaso de la recta contra la curva de "inflación". |
| 10-25 | Exposición: componer | `viz/lego-de-funciones.html`: cadena de 3 bloques, se ve el gráfico intermedio en cada etapa. Analogía social: una cadena de mediaciones (dato bruto → codificación → índice → interpretación). |
| 25-35 | Viz + apuesta: el doblez | `viz/sin-no-linealidad.html`. Se apuesta: "si apilo dos rectas, ¿qué sale?". Sale una recta. Frustración productiva. Entra ReLU: `max(0, x)`, la función más tonta del mundo, dibujada como una rampa. |
| 35-55 | Manos 1 | Notebook: componer funciones en Python, ver que `g(f(x))` cambia según el orden. Implementar ReLU en una línea. TODO: sumar dos rampas a mano para dibujar una "V" invertida. |
| 55-65 | Pausa | |
| 65-85 | El momento fuerte: sumar rampas | `viz/rampas.html`. El docente arranca con 1 rampa, después 2, 4, 8, contra la curva objetivo. **Aha del curso.** Se nombra: "esto que acabás de ver es el teorema de aproximación universal, y no vamos a demostrarlo porque acabás de verlo". |
| 85-105 | Manos 2 | `viz/red-como-dibujante.html` en pantalla; en el notebook, escriben a mano (sin PyTorch) una red de 1 capa oculta con 4 neuronas, con los pesos puestos a dedo, y la grafican. TODO: llevarla a 8 neuronas. |
| 105-120 | Cierre | `[EL LUNES]`: cuando leas "usamos una red neuronal", traducí mentalmente "usamos una función muy flexible con muchísimas perillas", y preguntá lo que hay que preguntar: ¿cuántas perillas? ¿cuántos datos? **Puente**: "sabemos dibujar cualquier cosa. Pero pusimos los pesos a mano. Con 8 perillas ya es un infierno; con 8 millones es imposible. ¿Cómo hace la máquina para encontrarlas sola? Clase que viene." |

**Conexión hacia atrás:** la recta de la clase 1 fracasa, y esa es la puerta. **Hacia adelante:**
poner pesos a mano es insostenible → clase 3.

---

### Clase 3 — Estar equivocado es un número, y ese número tiene pendiente
`clases/03-loss-y-gradiente/` · Espec: `_shared/especificaciones/clase-03-loss-y-gradiente.md`

**Gancho (10 min).**
Dos rectas sobre la misma nube de puntos, roja y azul. "¿Cuál es mejor?" Se vota. Siempre se
divide el aula. "Bueno, discutan." A los dos minutos alguien dice "depende de qué te importe".
**Exacto.** Para que la máquina elija sola, alguien tiene que escribir qué le importa. Eso es la
*loss*, y no es un detalle técnico: es una decisión metodológica con consecuencias.

**Objetivos. Vas a poder:**
- Explicar qué es una función de pérdida (*loss*) y por qué es una decisión tuya, no de la
  computadora.
- Mostrar en un dibujo qué es el gradiente: la dirección de máxima subida, y por qué vamos para el
  otro lado.
- Explicar el descenso por gradiente como "bajar una colina con niebla, tanteando la pendiente con
  el pie".
- Anticipar qué pasa si la tasa de aprendizaje (*learning rate*) es muy chica o muy grande, y
  reconocer los dos síntomas en un gráfico de loss.
- Explicar por qué elegir MSE en vez de MAE cambia a quién le hace caso el modelo.

**Intuición central.**
Si podés ponerle un número a "qué tan mal la estoy dibujando", ese número dibuja un paisaje sobre
el espacio de las perillas. Y todo el aprendizaje automático es: soltar una pelota en ese paisaje
y dejarla rodar hasta el fondo.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | Roja vs azul: ¿cuál es mejor? |
| 10-25 | Exposición: la loss | El desajuste de la clase 1 ahora tiene nombre. MSE y MAE. `viz/comparador-de-losses.html` con un outlier arrastrable. Discusión sustantiva: "un caso extremo, ¿es un error de medición o es el caso más importante de tu corpus?". |
| 25-40 | Manos 1a: arrastrá el outlier | Bloque práctico corto y temprano (slide 10 de la espec): arrastran el caso influyente y miran cuál de las dos rectas se mueve. Dura poco a propósito: la idea es que toquen antes de que llegue la parte pesada. |
| 40-60 | El paisaje y la niebla | `viz/valle-de-loss.html`. Cada punto del plano `(a,b)` es una recta posible; el color es qué tan mal está. **Aha 1**: encontrar la recta se convirtió en encontrar el fondo de un valle. Después, por qué la fuerza bruta muere en 8 dimensiones, y la pendiente sin cálculo. |
| 60-70 | Pausa | |
| 70-90 | El gradiente y el learning rate | La flecha en `viz/valle-de-loss.html` y `viz/loss-1d.html` (derivada = pendiente de la tangente, sin epsilon ni límites). Botón **"soltar la pelota"** con rastro. Slider de learning rate: chico (tarda una eternidad), justo, enorme (sale despedida). `viz/tasa-de-aprendizaje.html` corre tres pelotas en paralelo. |
| 90-110 | Manos 1b / 2 | Notebook: descenso por gradiente escrito a mano en 10 líneas, con derivadas numéricas (nada de cálculo simbólico). Ven la curva de loss bajar. TODO: romperlo con un lr de 1.5 y explicar el gráfico resultante. |
| 110-120 | Cierre | `[EL LUNES]`: cuando un paper dice "optimizamos", ahora sabés que quiere decir "soltamos una pelota en un paisaje que definimos nosotros". Y la pregunta de revisor: *¿qué paisaje?* **Puente**: "ya sabemos dibujar (clase 2) y sabemos buscar solos las perillas (hoy). La clase que viene juntamos las dos cosas y entrenamos de verdad, con PyTorch, y descubrimos el primer modo de mentirse a uno mismo." |

**Conexión hacia atrás:** resuelve el problema que dejó abierto la clase 2. **Hacia adelante:**
tenemos todas las piezas; falta el ciclo que las une y las trampas que trae.

---

### Clase 4 — El ciclo de entrenamiento, y la diferencia entre dibujar y calcar
`clases/04-entrenar-de-verdad/` · Espec: `_shared/especificaciones/clase-04-entrenar-de-verdad.md`

**Gancho (10 min).**
Dos modelos predicen el tono de titulares. El modelo A acierta el 99% en los datos con los que se
entrenó. El modelo B, el 84%. "¿Cuál publicarías?" Casi toda el aula elige A. Después se muestran
los datos nuevos: A acierta 61%, B acierta 82%. **A no aprendió: calcó.** Hoy vamos a entender
exactamente cómo pasa eso y cómo evitarlo, porque es *el* error metodológico que va a estar en el
paper de alguien de esta sala.

**Objetivos. Vas a poder:**
- Escribir y leer un training loop de PyTorch y decir qué hace cada una de sus cinco líneas.
- Explicar qué son *epoch*, *batch* y *learning rate* sin mirar el apunte.
- Diagnosticar sobreajuste (*overfitting*) mirando dos curvas de loss.
- Partir tus datos en entrenamiento / validación / test y explicar por qué el test se toca **una
  sola vez**, y qué pasa si lo mirás muchas veces.
- Correr un experimento chiquito completo y reportarlo honestamente.

**Intuición central.**
Un modelo con suficientes perillas puede pasar por todos tus puntos, incluido el ruido. Eso no es
aprender, es memorizar tu muestra. La única defensa es guardar datos que el modelo nunca vio.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | Modelo A vs modelo B. La trampa del 99%. |
| 10-30 | El ciclo | `viz/anatomia-del-loop.html`: diagrama con botón "un paso" que ilumina forward → loss → backward → update y muestra los números reales. Se traduce cada flecha a la línea de PyTorch correspondiente. |
| 30-50 | Manos 1 | Notebook: la red de la clase 2, ahora en PyTorch, entrenada con el descenso de la clase 3, sobre los mismos datos de la clase 1. **Se cierra el círculo de las cuatro clases con el mismo dataset.** TODO: cambiar el número de neuronas y ver el efecto. |
| 50-60 | Pausa | |
| 60-80 | Calcar vs dibujar | `viz/sobreajuste.html`: slider de capacidad y slider de cantidad de datos; curvas de train y val; la figura pasando por todos los puntos. Analogía: el codificador que aprendió las manías del corpus piloto. Se introduce *early stopping* como "pará cuando la validación empieza a empeorar". |
| 80-105 | Manos 2 | Notebook: partición train/val/test, curvas, early stopping, y un experimento de a dos con hipótesis escrita antes de correr. |
| 105-120 | Cierre + evaluación de la unidad | `[EL LUNES]`: la regla de oro (test una sola vez) y cómo se escribe en un paper. Repaso del arco 1-4 en una sola slide: perillas → composición → loss → ciclo. **Puente**: "todo esto lo hicimos con un número que entra y un número que sale. Pero tus datos no son números sueltos: son fotos, son discursos, son secuencias. Y ahí la *forma* del dato cambia todo. Clase que viene: por qué la arquitectura es una teoría sobre el mundo." |

**Conexión hacia atrás:** integra las clases 1-3. **Hacia adelante:** hasta acá el dato era un
escalar; la clase 5 rompe eso.

---

### Clase 5 — La forma de los datos manda (I): imágenes
`clases/05-imagenes-y-convoluciones/` · Espec: `_shared/especificaciones/clase-05-imagenes-y-convoluciones.md`

**Gancho (10 min).**
Se proyecta una foto de una movilización. "¿Cuánta gente hay?" Se estima a ojo. Después: la misma
foto corrida 20 píxeles a la derecha. "¿Cambió algo para vos?" No. "Para la red de la clase 4,
cambió *todo*: cada píxel es una variable distinta, y le movimos todas las variables." El problema
del día: cómo se le enseña a una máquina algo que para nosotros es obvio — que un objeto sigue
siendo el mismo objeto si está un poquito más a la derecha.

**Objetivos. Vas a poder:**
- Explicar por qué una imagen no es "una lista larga de números" y qué se pierde al tratarla así.
- Explicar qué hace una convolución mostrando un filtro deslizándose, y qué detecta un filtro.
- Decir en una frase qué **supuestos sobre el mundo** mete adentro una CNN (localidad, repetición
  del mismo patrón en todos lados, jerarquía) y en qué casos esos supuestos son falsos.
- Entrenar una CNN chiquita y comparar su desempeño contra la red densa de la clase 4.
- Leer críticamente un paper de ciencias sociales que usa imágenes (satelitales, archivo
  fotográfico, prensa gráfica) y hacer las tres preguntas correctas.

**Intuición central.**
La arquitectura de una red es una **teoría sobre cómo está estructurado el mundo**. La CNN dice:
"lo importante es local, y lo que aprendí a reconocer en una esquina vale en todas las esquinas".
Cuando esa teoría es cierta, la CNN necesita muchísimos menos datos. Cuando es falsa, te miente.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | La foto corrida 20 píxeles. |
| 10-25 | La imagen como grilla | `viz/vecindad-de-pixeles.html`: botón **"barajar los píxeles"**. La red densa da exactamente el mismo resultado con los píxeles barajados; tu ojo no puede ni ver qué es. **Aha**: la red densa nunca supo que había una grilla. |
| 25-45 | La convolución | `viz/kernel-deslizante.html`: filtro 3x3 con 9 sliders sobre una foto de prensa; presets de borde vertical, horizontal, desenfoque. `[CALLBACK DIBUJO]`: "el filtro es un pincel; la red aprende sus pinceles". |
| 45-60 | Manos 1 | Notebook: aplicar filtros a mano con numpy sobre una foto; después `nn.Conv2d`; ver los mapas de activación. |
| 60-70 | Pausa | |
| 70-85 | Jerarquía y supuestos | `viz/jerarquia.html` (bordes → texturas → partes → objeto) y `viz/supuestos-de-arquitectura.html` (tabla interactiva: qué supone cada arquitectura, cuándo se rompe). |
| 85-105 | Manos 2 | Entrenar una CNN chica en un sandbox rápido (FashionMNIST) y comparar contra la densa: misma cantidad de parámetros, mejor resultado. Después, el caso real: un clasificador binario sobre imágenes de prensa (multitud / no multitud) con transferencia mínima. |
| 105-120 | Cierre | `[EL LUNES]`: la lectura crítica de *Jean et al. 2016* (predecir pobreza desde imágenes satelitales) y las tres preguntas: ¿qué está midiendo realmente el modelo? ¿el supuesto de invariancia vale acá? ¿qué pasa fuera de la región de entrenamiento? **Puente**: "las imágenes tienen estructura espacial. El texto tiene otra estructura: el **orden**. Y el orden es más difícil, porque el significado de una palabra depende de las que están lejos." |

**Conexión hacia atrás:** la red densa de la clase 4 muestra su límite. **Hacia adelante:** si la
estructura espacial pide una arquitectura, la estructura secuencial pide otra.

---

### Clase 6 — La forma de los datos manda (II): texto, secuencias y embeddings
`clases/06-texto-secuencias-embeddings/` · Espec: `_shared/especificaciones/clase-06-texto-secuencias-embeddings.md`

**Gancho (10 min).**
Dos frases en pantalla:
*"La comisión rechazó al ministro."* / *"El ministro rechazó a la comisión."*
"¿Significan lo mismo?" Risas. Ahora se muestran las dos convertidas en bolsa de palabras: **son el
vector idéntico**. La técnica de análisis de texto más usada en ciencias sociales durante treinta
años no puede distinguir quién le hizo qué a quién. Hoy arreglamos eso.

**Objetivos. Vas a poder:**
- Explicar cómo se convierte texto en números: tokenización, vocabulario, one-hot, embedding.
- Explicar por qué un *embedding* es un mapa donde la cercanía significa parecido de uso, y por qué
  eso no es lo mismo que parecido de significado.
- Usar embeddings para medir similitud entre documentos de tu corpus y encontrar los vecinos de una
  palabra.
- Detectar y mostrar un sesgo en un espacio de embeddings, y explicar de dónde vino.
- Explicar por qué un modelo que lee en orden y va acumulando memoria (RNN) se olvida del principio,
  y por qué eso motiva lo de la clase que viene.

**Intuición central.**
Para que una máquina lea, cada palabra tiene que tener un **lugar en un mapa**, y ese lugar lo
determina la compañía que la palabra frecuenta. `[CALLBACK DIBUJO]`: hasta ahora dibujábamos
figuras; hoy dibujamos el mapa donde las palabras viven, y la geometría de ese mapa *es* el
significado que el modelo maneja.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | La comisión y el ministro. |
| 10-30 | De texto a números | `viz/tokenizador.html`: escribís una frase y ves cómo se parte. "Inconstitucionalidad" son varios pedazos. **Semilla plantada** para la clase 8 (por qué no sabe contar letras). One-hot: `viz/one-hot-vs-embedding.html`, la matriz gigante y absurda. Y la idea del embedding: darle a cada palabra un lugar. |
| 30-50 | Manos 1 | Notebook: tokenizar un corpus de discursos, construir vocabulario, contar, matriz de coocurrencia, y ver que "vecino en el mapa" ≈ "aparece en contextos parecidos". **Tienen que tokenizar antes de poder mirar el mapa**: por eso este bloque va antes que el siguiente. |
| 50-60 | Pausa | |
| 60-78 | El mapa de palabras | `viz/espacio-de-embeddings.html`: nube 2D del vocabulario político **construida con el corpus que acaban de tokenizar**, buscador, vecinos más cercanos, aritmética de vectores, y un panel de **sesgo** (qué ocupaciones caen cerca de qué género). Discusión: el sesgo del modelo es un dato sobre el corpus, y eso puede ser un hallazgo, no sólo un problema. |
| 78-95 | Manos 2 | Notebook: entrenar embeddings chiquitos sobre el corpus y explorarlos; medir similitud coseno entre discursos de distintos años. `[EL LUNES]` incorporado acá. |
| 95-110 | El orden importa | `viz/bolsa-vs-orden.html`. Después, la RNN contada en un minuto: leer palabra por palabra arrastrando una mochila de memoria. **Y su falla**: `viz/memoria-que-se-olvida.html`, una frase larga donde el sujeto queda a 30 palabras del verbo. |
| 110-120 | Cierre | Se plantea el problema abierto: "necesitamos algo que, al leer la palabra 'lo' de la línea 30, pueda mirar directamente a la palabra 'proyecto' de la línea 2, sin haber tenido que acordarse todo el camino. ¿Y si en vez de memoria le damos **atención**?" **Bloque apretado: si se atrasa, se recorta «las RNN en 30 segundos», nunca el puente.** |

**Conexión hacia atrás:** la clase 5 mostró que la forma del dato define la arquitectura; el texto
tiene otra forma. **Hacia adelante:** el fracaso de la memoria secuencial es exactamente el hueco
que llena attention.

---

### Clase 7 — Attention: cada palabra arma su propio resumen del contexto
`clases/07-attention-y-transformer/` · Espec: `_shared/especificaciones/clase-07-attention-y-transformer.md`

**Gancho (10 min).**
Una oración larga de un debate parlamentario, proyectada. "Cuando leíste la palabra *lo* al final,
¿a qué palabra fuiste a buscar?" Se marca en pantalla. Todos fueron al mismo lugar, y ninguno leyó
la oración de nuevo desde el principio: **saltaron**. Eso que hacés sin pensar tiene nombre y es
lo único nuevo del transformer.

**Objetivos. Vas a poder:**
- Explicar self-attention como "cada palabra le pregunta a todas las demás qué tan relevantes son
  para ella, y se arma un resumen ponderado".
- Explicar qué son query, key y value con una analogía que te acordás (el aviso clasificado).
- Explicar por qué hace falta la máscara causal en un modelo que genera texto, y qué pasa sin ella.
- Explicar para qué está el *positional encoding*: sin él, el transformer también sería una bolsa
  de palabras.
- Leer un mapa de atención y decir qué se puede y qué **no** se puede concluir de él.

**Intuición central.**
Attention es lo contrario de la memoria: en vez de acumular todo en una mochila que se va
desbordando, cada palabra **mira a todas las demás en paralelo** y se arma su propio resumen a
medida. `[CALLBACK DIBUJO]`: cada palabra dibuja su propio mapa de a quién mira; ese mapa tiene
perillas (Q, K, V) y se aprende con el mismo descenso por gradiente de la clase 3. Nada nuevo bajo
el sol, sólo mejor organizado.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | El salto que hiciste al leer "lo". |
| 10-30 | Attention a mano | `viz/attention-como-mesa.html`: hacés clic en una palabra y ves las flechas de grosor variable hacia las demás. Se hace primero **sin fórmula**: sólo "pesos que suman 1" y "promedio ponderado". |
| 30-45 | Q, K, V | `viz/qkv.html` con la analogía del aviso clasificado: cada palabra publica un aviso de "lo que ofrezco" (key) y busca "lo que necesito" (query); el match determina el peso; lo que se lleva es el value. Recién ahí aparece la fórmula, ya vacía de misterio. |
| 45-60 | Manos 1 | Notebook: implementar attention con 12 líneas de numpy/torch sobre una oración de verdad, imprimir la matriz de pesos, ver que las filas suman 1. |
| 60-70 | Pausa | |
| 70-85 | Máscara causal, cabezas, posición | `viz/matriz-de-atencion.html` (heatmap con triángulo), `viz/cabezas.html` (varias cabezas con patrones distintos). Por qué sin *positional encoding* volvemos a la bolsa de palabras de la clase 6. |
| 85-105 | Manos 2 | Notebook: armar el bloque transformer completo (attention + MLP + residual + norm) como piezas de Lego, y verificar formas de tensores. No se entrena todavía: se **construye**. |
| 105-120 | Cierre | `[EL LUNES]`: cómo leer (y cómo no) un paper que "interpreta" los mapas de atención de un modelo. Attention **no** es explicación causal. **Puente**: "tenemos el bloque. La clase que viene lo apilamos, lo entrenamos con datos de verdad, y lo vemos escribir. Y después traducimos cada pieza a algo que ChatGPT hace y que te vuelve loco." |

**Conexión hacia atrás:** resuelve la falla de memoria de la clase 6. **Hacia adelante:** el bloque
construido hoy se entrena mañana.

---

### Clase 8 — Un mini-GPT propio, y la traducción a ChatGPT
`clases/08-mini-gpt-y-los-llm/` · Espec: `_shared/especificaciones/clase-08-mini-gpt-y-los-llm.md`

**Gancho (10 min).**
Se lee en voz alta un párrafo de un debate parlamentario. Tiene la cadencia, las fórmulas de
cortesía, los giros. Se vota si es real o generado. Es generado — por un modelo de un millón y medio de
parámetros que entrenamos en menos de siete minutos, en esta misma clase, y que vas a poder mirar por dentro
línea por línea. **Todo lo que hace ChatGPT que te resulta mágico o irritante lo vas a poder
explicar antes de que termine la clase.**

**Objetivos. Vas a poder:**
- Entrenar un modelo de lenguaje desde cero y leer su curva de loss.
- Explicar qué significa "predecir la próxima ficha (*token*)" y por qué de ahí sale *todo* lo demás.
- Explicar, en términos del modelo que acabás de entrenar y no por analogía vaga:
  **por qué alucina**, **por qué le importa tanto el prompt**, **qué es la ventana de contexto**,
  **qué hace la temperatura**, **por qué cuenta mal las letras**, **por qué el mismo prompt da
  respuestas distintas**, y **por qué a veces se contradice a mitad de párrafo**.
- Explicar en qué se diferencia tu mini-GPT de ChatGPT (escala, datos, y sobre todo el
  entrenamiento posterior con humanos) y qué de lo que aprendiste **sí** escala.
- Decidir con criterio cuándo un LLM es una herramienta válida para una tarea de investigación.

**Intuición central.**
Un modelo de lenguaje es una máquina de dibujar **la distribución de probabilidad de la próxima
ficha**, condicionada por lo que hay en la ventana. No hay base de datos adentro, no hay
verificador de verdad, no hay casillero para "no sé". `[CALLBACK DIBUJO — el grande]`: en la clase
1 dibujábamos una recta con 2 perillas; hoy dibujamos una distribución sobre 5.000 palabras
posibles con un millón y medio de perillas. **Es la misma máquina.**

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | ¿Real o generado? Se vota. |
| 10-20 | El objetivo más tonto del mundo | Predecir la próxima ficha. Se muestra el dataset: ventana de texto → siguiente ficha. Se muestra el modelo bigram tonto, que ya escribe algo, y se ve por qué no alcanza. |
| 20-40 | Manos 1: entrenar | Notebook: se apilan los bloques de la clase 7, se entrena sobre el corpus de debates. La loss baja. Cada 500 pasos se imprime una muestra: de sopa de letras a palabras a sintaxis a cadencia parlamentaria. **Es el momento más lindo del curso.** |
| 40-50 | Pausa (mientras entrena) | El entrenamiento sigue corriendo de fondo. |
| 50-75 | **La traducción**: el modelo → ChatGPT | El bloque que paga todo el módulo. Una pieza a la vez, con su viz, y cada una termina en un comportamiento observable: `viz/temperatura.html`, `viz/ventana-de-contexto.html`, `viz/por-que-alucina.html`, `viz/contar-letras.html`. Ver la tabla de traducción en la especificación de la clase. |
| 75-100 | Manos 2 | Notebook: jugar con la temperatura sobre tu propio modelo; medir cuánto empeora al pasarse de ventana; hacer que alucine a propósito y explicar por qué; probar el conteo de letras. Ejercicio de a dos: *escribí el prompt que rompe el modelo* y explicá por qué se rompió. |
| 100-120 | Cierre | Qué le falta a tu mini-GPT para ser ChatGPT (escala, datos, instruction tuning y RLHF contados en 5 minutos) y qué **no** cambia con la escala. `[EL LUNES]`: usar LLMs en investigación — para qué sí (asistente de codificación con validación humana), para qué no (fuente de hechos). **Puente**: "entrenar uno tuyo desde cero es carísimo y casi nunca es lo que necesitás. Lo que vas a hacer de verdad es agarrar uno entrenado por otro. Clases 9 y 10." |

**Conexión hacia atrás:** entrena el bloque de la clase 7 con las herramientas de las clases 3 y 4.
**Hacia adelante:** el costo del pre-entrenamiento motiva el transfer learning.

---

### Clase 9 — Usar modelos que ya existen, sin creerles
`clases/09-modelos-preentrenados/` · Espec: `_shared/especificaciones/clase-09-modelos-preentrenados.md`

**Gancho (10 min).**
Se muestra el presupuesto estimado de entrenar un modelo grande. Después, tres líneas de código que
bajan un modelo que alguien ya entrenó y clasifican 5.000 titulares en 40 segundos. "Genial. Ahora
la pregunta que hace la diferencia entre tu paper y un blog post: **¿cómo sabés que está bien?**"
Ese es el 70% de la clase.

**Objetivos. Vas a poder:**
- Usar Hugging Face para bajar y aplicar un modelo pre-entrenado en español a tu corpus.
- Explicar transfer learning y fine-tuning con la metáfora del investigador que ya sabe el idioma y
  sólo tiene que aprender tu campo.
- Elegir entre tres estrategias según tu situación real: embeddings + clasificador simple,
  zero-shot, o fine-tuning; y justificar la elección por cantidad de datos etiquetados.
- Armar un conjunto de validación etiquetado a mano y reportar accuracy, precisión, recall, F1 y
  matriz de confusión **explicando qué significa cada uno en tu problema sustantivo**.
- Comparar siempre contra un baseline tonto y contra el acuerdo entre codificadores humanos.

**Intuición central.**
Un modelo pre-entrenado es como un informante clave: sabe muchísimo del terreno, te ahorra meses, y
tiene sus propias posiciones y puntos ciegos. Se lo usa, se lo cita, y se lo **contrasta**.
`[CALLBACK DIBUJO]`: no dibujamos desde cero; agarramos a alguien que ya sabe dibujar y le
enseñamos nuestro estilo con cuatro trazos.

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | Tres líneas de código y la pregunta incómoda. |
| 10-25 | Transfer learning | Qué se congela y qué se reentrena, dibujado como capas. Por qué las primeras capas son genéricas y las últimas específicas (callback a la jerarquía de la clase 5). Modelos en español: BETO, RoBERTuito, modelos multilingües. |
| 25-45 | Manos 1 | Notebook: `pipeline()` sobre titulares reales; embeddings de oraciones; búsqueda semántica en tu corpus; `viz/similitud-semantica.html`. |
| 45-55 | Pausa | |
| 55-75 | Evaluar de verdad | `viz/matriz-de-confusion.html` con slider de umbral: se ve cómo precisión y recall se pelean. Traducción a lenguaje llano: "de cada 100 notas que llamó *protesta*, 23 no lo eran". Baseline tonto. Kappa y el acuerdo entre humanos como techo realista. |
| 75-100 | Manos 2: el proyecto chico | Notebook: fine-tuning de un clasificador sobre ~500 titulares etiquetados; comparación honesta contra zero-shot y contra el baseline; `viz/zero-shot-vs-finetune.html` (cuántas etiquetas hacen falta). |
| 100-120 | Cierre | `[EL LUNES]`: la receta reproducible para clasificar un corpus propio, y qué números hay que reportar sí o sí. **Puente**: "sabés hacerlo andar y sabés medirlo. Falta lo más difícil: convencer a otro —y a vos mismo— de que lo que medís es lo que decís que medís. Última clase." |

**Conexión hacia atrás:** aprovecha lo aprendido sobre pre-entrenamiento en la clase 8.
**Hacia adelante:** la métrica no alcanza; falta validez.

---

### Clase 10 — Criterio: validez, sesgo, reproducibilidad y el revisor 2
`clases/10-criterio-validacion-y-etica/` · Espec: `_shared/especificaciones/clase-10-criterio-validacion-y-etica.md`

**Gancho (10 min).**
Se muestra un resultado precioso: un gráfico donde la "agresividad" del discurso opositor sube
sostenidamente durante una década. F1 de 0.91. Todos lo publicarían. Después se muestra el pliegue:
el modelo aprendió a detectar **la palabra "gobierno"**, que la oposición usa más. La serie
temporal es real, la métrica es real, y el hallazgo es falso. Bienvenidos a la clase más importante
del curso.

**Objetivos. Vas a poder:**
- Distinguir desempeño (¿acierta?) de **validez** (¿mide lo que digo que mide?) y aplicar los tres
  tipos de validez que importan acá: de constructo, de contenido, y externa.
- Auditar un modelo por sesgo con un test concreto y reportable, y explicar de dónde viene el sesgo.
- Hacer reproducible un análisis: semillas, versiones, datos, código, ficha del modelo.
- Anticipar y contestar las seis objeciones que un revisor le va a hacer a tu paper.
- Decir en voz alta **cuándo NO usar deep learning**, y defender esa decisión.
- Escribir la sección de métodos de un paper que use estas herramientas.

**Intuición central.**
El modelo siempre mide *algo*. Tu trabajo profesional no es hacerlo andar —eso lo hace cualquiera
en tres líneas— sino **demostrar qué es ese algo**. `[CALLBACK DIBUJO — el cierre]`: durante diez
clases aprendimos a dibujar. Hoy aprendemos a mirar un dibujo y preguntar: ¿de qué es esto un dibujo?

**Plan minuto a minuto.**
| Min | Bloque | Qué pasa |
|---|---|---|
| 0-10 | Gancho | El hallazgo hermoso y falso. |
| 10-30 | Validez de constructo | `viz/validez-de-constructo.html`: tres casos donde el modelo y el concepto divergen. Cómo se hace la validación: lectura manual de una muestra estratificada, casos límite, test de placebo, análisis de los falsos positivos (que es donde está el conocimiento). |
| 30-50 | Manos 1: auditoría de sesgo | `viz/sesgo-en-el-espejo.html` y notebook: la misma oración cambiando el sujeto (género, nacionalidad, región, clase); se miden las diferencias de score. Se produce una tabla reportable. Discusión: sesgo del corpus vs sesgo del modelo vs sesgo del mundo. |
| 50-60 | Pausa | |
| 60-75 | Reproducibilidad y ética práctica | Semillas, versiones fijadas, datos disponibles, ficha del modelo. Datos sensibles, anonimización, consentimiento y el problema del scraping. Qué se puede publicar y qué no. |
| 75-100 | Manos 2: el juicio | Actividad final. Se reparte un paper corto (real o construido) que usa estas técnicas. Mitad del aula lo defiende, mitad lo revisa. 15 minutos de preparación, 10 de audiencia. **Se evalúa con el checklist del curso.** |
| 100-115 | La caja de herramientas completa | Una slide con el mapa entero del curso: de la perilla al transformer. Cuándo NO usar deep learning (n chico, necesitás coeficientes interpretables, una regresión ya te lo resuelve, el costo del error es alto). `viz/checklist-revisor.html` genera un borrador de párrafo de métodos. |
| 115-120 | Cierre del curso | Adónde seguir, y la frase final: *lo que aprendiste no es a usar una biblioteca; es a no dejarte impresionar.* |

**Conexión hacia atrás:** convierte la capacidad técnica de la clase 9 en criterio profesional.
**Hacia adelante:** el proyecto propio del estudiante.

---

## 3. Decisiones transversales de diseño

### 3.1 Los datos: el corpus Aguasclaras y los corpus reales

**Problema.** Necesitamos discursos políticos y prensa en español, en cantidad suficiente para
entrenar un mini-GPT (~1 MB de texto), disponibles sin conexión, y sin cometer la barbaridad de
poner frases inventadas en boca de personas reales.

**Solución adoptada, en dos capas:**

1. **Corpus Aguasclaras (sintético, declarado).** Un país ficticio con su historia política,
   sus partidos, sus diputados y sus diarios. Generado programáticamente por
   `datos/generar_aguasclaras.py` a partir de gramáticas y plantillas, con semilla fija.
   Se usa para todo lo que requiera volumen: el mini-GPT (clases 7-8), las series temporales de
   menciones (clases 1-4), el corpus de titulares etiquetados (clase 9).
   **Tiene una ventaja pedagógica enorme y hay que explotarla explícitamente**: como conocemos el
   proceso generador, podemos auditar *exactamente* qué aprendió el modelo y qué se inventó. En la
   clase 8 eso permite mostrar una alucinación con la verdad al lado.
   Regla innegociable: en todo material donde aparezca, se rotula como sintético.

2. **Corpus reales de dominio público**, cuando se consigan y se verifiquen: discursos oficiales
   publicados por organismos públicos, textos de leyes, documentos históricos fuera de derechos.
   Se usan para los momentos de "esto es real" y para el `[EL LUNES]`. **Toda URL de descarga tiene
   que ser verificada por el equipo que construye la clase** (el entorno de desarrollo tiene la red
   restringida; Colab no). Cada notebook implementa el patrón de descarga con red:

   ```python
   # Patrón obligatorio en todos los notebooks
   try:
       datos = descargar(URL)          # en Colab, con internet
   except Exception:
       datos = generar_sinteticos()    # siempre funciona, semilla fija
       print("Usando el corpus sintético Aguasclaras (no hubo conexión).")
   ```
   Ningún notebook puede fallar por falta de red. Ninguno.

### 3.2 El dataset que atraviesa las clases 1 a 4

Las cuatro primeras clases usan **la misma serie**: porcentaje de palabras dedicadas a un tema
(seguridad, inflación, educación) en el discurso anual de apertura, a lo largo de 40 años.
Es deliberado: en la clase 4, cuando finalmente se entrena una red en PyTorch, los datos son los
mismos que en la clase 1 se ajustaban a ojo. El estudiante ve **el mismo problema resuelto cuatro
veces, cada vez mejor**. Ese reconocimiento es la mitad de la sensación de progreso.

### 3.3 La progresión de herramientas

| Clase | Qué usa | Qué se esconde |
|---|---|---|
| 1-2 | numpy + matplotlib, funciones a mano | Nada |
| 3 | numpy, derivadas numéricas a mano | El cálculo simbólico |
| 4 | PyTorch: tensores, `nn.Module`, autograd, optimizador | El detalle de backprop (se nombra, no se deriva) |
| 5-8 | PyTorch completo | Nada nuevo |
| 9-10 | Hugging Face `transformers` | El training loop (ya lo conocen: por eso se puede esconder) |

La regla: **una abstracción sólo se permite después de que hayan hecho a mano lo que esconde.**

### 3.4 Evaluación del curso

- **Cuestionario por clase** (`cuestionario.md` + soluciones): 8-12 ítems, mezcla de multiple choice
  conceptual, "qué pasa si...", lectura de gráfico, y **siempre al menos uno de criterio o ética
  aplicada**. Se resuelve en 15 minutos, no se corrige con nota: se usa para conversar.
- **Proyecto final opcional**: aplicar el pipeline de las clases 9-10 al corpus propio del
  estudiante, con el checklist de la clase 10 como rúbrica.

### 3.5 Glosario vivo

`recursos/glosario.md` se va llenando clase a clase con cada término en inglés que aparece, su
traducción, la analogía que usamos en clase, y **en qué clase se introdujo**. Los estudiantes lo
tienen abierto. El equipo que construye cada clase tiene que agregar sus términos.

---

## 4. El mapa de puentes (leer esto si construís una clase)

Cada clase abre una puerta que la siguiente cruza. Si construís la clase N, el último bloque de tus
slides **tiene que dejar planteado explícitamente el problema que resuelve la N+1**, y el gancho de
la N+1 tiene que retomarlo textualmente.

| Puente | La puerta que queda abierta | Cómo la cruza la clase siguiente |
|---|---|---|
| 1 → 2 | La recta no alcanza para dibujar la curva real | Componiendo funciones simples con un doblez |
| 2 → 3 | Poner los pesos a mano es imposible con más de 4 | Midiendo el error y bajando por su pendiente |
| 3 → 4 | Sabemos bajar, pero ¿bajar hasta dónde, y con qué datos? | El ciclo completo y el conjunto de validación |
| 4 → 5 | El dato era un número; el mundo son imágenes y textos | La arquitectura como teoría sobre la forma del dato |
| 5 → 6 | La estructura espacial pide convoluciones; ¿y la secuencial? | Tokens, embeddings y el problema del orden |
| 6 → 7 | La memoria secuencial se olvida del principio | Attention: mirar directo, en paralelo, a lo que importa |
| 7 → 8 | Tenemos el bloque armado pero sin entrenar | Se apila, se entrena, y se lo ve escribir |
| 8 → 9 | Entrenar desde cero es carísimo y casi nunca hace falta | Transfer learning y modelos pre-entrenados |
| 9 → 10 | El modelo anda y tiene buen F1. ¿Y eso qué prueba? | Validez, sesgo, reproducibilidad y el revisor |

---

## 5. Índice de entregables

Cada clase `clases/NN-slug/` contiene:

- `slides.html` — reveal.js, assets vendoreados por ruta relativa, 25-40 slides, notas del docente
  en `<aside class="notes">`.
- `notebook.ipynb` — Colab, autoinstalable, corre entero en CPU.
- `viz/*.html` — visualizaciones interactivas standalone, sin dependencias.
- `notas-docente.md` — el guion hablado, los tiempos, las preguntas para el aula, qué hacer si se
  atrasa (qué bloque se puede recortar) y qué hacer si sobra tiempo.
- `cuestionario.md` y `cuestionario-soluciones.md`.
- `referencias.md` — con las URLs marcadas como VERIFICAR o VERIFICADA.
