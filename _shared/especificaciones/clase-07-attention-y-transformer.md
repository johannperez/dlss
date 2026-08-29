# Clase 7 — Attention: cada palabra arma su propio resumen del contexto
**Directorio:** `clases/07-attention-y-transformer/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-6 (especialmente 6)

---

## 1. Narrativa de la clase

Esta clase tiene un riesgo específico y hay que nombrarlo de entrada: **es la clase donde es más
fácil perder al aula**. El transformer se explica habitualmente con matrices, con la fórmula
softmax(QKᵀ/√d)V y con diagramas de bloques. Con esta audiencia, ese camino es un desastre.

La estrategia de esta clase es invertir el orden habitual: **attention se enseña primero como un
gesto humano de lectura**, después como un promedio ponderado (que es aritmética de escuela), y
recién al final —cuando ya no hay misterio— aparecen las tres letras Q, K, V y la fórmula, como
notación de algo que ya entendieron. Si el aula sale sin haber visto la fórmula pero entendiendo el
mecanismo, la clase fue un éxito. Si sale habiendo visto la fórmula sin entender el mecanismo, fue
un fracaso, aunque hayan tomado apuntes prolijos.

El hilo:

1. **El salto de lectura.** Se lee una oración larga en pantalla y se les pregunta a qué palabra
   fueron cuando leyeron "lo". Todos saltaron al mismo lugar. **Attention no es una metáfora de
   lo que hacen: es un modelo de lo que acaban de hacer.**
2. **Promedio ponderado.** El mecanismo desnudo: cada palabra se arma un resumen del contexto
   donde cada otra palabra pesa distinto, y los pesos suman 1. Nada más. Esto se hace con números
   redondos en el pizarrón antes de cualquier código.
3. **¿De dónde salen los pesos?** Acá entra Q, K y V, con la analogía del **aviso clasificado**:
   cada palabra publica lo que ofrece (key), cada palabra busca lo que necesita (query), y el
   encuentro entre una búsqueda y una oferta determina el peso. Lo que se lleva no es la key sino
   el value: la mercadería, no el aviso.
4. **La fórmula, sin miedo.** Ahora sí se muestra, y se traduce término por término a la analogía.
   El softmax se presenta como "convertir puntajes en porcentajes que suman 100".
5. **Las tres decisiones de diseño.** (a) La **máscara causal**: si el modelo tiene que adivinar la
   próxima palabra, no puede espiar el futuro. (b) Las **cabezas múltiples**: distintos tipos de
   relación al mismo tiempo (sintáctica, temática, posicional). (c) El **positional encoding**: sin
   él, attention es una bolsa de palabras carísima — callback directo a la clase 6.
6. **El bloque completo.** Attention + MLP + conexión residual + normalización, presentados como
   piezas con una función clara cada una. La conexión residual se explica como "un desvío que deja
   pasar la información original", que es lo que evita que la señal se pierda al apilar.
7. **Construir sin entrenar.** El notebook arma el bloque y verifica formas. Se termina la clase con
   una máquina completa y apagada. Encenderla es la clase 8, y esa expectativa es deliberada.
8. **La advertencia interpretativa.** Los mapas de atención se ven hermosos y se sobreinterpretan
   constantemente. Attention **no es explicación**. Es un `[EL LUNES]` en negativo: lo más útil de
   hoy es lo que van a poder no creerse.

`[CALLBACK DIBUJO]` — "cada palabra dibuja su propio mapa de a quién mirar. Y esos mapas se dibujan
con perillas que se aprenden con el mismo descenso de la clase 3. Es la misma máquina de siempre,
mejor organizada."

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-5 | Leé esto: la frase donde «él» puede ser dos personas distintas. |
| 10-30 | Attention a mano | 6-10 | El mecanismo sin fórmulas: cada palabra arma su resumen del contexto. |
| 30-45 | Q, K, V | 11-17 | El aviso clasificado, el puntaje, softmax, y recién ahí la fórmula. |
| 45-60 | Manos 1 | 18 | Notebook: calcular una matriz de atención a mano, sin librerías. |
| 60-70 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 18. |
| 70-85 | Máscara causal, cabezas, posición | 19-30 | Las tres decisiones de diseño y el bloque transformer completo. |
| 85-105 | Manos 2 | 31 | De a dos: leer mapas de atención sobre texto real. |
| 105-120 | Cierre | 32-35 | La advertencia contra la sobreinterpretación, `[EL LUNES]`, el puente a la clase 8. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (35 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Attention | portada | | |
| 2 | Dónde quedamos | texto | La mochila que se olvida. La pregunta de la clase 6: ¿y si en vez de recordar, miramos? | |
| 3 | **Leé esto** | figura | Una oración larga de debate parlamentario (35 palabras) con una anáfora al final: "...y el oficialismo finalmente **lo** aprobó." | Silencio mientras leen. |
| 4 | ¿A dónde fuiste? | discusión | La misma oración. "Cuando leíste 'lo', ¿a qué palabra fuiste a buscar?" | Todos dicen la misma. Se marca en pantalla con una flecha. |
| 5 | No releíste todo | texto | No volviste al principio leyendo palabra por palabra. **Saltaste.** | "Eso que hacés sin pensarlo es lo único nuevo del transformer. Y ya está: esa es la clase. Lo demás es cómo se implementa." |
| 6 | El mecanismo, sin fórmulas | figura | Una fila de palabras. Desde la palabra "lo", flechas de distinto grosor hacia las demás. Los grosores anotados: 0.6, 0.2, 0.1, 0.05... | "Cada palabra reparte 100% de atención entre todas las demás. Reparte, no inventa: si le da más a una, le da menos a otra." |
| 7 | Y con eso arma un resumen | figura | El vector de "lo" siendo reemplazado por una mezcla: 60% del vector de "proyecto" + 20% de "comisión" + ... | "Esto es un promedio ponderado. Es la cuenta que hacés para calcular un promedio con pesos. Nada más difícil que eso." |
| 8 | En números | figura | Ejemplo numérico completo con 3 palabras y vectores de 2 dimensiones, hecho a mano en la slide, con la cuenta escrita. | Lo hace a mano, en voz alta, con números redondos. **Esta slide es obligatoria y no se puede saltear.** |
| 9 | **Hacé clic en una palabra** | VIZ | `viz/attention-como-mesa.html`. | Hace clic en varias palabras. "Miren cómo cambia el mapa según qué palabra pregunta." |
| 10 | La pregunta que falta | texto | ¿De dónde salen los pesos? | "Hasta acá les dije 'hay pesos'. Ahora: ¿quién los decide?" |
| 11 | **El aviso clasificado** | figura | Ilustración: un tablón de anuncios. Cada palabra pega un papelito que dice **"OFREZCO: soy un sustantivo plural masculino, tema económico"** (key). Y cada palabra camina con un papelito que dice **"BUSCO: mi sustantivo, plural, masculino"** (query). | "El peso es qué tan bien matchea lo que uno busca con lo que el otro ofrece. Igual que buscar departamento." |
| 12 | Y el value | figura | Al lado del aviso, la mercadería. "El aviso dice qué es; el value es lo que te llevás." | "Te podés llevar algo distinto de lo que decía el aviso. El aviso es para encontrarte; el value es el contenido." |
| 13 | Las tres, en el mismo dibujo | figura | Cada palabra con sus tres vectores: Q, K, V, saliendo de su embedding a través de tres cajitas (tres matrices de parámetros). | "Tres copias transformadas de la misma palabra, para tres funciones distintas. Y las tres transformaciones son perillas que se aprenden." |
| 14 | **Movelo** | VIZ | `viz/qkv.html`. | |
| 15 | El puntaje | figura | Producto punto entre una query y una key, dibujado como "qué tan alineadas están dos flechas". Dos flechas alineadas: puntaje alto. Perpendiculares: cero. | "Producto punto suena horrible y es 'cuánto apuntan para el mismo lado'." |
| 16 | De puntajes a porcentajes | figura | Cuatro puntajes crudos (3.2, 1.1, -0.5, 0.8) convertidos por softmax a (0.62, 0.15, 0.05, 0.18), con las barras al lado. | "Softmax = convertir puntajes en porcentajes que suman 100, exagerando un poco al ganador. Eso es todo. Y va a volver en la clase 8 con la temperatura." |
| 17 | **La fórmula** | fórmula | `Attention(Q,K,V) = softmax(QKᵀ/√d)·V`, con **cada símbolo pintado del color de su parte en la analogía del aviso** y una leyenda debajo traduciendo cada pedazo. | "Ahí está. Ya la entienden entera. Lo único que no expliqué es el √d, y es un detalle de escala para que los números no se disparen." |
| 18 | Bloque práctico 1 | texto | Consignas: attention a mano en el notebook. | "25 minutos. Van a escribir attention en 12 líneas." |
| 19 | Volvimos | discusión | ¿Sumaron 1 las filas? | "Si no suman 1, algo se rompió. Es la mejor verificación que hay." |
| 20 | Decisión 1: no espiar el futuro | figura | La matriz de atención con el triángulo superior tachado. Al lado: por qué. Si el modelo tiene que predecir la palabra 5 y puede mirar la palabra 6, no aprende nada: copia. | "Es hacer trampa en el examen. Se tapa con la máscara causal." |
| 21 | **La matriz** | VIZ | `viz/matriz-de-atencion.html`. | Muestra la matriz completa y después con máscara. |
| 22 | Decisión 2: varias cabezas | figura | Tres mapas de atención de la misma oración con patrones distintos: uno que conecta verbos con sujetos, uno que conecta con la palabra anterior, uno que agrupa por tema. | "Distintos tipos de relación al mismo tiempo. Como tener tres codificadores leyendo el mismo texto con tres libros de códigos distintos." |
| 23 | **Las cabezas** | VIZ | `viz/cabezas.html`. | |
| 24 | Decisión 3: la posición | figura | La misma oración desordenada. Para attention pura, **es la misma entrada**: no hay noción de orden. | "Volvimos a la bolsa de palabras de la clase pasada. Attention sola no sabe qué viene antes." |
| 25 | Positional encoding | figura | A cada palabra se le suma un vector que codifica su posición. Dibujado como "un sellito de número de orden". | "Se le pega un sello con el número de posición. Con eso, la palabra 'no' en la posición 3 es distinta de la misma en la posición 20." |
| 26 | El bloque completo | figura | Diagrama del bloque: entrada → attention → (+entrada) → norm → MLP → (+) → norm → salida. Con cada pieza rotulada con su función en castellano. | "Cuatro piezas. Vamos una por una." |
| 27 | La conexión residual | figura | Un desvío que rodea el bloque y vuelve a sumarse. | "Es una fotocopia de lo que entró, que se suma a la salida. Sirve para que la información no se pierda al apilar 12 bloques, y para que el gradiente de la clase 3 llegue hasta abajo. Es una de esas ideas simples que cambiaron todo." |
| 28 | El MLP de adentro | figura | Las dos capas densas con ReLU. | "¿Se acuerdan de la clase 2? Ahí está, la misma suma de rampas. Nunca se fue." |
| 29 | La normalización | texto | Reescalar para que los números no se vayan a las nubes ni se aplasten. | "Plomería. Importa que esté, no importa el detalle." |
| 30 | Apilar bloques | figura | 6 bloques idénticos, uno arriba del otro. | "Se apila el mismo bloque N veces. GPT-2 chico tiene 12. Los grandes, más de 100. No hay una idea nueva por piso: es el mismo piso repetido." |
| 31 | Bloque práctico 2 | texto | Consignas: armar el bloque completo y verificar formas. | "30 minutos. Al final de esto tienen un transformer entero. Apagado, pero entero." |
| 32 | **La advertencia** | figura | Un mapa de atención hermoso, y al lado la pregunta: ¿esto explica por qué el modelo dijo lo que dijo? | "No. Attention te dice de dónde vino la información, no por qué se tomó la decisión. Hay literatura entera sobre esto: *Attention is not Explanation*." |
| 33 | `[EL LUNES]` | texto | Si leés un paper que interpreta mapas de atención como si fueran evidencia de razonamiento del modelo, ahí tenés un comentario de revisor. Y si vos los usás, reportalos como exploratorio, no como explicación. | "Esto es de lo más útil que se llevan hoy: saber cuándo NO creerle a una figura linda." |
| 34 | El puente | texto | "Tenemos la máquina construida. La clase que viene le damos de comer 40 años de debates parlamentarios y la vemos aprender a escribir. Y después traducimos cada pieza a algo que ChatGPT hace." | |
| 35 | Glosario de hoy | texto | attention, self-attention, query, key, value, producto punto, softmax, máscara causal, cabeza, multi-head, positional encoding, conexión residual, normalización, bloque transformer. | |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/attention-como-mesa.html` — **la viz central de la clase**
- **Qué se ve.** Una oración real de debate parlamentario (~15 palabras) dispuesta horizontalmente,
  cada palabra en una cajita. Al hacer **clic en una palabra**, esa palabra se resalta y salen
  **arcos curvos** hacia todas las demás, con grosor y opacidad proporcionales al peso de atención.
  Sobre cada arco, el peso en porcentaje. Debajo, una barra apilada que muestra cómo se reparte el
  100%.
