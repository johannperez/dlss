# Clase 5 — La forma de los datos manda (I): imágenes
**Directorio:** `clases/05-imagenes-y-convoluciones/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-4 · **Apertura del módulo 2**

---

## 1. Narrativa de la clase

El módulo 1 terminó con una máquina general: entra un número, sale un número, y con suficientes
rampas dibuja cualquier cosa. El módulo 2 arranca mostrando que **esa generalidad es un problema**.
Una máquina que no supone nada sobre el mundo necesita una cantidad absurda de datos para descubrir
por su cuenta cosas que nosotros sabemos de antemano —por ejemplo, que dos píxeles vecinos tienen
que ver entre sí—. Meterle al modelo lo que ya sabés es la idea central de todo el módulo, y es una
idea profundamente familiar para un cientista social: **los supuestos no son una debilidad del
modelo, son lo que lo hace utilizable**. Un modelo sin supuestos no es más objetivo: es más
hambriento de datos y más fácil de engañar.

El hilo:

1. **La foto corrida.** Para vos es la misma foto. Para el modelo de la clase 4, cambiaron todas
   las variables a la vez. Se instala la pregunta: ¿cómo se le enseña a una máquina algo que para
   nosotros es tan obvio que ni lo pensamos?
2. **La demostración brutal: barajar los píxeles.** Se entrena la red densa con las imágenes
   normales y con los píxeles permutados (la misma permutación para todas). El desempeño es
   **prácticamente idéntico** (unas décimas: ruido de inicialización). Para vos, la segunda versión es ruido puro. Conclusión inevitable: **la red densa
   nunca supo que había una grilla.** Este es el argumento más contundente de la clase y hay que
   correrlo de verdad, no contarlo.
3. **La solución: mirar de a pedacitos.** La convolución, presentada primero como gesto (una
   ventanita que se desliza) y sólo después como operación.
4. **El filtro es un pincel.** `[CALLBACK DIBUJO]`: en la clase 2 sumábamos rampas para dibujar una
   curva; acá el modelo **dibuja sobre la imagen** — cada filtro produce un dibujo nuevo (el mapa de
   activación), que resalta lo que ese filtro busca. La red aprende sus propios pinceles.
5. **La jerarquía.** Bordes → texturas → partes → objetos. Es la respuesta concreta a "por qué
   profundo", que en la clase 2 quedó sólo enunciada.
6. **Los supuestos, explícitos.** Localidad, invariancia traslacional, jerarquía composicional.
   Y —crucial— **cuándo son falsos**: en una tabla de datos sociales, el vecino de una columna no
   tiene nada que ver con ella; en una imagen satelital, "lo mismo en cualquier lugar" es falso si
   el norte y el sur del país se ven distinto por razones que no son las que te interesan.
7. **El caso real y su lectura crítica.** Predicción de pobreza desde imágenes satelitales
   (Jean et al. 2016). Impresionante, útil y lleno de trampas. Se lee con las tres preguntas del
   curso. Este bloque es el `[EN TU INVESTIGACIÓN]` y es el que le da peso de ciencias sociales a la clase.
8. **El puente.** Si la estructura espacial exige una arquitectura, ¿qué exige la estructura
   secuencial del lenguaje?

**Advertencia de diseño.** Es fácil que esta clase se convierta en una clase de visión por
computadora, que no le sirve a casi nadie de esta audiencia. El objetivo real es
**"la arquitectura es una teoría"**; las CNN son el vehículo. Si hay que recortar por tiempo, se
recorta el detalle técnico (padding, stride, pooling) y **nunca** el bloque de supuestos ni el de
lectura crítica.

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-4 | ¿Cuánta gente hay? La misma foto, corrida un píxel. |
| 10-25 | La imagen como grilla | 5-10 | Barajemos: por qué al modelo de la clase 4 le da lo mismo. |
| 25-45 | La convolución | 11-16 | Mirar de a pedacitos, deslizar el filtro, la cuenta de parámetros. |
| 45-60 | Manos 1 | 17 | Notebook: pasar filtros a mano y mirar qué resalta cada uno. |
| 60-70 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 17. |
| 70-85 | Jerarquía y supuestos | 18-25 | La arquitectura como teoría sobre la forma del mundo, y cuándo es falsa. |
| 85-105 | Manos 2 | 26 | De a dos: entrenar la CNN chica y mirar los filtros aprendidos. |
| 105-120 | Cierre | 27-34 | El caso «pobreza desde el espacio», `[EN TU INVESTIGACIÓN]`, el puente a la clase 6. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (34 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | La forma de los datos manda | portada | | |
| 2 | Dónde quedamos | figura | El resumen del módulo 1 en una imagen. | "Tenemos una máquina que dibuja cualquier cosa. Hoy vamos a ver por qué eso no alcanza." |
| 3 | **¿Cuánta gente hay?** | figura | Foto de una movilización. | "Estimen a ojo. Nadie va a controlar." |
| 4 | La misma foto, corrida | figura | La misma foto desplazada 20 píxeles. | "¿Cambió algo para ustedes? No. Para el modelo de la clase 4, le cambiaron **todas** las variables de entrada al mismo tiempo." |
| 5 | Una imagen es una tabla de números | figura | Zoom progresivo sobre un pedacito de la foto hasta ver la grilla con los valores 0-255. | "Esto es lo único que ve la computadora." |
| 6 | Cómo la comía el modelo de la clase 4 | figura | La grilla 28x28 "desenrollada" en una fila larguísima de 784 números. | "Le agarrábamos la imagen y la estirábamos en una fila. Y ahí se perdió algo enorme." |
| 7 | Apuesta | discusión | "Si barajo los píxeles de todas las imágenes con la misma permutación y reentreno, ¿el modelo va a andar peor?" Votan. | Casi todos dicen que sí. |
| 8 | **Barajemos** | VIZ | `viz/vecindad-de-pixeles.html`, botón "barajar". | "Miren lo que ve el modelo. Ahora miren el resultado: **prácticamente el mismo desempeño** (unas décimas)." |
| 9 | La conclusión incómoda | texto | "La red densa nunca supo que había una grilla. Para ella, los 784 números eran 784 variables sueltas." | "Ustedes reconocen un gato en cualquier parte de la foto. La red tendría que aprender 'gato acá', 'gato allá', 'gato en la esquina' por separado. Con muchísimos ejemplos de cada posición." |
| 10 | Lo que nosotros sabemos y ella no | texto | Tres cosas: los píxeles cercanos se relacionan; un patrón vale igual en cualquier posición; las cosas grandes están hechas de cosas chicas. | "Estas tres cosas se las vamos a **regalar** al modelo. Se las metemos en la estructura." |
| 11 | Mirar de a pedacitos | figura | Una lupa de 3x3 sobre la imagen, en una posición. | "En vez de mirar los 784 de una, miramos de a nueve." |
| 12 | Y deslizarla | figura | Secuencia de 4 cuadritos mostrando la lupa en 4 posiciones, con el mapa de salida construyéndose. | "Y la misma lupa, con los mismos nueve números, recorre toda la imagen. **Los mismos**: por eso el patrón vale en cualquier lado." |
| 13 | **Movés el filtro vos** | VIZ | `viz/kernel-deslizante.html`. | Pone el preset "borde vertical". "Miren dónde se enciende: en los bordes verticales. Este filtro es un detector de bordes verticales y son nueve números." |
| 14 | El filtro es un pincel | figura | La imagen original y tres mapas de activación al lado (bordes verticales, horizontales, blur), en falso color. | `[CALLBACK DIBUJO]` "En la clase 2 sumábamos rampas para dibujar una curva. Acá el modelo **dibuja sobre la imagen**: cada filtro produce un dibujo nuevo que resalta lo que ese filtro busca." |
| 15 | Y los pinceles se aprenden | texto | Los 9 números del filtro son parámetros. Se aprenden con la loss y el gradiente de la clase 3. | "No hay nada nuevo en el mecanismo. Lo único nuevo es **qué forma tiene la máquina**." |
| 16 | La cuenta que importa | figura | Comparación de parámetros: capa densa de 784→64 = 50.176 pesos. Capa convolucional con 16 filtros de 3x3 = 144 pesos (nota de construcción: la clase usa 16 filtros; manda la clase). | "Unas trescientas cincuenta veces menos perillas. Y anda mejor. Porque le dijimos algo verdadero sobre el mundo." |
| 17 | Bloque práctico 1 | texto | Consignas: filtros a mano con numpy. | "25 minutos. Van a hacer un detector de bordes con nueve números." |
| 18 | Volvimos | discusión | ¿Qué filtro inventaron? | Se proyecta alguno del aula. |
| 19 | Apilar filtros | figura | Capa 1 sobre la imagen → capa 2 sobre los mapas de la capa 1 → capa 3. | "La segunda capa no mira la imagen: mira los dibujos que hizo la primera." |
| 20 | **La jerarquía** | VIZ | `viz/jerarquia.html`. | "Capa 1: bordes. Capa 2: esquinas y texturas. Capa 3: partes. Capa 4: objetos. Nadie programó esto: emergió." |
| 21 | Ahora sí, por qué "profundo" | texto | Callback explícito a la slide 29 de la clase 2, que quedó prometida. | "Se acuerdan que dije 'piezas hechas de piezas'? Esto es." |
| 22 | Pooling, en 30 segundos | figura | Una grilla que se achica quedándose con el máximo de cada cuadrante. | "Achica la imagen y se queda con lo más fuerte. Sirve para que la capa siguiente vea un pedazo más grande del mundo. Es todo lo que necesitan saber." |
| 23 | Una CNN completa | figura | Diagrama: imagen → conv → pool → conv → pool → aplanar → densa → salida. Con los tamaños anotados. | "Al final siempre hay una capa densa como las de la clase 4. La parte convolucional **extrae**, la densa **decide**." |
| 24 | **La arquitectura es una teoría** | texto | La slide conceptual de la clase, en grande. Tres supuestos de la CNN, enunciados como afirmaciones sobre el mundo. | "Cuando elegís una arquitectura estás afirmando cómo creés que está estructurado tu fenómeno. Es una decisión teórica disfrazada de decisión técnica." |
| 25 | **¿Cuándo son falsos?** | VIZ | `viz/supuestos-de-arquitectura.html`. | "Una tabla de encuesta: ¿el vecino de la columna 'edad' tiene que ver con ella? No. Poner una CNN sobre una tabla es afirmar una falsedad." |
| 26 | Bloque práctico 2 | texto | Consignas: entrenar la CNN y comparar. | "30 minutos." |
| 27 | El resultado | figura | Tabla comparativa: densa vs CNN, con la misma cantidad de parámetros. | "Mismos parámetros, mejor resultado, y encima aguanta que le muevas la imagen." |
| 28 | **El caso: pobreza desde el espacio** | figura | Descripción del enfoque de Jean et al. 2016: imágenes satelitales diurnas + luces nocturnas como señal intermedia → predicción de consumo/riqueza en zonas sin encuestas. | "Esto se publicó en Science y es genuinamente importante: hay países donde no hay datos de pobreza y esto los produce." |
| 29 | Las tres preguntas | texto | (1) ¿Qué está midiendo **realmente**? (2) ¿Valen los supuestos de la arquitectura acá? (3) ¿Qué pasa fuera de donde se entrenó? | "Estas tres preguntas se le hacen a cualquier paper de este tipo, y a su propio trabajo." |
| 30 | Las respuestas incómodas | texto | (1) Puede estar midiendo techos de chapa, densidad de construcción o presencia de rutas, y todas correlacionan con pobreza **en el país donde se entrenó**. (2) La invariancia traslacional vale; la de escala y la de región, no necesariamente. (3) Transferir a otro país es una apuesta fuerte y hay literatura que muestra que se degrada. | "Nada de esto invalida el trabajo. Todo esto tiene que estar discutido en el paper. Si no está, ahí está su comentario de revisor." |
| 31 | `[EN TU INVESTIGACIÓN]` | texto | Cómo leer un paper que usa imágenes: pedir la partición **geográfica**, el desempeño fuera de muestra, y qué pasa con los falsos positivos. Y: si tenés un archivo fotográfico o de prensa gráfica, esto es aplicable con pocos ejemplos etiquetados partiendo de un modelo pre-entrenado (la clase 9 lo hace con texto; con imágenes la lógica es la misma, pero no hay ejercicio de imágenes en la 9). | |
| 32 | Otros usos en ciencias sociales | texto | Lista corta y concreta: digitalización de archivos históricos (OCR de manuscritos, censos), análisis de imágenes de campaña, detección de contenido en redes, conteo de multitudes, cambio en el uso del suelo, análisis de material visual etnográfico. | "Si tienen imágenes en su investigación, hablen conmigo en el recreo." |
| 33 | El puente | texto | "La estructura del espacio pide convoluciones. ¿Y la estructura del lenguaje? El texto no es una grilla: es una **secuencia**, y el significado depende de cosas que están lejos." | "Clase 6: cómo se convierte un discurso en números sin perder el orden." |
| 34 | Glosario de hoy | texto | píxel, canal, filtro/kernel, convolución, mapa de activación, pooling, CNN, invariancia traslacional, sesgo inductivo, jerarquía de representaciones. | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/vecindad-de-pixeles.html`
- **Qué se ve.** Tres paneles. **Izquierda:** una imagen (prenda de FashionMNIST o un recorte de
  foto de prensa en gris). **Centro:** la misma imagen con los píxeles permutados. **Derecha:** dos
  barras de desempeño precalculado — "red densa: 87% / 87%" y "CNN: 91% / 62%".
