# Notas para quien da la clase 7

**Attention: cada palabra arma su propio resumen del contexto** · 120 minutos

> **Lo primero, y no es decorativo.** Ésta es **la clase donde es más fácil perder al
> aula**. El transformer se explica habitualmente con matrices, con
> `softmax(QKᵀ/√d)V` y con diagramas de bloques, y con esta audiencia ese camino es un
> desastre. Todo el diseño de esta clase consiste en **invertir el orden**: primero el
> gesto humano, después la aritmética de escuela, y recién al final las tres letras.
>
> **Criterio de éxito:** si el aula sale **sin haber visto la fórmula pero entendiendo el
> mecanismo**, la clase fue un éxito. Si sale **habiendo visto la fórmula sin entender el
> mecanismo**, fue un fracaso, aunque hayan tomado apuntes prolijos.

---

## 1. El arco narrativo, en diez líneas

1. Les hacés leer una oración larga con un «lo» al final, y les preguntás a dónde fueron.
2. Todos fueron al mismo lugar, y ninguno releyó desde el principio: **saltaron**.
3. Eso que hicieron sin pensar tiene nombre, y es lo único nuevo del transformer.
4. El mecanismo desnudo: cada palabra reparte 100 puntos entre las demás y se arma un
   **promedio ponderado**. Nada más difícil que eso, y lo hacés a mano en el pizarrón.
5. Falta una sola cosa: **¿de dónde salen los pesos?** Ahí entra el aviso clasificado:
   cada palabra publica lo que ofrece (key) y busca lo que necesita (query).
6. Recién entonces aparece la fórmula, ya vacía de misterio, y se traduce término a
   término a la analogía.
7. Tres decisiones de diseño: no espiar el futuro (máscara), varias lecturas en paralelo
   (cabezas), y el sellito de posición (sin él volvemos a la bolsa de palabras de la 6).
8. El bloque completo, como cuatro piezas con una función clara cada una, y la conexión
   residual contada como «el original del expediente sigue adjunto».
9. Construyen la máquina entera **y no la encienden**. Encenderla es la clase 8, y esa
   expectativa es deliberada.
10. Cierre en negativo: los mapas de atención se ven hermosos y se sobreinterpretan todo
    el tiempo. **Attention no es explicación.** Lo más útil que se llevan hoy es lo que
    van a poder no creerse.

---

## 2. Plan de tiempos real, bloque por bloque

| Empieza | Dura | Bloque | Slides | Qué pasa |
|---|---|---|---|---|
| **0:00** | 10 | Gancho | 1-5 | La oración, el silencio, la votación a mano alzada. |
| **0:10** | 20 | Attention a mano | 6-9 | El mecanismo sin fórmulas + la cuenta en el pizarrón + la viz central. |
| **0:30** | 15 | Q, K, V | 10-17 | El aviso clasificado, el puntaje, softmax, y recién ahí la fórmula. |
| **0:45** | 15 | **Manos 1** | 18 | Notebook, secciones 2 y 3. |
| **1:00** | 10 | **PAUSA** | 19 | **No se toca.** |
| **1:10** | 9 | Las tres decisiones | 20-26 | Máscara, cabezas, posición. Dos viz. |
| **1:19** | 6 | El bloque completo | 27-32 | Diagrama, residual, MLP, norm, apilar, y la tabla de la clase 5. |
| **1:25** | 20 | **Manos 2** | 33 | Notebook, secciones 4 a 8, de a dos. |
| **1:45** | 15 | Cierre | 34-38 | La advertencia, el lunes, las tres ideas, el glosario y el puente. |

**Suma 120 exactos** y coincide con el plan minuto a minuto de `PROGRAMA.md`. Los quince
minutos de 1:10 a 1:25 son para **trece slides**, así que van rápido y en bloque: es el
tramo que hay que ensayar. Si te comés cinco minutos ahí, se los sacás al bloque práctico
2 (sección 6), nunca al cierre.

> **Los números de slide de esta tabla son los del `slides.html`** (38 en total, los que
> muestra el contador abajo a la derecha), no los de la especificación, que iba hasta 35.
> La diferencia son tres slides que se agregaron: la de la pausa (19), la tabla de la
> clase 5 (32) y «las tres cosas de hoy» (36).

