# Clase 9 — Usar modelos que ya existen, sin creerles
**Directorio:** `clases/09-modelos-preentrenados/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-8 · **Apertura del módulo 3**
**Red:** este notebook **sí necesita internet** (descarga modelos de Hugging Face). Debe tener un
modo degradado documentado para cuando no haya red, usando embeddings locales de la clase 6.

---

## 1. Narrativa de la clase

Cambia el registro del curso. Hasta acá construimos para entender; a partir de acá usamos para
investigar. Y la clase tiene una tensión deliberada: **la parte de hacerlo andar es fácil y corta;
la parte de saber si anda bien es difícil y larga.** El reparto de tiempo tiene que reflejar eso —
si el equipo que construye la clase le dedica 90 minutos a Hugging Face y 20 a evaluación, arruinó
la clase. Es al revés.

El hilo:

1. **Tres líneas de código.** Se baja un modelo y se clasifican 5.000 titulares en 40 segundos.
   Asombro genuino, merecido. Y de inmediato: **"¿cómo sabés que está bien?"** Nadie tiene la
   respuesta. Ese hueco es la clase.
2. **Por qué funciona: transfer learning.** El modelo ya aprendió español —gramática, semántica,
   colocaciones— en un corpus gigantesco. Vos sólo tenés que enseñarle **tu** distinción, que es
   una capa fina arriba de todo eso. Callback a la jerarquía de la clase 5: las capas de abajo son
   genéricas, las de arriba son específicas. Por eso se congelan las de abajo.
3. **Las tres estrategias, con su regla de decisión.** No es "cuál es la mejor" sino "cuál según
   cuántas etiquetas tengas": (a) **embeddings + clasificador simple** (50-500 etiquetas, barato,
   interpretable, corre en CPU); (b) **zero-shot / LLM con prompt** (0 etiquetas para entrenar, las mismas 200-300 para evaluar; útil para explorar
   y para el primer pase, hay que validar igual); (c) **fine-tuning** (300+ etiquetas, mejor
   desempeño, más costo). Esta regla de decisión es uno de los entregables prácticos de la clase.
4. **Modelos en español.** Que no usen un modelo en inglés sobre texto en español, que pasa. BETO,
   RoBERTuito, modelos multilingües, y la advertencia de que el desempeño en español suele estar por
   debajo del reportado en inglés.
5. **El giro: evaluar.** La segunda mitad de la clase. Etiquetar a mano una muestra, la matriz de
   confusión, precisión y recall traducidos al problema sustantivo, el baseline tonto, y —el punto
   que esta audiencia entiende mejor que nadie— **el acuerdo entre codificadores humanos como techo
   realista**, medido con la misma métrica que el modelo (el F1 de un codificador contra el otro, no el
   kappa, que está en otra escala). Si dos humanos coinciden con F1 0,80, un modelo con 0,85 contra uno
   de ellos no es "mejor que un humano": es raro, y si pasa, sospechá.
6. **El proyecto chico.** Fine-tuning de verdad sobre titulares etiquetados, con comparación honesta
   contra las alternativas más baratas. Muchas veces la más barata gana, y cuando gana hay que
   decirlo.
7. **El puente.** Tenemos números buenos. ¿Y eso qué prueba? La clase 10.

**Advertencia sobre el registro.** Es la clase donde más riesgo hay de que se convierta en un
tutorial. El antídoto: cada bloque técnico termina con una pregunta de validez. La biblioteca es el
medio; el criterio es el contenido.

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-5 | Tres líneas de código y resultados que costaron una clase entera. |
| 10-25 | Transfer learning | 6-15 | Qué se congela, las tres estrategias, modelos en castellano. |
| 25-45 | Manos 1 | 16 | Notebook: zero-shot sobre el corpus de prensa, sin entrenar nada. |
| 45-55 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 16. |
| 55-75 | Evaluar de verdad | 17-25 | Etiquetar a mano, matriz de confusión, precisión y recall, el baseline tonto. |
| 75-100 | Manos 2: el proyecto chico | 26 | De a dos: clasificar y reportar métricas que un revisor acepte. |
| 100-120 | Cierre | 27-34 | Mirá los errores, qué hay que reportar, `[EN TU INVESTIGACIÓN]`, el puente a la clase 10. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (34 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Usar modelos que ya existen | portada | | |
| 2 | Lo que costó entrenar el de la clase 8 | texto | ~1,5M de parámetros, 10 minutos, 1 MB de texto. Y al lado, la estimación pública para un modelo grande: miles de GPUs, meses, millones de dólares. | "Nadie de esta sala va a entrenar uno desde cero. Ni falta que hace." |
| 3 | **Tres líneas** | código | `from transformers import pipeline` / `clf = pipeline("sentiment-analysis", model="...")` / `clf(titulares)`. | Lo corre en vivo sobre 5.000 titulares. 40 segundos. |
| 4 | Los resultados | figura | Una tabla con 10 titulares y su clasificación, con dos claramente mal. | "Miren estos dos. ¿Están bien?" |
| 5 | **La pregunta** | texto | En grande: **"¿Cómo sabés que está bien?"** | "Esta pregunta separa un paper de un blog post. Y le vamos a dedicar más tiempo que a la biblioteca." |
| 6 | Por qué funciona | figura | Diagrama: un modelo pre-entrenado en 100 GB de español, y arriba una capita fina que es tu tarea. | "Alguien ya le enseñó español. Vos le enseñás tu distinción." |
| 7 | Callback a la clase 5 | figura | La jerarquía: capas de abajo genéricas (bordes / morfología), capas de arriba específicas (objetos / tu categoría). | "Se acuerdan de esto. Es la misma idea, con texto." |
| 8 | Qué se congela | figura | El modelo con las capas de abajo con un candado y la de arriba con un destornillador. | "Congelás lo genérico, reentrenás lo específico. Menos perillas para mover = menos datos necesarios = clase 4." |
| 9 | La metáfora | texto | Un investigador que ya habla el idioma, conoce el país y sabe hacer trabajo de campo. Sólo hay que ponerlo al día con tu tema. Contratás eso, no a alguien desde cero. | "Y como todo informante: sabe muchísimo y tiene sus sesgos. Se lo usa y se lo contrasta." |
| 10 | **Las tres estrategias** | figura | Tabla de decisión: cuántas etiquetas tenés → qué usar. Con costos, requisitos y desempeño esperable. | "Esta tabla se la llevan. Es la decisión práctica que van a tomar de verdad." |
| 11 | Estrategia A: embeddings + clasificador | figura | Texto → vector (modelo pre-entrenado) → regresión logística. | "El clasificador es de estadística clásica y es **interpretable**. Corre en tu notebook. Con 200 etiquetas anda sorprendentemente bien y es mi primera recomendación siempre." |
| 12 | Estrategia B: zero-shot | figura | Se le describe la categoría con palabras y clasifica sin ejemplos. | "Cero etiquetas para entrenar; para evaluar, las mismas que cualquier otra. Mágico y poco confiable. Excelente para explorar; hay que validarlo igual que todo lo demás." |
| 13 | Estrategia C: fine-tuning | figura | Se reentrena el modelo con tus ejemplos. | "El mejor desempeño si tenés unos cientos de ejemplos bien etiquetados." |
| 14 | ¿Cuántas etiquetas hacen falta? | VIZ | `viz/zero-shot-vs-finetune.html`. | "Miren la curva: los primeros 100 ejemplos etiquetados valen muchísimo. Del 500 al 1000, mucho menos. **Etiquetar bien 200 casos vale más que cualquier prompt ingenioso.**" |
| 15 | Modelos en español | texto | BETO, RoBERTuito (entrenado en tuits en español), modelos multilingües. Y la advertencia: el desempeño reportado en inglés no transfiere. | "Si usan un modelo entrenado en inglés sobre texto en castellano, va a andar y va a andar mal. Y no se van a dar cuenta si no evalúan." |
| 16 | Bloque práctico 1 | texto | Consignas: pipeline, embeddings, búsqueda semántica. | "25 minutos." |
| 17 | Búsqueda semántica | VIZ | `viz/similitud-semantica.html`. | "Buscás por significado, no por palabra. Esto solo ya te cambia el trabajo con corpus grandes." |
| 18 | **Segunda parte: evaluar** | portada de sección | | "Ahora sí, lo importante." |
| 19 | Primero: etiquetá a mano | texto | Una muestra al azar de 200-300 casos, etiquetada por vos (mejor: por dos personas). **Sin mirar lo que dijo el modelo.** | "Sí, a mano. No hay atajo. Es la parte más aburrida y es la que hace que tu trabajo sea investigación." |
| 20 | La matriz de confusión | figura | La matriz 2x2 con los cuatro casilleros nombrados en el problema sustantivo, no en abstracto. | "Cuatro números. Y cada uno significa algo distinto para tu pregunta." |
| 21 | **Movés el umbral** | VIZ | `viz/matriz-de-confusion.html`. | "Miren: si bajo el umbral, agarro más protestas de verdad y también más falsas alarmas. **No podés tener las dos cosas de forma sostenida** (la precisión puede dar algún saltito, el recall nunca baja). Elegir el umbral es elegir qué error preferís, y eso es la clase 3 otra vez." |
| 22 | Precisión y recall, en castellano | texto | **Precisión**: de lo que el modelo llamó X, cuánto era X de verdad. **Recall**: de todo lo que era X, cuánto encontró. Con la frase operativa de cada uno en el problema del corpus de prensa. | "Nunca digan 'precisión de 0.83'. Digan 'de cada 100 notas que el modelo llamó protesta, 83 lo eran'. Si no lo pueden decir así, no lo entendieron." |
| 23 | ¿Cuál te importa más? | texto | Depende de la pregunta: para estimar una **prevalencia** te importan los dos y su balance; para armar un corpus que después vas a leer, te importa el recall; para hacer una afirmación fuerte sobre casos concretos, la precisión. | "Otra vez: es una decisión de investigación, no una métrica que se optimiza sola." |
| 24 | El baseline tonto | figura | Un corpus donde el 92% son "no protesta". Un modelo que dice "no protesta" siempre saca 92% de accuracy. | "Si su clase mayoritaria es el 92%, el 93% de accuracy es un desastre y suena bien. **Siempre reporten el baseline.**" |
| 25 | El techo humano | texto | Acuerdo entre codificadores: se reporta con kappa de Cohen, pero el techo se compara en la **misma métrica** que el modelo (el F1 de un codificador contra el otro). Si dos humanos coinciden con F1 0,78, ese es tu techo realista. | "Y si el modelo saca 0,95 donde dos humanos coinciden en 0,78, **no festejen: busquen el error**. Muchas veces hay una fuga de datos." |
| 26 | Bloque práctico 2: el proyecto chico | texto | Consignas: fine-tuning, comparación honesta, matriz de confusión, análisis de errores. | "40 minutos. De a dos." |
| 27 | Resultados del aula | discusión | Poner en común. | "¿A quién le ganó la regresión logística sobre embeddings al fine-tuning? Levanten la mano. Eso pasa seguido y hay que reportarlo." |
| 28 | Mirá los errores | texto | Los falsos positivos y falsos negativos son donde está el conocimiento: te dicen qué entendió el modelo por tu categoría. | "Leer 30 errores del modelo te enseña más sobre tu propia definición operativa que leer 300 aciertos." |
| 29 | Lo que hay que reportar | texto | Checklist: modelo y versión exactos, cantidad de datos etiquetados y por quién, partición, baseline, métricas con intervalos, matriz de confusión, y ejemplos de errores. | "Esto es la sección de métodos. Se los damos hecho en la clase 10." |
| 30 | `[EN TU INVESTIGACIÓN]` | texto | La receta completa en 7 pasos, imprimible: definí la categoría → etiquetá 300 al azar → medí el acuerdo entre dos codificadores → elegí estrategia según cuántas etiquetas tengas → evaluá en test → mirá los errores → reportá. | "Con esto, la próxima vez que se sienten con su corpus, lo clasifican. En serio. No es tarea para la clase que viene: es un proyecto de mediano plazo." |
| 31 | Cuando el modelo no es la respuesta | texto | Si tenés 200 documentos, leelos. Si tu categoría es ambigua para dos humanos, ningún modelo la va a resolver: el problema es la definición, no la herramienta. | "El mejor consejo de la clase: si dos codificadores no se ponen de acuerdo, no tenés un problema de modelo. Tenés un problema de concepto." |
| 32 | Lo que falta | texto | Tenemos un número bueno. ¿Prueba que medimos lo que decimos? | "No. Y esa es la última clase." |
| 33 | El puente | texto | "Clase 10: validez, sesgo, reproducibilidad, y el revisor 2." | |
| 34 | Glosario de hoy | texto | transfer learning, fine-tuning, congelar capas, zero-shot, few-shot, pipeline, embeddings de oración, matriz de confusión, precisión, recall, F1, baseline, kappa, umbral. | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/matriz-de-confusion.html` — **la viz central de la clase**
- **Qué se ve.** Un corpus simulado de 500 notas de prensa representadas como puntos, cada una con
  un "puntaje" del modelo (eje horizontal) y su clase verdadera (color). Una **línea vertical de
  umbral** arrastrable. A la derecha, la matriz de confusión 2x2 que se actualiza en vivo, con los
  cuatro casilleros rotulados **en el problema sustantivo** ("notas de protesta bien detectadas",
  "notas que no eran protesta y el modelo marcó", etc.). Debajo, precisión, recall, F1 y accuracy,
  **cada uno con su frase en castellano llano** que se actualiza con los números.