- **Controles.**
  - Clic en cualquier palabra para ver su mapa.
  - Selector de oración (5 oraciones preparadas, cada una con un fenómeno lingüístico distinto:
    una anáfora, una negación, una subordinada larga, una enumeración, una cita).
  - Toggle **"máscara causal"**: al activarlo, los arcos hacia la derecha desaparecen.
  - Toggle "mostrar todas a la vez" (que produce el heatmap, y conecta con la viz 3.4).
  - Selector de **cabeza** (1 a 4), que cambia el patrón. Conecta con la viz 3.3.
- **Qué tiene que hacer clic.** Que attention es **direccional y por palabra**: cada palabra tiene su
  propio mapa, y el mapa de "lo" no se parece en nada al de "el".
- **Momento aha.** Hacer clic en el pronombre y ver que el arco más grueso va justo al sustantivo al
  que se refiere. "Encontró el antecedente. Nadie le enseñó gramática."
- **Honestidad requerida.** Los pesos deben provenir de un modelo real (puede ser el mini-GPT de la
  clase 8, ya entrenado, con los pesos exportados a JSON) **o** estar rotulados como ilustrativos.
  Preferencia fuerte: usar los del modelo real, aunque el patrón sea menos prolijo. Un patrón
  imperfecto real enseña más que uno perfecto inventado, y permite decir "miren, esta cabeza hace
  algo que no entendemos", que es la verdad del campo.

