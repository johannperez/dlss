# Clase 5 — Notas para quien da la clase

**La forma de los datos manda (I): imágenes**
120 minutos · apertura del módulo 2 · prerrequisitos: clases 1 a 4

---

## 1. El arco narrativo en diez líneas

1. Proyectás una foto y preguntás cuánta gente hay. Todos contestan **en dos segundos y sin pensar**.
2. Mostrás la misma foto corrida unos píxeles. Para ellos es igual; para el modelo de la clase 4
   **cambiaron las 784 variables al mismo tiempo**. Ahí queda instalada la pregunta del día.
3. Aplanás una imagen delante de ellos y se ve dónde se perdió la vecindad.
4. **Votan** si barajar los píxeles empeora el modelo. Casi todos dicen que sí.
5. La viz muestra que la red densa saca **exactamente lo mismo**: nunca supo que había una grilla.
6. La solución es un gesto, no una fórmula: mirar de a nueve y deslizar la ventanita.
   Un filtro es un pincel; nueve números y ya tenés un detector de bordes.
7. Practican. Escriben la convolución con dos `for` e inventan un filtro propio.
8. Pausa. Vuelven y se apilan las capas: bordes → texturas → partes → objetos. Nadie programó eso.
9. **La slide de la clase**: la arquitectura es una teoría sobre el mundo. Y la viz de supuestos
   les muestra que, para una tabla de encuesta, esa teoría es falsa y conviene otra herramienta.
10. Cierre con el caso de pobreza desde satélites y las tres preguntas. El puente: el texto
    tampoco es una grilla; es una secuencia.

**Si te llevás una sola frase para repetir:** *los supuestos no son una debilidad del modelo,
son lo que lo hace utilizable. Un modelo sin supuestos no es más objetivo: es más hambriento
de datos y más fácil de engañar.*

---

## 2. Plan de tiempos real, bloque por bloque

> **Los números de slide de este documento son los que muestra el contador de
> `slides.html` abajo a la derecha (`n / 36`), con la pausa contada como la 18.**
> Si venís de leer la especificación, ahí la pausa no está numerada y todo lo que
> va después lleva un número menos.

| Min | Slides | Bloque | Qué hacés |
|---|---|---|---|
| **0-2** | 1 | Portada | Una frase y pasás. No leas objetivos. |
| **2-5** | 2 | Dónde quedamos | Cuatro viñetas, rápido. La quinta es el giro: la generalidad es un problema. |
| **5-7** | 3 | **¿Cuánta gente hay?** | Que tiren números en voz alta. No corrijas a nadie. |
| **7-10** | 4 | La foto corrida | *"¿Es la misma foto?"* Sí. *"Para la red le moví las 784 variables."* |
| **10-12** | 5 | La imagen es una tabla | Señalás un número y preguntás qué es. |
| **12-15** | 6 | Aplanar | Con el dedo: acá la grilla, acá la fila. Preguntás qué se perdió. |
| **15-17** | 7 | **VOTACIÓN** | A mano alzada, contás en voz alta y anotás en el pizarrón. |
| **17-23** | 8 | **VIZ barajado** | Barajar → tiras → barras. Después la pestaña «correrla». |
| **23-25** | 9-10 | La conclusión + los tres supuestos | La analogía del marco teórico, textual. |
| **25-28** | 11-12 | Mirar de a pedacitos y deslizar | El gesto con la mano. El nombre después. |
| **28-36** | 13 | **VIZ kernel deslizante** | El guion de la sección 5 de estas notas. |
| **36-40** | 14-15 | El pincel + se aprenden | El callback a la clase 2 y el cierre del «filtro al azar». |
| **40-43** | 16 | La cuenta que importa | Los dos números en el pizarrón. |
| **43-45** | 17 | Consignas del práctico 1 | Leelas en voz alta. |
| **45-60** | — | **Práctico 1** | Notebook, secciones 1-3. Pasás por las mesas. |
| **60-70** | **18** | **PAUSA** | Diez minutos. **No se toca.** Poné alarma. |
| **70-74** | 19 | Volvimos: ¿qué filtro inventaron? | Proyectás dos o tres del aula. |
| **74-78** | 20 | Apilar filtros | La segunda capa no mira la imagen. |
| **78-83** | 21 | **VIZ jerarquía** | «La rueda» y «la multitud». Aclarás que es un esquema. |
| **83-85** | 22-23 | Por qué profundo + pooling | La promesa de la clase 2, cobrada. Pooling en 30 s de verdad. |
| **85-88** | 24-25 | La CNN completa + **la arquitectura es una teoría** | La slide central. Leela despacio. |
| **88-94** | 26 | **VIZ supuestos** | Satelital primero; después «tabla de encuesta» y te callás. |
| **94-95** | 27 | Consignas del práctico 2 | |
| **95-108** | — | **Práctico 2** | De a dos. Secciones 4-5 del notebook. |
| **108-110** | 28 | El resultado | Comparás con lo que les dio a ellos. |
| **110-116** | 29-31 | El caso y las tres preguntas | El bloque de ciencias sociales. **Nunca se recorta.** |
| **116-120** | 32-36 | Cierre | El lunes, otros usos, tres ideas, glosario, puente. |