- **Controles.** Botón **"barajar"** (aplica la permutación con una animación de los píxeles
  volando a su nueva posición: la animación importa, muestra que no se pierde ni se agrega
  información). Botón "desbarajar". Selector de imagen.
- **Qué tiene que hacer clic.** Dos cosas simétricas: la red densa **no se entera** (mismo
  desempeño); la CNN **se desploma**. Que la CNN empeore es la prueba de que estaba usando la
  estructura espacial, y que la densa no empeore es la prueba de que nunca la usó.
- **Momento aha.** "La CNN se cae a 62% con las imágenes barajadas. Entonces el 91% que tenía venía
  de saber dónde estaba cada píxel. La densa siempre estuvo trabajando a ciegas."
- **Nota.** Los números tienen que salir de un experimento realmente corrido por el equipo que
  construya la clase, no inventados; se guardan en el notebook y la viz los muestra. Coherencia
  entre viz y notebook: obligatoria.

### 3.2 `viz/kernel-deslizante.html` — **la viz central de la clase**
- **Qué se ve.** **Izquierda:** la imagen de entrada en escala de grises, con un recuadro de 3x3
  resaltado en la posición actual y los 9 valores de los píxeles impresos adentro.
  **Centro:** el filtro 3x3, como una grilla de 9 celdas editables, cada una con su valor y
  coloreada (azul negativo / blanco cero / rojo positivo).
  **Derecha:** el mapa de activación que se va construyendo píxel por píxel, con el píxel actual
  parpadeando.
  **Abajo:** la cuenta del píxel actual escrita con los 9 productos y su suma, en grande.
