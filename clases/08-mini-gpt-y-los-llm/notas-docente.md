# Notas del docente — Clase 8

**Un mini-GPT propio, y la traducción a ChatGPT** · 120 minutos · cierre del módulo 2

> **Qué cambió en esta versión, y por qué.** La clase 7 se atrasó: el aula hizo sólo
> la primera parte del notebook (attention a mano) y el tramo de máscara, cabezas,
> posición y bloque quedó entreverado. Además llegó este feedback: *«me gustaría que al
> menos parte de los ejercicios se comiencen a resolver entre todos en la clase y no
> directamente en subgrupos [...]. Capaz que esta dinámica se podría hacer solo una vez
> a la semana.»* Por eso la clase 8 se rearmó así:
>
> 1. **Sin sub-salas.** La clase entera es *code-along* en plenario: compartís
>    pantalla, corrés una celda, el aula corre la misma y pone 👍 en el chat. Nadie
>    escribe código: se lee, se apuesta (🎲) y se corre. Lo que en clase se saltea está
>    marcado 🏠 en el notebook. Las sub-salas vuelven en la clase 9.
> 2. **Re-anclaje de la clase 7 en una slide** (la 6, «el bloque en una hoja»), en vez
>    de dar el bloque por sabido. La clase 8 no necesita el código de la 7: lo trae
>    copiado.
> 3. **Un esqueleto que vuelve:** «las cinco piezas de cualquier modelo en PyTorch»
>    (slide 11). Es la respuesta a «¿cómo lo hago yo?».
> 4. **Menos riesgo:** `PLAN_CORTO` (600 pasos) para máquinas lentas, y una celda
>    **🛟 plan B** que carga `modelo-del-curso.pt` si el entrenamiento no terminó.
> 5. **La traducción, en el orden del notebook** (temperatura → prompt → ventana →
>    alucinación → letras), con la alucinación como clímax. Y «rompan el modelo» pasa
>    a plenario.
>
> El deck ágil tiene **39 slides**. Cuatro quedaron ocultas (la muestra del paso 50,
> «se contradice y repite», la tabla de traducción entera y el glosario); se recuperan
> abriendo `slides.html?completo`. **Los números de slide de estas notas son los del
> deck ágil.**

---

## 0. Antes de entrar al aula (checklist de 5 minutos)

- [ ] Abrí `notebook.ipynb` y **corré el bootstrap y la carga del corpus** en tu máquina,
      antes de la clase. Si algo va a fallar, que falle sin treinta personas mirando.
- [ ] **Probá la celda 🛟 plan B** con `USAR_MODELO_DEL_CURSO = True`: tiene que cargar
      `modelo-del-curso.pt` y escribir la muestra del paso final. Es tu red de seguridad
      y la de cualquiera cuyo entrenamiento se cuelgue.
- [ ] Mandá antes de la clase el link del notebook en Colab y pedí que **lo abran y
      corran la sección 0 al entrar**, mientras arranca el gancho: el clone del repo
      tarda un rato en Colab, y así no se lo come el code-along.
- [ ] Abrí las cuatro `viz/*.html` una vez. Funcionan sin internet, pero comprobalo.
- [ ] Tené a mano `datos/README.md` §1.5 (por qué Aguasclaras es sintético). La pregunta
      «¿por qué no usaron discursos reales?» sale **siempre** y la respuesta es buena.
- [ ] Poné el reloj a la vista. Esta clase se atrasa sola: la parte de la traducción es
      tan divertida que se come el cierre, y el cierre es lo que paga el módulo.
- [ ] Decidí **ahora** si el aula tiene GPU (Colab con T4) o no. Cambia el número que
      decís en la slide 12 (y si conviene `PLAN_CORTO`).
- [ ] **Corré vos el notebook entero una vez, en la máquina con la que vas a proyectar.**
      Las muestras de las slides 15-18 y los números de las slides 27 y 30 son de la
      *corrida del curso*; en otra máquina u otra versión de torch salen otros (ver §9).
      Anotá los tuyos: qué nombres inventó tu modelo, cuántos bloques acierta, la curva
      de la ventana. Si vas a proyectar, proyectá tu corrida.

---

## 1. El arco narrativo, en diez líneas

1. Se lee un párrafo de debate parlamentario. Suena real. Se vota. Lo escribió una máquina
   (recombinando pedazos que memorizó del corpus: eso también se dice).
2. Esa máquina tiene 1.541.056 perillas y se entrena en cuatro a siete minutos, acá.
3. Su único objetivo es tontísimo: **poner una probabilidad a la próxima ficha**.
4. Y sin embargo, con ese objetivo, el dataset se arma solo y aparece todo lo demás.
5. Se arranca el entrenamiento en el minuto 33 —después de re-anclar el bloque de la
   clase 7 y de armar el modelo entre todos— y se lo deja corriendo como teatro.
6. Mientras corre, se ve la progresión: sopa de letras → sílabas → palabras → cadencia.
7. **Aprende la forma antes que el contenido.** Ése es el hallazgo de la primera mitad.
8. Segunda mitad: cada pieza del modelo se traduce a un comportamiento de ChatGPT que ya
   vivieron. Alucinación, prompt, ventana, temperatura, conteo de letras, contradicción.
9. Nada de eso es un bug misterioso: **todo se sigue del mecanismo**, y la escala no lo
   cambia.
10. Cierre: qué le falta para ser ChatGPT (escala, instruction tuning, RLHF), qué **no**
    cambia con la escala, y qué se puede hacer con esto en una investigación propia.

**La frase que tiene que quedar.** *«Un modelo de lenguaje produce texto plausible. Lo
plausible y lo verdadero coinciden la mayoría de las veces, y eso es exactamente lo que
hace tan peligrosa la excepción.»*

---

## 2. El plan de tiempos, bloque por bloque

