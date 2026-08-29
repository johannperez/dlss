# Soluciones y guía de corrección — Clase 10

> **Para el docente.** Cada solución dice cuál es la correcta, **por qué cada distractor es
> tentador**, y —lo importante— **qué confusión revela elegirlo**. Esa última columna es lo
> que sirve en el aula: te dice qué hay que volver a explicar y a quién.
>
> Las preguntas 6, 7, 10, 11 y 12 no tienen respuesta única. Van con **rúbrica**: se corrige
> el argumento, no la conclusión.

---

## 1. Desempeño y validez · **B**

> «El modelo reproduce las etiquetas de ese corpus con un F1 de 0,91.»

Es lo único que el número dice, literalmente. Todo lo demás es una inferencia que hay que
demostrar aparte.

| distractor | por qué tienta | qué confusión revela |
|---|---|---|
| **A** «detecta discurso de odio con un 91 % de eficacia» | Es la traducción automática que hace todo el mundo, incluidos los abstracts publicados. Suena a la misma frase. | **La confusión central de la clase.** Confunde «coincide con las etiquetas» con «detecta el fenómeno». Además cambia F1 por «eficacia», que no significa nada. Si eligen esta, volvé al gancho: el clasificador de política tenía F1 0,68 y encontraba el 21 % de un corpus 100 % positivo. |
| **C** «es mejor que un humano» | Aparece en la prensa técnica todo el tiempo. | Falta el término de comparación: **el techo humano es el acuerdo entre codificadores**, y no se midió. Un modelo evaluado contra las etiquetas de *un* codificador no se puede comparar con «un humano». (Clase 9, kappa.) |
| **D** «va a funcionar en otro corpus» | Parece modesta y razonable: es el mismo idioma. | Confunde **validez interna con externa**. Es exactamente lo que falla en el control positivo: mismo idioma, mismo tipo de texto, y el recall se derrumba de 0,64 a 0,21. |

---

## 2. Validez de constructo · **C**

> «Lo que el modelo mide es efectivamente el concepto del que habla el paper.»

| distractor | por qué tienta | qué confusión revela |
|---|---|---|
| **A** «está bien construido, sin errores de programación» | «Constructo» suena a «construcción». Es una trampa lingüística real. | Confusión de vocabulario, no conceptual. Se arregla nombrando a Cronbach y Meehl: el constructo es **el concepto teórico**, no el software. |
| **B** «generaliza bien a datos nuevos del mismo tipo» | Es una propiedad deseable y de hecho es *otra* validez. | Confunde constructo con **externa**. Un modelo puede generalizar perfecto a datos nuevos del mismo corpus y seguir midiendo la cosa equivocada: el de hoy generaliza bien a más prensa mexicana de 2020. |
| **D** «usa una arquitectura apropiada» | Suena técnicamente sofisticado. | Es la confusión más cara: cree que la validez es una **propiedad del modelo**. La validez es una propiedad de **la inferencia** que hacés con el modelo. El mismo modelo puede ser válido para una afirmación e inválido para otra. |

---

## 3. El clasificador que envejece

**(a)** **Validez externa** (temporal). Y de paso, validez de constructo: si el vocabulario
del populismo cambió, el instrumento ya no mide lo mismo aunque devuelva números.

**(b)** Dos explicaciones:
- **Sustantiva:** hubo menos discurso populista en 2020-2024. Es un hallazgo.
- **Instrumental:** el vocabulario cambió —otros actores, otros temas, otra coyuntura— y el
  modelo no reconoce las formas nuevas. La caída es del instrumento, no del fenómeno.

**(c)** El test que se busca es alguno de estos, y cualquiera vale si está bien especificado:

- **Muestra leída a mano en el período nuevo.** Codificá 150 textos de 2020-2024 a ciegas y
  comparalos con la predicción del modelo. Bajo la explicación sustantiva, el modelo y la
  codificación humana **coinciden** y los dos muestran menos populismo. Bajo la instrumental,
  la codificación humana encuentra populismo donde el modelo no.
- **Reentrenar sobre el período nuevo** con etiquetas nuevas y comparar los términos más
  influyentes con los del modelo viejo. Si son otros, el vocabulario se movió.
- **Casos límite de época:** tomá diez textos claramente populistas de 2013 y reescribilos con
  el vocabulario de 2022 sin cambiar el contenido. Si el puntaje cae, es el instrumento.

