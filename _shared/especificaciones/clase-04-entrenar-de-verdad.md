# Clase 4 — El ciclo de entrenamiento, y la diferencia entre dibujar y calcar
**Directorio:** `clases/04-entrenar-de-verdad/`
**Duración:** 120 min · **Prerrequisitos:** clases 1-3 · **Cierre del módulo 1**

---

## 1. Narrativa de la clase

Esta clase tiene dos mitades con funciones muy distintas.

La **primera mitad es de integración**: se juntan las tres clases anteriores en un mecanismo que
funciona, y se le pone el nombre de la herramienta real (PyTorch). El objetivo emocional acá es el
alivio y la potencia: "todo esto que hicimos a mano son cinco líneas, y ahora las cinco líneas no
te dan miedo porque sabés qué hace cada una". Es importante que PyTorch llegue **después** del
trabajo manual: la abstracción es una recompensa, no un atajo.

La **segunda mitad es de desconfianza**, y es la más importante del curso hasta acá para la práctica
profesional de esta audiencia. El sobreajuste no es un tecnicismo: es *el* modo en que estos métodos
producen hallazgos falsos publicables. Un cientista social que salga de este curso sabiendo
diagnosticar overfitting y partir datos correctamente ya justificó las diez clases, aunque no
recuerde qué es una ReLU.

El hilo:

1. **La trampa del 99%.** Se abre con dos modelos y el aula elige mal. Elegir mal es el punto.
2. **El ciclo, pieza por pieza.** Forward → loss → backward → step → repetir. Cada flecha del
   diagrama tiene su línea de PyTorch. Se muestra el diagrama y el código lado a lado, siempre.
3. **El reencuentro.** Se entrena la red de la clase 2, con el descenso de la clase 3, sobre los
   datos de la clase 1. Cuando aparece la curva ajustada, el docente pone al lado la foto del
   ajuste a ojo de la clase 1. **El mismo problema, resuelto cuatro veces, cada vez mejor.** Ese
   reconocimiento es el pago emocional del módulo.
4. **La vuelta de tuerca.** Se sube la capacidad del modelo y el ajuste mejora... y mejora... y
   sigue mejorando. Y ahí se hace la pregunta: "¿en qué momento esto dejó de ser bueno?". Se retoma
   la imagen sembrada en la clase 2 (el botón de 32 rampas).
5. **Datos que el modelo nunca vio.** La partición. Se hace visible que sin datos apartados **no
   hay manera de darse cuenta**: la loss de entrenamiento baja igual en los dos casos. La ceguera
   es el punto.
6. **Las curvas gemelas.** Train y validación en el mismo gráfico. La tijera que se abre. Early
   stopping como consecuencia obvia, no como técnica nueva.
7. **La disciplina.** Test una sola vez. Por qué mirar el test muchas veces es una forma lenta de
   sobreajustar a mano — y el paralelo directo con el p-hacking, que esta audiencia conoce bien.
8. **Cierre de módulo.** Una slide con las cuatro clases y la promesa de que a partir de la próxima
   los datos dejan de ser números sueltos.

`[CALLBACK DIBUJO]` — la formulación de hoy: **"dibujar es capturar la forma; calcar es copiar cada
manchita del original, incluidas las que son suciedad del papel."** Un modelo con demasiadas
perillas calca. La imagen del calco tiene que aparecer literalmente dibujada en una slide.

---




## 1.5 Presupuesto de tiempo (120 min)

Copiado del **plan minuto a minuto de `PROGRAMA.md`** y mapeado a los números de
slide de la sección 2. Si el bloque no entra en su casilla se recorta el bloque,
nunca la pausa. Qué se recorta si se atrasa y qué se agrega si sobra va en
`notas-docente.md`.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0-10 | Gancho | 1-4 | Modelo A vs modelo B: el que acierta todo y no sirve para nada. |
| 10-30 | El ciclo | 5-15 | Las cinco líneas del loop en PyTorch, una por una, más qué es un tensor. |
| 30-50 | Manos 1 | 16 | Notebook: el primer loop completo escrito por ellos. |
| 50-60 | **PAUSA** | — | **En serio, pausa.** Slide propia después de la 16. |
| 60-80 | Calcar vs dibujar | 17-29 | Sobreajuste, validación, early stopping, la tijera. |
| 80-105 | Manos 2 | 30 | De a dos: provocar el sobreajuste y verlo en la curva de validación. |
| 105-120 | Cierre + evaluación de la unidad | 31-36 | La regla de oro, `[EN TU INVESTIGACIÓN]`, cierre del módulo 1, el puente a la clase 5. |

