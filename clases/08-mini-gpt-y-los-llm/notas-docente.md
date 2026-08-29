# Notas del docente — Clase 8

**Un mini-GPT propio, y la traducción a ChatGPT** · 120 minutos · cierre del módulo 2

---

## 0. Antes de entrar al aula (checklist de 5 minutos)

- [ ] Abrí `notebook.ipynb` y **corré el bootstrap y la carga del corpus** en tu máquina,
      antes de la clase. Si algo va a fallar, que falle sin treinta personas mirando.
- [ ] Abrí las cuatro `viz/*.html` una vez. Funcionan sin internet, pero comprobalo.
- [ ] Tené a mano `datos/README.md` §1.5 (por qué Aguasclaras es sintético). La pregunta
      «¿por qué no usaron discursos reales?» sale **siempre** y la respuesta es buena.
- [ ] Poné el reloj a la vista. Esta clase se atrasa sola: la parte de la traducción es
      tan divertida que se come el cierre, y el cierre es lo que paga el módulo.
- [ ] Decidí **ahora** si el aula tiene GPU (Colab con T4) o no. Cambia el número que
      decís en la slide 12.

---

## 1. El arco narrativo, en diez líneas

1. Se lee un párrafo de debate parlamentario. Suena real. Se vota. Lo escribió una máquina.
2. Esa máquina tiene 1.541.056 perillas y se entrena en seis minutos, acá.
3. Su único objetivo es tontísimo: **poner una probabilidad a la próxima ficha**.
4. Y sin embargo, con ese objetivo, el dataset se arma solo y aparece todo lo demás.
5. Se arranca el entrenamiento en el minuto 20 y se lo deja corriendo como teatro.
6. Mientras corre, se ve la progresión: sopa de letras → sílabas → palabras → cadencia.
7. **Aprende la forma antes que el contenido.** Ése es el hallazgo de la primera mitad.
8. Segunda mitad: cada pieza del modelo se traduce a un comportamiento de ChatGPT que ya
   vivieron. Alucinación, prompt, ventana, temperatura, conteo de letras, contradicción.
9. Nada de eso es un bug misterioso: **todo se sigue del mecanismo**, y la escala no lo
   cambia.
10. Cierre: qué le falta para ser ChatGPT (escala, instruction tuning, RLHF), qué **no**
    cambia nunca, y qué se puede hacer con esto en una investigación el lunes.

**La frase que tiene que quedar.** *«Un modelo de lenguaje produce texto plausible. Lo
plausible y lo verdadero coinciden la mayoría de las veces, y eso es exactamente lo que
hace tan peligrosa la excepción.»*

---

## 2. El plan de tiempos, bloque por bloque

| Min | Bloque | Slides | Qué hacés vos |
|---|---|---|---|
| **0-10** | Gancho: ¿real o generado? | **1-5** | Leés el párrafo en voz alta. Votan a mano alzada. Revelás. La 5 es el callback del curso entero. |
| **10-20** | El objetivo más tonto del mundo | **6-11** | El dataset se arma solo, el bigrama, la arquitectura, la cross-entropy. Rápido: es repaso. |
| **20-40** | **Manos 1: a entrenar** | **12** | **El entrenamiento arranca acá. Minuto 20 como máximo.** Recorrés el aula y volvés al proyector con las slides 14-18. |
| **40-50** | **PAUSA** | **13** | En serio. El modelo entrena solo. |
| **50-75** | **La traducción** | **19-33** | Las muestras y la curva (14-19) se muestran al volver; después el bloque que paga el módulo, con sus cuatro viz. |
| **75-100** | Manos 2 | **34** | 25 minutos. De a dos. Rompan el modelo. |
| **100-120** | Cierre | **35-41** | Qué le falta, qué no cambia, la tabla, el glosario, qué te llevás, el lunes, el puente. |

*(El deck tiene 41 slides. Las 14 a 18 —las muestras del paso 0, 50, 400, 800 y 1200— se
intercalan durante el bloque práctico 1, cada vez que volvés al proyector: no son un
bloque expositivo aparte.)*