> **Lo que hay que exigir:** que digan **qué resultado esperarían bajo cada explicación**.
> Un test que da lo mismo pase lo que pase no es un test. Es el mismo error que la ablación
> de la slide 18.

---

## 4. Los términos más influyentes

**(a)**

| señales del concepto | atajos |
|---|---|
| paro, corte, marcha, reclamo, gremio, ruta | **clarín**, **jueves**, **fotogalería** |

*«ruta»* es discutible y conviene discutirlo en clase: es una señal razonable en un país donde
los cortes de ruta son la forma modal de protesta, y es un atajo si el corpus tiene mucha
sección de tránsito. **Que sea discutible es el punto:** la separación la hace una persona con
conocimiento del dominio, no un algoritmo.

**(b)** Por qué cada atajo separa sin medir:
- **clarín** — es el **medio**. Si un diario cubre más conflicto que otro, el nombre del medio
  predice la etiqueta sin decir nada sobre el conflicto. Es la fuga de la clase 9, con datos
  nuevos. Además: aparece en el texto porque alguien lo citó, no porque hubo conflicto.
- **jueves** — es un **artefacto del calendario**. Si las marchas suelen ser en jueves, el día
  predice; pero un jueves sin marcha no tiene nada de conflictivo, y una marcha en martes
  desaparece del radar.
- **fotogalería** — es un **artefacto del formato**: las notas con muchas fotos son coberturas
  en la calle. Predice el género periodístico, no el fenómeno.

**(c)** En otra provincia: se derrumba, porque «clarín» y los nombres locales no aparecen o
aparecen distinto. En 2015: se degrada, porque el repertorio de protesta y el vocabulario
periodístico cambian. **El modelo mide «¿esto se parece a la cobertura de conflicto de este
diario, en esta provincia, en estos años?».**

> **Error frecuente de corrección:** estudiantes que ponen *gremio* en la columna de atajos
> «porque es una palabra específica». No: es específica **del concepto**. El criterio no es
> «qué tan común es la palabra» sino **si la palabra está ahí porque ocurrió el fenómeno**.

---

## 5. La auditoría de sesgo mal leída

**(a) Lo que sí se puede concluir:** entre `abogadas` y `abogados` —el único par donde las dos
palabras están en el vocabulario— hay una diferencia de **0,055** a favor del femenino. Es un
dato reportable, con esa plantilla y ese modelo.

**(b) Las dos cosas que la persona afirma de más:**

1. **«No hay sesgo de género.»** Cuatro de las seis filas dan **exactamente 0,265** porque las
   palabras **no están en el vocabulario**. Ese número no es un puntaje del sujeto: es lo que
   devuelve la oración sin el sujeto. **La igualdad no es equidad, es ceguera.** Y tiene una
   consecuencia sustantiva: un modelo no puede ser justo con un grupo que no está en sus datos.
2. **«Los puntajes por ocupación son casi todos iguales.»** No se midió ocupación: se midió
   **presencia en el vocabulario**. Enfermeras y obreras dan igual entre sí y dan igual que
   cualquier palabra desconocida. No es un resultado sobre ocupaciones.

Y hay una tercera, más sutil, que vale como bonus: aun donde el par sí está en el vocabulario,
**una diferencia de puntaje no prueba daño**. Prueba una asociación en el modelo. Para hablar
de daño hay que mostrar el uso, quién decide con eso y a quién le cae el error.

**(c) Qué pedir antes de aceptar nada:**
- La **columna de vocabulario** (que en esta tabla, por suerte, está: hay que mirarla).
- **Más pares** y un test que diga si la diferencia se distingue del azar — con dos pares
  válidos no hay potencia para nada.
- La **plantilla completa** y varias plantillas distintas: el efecto puede ser de la oración
  y no del sujeto.
- **Para qué se va a usar el modelo.** La misma tabla justifica cosas distintas si el modelo
  mide o si el modelo decide.

---

## 6. Tres pares mínimos · rúbrica

No hay respuesta única. Se corrige con estos cuatro criterios:

