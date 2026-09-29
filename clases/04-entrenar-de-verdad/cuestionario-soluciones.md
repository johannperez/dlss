# Clase 4 — Soluciones comentadas

**Para quien corrige.** Cada ítem trae la respuesta y, sobre todo, **qué revela cada
distractor**. Un error no es sólo un error: es información sobre qué parte de la clase no
llegó. Donde dice **"si eligió X, volvé a…"** hay una slide o una celda concreta para
mandarlos.

---

## 1. Qué es el sobreajuste

**Correcta: B.** Anda muy bien sobre los datos con los que se entrenó y mal sobre datos que
no vio.

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** ("demasiados parámetros") | Es casi cierto y es la causa más común. | Confunde **causa** con **definición**. El sobreajuste es una *relación entre capacidad y datos*, no una propiedad del modelo solo: 5000 parámetros con 30 casos sobreajustan; con 3 millones de casos, no. Si eligió A, volvé a la **slide 28** (más datos cierra la tijera). |
| **C** ("loss de entrenamiento alta") | Suena mal, y "malo" se asocia con sobreajuste. | Es la definición de **subajuste**, exactamente lo contrario. Revela que no separó las dos curvas. Volvé a la **slide 26**. |
| **D** ("demasiadas épocas, siempre") | Es un caso real (por eso existe early stopping). | El "siempre" lo hace falso: se puede sobreajustar en la época 1 con un modelo enorme, y se puede entrenar 10.000 épocas sin sobreajustar si tenés muchísimos datos. |

---

## 2. Validación contra test

**Correcta: C.**

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** ("son lo mismo") | Es lo que se hace en la práctica en muchísimos trabajos: se aparta un conjunto y se lo llama indistintamente. | **Es la confusión central del bloque.** Si usaste un conjunto para decidir, ese conjunto ya no mide desempeño: mide desempeño *de la mejor de las opciones que probaste*, que está inflado por selección. Mandá a **early stopping (slide 27)**: ahí se ve por qué la validación se ensucia. |
| **B** ("la validación es más grande") | Confunde una convención de tamaño con la función. | Es un detalle de implementación, no la diferencia. |
| **D** ("se usa para entrenar") | Mezcla los tres montones. | Revela que no quedó claro qué significa "el modelo no lo vio". Volvé a la torta de la **slide 23**. |

**Para la discusión en clase.** La frase corta que conviene que se lleven:
**"validación decide, test reporta"**. Y el paralelo: el test es el preregistro.

---

## 3. Leer la tijera

**a.** En la **época 42**, el punto más bajo de la curva naranja. Porque a partir de ahí el
modelo sigue mejorando sobre los datos que ya vio (la azul baja) pero **empeora** sobre los que
no vio (la naranja sube): todo lo que aprende después es ruido específico de esa muestra.

*Errores típicos:* señalar el final (época 1500) — está mirando la azul, que es exactamente
lo que la clase pide no hacer. O señalar dónde las dos curvas se separan (~época 50):
está cerca y el razonamiento es bueno, dalo por válido si lo justifica, pero marcá que el
criterio operativo es el **mínimo de la naranja**, no el punto de separación.

**b.** La franja es **la parte de lo que el modelo aprendió que no le sirve para nada**: el
ruido de esa muestra particular. En términos de investigación, es la distancia entre el ajuste
dentro de la muestra y la capacidad predictiva fuera de ella: lo que no replicaría ni en otra
muestra de la misma población. *(Si alguien lo llama «validez interna contra externa», no lo
des por malo, pero marcá el matiz: esas palabras hablan de identificación causal y de
generalizar a otras poblaciones; el sobreajuste falla antes, en la misma población.)*

**c.** Que bajó la loss **de entrenamiento**, que es el único número que ese colega está
mirando y el único que no sirve para decidir nada. Sobre datos nuevos el modelo pasó de
**0.0133** (época 42) a **0.0225** (época 1500): **empeoró**, casi 70 % más. Y casi toda
la bajada que festeja (de 0.36 a ~0.02) pasa en las primeras quince épocas, fuera del
recorte del eje. Que la azul baje con más épocas no es una noticia: es lo que hace casi
siempre.

