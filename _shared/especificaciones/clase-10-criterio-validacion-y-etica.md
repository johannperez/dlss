# Clase 10 — Criterio: validez, sesgo, reproducibilidad y el revisor 2
**Directorio:** `clases/10-criterio-validacion-y-etica/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-9 · **Cierre del curso**

> **Nota de construcción.** La clase construida cambió el gancho de esta especificación: en vez de la
> "agresividad" con F1 0,91 y la palabra "gobierno", usa un clasificador de "esta nota es sobre
> política" (F1 0,68) que, aplicado a 824 oraciones de discursos presidenciales argentinos, encuentra 22 de
> cada 100. Donde esta especificación y la clase difieran, manda la clase (`PROGRAMA.md` §0.2).

---

## 1. Narrativa de la clase

Si el curso tuviera una sola clase, sería esta. Todo lo anterior existe para que esta se pueda dar
con autoridad: no se puede discutir con criterio la validez de un modelo que uno no entiende, y por
eso hicimos nueve clases de mecanismo. Hoy se cobra.

La tesis de la clase es una sola: **hacer andar el modelo es lo fácil y lo barato; demostrar qué es
lo que mide es el trabajo profesional.** Un cientista social que sale de acá aporta a un equipo de
ML algo que la formación técnica no da: la pregunta por la validez, la sospecha ante la métrica
linda, y la conciencia de que toda medición es una decisión con consecuencias.

El hilo:

1. **El hallazgo hermoso y falso.** El gancho tiene que doler: un resultado que todos publicarían,
   con la métrica alta y la serie temporal limpia, y el pliegue que lo destruye. Y la parte
   importante: **el modelo no falló**. Hizo exactamente lo que se le pidió. Falló la inferencia
   sustantiva que le colgamos encima.
2. **Desempeño ≠ validez.** La distinción central. Se trae el vocabulario que ellos ya tienen —
   validez de constructo, de contenido, externa — y se muestra que la literatura de ML lo redescubre
   con otros nombres y peor. Este es un momento en el que la disciplina de la audiencia tiene
   **ventaja** sobre el campo técnico, y hay que decírselo con todas las letras: les sube la
   autoridad y les cambia la relación con la herramienta.
3. **Cómo se valida, operativamente.** No como principio abstracto sino como procedimiento:
   lectura de una muestra estratificada, análisis sistemático de falsos positivos, test de placebo,
   test de casos límite construidos a mano, y validación externa contra una medida independiente.
4. **La auditoría de sesgo, hecha.** No se discute el sesgo: **se mide**, en el notebook, con un
   procedimiento que produce una tabla reportable. Y se distinguen tres cosas que se confunden todo
   el tiempo: sesgo del mundo, sesgo del corpus, y sesgo introducido por el modelado.
5. **Reproducibilidad práctica.** Semillas, versiones, datos, código, ficha del modelo. Y el
   problema específico y grave de los modelos cerrados que cambian sin aviso: un resultado obtenido
   con una API en marzo puede no reproducirse en junio.
6. **Ética aplicada, sin sermón.** Datos personales, scraping, consentimiento, riesgo de
   re-identificación, y la pregunta de para qué se va a usar el resultado. Formato: casos concretos
   y discutibles, no principios.
7. **El juicio.** La actividad final: media aula defiende un paper, media lo revisa. Es evaluación,
   es síntesis y es divertido.
8. **Cuándo NO usar deep learning.** La slide más honesta del curso, y la que más credibilidad da.
9. **El cierre.** El mapa completo, de la perilla al transformer, y la frase final.

`[CALLBACK DIBUJO — el cierre]` — "Durante diez clases aprendimos a dibujar. Hoy aprendimos a
pararnos frente a un dibujo y preguntar: **¿de qué es esto un dibujo?** Un modelo siempre dibuja
algo. Tu trabajo es demostrar qué."

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-6 | «El hallazgo»: un resultado que parece un descubrimiento y no lo es. |
| 10-30 | Validez de constructo | 7-19 | Los tres tipos de validez y las cinco maneras de validar en serio. |
| 30-50 | Manos 1: auditoría de sesgo | 20 | Notebook: medir el sesgo sobre el corpus de prensa. |
| 50-60 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 20. |
| 60-75 | Reproducibilidad y ética práctica | 21-27 | El checklist, los modelos cerrados, los casos y los criterios que sí sirven. |
| 75-100 | Manos 2: **el juicio** | 28-30 | Se defiende y se acusa un paper, y el aula dicta veredicto. |
| 100-115 | La caja de herramientas completa | 31-35 | Cuándo NO usar deep learning, qué le decís a un revisor, el mapa del curso. |
| 115-120 | Cierre del curso | 36 | El cierre. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (36 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Criterio | portada | | |
| 2 | **El hallazgo** | figura | Un gráfico precioso: "agresividad del discurso opositor" subiendo sostenidamente 2010-2023, con banda de confianza. Al costado: F1 = 0.91, n = 45.000 discursos. | "Esto lo publicás. Yo lo publico. ¿Alguien tiene una objeción?" |
| 3 | El pliegue | figura | El análisis de qué pesa más en la decisión del modelo: la palabra **"gobierno"**. Y un gráfico secundario: la frecuencia de "gobierno" en el discurso opositor sube igual. | "El modelo aprendió a detectar una palabra que la oposición usa más. La serie es real. La métrica es real. El hallazgo es falso." |
| 4 | El modelo no falló | texto | Hizo exactamente lo que le pedimos: separar dos grupos de textos. Lo que falló fue la etiqueta sustantiva que le pusimos al resultado. | "Este es el error que vamos a atacar hoy, y no se arregla con más datos ni con un modelo mejor." |
| 5 | Dos preguntas distintas | texto | **¿Acierta?** (desempeño) vs **¿Mide lo que digo que mide?** (validez). Un modelo puede tener desempeño perfecto y validez nula. | "El módulo pasado fue sobre la primera. Hoy es sobre la segunda, que es la difícil." |
| 6 | Ustedes tienen ventaja | texto | Validez de constructo, de contenido, externa, criterial: vocabulario de las ciencias sociales desde hace 70 años. La literatura de ML lo está redescubriendo con otros nombres. | "Esto que van a decir en una reunión con ingenieros no lo va a poder decir nadie más. Es su aporte, y es más valioso que saber PyTorch." |
| 7 | Validez de constructo | figura | Diagrama: el concepto ("agresividad") ↔ la medida (el clasificador). La brecha entre ambos. | "¿La cosa que medís es la cosa de la que hablás?" |
| 8 | **Tres casos** | VIZ | `viz/validez-de-constructo.html`. | Recorre los tres. "En los tres, la métrica es buena y la conclusión es falsa. Por razones distintas." |
| 9 | Validez de contenido | texto | ¿Tu medida cubre todas las dimensiones del concepto, o sólo la más fácil de detectar? | "Si 'polarización' incluye tono, contenido y estructura de la interacción, y tu modelo sólo ve tono, medís un tercio y lo llamás por el nombre completo." |
| 10 | Validez externa | texto | ¿Funciona fuera del corpus, del período, del país donde lo entrenaste? | "El corpus de entrenamiento es su muestra. Todo lo que saben de validez externa aplica igual." |
| 11 | Cómo se valida, en la práctica | texto | Cinco procedimientos concretos, numerados. Esta es la slide que fotografían. | "Ninguno es opcional en un paper serio." |
| 12 | 1. La muestra leída a mano | texto | 100-200 casos al azar (estratificados por la predicción del modelo), leídos y etiquetados a ciegas. | "Sí, otra vez a mano. Es la parte cara y es la que hace investigación." |
| 13 | 2. Los falsos positivos | texto | Leer 30 falsos positivos te dice qué entendió el modelo por tu categoría. Es análisis cualitativo sobre errores cuantitativos. | "Ahí está el conocimiento. Los aciertos no te enseñan nada." |
| 14 | 3. El test de placebo | figura | Aplicar el modelo a un corpus donde el fenómeno **no debería** aparecer. Si aparece igual, tenés un problema. | "Si tu detector de discurso de odio marca el boletín oficial, algo pasa." |
| 15 | 4. Casos límite construidos a mano | figura | Pares mínimos: la misma oración cambiando una palabra clave. Se ve si el modelo cambia por lo que debería cambiar. | "Es un experimento, no una observación. Y es más informativo que 10.000 casos observacionales." |
| 16 | 5. Validación externa | texto | Contrastar con una medida independiente: datos de encuesta, codificación de otro equipo, un evento conocido. | "Si tu índice de conflictividad no sube en los meses que todos sabemos que hubo conflicto, tenés un problema." |
| 17 | **Auditoría de sesgo** | portada de sección | | |
| 18 | Tres sesgos que no son lo mismo | texto | (a) sesgo **del mundo** (la realidad es desigual); (b) sesgo **del corpus** (tu muestra no representa el mundo); (c) sesgo **introducido** (por el modelado, el umbral, la loss). Cada uno se arregla distinto, y el primero no se "arregla". | "Confundirlos lleva a soluciones absurdas. Si el mundo es desigual y tu modelo lo refleja, el problema no es el modelo: es qué vas a hacer con él." |
| 19 | **Medilo** | VIZ | `viz/sesgo-en-el-espejo.html`. | Cambia el sujeto de una oración y muestra el score cambiando. "Misma estructura, misma valoración, distinto sujeto, distinto score. Y esto es reportable en una tabla." |
| 20 | Bloque práctico 1 | texto | Consignas: la auditoría en el notebook. | "30 minutos. Van a producir una tabla que podrían pegar en un paper." |
| 21 | Cuando el sesgo es el hallazgo | texto | Callback a la clase 6: el mismo instrumento que es dañino para decidir es valioso para medir. | "Depende enteramente de para qué lo usás." |
| 22 | **Reproducibilidad** | portada de sección | | |
| 23 | El checklist | texto | Semilla fijada, versiones exactas (`pip freeze`), datos disponibles o descripción de cómo obtenerlos, código en un repositorio, ficha del modelo con sus limitaciones, prompts exactos en el apéndice. | "Nada de esto es difícil. Es sólo disciplina, y hay que hacerla desde el día uno porque después no se puede reconstruir." |
| 24 | El problema de los modelos cerrados | texto | Un resultado obtenido con una API en marzo puede no reproducirse en junio: el modelo cambió y no te avisaron. Y las versiones viejas se despublican. | "Si su análisis depende de un modelo que puede desaparecer, su paper tiene fecha de vencimiento. Los modelos abiertos con versión fija tienen una ventaja metodológica que no es ideológica: es práctica." |
| 25 | **Ética aplicada** | portada de sección | | |
| 26 | Los casos | discusión | Cuatro casos breves para discutir en 2 minutos cada uno: (1) scrapear perfiles públicos de redes para estudiar polarización; (2) publicar un modelo que identifica autoría de textos anónimos; (3) usar un clasificador de riesgo en una oficina pública; (4) entrenar sobre entrevistas cedidas para otro fin. | "No hay respuesta correcta. Quiero escuchar los argumentos." |
| 27 | Los criterios que sí sirven | texto | ¿Quién soporta el costo del error? ¿El sujeto puede apelar? ¿Habría dado consentimiento para este uso? ¿El resultado se puede re-identificar? ¿A quién le sirve el hallazgo? | "Cinco preguntas. Se las llevan y se las hacen antes de empezar, no antes de publicar." |
| 28 | Bloque práctico 2: **el juicio** | texto | Consignas de la actividad final: se reparte un paper corto, mitad defiende, mitad revisa, 15 min de preparación, 10 de audiencia. | "Los revisores tienen que usar el checklist. Los defensores también, así saben qué les van a preguntar." |
| 29 | El juicio | discusión | La actividad. | El docente modera y anota en el pizarrón las objeciones que aparecen. |
| 30 | Veredicto | discusión | Se ordenan las objeciones por gravedad. ¿Cuáles son fatales y cuáles se arreglan con una revisión menor? | "Esta distinción es la que hace a un buen revisor: no todo problema es fatal, y decir que sí lo es también es un error." |
| 31 | **Cuándo NO usar deep learning** | texto | Seis situaciones: n chico; necesitás coeficientes interpretables para el argumento; una regresión o un diccionario ya resuelve; el costo del error es alto y no hay revisión humana; no tenés cómo validar; el problema es que la categoría está mal definida. | "Si esta lista los hace usar menos deep learning, el curso fue exitoso. En serio." |
| 32 | **Qué le decís a un revisor** | VIZ | `viz/checklist-revisor.html`. | Completa el checklist en vivo y genera el párrafo de métodos. "Esto se lo llevan y lo usan en el próximo paper que escriban." |
| 33 | Las seis objeciones que te van a hacer | texto | (1) ¿Cómo sabemos que mide lo que decís? (2) ¿Cuál es el baseline? (3) ¿Cómo partiste los datos? (4) ¿Cuánta validación humana hay? (5) ¿Es reproducible? (6) ¿Qué pasa con los errores y a quién afectan? | "Las seis. Siempre. Si su paper las contesta en el texto, van a tener una revisión mucho más tranquila." |
| 34 | **El mapa del curso** | figura | Una sola figura con las 10 clases: perilla → composición → loss → ciclo → convolución → embedding → attention → GPT → transfer → criterio. Con la metáfora del dibujo atravesándola. | Lo recorre en tres minutos. "Miren de dónde salieron. La primera clase movíamos dos sliders." |
| 35 | Adónde seguir | texto | Recursos para continuar, comunidades, y la sugerencia principal: **hacé un proyecto chico con tus datos**, no otro curso. | |
| 36 | Cierre | texto | La frase final, sola en la pantalla: **"Lo que aprendiste no es a usar una biblioteca. Es a no dejarte impresionar."** | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/validez-de-constructo.html`
- **Qué se ve.** Tres casos navegables con pestañas. En cada uno: arriba, **la conclusión que el
  investigador quiere sacar**; en el medio, **lo que el modelo efectivamente está usando** (las
  palabras o rasgos más influyentes); abajo, **la evidencia del desfasaje**.
  - **Caso 1 — el atajo léxico.** "Agresividad" que en realidad detecta la palabra "gobierno".
    Evidencia: al eliminar esa palabra del corpus, el desempeño se derrumba.
  - **Caso 2 — el confusor temporal.** Un clasificador de "populismo" que en realidad detecta el
    período (cambió el estilo de redacción de las fuentes en 2015). Evidencia: entrenado en un
    período, se derrumba en el otro.
  - **Caso 3 — la cobertura parcial.** "Polarización" medida sólo por tono, cuando el concepto
    incluye estructura de interacción. Evidencia: dos corpus con el mismo tono y estructuras de
    interacción opuestas reciben el mismo puntaje.