- **Controles.**
  - **Umbral arrastrable** (el control principal).
  - Slider de **prevalencia** de la clase positiva (del 50% al 3%). **Este control es el que produce
    el aha más importante.**
  - Slider de **calidad del modelo** (cuánto se separan las dos distribuciones).
  - Toggle "mostrar el baseline tonto" que agrega una barra con la accuracy de "decir siempre la
    clase mayoritaria".
- **Qué tiene que hacer clic.** Dos cosas: (1) precisión y recall se mueven en direcciones opuestas
  y no hay umbral que mejore ambos de forma sostenida; (2) **con clases desbalanceadas, la accuracy es una medida
  inútil**, y la precisión se derrumba aunque el modelo sea el mismo.
- **Momento aha.** Bajar la prevalencia al 5% sin tocar nada más: la accuracy casi no se mueve (!) y la precisión
  se desploma. "El modelo es exactamente el mismo. Cambió sólo cuán raro es el fenómeno. Y por eso
  detectar cosas raras es mucho más difícil de lo que parece."
- **Detalle.** Un panel "traducción a tu paper" que arma la oración: *"El clasificador identificó
  N notas como protesta, de las cuales aproximadamente P% lo eran efectivamente, y capturó R% del
  total de notas de protesta presentes en el corpus."* Copiable. Es un entregable práctico.