**La pausa de 10 minutos no es negociable y va marcada con una slide propia**
(`<section class="pausa">`), para que no se la coma el entusiasmo.

---

## 2. Guion de slides (36 slides)

| # | Slide | Tipo | Contenido | Qué dice el docente |
|---|---|---|---|---|
| 1 | Entrenar de verdad | portada | | |
| 2 | **Modelo A vs modelo B** | figura | Dos tarjetas: A: 99% de aciertos. B: 84%. Mismo problema (clasificar el tono de titulares). | "¿Cuál publicarían? Voten." Casi todos eligen A. |
| 3 | Con datos nuevos | figura | Las mismas tarjetas, ahora con una segunda fila: A: 61%. B: 82%. | Silencio. "El A no aprendió nada. Se aprendió los datos de memoria." |
| 4 | El error que vamos a evitar hoy | texto | "Este es el error metodológico más común y más caro de todo el campo. Está en papers publicados." | "Al final de hoy lo van a poder detectar en el trabajo de otro y, más importante, en el propio." |
| 5 | Dónde quedamos | figura | Las tres piezas de las clases 1-3 como engranajes sueltos. | "Hoy los conectamos." |
| 6 | El ciclo | figura | Diagrama circular grande: **datos → predicción (forward) → loss → gradientes (backward) → actualizar → volver**. | Lo recorre despacio, dos vueltas. |
| 7 | **Un paso a la vez** | VIZ | `viz/anatomia-del-loop.html`. | Aprieta "un paso" cinco veces mostrando los números reales. |
| 8 | Lo mismo, en PyTorch | código | Las 5 líneas del loop, con **colores que corresponden a las flechas del diagrama de la slide 6**. | "Cinco líneas. Y ustedes ya escribieron las cinco a mano la clase pasada." |
| 9 | `pred = modelo(x)` | código | La línea sola, en grande, con el diagrama al lado y la flecha correspondiente resaltada. | "Esto es la máquina de dibujar de la clase 2." |
| 10 | `loss = criterio(pred, y)` | código | Ídem. | "Esto es el número gris de la clase 1 y la decisión metodológica de la clase 3." |
| 11 | `loss.backward()` | código | Ídem. | "Esto es backpropagation. Calcula todos los gradientes de una. Es la línea que hace que este campo exista." |
| 12 | `optimizador.step()` | código | Ídem. | "Este es el paso cuesta abajo de la clase 3." |
| 13 | `optimizador.zero_grad()` | código | Ídem, con un cartel de advertencia. | "Y esta es la línea que todos se olvidan, incluido yo. Si no la ponés, los gradientes se acumulan y el modelo se vuelve loco. Es el error #1 de PyTorch." |
| 14 | Qué es un tensor | figura | Un número, una lista, una tabla, un cubo. Con ejemplos de cada uno en datos sociales (una edad, una serie, una matriz caso-variable, un corpus de documentos por palabras por tiempo). | "Un tensor es una tabla con más de dos dimensiones. Nada más. El nombre es innecesariamente imponente." |
| 15 | Vocabulario del entrenamiento | texto | **epoch** = una pasada por todos los datos. **batch** = el puñado de casos que mirás por vez. **iteración** = un paso. Con un ejemplo numérico concreto (1000 casos, batch 100 → 10 iteraciones = 1 epoch). | "Con el ejemplo numérico alcanza. No lo memoricen." |
| 16 | Bloque práctico 1 | texto | Consignas. | "20 minutos. Van a entrenar la red de la clase 2 sobre los datos de la clase 1." |
| 17 | **El reencuentro** | figura | Lado a lado: la foto del ajuste a ojo de la clase 1 (feo) y la curva entrenada de hoy (buena). Mismo dataset, mismos ejes. | "Este es el mismo problema que en la primera clase movíamos con dos sliders. Miren dónde llegamos en cuatro clases." |
| 18 | ¿Y si le pongo más neuronas? | figura | Tres ajustes con 4, 16 y 64 neuronas. La loss de entrenamiento: 0.8, 0.3, 0.02. | "Mejora. Mejora. Mejora. ¿Entonces le pongo 4000?" |
| 19 | **El calco** | figura | Ajuste con 200 neuronas: la curva pasa **exactamente** por todos los puntos, con oscilaciones absurdas entre ellos. Al lado, una ilustración: alguien calcando un dibujo y copiando también una mancha de café. | "Loss de entrenamiento: prácticamente cero. Perfecto. Y es basura." |
| 20 | ¿Por qué es basura? | figura | La misma curva de 200 neuronas, ahora con **cinco puntos nuevos** en rojo, del mismo fenómeno. Están lejísimos de la curva. | "Estos cinco puntos son de la misma realidad y el modelo perfecto los erra por kilómetros." |
| 21 | Dibujar vs calcar | texto | Dos definiciones: **dibujar** = capturar el patrón que se repite. **calcar** = reproducir esta muestra, incluido su ruido. | "El ruido de tu muestra no está en la próxima muestra. Por eso calcar no sirve." |
| 22 | Ustedes ya conocen esto | texto | Paralelos: un modelo con demasiados controles que ajusta perfecto y no replica; el p-hacking; el codificador que aprendió las manías del corpus piloto; la teoría *ad hoc* que explica todo. | "Esto no es un problema nuevo del deep learning. Es su problema de siempre, con más parámetros." |
| 23 | La única defensa | figura | La torta de datos partida en tres: **entrenamiento** (grande), **validación** (mediano), **test** (chico, con un candado dibujado). | "Guardás datos que el modelo no ve. No hay otra. No existe un test estadístico que te salve de esto." |
| 24 | Para qué es cada uno | texto | Entrenamiento: mover las perillas. Validación: elegir **cuántas** perillas (y cuándo parar). Test: el número que reportás, una sola vez. | "La validación se usa muchas veces. El test, una." |
| 25 | **Mové la capacidad** | VIZ | `viz/sobreajuste.html`. | Sube la capacidad despacio. "Miren las dos curvas: la azul sigue bajando, la naranja empezó a subir. Ahí. Justo ahí. Eso es el momento en que dejó de aprender y empezó a memorizar." |
| 26 | La tijera | figura | El gráfico canónico: loss de train bajando, loss de val bajando y después subiendo, con la brecha sombreada y una línea vertical punteada en el mínimo de validación. | "Esta figura la van a ver mil veces. Se llama la tijera y es un diagnóstico." |
| 27 | Early stopping | texto | "Pará cuando la validación empieza a empeorar." Y la advertencia: eso también es usar la validación para decidir, así que la validación tampoco es una medida limpia de desempeño. | "Por eso hacen falta tres conjuntos y no dos." |
| 28 | Más datos también sirve | VIZ | `viz/sobreajuste.html` con el slider de cantidad de datos. | "Miren: dejo la capacidad enorme y subo los datos. La tijera se cierra sola. Capacidad y datos son las dos caras de lo mismo." |
| 29 | Las otras defensas, en una slide | texto | Regularización (penalizar pesos grandes), dropout (apagar neuronas al azar durante el entrenamiento), data augmentation. Una línea cada una, con la intuición. | "No las vamos a usar hoy. Sepan que existen y qué problema atacan: todas hacen lo mismo, le sacan libertad al modelo." |
| 30 | Bloque práctico 2 | texto | Consignas: partición, curvas, early stopping, y el experimento de a dos con hipótesis escrita previa. | "**Escriban la hipótesis antes de correr.** Sí, como en un preregistro. Por algo será." |
| 31 | Resultados del aula | discusión | Espacio para poner en común. | "¿A quién le dio distinto de lo que esperaba? Esos son los interesantes." |
| 32 | La regla de oro | texto | **El test se mira una sola vez, al final, cuando ya no vas a cambiar nada.** | "Si mirás el test, ajustás, y volvés a mirar, estás optimizando contra el test a mano. Es p-hacking artesanal." |
| 33 | `[EN TU INVESTIGACIÓN]` | texto | La receta: partí los datos **antes** de mirar nada; separá por tiempo o por grupo si tu problema lo pide (no siempre al azar); reportá train, val y test. Y para revisar papers: si no dice cómo partió los datos, preguntalo. | "Si un paper reporta desempeño y no dice sobre qué datos, no reportó nada." |
| 34 | Cuidado con partir al azar | figura | Dos casos donde partir al azar te miente: datos temporales (predecir el pasado con el futuro) y datos agrupados (el mismo diputado en train y en test). | "Este es un error de nivel avanzado que van a cometer igual. Anótenlo." |
| 35 | Cierre del módulo 1 | figura | Una sola slide con las cuatro clases: **perilla → composición → loss → ciclo**, con una miniatura de la viz emblemática de cada una. | "Esto es todo el deep learning. Lo que viene son variaciones sobre esto para tipos de datos distintos." |
| 36 | El puente | texto | "Hasta acá: entra un número, sale un número. Pero tus datos son fotos, discursos, secuencias. **La forma del dato cambia la arquitectura, y la arquitectura es una teoría sobre el mundo.**" | "Clase 5: imágenes." |