- **Controles.** En cada caso, un botón **"aplicar el arreglo"** (quitar la palabra, entrenar y
  testear en períodos separados, agregar la dimensión faltante) que muestra el resultado corregido —
  que **casi siempre es mucho menos impresionante que el original**. Esa caída es el contenido.
- **Qué tiene que hacer clic.** Que la validez no se testea con una métrica: se testea con
  **intervenciones** sobre los datos y el diseño.
- **Momento aha.** El caso 1: "el F1 pasó de 0.91 a 0.58 cuando le saqué una palabra. Entonces el
  0.91 no era lo que yo pensaba."

### 3.2 `viz/sesgo-en-el-espejo.html`
- **Qué se ve.** Una plantilla de oración con un **hueco para el sujeto**:
  *"[SUJETO] reclamó frente a la sede del ministerio."* Debajo, una lista de sujetos posibles
  (variando género, nacionalidad, región, ocupación, edad). Al costado, el **score del modelo** para
  cada versión, ordenado, con barras. Y la diferencia máxima destacada en grande.
- **Controles.** Editor de la plantilla (se puede escribir cualquier oración con un hueco). Selector
  del conjunto de sujetos a probar (o lista editable). Selector de la dimensión a variar. Botón
  **"exportar tabla"**, que genera una tabla en markdown lista para pegar en un paper.