### 3.2 `viz/qkv.html`
- **Qué se ve.** Tres columnas para una oración de 6 palabras. Cada palabra muestra sus tres
  vectores como **flechas en un plano 2D** (se usa d=2 para poder dibujarlas), con Q en un color,
  K en otro, V en un tercero. Al centro, un panel de "matching": se elige una palabra como
  **preguntadora** y se ve su flecha Q comparada con las K de todas las demás, con el ángulo
  marcado y el puntaje calculado.
- **Controles.** Selector de palabra preguntadora. Sliders que **rotan** las matrices Q y K (es
  decir, cambian los parámetros aprendidos), mostrando cómo cambian todos los pesos. Botón
  "así lo aprendió el modelo" que vuelve a los valores entrenados.
- **Qué tiene que hacer clic.** Que Q y K son **transformaciones aprendidas** del mismo embedding, y
  que cambiarlas cambia a quién mira cada palabra. La atención no está dada: se aprende.
- **Momento aha.** Al rotar la matriz K: "cambió el aviso que publica cada palabra, y ahora el
  pronombre mira a otro lado. Estas rotaciones son las perillas."
- **Detalle de implementación.** Usar d=2 es una simplificación honesta y hay que rotularla: "los
  modelos reales usan 64 o más dimensiones por cabeza; acá usamos 2 para poder dibujarlas".