---

## 3. Visualizaciones interactivas

### 3.1 `viz/anatomia-del-loop.html`
- **Qué se ve.** El diagrama circular del training loop con 5 estaciones. En el centro, un panel de
  números en vivo: los valores actuales de los parámetros, la predicción, la loss, y los gradientes.
  A la derecha, **un mini-gráfico de los datos con la curva actual** y, abajo, la curva de loss que
  se va construyendo punto a punto.
- **Controles.** Botón **"un paso"** (avanza una estación, no una iteración completa: se recorre
  forward, loss, backward, step de a una, iluminando la estación activa y mostrando qué número
  cambió). Botón "una iteración completa". Botón "correr 50". Slider de learning rate. Botón reset.
- **Qué tiene que hacer clic.** Que el entrenamiento no es una caja negra sino **cuatro operaciones
  que se repiten**, y que en `backward` no cambia ningún parámetro (sólo se calculan gradientes) y
  en `step` no se calcula nada nuevo (sólo se aplican). Esa separación es fuente de confusión y esta
  viz existe para resolverla.
- **Momento aha.** "Ah, `backward` no mueve nada. Sólo anota para dónde habría que moverse. Recién
  `step` mueve."
- **Detalle.** Cada estación muestra, al iluminarse, **la línea de PyTorch correspondiente** en un
  recuadro de código. Es el puente entre el diagrama y el notebook.

