# Clase 1 — Notas para quien la da

**Una función es una máquina con perillas** · 120 minutos · 35 slides
Prerrequisitos: ninguno. Nivel de código de la audiencia: cero previo.

> **Lo único que no se puede perder hoy:** que se vayan sabiendo distinguir una
> **variable** de un **parámetro**, y con ganas de volver a la próxima clase.
> Todo lo demás es negociable.

---

## 1. El arco narrativo en diez líneas

1. Se proyectan los treinta y seis puntos sin ejes y se pregunta qué le pasó a este país.
2. Se revelan los ejes: es cuánto se habló de seguridad en los discursos de apertura.
3. Se pregunta qué **línea** resumiría eso. La intención de modelar aparece sola.
4. Para dibujar una recta hacen falta dos números. Ese es el curso entero.
5. Se instala la imagen de la clase: **la caja con perillas**, que vuelve diez clases.
6. Se separa lo que entra (variable) de lo que la deforma (parámetro). Se vota, se
   falla, y recién ahí se muestra la viz que lo resuelve.
7. Aparece un número que mide qué tan mal está el dibujo. **No se lo llama loss.**
8. Ellos mueven las perillas contra datos reales y descubren que hay un piso.
9. Se recorre el zoo de formas y se descubre que cada forma tiene un repertorio
   limitado: hay figuras que ninguna puede dibujar.
10. Fin con la puerta abierta: la salida no es una fórmula más rara, es apilar.
    Eso es la clase 2.

---

## 2. Plan de tiempos real

| Min | Slides | Bloque | Qué pasa |
|---|---|---|---|
| 0:00 | 1-2 | Apertura | Portada + «de dónde venimos». 3 minutos, no más. |
| 0:03 | 3-6 | **Gancho** | Los puntos misteriosos, la revelación, la votación, las tres candidatas. |
| 0:14 | 7-11 | Idea 1 | Dos números · la caja · la fórmula · variable vs parámetro · «ya usás parámetros». |
| 0:25 | 12 | **Viz 1** | `maquina-de-perillas.html`. El docente la mueve. 6 minutos. |
| 0:31 | 13-14 | Apuesta + **Viz 2** | Se vota primero, se muestra después. `variable-vs-parametro.html`. |
| 0:40 | 15 | El desajuste | Los palitos rojos y el número grande. 2 minutos. |
| 0:42 | 16 | **Manos 1** | Notebook, secciones 1-3. 18 minutos de trabajo. |
| 1:00 | 17 | **PAUSA** | 10 minutos. **No se toca.** |
| 1:10 | 18 | Volvimos | Qué encontraron. 2 minutos. |
| 1:12 | 19-24 | Idea 2 | El zoo: la grilla y las cinco formas, una slide cada una. |
| 1:22 | 25 | **Viz 3** | `zoo-de-funciones.html` y los tres desafíos. 3 minutos. |
| 1:25 | 26 | La misma fórmula, otra historia | El corazón sustantivo de la clase. |
| 1:27 | 27 | **Manos 2** | Notebook, sección 4 (`TODO 2`; el `TODO 3` para quien vaya rápido). Ajuste a ojo de a dos. 18 minutos. Las secciones 5 y 6 quedan para después de clase. |
| 1:45 | 28-29 | El ranking | La tabla y «lo que hicieron tiene nombre». |
| 1:50 | 30-32 | Cierre | `[EN TU INVESTIGACIÓN]` · el fracaso de la recta contra inflación · los dos caminos. |
| 1:57 | 33-35 | Salida | Qué te llevás · glosario · el puente a la clase 2. |

Suma: 120 minutos exactos, con la pausa adentro.

**Entre esta clase y la 2 hay dos días** (el curso va lunes, miércoles y viernes). Lo que
se pide para antes de la clase 2 tiene que entrar en menos de una hora: el cuestionario
(unos 20 minutos) y la sección 6 del notebook (unos 10). La sección 5, el `TODO 3` y el
bonus del cuestionario son opcionales. El `[EN TU INVESTIGACIÓN]` no es tarea con fecha:
es cómo se usa lo de hoy en su propio trabajo.

---

## 3. Qué preguntar al aula, y cuándo

### Minuto 3 — «¿Qué historia cuenta esto?» (slide 3)