- **Qué tiene que hacer clic.** Que el sesgo se **mide** con un procedimiento simple y sistemático
  (pares mínimos), no se discute en abstracto; y que el resultado es un dato reportable.
- **Momento aha.** La misma oración, dos sujetos, scores muy distintos. Silencio en el aula.
- **Advertencia obligatoria en la propia viz.** Un cartel: *"una diferencia de score no prueba daño;
  prueba una asociación en el modelo. Para afirmar daño hay que mostrar el uso concreto y a quién
  afecta."* Es una viz sobre rigor, no sobre indignación, y la advertencia es parte del contenido.

### 3.3 `viz/checklist-revisor.html` — **el entregable práctico del curso**
- **Qué se ve.** Un formulario con ~20 preguntas organizadas en cinco secciones (Datos, Medición,
  Modelo, Evaluación, Reproducibilidad y ética). A medida que se completa, **se genera en vivo, en
  un panel al costado, un borrador del párrafo de métodos** en castellano académico correcto.
- **Controles.** Campos de texto y selectores. Botón **"copiar el párrafo"**. Botón **"modo
  revisor"**, que invierte el formulario: dado un paper, marca qué falta y **genera la lista de
  comentarios de revisión** correspondiente, redactada con cortesía académica.
- **Qué tiene que hacer clic.** Que reportar bien no es un trámite: es un formato que ya existe y
  que se puede completar en 20 minutos si uno hizo las cosas bien desde el principio — y que es
  imposible de completar si no.