### 3.2 `viz/sobreajuste.html` — **la viz central de la clase**
- **Qué se ve.** Tres paneles.
  - **Panel principal (grande):** los datos. Puntos azules = entrenamiento, puntos naranjas =
    validación (visualmente distintos, con leyenda). La curva que el modelo dibuja, en negro.
    Y —clave— **la "verdad" subyacente en gris punteado**: la función real que generó los datos
    antes de agregarle ruido. Poder mostrar la verdad es la ventaja de usar datos sintéticos y hay
    que explotarla acá.
  - **Panel de curvas:** loss de train (azul) y loss de val (naranja) vs capacidad del modelo, con
    el punto actual marcado con una línea vertical.
  - **Panel de números:** loss train, loss val, y la **brecha** entre las dos, con un semáforo
    (verde / amarillo / rojo).
- **Controles.**
  - Slider **"capacidad"** (número de rampas/neuronas: 1 a 60). Es el control estrella.
  - Slider **"cantidad de datos"** (10 a 400).
  - Slider **"cuánto ruido tienen las mediciones"** (0 a alto).
  - Botón **"generar otra muestra"**: vuelve a muestrear del mismo proceso generador y **redibuja
    la curva ajustada**. Con capacidad alta, la curva cambia salvajemente de muestra a muestra; con
    capacidad justa, casi no cambia. **Esta es la mejor demostración de varianza que existe** y hay
    que ponerla.
  - Toggle "mostrar la verdad".
- **Qué tiene que hacer clic.** Tres cosas: (1) la loss de entrenamiento **siempre** mejora con más
  capacidad, así que no sirve como criterio; (2) hay un punto óptimo y está en la validación;
  (3) más datos mueve el punto óptimo hacia la derecha.
- **Momento aha.** Apretar "generar otra muestra" cinco veces con capacidad 60: "la curva salta como
  loca y siempre pasa por todos los puntos. **No está aprendiendo el fenómeno: está aprendiendo la
  muestra.**"