Es **la** pregunta de la clase y hay que aguantarse el silencio. Contá hasta quince
antes de volver a hablar. Anotá dos o tres versiones en el pizarrón, textuales.

**Respuestas típicas y qué hacer con cada una:**

| Lo que dicen | Qué hacer |
|---|---|
| «Es la inflación / el dólar» | No corrijas. Anotalo. En la slide 4 la revelación pega más fuerte. |
| «Hubo una crisis en 2001» | Perfecto: están leyendo el eje x sin que se lo hayas dado. Marcalo: «me acabás de decir que sabés qué es el eje horizontal». |
| «Sube» | Preguntá: «¿sube siempre? ¿o sube y baja?». Es la primera vez que discuten forma. |
| «Faltan los ejes, no se puede decir nada» | **Regalo.** «Tenés razón, y sin embargo cinco personas dijeron algo. Guardá esa incomodidad: es la clase 10.» |
| Silencio total | Tirá vos una versión obviamente absurda («esto es la cantidad de pingüinos») y esperá. Alguien va a corregirte y ya arrancó la conversación. |

### Minuto 10 — «¿Qué línea dibujarías?» (slide 5)

Que lo hagan **con el brazo en el aire**, no con palabras. Después votá A/B/C y
anotá los tres números. **Se usan en la clase 4**: cuando aparezca el sobreajuste,
volvés a esos números y decís «once de ustedes votaron la C».

### Minuto 21 — «Díganme un parámetro de su investigación» (slide 10)

Primero pedí una **variable**: sale rápido y da confianza. Después pedí un
**parámetro**: cuesta mucho más, y ese esfuerzo es el contenido de la clase.

Respuestas típicas:
- *«El coeficiente de mi regresión»* → perfecto, es el ejemplo canónico.
- *«El tamaño de la muestra»* → confusión útil: `n` no entra al modelo, es una
  propiedad del diseño. La regla del dedo se aplica a los números que entran.
- *«La edad»* → es variable. Preguntá: «¿la edad cambia de una fila a otra de tu
  base?». Se contesta solo.
- *«El nivel de significación, 0.05»* → excelente y sutil: es un parámetro **de tu
  procedimiento**, no del modelo. Vale marcarlo así y seguir.

### Minuto 31 — La apuesta (slide 13)

**Esta slide va antes de la viz. Siempre.** Contá las manos en voz alta y anotá el
reparto. Suele ganar **C** («las dos cosas»), que es la respuesta intuitiva y
equivocada. No corrijas: pasá a la viz y dejá que la vean fallar.

### Manos 2 y el ranking (1:27 a 1:48) — «¿Cómo hiciste para bajar el número?»

Se pregunta mientras recorrés las parejas en el bloque práctico 2 y otra vez con la tabla
del ranking (slide 28, a la 1:45). En el bloque práctico 1 (minuto 42) todavía no hay
desajuste en el notebook: aparece en la sección 4.
La pregunta **no** es cuánto sacaron. Es cómo buscaron. La respuesta que querés
escuchar es «primero moví una y después la otra». Cuando alguien lo diga, repetilo
en voz alta para todos: eso es **descenso por coordenadas** y se nombra en la clase 3.

---

## 4. Las confusiones que van a aparecer, y cómo desarmarlas

**«`x` y `a` son lo mismo, son letras.»**
Se manifiesta cuando mueven el slider equivocado buscando un efecto. La viz
`variable-vs-parametro.html` existe exactamente para esto. Reforzá con la regla del
dedo: *¿cambia de una fila a otra de mi base? Variable. ¿Es el mismo para toda la
base? Parámetro.* Repetila tres veces en la clase, textual.

**«Entonces la máquina descubre la fórmula.»**
Es la más importante de desarmar y aparece siempre. Respuesta corta y firme:
**vos elegís la familia de figuras; la máquina elige un miembro de esa familia.**
La elección de familia es tuya y es teórica. Se retoma en las clases 5 y 10. Si no
lo desarmás hoy, en la clase 9 alguien va a decir «el modelo descubrió que…» y va a
ser tarde.

**Miedo al `def`.**
Se traban en la sintaxis y no llegan al contenido. La celda del `def` se lee en voz
alta **palabra por palabra, incluidos los dos puntos y la indentación**. Decilo
explícitamente: «Python es maniático con los espacios y no es culpa tuya».