**El único hito que no se negocia: el entrenamiento arranca en el minuto 20.** Si a las
20 no arrancó, saltate lo que sea (el bigrama, la cross-entropy) y arrancalo. Todo lo
demás de la clase depende de que a las 50 haya un modelo entrenado.

---

## 3. Bloque por bloque: qué decir, qué preguntar, qué va a pasar

### Gancho (0-10) — slides 1 a 5

Leés el párrafo generado **en voz alta y con tono de sesión**. No lo proyectes primero:
que lo escuchen. Después lo proyectás y preguntás:

> **«¿Lo dijo alguien o lo escribió una máquina? A mano alzada.»**

**Lo que va a pasar.** El aula se parte más o menos por la mitad, con una mayoría
inclinada a «lo dijo alguien» si leíste bien. Alguien va a decir «se nota que es una
máquina porque no dice nada concreto» — **agarrá ese comentario y guardalo**, porque es
literalmente el hallazgo de la primera mitad de la clase. Escribilo en el pizarrón:
*«no dice nada»*. Volvés a él en el minuto 45.

Después la promesa, y decila mirando al aula, no a la slide:

> «Todo lo que hace ChatGPT y te resulta mágico o irritante lo vas a poder explicar
> antes de que termine esta clase. No con una metáfora: con el mecanismo, mirando el
> modelo que ustedes van a entrenar.»

### El objetivo más tonto (10-20) — slides 6 a 11

**Esto es repaso y tiene que ir rápido.** No hay nada nuevo: fichas (clase 6),
embeddings (clase 6), bloque transformer (clase 7), loss y descenso (clases 3 y 4).

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

### Manos 1: entrenar (20-40) — slide 12 (y las muestras, 14 a 18)

Consigna en el pizarrón, grande:

> **1. Corran hasta la celda del entrenamiento. 2. Arránquenla. 3. NO la miren.
> Sigan leyendo la sección 6 mientras corre.**

Mientras corre, recorrés el aula. Los problemas que van a aparecer, en orden de
frecuencia:

1. **No corrieron el bootstrap.** Un tercio del aula, siempre.
2. **Corrieron celdas salteadas** y `tok` no existe. «Reiniciar entorno y ejecutar todo».
3. **Colab les asignó CPU y esperaban GPU.** Está bien: el notebook lo detecta y usa 1200
   pasos en vez de 3000. Decilo en voz alta para que nadie se asuste.
4. **Alguien cambió `DIM` "para probar"** y ahora el `revisar()` de las perillas falla con
   un mensaje que se lo dice. Ese mensaje está escrito para eso.

**Volvé a la pantalla tres veces** durante el bloque, en el proyector, con tu propia
corrida — para eso están las slides 14 a 18: paso 0, 50, 400, 800 y 1200. Leé la muestra en voz alta cada vez. **Es teatro y
hay que actuarlo.** En el paso 400 ya hay palabras del castellano y vale la pena decir:
«nadie le dio un diccionario».

### Pausa (40-50) — slide 13

**No la negocies.** El modelo entrena solo. Si alguien quiere preguntar algo, que
pregunte en la pausa: mucha gente que no levanta la mano delante de treinta personas sí
se acerca al escritorio.

### La traducción (50-75) — slides 19 a 33

**Este es el bloque por el que se hicieron las siete clases anteriores.** Ritmo:
cada pieza es una slide de mecanismo + una viz o una demo, y **cada una termina en una
frase que empieza con «por eso»**. Si una pieza no termina en un «por eso», sacala.

El orden importa y es este:

