# Guía del docente

**Para quien va a dictar el curso entero.** No es un resumen del programa: eso
está en `PROGRAMA.md`. Esto es lo que necesitás saber para pararte adelante de un
aula de cientistas sociales veinte horas y que salga bien.

Se lee de una sentada, y después se vuelve a la sección que haga falta.

> **La frase que ordena todo el curso, y conviene que la digas en voz alta la
> primera clase:** *"acá no se viene a aprender a usar una biblioteca. Se viene a
> aprender a no dejarse impresionar."* Es literalmente la última slide de la
> clase 10. Si el curso termina con un aula que sabe hacer preguntas incómodas y
> no sabe entrenar un ResNet, salió perfecto.

---

## 1. Qué leer, y con cuánta anticipación

### Una vez, antes de arrancar el curso (unas cuatro horas)

| Qué | Por qué |
|---|---|
| `PROGRAMA.md`, entero | La filosofía, el plan de las diez clases, y sobre todo la **§4, el mapa de puentes**. Si no tenés el mapa de puentes en la cabeza, las clases se sienten sueltas. |
| `datos/README.md`, entero | **La media hora que más rinde de toda la preparación.** Cada corpus tiene una trampa documentada, y varias de esas trampas *son* contenido del curso. Si no las conocés, vas a afirmar cosas que no son. |
| `recursos/glosario.md` | Para tener a mano la traducción que usa el curso. Si vos decís "pérdida" y las slides dicen "loss", el aula reaprende vocabulario cada martes. |
| `_shared/especificaciones/00-ESTADO-CURSO.md` | Qué está medido, qué quedó abierto y qué hay que arreglar antes de dictar. |

### Antes de cada clase (una hora y media, la noche anterior)

1. **`clases/NN-slug/notas-docente.md`, entero.** Es el guion hablado: los
   tiempos reales bloque por bloque, las preguntas al aula con las respuestas que
   van a dar, las confusiones típicas con el desarme escrito, qué recortar si te
   atrasás y qué hacer si te sobra tiempo. **Es el documento más importante del
   repo para vos.**
2. **Pasá las slides completas, con `S` abierto** (esa tecla abre las notas del
   docente en una segunda ventana). Cronometrá los tres bloques donde más te
   suele pasar el tiempo.
3. **Corré el notebook entero, en tu máquina y en Colab.** No lo leas: corrélo.
   Los tiempos medidos están en la tabla de la sección 3 de esta guía. La clase 8
   tarda unos cinco minutos y medio; el resto, menos de un minuto y medio.
4. **Abrí cada viz suelta y movela.** Las viz embebidas en las slides van en modo
   compacto para entrar en el iframe; sueltas tienen el título, el pie y los
   textos completos. **Casi todas conviene proyectarlas sueltas**, y las notas te
   dicen cuáles.
5. **Leé el `cuestionario-soluciones.md`.** No para tomarlo: para saber qué se
   supone que quedó claro.

### Cinco minutos antes de entrar

Cada `notas-docente.md` termina con un checklist de cinco minutos. Hacelo.
Lo común a las diez clases:

- [ ] Las slides abiertas y en pantalla completa (`F`), en **modo oscuro si la
      sala tiene mucha luz** (botón abajo a la derecha en las viz; en las slides,
      el tema sigue al del sistema).
- [ ] Las viz de hoy abiertas en **pestañas aparte**, en el orden en que van.
- [ ] El notebook de hoy abierto **y ya corrido** en una ventana aparte: si el
      wifi del aula se cae, tenés los resultados en pantalla.
- [ ] Un plan B sin proyector (ver §2).
- [ ] El reloj a la vista. En serio.

---

## 2. El equipamiento mínimo

**Lo imprescindible:**

- Un **proyector o pantalla** de al menos 1280×720. Todas las slides y las viz se
  probaron a esa resolución. Si la sala es grande, proyectá las viz **sueltas**:
  embebidas en la slide se achican para entrar.
- **Tu** laptop, con el repo bajado. No dependas de la red del aula para dar la
  clase: todo el material abre con `file://` y funciona sin internet. Es a
  propósito.