### 3.3 `viz/cabezas.html`
- **Qué se ve.** Cuatro mapas de atención de la **misma oración**, en grilla 2x2, uno por cabeza,
  con títulos descriptivos derivados de lo que hace cada una ("mira a la palabra anterior",
  "conecta verbo con sujeto", "se enfoca en la primera palabra", "difusa / no interpretable").
- **Controles.** Selector de oración. Botón "superponer" que muestra la suma de las 4.
- **Qué tiene que hacer clic.** Que las cabezas se especializan solas, y que **algunas no hacen nada
  interpretable**, y eso es normal.
- **Momento aha.** "Una de las cuatro cabezas no se entiende. En un modelo real, la mayoría no se
  entiende. Y sin embargo funciona."
- **Nota pedagógica.** Incluir la cabeza no interpretable es una decisión deliberada contra la
  narrativa de que "cada cabeza tiene un rol lingüístico claro", que es una simplificación que
  circula mucho y que la literatura de interpretabilidad no sostiene.

### 3.4 `viz/matriz-de-atencion.html`
- **Qué se ve.** El heatmap cuadrado: filas = palabra que pregunta, columnas = palabra mirada.
  Escala de color secuencial. Con las palabras rotuladas en los dos ejes.
- **Controles.** Toggle **"máscara causal"** (aparece el triángulo gris). Hover sobre una celda:
  se resalta la fila y la columna y se muestra "la palabra X le presta 34% de su atención a la
  palabra Y". Slider "posición actual" que recorre las filas de arriba a abajo, simulando la
  generación palabra por palabra: **se ve crecer el triángulo**.