0. La **curva de loss** (slide 19), que quedó pendiente del bloque anterior — 2,5 min.
1. **Por qué alucina** (slides 21-23, viz `por-que-alucina.html`) — 7 min, el más largo.
2. **Por qué le importa el prompt** (24) — 2 min, con la demo de dos prompts del notebook.
3. **La ventana de contexto** (25-27, viz `ventana-de-contexto.html`) — 5 min.
4. **La temperatura** (28-30, viz `temperatura.html`) — 5 min.
5. **Por qué cuenta mal las letras** (31-32, viz `contar-letras.html`) — 2 min.
6. **Por qué se contradice y por qué repite** (33) — 1 min, sin viz.

**Suman 24,5 y el bloque tiene 25.** No hay aire: los minutos de cada slide están en
sus `aside` y ya están ajustados a esa suma. Si te pasás en una, sacale a otra — o usá
la lista de recortes de §7, que está en orden.

**El momento clave de todo el módulo** es el de la alucinación, y se hace así:
mostrás el prompt del diputado que existe, el modelo contesta bien, mostrás el padrón,
está. Después el de la diputada inventada, el modelo contesta con la misma soltura,
mostrás el padrón, **no está**. Y entonces la pregunta, con pausa:

> **«¿Cuál de las dos salidas se veía distinta?»**

Silencio. No la contestes vos. Que la conteste alguien: «ninguna». Ahí sacás el número
honesto que está en el panel de la viz: el modelo **le acierta el bloque a 54 de los 60
diputados reales**. Sabe cosas. Y aun así no hay manera de saber, mirando, si este caso
es uno de los que sabe.

### Manos 2 (75-100) — slide 34

**25 minutos, de a dos.** Cuatro consignas y un desafío. Recorrés y vas juntando los
mejores hallazgos para ponerlos en común en el minuto 95.

**Guardá 5 minutos para la puesta en común.** Es la mejor parte y la que siempre se
come el reloj. Elegí dos o tres pares y que cuenten qué rompieron y **por qué se rompió**.
Esa segunda mitad es la que evaluás.

### Cierre (100-120) — slides 35 a 41

Tres cosas, en este orden y sin saltearse ninguna:

1. **Qué le falta para ser ChatGPT.** Escala, instruction tuning, RLHF. Dos líneas cada
   una. El punto que hay que dejar clarísimo: **el paso 2 y el 3 son los que lo
   convierten de autocompletador en asistente**, y también de donde sale la adulación.
2. **Qué NO cambia con la escala.** La slide más importante de la clase. Decila despacio:
   *«Los modelos de 2030 van a ser mucho mejores que los de hoy y van a seguir sin tener
   casillero de "no sé", van a seguir tokenizando, van a seguir teniendo ventana finita
   y van a seguir sorteando. La escala mejora la calidad, no cambia la naturaleza.»*
3. **`[EL LUNES]`** y el puente.

---

## 4. Las preguntas que hacés al aula, y cuándo

| Minuto | Pregunta | Para qué |
|---|---|---|
| 2 | «¿Real o generado? A mano alzada.» | La apuesta. Sin ella, la revelación no vale nada. |
| 8 | «¿Qué les hizo sospechar?» | Sale «no dice nada concreto». Guardalo: es el hallazgo del minuto 45. |
| 14 | «¿Cuántos ejemplos de entrenamiento hay en una ventana de 8 fichas?» | Casi todos dicen «uno». Son ocho. |
| 45 | «Ya escribe como un diputado. ¿Está diciendo algo?» | Se cobra la apuesta del minuto 8: **la forma se aprende antes que el contenido**. |
| 56 | «¿Cuál de las dos salidas se veía distinta?» | El corazón de la clase. No la contestes vos. |
| 62 | «Antes de mover el slider: ¿qué le va a pasar al ORDEN de las barras?» | Casi todos dicen «va a cambiar». No cambia nunca. |
| 68 | «¿En qué tamaño de ventana creen que se va a romper?» | La apuesta antes de la viz de la ventana. |
| 105 | «Si mañana los modelos son diez veces más grandes, ¿cuál de estas cosas se arregla?» | La slide de "qué no cambia con la escala". Ninguna. |

---

## 5. Las respuestas típicas y cómo usarlas