### 3.2 `viz/similitud-semantica.html`
- **Qué se ve.** Un campo de búsqueda y un corpus de ~300 titulares. Al escribir una consulta, se
  rankean los titulares por similitud coseno con la consulta, mostrando el puntaje.
- **Controles.** Campo de búsqueda libre. Toggle **"búsqueda por palabra clave"** vs **"búsqueda
  semántica"**, mostrando los dos rankings lado a lado.
- **Qué tiene que hacer clic.** Que la búsqueda semántica encuentra documentos que **no contienen
  la palabra buscada** — y que eso es exactamente lo que resuelve el problema clásico de armar un
  corpus con una lista de términos (que siempre deja afuera lo que no se te ocurrió).
- **Momento aha.** Buscar "protesta" y encontrar titulares sobre "corte de ruta", "movilización",
  "reclamo frente a la sede". "Esto es lo que su búsqueda por palabras clave venía perdiendo."
- **Contrapunto obligatorio.** Un botón **"mostrar los falsos positivos"** que revela los casos que
  la búsqueda semántica trae y no corresponden (una nota sobre "reclamo publicitario", por ejemplo).
  La viz no puede ser sólo propaganda de la técnica.

### 3.3 `viz/zero-shot-vs-finetune.html`
- **Qué se ve.** Un gráfico de líneas: eje X = cantidad de ejemplos etiquetados (0 a 2000, escala
  log), eje Y = F1. Tres curvas: zero-shot (línea horizontal, no mejora con datos),
  embeddings + regresión logística (sube rápido y se aplana), fine-tuning completo (arranca peor con
  pocos datos, después supera). Con bandas de incertidumbre.