*Este ítem es el que mejor separa a quien entendió de quien memorizó.* Quien contesta "bajó
un montón, está bien" no leyó el eje de colores.

---

## 4. Cuatro diagnósticos

| caso | diagnóstico |
|---|---|
| **I** — las dos altas | **3.** Subajuste. El modelo no captura ni siquiera lo que hay. Puede ser capacidad insuficiente, pocas épocas, o un learning rate mal puesto (revisar primero la curva de loss: si nunca bajó, es lr). |
| **II** — train baja, val alta | **1.** Sobreajuste. El caso de manual. |
| **III** — las dos bajas | **2.** Todo bien (con una salvedad: chequeá que la tarea no sea trivial o que no haya fuga, ver caso IV). |
| **IV** — train alta, val **más baja** | **4.** Algo raro pasa. |

**Las dos causas que se buscan en el IV** (con una alcanza para aprobar, con dos está
completo):

- **La validación es más fácil que el entrenamiento** por casualidad o por construcción: cayó
  un conjunto de casos menos ruidosos, o menos diverso, o de un período más estable. Con
  muestras chicas pasa todo el tiempo. *(En la slide 20 de esta clase pasa algo así: la red
  de 16 rampas da 0.0094 en entrenamiento y 0.0047 en los cinco años apartados. La loss de
  entrenamiento no es «alta», pero la de validación queda más baja, por cuáles cinco años
  tocaron.)*
- **Hay fuga o contaminación**: casos duplicados, o el mismo grupo de los dos lados, o —el
  caso más silencioso— el preprocesamiento (normalizar, imputar, seleccionar variables) se
  hizo **sobre todos los datos juntos antes de partir**, así que la validación ya influyó en
  el modelo.
- También vale: hay técnicas (como dropout) que están activas durante el entrenamiento y
  apagadas durante la evaluación, y eso hace que la loss de train se vea peor. Es una respuesta
  avanzada y correcta.

**Ojo al corregir:** que un estudiante desconfíe del caso IV en vez de festejarlo es
exactamente el hábito que la clase quiere instalar. Premialo.

---

## 5. 30 casos, 5000 parámetros

**a.** La loss de entrenamiento va a bajar **prácticamente a cero**. Con 5000 perillas y 30
casos, el modelo puede pasar exactamente por todos los puntos.

**b.** La de test va a ser **mala**, y además **inestable**: con otra muestra de los mismos 30
casos el modelo dibujaría algo completamente distinto (es el botón «otra muestra» de la viz).

**c.** Sí, cambia. Con 30.000 casos, 5000 parámetros ya no alcanzan para memorizar y el modelo
tiene que encontrar regularidades de verdad. **La regla no es "pocos parámetros": es la
relación parámetros / datos.** Quien no marca este matiz entendió la mitad, y es la mitad que
después lo hace desconfiar de todos los modelos grandes por las razones equivocadas.

---

## 6. Duplicar los datos

**Correcta: B.** Se achica.

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** ("se agranda") | Suena a que "más datos, más difícil". | Invierte la relación capacidad/datos. Volvé a la **slide 28** y hacé la demostración en vivo con el slider. |
| **C** ("no cambia") | Piensa el sobreajuste como propiedad del modelo. | Es la misma confusión que el distractor A del ítem 1. |
| **D** ("desaparece del todo") | Exagera la respuesta correcta. | Falso: con suficientes datos la brecha se vuelve chica, no cero. (El ruido de medición no explica la brecha: pone un piso a las **dos** curvas por igual.) |

---

## 7. Ordenar el loop

```python
prediccion = modelo(x)                  # 1. PREDECIR: dibujá con las perillas de ahora
perdida = criterio(prediccion, y)       # 2. COMPARAR: un número para "qué tan mal"
optimizador.zero_grad()                 # 3. BORRAR: tirá lo anotado la vuelta pasada
perdida.backward()                      # 4. ANOTAR: para dónde habría que moverse
optimizador.step()                      # 5. MOVER: recién acá se mueven las perillas
```

**Se acepta** `zero_grad()` al final del cuerpo del loop en vez de en el medio: es equivalente
y hay código real escrito así. Lo que **no** se acepta es `zero_grad()` después de
`backward()` y antes de `step()` — eso borra los gradientes recién calculados y el modelo no
se mueve nunca. Si alguien lo ordenó así, es un error valioso: hacelo correr.