| criterio | qué mirar |
|---|---|
| **Cambia una sola cosa** | El error número uno: pares que cambian el verbo *y* el sujeto *y* el tema. Si cambian dos cosas, el par no informa nada. **Este es el criterio que más se falla.** |
| **La predicción está escrita antes** | Tienen que decir qué esperan que pase. Un par sin predicción es una observación, no un experimento. |
| **El «no debería cambiar» es realmente irrelevante** | Cambiar «martes» por «jueves» sirve. Cambiar «el gobierno» por «el oficialismo» **no** es irrelevante: son sinónimos para vos, no necesariamente para el modelo. Los dos casos son interesantes, pero hay que saber cuál se está haciendo. |
| **El caso límite es genuinamente difícil** | Si el «límite» es obvio, no es límite. La señal de que está bien elegido es que **el aula se divide** al codificarlo. |

**Ejemplos que funcionan** (para el clasificador de «crítica al gobierno»):

- *Debería cambiar:* «El gobierno anunció el plan de obras» / «El gobierno fracasó con el plan
  de obras». Testea si detecta valoración o sólo el tema.
- *No debería cambiar:* «El ministro criticó la gestión anterior el martes» / «…el jueves».
  Testea sensibilidad a ruido irrelevante.
- *Límite:* «La oposición celebró los datos de empleo». ¿Es crítica al gobierno? Depende de si
  la crítica es explícita o inferida por el lector. **Si el codificador humano duda, la
  definición operativa está incompleta, y eso no lo arregla ningún modelo.**

---

## 7. El test de placebo · rúbrica

**(a) El corpus.** Tiene que cumplir dos condiciones y hay que exigir las dos: que el
fenómeno **no debería estar**, y que se **parezca en todo lo demás** al corpus de trabajo
(mismo idioma, registro parecido, época parecida). Buenos candidatos: boletín oficial, actas
de asamblea de consorcio, reseñas de productos, resúmenes de partidos de fútbol, manuales de
instrucciones. Mal candidato: texto en otro idioma o de otro siglo, porque si el modelo falla
no sabés por cuál de las diez diferencias falló.

**(b) Resultado esperado si el modelo es válido.** Una tasa de positivos **muy baja y
compatible con la prevalencia real** en ese corpus (que suele ser cerca de cero). Ojo con el
umbral: con el umbral en 0,5 y un modelo mal calibrado, «bajo» puede seguir siendo 15 %.
Conviene reportar la **distribución de puntajes**, no sólo la proporción por encima del corte.

**(c) Qué haría sospechar.** Una tasa alta, y sobre todo **una tasa alta con puntajes altos**.
Y hay que mirar *cuáles* marcó: si el detector de odio marca los textos del boletín oficial
que hablan de migración, no está detectando odio: está detectando **tema**. Eso es información
mucho más útil que la proporción.

**(d) El control positivo.** Un corpus donde el fenómeno tiene que aparecer sí o sí: un
conjunto de casos ya juzgados como discurso de odio, o textos de foros conocidos y moderados
por ese motivo. Si ahí el recall es bajo, el modelo **no estaba detectando el fenómeno tampoco
antes**, sólo que en el corpus de test nadie se dio cuenta.

> **Bonus para discutir:** un placebo tiene un problema ético propio. Para armar el control
> positivo hay que juntar un corpus de discurso de odio, y eso es un objeto que hay que
> manejar con cuidado. Vale la pena mencionarlo si alguien lo trae.

---

## 8. El apéndice mínimo

Los seis, y qué se rompe si falta cada uno:

| elemento | qué se rompe si falta |
|---|---|
| **Semilla** | Ni los propios autores pueden reproducir sus números. Cualquier diferencia que reporten es indistinguible del ruido de la partición. |
| **Versiones exactas** (`pip freeze`) | El comportamiento cambia entre versiones menores. Dentro de dos años el mismo código da otro resultado y nadie sabe por qué. |
| **Datos disponibles, o su procedencia exacta** | No se puede repetir el análisis ni verificar las exclusiones. Si no se pueden publicar, hay que decir por qué. |
| **Código en un repositorio** | Nadie puede ver las decisiones que no están en el texto (preprocesamiento, filtros, cortes). |
| **Ficha del modelo** con sus limitaciones | Quien lo reutilice no sabe para qué **no** sirve, y lo va a aplicar donde no corresponde. |
| **Prompts exactos y versión del modelo**, si se usó un LLM | El modelo cambia sin aviso y las versiones viejas se despublican. El resultado deja de existir. |

