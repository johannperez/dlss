# Soluciones comentadas — Clase 7

**Para quien da la clase.** Cada ítem trae la respuesta correcta, **por qué cada distractor
es tentador**, y **qué confusión revela elegirlo**. Esa última parte es la que sirve: si en
un grupo de treinta hay ocho que eligen el mismo distractor, no es distracción, es una
explicación que no funcionó, y sabés cuál.

---

## 1. ¿Qué hace attention?

**Correcta: B** — *para cada palabra, calcula un peso hacia cada una de las otras y arma un
promedio ponderado del contexto*.

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** (recorre y guarda en memoria) | Es **exactamente la RNN de la clase 6**, y viene fresca. Además «memoria» es la metáfora que todo el mundo tiene para «modelo que lee». | La confusión número uno de la clase: **attention no es una memoria**. No hay ningún estado que se arrastre. Todas las palabras se miran en paralelo, de una. Desarmalo así: «la RNN se acuerda; attention mira». Y agregá la consecuencia: por eso se entrena rápido en GPU, y por eso hay una ventana finita. |
| **C** (busca en un diccionario) | Es el modelo mental por defecto de «la computadora entiende palabras»: que adentro hay definiciones. | Creen que el significado está **guardado** en algún lado. En realidad el significado que el modelo maneja es **posicional y relacional**: sale de la compañía (clase 6) y del contexto (hoy). No hay definiciones adentro. |
| **D** (compara con el corpus) | Es cómo funciona una búsqueda, y mucha gente supone que un LLM es «un buscador con onda». | Creen que hay una base de datos adentro. Esta confusión es la que hace que la gente se sorprenda de que un LLM alucine. Se paga en la clase 8: **no hay base de datos, hay parámetros**. |

**Bandera roja:** si más de un tercio elige A, volvé a la slide 6 antes de seguir con la
clase 8. Sin esto, el mini-GPT de la 8 no se entiende.

---

## 2. Query, key y value

**Correcta: B** — *tres transformaciones del mismo vector de entrada*.

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** (tres entradas distintas) | Los nombres suenan a cosas separadas, y en una base de datos una *query* y una *key* **sí** son objetos distintos. | Es la confusión más común con Q, K y V: creer que son tres cosas que entran. Se desarma con la slide 13 (las tres cajas saliendo del mismo embedding) y señalando la `X` en `Q = X @ W_q`, `K = X @ W_k`, `V = X @ W_v`: la misma `X`, tres veces. |
| **C** (query y key son lo mismo) | Es media verdad peligrosa: en *self*-attention las tres salen del mismo texto, así que se sienten iguales. | No distinguen **rol** de **origen**. El mismo origen, tres roles: qué busco, qué ofrezco, qué aporto. La analogía del aviso clasificado existe exactamente para esto. |
| **D** (son las tres capas) | «Tres cosas con nombre raro» + «un modelo tiene capas» = conclusión razonable si te perdiste. | Se perdió en la arquitectura general. No es grave a esta altura; se recupera con el diagrama de la slide 27. |

---

## 3. La fila de «y»

**a)** A **«seguridad»**, con 0,39 (39% de su atención).

**b)** La fila suma **1,00** (0,28 + 0,23 + 0,39 + 0,05 + 0,05 ≈ 1,00). Las columnas suman
cualquier cosa porque **cada palabra reparte su propio 100%**, y nada obliga a que una
palabra sea *mirada*, en total, un 100%. Hay palabras que mira todo el mundo (la primera
coma: 4,03) y palabras que no mira nadie (0,00).

> **La respuesta que buscás en la parte b** es que la fila y la columna **no son
> simétricas**. Si alguien contesta «las columnas también deberían sumar 1 pero hay error
> de redondeo», ahí tenés a alguien que está leyendo el heatmap al revés. Es la confusión
> más frecuente del tema y hay que atenderla en el momento. La analogía que la resuelve en
> diez segundos: **matriz de adyacencia de una red de citas**. Que A cite a B no implica
> que B cite a A. La fila es «a quién cito yo»; la columna, «quién me cita».

**c)** Esa cabeza parece estar **cerrando la enumeración**: cuando llega la conjunción «y»,
reparte su atención entre los tres sustantivos enumerados y casi nada entre los artículos.
Es una hipótesis razonable y vale contarla.

**Lo que NO autoriza a concluir**: que el modelo «entienda» qué es una enumeración; que esa
cabeza «sea» la cabeza de las enumeraciones (habría que verlo en muchas oraciones, no en
una); y sobre todo, que esas tres palabras **causen** la salida del modelo. El mapa
describe por dónde pasó la información. Nada más. *(Esto anticipa el ítem 11.)*