- Un **pizarrón o una hoja grande**. Hay cuatro o cinco momentos del curso donde
  dibujar dos círculos a mano gana por lejos: la validez de constructo de la
  clase 10 es el más claro.

**Lo deseable:**

- **Que los estudiantes traigan laptop.** El curso tiene 20 bloques de "a las
  manos" (dos por clase, 45 minutos en total por clase) y son la mitad del
  aprendizaje. **De a dos por máquina funciona igual de bien o mejor**: uno
  maneja, el otro lee en voz alta y discute. Con una máquina cada tres empieza a
  perderse gente.
- **Wifi para los estudiantes.** Colab necesita internet. Sin wifi, el curso se
  puede dar igual (ver el plan B), pero perdés los bloques prácticos.

**Plan B sin wifi para los estudiantes** (funciona, y conviene tenerlo pensado):

1. Los notebooks corren locales si alguien instaló Python (ver `recursos/setup.md`
   §2). Llevá el repo en un pendrive.
2. Si eso tampoco: proyectá el notebook y **corrélo vos**, pidiendo al aula que
   te diga qué número cambiar antes de cada celda. Se pierde el hacer, no se
   pierde el ver. Las visualizaciones no necesitan red y siguen siendo el 60 % de
   la clase.
3. Las clases 9 y 10 necesitan Hugging Face para el camino "con red". **Las dos
   tienen un camino sin red ya escrito y probado** (PPMI+SVD y TF-IDF con
   regresión logística): los números cambian, el argumento no. Está en
   `datos/README.md` §3.

---

## 3. Los tiempos, medidos

Los notebooks, corridos de punta a punta con `nbconvert --execute` en CPU, sin
GPU, el 2026-08-29:

| Clase | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Tarda** | 8 s | 9 s | 9 s | 29 s | 1 min 21 s | 19 s | 15 s | **5 min 29 s** | 17 s | 15 s |

En Colab gratis (2 vCPU compartidas) contá **entre una y dos veces** eso: la
clase 5 puede irse a 3-4 minutos y la 8 a 8-10. Ninguna otra pasa del minuto.

**El único notebook que hay que planificar es el de la clase 8**, y ya está
planificado: se lanza el entrenamiento a los 20 minutos, **la pausa de 10 minutos
se toma mientras entrena**, y a los 40 está listo. Si en tu aula tarda más, no
pasa nada: el bloque siguiente no lo necesita terminado.

---

## 4. Un aula con niveles de programación muy distintos

Es la situación normal, no la excepción. En una cohorte típica hay tres grupos:

| Quién | Cuántos | Qué necesita |
|---|---|---|
| **Nunca escribió una línea de código** | un tercio | Que nadie le haga sentir que llegó tarde. |
| **Hizo un curso de R o de Python alguna vez** | la mitad | Que no le repitan lo que ya sabe. |
| **Programa todos los días** | dos o tres | Algo que hacer cuando termina en cinco minutos. |

**Lo que funciona, probado:**

1. **De a dos, y mezclados a propósito.** En el primer práctico de la clase 1
   armá vos las parejas, poniendo a alguien con experiencia con alguien sin. Y
   decí la regla en voz alta: **"el que sabe no toca el teclado"**. Es la regla
   más importante de la cursada y hay que repetirla las diez clases.
2. **Los `TODO` están graduados.** Cada notebook tiene `TODO`s obligatorios y uno
   o dos marcados como opcionales o "para los que terminaron". Ésos son para el
   tercer grupo. No los conviertas en obligatorios.
3. **Nunca digas "esto es fácil".** Está en las reglas de la casa y es la más
   importante de todas: si al que no le sale se entera de que era fácil, la pasa
   peor. Tampoco digas "no se asusten": no se anuncia el susto.
4. **Anticipá los errores en vez de esperarlos.** La mitad de los problemas de
   los bloques prácticos son tres cosas: correr las celdas fuera de orden,
   olvidarse de correr la celda de bootstrap, y que se apagó la sesión de Colab.
   Escribilas en el pizarrón el primer día y señalá el pizarrón en vez de
   explicarlas de nuevo.