- **Momento aha.** Al intentar completarlo para un análisis hecho sin disciplina: **no se puede**.
  Faltan la semilla, la versión, el número de casos validados. "Este formulario es un detector de
  proyectos mal llevados, y es mejor descubrirlo ahora que en la revisión."
- **Persistencia.** Guardar el estado en `localStorage` para que puedan volver a él, envuelto en
  try/catch.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** ~8 min. Reutiliza el clasificador entrenado en la clase 9 (se carga; si no
está, se reentrena rápido). **Dependencias:** las de la clase 9 + pandas.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Objetivo: hoy no entrenamos nada nuevo. **Auditamos.** | |
| 2 | code | Cargar el clasificador y el corpus de la clase 9. Reportar sus métricas para tenerlas a la vista. | Punto de partida: un modelo "bueno". |
| 3 | md | **1. Qué está usando el modelo.** | |
| 4 | code | Para el clasificador simple (regresión logística sobre bag-of-words, entrenado acá en 10 segundos como modelo auditable), imprimir los 20 términos con mayor peso en cada clase. | Se usa un modelo interpretable **a propósito**: la interpretabilidad es una razón legítima para elegir un modelo más simple, y hay que mostrarlo, no sólo decirlo. |
| 5 | md | `TODO 1` — Leé los 20 términos. ¿Alguno te preocupa? ¿Hay alguno que sea un atajo en vez de una señal del concepto? | |
| 6 | code | **El test de ablación**: quitar del corpus el término más influyente, reentrenar, comparar métricas. | La caída es la evidencia. |
| 7 | md | `TODO 2` — ¿Cuánto cayó? Si cayó mucho, ¿qué implica sobre lo que el modelo estaba midiendo? | |
| 8 | md | **2. Análisis de falsos positivos.** | |
| 9 | code | Imprimir 20 falsos positivos con el texto completo y el score. | |
| 10 | md | `TODO 3` — Clasificá esos 20 errores en categorías propias (ej.: ironía, tema parecido, error de etiqueta humana, ambigüedad genuina). Contá cuántos hay de cada una. | Se produce una tabla de tipología de errores: es un resultado publicable. |
| 11 | md | **3. Test de placebo.** | |
| 12 | code | Aplicar el clasificador a un corpus donde el fenómeno no debería estar (textos administrativos, o el mismo corpus con el texto barajado). Ver qué proporción marca como positivo. | |
| 13 | md | `TODO 4` — ¿Qué proporción marcó? ¿Qué esperabas? *Pista: sobre texto barajado, un modelo que usa orden debería caer; uno que usa sólo palabras sueltas, no.* | Un diagnóstico elegante: revela si el modelo usa sintaxis o sólo vocabulario. |
| 14 | md | **4. Casos límite construidos.** | |
| 15 | code | Lista de ~15 pares mínimos escritos a mano (misma oración con una diferencia clave: negación, cambio de agente, cambio de sujeto). Se pasan por el modelo y se muestran los scores en pares. | |
| 16 | md | `TODO 5` — Escribí **tres pares mínimos propios** que pongan a prueba tu categoría y probalos. ¿El modelo se comporta como esperás? | Ejercicio de diseño experimental, que es el corazón de la validación. |
| 17 | md | **5. Auditoría de sesgo.** | |
| 18 | code | La plantilla con hueco: se genera un conjunto de oraciones variando el sujeto en tres dimensiones. Se calculan los scores. Se produce una **tabla ordenada con la diferencia máxima y un test simple de diferencia de medias**. | El entregable principal del notebook. |
| 19 | code | Gráfico de barras de los scores por grupo, con intervalos. | |
| 20 | md | `TODO 6 (criterio)` — Interpretá la tabla. (a) ¿La diferencia es grande en términos prácticos, no sólo estadísticos? (b) ¿De dónde puede venir? (c) ¿Cambia tu conclusión según si el modelo se usa para decidir o para medir? | |
| 21 | md | **6. Reproducibilidad.** | |
| 22 | code | Celda que genera automáticamente el **bloque de reproducibilidad**: versiones de todas las bibliotecas, semilla, hash del modelo, fecha, cantidad de datos, hash del archivo de datos. Impreso en formato listo para el apéndice. | Función que se llevan y pegan en todos sus proyectos. |
| 23 | md | `TODO 7` — Corré todo el notebook de nuevo desde cero. ¿Te dieron **exactamente** los mismos números? Si no, buscá dónde está la fuente de aleatoriedad no fijada. | Un ejercicio que casi siempre encuentra algo, y esa experiencia enseña más que la slide. |
| 24 | md | **7. La ficha del modelo.** | |
| 25 | code | Plantilla de *model card* / ficha de medida, con los campos a completar: qué mide, con qué datos se entrenó, desempeño por subgrupo, limitaciones conocidas, usos no recomendados. | |
| 26 | md | `TODO 8 (final)` — Completá la ficha para el clasificador de esta clase. Es el entregable del curso. | |
| 27 | md | **Para llevarte**: el checklist completo, la receta de las clases 9-10, y la lista de "cuándo no usar esto". | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Buena métrica = buena medida"** | Es la confusión que organiza toda la clase. | El gancho, y la viz 3.1. Frase: "la métrica te dice que el modelo reproduce tus etiquetas. No te dice nada sobre si tus etiquetas miden tu concepto." |
| **"El modelo es objetivo porque es matemático"** | Aparece siempre, y a veces del lado del entusiasmo y a veces del lado de la crítica. | Se enumeran las decisiones humanas: qué datos, qué etiquetas, qué loss, qué umbral, qué se reporta. Cinco decisiones, todas discutibles. La objetividad no está en el método sino en la explicitación. |
| **"El sesgo se arregla balanceando los datos"** | Solución mágica muy difundida. | Se distinguen los tres sesgos (slide 18). Balancear ayuda con el sesgo de corpus; no toca el sesgo del mundo ni el introducido por el umbral. Y a veces balancear distorsiona la estimación de prevalencia, que era el objetivo. |
| **Sobrecorrección: "entonces esto no sirve para nada"** | Muy frecuente al final de un curso crítico, y es un fracaso pedagógico igual que el entusiasmo acrítico. | Se ataca explícitamente en la slide 31 y en el cierre: la lista de "cuándo no usar" es corta y precisa, no total. La herramienta sirve; lo que no sirve es usarla sin validar. |
| **Confundir interpretabilidad con validez** | "Uso un modelo simple, entonces es válido." | Un modelo interpretable puede estar midiendo lo incorrecto de manera perfectamente transparente. La interpretabilidad **ayuda a detectar** el problema; no lo previene. |
| **Creer que la validación es un paso final** | La dejan para el final y no llegan. | La validación se diseña **antes** de entrenar: la muestra a etiquetar, los casos límite y el test de placebo se planifican junto con el proyecto. Se dice como consejo operativo. |
| **"Reproducible = el código está en GitHub"** | Confunden disponibilidad con reproducibilidad. | Si no están la semilla, las versiones y los datos (o su procedencia exacta), el código no reproduce nada. Se demuestra con el TODO 7. |
| **Pensar que la ética es un trámite del comité** | La tratan como formulario. | Los casos de la slide 26 no tienen respuesta obvia y hay desacuerdo real en el aula. Ese desacuerdo es la demostración de que es una discusión sustantiva. |