- **Detalle pedagógico.** Un cartel que traduce el estado actual a lenguaje de investigación:
  con brecha grande, "tu modelo aprendió particularidades de **esta** muestra: no va a replicar";
  con capacidad baja, "tu modelo es demasiado rígido para el fenómeno: te estás perdiendo estructura
  real".

### 3.3 `viz/particion.html` (auxiliar, chica pero necesaria)
- **Qué se ve.** 100 casos dibujados como cuadraditos. Se pintan de tres colores según la partición.
- **Controles.** Sliders de proporción train/val/test. Selector de **estrategia de partición**:
  "al azar", "por tiempo", "por grupo (ej. por diputado)".
- **Qué tiene que hacer clic.** Que con datos temporales, partir al azar mete el futuro en el
  entrenamiento; con datos agrupados, mete al mismo sujeto en train y en test. La viz muestra
  explícitamente las **fugas** (leakage) resaltando en rojo los casos problemáticos.
- **Momento aha.** "Con datos de panel, partir al azar es hacer trampa sin darte cuenta."
- **Nota.** Es la viz que más directamente les sirve *en su investigación*. Corta pero indispensable.

---

## 4. Especificación del notebook

**Tiempo de ejecución:** < 4 minutos, CPU. **Dependencias:** torch, numpy, matplotlib.
**Primera celda instala torch si falta** (en Colab ya está).

| # | Tipo | Contenido | Notas |
|---|---|---|---|
| 1 | md | Qué vamos a hacer + advertencia de que hoy aparece PyTorch. | |
| 2 | code | Imports, `torch.manual_seed(0)` con comentario explicando **por qué se fija la semilla** (reproducibilidad: tema de la clase 10, se siembra hoy). | |
| 3 | md | **Tensores en 3 minutos.** | |
| 4 | code | Crear tensores, ver `.shape`, sumar, multiplicar. Comparación explícita con arrays de numpy. | Corto. No es una clase de PyTorch. |
| 5 | md | **Autograd: la magia que ya entendés.** | |
| 6 | code | `x = torch.tensor(3.0, requires_grad=True)`, `y = x**2`, `y.backward()`, `print(x.grad)` → 6.0. Y al lado, la derivada numérica de la clase 3 dando 6.0000001. | **Momento clave**: lo que hicieron a mano la clase pasada, hecho exacto y automático. |
| 7 | md | `TODO 1` — Probá con `y = x**3` en `x=2`. ¿Cuánto da? Verificalo con la derivada numérica de la clase 3. *Pista: copiá la función `derivada_numerica` del notebook anterior.* | |
| 8 | md | **El modelo.** | |
| 9 | code | La red de la clase 2, ahora como `nn.Sequential(nn.Linear(1,16), nn.ReLU(), nn.Linear(16,1))`. Al lado, en comentario, **la misma red escrita a mano de la clase 2**. Y `sum(p.numel() for p in modelo.parameters())` para contar perillas. | La equivalencia explícita es obligatoria: sin ella, PyTorch se vuelve magia. |
| 10 | md | **El loop.** | |
| 11 | code | El training loop completo, 10 líneas, **con un comentario numerado por línea** que remite al diagrama de las slides. | |
| 12 | code | Gráficos: curva de loss + ajuste final sobre los datos. | |
| 13 | md | `TODO 2` — Cambiá `16` por `4` y después por `64`. Anotá la loss final de cada uno en una tabla en este comentario. | |
| 14 | md | `TODO 3` — Cambiá el learning rate a 1.0. ¿Reconocés la firma de la curva? *Pista: es una de las tres que viste en la viz de la clase 3.* | Refuerzo del diagnóstico visual. |
| 15 | md | **Partir los datos.** | |
| 16 | code | Split 60/20/20 con índices explícitos (nada de `train_test_split` todavía: se hace a mano con slicing para que se vea que no hay magia). Se imprime cuántos casos quedan en cada uno. | |
| 17 | code | Training loop modificado: calcula loss de train **y** de validación cada epoch, guarda las dos listas. | |
| 18 | code | El gráfico de la tijera: las dos curvas, con la línea vertical en el mínimo de validación. | La figura que tienen que saber leer. |
| 19 | md | `TODO 4` — Subí las neuronas a 256 y bajá los datos de entrenamiento a 15. Corré. Describí la tijera que te dio. *Pista: mirá en qué epoch la curva naranja toca su punto más bajo.* | Fabricar overfitting a propósito. |
| 20 | code | Early stopping implementado en 5 líneas (guardar el mejor estado, con `paciencia`). | |
| 21 | md | **El experimento de a dos.** Consigna: elegí UNA cosa para cambiar (neuronas, capas, lr, cantidad de datos, ruido). **Escribí acá abajo tu hipótesis ANTES de correr.** Después corré, y escribí si acertaste. | Celda de markdown con un espacio para completar. La disciplina del preregistro, en miniatura. |
| 22 | code | Celda de experimentación libre, con la estructura ya armada para que sólo cambien un parámetro. | |
| 23 | md | **El test, una sola vez.** | |
| 24 | code | Evaluación en test. Con un comentario grande: `# ⚠️ Esta celda se corre UNA vez, al final. Si volvés a cambiar el modelo, tu test ya está quemado.` | |
| 25 | md | `TODO 5 (criterio)` — Escribí en dos oraciones cómo reportarías este resultado en un paper. ¿Qué números incluirías y cuáles no? | Prepara la clase 10. |
| 26 | md | **Para llevarte** + cierre del módulo + puente. | |