5. **El curso no exige saber Python.** Exige poder *leer* Python y cambiar
   números. Decilo explícitamente en la clase 1: es cierto, y baja la ansiedad de
   un tercio del aula de golpe.
6. **Para los que programan:** el ejercicio que los mantiene ocupados sin sacarlos
   del curso es *"rompelo y explicá por qué se rompió"*. Está pedido
   explícitamente en varias clases (el `lr = 1.5` de la clase 3, el prompt que
   rompe el modelo de la clase 8) y funciona porque no es más código: es más
   criterio.

---

## 5. La primera clase, para que nadie se asuste

La deserción de este tipo de curso pasa entre la clase 1 y la 2, y casi siempre
por miedo, no por dificultad. Cinco cosas concretas:

1. **No arranques con el temario.** La clase 1 arranca con una nube de puntos sin
   ejes y la pregunta *"¿qué le pasó a este país?"*. Se discute tres minutos
   antes de que aparezca la palabra "modelo". Que la primera actividad del curso
   sea **interpretar un dato**, que es lo que ellos saben hacer, no programar,
   que es lo que no.
2. **Decí, con estas palabras, para qué NO es el curso.** *"No vas a derivar
   backpropagation. No vas a competir en Kaggle. No vas a salir de acá siendo
   data scientist, y no es el objetivo."* Está en la primera página de
   `PROGRAMA.md` y hay que decirlo en voz alta.
3. **Que corran una celda en los primeros 40 minutos.** El bloque de manos de la
   clase 1 empieza en el minuto 40 y el primer `TODO` es cambiar dos números y
   mirar un gráfico. Nadie se va de la primera clase sin haber corrido algo.
4. **Manden `recursos/setup.md` con dos días de anticipación** y pedí que abran
   Colab **antes** de venir. El que llega con Colab funcionando ya ganó. El que
   no, lo resuelve en los primeros diez minutos del práctico con el compañero.
5. **El chiste de la clase 1 que hay que hacer.** Al final del segundo práctico,
   cuando compitieron por bajar el desajuste a mano: *"ustedes acaban de hacer, a
   mano, con dos perillas y en diez minutos, lo que una computadora hace con mil
   millones de perillas en dos semanas. La idea es exactamente la misma. Lo único
   que falta es que la máquina sepa para dónde mover."* Es verdad, y es la mejor
   inyección de confianza del curso.

**Y una cosa que no hay que hacer:** no prometas que "al final del curso van a
poder hacer X con sus datos". Prometé lo del `[EL LUNES]`: algo chiquito y
concreto **esta semana**. El curso está diseñado alrededor de eso.

---

## 6. Cómo evaluar

### 6.1 Los cuestionarios (formativos, sin nota)

Cada clase tiene `cuestionario.md` y `cuestionario-soluciones.md`: 8 a 12 ítems,
mezcla de opción múltiple conceptual, "qué pasa si…", lectura de gráfico, y
**siempre al menos uno de criterio o ética aplicada**.

**Cómo usarlos, que es lo que importa:** se resuelven en 15 minutos, **de a dos**,
al principio de la clase siguiente, y **no se corrigen con nota**. Se usan para
conversar: pedís que levanten la mano los que contestaron A, los que contestaron
B, y discutís las dos. Las soluciones explican *por qué cada distractor es
tentador*, que es la parte que sirve.

> El cuestionario de la clase 10 declara 50 minutos porque incluye tres ítems de
> diseño y uno de una página. **Para los 15 minutos de rutina, usá las cinco
> preguntas mínimas que el propio archivo lista**, y dejá el resto como
> integrador o como parte del proyecto final.

### 6.2 El proyecto final (la evaluación de verdad)

**Propuesta, y es la que recomendamos:** un proyecto chico sobre **el corpus
propio del estudiante**, hecho de a uno o de a dos, entregado tres o cuatro
semanas después de la clase 10. No es un examen: es un artefacto que después les
sirve.

**La consigna, en seis puntos:**