| Empieza | Dura | Bloque | Slides | Qué hacés vos |
|---|---|---|---|---|
| **0:00** | 8 | Gancho: ¿real o generado? | **1-5** | Leés el párrafo en voz alta. Votan. Revelás. Mientras, el aula corre la sección 0 del notebook. |
| **0:08** | 7 | **El bloque de la clase 7, en una hoja** | **6-7** | El re-anclaje. Cuatro piezas, dos líneas de código, una pregunta al chat. Después la arquitectura completa: «no hay ninguna pieza nueva». |
| **0:15** | 18 | **Code-along A: armar y arrancar** | **8-12** | En vivo, notebook secciones 2 a 5: el dataset se arma solo 🎲, el bigrama 🎲, las cinco piezas (11), el modelo 🎲 y la configuración. **El entrenamiento arranca a las 0:33.** |
| **0:33** | 12 | **Mientras entrena** | **13-18** | La loss (13), lo que dibuja el modelo (14) y las muestras, leídas **entre todos** (TODO 1 en vivo). Al terminar, la celda 🛟 plan B. |
| **0:45** | 10 | **PAUSA** | **19** | **No se toca.** |
| **0:55** | 35 | **La traducción, sobre su modelo** | **20-33** | La curva (20) y después cinco piezas en el orden del notebook: temperatura (22-24, sección 7), prompt (25), ventana (26-28, sección 8), alucinación (29-31, sección 9) y letras (32-33, sólo la viz). Cada una: apuesta → celda → viz → «por eso». |
| **1:30** | 15 | **Rompan el modelo, en plenario** | **34** | Dos minutos para escribir un prompt en el chat; corrés cuatro o cinco en vivo; el aula dice qué pieza lo explica. |
| **1:45** | 15 | Cierre | **35-39** | Qué le falta, qué no cambia, qué te llevás, `[EN TU INVESTIGACIÓN]` (con las preguntas 1 y 3 del TODO 5, entre todos) y el puente. |

**Suma 120.** Los dos bloques prácticos de 20 y 25 minutos de la versión anterior se
fueron: ahora la práctica está **adentro** de cada bloque, en plenario. El tiempo que se
ganó lo usan el re-anclaje de la clase 7 (7 min) y la traducción (de 25 a 35 min), que es
donde el aula **ve funcionando** lo que se explica.

**El único hito que no se negocia: el entrenamiento arranca a las 0:33.** Si a las 0:30
no llegaste a la sección 5, saltate el bigrama y la búsqueda de la máscara, y arrancalo.
Y si a alguien no le termina, no esperes: la celda 🛟 plan B lo pone al día.

**Las sub-salas.** Esta clase no las usa, a propósito (ver el recuadro de arriba). Si
el aula pide trabajar en grupo, ofrecé los 🏠 del notebook como trabajo en pares
**después** de la clase. Las sub-salas vuelven en la 9, donde auditar un modelo ajeno
se presta para el trabajo en grupo y el aula ya llega con las cinco piezas.

---

## 3. Bloque por bloque: qué decir, qué preguntar, qué va a pasar

### Gancho (0:00-0:08) — slides 1 a 5

Leés el párrafo generado **en voz alta y con tono de sesión**. No lo proyectes primero:
que lo escuchen. Después lo proyectás y preguntás:

> **«¿Lo dijo alguien o lo escribió una máquina? A mano alzada.»**

**Lo que va a pasar.** El aula se parte más o menos por la mitad, con una mayoría
inclinada a «lo dijo alguien» si leíste bien. Alguien va a decir «se nota que es una
máquina porque no dice nada concreto» — **agarrá ese comentario y guardalo**, porque es
literalmente el hallazgo de la primera mitad de la clase. Escribilo en el pizarrón:
*«no dice nada»*. Volvés a él mientras entrena, cuando lean las muestras (0:40).

Después la promesa, y decila mirando al aula, no a la slide:

> «Todo lo que hace ChatGPT y te resulta mágico o irritante lo vas a poder explicar
> antes de que termine esta clase. No con una metáfora: con el mecanismo, mirando el
> modelo que ustedes van a entrenar.»

### El bloque de la clase 7, en una hoja (0:08-0:15) — slides 6 y 7

**El objetivo es cerrar la clase 7 sin volver a darla.** Ahí quedaron mezcladas seis
ideas en quince minutos; acá se ordenan en cuatro piezas con una frase cada una:

| Pieza | La frase | La línea |
|---|---|---|
| ① Attention | las fichas **se pasan información** | `x = x + self.atencion(self.norma1(x))` |
| ② MLP | cada ficha **piensa sola** | `x + self.mlp(self.norma2(x))` |
| ③ Residual | el original del expediente **sigue adjunto** | el `x +` de las dos líneas |
| ④ Norma | plomería: que los números no se disparen | `norma1`, `norma2` |

Adentro de ① viven las otras tres ideas, y se dicen en una línea cada una: Q, K y V son
**tres lecturas de la misma `x`**; la máscara es **una regla, no se aprende**: no se
espía el futuro; las cabezas son **varias lecturas en paralelo**. Afuera del bloque, en
la entrada, el sellito de posición.

**No vuelvas a explicar la fórmula de attention ni el aviso clasificado.** Si alguien
pregunta, «es lo de la clase 7, y para hoy alcanza con esto». La pregunta al aula es
una sola y se contesta en el chat: **«¿en qué línea está la máscara? ¿y el
residual?»** (proyectá la celda del `BloqueTransformer` de tu notebook). Si la
contestan, la clase 7 quedó cerrada.

La slide 7 (la arquitectura completa) se recorre con el dedo: «fichas, clase 6;
embeddings, clase 6; posición y bloques, clase 7; la última caja es lo único de hoy».

### Code-along A: armar y arrancar (0:15-0:33) — slides 8 a 12

**Cómo se hace el code-along.** Compartís pantalla con el notebook a la izquierda y el
chat a la derecha. Corrés una celda, decís en voz alta qué imprimió, y esperás a que
haya unos dos tercios de 👍. No esperes al último: «si te quedaste, *Entorno de
ejecución → Ejecutar anteriores* y te ponés al día». Los errores que peguen en el chat
se resuelven **en voz alta**: el error de uno le sirve a todos.

Las slides 8 a 10 (objetivo, dataset, bigrama) se intercalan con las secciones 1 a 3
del notebook. Las tres celdas 🎲 de este bloque son: «¿cuántos ejemplos hay en una
ventana de 8?» (ocho), «¿una tabla de conteos escribe algo?» (sí, sílabas) y «¿en qué
línea está la máscara?» (sección 4). La slide 11, **las cinco piezas**, va justo antes de
la sección 4, y la leés en un minuto: cada fila se ve funcionando en el notebook. Volvé a
ella cada vez que pases de una pieza a la siguiente («estamos en la 4, la de la clase 4»).

No hay nada nuevo salvo las piezas 1 y 5: fichas (clase 6), embeddings (clase 6), bloque
transformer (clase 7), loss y descenso (clases 3 y 4).