- **Controles.** Slider de **"cuántas etiquetas puedo producir"**: al moverlo, se marca la línea
  vertical y **se ilumina cuál de las tres estrategias conviene ahí**, con un cartel de
  recomendación y una estimación de costo en horas de codificación.
- **Qué tiene que hacer clic.** Que la decisión de estrategia es una función de un recurso que
  ellos controlan (horas de codificación), no de cuál técnica está de moda.
- **Momento aha.** Ver el cruce: con menos de ~150 etiquetas, fine-tuning es **peor** que la
  regresión logística sobre embeddings. "Más sofisticado no es mejor cuando tenés pocos datos.
  Es la clase 4 otra vez: capacidad contra datos."
- **Honestidad.** Las curvas tienen que provenir de un experimento real corrido por el equipo sobre
  el corpus del curso, con el notebook que lo genera incluido. Si no se puede, se rotula
  explícitamente como esquemática y se cita literatura que sustente la forma.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** ~12 min en CPU (el fine-tuning es el grueso: 3 epochs sobre 800 ejemplos
con un modelo chico). **Requiere internet.** **Dependencias:** transformers, torch, datasets,
scikit-learn, pandas.
**Modo degradado sin red:** documentado en la primera celda; se usan los embeddings de la clase 6 y
una regresión logística, y se saltean las celdas de HF.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Objetivo. Advertencia de red y del modo degradado. | |
| 2 | code | Instalación (`pip install transformers datasets`) y verificación de conexión con un mensaje claro si falla. | |
| 3 | code | Carga del corpus de titulares con etiquetas (Aguasclaras prensa: ~1200 titulares etiquetados en 2 categorías). Distribución de clases. **Se imprime el baseline de clase mayoritaria de entrada.** | Que el baseline esté antes que cualquier modelo, para que sea la vara desde el principio. |
| 4 | md | **Tres líneas.** | |
| 5 | code | `pipeline()` con un modelo de sentimiento en español sobre 20 titulares. Tabla de resultados. | |
| 6 | md | `TODO 1` — Leé los 20 resultados y marcá cuáles te parecen mal. ¿Cuántos son? *Pista: ojo con la ironía y con los titulares que informan sobre algo negativo sin valorarlo.* | La evaluación empieza a mano, en el minuto 5. Deliberado. |
| 7 | md | **Embeddings de oración.** | |
| 8 | code | Cargar un modelo de embeddings de oración en español, vectorizar los 1200 titulares. Mostrar la forma de la matriz resultante. | |
| 9 | code | Búsqueda semántica: función `buscar(consulta, k)`. Probar con 3 consultas. Comparar con búsqueda por substring. | |
| 10 | md | `TODO 2` — Buscá algo de tu propio interés y compará los dos métodos. ¿Qué encontró la búsqueda semántica que la de palabras perdió? ¿Y qué trajo de más? | Los dos lados, siempre. |
| 11 | md | **Estrategia A: embeddings + regresión logística.** | |
| 12 | code | Partición train/test **estratificada** (callback a la clase 4). Entrenar `LogisticRegression` sobre los embeddings. Reportar accuracy, precisión, recall, F1, matriz de confusión. | La estrategia más simple, primero. Es un mensaje. |
| 13 | code | Imprimir la matriz de confusión con etiquetas sustantivas y las frases en castellano llano generadas automáticamente. | Función reutilizable `reportar(y_true, y_pred)` que el estudiante se lleva. |
| 14 | md | `TODO 3` — Compará contra el baseline de clase mayoritaria. ¿Cuánto ganó realmente el modelo? | |
| 15 | md | **Estrategia B: zero-shot.** | |
| 16 | code | Clasificación zero-shot con descripciones de categoría. Mismas métricas. Comparación en una tabla. | Suele perder. Hay que mostrarlo. |
| 17 | md | **Estrategia C: fine-tuning.** | |
| 18 | code | Fine-tuning de un modelo chico en español, 3 epochs, con curva de loss de train y validación. | **Se señala que es el mismo training loop de la clase 4**, ahora escondido detrás de `Trainer` — y se muestran las dos versiones para que la abstracción no sea magia. |
| 19 | code | Evaluación en el mismo test. Tabla comparativa final de las tres estrategias + baseline. | |
| 20 | md | `TODO 4` — ¿Cuál ganó? ¿La diferencia justifica el costo computacional y de tiempo? Escribí tu recomendación para un colega con tu mismo corpus. | La pregunta profesional, no la técnica. |
| 21 | md | **La curva de cuántas etiquetas.** | |
| 22 | code | Entrenar la estrategia A con 25, 50, 100, 200, 400, 800 ejemplos y graficar F1 vs cantidad. | Genera la curva de la viz 3.3 con sus propios datos. |
| 23 | md | `TODO 5` — ¿A partir de cuántas etiquetas deja de mejorar mucho? Traducí eso a horas de codificación (estimá 30 segundos por titular). | Convierte una curva en una decisión de presupuesto. |
| 24 | md | **Mirá los errores.** | |
| 25 | code | Imprimir los 15 falsos positivos y los 15 falsos negativos, con el texto completo. | |
| 26 | md | `TODO 6 (el importante)` — Leé los 30 errores. Escribí: (a) ¿tienen algo en común? (b) ¿alguno está en realidad **bien clasificado** y la etiqueta humana estaba mal? (c) ¿qué te dice esto sobre tu definición de la categoría? | El (b) es clave: casi siempre pasa, y descubrirlo cambia la relación con las métricas para siempre. |
| 27 | md | **Acuerdo entre codificadores.** | |
| 28 | code | Se dan dos columnas de etiquetas humanas sobre los mismos 100 casos (incluidas en los datos) y se calcula el porcentaje de acuerdo y el kappa de Cohen. Se compara con el desempeño del modelo. | |
| 29 | md | `TODO 7 (criterio)` — Si el kappa entre humanos es 0.71 y tu modelo saca F1 0.88 contra las etiquetas de uno solo de ellos, ¿qué está pasando? ¿Qué reportarías? | Excelente pregunta de discusión: puede ser fuga, puede ser que el modelo aprendió el estilo de ese codificador. |
| 30 | md | **Guardar y reutilizar** el modelo. Y una función `clasificar_corpus(textos)` lista para que la usen con sus datos. | Entregable práctico real. |
| 31 | md | **Para llevarte**: la receta de 7 pasos + puente a la clase 10. | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Anda porque el output tiene sentido"** | Validan leyendo 5 casos que salieron bien. | Se muestra que 5 casos elegidos por uno mismo no son una muestra. Se exige la muestra al azar etiquetada a ciegas. |
| **Confundir accuracy con desempeño** | Reportan 93% en un corpus con 92% de clase mayoritaria. | Viz 3.1 con el slider de prevalencia. Es la lección más transferible de la clase. |
| **Confundir precisión con recall** | Los usan indistintamente. | Se prohíbe decir el número sin la frase en castellano. La regla del curso: si no podés decir "de cada 100 que el modelo llamó X, N lo eran", no lo entendiste. |
| **"El modelo es mejor que los codificadores humanos"** | Festejan un F1 alto. | El techo del acuerdo humano, en la misma métrica que el modelo. Un modelo que lo supera claramente es raro: sospechá que mide otra cosa, o que hay fuga. |
| **Usar modelos en inglés sobre texto en español** | Muy frecuente, porque son los que aparecen primero en los tutoriales. | Se muestra en vivo el mismo texto clasificado por un modelo en inglés y uno en español. |
| **Fine-tuning como default** | Creen que es "la manera correcta". | Viz 3.3 y la tabla comparativa del notebook. No es el default: se elige según cuántas etiquetas tenés, y cuesta más cómputo que las otras dos estrategias. |
| **No mirar los errores** | Terminan en la métrica. | El TODO 6, que casi siempre revela etiquetas humanas mal puestas. Es la experiencia que cambia el hábito. |
| **Creer que zero-shot no necesita validación** | "Como no entrené nada, no hay sobreajuste." | Hay que validar **más**, no menos: no tenés ni idea de qué entendió el modelo por tu categoría. Y probar varios prompts y quedarse con el mejor **es** ajustar contra el test. |
| **Ignorar la versión del modelo** | Escriben "usamos BERT". | Los modelos se actualizan y se despublican. Hay que fijar la versión exacta (el hash del commit en HF). Se retoma en la clase 10. |
| **Etiquetar mirando la predicción del modelo** | Contaminan el gold standard. | Regla explícita: se etiqueta **a ciegas**, antes de ver nada. Es el mismo principio del doble ciego. |