> **Ojo con el reloj.** El presupuesto oficial le da 20 minutos al práctico 2 (85-105) y 15 al
> cierre. El plan de arriba le saca cinco minutos al práctico y se los da al bloque del caso,
> porque el práctico se puede terminar en casa y **la lectura crítica no**.

---

## 3. Qué preguntar al aula, y cuándo

| Momento | La pregunta | Para qué |
|---|---|---|
| Slide 3 | **"¿Cuánta gente hay?"** | Que contesten sin pensar. Eso es lo que hay que explicar después. |
| Slide 4 | **"¿Es la misma foto?"** | Que digan "sí" en voz alta. Es el contraste con lo que le pasa al modelo. |
| Slide 6 | "¿Qué información tenía la grilla que la fila no tiene?" | Que aparezca la palabra **vecindad** o **posición**. Anotala en el pizarrón. |
| Slide 7 | **"¿A, B o C? Voten."** | Sin la apuesta previa, la viz que sigue es un dibujito lindo. |
| Slide 8, después de barajar | "¿Quién había votado A?" | El error público sin costo. Es el motor de la clase. |
| Slide 13 (viz) | "¿Cuántos filtros al azar sirvieron?" | Prepara la slide 15: por eso se **aprenden**. |
| Slide 16 | "¿De dónde sale que 288 alcancen?" | Que aparezca «se reusan los mismos nueve números». |
| Slide 25 | **"¿Alguien puede darme un supuesto de este tipo en su propio trabajo?"** | El momento en que la clase deja de ser sobre CNNs. |
| Slide 26 (viz) | "Si reordenás las columnas de tu CSV, ¿cambió algo?" | Demuele el supuesto de vecindad para tablas, en una línea. |
| Práctico 2 | "¿Qué tienen en común los errores?" | La pregunta profesional de toda la clase. |

---

## 4. Las respuestas típicas y cómo usarlas

**En la votación de la slide 7.** La mayoría vota A («empeora muchísimo»). Está bien que se
equivoquen: el razonamiento es correcto para *nosotros* (nosotros no reconocemos nada en el
revoltijo) y falso para la red densa. Usá exactamente esa frase: *"votaron pensando en ustedes,
no en el modelo"*.

**"Es que barajar destruye la información."** Es la objeción más frecuente y es *falsa*: una
permutación es reversible, no se pierde ni un número. Por eso la viz muestra las dos tiras de
784 valores. Si alguien insiste, mostrá el `assert` del notebook: `np.allclose(originales
ordenados, barajados ordenados)` da `True`.

**"Entonces la CNN es mejor."** Frená ahí. La CNN es mejor **para datos con grilla**.
Prometeles que después de la pausa vas a mostrar un caso donde es peor que casi todo, y cumplilo
con la viz de supuestos.

**"¿Y si en vez de barajar rotamos la imagen?"** Excelente pregunta y aparece todos los años.
La invariancia **traslacional** viene de regalo; la **rotacional** no. Si tus fotos de test están
rotadas 90°, la CNN se cae. Se arregla con *data augmentation* (entrenar con copias rotadas), que
es admitir el supuesto y comprarlo con datos. Es la pregunta 4 del cuestionario.

**"Mi archivo tiene 300 fotos, no 12.000."** Esa es la buena noticia del día: es exactamente el
régimen donde el sesgo inductivo paga. Y es la puerta a la clase 9 (usar un modelo ya entrenado
por otro). Anotá quién lo preguntó: tiene una monografía ahí.

---

## 5. El guion de la viz del filtro (slide 13)

Es la viz central y conviene tenerlo pautado. Seis minutos.

1. **Preset «borde vertical» sobre el afiche de campaña.** *"Miren dónde se enciende: en los
   contornos verticales de las letras. Nadie escribió una regla sobre bordes: elegimos nueve
   números."*
2. **Preset «todo cero».** No aparece nada. *"Todo por cero es cero. El filtro es una elección."*
3. **Preset «identidad».** Sale la imagen igual. *"Ésta es la que tienen que resolver en el
   `TODO 3`. No se los digo."*