**Error frecuente:** poner `step()` antes de `backward()`. Revela la confusión de siempre
(creer que `backward` es "el que entrena"). Mandalo a la viz de anatomía.

---

## 8. El bug clásico

**a.** Falta `optimizador.zero_grad()`.

**b.** La curva de loss baja al principio y después **no se asienta**: oscila, sube y baja,
y a veces diverge (se va a `nan`). En el notebook, con los datos de la clase y `lr=0.15`,
oscila entre ~0.02 y ~0.06 sin irse al infinito (es la celda opcional después del TODO 3).
En modelos chicos a veces "anda" y da un resultado peor sin avisar, que es lo peligroso.

**c.** Porque PyTorch **acumula** gradientes: los de esta vuelta se suman a los de todas las
anteriores. Cada `step()` empuja con esa suma de pendientes viejas, como una inercia sin
freno: el modelo se pasa de largo, vuelve y se vuelve a pasar.

*Nota para quien corrige:* si alguien dice "el modelo no aprende", es parcialmente correcto
pero no describe el síntoma. Si dice "los pasos crecen sin límite", también es parcial: con
estos datos oscila más de lo que explota. Pedile que corra la celda opcional: ver la curva
ir y venir vale más que la explicación.

---

## 9. Vocabulario con números

**a.** 1200 / 200 = **6 iteraciones por época**.
**b.** 6 × 15 = **90 actualizaciones**. (Una por iteración: `step()` se llama una vez por lote,
no una vez por época.)
**c.** 3000 / 6 = **500 épocas**.

**Error frecuente en b:** contestar 15 (una actualización por época). Revela que sigue pensando
que "entrenar una época" es un solo paso. Es exactamente la confusión que la slide 15 quiere
evitar, y por eso conviene que en el aula quede clarísimo que en **esta** clase 1 época = 1
iteración sólo porque los datos entran en un solo lote (desde la clase 5 ya no).

---

## 10. Datos de panel: 50 diputados

**a. Partición por grupo**, con el diputado como grupo: los 20 discursos de un diputado caen
**enteros** de un solo lado. Por ejemplo 35 diputados para entrenar, 7 para validar, 8 para
test. En `ssdl`: `datos.particion_por_grupo([d["diputado"] for d in discursos])`.

**b.** Si partís al azar, el mismo diputado queda en entrenamiento y en test. El modelo puede
aprender **su estilo personal** —sus muletillas, sus temas, su manera de saludar— y después
"predecir" su partido reconociéndolo a él. **No está prediciendo el partido: está identificando
a la persona.** El número que sale es alto y no mide lo que decís que mide.

*Respuesta parcial frecuente:* "porque hay dependencia entre las observaciones". Correcto pero
insuficiente; pedí que digan **qué aprendería** el modelo. La versión concreta es la que sirve.

**c. No.** El modelo es el mismo; lo que cambió es que ahora **estás midiendo bien**. El número
alto anterior era una ilusión creada por la partición. Esta pregunta separa a quien entendió
la lógica de quien cree que el objetivo es maximizar un número. Si alguien contesta "sí,
empeoró", volvé con él a la slide 35: el test al azar daba 2,2 veces mejor, y era un número
inflado por la fuga (cuánto, no se puede saber).

---

## 11. Serie mensual 2010-2023

**a. Partición temporal**: por ejemplo entrenar con 2010-2019, validar con 2020-2021, testear
con 2022-2023. Los bloques son **contiguos y en orden**. En `ssdl`:
`datos.particion_temporal(meses, corte_val, corte_test)`, con `meses` **numérico y
ordenable** (por ejemplo `2010 + (mes - 1) / 12`, o un índice de 0 a 167) y los cortes en la
misma escala: con textos como `"ene-2010"` la comparación `<` no ordena por fecha.