---

## 6. Analogías y metáforas de ciencias sociales

- **El informante clave.** Un modelo pre-entrenado sabe muchísimo del terreno y te ahorra meses; y
  como todo informante, tiene su posición, sus puntos ciegos y su manera de nombrar las cosas.
  Se lo usa, se lo cita con precisión (versión incluida) y se lo triangula.
- **El equipo de codificadores.** El fine-tuning es entrenar un codificador: le mostrás ejemplos,
  aprende tu libro de códigos, y después codifica el resto. Todo lo que sabemos de la codificación
  humana aplica: hace falta acuerdo inter-codificador, hace falta un manual explícito, y hace falta
  revisar los casos límite.
- **El acuerdo humano como techo.** El acuerdo inter-codificador (reportado con kappa; comparado con el modelo en la misma métrica) es un límite epistemológico, no un detalle
  de calidad: si dos expertos no coinciden, la categoría no está bien definida, y ninguna máquina va
  a resolver un problema conceptual. Este es probablemente el punto más valioso que un cientista
  social aporta a un equipo de ML, y hay que decírselo así.
- **El muestreo y la prevalencia.** Detectar un fenómeno raro con un instrumento imperfecto es un
  problema clásico de epidemiología: con baja prevalencia, aun un test muy bueno produce
  mayoritariamente falsos positivos. Es exactamente el aha de la viz 3.1 y tiene un siglo de
  literatura detrás.