**«Se nota que es una máquina porque no dice nada.»** (minuto 8)
La mejor respuesta posible y la vas a escuchar casi seguro. **Escribila en el pizarrón.**
En el minuto 45 volvés: *«Tenían razón. Y esto es lo importante: la forma —el género
discursivo, las fórmulas de cortesía, la estructura de turnos— se aprende antes que
cualquier contenido, y con mucho menos esfuerzo. En los modelos grandes eso sigue siendo
cierto: sólo que están tan bien hechos que la disociación es mucho más difícil de ver.»*

**«¿Entonces adentro tiene guardados los discursos?»**
No. Y hay una demostración de tres segundos: el corpus pesa 1,1 MB, el modelo pesa 6,2 MB
pero son 1,5 millones de números; y en la clase 9 vas a ver modelos entrenados con
terabytes que pesan gigabytes. **No entra.** Lo que hay es una compresión con pérdida, y
lo que se perdió es exactamente lo que después se inventa.

**«¿Y si le digo que no invente?»**
Excelente pregunta y hay que probarla en vivo: el notebook tiene la celda
(`MI_PROMPT_ROMPEDOR = "Por favor no inventes nada..."`). El prompt **condiciona la
distribución**, no instala un verificador. Puede bajar la tasa; no puede sacar el
mecanismo. Y ojo con la sobrecorrección: en modelos con RLHF el prompt sí ayuda bastante,
porque los entrenaron para decir «no sé» más seguido. Ayuda. No garantiza.

**«Entonces son inútiles para investigar.»** (aparece siempre en el minuto 95)
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
| **«Tiene una base de datos adentro»** | Preguntan dónde está guardada la información. | Los números del párrafo de arriba: 1,5 M de parámetros vs el corpus. No hay tablas: hay una función. Por eso no se le puede «corregir un dato». |
| **«Alucina porque le faltan datos»** | Creen que es un problema de cobertura y que se arregla con más corpus. | Alucina **por diseño**: siempre produce la continuación más plausible. Con más datos alucina *menos seguido*, no *distinto*. Es la slide «qué no cambia con la escala». |
| **«La temperatura lo hace más creativo/inteligente»** | Antropomorfizan el parámetro. | La viz de temperatura: **el orden de las barras no cambia nunca**. Sólo cambia el riesgo del sorteo. |
| **Alucinación = error** | Todo error se llama alucinación. | Distinción útil: un **error** es equivocarse en algo que estaba en la distribución; una **alucinación** es *fabricar una entidad* con confianza. Para investigar, la segunda es mucho peor **porque es verosímil**. |
| **«Este modelito no tiene nada que ver con ChatGPT»** | Descreimiento por escala. | La arquitectura es la misma; cambian escala, datos y las dos etapas posteriores. Todo lo de la tabla de traducción **sí** transfiere; la calidad y el conocimiento del mundo, no. |
| **«T=0 lo hace reproducible»** | Reportan T=0 como suficiente. | Ayuda mucho y no alcanza: cambia la versión del modelo sin aviso, cambia el hardware, hay no determinismo en la infraestructura. Se retoma en la clase 10. |
| **«El modelo entiende»** | Aparece cuando lo ven escribir bien. | No lo pelees de frente. Reformulá: *«¿qué te haría cambiar de opinión?»* y volvé a la alucinación: entender incluye poder decir «no sé». |
| **Confundir loss baja con modelo bueno** | «Le dio 0,19, entonces anda bárbaro.» | 0,19 sobre un corpus de plantillas es *demasiado* bueno, y esa es la señal. Ver §9. |

---

## 7. Si vas atrasado / si vas adelantado

### Si vas atrasado (te va a pasar)

Se recorta **en este orden**, y ni un paso antes de tiempo:

1. **El bigrama** (slide 8). Duele, pero se cuenta en dos frases sin correr nada.
2. **«Por qué repite con T baja»** (la mitad derecha de la slide 33). Es una curiosidad, no una pieza.
3. **«Por qué se contradice»** (la mitad izquierda de la 33) — se cuenta en una frase
   adentro del bloque del prompt.