1. **Una pregunta sustantiva** de tu investigación, que se pueda contestar
   clasificando o midiendo algo sobre un corpus de texto (o de imágenes) que ya
   tenés. Una carilla: la pregunta, por qué importa, y qué esperás encontrar
   **escrito antes de correr nada**.
2. **El corpus, descrito con la forma de una `datasheet`** (clase 10): de dónde
   salió, cómo se recolectó, qué se excluyó, qué licencia tiene, y qué le falta.
3. **Un conjunto de validación etiquetado a mano**: 100 a 200 casos, elegidos al
   azar pero **estratificados**, etiquetados **antes de ver ninguna predicción**.
   Si pueden, que dos personas etiqueten 50 y reporten kappa.
4. **El modelo**, elegido con el criterio de la clase 9 (por cuántas etiquetas
   podés producir, no por cuál técnica está de moda) y **comparado contra un
   baseline tonto**. Puede ser TF-IDF más regresión logística: eso no baja la
   nota, la sube si está justificado.
5. **La validación de la clase 10, no las métricas de la 9.** Un test de placebo
   o un control positivo, tres pares mínimos escritos a mano, y un análisis de
   los falsos positivos. **Esto es lo que se evalúa.**
6. **Una sección de métodos de dos páginas**, con la ficha del modelo, la
   semilla, las versiones y un párrafo de limitaciones que diga para qué **no**
   sirve el instrumento.

**La rúbrica es el checklist del revisor de la clase 10**
(`clases/10-criterio-validacion-y-etica/viz/checklist-revisor.html`), y conviene
entregarla junto con la consigna. Que sepan de antemano con qué se los va a
mirar es parte de la lección.

**Criterio de corrección, dicho sin vueltas:** un proyecto donde el modelo anda
mal y la validación está bien hecha **aprueba mejor** que uno con F1 de 0,91 y
ninguna evidencia de validez. Decilo cuando entregues la consigna. Es la tesis
del curso entero y hay que sostenerla en la nota.

**Alternativa si no tienen corpus propio** (pasa con estudiantes de grado):
auditar un paper publicado que use estas técnicas, con el mismo checklist. Es el
ejercicio de "el juicio" de la clase 10, hecho en serio y por escrito. Sale igual
de bien.

---

## 7. Los diez momentos donde el aula se pierde

Ordenados por clase. Cada uno tiene el síntoma, la causa y el rescate. Están
sacados de las secciones de "confusiones típicas" de los diez
`notas-docente.md`, que traen el desarme largo.

### 1 · Clase 1, minuto ~25 — *variable y parámetro se les mezclan*

**Síntoma:** contestan "las dos mueven la curva" y se quedan callados.
**Causa:** los dos son números y en la fórmula se ven igual.
**Rescate:** la apuesta de la slide 13 **antes** de mover nada: *"si muevo esta
perilla, ¿se mueve la bolita o se mueve la curva?"*. Voto a mano alzada, y recién
después lo movés. Sin la predicción fallida, la viz es decoración. Y la frase que
lo fija: **la variable cambia de caso en caso; el parámetro es el mismo para toda
tu base.**

### 2 · Clase 2, minuto ~30 — *"apilar rectas debería dar algo más complicado"*

**Síntoma:** no aceptan que dos rectas encadenadas den una recta, y sin eso el
resto de la clase no tiene motivo.
**Causa:** es contraintuitivo y es el punto entero de la clase.
**Rescate:** que lo vean, no que se lo cuenten. `viz/sin-no-linealidad.html` con
la apuesta antes. Si igual no cierra: hacelo con números en el pizarrón,
`3(2x+1) − 4` es otra recta, y punto. Después entra ReLU y el alivio es enorme.

### 3 · Clase 3, minuto ~40 — **el salto al espacio de perillas. El momento más difícil del curso.**

**Síntoma:** miran el mapa de la loss y creen que los ejes son los datos.
Preguntan "¿dónde están los años?".
**Causa:** cambió el espacio y nadie lo anunció. En un gráfico los ejes eran año
y porcentaje; ahora los ejes son `a` y `b`, y **cada punto del plano es una recta
entera**.
**Rescate:** anunciá el cambio de espacio **antes** de mostrar el mapa, con las
dos figuras lado a lado y el dedo señalando: *"acá cada punto es un discurso; acá
cada punto es una recta posible"*. Y la pregunta de control de la slide 12: *"si
me muevo un centímetro a la derecha en este mapa, ¿qué cambió?"*. Si no la
contestan, no sigas: repetí. **Este es el momento del curso donde más gente se
pierde, y si se pierde acá se pierde para las clases 4 a 8.**