- **El diccionario validado.** Muchos en el aula usaron LIWC o diccionarios de sentimiento. La
  discusión sobre su validez en español y en contexto es la misma discusión de hoy, con más
  parámetros. Reconocerlo les da autoridad sobre el tema en vez de quitársela.
- **La operacionalización, otra vez.** Volvemos al punto de la clase 1: antes del modelo hay una
  decisión de medición. El modelo no define qué es "protesta": vos lo definís, y el modelo lo
  reproduce con sus propias distorsiones.

---

## 7. Cuestionario: temas a evaluar (12 ítems)

1. **[MC conceptual]** ¿Qué es transfer learning y por qué permite usar menos datos?
2. **[MC conceptual]** ¿Qué significa congelar capas?
3. **[Leer un gráfico]** Una matriz de confusión con números. Calcular precisión y recall y
   **escribir las dos frases en castellano llano**.
4. **[Leer un gráfico]** Un corpus con 4% de clase positiva y un modelo con 96% de accuracy.
   ¿Es bueno? Justificar.
5. **[Qué pasa si]** Bajás el umbral de clasificación. ¿Qué le pasa a la precisión? ¿Y al recall?
   ¿En qué situación de investigación preferirías cada uno?
6. **[Qué pasa si]** Tenés 60 documentos etiquetados. ¿Qué estrategia elegís y por qué? ¿Y con 3.000?
7. **[MC]** ¿Por qué no conviene usar un modelo entrenado en inglés sobre un corpus en español?
8. **[Aplicación]** Tenés 20.000 notas de prensa y querés identificar las que mencionan conflicto
   laboral. Describí el procedimiento completo, incluyendo cuántas etiquetás a mano y cómo evaluás.