**d)** Por la **máscara causal**. La columna de una palabra sólo puede recibir atención de
ella misma y de las que vienen **después**; las dos últimas de la oración casi no tienen a
nadie detrás. A la última columna (*justicia*) sólo podría mirarla la propia *justicia*, y
a la anteúltima (*la*), sólo *la* y *justicia*.

Y acá hay un segundo paso, que es el que hay que hacer explícito: que esas columnas den
**0,00 y no otra cosa** no lo decide la máscara, lo decide el modelo. Esa última palabra
tenía permitido mirarse a sí misma y eligió no hacerlo (reparte su 100% entre las dos
comas). En otra cabeza, esa misma columna podría valer hasta 1,00. **La máscara acota
cuánto puede valer una columna; el valor exacto lo pone el modelo.**

> **Si alguien responde «porque son palabras poco importantes»**, ahí hay una lectura del
> heatmap como si fuera un ranking de importancia. Es un error caro y conviene corregirlo:
> lo que hay en el triángulo superior no es «poco importante», es **inaccesible**.

---

## 4. Sin máscara causal

**a)** Aprende a **copiar**, no a predecir. Si para adivinar la palabra 5 puede mirar la
palabra 5 (y la 6, y la 7), la tarea deja de tener dificultad: la respuesta está en la
entrada. Aprende la función identidad desplazada, que no sirve para generar nada.

**b)** Porque la loss mide exactamente lo que el modelo está haciendo bien: acertar la
próxima palabra **con la información que le diste**. Y le diste la respuesta. La loss va a
bajar rapidísimo y hasta valores absurdamente bajos. **Una loss que baja no significa que
el modelo aprendió lo que vos querías: significa que aprendió a resolver la tarea que
efectivamente le planteaste.** Es el mismo error de fondo que la fuga de datos de la
clase 4, con otro disfraz.

**c)** En el momento de **generar**. Cuando le pedís que escriba texto nuevo, no tiene
futuro para espiar y produce basura. La distancia entre «loss hermosa» y «genera basura» es
el síntoma.

> **Conexión que conviene hacer explícita:** este ítem es la clase 4 (fuga de datos) en
> ropa nueva. Si el grupo ya vio aquello, decilo: «esto es fuga de datos, y la máscara es
> la partición». Se les acomoda solo.

---

## 5. Sin *positional encoding*

**a)** Cualquier par de frases con **las mismas palabras en distinto orden**. La del curso
es *«la comisión rechazó al ministro»* / *«el ministro rechazó a la comisión»*. Se busca que
den una propia: *«el sindicato denunció a la empresa»* / *«la empresa denunció al
sindicato»*; *«el juez procesó al intendente»* / *«el intendente procesó al juez»*.

> **Si alguien objeta que en esos pares también cambian los artículos** (*al* de un lado,
> *a la* del otro), tiene razón y es una buena objeción: en rigor no son la misma bolsa de
> palabras hasta que sacás las palabras vacías, que es exactamente la aclaración que hizo
> la clase 6. La demostración limpia, sin artículos de por medio, es la del notebook:
> **la misma oración con las palabras barajadas** da la misma salida, sólo que reordenada
> (diferencia máxima ≈ 5·10⁻⁷, que es error de redondeo). Dale el punto y mostrá esa celda.

> **El ejercicio real es que sea del área de quien responde**, porque ahí se ve que el
> problema no es lingüístico sino sustantivo: en su investigación, **quién le hace qué a
> quién** suele ser exactamente la variable.

**b)** Queda equivalente a la **bolsa de palabras** (*bag of words*) de la clase 6. Es la
técnica de análisis de texto más usada en ciencias sociales durante treinta años, y es
justamente la que la clase 6 mostró rota. Sin posición, attention es **una bolsa de
palabras carísima**.

> **Si responden «queda como TF-IDF»**, es igual de correcto en espíritu: TF-IDF es una
> bolsa de palabras con pesos. Aceptalo y aclará la diferencia.

---

## 6. Softmax

**a)** 0,61 + 0,15 + 0,05 + 0,18 = **0,99** (es 1,00; falta un centésimo por redondeo). Se
lleva más atención la primera, con **61%**.

**b)** Se **afila**: los pesos pasan a **0,96 · 0,01 · 0,00 · 0,03**. El ganador se lleva
casi todo. La razón: el softmax exponencia, y multiplicar los puntajes por 3 es elevar cada
exponencial al cubo — las diferencias que ya existían se agrandan multiplicativamente.

**c)** Se **aplana**: **0,28 · 0,25 · 0,22 · 0,25**, casi un reparto parejo. Si los
puntajes se achican, todas las exponenciales se parecen y el softmax pierde criterio.

