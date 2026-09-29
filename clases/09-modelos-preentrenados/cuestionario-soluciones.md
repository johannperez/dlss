# Clase 9 — Soluciones comentadas

> **Para quien corrige.** Lo importante no es cuál marcaron: es **qué confusión revela cada
> distractor**. Cada respuesta incorrecta de acá abajo la eligió alguien de verdad, por un
> motivo entendible. Usá el motivo para enseñar, no el error para descontar.
> Las preguntas 4, 6, 8, 9, 10, 11 y 12 no tienen respuesta única: tienen respuestas
> **defendibles**, y el criterio de corrección es si el argumento se sostiene.

---

## 1. Transfer learning → **b)**

**Por qué b.** El modelo ya aprendió regularidades del idioma (morfología, sintaxis, qué
palabras aparecen juntas) en un corpus enorme. Esa parte ya está pagada. Lo único que
falta aprender es tu distinción, que es una capa fina arriba de todo eso — y una capa fina
tiene pocos parámetros, así que necesita pocos datos. Es la clase 4 exactamente: menos
perillas, menos datos.

**Por qué tienta a):** *"ya vio ejemplos de tu categoría"*. Es la confusión más común y la
más importante de desarmar. **El modelo nunca vio tu categoría.** No sabe qué es
"protesta" para vos, ni qué es "conflicto laboral" en tu marco teórico. Sabe castellano.
Quien elige esta opción está imaginando una base de datos adentro del modelo, y de ahí a
creerle todo hay un paso. Es el mismo error que la clase 8 desarmó con la alucinación.

**Por qué tienta c):** *"los modelos grandes generalizan mejor"*. Suena a sentido común y
está mal como principio general: el tamaño solo no garantiza nada, y cuánto ayuda depende
de la tarea, del idioma y de cuántos datos tenés. Ojo con qué evidencia usás acá: la curva
de la clase **no** compara modelos grandes contra chicos, compara vectores prestados contra
aprender el vocabulario desde cero (TF-IDF, sin nada prestado). Lo que muestra es que **más
perillas sin conocimiento previo necesitan muchos más datos** (con 25 etiquetas, 0,14
contra 0,45). Justamente por eso b) es la correcta: lo que hace andar a un modelo
pre-entrenado con pocos datos es lo que ya aprendió, no su tamaño.

**Por qué tienta d):** confunde pre-entrenamiento con validación. Son dos cosas distintas
y la segunda la tenés que hacer vos, con tus datos. Quien elige esta opción cree que el
modelo viene "certificado de fábrica" — que es exactamente lo que la clase intenta evitar.

---

## 2. Congelar capas → **b)**

**Por qué b.** Congelar es fijar los parámetros: no reciben gradiente, no se mueven. Sólo
se entrenan las capas de arriba.

**Segunda parte — la relación con la clase 4.** Congelar **baja deliberadamente la
capacidad del modelo**: hay muchísimas menos perillas que ajustar, así que hacen falta
muchos menos datos para ajustarlas sin calcar. Es la misma decisión que tomaron en la
clase 4 cuando eligieron 8 rampas en vez de 32. Si alguien contesta "para que entrene más
rápido", es cierto pero secundario: **la razón principal es estadística, no computacional.**

**Por qué tienta a):** confunde congelar con guardar/cachear. Vocabulario, no concepto.
Se corrige en diez segundos.
**Por qué tienta c):** está describiendo *cuantización*, que existe y es otra cosa.
Quien marca esto suele haber leído sobre modelos chicos y mezcló dos optimizaciones.
**Por qué tienta d):** confunde congelar con la disciplina de la partición. Vale la pena
señalar que las dos cosas sirven para evitar el sobreajuste, por caminos distintos.

---

## 3. Leer una matriz de confusión

**(a) Los números.**

- precisión = 48 / (48 + 24) = **0,67**
- recall = 48 / (48 + 32) = **0,60**
- accuracy = (48 + 296) / 400 = **0,86**
- (F1 = **0,63**, si lo piden)

**(b) Las frases.** Esto es lo que se corrige de verdad. Tienen que decir algo equivalente a:

> *De cada 100 notas que el modelo marcó como conflicto laboral, **67** lo eran de verdad.*
> *De cada 100 notas que realmente eran de conflicto laboral, el modelo encontró **60**.*

Si escribieron los números pero no las frases, **la respuesta está incompleta**, y hay que
decírselo así: es la regla de la casa. Si las frases están invertidas (usan el total de
casos reales en el denominador de la precisión), lo que revela es que están leyendo la
matriz por filas cuando la precisión se lee por columnas. Dibujásela: la precisión mira la
**columna** del "sí" del modelo; el recall mira la **fila** del "sí era".

**(c) El bobo.** Hay 80 positivos reales sobre 400, o sea 20 %. Decir siempre "no" acierta
**320/400 = 0,80**. Tu modelo saca 0,86. **La ganancia real es de 6 puntos, no de 86.**
Ese contraste es toda la pregunta.

---

## 4. Un número que suena bien

**Respuesta corta: no, el resultado no dice nada todavía, y probablemente sea malo.**

Con 4 % de prevalencia, el modelo bobo que dice siempre "no es sobre violencia de género"
saca **96 % de accuracy** y no encuentra **ni una sola** denuncia. Tu colega tiene
exactamente la misma accuracy que un modelo que no hace nada.

Qué pedirle, en orden:
1. **Precisión y recall**, con sus frases. Son los únicos números que distinguen su modelo
   del bobo.
2. **La matriz de confusión.** Cuatro números, no uno.
3. **El baseline** explícito al lado.

Qué buscar en las respuestas: lo que se evalúa acá **no es el cálculo, es el reflejo**.
Que ante un porcentaje alto la primera pregunta sea *"¿cuál es la prevalencia?"*.
Si alguien contesta "está bien porque 96 es alto", volvé a la viz de la matriz con el
slider de prevalencia: es exactamente ese movimiento.

---

## 5. Qué pasa si bajás el umbral

**(a)** Bajar el umbral hace que el modelo diga "sí" más veces. Entonces:
- el **recall sube** (agarra más de los que sí eran; se le escapan menos),
- la **precisión baja** (entre los que marcó hay más falsas alarmas).

Con más precisión: el recall **nunca baja** al bajar el umbral (sólo sube o se queda
igual). La precisión **tiende** a bajar, pero no es monótona: si el caso que entra al
bajar el umbral es un acierto, sube un poco. En el gráfico de la sección 9 del notebook se
ven esos saltitos (el propio código los cuenta). Lo que no hay es un umbral que mejore las
dos **de forma sostenida**: es un trade-off.
Si alguien contesta "depende del modelo", es **parcialmente correcta para la precisión**
(tramo a tramo puede subir o bajar); para el recall, no. Dale el punto si lo justifica así;
medio punto si sólo dice "depende".

**(b) Las situaciones.** Se busca concreción. Ejemplos que valen:

- **Bajar el umbral (privilegiar recall):** estás armando un corpus de notas sobre
  protesta que después **vas a leer una por una**. Preferís que te sobren cien notas de
  más antes que perderte diez protestas. La basura la filtrás leyendo; lo que no está,
  no lo podés recuperar.
- **Subir el umbral (privilegiar precisión):** vas a escribir en el paper *"estos 40
  medios cubrieron el conflicto"* y vas a nombrarlos. Cada falso positivo es un error
  publicado con nombre y apellido.

No vale: *"cuando querés más recall"*. Eso es repetir la definición, no aplicarla.

---

## 6. Qué estrategia elegís

**(a) Con 60 (y 100 como máximo).** Embeddings + un clasificador simple, o directamente un
diccionario / zero-shot como primer pase. Razón: con esa cantidad, aprender la
representación desde cero (sin nada prestado) pierde feo — en el corpus del curso, con 25
etiquetas TF-IDF desde cero saca **F1 0,14** contra **0,45** de embeddings + logística, y
sigue perdiendo hasta cerca de las 680. Si alguien propone fine-tuning, no está mal, pero
tiene que saber que con tan pocas etiquetas es inestable (en la medición opcional del
notebook, con 50 etiquetas dio de 0,22 a 0,57 según la semilla) y que hay que compararlo
contra la opción del medio. La curva de la clase no mide fine-tuning: no la uses como
argumento contra él.
**Respuesta aún mejor:** *"con 100 etiquetas mi problema no es qué modelo usar, es que no
me alcanza ni para evaluar bien. Primero consigo 200-300 para tener un test decente."*
Si alguien contesta eso, tiene diez.