**«Si toco algo, rompo todo.»**
Se manifiesta como silencio: corren las celdas en orden y no experimentan.
El antídoto es teatral y dura treinta segundos: **rompé una celda a propósito
adelante de todos** (borrá los dos puntos del `def`), mostrá el error rojo gigante,
arreglalo, volvé a correr. «El error rojo no es un reto, es información.»

**«Bajé el número, entonces mi modelo es verdadero.»**
Hoy sólo se planta la duda; se cosecha en la clase 4. Frase para plantarla:
«bajar el desajuste te dice que tu recta pasa cerca de estos puntos. No te dice
nada sobre por qué, ni sobre si va a pasar cerca de los puntos del año que viene».

**Leer `f(x)` como «f por x».**
Clásico de quien viene de la aritmética escolar. Se dice **una vez, explícito**:
«no es una multiplicación, son los paréntesis de "aplicá f a x". Es notación
desafortunada y la sufrimos todos». Si lo decís al pasar, no queda.

**«¿Hay que memorizar las fórmulas del zoo?»**
Se manifiesta como gente copiando fórmulas en el cuaderno en el minuto 72.
Cortalo apenas lo veas: «no hay nada que memorizar. Quiero que reconozcan la
**forma**. Si ven una S, piensan "sigmoide" y buscan la fórmula en Google».

**Confundir el eje: «0,44 % es poquísimo, entonces no le importaba la seguridad».**
Es una lectura razonable y equivocada. La serie es **porcentaje de palabras de un
discurso**, y un discurso habla de veinte cosas: 0,44 % de las palabras dedicadas a
un solo léxico de 24 palabras es muchísimo en términos relativos. Lo que importa no
es el nivel absoluto sino **la variación entre años**. Si sale esta pregunta,
felicitá: es exactamente el tipo de duda que hay que tener.

---

## 5. Si vas atrasado

**Lo que se recorta, en este orden:**

1. **Slide 2** («de dónde venimos»). Es la primera en irse: gana 2 minutos.
2. **Slides 22 y 24** (exponencial y seno). Se mencionan de paso desde la grilla del
   zoo (slide 19) y listo. Gana 2,5 minutos.
3. **Slide 11** («ustedes ya usan parámetros»). Se dice en una frase sobre la
   slide 10. Gana 1 minuto.
4. **El bloque práctico 2** se recorta a 12 minutos y el `TODO 3` (la búsqueda por
   grilla) queda como opcional para después. Gana 6 minutos. No lo sumes como tarea
   obligatoria: entre la clase 1 y la 2 hay dos días.
5. **Slide 32** (los dos caminos). Se dice en dos frases sobre la slide 31.

**Lo que NUNCA se recorta:**

- **La pausa.** Si te la comés, la segunda mitad se atropella y la gente se va con
  cara de haber sufrido. Diez minutos, cronometrados.
- **La apuesta de la slide 13.** Sin la predicción fallida, la viz 2 es un dibujito
  lindo. Si no tenés tiempo para las dos, hacé la apuesta y mostrá la viz treinta
  segundos.
- **El desafío 3 del zoo** (slide 25). Es el gancho de la clase 2. Si lo salteás, la
  clase que viene arranca sin motor.
- **El `[EN TU INVESTIGACIÓN]`** (slide 30). Es lo único que se llevan puesto.

---

## 6. Si vas adelantado

- Abrí `viz/maquina-de-perillas.html` **sola, a pantalla completa**, y hacé la
  ronda de «díganme dos números y los pongo». Sale una competencia sola.
- En la slide 4, cambiá el léxico en vivo: abrí `datos/preparar_corpus.py`, mostrá
  las 24 palabras de `LEXICO["seguridad"]`, y preguntá al aula cuál sacarían y cuál
  agregarían. Es cinco minutos de oro y siembra la clase 10 entera. Si nadie lo ve,
  preguntá: «¿y "seguridad social"?». Esa sola palabra ambigua pesa más que «policía»
  (ver §8).
- En el zoo, poné el modo libre y pedí que **describan una serie de su propia
  investigación** eligiendo una de las seis formas. Que digan por qué.