---

## 6. Analogías y metáforas de ciencias sociales

- **Validez de constructo, tal cual.** No hace falta analogía: es literalmente el concepto de
  Cronbach y Meehl (1955) aplicado a un instrumento nuevo. Decirlo así les devuelve el terreno:
  **este es su campo, no el de la ingeniería.**
- **El modelo como instrumento de medición.** Un clasificador es un instrumento, como una escala de
  actitudes. Se reporta su construcción, su fiabilidad, su validez y sus limitaciones. Nadie
  publicaría una escala sin reportar su alfa; nadie debería publicar un clasificador sin reportar su
  matriz de confusión sobre una muestra validada.
- **El atajo léxico y la validez aparente.** El caso 1 de la viz 3.1 es el equivalente de un ítem de
  encuesta que mide la comprensión de la pregunta y no el constructo. Es un problema clásico con
  ropa nueva.
- **El sesgo del instrumento vs el sesgo del mundo.** Un termómetro mal calibrado y un país que
  realmente hace calor son dos problemas distintos. La confusión entre ambos produce tanto negación
  ("es sólo el reflejo de la realidad") como magia ("arreglemos el modelo y arreglamos el mundo").
- **El feedback invisible.** Un sistema que despriorizó un caso y nadie lo revisó nunca no genera
  evidencia de su error. Es el mismo problema que la selección en la muestra: sólo observás los
  casos que pasaron el filtro. Esta es probablemente la lección de mayor valor práctico de todo el
  curso para quien vaya a trabajar en el Estado o en una ONG.