4. **Cambiá el filtro a mano**, un número, delante de ellos. Que vean que el mapa cambia en vivo.
5. **«Filtro al azar», diez veces, contando en voz alta** cuántos sirven. Casi ninguno.
   Ese conteo es el pie de la slide siguiente.
6. **Vocabulario, dos veces:** el **filtro** son los nueve números (panel 2); el **mapa de
   activación** es el dibujo (panel 3). Señalá los paneles con el dedo mientras lo decís.

---

## 6. Las confusiones de principiante y cómo desarmarlas

| Confusión | Cómo se manifiesta | Cómo la desarmás |
|---|---|---|
| **«La CNN es mejor que la densa»** | Generalizan una comparación específica. | Es mejor *para datos con estructura espacial*. Viz de supuestos, fila de datos tabulares. |
| **«El filtro busca objetos»** | Creen que un filtro de la primera capa detecta «personas». | Un filtro de 3×3 sólo ve nueve píxeles: no puede ver una persona. Las cosas grandes aparecen por **composición**, en capas profundas. Viz de jerarquía. |
| **Filtro vs mapa de activación** | Llaman «filtro» a la imagen de salida. | Vocabulario firme y repetido, señalando los paneles 2 y 3 de la viz. Es la confusión que más se pega si no la cortás el primer día. |
| **«El modelo ve como nosotros»** | Antropomorfización. | El `TODO 5`: el modelo confunde copas de árboles con multitudes. Ningún humano hace eso. |
| **Pánico con las dimensiones** | Se pierden con `(batch, canales, alto, ancho)` y se frustran con los errores de forma. | La mnemotecnia: *cuántas fotos, cuántas capas de color, cuán alta, cuán ancha*. Y **enseñales a leer el error**: «expected 4-dimensional input… got 2-dimensional» te está diciendo qué falta. Leer errores es contenido. |
| **Querer entender pooling/stride/padding a fondo** | Se traban en detalles. | Decilo explícito: *"esto es plomería. El día que armes una red lo googleás. No son conceptos."* |
| **«Entonces mido pobreza con satélites y listo»** | Entusiasmo acrítico con el caso. | Slides 30-31, y la pregunta que ordena todo: **¿qué está midiendo realmente?** |
| **«¿Por qué el mapa sale más chico?»** | Confusión con las formas de salida. | La ventana no se puede asomar afuera de la foto: pierde un píxel de cada lado. Nada más. |

---

## 7. Si vas atrasado (y vas a ir atrasado)

**El orden en que se recorta:**

1. **Slide 23 (pooling).** Es plomería declarada. Decí una frase y pasá.
2. **Slide 33 (otros usos en ciencias sociales).** Mandalo por mail; está escrito.
3. **Slide 22 (por qué profundo).** Duele, pero se puede resumir en la 21 mientras mostrás la viz.
4. **Cinco minutos del práctico 2.** El notebook se puede terminar en casa; lo que no se puede
   es hacer la lectura crítica sin docente.

**Lo que NUNCA se recorta, en ningún escenario:**

- **La pausa** (minutos 60-70).
- **La votación de la slide 7 y la viz del barajado.** Sin la apuesta previa la clase se
  desinfla entera.
- **Las slides 25-26** (la arquitectura es una teoría + cuándo es falsa). Es el objetivo real de
  la clase; las CNN son el vehículo.
- **Las slides 29-31** (el caso y las tres preguntas). Es lo que hace que esta sea una clase de
  ciencias sociales y no de visión por computadora.

Si tenés que elegir entre terminar el práctico 2 y hacer el bloque 29-31, hacé el bloque 29-31.

---

## 8. Si vas adelantado

- **Volvé a la viz del kernel y dejá que un estudiante maneje.** Que elija imagen y filtro y
  narre lo que ve. Es la mejor forma de comprobar si el vocabulario quedó.
- **Abrí la viz de supuestos y recorré las cinco opciones de datos**, no sólo dos. La de «una
  red de contactos» genera buena discusión.
- **La pregunta de la rotación**: mostrala en el notebook rotando `X_te` con
  `torch.rot90(X_te, 1, (2, 3))` y midiendo. Se cae. Es un minuto y vale oro.
- **Adelantá la conversación de la clase 9**: "¿y si no tengo 12.000 imágenes etiquetadas?".

---

## 9. Los chistes y las analogías que funcionan

- **La foto corrida.** *"Para ustedes es la misma foto. Para el modelo de la clase 4, es una
  catástrofe cósmica."*
- **El barajado.** Mientras corre la animación: *"miren, no se perdió ni un píxel. Es la misma
  información. Es un tetris."* Y después: *"la red densa sacó lo mismo. No se enteró de nada.
  Es el compañero de trabajo que dice que sí a todo."*