**Los relojes que importan.** Si a las **0:45** no arrancaste el bloque práctico 1,
estás atrasado. Si a la **1:25** no arrancaste el 2, recortá según la sección 6 de estas
notas. La pausa arranca a la 1:00 pase lo que pase.

---

## 3. Qué preguntar al aula, cuándo, y qué van a contestar

### Minuto 2 — slide 2, «Dónde quedamos»
**Preguntá:** «¿De qué se olvidaba la mochila de la clase pasada?»
**Van a decir:** «del principio», «de lo que leyó primero».
**Qué hacés con eso:** «Exacto. Hoy vamos a sacarle la mochila y darle anteojos.»
Si nadie contesta, no insistas: decilo vos y seguí. El gancho de hoy es la slide 3, no
ésta.

### Minuto 5 — slide 4, la votación
**Preguntá, con las cuatro opciones en pantalla y a mano alzada:** «Cuando leíste *lo*,
¿a qué palabra fuiste a buscar?»
**Van a votar:** A («proyecto») por goleada, con dos o tres D («oficialismo») y alguna
risa.
**Qué hacés con eso, y esto es lo importante:** elegí a alguien que votó A y preguntale
**«¿releíste la oración entera para encontrarla?»**. Va a decir que no. Ese «no» es la
clase. Repetilo en voz alta: «no releyó. **Saltó.**»
**Si alguien vota D en serio** (no en chiste): es oro. Preguntale por qué, y vas a
escuchar un argumento sintáctico legítimo (el sujeto más cercano). Usalo en la slide 34:
«hasta nosotros, que somos hablantes nativos, tenemos ambigüedad acá. Y sin embargo un
modelo con medio millón de perillas se juega por una».

### Minuto 18 — slide 8, la cuenta a mano
**Preguntá:** «Si le subo el peso a *proyecto* de 0,6 a 0,9, ¿para dónde se va la flecha
violeta?»
**Van a decir:** «para arriba», «para la derecha», «hacia proyecto».
**Qué hacés:** movelo y que vean que sí. Y después la pregunta que cierra:
**«¿puede irse afuera de las tres flechas?»** La respuesta es no, y la razón —los pesos
suman 1— es toda la intuición del mecanismo. Si esta pregunta la contestan bien, la clase
está ganada.

### Minuto 26 — slide 9, la viz central
**Preguntá:** «¿Alguien encontró una palabra que mire a algo raro?»
**Siempre aparece una.** Anotala en el pizarrón con el nombre de quien la encontró y
volvé a ella en la slide 34. Es el mejor material que vas a tener para la advertencia
final, porque es de ellos.

### Minuto 62 — slide 20, «volvimos»
**Preguntá:** «¿Les sumaron 1 las filas?»
**Van a decir:** «sí», y alguno «a mí me dio 0,99».
**Qué hacés:** «Eso es redondeo al imprimir, no un bug. Y ahora la pregunta que importa:
¿cuánto sumaron las columnas?» Silencio. «Cualquier cosa. Y está bien.»

### Minuto 106 — slide 34, la advertencia
**Preguntá:** «¿Qué evidencia pedirían ustedes para afirmar que el modelo **usó** esa
palabra?»
**Van a decir, en este orden:** «que la mire mucho» (no alcanza), «que se repita en
muchos casos» (mejor, pero sigue siendo correlacional), y con suerte alguien dice
**«sacarla y ver si cambia»**.
**Qué hacés:** si alguien dice eso, celebralo con nombre y apellido. Es exactamente la
respuesta: una **intervención**, no una inspección. Si no sale sola, guialos:
«¿cómo demostrarían en su propia investigación que una variable causa algo?». Ahí sale.

---

## 4. Las confusiones que van a aparecer, y cómo se desarman