9. **[Interpretación]** El acuerdo entre dos codificadores humanos es kappa 0.65. Tu modelo saca
   F1 0.92 contra las etiquetas de uno de ellos. Nombrá dos explicaciones posibles y cómo
   distinguirías entre ellas.
10. **[Análisis de errores]** Se dan 6 falsos positivos de un clasificador de "protesta". Identificar
    qué patrón sistemático los une y qué implica para la definición de la categoría.
11. **[Reporte]** Escribí las tres oraciones de la sección de métodos que reportan un clasificador,
    con todos los elementos necesarios para que otro pueda replicarlo.
12. **[Criterio / ética aplicada]** Un organismo público quiere usar un clasificador de "riesgo" sobre
    denuncias ciudadanas para priorizar cuáles atender primero. El modelo tiene F1 de 0.85.
    (a) ¿Qué métrica te preocupa más y por qué? (b) ¿Qué pasa con las denuncias que el modelo
    despriorizó y nadie leyó nunca? (c) ¿Qué mecanismo exigirías antes de que se implemente?
    *(Se busca: recall sobre casos graves; el problema del **feedback invisible** —los falsos
    negativos nunca se descubren, así que el sistema parece funcionar mejor de lo que funciona—;
    y como salvaguarda, auditoría por muestreo de los casos despriorizados, más revisión humana.)*