La única idea nueva de verdad es **«el dataset se arma solo»**, y merece treinta
segundos de silencio:

> «Para entrenar un clasificador de titulares alguien tiene que etiquetar titulares, de
> a uno. Para entrenar esto sólo hace falta texto: la respuesta correcta es la palabra
> que efectivamente venía después. Por eso se puede entrenar con internet entero, y por
> eso los LLM existen y los clasificadores buenos siguen siendo caros.»

Y el punto de eficiencia que a nadie se le ocurre solo:

> **«Una ventana de 8 fichas no es un ejemplo de entrenamiento: son ocho.»**

El bigrama es opcional si vas justo, **pero no lo saltees si podés evitarlo**: ver que
con una tabla de conteos ya salen sílabas del castellano baja mucho el misticismo.

**A las 0:33, la slide 12 y el entrenamiento.** Antes de arrancarlo, anticipá: *«esto
va a escribir cosas que suenan a debate parlamentario y no dicen nada. Ése es el
punto.»* Si alguien avisa que su máquina es lenta, `PLAN_CORTO = True` en la celda de
la configuración.

Los problemas que van a aparecer en el chat, en orden de frecuencia:

1. **No corrieron el bootstrap.** Un tercio del aula, siempre.
2. **Corrieron celdas salteadas** y `tok` no existe. «Reiniciar entorno y ejecutar todo».
3. **Colab les asignó CPU y esperaban GPU.** Está bien: el notebook lo detecta y usa 1200
   pasos en vez de 3000. Decilo en voz alta para que nadie se asuste.
4. **Alguien cambió `DIM` "para probar"** y ahora el `revisar()` de las perillas falla con
   un mensaje que se lo dice. Ese mensaje está escrito para eso.
5. **El entrenamiento no termina o se cuelga.** No esperes: que lo corten con ■ y corran
   la celda 🛟 plan B, que carga el modelo del curso. **Nadie se queda afuera de la
   segunda mitad por una máquina lenta.**

### Mientras entrena (0:33-0:45) — slides 13 a 18

Mientras corre van la loss (13: «qué probabilidad le diste a la respuesta que vino»; el
paso 0 vale log 71 = 4,26, «no tengo ni idea») y lo que dibuja el modelo (14). Después,
**las muestras, leídas entre todos**: es el TODO 1 del notebook, en vivo. Proyectá tu
corrida y usá las slides 15 a 18 (pasos 0, 400, 800 y 1200) de respaldo. Leé la muestra
en voz alta cada vez y preguntá al chat **«¿qué aprendió entre ésta y la anterior?»**.
**Es teatro y hay que actuarlo.** En el paso 400 ya hay palabras del castellano y vale
la pena decir: «nadie le dio un diccionario». Y en la última se cobra el «no dice nada»
del gancho: **la forma se aprende antes que el contenido**.

Cuando el entrenamiento termina, todos corren la celda 🛟 plan B. A quien terminó no le
hace nada; a quien lo cortó le carga el modelo del curso. Y te deja decir algo que vale
oro para «¿cómo lo hago yo?»: **cargar un modelo entrenado son tres líneas, porque el
modelo son sus perillas.**

**Las muestras de las slides son de la corrida del curso.** En la misma máquina y con
las mismas versiones de las librerías, el notebook las reproduce letra por letra; en
otra, no. En la revisión, con torch 2.14 en un procesador ARM, las muestras de los pasos
0, 50 y 1200 salieron casi iguales y las de 150, 400 y 800 fueron otras: **no apareció
«Nelida Falcon»**. Para no depender de eso:

- la celda del entrenamiento imprime qué nombres inventó **tu** modelo en sus muestras;
- la sección 9 mide la invención sobre 60 sorteos (en la corrida de verificación: 8 de
  57 nombres no existían). Ese número es el que sostiene el argumento, no una muestra
  suelta.

Y si un estudiante pregunta por qué su texto es distinto con la misma semilla, es un
regalo: *misma semilla, otra máquina, otro texto* es exactamente el punto de la clase 10.

### Pausa (0:45-0:55) — slide 19

**No la negocies.** El modelo entrena solo. Si alguien quiere preguntar algo, que
pregunte en la pausa: mucha gente que no levanta la mano delante de treinta personas sí
se acerca al escritorio.

### La traducción (0:55-1:30) — slides 20 a 33

**Este es el bloque por el que se hicieron las siete clases anteriores.** Ritmo:
cada pieza es **apuesta → celda del notebook, en vivo → viz → una frase que empieza con
«por eso»**. Si una pieza no termina en un «por eso», sacala. La diferencia con la
versión anterior es que acá el aula **ve funcionando su propio modelo**: la práctica
está adentro de la explicación, no 25 minutos después en una sub-sala.

El orden es **el del notebook** (las celdas de cada sección usan funciones de la
anterior, así que no se puede saltar adelante):

0. La **curva de loss** (slide 20, notebook sección 6) — 3 min.
1. **La temperatura** (22-24, sección 7, viz `temperatura.html`) — 8 min. El TODO 2 es 🎲:
   «¿a qué temperatura deja de ser legible?», votan y corrés. El TODO 3 (mismo prompt,
   respuestas distintas) va en vivo.
2. **Por qué le importa el prompt** (25) — 2 min, con la demo de dos prompts.
3. **La ventana de contexto** (26-28, sección 8, viz `ventana-de-contexto.html`) — 7 min.
   El TODO 4 (romperla a mano) es 🏠.
4. **Por qué alucina** (29-31, sección 9, viz `por-que-alucina.html`) — 10 min, **el
   clímax**. La medición sobre 60 sorteos es 🏠: en clase alcanza con la viz y la celda
   del padrón.
5. **Por qué cuenta mal las letras** (32-33, viz `contar-letras.html`) — 3 min, **sólo
   la viz**: la sección 10 del notebook es 🏠.

**Suman 33 y el bloque tiene 35**: los dos de aire son para las apuestas, que siempre se
estiran. «Por qué se contradice y por qué repite» quedó oculta: se dice en una frase
adentro del bloque del prompt («no hay un estado de creencias: cada ficha se condiciona
al texto anterior, y si arrancó mal sigue por ahí»).

**El momento clave de todo el módulo** es el de la alucinación, y se hace así:
mostrás el prompt del diputado que existe, el modelo contesta bien, mostrás el padrón,
está. Después el de la diputada inventada, el modelo contesta con la misma soltura,
mostrás el padrón, **no está**. Y entonces la pregunta, con pausa:

> **«¿Cuál de las dos salidas se veía distinta?»**

Silencio. No la contestes vos. Que la conteste alguien: «ninguna». Ahí sacás el número
honesto que está en el panel de la viz: el modelo **le acierta el bloque a 54 de los 60
diputados reales** (en la corrida del curso; en la revisión con otra versión de torch,
48). Sabe cosas. Y aun así no hay manera de saber, mirando, si este caso es uno de los
que sabe.

**Decí con precisión qué se ve en los tres casos falsos:** la entidad falsa (la diputada,
la ley, la provincia) la pusimos **nosotros** en el prompt. El modelo no la rechaza:
**acepta la premisa falsa** y la completa. Es un fenómeno distinto de fabricar, e igual de
importante: si tu pregunta trae un supuesto falso, la respuesta lo hereda. La «cita» ni
siquiera es inventada: es una frase que está 124 veces en el corpus, recitada de memoria
y pegada a una provincia que no existe. La fabricación espontánea es la de Nélida Falcón
(y la de la medición sobre 60 sorteos del notebook).

### Rompan el modelo, en plenario (1:30-1:45) — slide 34

**Antes eran 25 minutos de a dos; ahora son 15 entre todos.** Dos minutos para que cada
uno escriba en el chat un prompt que crea que rompe el modelo, y con qué temperatura.
Elegí cuatro o cinco **distintos entre sí** (uno largo que empuje la pista fuera de la
ventana, uno con premisa falsa, uno con T alta, uno fuera de género, uno que pida
contar) y corrélos en la celda de la sección 11. Para cada uno: **apuesta → correr →
«¿qué pieza lo explica?»**, y nombrá la fila de la tabla de traducción. Esa segunda
mitad —el porqué— es la que vale.

Los TODO 2 a 5 quedan como práctica 🏠, opcional, antes de la clase 9.

### Cierre (1:45-2:00) — slides 35 a 39

Tres cosas, en este orden y sin saltearse ninguna:

1. **Qué le falta para ser ChatGPT.** Escala, instruction tuning, RLHF. Dos líneas cada
   una. El punto que hay que dejar clarísimo: **el paso 2 y el 3 son los que lo
   convierten de autocompletador en asistente**, y también de donde sale la adulación.
2. **Qué NO cambia con la escala.** La slide más importante de la clase. Decila despacio:
   *«Los modelos que vengan van a ser mucho mejores y van a compensar varias de estas
   cosas —con herramientas, con razonamiento paso a paso, con ventanas enormes—. Pero
   mientras predigan la próxima ficha, adentro no va a haber nada que detecte "no sé",
   van a seguir tokenizando, van a tener una ventana finita y van a sortear. La escala
   mejora la calidad, no cambia la naturaleza.»* No lo vendas como profecía: la
   audiencia va a probar ChatGPT esa noche, y si le cuenta bien las erres de
   «ferrocarril», el mensaje tiene que seguir en pie.
3. **`[EN TU INVESTIGACIÓN]`** (slide 38), con las preguntas 1 y 3 del TODO 5 abiertas
   al chat: «¿podrías distinguir la invención sin el padrón?» y «¿qué tarea **sí**
   podés hacer con una herramienta así?». Y el puente (39).

---

## 4. Las preguntas que hacés al aula, y cuándo

| Hora | Pregunta | Para qué |
|---|---|---|
| 0:02 | «¿Real o generado? A mano alzada.» | La apuesta. Sin ella, la revelación no vale nada. |
| 0:06 | «¿Qué les hizo sospechar?» | Sale «no dice nada concreto». Guardalo: se cobra mientras entrena. |
| 0:12 | «¿En qué línea está la máscara? ¿Y el residual?» (al chat) | El re-anclaje de la clase 7. Si la encuentran, la 7 quedó cerrada. |
| 0:18 | «¿Cuántos ejemplos de entrenamiento hay en una ventana de 8 fichas?» | Casi todos dicen «uno». Son ocho. |
| 0:40 | «Ya escribe como un diputado. ¿Está diciendo algo?» | Se cobra la apuesta del gancho: **la forma se aprende antes que el contenido**. |
| 1:00 | «Antes de correr: ¿qué le va a pasar al ORDEN de las barras si subo la temperatura?» | Casi todos dicen «va a cambiar». No cambia nunca. |
| 1:10 | «¿En qué tamaño de ventana creen que se va a romper?» | La apuesta antes de la viz de la ventana. |
| 1:18 | «¿Cuál de las dos salidas se veía distinta?» | El corazón de la clase. No la contestes vos. |
| 1:48 | «Si los modelos fueran diez veces más grandes, ¿cuál de estas cosas desaparece?» | La slide de «qué no cambia con la escala». Ninguna desaparece; varias se disimulan mejor. |

---

## 5. Las respuestas típicas y cómo usarlas

**«Se nota que es una máquina porque no dice nada.»** (0:06)
La mejor respuesta posible y la vas a escuchar casi seguro. **Escribila en el pizarrón.**
Mientras entrena, con las muestras, volvés: *«Tenían razón. Y esto es lo importante: la forma —el género
discursivo, las fórmulas de cortesía, la estructura de turnos— se aprende antes que
cualquier contenido, y con mucho menos esfuerzo. En los modelos grandes eso sigue siendo
cierto: sólo que están tan bien hechos que la disociación es mucho más difícil de ver.»*

**«¿Entonces adentro tiene guardados los discursos?»**
**En este mini-GPT, en buena parte sí**, y conviene decirlo: el modelo pesa 6,4 MB y el
corpus 1,1 MB, así que le sobra lugar, y memorizó las plantillas del generador (la
sección 12 del notebook mide cuánto de la muestra final está calcado del corpus; en la
corrida de verificación, 5 de 6 pedazos de 40 caracteres). Por eso la cita del gancho
sale casi textual: está 124 veces en el corpus.

**En un LLM grande la cuenta da al revés:** el texto de entrenamiento (decenas de
terabytes) supera por lejos a los pesos, y no entra entero. Lo que hay es algo parecido a
una compresión con pérdida, sin índice. Pero ojo: **igual memorizan tal cual** lo que
vieron repetido muchas veces (Carlini et al. 2021 extrajeron textos de entrenamiento
verbatim de GPT-2). Lo que no quedó es lo que después se completa con lo plausible.