**b.** Contesta *"¿este modelo sirve para predecir el mes que viene, con la información que
tengo hasta hoy?"*. **No** contesta *"¿qué explica la conflictividad?"* ni *"¿esto vale para
otro país?"*. Y no contesta "¿sirve para un período con otro régimen?": si el test cae entero
en la pandemia, estás midiendo desempeño en un régimen que no estaba en el entrenamiento — lo
cual puede ser exactamente lo que querés medir, pero hay que decirlo.

**c.** Ejemplos válidos, cualquiera alcanza:
- El índice se construyó **estandarizando con la media y el desvío de toda la serie**, así que
  cada valor de 2012 ya contiene información de 2022. *(Es la fuga más frecuente y la más
  invisible: el preprocesamiento hecho antes de partir.)*
- Se usó una **media móvil centrada** o un suavizado que mira hacia adelante.
- La codificación de los eventos se hizo **retrospectivamente**, sabiendo cómo terminó cada
  conflicto.
- Se seleccionaron las variables predictoras mirando su correlación con el resultado **en toda
  la serie**.

---

## 12. El revisor 2

Se busca que aparezcan estas tres (con estas palabras o equivalentes). Sugerimos puntuar 1 por
cada una, y anotar aparte el bonus.

**Pregunta 1 — ¿Sobre qué datos es ese 94 %?**
*Qué problema busca:* que el número sea la accuracy de **entrenamiento**, en cuyo caso no dice
nada sobre el desempeño del clasificador. Redacción sugerida: *"¿El 94 % corresponde a datos
apartados que el modelo no vio durante el entrenamiento? Convendría reportarlo explícitamente."*

**Pregunta 2 — ¿Cómo partieron los datos?**
*Qué problema busca:* fuga por medio, por período o por nota duplicada. Redacción sugerida:
*"¿La partición fue al azar? Si las noticias provienen de un conjunto acotado de medios o de
un período corto, una partición al azar puede permitir que el modelo reconozca el medio o la
coyuntura en lugar del tono. ¿Consideraron partir por medio o por fecha?"*

**Pregunta 3 — ¿Cuál es la clase mayoritaria / el baseline?**
*Qué problema busca:* que el 94 % sea trivial. Si el 93 % de las noticias son de tono neutro,
un clasificador que dice "neutro" siempre saca 93 %. Redacción sugerida: *"¿Cuál es la
distribución de clases y qué accuracy obtiene un clasificador de mayoría? Ayudaría reportar
también precisión y recall por clase."*

**Bonus — ¿Cuántas configuraciones probaron antes de quedarse con esta?**
*Qué problema busca:* selección sobre el conjunto de test (p-hacking artesanal). Es la
pregunta que casi nadie hace y la que esta clase habilita.

**También se acepta como cuarta/quinta**, y conviene mencionarlo al devolver:
- ¿Quién y cómo definió las etiquetas de "tono", y cuál es el acuerdo entre codificadores?
  *(Es la clase 10, pero si alguien la escribe, celebralo.)*
- ¿El conjunto de test tiene suficientes casos para que el 94 % sea distinguible del 90 %?

**Cómo corregir el tono.** La consigna pide *exigente y educada*. Descontá si la redacción es
agresiva o irónica: revisar bien es parte del oficio, y esta es una oportunidad barata de
practicarlo. Descontá también si las tres preguntas son en realidad la misma pregunta escrita
de tres maneras.

---

## 13. Tu propia investigación

**Sin puntaje. Se corrige que esté hecho, no qué dice.**

Qué mirar al leerlas, para la puesta en común de la clase 5:

- Si alguien contesta "mis casos son independientes" y su unidad de análisis son
  **entrevistas**, **notas de un mismo medio**, **provincias en varios años** o **hogares con
  varios miembros**: es el caso más común y el más productivo para discutir. No lo corrijas por
  escrito; llevalo al aula.
- Si nadie puede nombrar su baseline, es señal de que hay que dedicarle cinco minutos al
  arranque de la clase siguiente. El baseline no es un tecnicismo: es la única manera de saber
  si un número es bueno.
- Si alguien dice "mi pregunta no es predictiva, es explicativa", **tiene razón y es la mejor
  respuesta posible**. Ahí el marco de train/test se usa distinto (como chequeo de robustez, no
  como resultado principal), y esa distinción es el corazón de Yarkoni & Westfall (2017), que
  está en `referencias.md`.