### 4 · Clase 3, cualquier minuto — *pánico ante la palabra "derivada"*

**Síntoma:** dejan de escuchar apenas la decís.
**Causa:** trauma escolar, casi siempre.
**Rescate:** no la digas primero. Decí **pendiente**, y mostrala como "cuánto
sube si me muevo un poquito para allá". La palabra derivada aparece después, como
sinónimo, cuando ya la vieron moverse. En este curso **no se deriva nada**: se
mide moviéndose un poquito, que es lo que hace el notebook.

### 5 · Clase 4, minuto ~30 — *el primer contacto con PyTorch*

**Síntoma:** se traban con `zero_grad()`, con `nn.Sequential` o con un error de
forma, y se les va el bloque práctico entero.
**Causa:** apareció una herramienta nueva justo cuando estaban siguiendo el hilo.
**Rescate:** está anticipado en las slides: cada línea del loop se traduce a una
flecha del diagrama, y `nn.Sequential` aparece **con la versión a mano al lado y
un `assert` que comprueba que dan lo mismo**. Si igual se traban, contá tu propia
vez que te olvidaste `zero_grad()` y perdiste una tarde. Funciona.

### 6 · Clase 5, bloque práctico — *pánico con las dimensiones*

**Síntoma:** errores de forma en cadena, y frustración.
**Causa:** `(lote, canales, alto, ancho)` es cuatro cosas y ninguna es obvia.
**Rescate:** la disciplina de `print(algo.shape)` **enseñada como hábito
profesional, no como parche**. Y decir en voz alta lo que las notas dicen:
*"pooling, stride y padding son plomería. El día que armes una red los googleás.
No los estudies."*

### 7 · Clase 6, minuto ~65 — *"cerca en el mapa = significa lo mismo"*

**Síntoma:** interpretan la similitud coseno como sinonimia, o peor, como
**acuerdo** entre dos documentos.
**Causa:** el mapa es tan convincente que se lo lee como semántica.
**Rescate:** *"el modelo sabe con quién sale una palabra, no qué quiere decir"*.
Y el contraejemplo del curso: dos palabras antónimas que aparecen en los mismos
contextos quedan **pegadas** en el mapa. Es el momento donde el aula pasa de
maravillada a útil, y no hay que dejarlo pasar.

### 8 · Clase 7, minuto ~35 — *"Q, K y V son tres cosas distintas"*

**Síntoma:** creen que son tres entradas separadas y buscan de dónde salen.
**Causa:** el diagrama con tres cajas invita a eso.
**Rescate:** la slide 13, señalando: **las tres salen del mismo vector**, pasado
por tres transformaciones distintas que son perillas aprendidas. Una palabra
publica un aviso (*key*), busca un aviso (*query*) y aporta algo cuando la miran
(*value*), y las tres cosas son la misma palabra vista de tres maneras.

### 9 · Clases 7 y 10 — *"el mapa de atención explica la decisión"*

**Síntoma:** quieren usar el mapa de atención como evidencia en un paper. Es la
confusión **más peligrosa del curso para esta audiencia**, porque se publica.
**Causa:** el mapa es hermoso y parece una explicación.
**Rescate:** el mapa muestra **por dónde pasó la información**, no **por qué el
modelo decidió**. Está la literatura de los dos lados (*Attention is not
Explanation* y su réplica) y hay que citar las dos: el punto no es que el mapa no
sirva, es que no prueba lo que la gente le hace decir. Se retoma en la clase 10
como caso de validez.

### 10 · Clase 10, minuto ~15 — *la sobrecorrección: "entonces esto no sirve para nada"*