**«¿Y si le digo que no invente?»**
Excelente pregunta y hay que probarla en vivo: el notebook tiene la celda
(`MI_PROMPT_ROMPEDOR = "Por favor no inventes nada..."`). El prompt **condiciona la
distribución**, no instala un verificador. Puede bajar la tasa; no puede sacar el
mecanismo. Y ojo con la sobrecorrección: en modelos con RLHF el prompt sí ayuda bastante,
porque los entrenaron para decir «no sé» más seguido. Ayuda. No garantiza.

**«Entonces son inútiles para investigar.»** (aparece siempre al final de «rompan el modelo»)
**Es la sobrecorrección y hay que atajarla explícitamente**, o se van con lo contrario de
lo que queríamos. La regla que sirve:

> Un LLM es buena herramienta donde **la validación es barata y el error es visible**
> (¿este titular menciona una protesta? lo leo y lo chequeo en dos segundos) y es pésima
> donde **validar cuesta tanto como hacer el trabajo** (¿existe esta cita? ¿es correcto
> este dato?).

**«Mi mini-GPT escribe cualquier cosa, no me sirve.»**
Anticipalo **antes** de entrenar, no después: *«esto va a escribir cosas que suenan a
debate parlamentario y no significan nada. Eso es exactamente el punto.»*

---

## 6. Confusiones de principiante y cómo desarmarlas

| Confusión | Cómo se manifiesta | Cómo la desarmás |
|---|---|---|
| **«Tiene una base de datos adentro»** | Preguntan dónde está guardada la información. | No hay tablas ni índice: hay una función. Por eso no se le puede «corregir un dato». Matiz honesto: lo que se repite mucho sí queda memorizado tal cual (este mini-GPT memorizó las plantillas; ver §5). |
| **«Alucina porque le faltan datos»** | Creen que es un problema de cobertura y que se arregla con más corpus. | Alucina **por diseño**: siempre produce la continuación más plausible. Con más datos alucina *menos seguido*, no *distinto*. Es la slide «qué no cambia con la escala». |
| **«La temperatura lo hace más creativo/inteligente»** | Antropomorfizan el parámetro. | La viz de temperatura: **el orden de las barras no cambia nunca**. Sólo cambia el riesgo del sorteo. |
| **Alucinación = error** | Todo error se llama alucinación. | Distinción útil: un **error** es equivocarse en algo que estaba en la distribución; una **alucinación** es *fabricar una entidad* con confianza. Y hay una tercera, que la viz muestra: **aceptar una premisa falsa** que venía en el prompt. Para investigar, las dos últimas son mucho peores **porque son verosímiles**. |
| **«Este modelito no tiene nada que ver con ChatGPT»** | Descreimiento por escala. | La arquitectura es la misma; cambian escala, datos y las dos etapas posteriores. Todo lo de la tabla de traducción **sí** transfiere; la calidad y el conocimiento del mundo, no. |
| **«T=0 lo hace reproducible»** | Reportan T=0 como suficiente. | Ayuda mucho y no alcanza: cambia la versión del modelo sin aviso, cambia el hardware, hay no determinismo en la infraestructura. Se retoma en la clase 10. |
| **«El modelo entiende»** | Aparece cuando lo ven escribir bien. | No lo pelees de frente. Reformulá: *«¿qué te haría cambiar de opinión?»* y volvé a la alucinación: entender incluye saber cuándo no sabés, y acá no hay nada que lo detecte. |
| **Confundir loss baja con modelo bueno** | «Le dio 0,19, entonces anda bárbaro.» | 0,19 sobre un corpus de plantillas es *demasiado* bueno, y esa es la señal. Ver §9. |

---

## 7. Si vas atrasado / si vas adelantado

### Si vas atrasado (te va a pasar)

Se recorta **en este orden**, y ni un paso antes de tiempo:

1. **El bigrama** (slide 10). Duele, pero se cuenta en dos frases sin correr nada.
2. **La búsqueda de la máscara en el chat** (slide 6): la señalás vos y seguís.
3. **El TODO 3** (mismo prompt, respuestas distintas): se dice con la slide 24, sin
   correr la celda.
4. **La viz de contar-letras** — se muestra 90 segundos sin abrirla, con la slide sola.
5. **«Rompan el modelo» baja de 15 a 8 minutos**: dos prompts del chat en vez de cinco.

**Lo que NUNCA se recorta:**

- **La pausa.** Diez minutos. Si te la comés, la segunda mitad se atropella y la segunda
  mitad es la clase.
- **El bloque de la alucinación.** Es la razón de ser del módulo.
- **El re-anclaje de la clase 7** (slide 6). Son cinco minutos, y sin ellos la mitad
  del aula entrena una caja negra.
- **El arranque del entrenamiento a las 0:33.** Y si alguien no llega, el plan B, no la
  espera.
- **La slide «qué NO cambia con la escala»** (36). Si sólo te quedan tres minutos,
  esa slide y el `[EN TU INVESTIGACIÓN]`. Todo lo demás es prescindible antes que eso.
- **El puente a la clase 9.** Sin él, la 9 arranca en el aire.

### Si vas adelantado

- Abrí `slides.html?completo` y recuperá «se contradice y repite» (la que está oculta
  después de las letras): un minuto, y conecta con el bucle que alguien seguro encontró
  rompiendo el modelo.
- Abrí `viz/temperatura.html` con el prompt «El bloque del » y hacé que el aula prediga
  qué partido va a salir antes de generar. Es divertido y muestra la distribución en vivo.
- Mostrá `viz/tokenizador.html` de la **clase 6** al lado de `contar-letras.html`. El
  guiño «prometido en la clase 6, cumplido» funciona mejor con las dos abiertas.
- Discutan: *«si el corpus fueran discursos parlamentarios reales en vez de sintéticos,
  ¿qué cambiaría?»* (Respuesta: aprendería mucho peor con el mismo presupuesto, el
  vocabulario es 10-20 veces más rico; y no podríamos hacer la demo de la alucinación,
  porque nadie puede verificar en cinco segundos si un diputado argentino existe.)
- Que alguien busque en el `padron_detalle` de `datos-mini-gpt.json` los **6** diputados
  a los que el modelo (de la corrida del curso) les erra el bloque, y que discutan si
  tienen algo en común.
  (Comprobado: **cinco de los seis** comparten nombre de pila o apellido con otro
  diputado —Godoy, Peralta y Zabaleta con uno de **otro** bloque; Osvaldo **Y**barra
  del VVA con Osvaldo **I**barra del MPR, que es el más lindo de todos—. El único sin
  ninguna colisión es Fabián Heredia. O sea: el modelo aprendió «apellido → bloque»,
  y se le cae justo donde el apellido no alcanza.)