- **Controles.**
  - Los 9 valores del filtro, editables (sliders chicos o inputs numéricos).
  - **Presets**: borde vertical, borde horizontal, desenfoque, realce, detector de diagonal,
    "identidad", "todo cero".
  - Botón **"paso a paso"** (mueve la ventana una posición y muestra la cuenta) y botón
    **"deslizar todo"** (animación completa, ~3 segundos).
  - Slider de velocidad.
  - Selector de imagen: una prenda, una cara, una foto de multitud, un afiche de campaña, un
    fragmento de página de diario.
- **Qué tiene que hacer clic.** Que la convolución es una multiplicación y una suma repetida, sin
  ningún misterio, y que **la elección de nueve números determina qué se ilumina**.
- **Momento aha.** Al poner el preset "borde vertical" sobre la foto del afiche: sólo se encienden
  los bordes verticales. "Con nueve números hice un detector."
- **Segundo momento.** Con el preset "todo cero" no aparece nada; con "identidad" sale la imagen
  igual. Los casos degenerados ayudan a entender que el filtro es una elección.
- **Detalle.** Un botón **"filtro al azar"** que se puede apretar muchas veces: casi todos los
  filtros al azar producen porquería. Eso motiva "por eso hay que **aprenderlos**", que es la
  slide 15.