- **La caja negra y la autoridad experta.** Delegar una decisión en un sistema que nadie puede
  explicar es un problema de legitimidad, no sólo de precisión. Es discusión de teoría política y
  el aula la puede llevar mejor que nadie.
- **El revisor 2 como dispositivo pedagógico.** El chiste funciona y organiza toda la clase: hay que
  escribir para el lector más desconfiado. Anticipar sus seis objeciones es un método de trabajo.

---

## 7. Cuestionario: temas a evaluar (12 ítems)

1. **[MC conceptual]** ¿Cuál es la diferencia entre desempeño y validez?
2. **[MC conceptual]** ¿Qué es la validez de constructo aplicada a un clasificador?
3. **[Qué pasa si]** Tu clasificador de "populismo" fue entrenado con textos de 2010-2015 y lo
   aplicás a 2020-2024. ¿Qué tipo de validez está en juego y cómo lo testearías?
4. **[Leer un gráfico]** Se muestra la tabla de términos más influyentes de un clasificador de
   "conflictividad". Identificar cuáles son señales del concepto y cuáles son atajos, y explicar la
   diferencia.
5. **[Leer un gráfico]** Una tabla de auditoría de sesgo con scores por subgrupo. Decir qué se puede
   concluir y —más importante— **qué no**.