**(b) Con 3.000.** Sí cambia: ahí el fine-tuning tiene con qué, y probablemente gane.
Pero **hay que medirlo**, no suponerlo, y hay que preguntarse si la diferencia justifica
el costo. Si el fine-tuning saca 0,72 y la logística 0,69, sobre 20.000 documentos esa
diferencia puede no mover ninguna conclusión sustantiva — y la logística es interpretable
y corre en un notebook.

**(c) La comparación obligatoria, en los dos casos:** contra el **baseline de clase
mayoritaria** y contra un **piso barato** (diccionario o TF-IDF). Sin piso, un F1 de 0,82
no significa nada. Esta parte de la pregunta es la que más se olvida y es la que más
importa.

---

## 7. Modelos en inglés sobre castellano → **b)**

**Por qué b.** Va a correr. Va a devolver etiquetas con probabilidades de aspecto
respetable. Y va a andar peor de lo que creés: el tokenizador parte mal las palabras del
castellano (las rompe en pedazos raros) y las representaciones se construyeron con otro
idioma. Lo grave no es que ande mal: es que **anda mal en silencio**.

**Por qué tienta a):** *"va a tirar un error"*. Es la esperanza de que el software avise.
No avisa. Esa es la lección: **el software nunca avisa cuando el problema es de validez.**
Vale la pena decirlo con esas palabras.

**Por qué tienta c):** *"el sentimiento es universal"*. Es una afirmación teórica fuerte,
discutible en su propia disciplina, y acá además es empíricamente falsa para el modelo:
lo que el modelo aprendió no es "el sentimiento", es la distribución de palabras de un
corpus en inglés. Buena excusa para cinco minutos de discusión.

**Por qué tienta d):** cree que hay traducción interna. No hay. Nada traduce nada.

---

## 8. El procedimiento completo

Rúbrica: se busca que estén **estos siete elementos**. Faltar uno no invalida la respuesta,
pero faltar el 2 o el 5 sí.

1. **Definición operativa escrita** de "conflicto laboral", con casos límite resueltos
   (¿un paro de un gremio? ¿un reclamo salarial sin medida de fuerza? ¿un conflicto en
   otro país?).
2. **Muestra al azar de 200-300 notas**, etiquetadas **a ciegas** (sin ver la salida de
   ningún modelo). Este punto es no negociable.
3. **Doble codificación de una submuestra** (unas 60) y cálculo del **kappa**. Si el kappa
   es bajo, se para y se arregla la definición: no se sigue.
4. **Partición**: train/val/test, y **por grupo si hay estructura** (por medio, por
   período). Con notas de prensa, partir al azar cuando la fuente predice la etiqueta es
   la fuga clásica de esta clase.
5. **Baseline**: clase mayoritaria + un piso barato (diccionario de términos).
6. **Elegir estrategia según cuántas etiquetas** hay, y evaluar en el test **una sola vez**.
7. **Después del número**: leer 30 errores de los dos tipos, y reportar precisión, recall,
   matriz y ejemplos.

**Errores típicos y qué revelan:**
- *"Etiqueto las 200 que el modelo marcó como conflicto laboral."* Revela que no entendió
  el muestreo: así sólo podés estimar precisión, nunca recall, porque no mirás nada de lo
  que el modelo descartó.
- *"Etiqueto y voy corrigiendo lo que el modelo dice."* Contamina el patrón de referencia.
  Es el error del doble ciego.
- *"Entreno con 19.000 y evalúo con 1.000."* No tiene 20.000 etiquetados: tiene 20.000
  documentos. La confusión entre *tener datos* y *tener etiquetas* es la más frecuente de
  la clase.

---

## 9. El modelo y los humanos

**(a) Las dos explicaciones.** La alegre y la que no.