Se acepta también, en lugar del último, **el número de casos validados a mano**; es igual de
imprescindible. Lo que **no** se acepta es «el código está en GitHub» como respuesta a todo:
es exactamente la confusión que la pregunta busca detectar.

---

## 9. Tres explicaciones, y cómo distinguirlas

**(a) Las tres:**
- **Sesgo del mundo:** en esa región efectivamente circula más discurso agresivo. El modelo
  refleja algo que existe.
- **Sesgo del corpus:** los textos de esa región en tu corpus vienen de fuentes distintas
  (por ejemplo, más medios sensacionalistas, o más cobertura de conflictos) que los del resto.
- **Sesgo introducido:** lo pusiste vos. El topónimo se coló como término predictivo porque en
  el entrenamiento coincidía con los casos positivos; o el umbral, o el remuestreo.

**(b) Cómo distinguirlas empíricamente.** Esto es lo que se corrige:

- **Contra el introducido:** el test más barato. **Pares mínimos**: la misma oración cambiando
  sólo el topónimo. Si el puntaje se mueve con todo lo demás igual, el modelo tiene el nombre
  del lugar adentro. Complemento: quitar los topónimos del corpus y reentrenar.
- **Contra el del corpus:** comparar **la composición de fuentes** por región. Si la región
  aparece sobre todo en medios de un tipo, ahí está. Test: reponderar o estratificar por medio
  y volver a medir la diferencia. Si desaparece, era composición.
- **Contra el del mundo:** hace falta una **medida externa**. Codificación humana a ciegas de
  una muestra estratificada por región (¿los humanos también ven más agresividad?), o datos
  independientes (registros de conflictividad, encuestas). Si la codificación humana replica la
  diferencia sobre textos comparables, hay algo del mundo.

**(c) Sí, cambia lo que reportás.** Si las tres operan a la vez —que es lo normal— no podés
reportar «hay más agresividad en X». Reportás la diferencia medida, **la descomposición
parcial que lograste** y lo que quedó sin identificar. Y sobre todo: cambia el uso. Una
diferencia con componente instrumental no identificado **no se puede usar para decidir sobre
nadie**, aunque sí sirva para describir el corpus.

> **Lo que hay que castigar en la corrección:** respuestas que nombran las tres explicaciones
> y no proponen ningún dato. Nombrarlas es la parte fácil; distinguirlas es la pregunta.

---

## 10. Cuándo no · rúbrica

Se corrige que sean **concretas** y que la alternativa sea **específica**.

| nivel | cómo se ve |
|---|---|
| **Insuficiente** | «Cuando hay pocos datos», «cuando el problema es simple». Repite la slide sin aplicarla. |
| **Suficiente** | Nombra un capítulo, un corpus o una variable propia, y dice qué usaría en su lugar. |
| **Bueno** | Además **estima el costo** de la alternativa (cuántas horas de codificación, qué se pierde) y dice qué haría falta para que valiera la pena el modelo. |

Ejemplos de respuestas buenas que suelen aparecer:
- «Mis 180 entrevistas codificadas: entrenar ahí es sobreajustar. Sigo con codificación manual
  y uso el modelo sólo para **buscar** pasajes candidatos, no para clasificarlos.»
- «Mi argumento es que el efecto del ingreso sobre la participación es de tal tamaño. Necesito
  el coeficiente y su error estándar: una regresión. El deep learning me da una predicción que
  no puedo interpretar y que nadie me va a discutir en los términos que me interesan.»
- «Mi corpus tiene 400 documentos y un diccionario de doce palabras ya da lo mismo. El tiempo
  que ahorro lo pongo en leer 100 casos a mano, que es lo que me faltaba.»

---

## 11. Tres comentarios de revisor · solución modelo

**Fatal 1 — no hay validación de la medida.**
El artículo afirma medir *polarización afectiva* pero sólo reporta exactitud en la tarea. No
hay evidencia de que el clasificador mida el constructo: ni muestra codificada a mano, ni
acuerdo entre codificadores, ni análisis de errores. **Sin esto, el hallazgo del 31 % no es
interpretable.** *Fatal: requiere trabajo empírico nuevo, no reescritura.*