### 3.3 `viz/jerarquia.html`
- **Qué se ve.** Cuatro columnas (capa 1 a capa 4). En cada una, una grilla de 8 miniaturas que
  representan **qué hace que esa unidad se active al máximo**. Capa 1: bordes y colores. Capa 2:
  texturas, esquinas, curvas. Capa 3: partes (una rueda, una cara, una ventana). Capa 4: objetos y
  escenas completas.
- **Controles.** Click en una unidad de la capa 3 → se resaltan las unidades de la capa 2 que más
  la alimentan, con líneas. Click en una unidad de capa 2 → ídem hacia capa 1. Se puede recorrer la
  composición hacia abajo.
- **Qué tiene que hacer clic.** Que "profundo" significa *composicional*: lo complejo está hecho de
  lo simple, y el modelo lo descubrió solo.
- **Momento aha.** "Nadie le dijo que existían las ruedas. Aparecieron porque eran útiles para
  predecir."
- **Implementación.** Las imágenes pueden ser generadas sintéticamente (patrones simples para las
  capas 1-2) y esquemáticas para las 3-4; **no se pueden bajar imágenes de papers de feature
  visualization** (sin red, y por licencias). Se dibujan con canvas. Se rotula honestamente:
  "esquema ilustrativo basado en la literatura de visualización de features".