| Confusión | Cómo se manifiesta | Cómo la desarmás |
|---|---|---|
| **«Attention es un tipo de memoria»** | La asimilan a la RNN de la clase 6. | Es lo contrario: **no hay ningún estado que se arrastre**. Todas las palabras se miran en paralelo, de una. Por eso se entrena rápido en GPU, y por eso hay una ventana de contexto finita (clase 8). Frase: «la RNN se acuerda; attention mira». |
| **Confundir filas con columnas** | Leen «esta palabra fue mirada» cuando dice «esta palabra miró». | La convención dicha en voz alta **cada vez**: **fila = quien pregunta**. Y `viz/matriz-de-atencion.html`, con la columna verde de sumas 1,00 y la fila roja de sumas cualquiera. Es la confusión número uno de la clase. |
| **«Q, K y V son tres cosas distintas»** | Creen que son tres entradas separadas. | Slide 13: las tres cajas salen del **mismo** embedding. Y la celda del notebook donde `Q = X @ W_q`, `K = X @ W_k`, `V = X @ W_v`: la misma `X` tres veces. Señalá la `X`. |
| **Miedo al softmax** | La palabra los bloquea y dejan de escuchar. | «Convertir puntajes en porcentajes que suman 100.» Slide 16, con los cuatro números y las barras. **Nunca escribas la fórmula del softmax en esta clase**: se escribe en la 8, con la temperatura. |
| **«La máscara es para ahorrar cómputo»** | Confunden su propósito. | Es para **no hacer trampa**. Analogía: el examen donde ves la hoja del compañero. Sacás diez y no aprendiste nada. |
| **«Cada cabeza tiene un rol lingüístico claro»** | Sobreinterpretan; lo leyeron en algún lado. | `viz/cabezas.html`. Los rótulos de esa viz se **calculan midiendo**, y varias cabezas quedan rotuladas «no se deja resumir en una regla simple». Esa es la verdad del campo. |
| **«El mapa explica la decisión»** | La confusión más importante para esta audiencia. | Slides 32-33. El argumento: se pueden construir mapas muy distintos que producen la **misma** salida (Jain & Wallace 2019). Si el mapa no determina la salida, no la explica. |
| **Perderse en las dimensiones** | Errores de forma constantes en el notebook. | La disciplina de `print(algo.shape)` **enseñada como método**, no como accidente. La tabla de formas está al final del notebook: proyectala durante el bloque práctico 2. |
| **«¿Y esto es todo? ¿No hay nada más?»** | Decepción, o incredulidad. | **Sí, esto es todo.** Y contestarlo así es importante: la sensación de que «tiene que haber algo más escondido» es la que sostiene la mistificación de la IA. Lo que hay de más es **escala y datos**, no una idea oculta. |

---

## 5. Los chistes y las analogías que funcionan

- **El aviso clasificado.** La analogía central. Contala con un ejemplo del aula: «busco
  monoambiente, luminoso, cerca del subte». El chiste que siempre funciona y que además
  es **conceptualmente correcto**: *«el aviso dice luminoso y a estrenar; el value es lo
  que efectivamente hay cuando vas a verlo»*. La diferencia entre lo que alguien dice que
  ofrece y lo que da es exactamente la diferencia entre key y value.
- **La ronda de presentación.** Para el mismo trío: key = lo que decís que sos, query =
  lo que venís a buscar, value = lo que efectivamente aportás cuando te consultan.
- **El equipo de codificadores.** Para multi-head: varios analistas leen el mismo texto
  con libros de códigos distintos (uno marca actores, otro temporalidad, otro valoración)
  y después se juntan los resultados. Es análisis de contenido multidimensional, tal cual.
- **El original del expediente.** Para la conexión residual: cada oficina agrega su
  dictamen y el documento original sigue adjunto. Si cada oficina lo reemplazara por su
  resumen, a la quinta no quedaría nada del caso. Con público de administración pública
  esta analogía produce risa de reconocimiento.
- **La red de citas.** Para la asimetría fila/columna: que A cite a B no implica que B
  cite a A. Quien haya visto análisis de redes reconoce el objeto entero, incluida la
  matriz de adyacencia dirigida.
- **El examen con la hoja del compañero.** Para la máscara causal.
- **«No hay una idea nueva por piso.»** Para apilar bloques. Es la frase que más
  desmitifica de toda la clase: los modelos grandes no tienen ideas escondidas en las
  capas de arriba; tienen el mismo piso repetido, con más plata.

---

## 6. Si vas atrasado

**Se recorta en este orden. Lo de más arriba se saca primero.**

1. **Slide 32 (`supuestos-de-arquitectura.html`).** Es un gesto de continuidad muy lindo
   y cuesta 2 minutos. Se muestra 20 segundos diciendo «acá está la tabla de la clase 5
   con las dos filas que estaban grises, abiertas» y se pasa. O se saca entera.
2. **Slide 30 (la normalización).** Se resume en una frase al pasar: «hay una pieza más
   que reescala los números para que no se disparen. Es plomería, importa que esté.»