---

## 5. Errores y confusiones típicas

| Confusión | Cómo se manifiesta | Cómo se desarma |
|---|---|---|
| **"Más capacidad siempre es mejor"** | Es la intuición por defecto y viene reforzada por el marketing de los modelos grandes. | Viz 3.2 + el botón "generar otra muestra". Y el matiz honesto: con **muchísimos** datos, más capacidad sí suele ser mejor, y por eso los modelos grandes funcionan. La regla es la relación capacidad/datos, no la capacidad sola. Decir el matiz evita que después se sientan engañados. |
| **Olvidarse `zero_grad()`** | Los gradientes se acumulan y la loss hace cosas raras. | Se anticipa en la slide 13 y se pone un ejercicio opcional donde se saca a propósito para ver el desastre. Aprender el bug produciéndolo. |
| **Confundir epoch con iteración** | Reportan "entrené 1000 iteraciones" cuando quieren decir epochs. | La slide 15 con el ejemplo numérico concreto, y un `print` en el notebook que muestra los dos contadores en paralelo. |
| **"La validación es para medir qué tan bueno es el modelo"** | Reportan el número de validación como resultado final. | Se distingue: validación = **tomar decisiones** (cuántas neuronas, cuándo parar). Test = **reportar**. Si usaste la validación para decidir, el número de validación ya está contaminado. |
| **Mirar el test varias veces** | "Probé cinco configuraciones y elegí la que mejor dio en test." | El paralelo con el p-hacking, dicho con esas palabras. Esta audiencia entiende inmediatamente por qué está mal, si se lo traduce a su vocabulario. |
| **Partir al azar datos temporales o de panel** | El más difícil de ver y el más frecuente en ciencias sociales. | Viz 3.3, con el resaltado de fugas. Y la pregunta operativa: "¿tu modelo, al predecir el caso del test, está usando información que en la vida real no habría tenido todavía?" |
| **Creer que el modelo "entiende" cuando ajusta bien** | Atribución de comprensión. | La curva de 200 neuronas ajusta perfecto y erra los puntos nuevos por kilómetros. La evidencia visual es suficiente. |
| **"¿Cuántos epochs hay que hacer?"** | Buscan una regla. | "Hasta que la validación deje de mejorar. Por eso existe early stopping: la respuesta la da el gráfico, no una tabla." |
| **Pánico ante `nn.Sequential`** | Sienten que apareció magia nueva. | La celda 9, con la red escrita a mano al lado. Se corre y se verifica que dan el mismo resultado. |

---

## 6. Analogías y metáforas de ciencias sociales

- **El calco.** La imagen central: dibujar es capturar la forma; calcar es copiar cada manchita,
  incluida la suciedad del papel. La suciedad del papel es el error de medición de tu muestra.
- **El modelo saturado de controles.** Todos vieron una regresión con tantos controles que el R²
  es hermoso y el modelo no dice nada. Es exactamente lo mismo: capacidad vs datos.
- **El p-hacking y el preregistro.** Mirar el test muchas veces es p-hacking manual. El
  preregistro es, funcionalmente, apartar el test antes de mirar. La analogía es tan exacta que
  conviene hacerla explícita: **el conjunto de test es el preregistro del aprendizaje automático.**