### 3.4 `viz/supuestos-de-arquitectura.html`
- **Qué se ve.** Una tabla interactiva de 4 filas (Densa/MLP, CNN, RNN, Transformer) y 3 columnas
  (Qué supone, Cuándo es cierto, Cuándo te miente). Al hacer clic en una celda se despliega un
  ejemplo concreto de ciencias sociales, con una mini-figura.
- **Controles.** Un selector arriba: **"tengo estos datos..."** con opciones (una tabla de encuesta,
  fotos satelitales, una serie temporal mensual, un corpus de discursos, una red de contactos).
  Al elegir, la tabla resalta en verde las arquitecturas cuyos supuestos son razonables y en rojo
  las que no, con la justificación en una oración.
- **Qué tiene que hacer clic.** Que elegir arquitectura no es elegir "la más nueva", sino la que
  supone algo verdadero sobre **tus** datos.
- **Momento aha.** Al elegir "una tabla de encuesta": todo se pone rojo o amarillo y aparece el
  cartel "para datos tabulares, un modelo de árboles (gradient boosting) suele ganarle a una red
  neuronal". **Honestidad brutal y muy valiosa para esta audiencia**, que trabaja con tablas todo el
  tiempo. Sembra la conversación de "cuándo NO usar deep learning" de la clase 10.