3. **Slide 23 + viz de cabezas (24) → dejá sólo la viz.** La idea de multi-head se dice
   en 40 segundos mientras la viz está en pantalla.
4. **Slide 15 (el producto punto).** Se puede decir sin la viz: «producto punto es cuánto
   apuntan dos flechas para el mismo lado».
5. **El bloque práctico 2 se acorta a 12 minutos** y se les pide que hagan sólo las
   secciones 4 y 8 del notebook (máscara y bloque completo), dejando multi-head y
   posición como tarea. El notebook está escrito para poder terminarse solo en casa.

**Lo que NUNCA se recorta:**

- **La pausa.** Diez minutos, a la hora en punto. Si se la come el entusiasmo, la segunda
  mitad se atropella y el cierre —que es la parte que le sirve a esta audiencia para su
  trabajo— queda en tres minutos apurados.
- **La slide 8 (la cuenta a mano).** Es la única aritmética explícita de la clase y es la
  que sostiene todo lo demás. Sin ella, la fórmula de la slide 17 es magia.
- **Las slides 34-35 (attention no es explicación).** Es el `[EL LUNES]` de la clase y lo
  más útil que se llevan. Si tenés que elegir entre terminar el bloque completo y hacer
  la advertencia, hacé la advertencia.
- **El puente a la clase 8.** Treinta segundos, y son los que hacen que vuelvan.

---

## 7. Si vas adelantado

- **Hacé la demostración de la bolsa de palabras en vivo**, en la slide 25: escribí las
  dos oraciones («la comisión rechazó al ministro» / «el ministro rechazó a la comisión»)
  y preguntá qué le pasaría a la matriz de atención si permutaras las palabras. Después
  corré la celda del notebook que lo demuestra, proyectada.
- **Abrí `viz/attention-como-mesa.html` y pediles oraciones.** Están las cinco del corpus;
  recorré la de la enumeración («la educación, la salud, la seguridad y la justicia») y
  preguntá qué esperan que mire cada sustantivo. Se arma una discusión buena.
- **Detenete en el recuadro del costo cuadrático de la slide 31** en vez de pasarlo.
  «Si cada palabra mira a todas, con 100 palabras hay 10.000 pares; con 1.000, un millón.
  Por eso existe la ventana de contexto y por eso cuesta plata que sea grande.» Es la
  puerta directa a la clase 8 y es lo que necesitan para el **ítem 9 del cuestionario**;
  si vas muy justo de tiempo se lee en veinte segundos, pero no lo saltees del todo.
- **Mostrá `medir-atencion.py`** proyectado, la clase `BloqueTransformer`, y compará
  línea por línea con la del notebook. Que vean que es el mismo código, y que el modelo
  que produjo los mapas de las viz se entrenó con eso, en CPU, en menos de un minuto.

---

## 8. Si te preguntan X

### «¿Y esto es todo? ¿No hay nada más adentro de ChatGPT?»
**Sí, esto es todo.** Lo que hay de más es **escala** (más bloques, más cabezas, más
números por palabra), **datos** (billones de palabras en vez de dos millones) y un
**entrenamiento posterior con humanos** que vemos en la clase 8. Pero el mecanismo es
éste, sin una idea escondida. Y contestarlo así, sin adornos, es importante: la sensación
de que tiene que haber algo más es lo que sostiene la mistificación. Lo asombroso no es la
idea; es que **esta idea tan simple, repetida cien veces con muchísimos datos, haga lo que
hace**. Eso sí es un problema abierto y honesto.

### «¿Entonces el modelo entiende el texto?»
Depende enteramente de qué llamemos entender, y ahí ustedes tienen más herramientas que
yo. Lo que puedo afirmar es lo que hace: **arma promedios ponderados de representaciones,
con pesos aprendidos de la co-ocurrencia en un corpus**. Eso produce comportamientos que
se parecen mucho a comprender, y falla de maneras que ningún humano falla (la clase 8 está
llena de ejemplos). Mi recomendación práctica: en un paper, no escribas «el modelo
entiende». Escribí qué hizo y con qué evidencia. La palabra «entiende» te va a costar un
revisor 2, y con razón.