- **El codificador que se malacostumbró.** Un codificador entrenado con un corpus piloto muy
  particular aprende reglas que sólo valen ahí ("cuando dice 'compañeros' es peronismo"). Al
  cambiar de corpus, falla. Es sobreajuste humano y todos lo vivieron.
- **Validez interna vs externa.** El overfitting es, casi literalmente, **validez interna perfecta
  con validez externa nula**. Traducirlo a este par conceptual, que ya manejan, hace que el tema se
  entienda en treinta segundos.
- **La muestra piloto.** Ajustar el instrumento con la misma muestra con la que después vas a
  reportar resultados: nadie lo haría, y sin embargo es lo que hace un modelo sin partición.
- **El caso del diputado repetido.** Si el mismo diputado aparece en train y en test, el modelo
  puede aprenderse su estilo y "predecir" sus discursos de test. La partición por grupo es la
  versión ML del problema de la independencia de las observaciones.

---

## 7. Cuestionario: temas a evaluar (12 ítems)

1. **[MC conceptual]** ¿Qué es el overfitting?
2. **[MC conceptual]** ¿Para qué sirve el conjunto de validación, a diferencia del de test?
3. **[Leer un gráfico]** La tijera. Marcar en qué epoch habría que haber parado y explicar por qué.
4. **[Leer un gráfico]** Cuatro combinaciones de loss train/val (ambas altas; train baja y val alta;
   ambas bajas; train alta y val baja) y sus cuatro diagnósticos, para aparear. *(El cuarto caso es
   raro y sugiere un problema de partición: buen ítem de discusión.)*
5. **[Qué pasa si]** Tenés 30 casos y un modelo con 5000 parámetros. ¿Qué esperás que pase con la
   loss de entrenamiento? ¿Y con la de test?
6. **[Qué pasa si]** Duplicás la cantidad de datos manteniendo el modelo. ¿Qué le pasa a la brecha
   entre train y validación?
7. **[Código]** Ordenar las cinco líneas del training loop, que se dan desordenadas.
8. **[Código]** Se muestra un loop al que le falta `zero_grad()`. ¿Qué síntoma esperarías ver?
9. **[Vocabulario]** Definir epoch, batch e iteración con un ejemplo numérico dado
   (1200 casos, batch de 200).
10. **[Aplicación]** Tenés discursos de 50 diputados, 20 discursos cada uno, y querés predecir el
    partido. ¿Cómo partís los datos y por qué **no** al azar?
11. **[Aplicación]** Tenés una serie mensual 2010-2023 y querés predecir conflictividad. ¿Cómo
    partís y por qué?
12. **[Criterio / ética aplicada]** Un paper reporta 94% de accuracy en clasificación automática de
    tono en noticias. No menciona partición de datos. Escribí las **tres** preguntas que le harías
    como revisor, en el tono en que se las escribirías al autor. *(Se busca: ¿sobre qué datos es ese
    94%? ¿cómo partieron? ¿cuál es el baseline / cuál es la clase mayoritaria? Y bonus: ¿cuántas
    configuraciones probaron antes de quedarse con esta?)*

---

## 8. Referencias

**Para el estudiante:**
- Documentación oficial de PyTorch, tutorial *Learn the Basics* — se les señalan sólo las secciones
  de tensores y de training loop, avisando que el resto es para después. `[VERIFICAR URL]`
- Un video corto sobre overfitting con visualización (StatQuest tiene versiones muy accesibles).
  `[VERIFICAR URL]`

**Para el docente:**
- Yarkoni, T. & Westfall, J. (2017), *Choosing Prediction Over Explanation in Psychology*,
  Perspectives on Psychological Science. **La mejor lectura existente para traducir la distinción
  ajuste/predicción al lenguaje de las ciencias sociales.** Muy recomendable asignarla también a los
  estudiantes interesados. `[VERIFICAR]`
- Kapoor, S. & Narayanan, A. (2023), *Leakage and the Reproducibility Crisis in ML-based Science*,
  Patterns. **Es la referencia clave para la slide 34 y para toda la clase 10**: cataloga los tipos
  de fuga de datos en ciencia aplicada. `[VERIFICAR]`
- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*, cap. 7 (model assessment).
  Gratis online. Para consulta. `[VERIFICAR URL]`