- **Nota.** Las filas de RNN y Transformer quedan grises con "lo vemos en las clases 6 y 7";
  la viz se **reutiliza** en la clase 7 con esas filas activadas. Reusar la misma viz dos veces con
  más contenido desbloqueado da sensación de progreso.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** < 8 minutos en CPU (el entrenamiento de la CNN es el grueso; se limita a
2 epochs sobre un subconjunto de 8.000 imágenes). **Dependencias:** torch, torchvision, matplotlib.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Objetivo del día. Advertencia de tiempos de ejecución. | |
| 2 | code | Imports + descarga de FashionMNIST (con try/except y fallback a un `.npz` chiquito incluido en `datos/`). | **Rotulado explícito**: "esto es un sandbox técnico, no es ciencia social; volvemos al dominio en la celda 18". |
| 3 | code | Mostrar 16 imágenes con sus etiquetas. Imprimir `shape`. | |
| 4 | md | **Una imagen es una tabla.** | |
| 5 | code | Imprimir la matriz de números de una imagen chica (recortada a 8x8) al lado de la imagen. | El momento "ah, son números". |
| 6 | md | **El experimento del barajado.** | |
| 7 | code | Entrenar la red densa de la clase 4 (misma arquitectura) sobre las imágenes normales. Reporta accuracy. ~90 seg. | |
| 8 | code | Aplicar una permutación fija a todos los píxeles. Mostrar 4 imágenes barajadas. Reentrenar. Reportar. | **El resultado es prácticamente idéntico.** Hay que fijar semilla para que salga bien en clase. |
| 9 | md | `TODO 1` — Escribí en una oración qué demuestra este experimento. *Pista: pensá qué información tenía la imagen original que la barajada no tiene, y si el modelo la usaba.* | |
| 10 | md | **Filtros a mano.** | |
| 11 | code | Función `convolucion(imagen, filtro)` escrita con dos `for` anidados, sin usar torch. Lenta y transparente. | Se subraya que es lenta a propósito: se ve la cuenta. |
| 12 | code | Aplicar tres filtros conocidos (Sobel vertical, horizontal, blur) y graficar los tres resultados. | |
| 13 | md | `TODO 2` — Inventá un filtro que detecte diagonales. *Pista: mirá el de bordes verticales y pensá qué forma tiene que tener la zona positiva.* | |
| 14 | code | Esqueleto + celda de visualización. | |
| 15 | md | `TODO 3` — ¿Qué filtro deja la imagen igual? *Pista: pensá en la multiplicación por 1.* | Identidad. Ejercicio de un minuto que consolida la mecánica. |
| 16 | md | **La CNN.** | |
| 17 | code | `nn.Conv2d` reemplazando el doble `for`; verificación de que da lo mismo que la implementación manual (con `assert` y tolerancia). Definición de la CNN completa. Conteo de parámetros vs la densa. | La verificación manual↔torch es obligatoria (misma política que en la clase 4 con `nn.Sequential`). |
| 18 | code | Entrenar la CNN, 2 epochs. Comparar accuracy con la densa. Volver a barajar y ver que la CNN **sí** se desploma. | Cierra el experimento del inicio. |
| 19 | code | **Ver los filtros aprendidos**: graficar los 16 filtros de la primera capa como imágenes de 3x3. Y los mapas de activación de una imagen. | "Estos nueve números por filtro los encontró el descenso por gradiente de la clase 3." |
| 20 | md | `TODO 4` — Mirá los filtros aprendidos: ¿alguno se parece a los que hiciste a mano? | Casi siempre hay algún detector de borde. Momento lindo. |
| 21 | md | **Volvemos a ciencias sociales.** | |
| 22 | code | Mini-caso: clasificar imágenes en dos categorías de un corpus visual chico (multitud / no multitud, o afiche / no afiche) con ~200 imágenes por clase, generadas o de dominio público, usando la misma CNN. Se reporta accuracy y **matriz de confusión**. | Primera aparición de la matriz de confusión: se muestra sin explicar en detalle, "la clase 9 vive de esto". |
| 23 | md | `TODO 5 (criterio)` — Mirá los errores del modelo (se grafican los 9 casos peor clasificados). Escribí qué tienen en común. *Pista: el conocimiento está en los errores, no en los aciertos.* | **Este TODO es el más importante del notebook.** Es un hábito profesional, no un ejercicio técnico. |
| 24 | md | **Para llevarte** + puente al texto. | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"La CNN es mejor que la densa"** (en general) | Generalizan una comparación específica. | La CNN es mejor **para datos con estructura espacial**. Sobre una tabla de encuesta es peor que casi todo. Viz 3.4, con la fila de datos tabulares. |
| **"El filtro busca objetos"** | Creen que un filtro de la primera capa detecta "personas". | Un filtro de 3x3 sólo puede ver 9 píxeles: no puede ver una persona. Las cosas grandes aparecen recién en capas profundas, por composición. La viz 3.3 lo hace evidente. |
| **Confundir el filtro con el mapa de activación** | Llaman "filtro" a la imagen de salida. | Vocabulario firme y repetido: el **filtro** son los 9 números (el pincel), el **mapa de activación** es el dibujo que produce. La viz 3.2 los muestra en paneles separados y rotulados. |
| **"El modelo ve como nosotros"** | Antropomorfización. | Se muestran ejemplos donde la CNN se confunde de maneras que ningún humano se confundiría (dos imágenes casi idénticas para el ojo, clasificadas distinto). Prepara el terreno para el escepticismo de la clase 10. |
| **Pánico con las dimensiones** | Se pierden con canales, batch, alto, ancho, y los errores de shape los frustran. | Regla mnemotécnica repetida: `(batch, canales, alto, ancho)` — "cuántas fotos, cuántas capas de color, cuán alta, cuán ancha". Y se enseña a **leer el mensaje de error de shape**, que dice exactamente qué esperaba y qué recibió. Enseñar a leer errores es contenido. |
| **Creer que hay que entender pooling/stride/padding a fondo** | Se traban en detalles. | Se dice explícitamente: "estos son detalles de plomería. Si alguna vez armás una CNN los vas a googlear. No son conceptos." |
| **"Entonces puedo medir pobreza con satélites y listo"** | Entusiasmo acrítico con el caso de la slide 28. | Las slides 29-30. Y la pregunta que ordena todo: **¿qué está midiendo realmente?** Se retoma en la clase 10 como validez de constructo. |