### «¿Cómo sé cuántas cabezas o cuántos bloques usar en mi investigación?»
**Casi con seguridad no vas a tener que decidirlo.** Entrenar un transformer desde cero
es carísimo y casi nunca es lo que necesitás: lo que vas a hacer es agarrar uno ya
entrenado (clase 9). Ahí la decisión no es cuántas cabezas, sino **cuál modelo, entrenado
con qué datos, y cómo lo valido**. Si algún día sí tenés que decidirlo, la respuesta
honesta del campo es: se copia una configuración conocida que ande y se ajusta poco.

### «Si attention mira a todas las palabras, ¿por qué ChatGPT se olvida de lo que le dije
hace un rato?»
Porque «todas las palabras» son **todas las que entran en la ventana**. Y la ventana es
finita por una razón concreta: si cada palabra mira a todas, la cantidad de pares crece
con el **cuadrado** de la longitud. Con 1.000 fichas son un millón de pares; con 100.000,
diez mil millones. Attention resolvió el problema de memoria de las RNN y a cambio
introdujo un problema nuevo, que es de costo. Eso es lo que se compra cuando se paga por
«más contexto». Lo vemos con el modelo propio en la clase 8.

### «Un paper que quiero citar dice que el mapa de atención muestra que el modelo se basa
en tal palabra. ¿Está mal?»
**Una parte es defendible y la otra no.** Es defendible decir que **por ahí pasó la
información**: el mapa describe de dónde salieron los números. No es defendible decir que
esa palabra **causó** la salida, y ahí ustedes ya tienen todo el vocabulario: es
correlación presentada como causa. La evidencia adecuada sería una **intervención**
(cambiar esa palabra por otra y ver si cambia la predicción), o al menos una prueba de
robustez sobre muchos casos. Y hay literatura específica que lo discute: Jain & Wallace
(2019) muestran que se pueden construir mapas muy distintos con la misma salida; Wiegreffe
& Pinter (2019) matizan. Citá las dos: **mostrar un debate abierto es más fuerte que
elegir un bando**.

---

## 9. Detalles de producción

- **Antes de entrar al aula**, abrí las cinco viz una vez (`viz/*.html`) para que el
  navegador tenga todo en cache. Abren con `file://`, sin internet, pero la primera carga
  del `datos-atencion.js` (62 KB) tarda un pestañeo.
- **El botón de tema claro/oscuro** está abajo a la derecha en cada viz suelta. En el
  proyector, el tema claro se lee mejor casi siempre; si la sala está muy oscura, probá
  el otro **antes** de empezar, no durante.
- **Los mapas de atención de las viz son de un modelo real y chiquito.** Si alguien
  pregunta si son «de verdad», la respuesta es sí, y `medir-atencion.py` está en la
  carpeta: se corre en menos de un minuto en CPU y da **exactamente** lo mismo, porque la
  semilla está fija (se verificó dos veces: sale igual hasta el cuarto decimal).
- **Si el bloque 1 del modelo te muestra cabezas que se miran casi sólo a sí mismas**, no
  es un error de la viz: es lo que aprendió. Decilo. Es una observación real sobre modelos
  chicos y poco entrenados, y sirve de antídoto contra la idea de que cada pieza hace algo
  interpretable.
- **El notebook entero corre en menos de un minuto en CPU** (medido dos veces: 12 s y 15 s,
  0 errores). La única celda que se hace esperar es la de los embeddings
  de la clase 6, que recalcula PPMI + SVD sobre el corpus real sin red: entre 5 y 30
  segundos según la máquina. Avisalo antes de que arranquen el bloque práctico 1, o vas a
  tener cinco manos levantadas diciendo «se colgó».
- **No entrenes el modelo «un poco más» pensando que va a mejorar.** Se probó: con 6000
  pasos y una tasa de aprendizaje más baja la loss de validación mejora (4,60 → 4,23) y
  **la clase empeora**. Las cabezas se vuelven difusas, «lo» pasa a mirarse sobre todo a
  sí misma y en la enumeración la atención se va a los artículos: se pierden los dos
  momentos aha de las viz. El modelo que está en el repo se eligió por lo que **muestra**,
  y eso está dicho en `medir-atencion.py`.
- **Si querés cambiar las oraciones de las visualizaciones**, corré
  `python3 medir-atencion.py --listar-candidatas`: imprime las 563 oraciones del corpus
  que califican (largo justo y todas sus palabras en el vocabulario) y sale sin entrenar.
  Elegís las que quieras, las ponés en `ORACIONES_ELEGIDAS` y volvés a correr el script
  sin la opción.