- **Qué tiene que hacer clic.** Que las **filas** suman 1 (cada palabra reparte su 100%) y las
  columnas no. Es la confusión más frecuente al leer estos heatmaps.
- **Momento aha.** Con el slider de posición: "cuando el modelo está escribiendo la palabra 7, sólo
  existen 7 columnas. Las de la derecha todavía no pasaron."
- **Detalle.** Un panel que muestra la suma de cada fila (siempre 1.00) y la de cada columna
  (cualquier cosa). Esa asimetría es el contenido.

### 3.5 Reutilización: `viz/supuestos-de-arquitectura.html`
Se **reutiliza la viz de la clase 5** con las filas de RNN y Transformer ahora desbloqueadas y con
contenido. El estudiante reconoce la herramienta y ve que "se le llenó una fila más". Es un gesto
chiquito de continuidad que vale mucho.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** < 3 minutos, CPU (no se entrena nada pesado hoy). **Dependencias:** torch,
numpy, matplotlib.

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Objetivo: hoy **construimos**, no entrenamos. | Expectativa explícita. |
| 2 | code | Imports. Carga de los embeddings entrenados en la clase 6 (o se reentrenan en 30 seg). Una oración de ejemplo tokenizada. | Continuidad con la clase 6. |
| 3 | md | **Promedio ponderado a mano.** | |
| 4 | code | Tres vectores de 2 dimensiones y tres pesos que suman 1. Calcular el promedio ponderado con una multiplicación y una suma. Graficar los tres vectores y el resultado como flechas. | La aritmética de la slide 8, en código. Se ve que el resultado cae "entre" los tres. |
| 5 | md | `TODO 1` — Cambiá los pesos para que el resultado quede casi encima del primer vector. *Pista: los pesos tienen que seguir sumando 1.* | |
| 6 | md | **Attention, paso a paso.** | |
| 7 | code | Definir `X` (matriz de embeddings de la oración, forma `(n_palabras, d)`). Imprimir su forma. | Se hace explícito el hábito de imprimir `.shape` en cada paso. |
| 8 | code | Crear `W_q`, `W_k`, `W_v` al azar. Calcular `Q = X @ W_q`, etc. Imprimir formas. | |
| 9 | code | `puntajes = Q @ K.T` → imprimir la matriz y su forma `(n, n)`. Visualizar como heatmap **antes** del softmax (números feos, positivos y negativos). | Ver el "antes" hace entender qué hace el softmax. |
| 10 | code | Aplicar softmax por filas. Heatmap del "después". `assert` de que las filas suman 1. | |
| 11 | md | `TODO 2` — Verificá que las **columnas** no suman 1. ¿Por qué esa asimetría? *Pista: cada palabra reparte su propia atención; nada obliga a que una palabra sea mirada en total 100%.* | |
| 12 | code | `salida = pesos @ V`. Imprimir formas. Comparar `X` y `salida`: mismas dimensiones, contenidos distintos. | "Entró una oración, salió una oración con cada palabra 'contextualizada'." |
| 13 | md | **La máscara causal.** | |
| 14 | code | Construir la máscara triangular con `torch.tril`, aplicarla poniendo `-inf` **antes** del softmax, y comparar los dos heatmaps. | El `-inf` antes del softmax es un detalle que confunde: se explica que es "puntaje tan bajo que después del softmax queda 0". |
| 15 | md | `TODO 3` — ¿Qué pasa si aplicás la máscara **después** del softmax en vez de antes? Probalo y mirá si las filas siguen sumando 1. *Pista: no van a sumar 1. Eso rompe el promedio ponderado.* | Un error real y frecuente, convertido en ejercicio. |
| 16 | md | **Multi-head.** | |
| 17 | code | Envolver lo anterior en una función `attention(X, Wq, Wk, Wv, mask)`. Llamarla 4 veces con matrices distintas. Concatenar las salidas. Graficar los 4 heatmaps. | Se ve que "multi-head" es literalmente "hacerlo 4 veces con otras perillas y pegar los resultados". |
| 18 | md | **Positional encoding.** | |
| 19 | code | Demostración: calcular attention sobre la oración y sobre la **misma oración con las palabras permutadas**, sin positional encoding. Verificar que las salidas son las mismas (permutadas). | La demostración de que attention sola es una bolsa de palabras. Callback a la clase 6, en código. |
| 20 | code | Agregar el positional encoding (senos y cosenos, o embeddings de posición aprendidos: **preferir los aprendidos, son más simples de explicar**) y repetir. Ahora las salidas difieren. | |
| 21 | md | **El bloque completo.** | |
| 22 | code | Clase `BloqueTransformer(nn.Module)` con attention multi-head, MLP, dos LayerNorm y las dos conexiones residuales. ~30 líneas, **comentadas línea por línea con su función en castellano**. | La celda más larga del notebook. Se lee en clase entera. |
| 23 | code | Pasar un batch de prueba y verificar que la forma de salida es igual a la de entrada. `print` de todas las formas intermedias. | La verificación de formas es el hábito profesional que se enseña acá. |
| 24 | md | `TODO 4` — Sacá la conexión residual (borrá el `+ x`) y mirá qué pasa con la magnitud de la salida después de apilar 6 bloques. *Pista: imprimí `salida.std()` con y sin residual.* | Se ve la señal desvanecerse. Motiva la residual con evidencia. |
| 25 | code | Apilar 6 bloques y contar parámetros. Comparar con la red de la clase 4. | "Pasamos de 65 parámetros a 300.000. Y en la clase 8 vamos a un millón y medio." |
| 26 | md | `TODO 5 (interpretación)` — Mirá el mapa de atención de una cabeza. Escribí una hipótesis de qué está haciendo. Y después escribí por qué esa hipótesis **no es una explicación** del comportamiento del modelo. | El ejercicio de humildad epistémica de la clase. |
| 27 | md | **Para llevarte** + puente: "en la clase 8 le damos de comer". | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Attention es un tipo de memoria"** | Lo asimilan a la RNN. | Es lo contrario: no hay estado que se arrastre. **Todas las palabras se miran en paralelo, de una.** Esa es la razón por la que se puede entrenar rápido en GPU y por la que hay una ventana de contexto finita (clase 8). |
| **Confundir las filas con las columnas del heatmap** | Leen "esta palabra fue mirada" cuando dice "esta palabra miró". | Viz 3.4 con el panel de sumas de fila y columna. Y la convención dicha en voz alta cada vez: **fila = quien pregunta**. |
| **"Q, K y V son tres cosas distintas"** | Creen que son tres entradas separadas. | Son tres transformaciones **del mismo vector de entrada**. Slide 13 con las tres cajitas saliendo del mismo embedding, y la celda 8 del notebook donde las tres se calculan de `X`. |
| **Miedo al softmax** | La palabra los bloquea. | "Convertir puntajes en porcentajes que suman 100." Slide 16 con los números. Nunca se escribe la fórmula del softmax en esta clase; se escribe recién en la 8, con la temperatura. |
| **"La máscara es para ahorrar cómputo"** | Confunden su propósito. | Es para no hacer trampa. Si podés ver la respuesta, no aprendés a predecirla. Analogía: un examen donde ves la hoja del compañero. |
| **Creer que cada cabeza tiene un rol lingüístico claro** | Sobreinterpretan. | Viz 3.3, con la cabeza deliberadamente no interpretable. |
| **"El mapa de atención explica la decisión"** | La confusión más importante de la clase para esta audiencia. | Slides 32-33. Argumento: se pueden construir mapas de atención muy distintos que producen la **misma** salida; entonces el mapa no determina la salida y no puede explicarla por sí solo. Referencia: Jain & Wallace 2019. |
| **Perderse en las dimensiones** | Errores de shape constantes. | La disciplina de imprimir `.shape` en cada celda, enseñada explícitamente como método, no como accidente. Y la tabla de referencia de formas al final del notebook. |
| **"¿Y esto es todo? ¿Nada más?"** | Decepción, o incredulidad. | Sí, esto es todo. Y es una respuesta importante: la sensación de que "tiene que haber algo más" es la que sostiene la mistificación de la IA. Lo que hay de más es **escala y datos**, no una idea escondida. |