1. **La categoría es más fácil de lo que el kappa sugiere, y el desacuerdo humano está
   concentrado en pocos casos límite.** Puede pasar: dos codificadores pueden discrepar
   sistemáticamente en un subconjunto chico y difícil, y el modelo estar aprendiendo bien
   el grueso.
2. **Hay fuga, o el modelo aprendió el estilo de *ese* codificador.** Ésta es la
   explicación probable. Un F1 de 0,92 contra un único codificador cuando dos humanos
   coinciden mucho menos suele significar que el modelo está capturando idiosincrasias de
   quien etiquetó, o que algo del test estuvo en el train.

**(b) Cómo distinguirlas** — y esto es lo que se corrige:

- **Evaluá el mismo modelo contra las etiquetas del *otro* codificador.** Si el F1 se cae,
  el modelo aprendió a **un** codificador, no la categoría. Es la prueba más barata y más
  concluyente que existe, y toma cinco minutos.
- **Evaluá a un codificador humano contra el otro con la misma métrica que usás para el
  modelo** (F1, no kappa). Si el humano saca 0,80 y el modelo 0,92, el modelo está por
  encima del techo humano y hay que buscar el problema. Comparar el 0,92 con el kappa 0,65
  directamente es mezclar escalas: el kappa está corregido por azar y un F1 no. Si alguien
  lo hace, marcáselo; es el error más común de esta pregunta.
- **Partí por grupo** (por medio, por período, por codificador) y mirá si el número se
  desploma. Es la prueba de fuga estándar de la clase 4.
- **Mirá los errores.** Si el modelo acierta sospechosamente en un subconjunto homogéneo
  (todos del mismo medio, todos del mismo mes), ahí está el atajo.

---

## 10. Análisis de errores

**(a) El patrón.** Los seis contienen la palabra **"reclamo"** (o "reclamar"), pero en
seis sentidos distintos: vecinal, parlamentario, **publicitario/comercial**, deportivo, de
usuarios de un servicio, y societario. El modelo aprendió que "reclamo" indica protesta.
En castellano, "reclamo" es un término polisémico que cubre desde una movilización hasta
un aviso publicitario retirado por competencia desleal.

**(b) Qué dice sobre la definición operativa.** Que la categoría "protesta" se está
apoyando en un **marcador léxico** en vez de en sus rasgos constitutivos. Si tu concepto de
protesta implica **acción colectiva en el espacio público con un destinatario político**,
entonces la palabra "reclamo" no alcanza ni de cerca: hay reclamos sin acción colectiva
(el societario, el deportivo), sin espacio público (el parlamentario) y sin destinatario
político (el publicitario). El modelo no se equivocó: **hizo explícito que tu definición
operativa era más pobre que tu definición teórica.** Esto es lo que la sección 10 del
notebook llama "leer 30 errores te enseña más sobre tu categoría que leer 300 aciertos".

**(c) Cuáles podrían estar bien.** El **1** (vecinos que elevan un reclamo formal al
municipio) y el **5** (usuarios por cortes de luz) son candidatos legítimos: hay un
colectivo, un destinatario público y una demanda. **Depende de si tu definición exige
acción contenciosa** (movilización, corte, medida de fuerza) o si admite el reclamo
institucionalizado. El **2** depende de si contás la protesta parlamentaria como protesta
—muchos marcos teóricos la excluyen explícitamente porque es acción dentro del sistema—.
Los **3**, **4** y **6** son falsos positivos en cualquier definición razonable.

**Lo importante de esta pregunta:** que noten que la respuesta a "¿está bien clasificado?"
**no la da el modelo ni la métrica: la da su libro de códigos.** Y que si el libro de
códigos no contesta, el libro de códigos está incompleto.

---

## 11. La sección de métodos

Una respuesta que aprueba tiene que contener, sí o sí:

- **el modelo con su identificador exacto y su versión/revisión** (no "usamos BERT");
- **cuántos casos se etiquetaron a mano, por cuántas personas**, y el **acuerdo entre
  codificadores** sobre una submuestra;
- **cómo se partieron los datos** y por qué;
- **el baseline** al lado del resultado;
- **precisión, recall y F1** (no sólo accuracy) con la matriz de confusión;
- **la semilla** y la disponibilidad del código/datos.