**La perilla de la clase 8 es la temperatura.** Es literalmente esto: dividir los puntajes
por un número antes del softmax. Temperatura baja = puntajes agrandados = distribución
afilada = el modelo elige siempre lo más probable y escribe aburrido y repetitivo.
Temperatura alta = puntajes achicados = distribución aplanada = el modelo se manda cosas
raras. **Que lo descubran acá, con cuatro números, hace que en la clase 8 la temperatura no
sea un misterio sino un reencuentro.**

> **Error frecuente en b:** contestar «se aplana» razonando que multiplicar por 3 «hace
> todo más grande, así que todos suben». Revela que están pensando en la escala absoluta y
> no en las **diferencias**. La pregunta que lo destraba: «¿qué pasa con la *distancia*
> entre 2,0 y 0,6 si multiplico los dos por 3?».

---

## 7. Cabezas múltiples

**Correcta: B**.

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** (procesar varias oraciones) | «Paralelo» aparece en las dos explicaciones y se mezcla. Además el *batch* sí procesa varias oraciones a la vez. | Confunden **multi-head** con **batch**. Se aclara con la tabla de formas del notebook: el lote es la dimensión `B`; las cabezas son la `H`. Son ejes distintos del mismo tensor. |
| **C** (repuesto / redundancia) | Suena a ingeniería sensata. | Ninguna confusión grave, pero sí una idea equivocada de que el modelo tiene tolerancia a fallas. No la tiene: si sacás una cabeza entrenada, el modelo empeora. |
| **D** (reducir parámetros) | Hay algo cierto escondido: el ancho se **reparte** entre las cabezas, así que cuatro cabezas de 24 usan lo mismo que una de 96. | Media verdad. Aclará: no reducen parámetros, los **reorganizan**. Cuatro lecturas de 24 números en vez de una de 96. La ganancia es de diversidad, no de tamaño. Quien elige D suele haber entendido bien la mecánica; corregilo con cuidado, es un buen error. |

---

## 8. La conexión residual

**Correcta: B**.

| distractor | por qué es tentador | qué confusión revela |
|---|---|---|
| **A** (normaliza) | Están al lado en el diagrama y las dos suenan a plomería. | Mezclan las dos piezas «aburridas» del bloque. Se separa fácil: la normalización **reescala**; la residual **suma la entrada**. Y sólo una de las dos tiene una historia (el expediente). |
| **C** (conecta la última con la primera) | La palabra «conexión» sugiere algo global, y hay arquitecturas recurrentes que sí hacen eso. | Se imaginan un ciclo. Aclará que la residual es **local a cada bloque**: rodea ese bloque y nada más. |
| **D** (guarda datos de entrenamiento) | Es la fantasía de la base de datos adentro, otra vez. | La misma confusión del distractor D del ítem 1. Si aparecen las dos en la misma persona, vale una conversación aparte: **el modelo no guarda los datos**, guarda parámetros. |

**Respuesta completa que buscás:** `salida = entrada + lo_que_hizo_el_bloque`. Sirve para
dos cosas: (1) la información original no se pierde al apilar muchos bloques, y (2) el
gradiente de la clase 3 llega hasta abajo sin diluirse. El `TODO 4` del notebook lo muestra
con números: sin residual, la desviación estándar de la salida se derrumba después de seis
bloques.

---

## 9. Attention contra la memoria de las RNN

**Lo que tiene que aparecer en la primera parte:**

- La RNN lee **en orden** y arrastra una única mochila de memoria. Todo lo que leyó tiene
  que caber ahí, y lo viejo se va diluyendo. A treinta palabras del principio, del sujeto
  ya no queda casi nada.
- Attention **no arrastra nada**: cada palabra puede mirar directamente a cualquier otra,
  esté a dos palabras o a doscientas. **La distancia dejó de costar.** No hay camino que
  recorrer, hay un salto.

**Lo que tiene que aparecer en la segunda parte (la que importa):**

- El problema nuevo es el **costo cuadrático**. Si cada palabra mira a todas, con 100
  palabras hay 10.000 pares; con 1.000 palabras, un millón; con 100.000, diez mil millones.
- Consecuencia práctica: la **ventana de contexto es finita**, y agrandarla cuesta plata de
  verdad. Es exactamente lo que se paga cuando se paga por «más contexto», y es la razón
  por la que un asistente se «olvida» de lo que le dijiste hace rato.

> **Criterio de corrección.** La primera parte la contesta casi todo el mundo. **La segunda
> parte es la que separa.** Si alguien dice «el problema nuevo es que no sabe el orden»,
> está confundiendo el ítem 5 con éste: la posición no es un problema *nuevo*, es una pieza
> que ya agregamos. Si alguien dice «el problema es que necesita muchos datos», es una
> respuesta legítima y bien pensada (la fila del transformer en
> `viz/supuestos-de-arquitectura.html` dice exactamente eso), pero no es el costo
> cuadrático: dale el punto y agregá el otro.