---

## 6. Analogías y metáforas de ciencias sociales

- **El salto de lectura.** La analogía inicial no es una analogía: es el fenómeno. La comprensión
  lectora funciona por resolución de referencias, no por memorización lineal.
- **El aviso clasificado / la ronda de presentación.** En una reunión donde cada uno dice quién es y
  qué necesita, después cada cual habla con quien le sirve. Key = lo que decís que sos; query = lo
  que buscás; value = lo que efectivamente aportás cuando te consultan. La diferencia entre lo que
  alguien **dice que ofrece** y lo que **efectivamente da** es un chiste que funciona y además es
  conceptualmente correcto.
- **El equipo de codificadores con libros distintos.** Las cabezas múltiples: varios analistas leen
  el mismo texto buscando cosas distintas (uno marca actores, otro marca temporalidad, otro marca
  valoración) y después se juntan los resultados. Es exactamente análisis de contenido
  multidimensional.
- **La red de citas.** El mapa de atención se parece a una matriz de adyacencia: quién mira a quién,
  con pesos. Quien haya visto análisis de redes reconoce el objeto inmediatamente, incluyendo la
  asimetría (A cita a B no implica B cita a A) — que es exactamente la asimetría fila/columna.
- **Attention no es explicación / la correlación no es causalidad.** El paralelo es directo y esta
  audiencia lo tiene incorporado: que el modelo haya *mirado* una palabra no prueba que esa palabra
  haya *causado* la salida. Usar el vocabulario que ya tienen ahorra media hora de discusión.