Ejemplo de respuesta completa, para mostrar en clase:

> Clasificamos los 20.148 titulares con un clasificador de regresión logística entrenado
> sobre representaciones de oración obtenidas del modelo `<identificador>` (revisión
> `<hash>`). Dos codificadoras etiquetaron a ciegas una muestra aleatoria de 300 titulares
> según el manual del Anexo A; el acuerdo entre ellas fue de 0,81 (kappa de Cohen = 0,68)
> y los desacuerdos se resolvieron por discusión. La partición fue por medio, para evitar
> que el modelo aprendiera a identificar la fuente en lugar del fenómeno: 210 titulares
> para entrenamiento y 90 para test. Sobre el conjunto de test, el clasificador alcanzó
> una precisión de 0,74 y un recall de 0,71 (F1 = 0,72); la clase mayoritaria por sí sola
> alcanza una accuracy de 0,79 frente a 0,89 del clasificador. La matriz de confusión y
> una muestra de errores de ambos tipos están en el Anexo B. El código, las etiquetas y la
> semilla (1983) están disponibles en `<repositorio>`.

*(Los números del ejemplo cierran entre sí: con 21 % de positivos, precisión 0,74 y recall
0,71, la accuracy da 0,89. Hacé la cuenta con el aula: es justo lo que un revisor chequea.)*

**El error más común:** reportar sólo accuracy y F1, sin baseline y sin acuerdo entre
codificadores. Sin esos dos, un revisor informado no puede evaluar nada, y con razón.

---

## 12. Criterio y ética aplicada

Esta pregunta no tiene una respuesta correcta, pero **sí tiene respuestas que revelan que
no se entendió el problema**. Lo que se busca:

**(a) Cuál métrica.** **El recall sobre los casos graves.** Un falso negativo acá es una
denuncia real que se despriorizó y no se atendió; el costo del error no está repartido
parejo entre los dos tipos. Si alguien contesta "precisión, para no perder recursos
atendiendo denuncias que no lo ameritan", el argumento existe y hay que discutirlo, pero
hay que hacer notar la asimetría: el costo de un falso positivo lo paga el organismo (una
visita de más), el de un falso negativo lo paga una persona.
Respuesta aún mejor: **"depende de qué es la clase positiva, y sobre todo: el F1 global
esconde el desempeño en los subgrupos. Quiero recall desagregado por tipo de denuncia y
por barrio."**

**(b) El feedback invisible — el corazón de la pregunta.** Las denuncias despriorizadas
**nunca se leen**, así que nunca se descubre que estaban mal clasificadas. El sistema no
tiene forma de enterarse de sus propios falsos negativos: sólo recibe información sobre
los casos que sí atendió. Con el tiempo, **parece funcionar mejor de lo que funciona**, y
si además se reentrena con los casos atendidos, el sesgo se refuerza solo. Es un bucle de
retroalimentación que se cierra sobre sí mismo.
Si alguien identifica esto sin ayuda, es la mejor respuesta del cuestionario.

**(c) Un mecanismo concreto.** Vale cualquiera que ataque el problema de (b):

- **Auditoría por muestreo de los casos despriorizados**: leer a mano una muestra aleatoria
  de las denuncias que el sistema mandó al fondo, todos los meses, de forma permanente.
  Resuelve el feedback invisible: es la única manera de medir el recall real en producción.
- **Un piso de revisión humana**: ninguna denuncia se cierra sin que la haya visto una
  persona; el modelo ordena la cola, no decide el descarte.
- **Métricas desagregadas y publicadas** por subgrupo, con un umbral de disparidad que
  dispare revisión.
- **Derecho a explicación y a revisión** para quien denunció.

**Respuestas que hay que trabajar:** *"que suban el F1 a 0,95"*. Revela que se cree que el
problema es de calidad del modelo cuando es de **diseño del sistema**. Un modelo perfecto
en un sistema sin auditoría sigue sin poder descubrir sus propios errores. Y *"que no lo
usen"*: es una posición legítima, pero pedile que la defienda contra la alternativa real,
que suele ser una cola por orden de llegada, que también prioriza y también tiene sesgos
—sólo que nadie los mide.