---

## 6. Analogías y metáforas de ciencias sociales

- **El sesgo inductivo como teoría previa.** Un modelo sin supuestos no es más objetivo: es más
  ignorante. Igual que una investigación sin marco teórico no es más neutral, es más desorientada.
  Esta analogía es la columna vertebral de la clase y hay que decirla textualmente.
- **La codificación de contenido con libro de códigos.** Un filtro es una regla de codificación
  ("marcá cuando aparezca este patrón") que se aplica sistemáticamente a todo el material. La CNN
  es un ejército de codificadores con reglas aprendidas, aplicadas exhaustivamente. La diferencia
  con la codificación humana: la regla no está escrita en castellano, y ese es exactamente el
  problema de interpretabilidad de la clase 10.
- **Invariancia traslacional = comparabilidad.** Decir "el mismo patrón significa lo mismo en
  cualquier parte de la imagen" es el mismo tipo de supuesto que decir "esta pregunta de encuesta
  significa lo mismo en todas las provincias". A veces es cierto y a veces es una fuente conocida
  de sesgo. Nombrarlo como *equivalencia de medición* le da un anclaje disciplinar.
- **La jerarquía de representaciones y los niveles de análisis.** Micro → meso → macro. El modelo
  arma sus propios niveles intermedios, y —como en la teoría social— los niveles intermedios son
  donde está lo interesante y lo difícil de interpretar.
- **El archivo fotográfico.** Digitalizar y clasificar 40.000 fotos de archivo es literalmente
  imposible a mano y perfectamente factible con esto. Es el ejemplo que más rápido convierte a
  historiadores y antropólogos visuales.
- **El OCR de censos manuscritos.** Un caso donde la tecnología ya cambió la práctica de la
  historiografía cuantitativa, y donde los errores de reconocimiento tienen sesgos sistemáticos
  (nombres poco frecuentes, caligrafías regionales) que se traducen en sesgos de muestra.

---

## 7. Cuestionario: temas a evaluar (11 ítems)