---

## 8. Referencias

**Para el estudiante:**
- Hugging Face, curso oficial de NLP, capítulos 1-3 (hay versión en español). `[VERIFICAR URL]`
- Cañete, J. et al. (2020), *Spanish Pre-Trained BERT Model and Evaluation Data* (BETO).
  `[VERIFICAR]`
- Pérez, J.M. et al., *pysentimiento* / RoBERTuito — herramientas para análisis de texto en español
  rioplatense, muy pertinentes para esta audiencia. `[VERIFICAR]`

**Para el docente:**
- Grimmer, J., Roberts, M. & Stewart, B. (2022), *Text as Data*, especialmente los capítulos sobre
  clasificación supervisada y validación. `[VERIFICAR]`
- Grimmer, J. & Stewart, B. (2013), *Text as Data: The Promise and Pitfalls of Automatic Content
  Analysis Methods for Political Texts*, Political Analysis. **La consigna "validate, validate,
  validate" de este paper es el lema de la clase.** `[VERIFICAR]`
- Krippendorff, K., *Content Analysis*, para el marco de fiabilidad entre codificadores.
  `[VERIFICAR]`
- Barberá, P. et al. (2021), *Automated Text Classification of News Articles: A Practical Guide*,
  Political Analysis. **Es prácticamente el manual de esta clase**, incluida la discusión de cuántos
  documentos etiquetar. `[VERIFICAR]`