- **El libro de códigos.** Un filtro es una regla de codificación aplicada exhaustivamente; una
  CNN es un ejército de codificadores que no se cansa, no se enferma y no discute. El problema:
  **su libro de códigos no está escrito en castellano**. Nadie sabe qué codificó.
- **El marco teórico.** *"Un modelo sin supuestos no es más objetivo: es más ignorante.
  Igual que una investigación sin marco teórico no es más neutral, es más desorientada."*
  Decila textual; es la columna vertebral de la clase.
- **La equivalencia de medición.** «Un patrón vale igual esté donde esté» = «esta pregunta
  significa lo mismo en todas las provincias». Los mira a los ojos.
- **Los filtros al azar.** *"Van nueve. ¿Alguno les gustó? Bueno, por eso existe el descenso
  por gradiente."*

---

## 10. Si te preguntan X

**«¿Esto no es lo mismo que un filtro de Instagram?»**
Sí, literalmente: los filtros de desenfoque y de realce de cualquier editor de fotos **son**
convoluciones, y son de los que están en la viz. Lo nuevo acá es que los nueve números **no los
elige un diseñador: los encuentra el descenso por gradiente**, optimizando una tarea. Es una
gran analogía y conviene usarla, no esquivarla.

**«¿Cuántas imágenes etiquetadas necesito para mi archivo?»**
Honestamente: depende de qué tan separables sean tus categorías, y no hay número mágico. Órdenes
de magnitud realistas: con **100-300 por clase** y un modelo ya entrenado por otro (clase 9) se
puede empezar a mirar algo; entrenando desde cero, como hoy, necesitás miles. La respuesta
metodológica es mejor que la técnica: **etiquetá 100, medí, y decidí si vale la pena seguir
etiquetando.** Es exactamente el mismo razonamiento que con codificadores humanos.

**«¿Esto no es una caja negra? ¿Cómo lo justifico ante un revisor?»**
Es una caja negra en el sentido de que no podés leer la regla; no lo es en el sentido de que
podés **auditar su comportamiento**. Lo que se reporta no es "qué piensa el modelo", sino:
cómo partiste los datos, qué acierta y qué falla, **en qué subgrupos falla más**, y qué pasa
fuera de la muestra. Eso es exactamente lo que hicieron en el `TODO 5`. La clase 10 es entera
sobre esto.

**«¿No estamos automatizando un sesgo? Si el archivo tiene más fotos de un tipo de acto…»**
Sí, y esa es la lectura correcta. El modelo aprende **la distribución del archivo**, no la del
mundo: si tu archivo sobrerrepresenta las movilizaciones grandes y céntricas, el modelo va a ser
peor con las chicas y periféricas, y ese error no se distribuye al azar. Es la contracara de que
funcione. La salvaguarda mínima: reportar desempeño **por subgrupo**, no sólo global.

**«¿Puedo usar esto para contar personas en una foto y publicar el número?»**
Podés estimarlo; publicarlo como dato requiere lo mismo que cualquier medición: validación contra
un patrón de oro en tu propio material, un intervalo de error, y decir de dónde salió. El conteo
de multitudes es un campo con literatura propia y con disputa política sobre las cifras, así que
si vas a entrar ahí, entrá con la validación adelante y no atrás.

**«¿Y esto para qué me sirve si yo trabajo con encuestas?»**
Dos cosas, y las dos son de esta clase. Primero: ahora sabés **cuándo NO usarlo** —la viz de
supuestos con la tabla de encuesta— y eso te ahorra un proyecto entero mal encarado. Segundo: la
idea de que **la arquitectura es una teoría** no es sobre imágenes; es sobre cualquier modelo,
incluidos los tuyos. Cuando elegís efectos fijos por provincia estás afirmando algo sobre el
mundo, exactamente igual.

---

## 11. Chequeo antes de entrar al aula

- [ ] `slides.html` abre con doble clic, sin internet, y las cuatro viz cargan adentro.
- [ ] Probaste las viz **sueltas** en pantalla completa: son las que vas a proyectar.
- [ ] Corriste el notebook entero una vez esta semana (**tarda unos 2 minutos** en CPU:
      medido acá, 116 s con la máquina tranquila; en Colab, más).
- [ ] Tenés la alarma de la pausa puesta.
- [ ] Sabés de memoria los cuatro números de la slide 28: **85,8 / 85,6 / 87,8 / 83,2**,
      y el par de la foto corrida: **32,3** contra **74,1**.
- [ ] Si conseguiste una foto real de una movilización con licencia libre, ponela en la slide 3
      en lugar del esquema sintético. El esquema funciona, pero una foto de verdad funciona mejor.