---

## 8. Chistes y analogías que funcionan

- **El informante que nunca dice «no sé».** Todo el mundo entrevistó a alguien así:
  completa, redondea, arma una historia coherente. No miente por maldad; la conversación
  tiene una fuerza de completitud. **Un LLM es ese informante llevado al extremo**, y las
  técnicas de manejo son las mismas: triangular, pedir fuentes, chequear contra otro
  registro. Esta es la mejor analogía de la clase con esta audiencia.
- **La cita inventada con formato perfecto.** El formato de una referencia bibliográfica
  es lo **más predecible que existe en un texto académico**; los datos concretos, lo
  menos. El modelo produce exactamente lo que se espera: estructura impecable, contenido
  inventado. Con esta audiencia es letal, en el buen sentido.
- **El género discursivo (Bajtín).** El modelo aprende la forma del debate antes que
  cualquier contenido. Si tenés gente de análisis del discurso, esto les cierra al
  instante y les da una entrada propia al tema.
- **La memoria de la entrevista.** La RNN de la clase 6 olvida gradualmente; el
  transformer tiene un **corte duro** en el dato. Lo que quedó afuera de la ventana no
  está borroso: **no está**. (Ojo: la curva de aciertos igual sube de a poco, porque la
  información entra de a poco; el corte es del dato, no de la curva.)
- **La temperatura y el codificador cansado.** Un codificador humano cansado es de alta
  temperatura: más variable, menos predecible. Uno rígido codifica siempre igual y pierde
  matices. Ni un extremo ni el otro es «el correcto»: depende de la tarea. Y el punto
  metodológico: si tu instrumento tiene variabilidad, **tenés que reportarla**.
- **El chiste que funciona:** cuando el modelo se inventa una diputada, decir con cara de
  póker *«bueno, técnicamente no mintió: mentir requiere saber la verdad»*.

---

## 9. Los números de esta clase (medidos, no estimados)

Todo lo que sigue salió de correr
`PYTHONPATH=_shared python3 clases/08-mini-gpt-y-los-llm/entrenar-mini-gpt.py`
en el contenedor de construcción (torch 2.13, CPU x86 de 4 hilos): es **la corrida del
curso**, la de las slides y las viz. **Si citás un número en el aula, citá estos, o los de
tu propia corrida diciendo que son tuyos.** Más abajo, cuánto cambian en otra máquina.

| qué | valor |
|---|---|
| parámetros del modelo | **1.541.056** (4 bloques · 4 cabezas · dim 176 · ventana 128 fichas) |
| corpus | Aguasclaras, 1.098.206 caracteres, vocabulario de **71** fichas |
| entrenamiento (la celda sola, 1200 pasos) | **entre 4 y 7 minutos** en CPU con **4 hilos**. Seis cronometrajes de la misma corrida: **243 s** y **267 s** con `entrenar-mini-gpt.py`, y **280 s**, **297 s**, **360 s** y **432 s** con la celda del notebook (0,23 a 0,36 s por paso). |
| el notebook ENTERO, de punta a punta | **entre 5 min 20 s y 8 min** (`nbconvert --execute`): **322 s**, **339 s**, **361 s**, **368 s**, **376 s**, **404 s**, **480 s**. |
| por qué se mueve tanto | La CPU es compartida: el mismo notebook, en la misma máquina, tarda un 40-80% más si tenés el navegador con las viz abierto al lado — que es exactamente lo que va a pasar en el aula. **Decí «entre cuatro y siete minutos» y planificá con siete.** Nunca des un número al segundo. |
| loss de validación | **4,23 → 0,19** (el punto de partida de «no tengo idea», repartir parejo, es log 71 = 4,26; no es un piso: estar confiadamente equivocado da más) |
| loss del bigrama en validación | **2,24** (la línea de base tonta) |
| tamaño del checkpoint | **6,4 MB en disco** (1.541.056 × 4 bytes = 6,2 MB de pesos, más las máscaras de atención y el vocabulario) para un corpus de 1,1 MB |
| aciertos de bloque sobre el padrón | **54 de 60** diputados reales |
| aciertos de provincia sobre el padrón | 33 de 60 |
| ventana, pista cerca (apellido) | 7 / 14 / 24 / 27 / 28 de 30 con ventana 4 / 8 / 12 / 16 / 24; líneas de base: azar 5/30, siempre «FCA» 7/30 |
| ventana, pista lejos | 6 de 24 con la ventana entera; líneas de base: azar 4/24, siempre «Partido de la Union Nacional» 8/24 |
| nombres inventados en las muestras | «Nelida Falcon», en la del paso 800 |

**Lo mismo en otra máquina (para que no te agarre desprevenido).** Misma semilla y mismo
código; distinta CPU o distinta versión de torch → los pesos cambian en las últimas
cifras y el sorteo se va por otro camino. Varias corridas de revisión en otra máquina
(torch 2.14, macOS ARM, 4 hilos): la del revisor y las de la verificación (notebook y
script, que en la misma máquina dieron los mismos números de modelo):

| qué | corrida del curso | otra máquina |
|---|---|---|
| entrenamiento (1200 pasos) | 4 a 7 min | 1 min 41 s a 2 min 5 s (84-104 ms por paso; el script entero, con las 420 generaciones y la exportación, 3 a 3,5 min) |
| loss final train / val | 0,185 / 0,186 | 0,183 / 0,184 |
| aciertos de bloque / provincia | 54 / 33 de 60 | 48 / 33 de 60 |
| ventana cerca (4 / 8 / 12 / 16 / 24 / 128) | 7 / 14 / 24 / 27 / 28 / 28 de 30 | 5 / 15 / 22 / 26 / 27 / 24 de 30 |
| muestras de los pasos 150, 400, 800 | las de las slides | otras; **sin «Nelida Falcon»** |
| muestras de los pasos 0, 50, 1200 | las de las slides | casi iguales |
| fabricación sobre 60 encabezados (sección 9) | (no se midió en la corrida del curso) | 8 de 57 nombres no existen |

La lectura de la clase no cambia con ninguno de estos números. Lo que cambia es que
**no podés prometer que la pantalla del estudiante va a coincidir con la slide**: decí
«en la corrida del curso» y, si podés, proyectá la tuya.