**Fatal 2 — la exactitud del 94 % no dice nada sin la prevalencia ni el piso.**
En una tarea con clases desbalanceadas, decir siempre la clase mayoritaria puede dar 90 %.
Faltan prevalencia, precisión, recall y la línea de base. Y falta la **variación por partición**:
sin ella no se puede juzgar si el aumento del 31 % supera el ruido del propio instrumento.
*Fatal: puede tumbar el resultado principal.*

**Menor — el salto de la medida a la conclusión causal.**
«Las redes sociales amplifican la hostilidad» no se sigue de una serie temporal de tuits
durante una campaña: falta el contrafáctico y hay al menos dos confusores obvios (la campaña
misma, y cambios en la composición de usuarios). *Menor sólo si se reformula la conclusión
como descriptiva; fatal si el artículo insiste en la interpretación causal.*

**Otros comentarios aceptables:** el modelo no está identificado con versión ni revisión (menor,
salvo que sea una API cerrada, y entonces sube a serio); no se dice cómo se recolectaron los
2,4 millones de tuits ni qué se excluyó (serio); no hay ficha ni auditoría por subgrupo y el
tema es hostilidad política (serio si el modelo se va a publicar).

> **Cómo evaluar:** lo que se busca **no** es que encuentren muchos problemas. Es que
> **distingan gravedad**. Un estudiante que marca los seis como fatales entendió la mitad:
> tratar todo como fatal bloquea trabajo bueno y quema la credibilidad del revisor para cuando
> encuentre algo que sí lo es. Esa distinción es el aprendizaje de la pregunta.

---

## 12. La consulta del municipio · rúbrica

Se busca que la respuesta cubra estos cinco puntos. Los tres primeros los produce casi todo el
mundo; **el cuarto y el quinto son los que separan una respuesta buena de una excelente.**

| punto | qué tiene que aparecer |
|---|---|
| **1. Quién soporta el costo del error** | No es el municipio: es la persona cuyo reclamo queda al final de la cola. El error del sistema y el costo del error caen en lugares distintos, y eso cambia todo el análisis. |
| **2. Vía de apelación humana** | Tiene que existir una manera de que una persona pida revisión, y esa manera tiene que ser **usable** por quien más la necesita (no un formulario web si el reclamo llegó por teléfono). |
| **3. Qué se está midiendo, y con qué datos** | Los reclamos registrados **no son** las necesidades: son las necesidades **de quienes saben y pueden reclamar**. Sesgo de selección clásico. Un modelo entrenado ahí prioriza a quien ya sabía navegar el Estado. |
| **4. El feedback invisible** ⚑ | **El punto más importante y el que más se omite.** Un caso despriorizado que nadie revisó **no genera evidencia de su propio error**. El sistema sólo ve los casos que atendió, así que sus métricas van a verse bien para siempre. Antídoto obligatorio: **auditoría por muestreo aleatorio de los casos despriorizados**, atendidos igual, para medir la tasa de error donde el sistema es ciego. |
| **5. Cuándo recomendar no hacerlo** ⚑ | Si no hay **presupuesto sostenido** para ese monitoreo. Un sistema de priorización sin auditoría de los despriorizados es un sistema que no se puede evaluar, y un sistema que no se puede evaluar no se puede defender ante nadie. También: si no hay vía de apelación, o si el municipio quiere el modelo para **justificar** una reducción de personal ya decidida (ahí el modelo es una coartada, no una herramienta). |

**Preguntas que una buena respuesta hace antes de opinar:** ¿cuál es el criterio de prioridad
hoy, y quién lo aplica? ¿Qué problema concreto quieren resolver — volumen, equidad, tiempos?
¿Qué pasa hoy con un reclamo que no se atiende? ¿Quién va a operar el sistema y con qué
capacitación? ¿Está previsto que el modelo se vuelva a entrenar, y con qué datos?

**Condiciones exigibles razonables:** ficha del modelo pública; auditoría por subgrupo (barrio,
canal de ingreso, idioma) **antes** de implementar; el modelo **ordena**, no descarta; período
de prueba en paralelo con el criterio actual, comparando resultados; publicación de las
métricas de operación.

> **Señal de excelencia:** la respuesta distingue las condiciones **técnicas** (validación,
> auditoría, umbral) de las **institucionales** (quién decide, quién revisa, quién paga el
> monitoreo) y dice que las segundas son las que hacen fracasar los proyectos. Eso es
> exactamente el aporte que un cientista social hace en ese equipo y que nadie más hace.