4. **La viz de contar-letras** — se muestra 90 segundos sin abrirla, con la slide sola.
5. **Manos 2 baja de 25 a 15 minutos** y se saltea el desafío de a dos.

**Lo que NUNCA se recorta:**

- **La pausa.** Diez minutos. Si te la comés, la segunda mitad se atropella y la segunda
  mitad es la clase.
- **El bloque de la alucinación.** Es la razón de ser del módulo.
- **La slide «qué NO cambia con la escala»** (36). Si sólo te quedan tres minutos,
  esa slide y el `[EL LUNES]`. Todo lo demás es prescindible antes que eso.
- **El puente a la clase 9.** Sin él, la 9 arranca en el aire.

### Si vas adelantado

- Abrí `viz/temperatura.html` con el prompt «El bloque del » y hacé que el aula prediga
  qué partido va a salir antes de generar. Es divertido y muestra la distribución en vivo.
- Mostrá `viz/tokenizador.html` de la **clase 6** al lado de `contar-letras.html`. El
  guiño «prometido en la clase 6, cumplido» funciona mejor con las dos abiertas.
- Discutan: *«si el corpus fueran discursos parlamentarios reales en vez de sintéticos,
  ¿qué cambiaría?»* (Respuesta: aprendería mucho peor con el mismo presupuesto, el
  vocabulario es 10-20 veces más rico; y no podríamos hacer la demo de la alucinación,
  porque nadie puede verificar en cinco segundos si un diputado argentino existe.)
- Que alguien busque en el `padron_detalle` de `datos-mini-gpt.json` los **6** diputados
  a los que el modelo les erra el bloque, y que discutan si tienen algo en común.
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
  transformer tiene un **corte duro**. Lo que quedó afuera de la ventana no está borroso:
  **no está**.
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
en el contenedor de construcción. **Si citás un número en el aula, citá estos.**

| qué | valor |
|---|---|
| parámetros del modelo | **1.541.056** (4 bloques · 4 cabezas · dim 176 · ventana 128 fichas) |
| corpus | Aguasclaras, 1.098.206 caracteres, vocabulario de **71** fichas |
| entrenamiento (la celda sola, 1200 pasos) | **entre 4 y 7 minutos** en CPU con **4 hilos**. Cinco cronometrajes de la misma corrida: **243 s** y **267 s** con `entrenar-mini-gpt.py`, y **297 s**, **360 s** y **432 s** con la celda del notebook (0,25 a 0,36 s por paso). |
| el notebook ENTERO, de punta a punta | **entre 5 min 40 s y 8 min** (`nbconvert --execute`): **339 s**, **361 s**, **368 s**, **376 s**, **404 s**, **480 s**. |
| por qué se mueve tanto | La CPU es compartida: el mismo notebook, en la misma máquina, tarda un 40-80% más si tenés el navegador con las viz abierto al lado — que es exactamente lo que va a pasar en el aula. **Decí «entre cuatro y siete minutos» y planificá con siete.** Nunca des un número al segundo. |
| loss de validación | **4,23 → 0,19** (el piso teórico de «no tengo idea» es log 71 = 4,26) |
| loss del bigrama en validación | **2,24** (la línea de base tonta) |
| tamaño del checkpoint | 6,2 MB para un corpus de 1,1 MB |
| aciertos de bloque sobre el padrón | **54 de 60** diputados reales |
| aciertos de provincia sobre el padrón | 33 de 60 |

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
fichas de un texto muy repetitivo. Si querés mostrar una tijera de verdad, entrená el
mismo modelo sobre `texto[:25_000]` (25 KB): la validación toca fondo cerca del paso
**700-900** (≈ 0,70-0,74) y **sube** hacia el 1200 (0,79-0,82) mientras la de train sigue
bajando a **0,10**. Ésos son los números del ítem 6 del cuestionario.