- **La conexión residual como el original del expediente.** Cada oficina agrega su dictamen, pero el
  documento original sigue adjunto. Si cada oficina reemplazara el expediente por su resumen, a la
  quinta oficina no quedaría nada del caso.

---

## 7. Cuestionario: temas a evaluar (11 ítems)

1. **[MC conceptual]** ¿Qué hace el mecanismo de attention?
2. **[MC conceptual]** ¿Cuál es la diferencia entre query, key y value?
3. **[Leer un gráfico]** Un heatmap de atención con las palabras rotuladas. Responder: ¿a qué palabra
   le presta más atención la palabra "X"? Y: ¿qué suma 1, las filas o las columnas?
4. **[Qué pasa si]** Sacás la máscara causal de un modelo que genera texto. ¿Qué aprende el modelo y
   por qué su loss de entrenamiento sería engañosamente buena?
5. **[Qué pasa si]** Sacás el positional encoding. ¿Qué dos frases se volverían indistinguibles?
   Dar un ejemplo propio.
6. **[Cálculo simple]** Dados cuatro puntajes y su softmax ya calculado, verificar que suman 1 e
   identificar cuál recibe más peso. Y: si multiplico todos los puntajes por 3, ¿la distribución se
   afila o se aplana? *(Prefigura la temperatura de la clase 8.)*