---

## 10. Las dos piezas sin rótulo

**a)** Las dos son **normalizaciones** (*layer norm*). Reescalan los números de cada palabra
para que no se disparen ni se aplasten capa tras capa. Es plomería: importa que estén, no
importa el detalle.

**b)** Son las dos **conexiones residuales**. Cada una lleva una copia de lo que entró y la
suma a la salida de su pieza. «El original del expediente sigue adjunto.»

**c)** Porque **entra un tensor `(oraciones, palabras, números)` y sale uno idéntico en
forma**, con otro contenido. Eso importa porque es la condición para **apilar**: si la
salida tuviera otra forma, no podrías enchufarle otro bloque igual. Por eso GPT-2 chico
tiene doce pisos idénticos y no doce piezas distintas. **No hay una idea nueva por piso.**

> **Error común en a:** poner «attention» y «MLP» en los `???` porque los leen como los
> lugares donde va lo importante. Revela que el diagrama se está leyendo como una lista de
> las cuatro piezas y no como un recorrido. Recorrelo con el dedo, de izquierda a derecha,
> y se resuelve.
>
> **Error común en b:** «son las conexiones entre capas». Revela que no vieron que la
> flecha **saltea** el bloque: sale antes y llega después. Que sea un desvío es todo el
> punto.

---

## 11. El paper y la palabra «inmigrante»

**a) Qué es defendible y qué no.**

- **Defendible:** que al calcular la representación de esa nota, el modelo **tomó
  información** de la palabra «inmigrante» en una proporción alta. Eso es lo que el mapa
  describe: por dónde fluyó la información.
- **No defendible:** que el modelo «se **basa** en» esa palabra **para decidir**. El mapa no
  determina la salida. Jain & Wallace (2019) muestran que se pueden construir mapas de
  atención muy distintos que producen **la misma predicción**; si dos mapas contradictorios
  dan la misma salida, mirar el mapa no alcanza para explicar la salida.
- **Tampoco defendible, y es un salto aparte:** que eso «evidencie el sesgo del modelo».
  Aunque la palabra sí causara la clasificación, faltaría mostrar que esa asociación es
  **injustificada** respecto de la tarea, y no simplemente un reflejo de cómo están
  escritas las notas del corpus. Son dos afirmaciones distintas y el paper las encadena
  como si fueran una.

**b) Qué evidencia pedir.**

1. **Una intervención.** Reemplazar «inmigrante» por una palabra comparable («turista»,
   «vecino», «residente») en los mismos textos y ver si cambia la predicción, y cuánto.
   Eso es un experimento; el mapa es una descripción.
2. **Que sea sistemático.** No un caso: una muestra grande, con el efecto promedio y su
   dispersión. Un mapa lindo es una anécdota.
3. **Un piso de comparación.** ¿Cuánto cambia la predicción si intervenís una palabra
   **cualquiera**? Sin ese piso, no sabés si el efecto es grande.
4. **La composición del corpus de entrenamiento.** Si en los datos las notas con esa palabra
   son mayoritariamente negativas, el modelo aprendió una regularidad del corpus. Eso puede
   ser un **hallazgo sobre la prensa** — que es más interesante que un reproche al modelo.

**c) El experimento propio, escrito para un revisor.**

> Para evaluar si el término *inmigrante* incide en la clasificación, construimos pares
> contrafácticos mínimos: para cada nota del conjunto de test que contiene el término
> (n = …), generamos una versión idéntica sustituyendo *inmigrante* por cada uno de tres
> términos de control apareados por frecuencia y categoría gramatical. Reportamos el cambio
> promedio en la probabilidad predicha de la clase negativa, con intervalos de confianza, y
> lo comparamos con el cambio producido por sustituciones de control sobre términos
> igualmente frecuentes pero temáticamente neutros. Los mapas de atención se reportan como
> material exploratorio y no como evidencia del mecanismo de decisión.

> **Qué buscar al corregir.** No busques la palabra «causalidad»: buscá que aparezca la
> idea de **intervenir** en vez de **inspeccionar**. Esta audiencia tiene la distinción
> incorporada de su propio oficio; el trabajo de la clase es sólo mostrarle que se aplica
> acá igual.
>
> **La respuesta más común y la más floja** es «le pediría que muestre más ejemplos». Está
> en la dirección correcta (sistematicidad) pero se queda en lo observacional: más mapas
> siguen siendo mapas. Repreguntá: «¿y si te muestra cien mapas iguales, ya te alcanza?».
>
> **La respuesta que hay que celebrar** es cualquiera que proponga **cambiar la palabra y
> volver a medir**, aunque esté mal redactada.