> **Precisión sobre estos números, porque importa en una clase que enseña a no inventar.**
> Se corrieron **dos veces**. La **forma** —tijera clarísima, train diez veces más chica
> que val— sale idéntica las dos veces. Los **valores paso a paso, no**: con 25 KB el
> conjunto de validación son 2.500 fichas, y medir la loss sobre ocho lotes de ese
> puñado tiene ruido de ±0,1. En una corrida el mínimo cayó en el paso 900 (0,70) y en
> la otra en el 700 (0,74). **La tabla del cuestionario es una corrida real, no la
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
la ventana entera — apenas por encima del azar (1 de 6) — y la curva es **plana**. Nunca
aprendió esa dependencia larga: sólo 67 de las 238 apariciones la tienen a menos de 128
fichas, y 1200 pasos de un modelo de 4 bloques no alcanzan.

Publicar la viz original habría sido **inventar un resultado**, que es exactamente lo que
este curso enseña a no hacer. Así que la viz muestra ahora dos mediciones reales:

- **la pista cerca** (el nombre del diputado predice su bloque, a ~16 fichas):
  7/30 → 14/30 → 24/30 → 28/30 a medida que el nombre entra en la ventana. **El corte
  duro se ve perfecto.**
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
| La salida es **siempre** una distribución de probabilidad | Alucina; nunca dice «no sé» espontáneamente; suena igual de seguro cuando acierta que cuando inventa |
| Está **condicionada por el texto previo** | El prompt cambia todo; el rol asignado («sos un experto en…») cambia el registro; el prompt es un instrumento de medición |
| La **ventana de atención es finita** | Se olvida del principio de una conversación larga; ignora instrucciones lejanas; hay que repetir lo importante al final |
| **Costo cuadrático** de attention | Por qué la ventana tiene un límite y por qué un prompt largo cuesta más caro |
| Hay un **sorteo** al elegir la ficha (temperatura) | El mismo prompt da respuestas distintas; T=0 lo hace repetitivo; T alta lo hace delirante; sin semilla no hay reproducibilidad |
| Trabaja con **fichas**, no con letras | Cuenta mal las letras, falla con rimas y anagramas, se equivoca con aritmética, anda peor en idiomas poco representados |
| **No hay estado de creencias**, sólo condicionamiento | Se contradice; una vez que arrancó por un camino equivocado sigue por ahí; se lo puede «convencer» de casi cualquier cosa |
| Entrenado para predecir **texto plausible** | Produce referencias bibliográficas con formato perfecto y datos inventados: el formato es lo más predecible que hay |
| **Instruction tuning + RLHF** encima | Responde consignas en vez de completar; es amable; a veces adula y te da la razón |
| Aprendió **del corpus** | Reproduce los sesgos del corpus; sabe mucho de lo que abunda en internet y poco de lo que no |

---

## 11. Si te preguntan X — las cinco difíciles

### 1. «¿Esto quiere decir que los LLM no entienden nada?»

**La pregunta honesta de la clase, y merece una respuesta honesta.** No contestes ni que
sí ni que no, porque las dos son propaganda.

Lo que **sí** podemos afirmar desde el mecanismo, sin discusión: no hay un módulo que
verifique verdad, no hay un estado de creencias que se sostenga entre respuestas, y no
hay un casillero para «no sé». Eso no es opinión: es lo que acaban de ver.

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
3. **Una muestra validada a mano**: al menos 100 casos codificados por vos, y reportás el
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
modelos de 2030 van a ser mucho mejores y van a seguir produciendo una distribución sobre
la próxima ficha, van a seguir tokenizando, van a seguir teniendo una ventana finita y
van a seguir sorteando. La escala mejora la calidad; no cambia la naturaleza.

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
- El puente a la clase 9 conviene mandarlo por escrito el mismo día: *«entrenar uno desde
  cero cuesta una fortuna y casi nunca es lo que necesitás. La próxima agarramos uno que
  ya entrenó otro.»*