- Mostrá la serie de otro tema (`educacion`, `trabajo`, `salud`) en el notebook y
  preguntá cuál tiene la tendencia más clara. Ojo: los números de la slide están
  medidos sólo para `seguridad` e `inflacion`.

---

## 7. Los chistes y las analogías que funcionan

- **El ecualizador de audio.** Cinco perillas, un sonido. Nadie sabe la fórmula del
  ecualizador y todo el mundo lo usa bien. *Se puede tener criterio sobre un sistema
  sin conocer su interior* — y ese es el objetivo del curso entero. Úsala en la
  slide 7.
- **«Te la puedo dibujar por teléfono.»** En la slide 7: «si me decís esos dos
  números por teléfono, yo dibujo exactamente esta recta en mi casa sin haber visto
  nunca los datos». Es la definición operativa de parámetro y se acuerdan mejor que
  de cualquier definición formal.
- **La receta y el plato.** La receta (la función) es la misma; las cantidades
  (los parámetros) definen el resultado; los ingredientes de hoy (las variables)
  cambian cada día.
- **«Dos perillas contra miles de millones.»** En la slide 29, con las manos. «Ustedes
  acaban de hacer a mano, en diez minutos, el corazón de lo que hace GPT: mover perillas
  para bajar un número. Encima hay un salto de tamaño enorme, una idea sobre cómo elegir
  la dirección y una arquitectura particular. Pero no hay magia escondida.»
- **El error rojo.** «El error rojo no es un reto, es información.» Repetila cada
  vez que alguien levante la mano asustado.
- **La lista de 24 palabras escrita un martes.** Funciona porque es humilde y es
  verdad: «entre el concepto "cuánto le importa la seguridad a este gobierno" y este
  número hay una lista de palabras que escribió una persona un martes».

**Lo que NO funciona y conviene evitar:**

- «No se asusten.» **Nunca se anuncia el susto.** Si alguien no estaba asustado,
  ahora sí.
- «Esto es facilísimo.» A quien no le sale, la pasa peor.
- La analogía del cerebro. Hoy no hace falta y en la clase 2 hay que desarmarla.
  Evitá plantarla.
- Nombrar la derivada. **Hoy esa palabra no se pronuncia.** Si alguien la dice,
  contestá: «sí, exactamente, y en la clase 3 le vamos a poner ese nombre».

---

## 8. Si te preguntan X

### «Pero esto es una regresión lineal de toda la vida. ¿Dónde está el deep learning?»

La pregunta correcta, y la va a hacer quien más sabe. Respuesta honesta: **sí, es
exactamente eso**, y a propósito. Lo que cambia en las nueve clases que vienen no es
el procedimiento —elegir una familia de figuras y buscar los parámetros que mejor
ajustan— sino **de qué familia estamos hablando**. En la clase 2 la familia pasa a
tener miles de miembros y a poder dibujar cualquier cosa; en la 8, un millón y medio
de perillas. El procedimiento es el mismo desde hoy hasta el final. Si eso te suena
decepcionante, es una buena señal: quiere decir que entendiste.

### «¿Y cómo sé si mi modelo está bien? El número bajó, ¿alcanza?»

No, y hoy no lo podemos contestar del todo. Lo que sí se puede decir ya: **el
desajuste te dice qué tan cerca pasa tu recta de estos puntos, y nada más**. No te
dice si va a pasar cerca de los puntos del año que viene (eso es la clase 4), ni si
la relación es causal (eso no lo contesta ningún modelo de este curso), ni si tu
medida mide lo que decís que mide (eso es la clase 10). Decilo así, con las tres
cosas separadas: la gente se queda tranquila cuando entiende que hay un plan.

### «¿Esto sirve para predecir el futuro?»

Con una serie de 36 puntos y dos parámetros, no. Y conviene decirlo fuerte hoy para
que no haya que desdecirse después. Lo que sí hace un modelo así es **resumir**: te
da una afirmación compacta y discutible («entre 1984 y 2019 subió, poquito y con
mucho ruido») en lugar de 36 números sueltos. Predecir es otro problema, necesita
otros supuestos, y la clase 4 se ocupa de por qué es tan fácil engañarse ahí.

### «¿Por qué elevar los errores al cuadrado y no tomar el valor absoluto?»