**Sobre la GPU: no la pudimos medir.** El contenedor donde se construyó esta clase no
tiene GPU, así que **no hay número medido para T4** y no lo inventamos. El notebook
detecta la GPU y sube a 3000 pasos. **Pedido concreto a quien dé esta clase por primera
vez en Colab con T4: anotá el tiempo que imprime la celda y ponelo acá.**

**Ojo con la loss de 0,19: es demasiado buena, y eso es contenido, no un logro.**
Aguasclaras sale de plantillas y tiene 849 palabras distintas — un corpus real de ese
tamaño tendría 10 a 20 veces más. **El modelo aprende mucho mejor de lo que aprendería
con texto real.** Decilo en el aula cuando muestres la curva: si no, se van con una
impresión falsa de lo fácil que es esto. El antídoto está a mano y es un buen ejercicio
para quien quede picado: `datos.corpus_mini_gpt()` son 2,2 MB de discursos reales y el
mismo modelo se puede entrenar encima para comparar.

**Y sobre la tijera (clase 4).** Con el corpus entero **no hay tijera**: al paso 1200,
train 0,185 y val 0,186. Tiene sentido: 1,5 millones de perillas sobre casi un millón de
fichas de un texto muy repetitivo. (Que no haya tijera no quiere decir que no memorice:
con un corpus de plantillas, lo que memoriza de train también aparece en val.) Si querés
mostrar una tijera de verdad, entrená el mismo modelo sobre `texto[:25_000]` (25 KB): la
train baja a **0,10** y la validación se queda en **0,70-0,82**. **La señal robusta es esa
brecha** (0,10 contra 0,8): desde el paso ~400 la validación está plana dentro del ruido
(±0,1), así que «toca fondo y sube» se ve en unas corridas y en otras no tanto. Ésos son
los números del ítem 6 del cuestionario.

> **Precisión sobre estos números, porque importa en una clase que enseña a no inventar.**
> Se corrieron **tres veces**. La **forma** —train diez veces más chica que val— sale
> idéntica las tres. Los **valores paso a paso, no**: con 25 KB el conjunto de validación
> son 2.500 fichas, y medir la loss sobre ocho lotes de ese puñado tiene ruido de ±0,1.
> El mínimo cayó en el paso 900 (0,70), en el 700 (0,74) y, en la revisión con otra
> versión de torch, en el 1000 (0,70, y 0,78 al final). **La tabla del cuestionario es una corrida real, no la
> única posible**, y si alguien la reproduce y le da el mínimo en otro paso, la
> respuesta sigue siendo la misma y el motivo es una buena conversación de clase.
> Tiempo: entre **224 s y 360 s**, con la misma dispersión de CPU que todo lo demás.

---

## 9 bis. Una viz que se rehízo después de medir, y por qué conviene contarlo

`viz/ventana-de-contexto.html` iba a mostrar otra cosa. El plan original era: el
encabezado del turno dice de qué bloque es quien habla, y setenta fichas después el
orador dice «El bloque del …»; si el encabezado se cae de la ventana, el modelo tendría
que perder la respuesta.

**Se midió sobre 24 pasajes reales del corpus y no pasa.** El modelo acierta 6 de 24 con
la ventana entera, y la curva es **plana**. Y ojo con la línea de base: el azar da 4 de 24,
pero **contestar siempre el bloque más frecuente** (el PUN) da **8 de 24**. O sea: con la
pista lejos, el modelo no le gana a no mirar la pista (con la ventana en 8, sin pista,
contesta siempre PUN y saca justo 8). Nunca aprendió esa dependencia larga: sólo 67 de
las 238 apariciones la tienen a menos de 128 fichas, y 1200 pasos de un modelo de 4
bloques no alcanzan.

Publicar la viz original habría sido **inventar un resultado**, que es exactamente lo que
este curso enseña a no hacer. Así que la viz muestra ahora dos mediciones reales:

- **la pista cerca** (el apellido del diputado predice su bloque; está a ~9 fichas):
  7/30 (ventana 4) → 14/30 (8, con medio apellido) → 24/30 (12) → 27-28/30 (16 en
  adelante). **La curva sube de a poco**, a medida que entran las letras del apellido:
  el corte duro es del **dato** (la letra que quedó afuera no está), no de la curva. Una
  versión anterior marcaba como pista el nombre completo, y el cartel de «perdiste la
  pista» aparecía con el modelo contestando bien (con el apellido solo le alcanzaba);
  se corrigió.
- **la pista lejos**: la curva plana. Y eso resultó **mejor** que el plan original,
  porque enseña algo más fino: *estar adentro de la ventana no alcanza*. Es el
  **lost in the middle** de los modelos grandes, en miniatura y medido en el aula.

**Contá esta historia en clase si te da el tiempo.** Que el material del curso haya
tenido que cambiar porque la medición dijo otra cosa es la mejor lección posible sobre
cómo se trabaja, y dura noventa segundos.

---

## 10. La tabla de traducción (imprimila y tenela a mano)

| Pieza del mini-GPT | Comportamiento de ChatGPT que explica |
|---|---|
| La salida es **siempre** una distribución de probabilidad | Alucina; no tiene cómo saber cuándo no sabe (si dice «no sé», también es una continuación aprendida); suena igual de seguro cuando acierta que cuando inventa |
| Está **condicionada por el texto previo** | El prompt cambia todo; el rol asignado («sos un experto en…») cambia el registro; el prompt es un instrumento de medición |
| La **ventana de atención es finita** | Se olvida del principio de una conversación larga; ignora instrucciones lejanas; lo importante, al principio o al final (nunca en el medio), y repetido |
| **Costo cuadrático** de attention | Por qué la ventana tiene un límite y por qué un prompt largo cuesta más caro |
| Hay un **sorteo** al elegir la ficha (temperatura) | El mismo prompt da respuestas distintas; T=0 lo hace repetitivo; T alta lo hace delirante; sin semilla no hay reproducibilidad |
| Trabaja con **fichas**, no con letras | Le cuesta contar letras, las rimas, los anagramas y la aritmética (los modelos grandes lo compensan en parte, no del todo); anda peor en idiomas poco representados |
| **No hay estado de creencias**, sólo condicionamiento | Se contradice; una vez que arrancó por un camino equivocado sigue por ahí; se lo puede «convencer» de casi cualquier cosa |
| Entrenado para predecir **texto plausible** | Produce referencias bibliográficas con formato perfecto y datos inventados: el formato es lo más predecible que hay |
| **Instruction tuning + RLHF** encima | Responde consignas en vez de completar; es amable; a veces adula y te da la razón (ya asoma sin RLHF; el RLHF la refuerza mucho) |
| Aprendió **del corpus** | Reproduce los sesgos del corpus; sabe mucho de lo que abunda en internet y poco de lo que no |