1. **[MC conceptual]** ¿Qué supuesto sobre el mundo incorpora una CNN que una red densa no tiene?
2. **[MC conceptual]** ¿Qué es un filtro/kernel? *(Distractor: "la imagen de salida".)*
3. **[Qué pasa si]** Barajás los píxeles de todas las imágenes con la misma permutación. ¿Qué le
   pasa a la red densa? ¿Y a la CNN? ¿Por qué la diferencia?
4. **[Qué pasa si]** Entrenás una CNN con fotos centradas y la aplicás a fotos donde el objeto está
   en una esquina. ¿Anda? ¿Y si las fotos de prueba están rotadas 90°? *(La invariancia traslacional
   sí; la rotacional no viene gratis: es un matiz excelente.)*
5. **[Leer una figura]** Se muestran cuatro filtros 3x3 con sus valores y cuatro mapas de
   activación, para aparear.
6. **[Cuenta]** ¿Cuántos parámetros tiene una capa convolucional con 16 filtros de 3x3 sobre una
   imagen en escala de grises (contando sesgos)? *(16·9 + 16 = 160.)* Comparar con una capa densa
   de 784→16.
7. **[MC]** ¿Por qué las capas profundas detectan cosas más complejas?
8. **[Aplicación]** Tenés una base de encuesta con 60 columnas. ¿Tiene sentido usar una CNN?
   Justificá en términos de supuestos.
9. **[Aplicación]** Querés clasificar 5.000 fotos de un archivo histórico en tres categorías.
   ¿Qué necesitás como mínimo antes de empezar? *(Etiquetas, una partición honesta, y una idea de
   cuál es el baseline.)*
10. **[Lectura crítica]** Se da un resumen de un estudio que predice pobreza desde imágenes
    satelitales con R²=0.75. Escribí las tres preguntas de la slide 29 aplicadas a este caso.
11. **[Criterio / ética aplicada]** Una ONG propone usar imágenes satelitales para asignar ayuda
    social en zonas sin datos de encuesta. Mencioná **dos riesgos concretos** y **una salvaguarda**
    que exigirías antes de que se implemente. *(Se busca: que el modelo puede estar midiendo un
    proxy que se rompe en otra región; que los errores no se distribuyen al azar sino que se
    concentran en poblaciones específicas; y como salvaguarda, validación con datos de terreno en
    la región de aplicación, más un mecanismo de apelación humana.)*

---

## 8. Referencias

**Para el estudiante:**
- Jean, N. et al. (2016), *Combining satellite imagery and machine learning to predict poverty*,
  Science 353(6301). **Lectura obligatoria de la clase.** `[VERIFICAR]`
- Un video corto e ilustrado sobre convoluciones (3Blue1Brown tiene uno sobre la operación de
  convolución en general, muy claro). `[VERIFICAR URL]`
- Olah, C. et al., *Feature Visualization* (Distill.pub, 2017) — para mirar las imágenes de la
  jerarquía de verdad. `[VERIFICAR URL]`

**Para el docente:**
- Torres, J. & Cantú, F. (2022), sobre uso de imágenes satelitales y visión por computadora en
  ciencia política — verificar título y disponibilidad; hay literatura reciente en *Political
  Analysis* sobre CNN aplicadas a datos electorales y de conflicto. `[VERIFICAR]`
- Cantú, F. (2019), *The Fingerprints of Fraud: Evidence from Mexico's 1988 Presidential Election*,
  APSR — usa una CNN sobre imágenes de actas electorales para detectar alteraciones. **Es el mejor
  ejemplo existente de CNN haciendo ciencia política de verdad** y conviene mostrarlo aunque sea
  brevemente. `[VERIFICAR]`
- Grimmer, Roberts & Stewart, *Text as Data*, para el marco de "medición" que se retoma en la
  clase 10. `[VERIFICAR]`
- Sobre la superioridad de los métodos de árboles en datos tabulares: Grinsztajn, Oyallon &
  Varoquaux (2022), *Why do tree-based models still outperform deep learning on tabular data?*
  **Sustenta el cartel honesto de la viz 3.4.** `[VERIFICAR]`