Excelente pregunta y **es metodológica, no técnica**. Elevar al cuadrado hace que un
error grande pese muchísimo más que varios chicos: estás decidiendo que fallar feo
en 1998 es peor que fallar poquito en diez años. El valor absoluto (MAE) los trata
igual. **Las dos opciones son defendibles y dan modelos distintos.** En la clase 3
hay una visualización dedicada a esto, con un caso atípico que se arrastra a la
recta. Anotala como pregunta abierta: se cobra en la clase 3.

### «El “% de palabras dedicadas a seguridad”, ¿mide de verdad la prioridad del gobierno?»

**No necesariamente, y esta es la conversación que cierra el curso.** Al menos cuatro
razones para dudar: (1) hablar mucho de algo puede ser **reacción** a la agenda
mediática y no prioridad propia; (2) un gobierno puede **actuar mucho y hablar poco**,
o al revés; (3) el discurso de apertura es un **género** con reglas propias, no un
volcado de prioridades; (4) el largo de los discursos cambió por un factor de nueve,
y aunque normalizamos por palabras, eso cambia qué cabe adentro. Y encima está la
lista de 24 palabras, que la escribimos nosotros, con un problema adentro: (5) la palabra
«seguridad» aporta 228 de los 461 aciertos del léxico, y al menos 64 de esas 228 son
«seguridad social» (44), «jurídica» (10), «alimentaria» (7) o «vial» (3). Alrededor del
14 % de la serie mide jubilaciones, contratos, comida o tránsito, no delito
(`medir-referencias.py`, sección 5). **Esto no invalida la medida: la
vuelve discutible, que es distinto.** El trabajo es escribir en el paper la frase
correcta: no «cuánto le importaba la seguridad» sino «cuánto espacio le dio la
Presidencia al léxico de seguridad en el mensaje anual al Congreso».

### «¿El peso muestral no es un parámetro?»

No: es una **variable**. Cada encuestado tiene su propio peso y vive en una columna de la
base. La regla del dedo lo resuelve sola. Lo que es igual para toda la muestra es el
procedimiento que calculó los pesos: como el 0,05, es un parámetro **del procedimiento**,
no del modelo (ver §3, minuto 21). Es una confusión buena: dejá que el aula la resuelva
con la regla.

### «¿Los discursos son todos iguales? ¿Misma fecha, todo parejo?»

No del todo, y conviene saberlo antes de que lo pregunten. (1) Hasta 1994 las sesiones
se abrían el **1 de mayo**; desde la reforma de 1994, el **1 de marzo**: 11 de los 36
puntos son de mayo. (2) En el corpus fuente, **el discurso de 2006 es una copia del de
2005** (mismas 18.234 palabras, mismo 0,1645 %): la serie tiene 36 puntos pero 35
discursos distintos. En la clase 1 lo dejamos a la vista y no lo sacamos; en la clase 4
vuelve como ejemplo de fuga. Los detalles están en `datos/README.md` §1.1.

### Bonus, por si aparece: «¿me tengo que aprender Python?»

No para este curso. Tenés que poder **leer** código y **cambiar números**. Escribir
código desde cero no es requisito de ninguna de las diez clases. Si querés afianzar
la sintaxis por tu cuenta, en `referencias.md` está py4e en castellano.

---

## 9. Checklist de cinco minutos antes de entrar

- [ ] `slides.html` abierto y probado **en el proyector** (1280×720 como mínimo).
- [ ] Las tres viz abiertas en pestañas aparte, por si querés proyectarlas solas.
- [ ] El notebook corrido de punta a punta una vez, hoy, en la máquina que vas a usar.
- [ ] El link del notebook escrito en el pizarrón **antes** de empezar.
- [ ] Un temporizador para la pausa. En serio.
- [ ] Los números de la clase, a mano: piso de la recta **0.0146**, raya horizontal
      **0.0165**, arranque de la viz **0.0368**, inflación (suavizada) mejor recta
      **0.00156** contra raya horizontal **0.00157**. Si ves otros, corré
      `medir-referencias.py`: lo más probable es que hayan cambiado los datos.
- [ ] Saber que si algo del HTML no anda, `_shared/plantillas/demo.html` te dice si
      el problema es de la biblioteca o tuyo.