7. **[MC]** ¿Para qué sirven las cabezas múltiples?
8. **[MC]** ¿Qué función cumple la conexión residual?
9. **[Conceptual abierta]** Explicá con tus palabras, sin fórmulas, por qué attention resuelve el
   problema de memoria de las RNN. Y mencioná **qué problema nuevo introduce**. *(Costo cuadrático
   con la longitud → ventana de contexto finita. Es la puerta a la clase 8.)*
10. **[Lectura de arquitectura]** Se da el diagrama de un bloque transformer con dos piezas sin
    rótulo, para identificar.
11. **[Criterio / ética aplicada]** Un paper afirma: "el mapa de atención muestra que el modelo se
    basa en la palabra *inmigrante* para clasificar la nota como negativa, lo que evidencia el sesgo
    del modelo". Evaluá esa afirmación: ¿qué parte es defendible y qué parte no? ¿Qué evidencia
    adicional pedirías? *(Se busca: que attention muestra flujo de información, no causalidad; que
    la evidencia adecuada sería una intervención —cambiar la palabra y ver si cambia la predicción—
    y no una inspección del mapa.)*

---

## 8. Referencias

**Para el estudiante:**
- Jay Alammar, *The Illustrated Transformer* — el material visual de referencia. Se les recomienda
  leerlo **después** de esta clase, no antes. `[VERIFICAR URL]`
- 3Blue1Brown, capítulos sobre transformers y attention de la serie de deep learning. `[VERIFICAR URL]`
- Vaswani, A. et al. (2017), *Attention Is All You Need* — se les muestra la primera página para
  desmitificar: es un paper corto y legible en su introducción. `[VERIFICAR]`

**Para el docente:**
- Jain, S. & Wallace, B. (2019), *Attention is not Explanation*, NAACL. **Sustenta las slides 32-33
  y el ítem 11 del cuestionario.** `[VERIFICAR]`
- Wiegreffe, S. & Pinter, Y. (2019), *Attention is not not Explanation* — la réplica. Mencionarla es
  honesto: el debate está abierto y matizado, y mostrar un debate abierto enseña cómo funciona el
  campo. `[VERIFICAR]`
- Karpathy, A., *Let's build GPT: from scratch, in code, spelled out* — el video que estructura las
  clases 7 y 8. **El equipo que construya estas clases debe verlo entero antes de escribir nada.**
  `[VERIFICAR URL]`
- Elhage, N. et al., *A Mathematical Framework for Transformer Circuits* — sólo para el docente
  curioso; no se asigna. `[VERIFICAR URL]`