6. **[Diseño]** Escribí tres pares mínimos para poner a prueba un clasificador de "crítica al
   gobierno". Explicá qué testea cada uno.
7. **[Diseño]** Diseñá un test de placebo para un detector de discurso de odio. ¿Qué corpus usarías
   y qué resultado esperarías?
8. **[Reproducibilidad]** Enumerá los seis elementos mínimos que tiene que tener el apéndice
   metodológico de un paper que usa un clasificador.
9. **[Distinción]** Un modelo asigna scores más altos de "agresividad" a textos que mencionan cierta
   región del país. Distinguí las tres explicaciones posibles (sesgo del mundo, del corpus,
   introducido) y decí cómo distinguirías entre ellas empíricamente.
10. **[Criterio]** Mencioná tres situaciones concretas en las que **no** usarías deep learning para
    tu problema, y qué usarías en su lugar.
11. **[Revisión]** Se da el resumen de un paper. Escribí tres comentarios de revisor, ordenados por
    gravedad, distinguiendo cuál es fatal y cuáles se arreglan con una revisión menor.
12. **[Ética aplicada]** Un municipio quiere usar un modelo entrenado con reclamos ciudadanos para
    priorizar la atención. Te consultan **antes** de implementarlo. Escribí una respuesta de una
    página: qué preguntarías, qué exigirías como condición, qué monitorearías después de la
    implementación, y en qué caso recomendarías directamente no hacerlo. *(Se busca: quién soporta
    el error; el problema del feedback invisible; la necesidad de una vía de apelación humana;
    auditoría por muestreo de los casos despriorizados; y la recomendación de no hacerlo si no hay
    presupuesto para monitoreo continuo.)*