**Síntoma:** el aula termina paralizada y con culpa.
**Causa:** es el fracaso pedagógico típico del final de un curso crítico, y es
**tan malo como el entusiasmo acrítico**.
**Rescate:** dos slides están puestas para esto: la que muestra que el mismo
instrumento que es dañino para **decidir** puede ser valioso para **medir**, y la
lista de cuándo NO usar deep learning, que es **corta y precisa, no total**. Si el
aula se va paralizada, la clase salió mal.

**Y una mención honorífica, transversal:** *"el modelo entiende"*. Aparece en las
clases 6, 7, 8 y 9, cada vez con otra ropa. No la pelees de frente: reformulá con
la pregunta que sí sirve — ***"¿qué te haría cambiar de opinión?"*** — y volvé al
mecanismo. Discutir si entiende es una discusión filosófica; discutir qué hace es
una discusión que se puede ganar con una viz.

---

## 8. Las siembras que no se pueden tocar

El curso tiene cinco cosas plantadas en una clase que se cobran en otra. Si
recortás una punta, **avisá o recortá las dos**:

| Se planta en | Se cobra en | Qué es |
|---|---|---|
| Clase 1, viz del zoo | Clase 2 | **La rampa** aparece sin explicación entre las seis formas. |
| Clase 2, botón "32 rampas" | Clase 4 | 96 perillas para 36 datos, desajuste 0,00001. Es el sobreajuste antes de tener nombre. **El golpe fuerte es el numérico, no el visual: cobralo con ese par de números.** |
| Clase 5, `viz/supuestos-de-arquitectura.html` | Clase 7 | Se construye con dos filas grises (RNN y Transformer) y la clase 7 las desbloquea con el cartel *"prometido en la clase 5, cumplido"*. |
| Clase 6, panel "¿cuántas erres tiene?" | Clase 8 | El tokenizador plantea la pregunta y no la contesta. La clase 8 la cierra con la viz de contar letras. |
| Clase 6, slide 36 (el puente) | Clase 7 | *"¿y si en vez de recordar, miramos directamente?"* — **es lo único de la clase 6 que nunca se recorta.** |

---

## 9. Adaptaciones del formato

El curso está diseñado para **10 × 2 h**. Las dos variantes que más se piden:

### 5 clases de 4 horas

Es la adaptación **fácil**: se juntan de a dos y se respetan los pares que ya son
módulos.

| Encuentro | Clases | Ajuste |
|---|---|---|
| 1 | 1 + 2 | Se puede sacar el repaso de la clase 2 ("dónde quedamos", 2 min) y el gancho de la 2 se acorta: la frustración de la recta ya viene fresca. |
| 2 | 3 + 4 | El natural: la clase 4 usa exactamente lo de la 3. Se ahorra el repaso. |
| 3 | 5 + 6 | Las dos son "la forma del dato manda". El puente 5→6 se dice de corrido. |
| 4 | 7 + 8 | **El mejor par de todos**: se construye el bloque y se lo entrena el mismo día. Además el entrenamiento de la clase 8 puede lanzarse antes. |
| 5 | 9 + 10 | El módulo de criterio, entero. El juicio de la clase 10 se puede alargar a los 25 minutos que pide el programa. |

**Lo que hay que agregar sí o sí: dos pausas de 15 minutos por encuentro, no una
de 10.** Cuatro horas seguidas de esto no las aguanta nadie. Y **al menos tres
bloques de manos** por encuentro: el riesgo del formato largo es que se convierta
en una charla.

**Lo que se pierde:** la semana entre clase y clase, que es donde el `[EL LUNES]`
se hace. Compensalo pidiendo el `[EL LUNES]` de las dos clases como una sola
tarea entre encuentros, y dedicando los primeros diez minutos del encuentro
siguiente a que dos o tres personas cuenten qué les pasó.

### 20 clases de 1 hora

Es la adaptación **difícil**, porque una hora no alcanza para el ciclo
completo de "gancho → idea → manos". La regla:

**Cada clase de 2 h se parte por su pausa.** Los diez planes minuto a minuto ya
están escritos con la pausa a los 60 minutos, así que el corte cae solo:

- **Media A** (los primeros 60 min): gancho + idea 1 + práctico 1.
- **Media B** (los últimos 60 min): idea 2 + práctico 2 + cierre.

Ajustes obligatorios:

1. **La media B necesita cinco minutos de reenganche.** Usá la slide de "volvimos"
   que varias clases ya tienen, o improvisá una: *"veníamos de…"*.
2. **La media A necesita un cierre que no existe.** No la termines en el medio de
   un práctico: cerrala con la pregunta que la media B va a contestar. Escribila
   antes, no improvises.
3. **El `[EL LUNES]` va siempre en la media B.** Nunca lo partas.
4. **La clase 8 no se parte bien**: su entrenamiento arranca a los 20 minutos y la
   pausa está diseñada para ocurrir *mientras entrena*. Para 20×1h, dale a la
   clase 8 dos horas seguidas o lanzá el entrenamiento al final de la media A y
   dejalo corriendo.
5. **La clase 10 tampoco**: "el juicio" son 20 minutos continuos. Va entero en la
   media B, y probablemente necesites una clase 21 de cierre.

**Lo que se gana:** ritmo, y menos deserción por cansancio.
**Lo que se pierde:** los bloques de manos largos, que es donde pasan las cosas.
Si podés elegir, elegí el formato de 2 h.

### Otras variantes que se piden y no recomendamos

- **Un taller intensivo de dos días.** Se puede, pero el curso deja de funcionar:
  no hay `[EL LUNES]` posible y el 70 % de lo que se lleva la gente es criterio,
  que necesita reposo. Si te obligan, dictá las clases 1, 2, 3, 4, 8, 9 y 10 y
  dejá 5, 6 y 7 como material de lectura con las viz.
- **Sacar la clase 10 "por falta de tiempo".** Es la clase más importante del
  curso. Si hay que sacar una, sacá la 5 (es la única que no está en la cadena
  principal de puentes: 4 → 6 se puede decir en dos minutos). Y ni así conviene.

---

## 10. Diez cosas prácticas que se aprenden dando el curso

1. **La pausa de 10 minutos no se toca.** Está en el presupuesto de las diez
   clases y tiene una slide propia. Si te la comés, la segunda mitad se atropella
   y la segunda mitad siempre es la importante.
2. **Proyectá las viz sueltas, no embebidas.** Embebidas entran en la slide;
   sueltas tienen el pie con la explicación y los textos completos.
3. **El botón de tema está abajo a la derecha en cada viz.** Si la sala tiene
   mucha luz, oscuro; si tiene poca, claro. Probalo antes, no en vivo.
4. **Cuando hagas una pregunta, esperá.** El silencio de cinco segundos es una
   herramienta, no un problema. Varias notas del docente lo piden con esas
   palabras.
5. **Pedí la apuesta antes de mover el slider.** Está en casi todas las clases y
   es la diferencia entre una viz que enseña y un dibujito lindo.
6. **Anotá los minutos reales la primera vez que lo dictes.** Los planes son de
   diseño, no de medición: nadie dio este curso todavía con estudiantes.
   Corregí la tabla de tu `notas-docente.md` y dejala mejor para el próximo.
7. **Los números de las slides están medidos y hay scripts que los remiden.** Si
   cambiás un dato o el paso de un slider, corré el `medir-*.py` de esa clase y
   actualizá. Un número inventado en un curso sobre no inventar es el peor error
   posible.
8. **Aguasclaras se rotula como sintético cada vez que aparece.** Cada vez. No es
   burocracia: es la mitad de la lección de la clase 10.
9. **Si te preguntan algo que no sabés, decilo.** Y anotalo. El curso se da
   adelante de gente que sabe de metodología más que vos: la autoridad viene de
   la honestidad, no de tener todas las respuestas.
10. **Antes de publicar el curso**, hay dos cosas pendientes que no son opcionales:
    escribirles a los recopiladores de los dos corpus de discursos (no declaran
    licencia) y reemplazar la URL del repositorio en la celda de bootstrap de los
    diez notebooks, en la plantilla y en `recursos/setup.md`. Está detallado en
    `_shared/especificaciones/00-ESTADO-CURSO.md`.