---

## 11. Si te preguntan X — las cinco difíciles

### 1. «¿Esto quiere decir que los LLM no entienden nada?»

**La pregunta honesta de la clase, y merece una respuesta honesta.** No contestes ni que
sí ni que no, porque las dos son propaganda.

Lo que **sí** podemos afirmar desde el mecanismo, sin discusión: no hay un módulo que
verifique verdad, no hay un estado de creencias que se sostenga entre respuestas, y no
hay nada que detecte «esto no lo sé» (si dice «no sé», es una continuación más). Eso no
es opinión: es lo que acaban de ver.

Lo que **está genuinamente en discusión**: si de predecir texto a esa escala emerge algo
que merezca llamarse comprensión. Hay gente muy seria de los dos lados y **no está
resuelto**. Lo que sí podés decir: la pregunta «¿entiende?» es menos útil de lo que
parece para tu trabajo. La pregunta útil es **«¿puedo verificar barato si esta salida
concreta es correcta?»**, y ésa sí tiene respuesta caso por caso.

### 2. «¿Puedo usar ChatGPT para codificar mi corpus y ponerlo en un paper?»

Sí, con condiciones, y son las mismas que le exigirías a un codificador humano:

1. **Prompt fijo, escrito en un archivo, y va en el apéndice.** El prompt es tu libro de
   códigos. Si lo cambiás, cambiaste el instrumento y los resultados anteriores no son
   comparables.
2. **Temperatura 0 y semilla, si el proveedor te la deja fijar.**
3. **Una muestra validada a mano**: al menos 200 casos codificados por vos, y reportás el
   acuerdo (kappa o el que uses). Sin esto no tenés nada.
4. **Un baseline tonto** para comparar. Si un diccionario de palabras clave da lo mismo,
   usá el diccionario: es más barato y más transparente.
5. **Modelo, versión y fecha exactos.** «GPT-4» no es una versión.

Y el criterio que ordena todo: **esto sirve donde el error es visible y barato de
verificar**. Codificar titulares, sí. Extraer hechos, no.

### 3. «¿Por qué no usamos discursos reales, si tenemos 8 MB?»

Por una sola razón y es decisiva: **con Aguasclaras tenemos el padrón de la verdad**.
Cuando el modelo se inventa una diputada, abrimos la lista completa y mostramos, en cinco
segundos y delante de todos, que no está. Con un corpus real habría que ir a chequear a
mano cada afirmación — que es, justamente, el problema del que trata la clase.

Y el precio hay que decirlo también: el vocabulario es pobre, así que **el modelo aprende
mejor de lo que aprendería con texto real**. Está en `datos/README.md` §1.5, y quien
quiera comparar tiene `datos.corpus_mini_gpt()` con 2,2 MB de discursos de verdad.

### 4. «Si la máquina escribe como un diputado, ¿el discurso político es predecible?»

**Es la mejor pregunta que puede salir en esta clase** y hay que tomarla en serio, no
esquivarla.

Lo que el experimento muestra: **una parte muy grande de la información de un texto
institucional está en su forma**, y esa parte es aprendible con relativamente poco. Eso no
es una novedad para nadie que haya trabajado con análisis del discurso — es la noción de
género — pero acá está **cuantificada**: 1,5 millones de parámetros y cinco minutos.

Lo que **no** muestra: que el contenido sea predecible. El modelo produce forma vacía. La
disputa política —qué se dice, quién lo dice, qué consecuencias tiene— no está en lo que
el modelo aprendió. Y el corpus es sintético, así que ni siquiera podemos hablar de
discurso real.

El giro que vale la pena dejar planteado: **si la forma es tan predecible, entonces lo
interesante para investigar es la desviación**. Los momentos en que un discurso se sale
del género. Eso sí es una hipótesis de investigación y sale de esta clase.

### 5. «Entonces, ¿me conviene aprender esto o esperar a que los modelos lo hagan solo?»

Lo que aprendiste hoy **no se vuelve obsoleto**, y esa es la apuesta del curso. Los
modelos que vengan van a ser mucho mejores, y van a compensar muchas de estas cosas con
herramientas y con razonamiento paso a paso. Pero mientras sean modelos de lenguaje,
van a producir una distribución sobre la próxima ficha, van a tokenizar, van a tener una
ventana finita y van a sortear. La escala mejora la calidad; no cambia la naturaleza.

Lo que sí se vuelve obsoleto es la lista de trucos de prompting y la API de tal
biblioteca. Por eso este curso enseña el mecanismo y no los trucos.

Y la parte que nunca la va a hacer el modelo por vos: **decidir si lo que medís es lo que
decís que medís**. Eso es la clase 10, y es tu oficio.

---

## 12. Después de la clase

- Los términos nuevos van a `recursos/glosario.md` (ya están cargados: *token*,
  *cross-entropy*, *temperature*, *context window*, *hallucination*, *autoregressive*,
  *instruction tuning*, *RLHF*).
- Si el aula corrió el notebook en Colab con GPU, **pediles el número de segundos** y
  actualizá la §9 de este archivo. Es la única cifra de la clase que quedó sin medir.
  (La ruta con GPU ya no se rompe: el sorteo se hace en CPU. Se probó simulando la GPU con
  el backend MPS de una Mac; en una T4 real no se probó.)
- Recordales que los 🏠 del notebook (la loss a mano, los TODO 2 a 5, la fabricación
  medida, el BPE) son opcionales, antes de la clase 9, y no más de media hora. Si
  alguien quiere hacerlos en pares, mejor.
- Las secciones 6 a 9 de la clase 7 que no se hicieron **no son requisito**: la 8 ya
  las cubrió con el re-anclaje y con el modelo funcionando. Quien quiera, las hace en
  casa.
- El puente a la clase 9 conviene mandarlo por escrito el mismo día: *«entrenar uno desde
  cero cuesta una fortuna y casi nunca es lo que necesitás. La próxima agarramos uno que
  ya entrenó otro.»*