---

## 8. Referencias

**Para el estudiante:**
- Grimmer, J. & Stewart, B. (2013), *Text as Data: The Promise and Pitfalls...*, Political Analysis.
  El principio de validación permanente. `[VERIFICAR]`
- Kapoor, S. & Narayanan, A. (2023), *Leakage and the Reproducibility Crisis in ML-based Science*,
  Patterns. **Lectura central de la clase.** `[VERIFICAR]`
- Mitchell, M. et al. (2019), *Model Cards for Model Reporting*, FAccT. Para la ficha del modelo.
  `[VERIFICAR]`
- Narayanan, A. & Kapoor, S., *AI Snake Oil* (libro y blog) — para el criterio general sobre qué
  promete y qué no promete la IA. Muy legible para esta audiencia. `[VERIFICAR URL]`

**Para el docente:**
- Cronbach, L. & Meehl, P. (1955), *Construct Validity in Psychological Tests*. La fuente clásica,
  y vale citarla en clase para marcar que el problema tiene 70 años. `[VERIFICAR]`
- Jacobs, A.Z. & Wallach, H. (2021), *Measurement and Fairness*, FAccT. **El puente explícito entre
  la teoría de la medición de las ciencias sociales y el fairness en ML. Es exactamente la tesis de
  esta clase, escrita por gente del campo técnico.** `[VERIFICAR]`
- Salganik, M., *Bit by Bit: Social Research in the Digital Age* — capítulos sobre ética y sobre
  datos observacionales masivos. Disponible online. `[VERIFICAR URL]`
- Gebru, T. et al. (2021), *Datasheets for Datasets*. `[VERIFICAR]`
- Selbst, A. et al. (2019), *Fairness and Abstraction in Sociotechnical Systems*, FAccT — para la
  discusión sobre por qué "arreglar el modelo" no arregla el sistema. `[VERIFICAR]`
- Para la actividad del juicio: conviene que el equipo prepare **dos** papers cortos (uno defendible
  con reparos menores, otro con un problema fatal de validez) para poder rotar la actividad entre
  cohortes. Pueden ser construidos ad hoc y rotulados como material didáctico.
