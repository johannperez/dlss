# Notas para quien da la clase 10

**Criterio: validez, sesgo, reproducibilidad y el revisor 2** · 120 minutos · 40 slides

> Esta es la clase que justifica el curso. Todo lo anterior existe para que hoy se pueda
> discutir validez con autoridad: no se puede sospechar de un modelo que no se entiende.
> Si algo hay que dar bien, es esto.

---

## 1. El arco narrativo, en diez líneas

1. Mostramos un clasificador que **anda**: accuracy 0,83, F1 0,68, le gana al piso por 0,11.
2. Preguntamos al aula si tiene objeciones. No las tiene. **Esto se publica.**
3. Miramos qué usa: **seis de los veinte** términos que más pesan son **nombres propios
   mexicanos de 2018-2021**. Uno de cada tres.
4. Se lo aplicamos a discursos presidenciales argentinos, que son 100 % política: encuentra el **21 %**.
5. Y decimos la frase incómoda: **el modelo no falló**. Falló la etiqueta que le colgamos.
6. Nombramos la distinción: **desempeño** (¿acierta?) contra **validez** (¿mide lo que digo?).
7. Y devolvemos el terreno: validez de constructo es de ellos, tiene 70 años, y acá tienen ventaja.
8. Damos los cinco procedimientos, más el que nadie hace: **medir la banda de ruido primero**.
9. Auditamos sesgo con un procedimiento, no con una opinión, y aprendemos que **ceguera no es equidad**.
10. Cerramos con lo accionable: reproducibilidad, ética con casos, el juicio, cuándo **no** usar
    esto, y el checklist que se llevan.

**La frase que organiza todo:** *un modelo siempre dibuja algo; tu trabajo es demostrar qué.*

---

## 2. El plan de 120 minutos

**Esta tabla suma 120 exactos y es la que hay que llevar al aula.** Los minutos que están
acá son los mismos que figuran arriba de cada `<aside class="notes">` en `slides.html`: si
tocás uno, tocá el otro.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| **0-10** | **Gancho** | 1-6 | Portada (1), el puente desde la clase 9 (2), el panel de métricas y *«¿alguien tiene una objeción?»* (3), los dos pliegues (4-5), «el modelo no falló» (6). |
| **10-30** | **Validez** | 7-18 | Desempeño ≠ validez (7), ustedes tienen ventaja (8), el abismo (9), **VIZ 1, 5 min** (10), contenido y externa (11), los cinco procedimientos (12), uno por uno (13-17), **la banda de ruido** (18). |
| **30-38** | **Sesgo** | 19-22 | Los tres sesgos (20), **VIZ 2, 4 min** (21), ceguera no es equidad (22). |
| **38-39** | Consignas del práctico 1 | 23 | |
| **39-59** | **MANOS 1 · la auditoría** | — | Notebook, secciones 1 a 9, de a dos. **20 minutos.** |
| **59-69** | **PAUSA** | 24 | **No negociable.** |
| **69-71** | El sesgo como hallazgo | 25 | Antídoto contra la sobrecorrección. |
| **71-76** | Reproducibilidad | 26-28 | El checklist (27) y los modelos cerrados (28). |
| **76-85** | Ética aplicada | 29-30 | Los cuatro casos (7 min) y las cinco preguntas (2). |
| **85-105** | **MANOS 2 · el juicio** | 31-32 | **12 de preparación + 8 de audiencia**, con los papers de `material-el-juicio.md`. El veredicto (32) se arma durante la audiencia. |
| **105-108** | Cuándo NO usar deep learning | 33 | La slide más honesta. |
| **108-111** | **VIZ 3 · el checklist** | 34 | En vivo, en el proyector. |
| **111-113** | Las seis objeciones | 35 | La versión que se memoriza. |
| **113-115** | El mapa del curso | 36 | Las diez clases, una frase cada una. |
| **115-116** | Glosario | 37 | Rápido: señalá dos términos y seguí. |
| **116-118** | Qué te llevás | 38 | Tres ideas y el bloque del lunes. |
| **118-119** | Adónde seguir | 39 | |
| **119-120** | Cierre | 40 | La frase sola en la pantalla. |

> **De dónde salen los recortes.** El mazo dado sin apuro, con la VIZ 1 recorrida entera, los
> cinco procedimientos uno por uno y el juicio de 25 minutos, son **unos 150 minutos**: hay
> media hora de más y **ya está descontada en la tabla de arriba**. Lo que se sacrificó, en
> este orden: la VIZ 1 de 8 a 5 minutos, los procedimientos 13 a 17 a un minuto cada uno
> (están enteros en la lista de la slide 12), el práctico 1 de 30 a 20, el juicio de 25 a 20,
> y los casos de ética de 11 a 7. **Si el aula es chica y vas holgado**, lo primero que
> conviene devolver es el juicio a 25 minutos; lo segundo, la VIZ 1.
>
> El presupuesto oficial de `PROGRAMA.md` es 10 gancho + 20 validez + 20 manos 1 + 10 pausa +
> 15 repro/ética + 25 el juicio + 15 caja de herramientas + 5 cierre. La tabla de arriba lo
> respeta bloque por bloque, salvo que corre la pausa nueve minutos más tarde (queda igual en
> el medio de la clase) y le devuelve esos minutos al bloque de sesgo, que en el guion
> original vivía adentro del práctico.

## 3. Qué preguntar al aula, y cuándo

| Momento | La pregunta | Qué hacer con lo que digan |
|---|---|---|
| Slide 3 | **«¿Alguien tiene una objeción? Esto se publica.»** | Van a preguntar por el piso, por la partición, por el n. Todo está contestado. Ese es el punto: **con ese panel adelante, un revisor razonable lo aprueba.** No pases de slide hasta que alguien diga «se ve bien». |
| Slide 4 | «¿Esto es una señal del concepto o es una guía telefónica?» | No des vos la conclusión. Esperá. Alguien la dice. |
| Slide 9 | «¿Cómo demostrarían que una escala de anomia mide anomia?» | Lo que contesten **son** los cinco procedimientos que vienen. Anotalos en el pizarrón y después mostrá la coincidencia: es el momento en que se dan cuenta de que ya sabían. |
| VIZ 1, caso 2 | «¿Cómo lo arreglarían?» | Van a proponer cosas razonables (partir por año, entrenar en un período). Mostrá que ninguna funciona con esos datos. **Que el arreglo no exista es la lección.** |
| Slide 14 | Leé los cinco falsos positivos y preguntá caso por caso, a mano alzada: «¿esto es política?» | Se van a partir en el titular de Biden y en el de las abuelas. Ahí decís: «su F1 está midiendo el desacuerdo entre ustedes y quien codificó el corpus». |
| Slide 18 | «¿Cuántos papers vieron que reporten un F1 con intervalo?» | Silencio. El silencio es el argumento. |
| Slide 20 | «Denme un ejemplo de cada uno de los tres sesgos, de su campo.» | El del mundo es fácil, el introducido es el que cuesta. Si nadie lo encuentra, dales el umbral. |
| Slide 22 | «Si les muestro una tabla donde todos los grupos sacan el mismo puntaje, ¿qué concluyen?» | La respuesta ingenua es «no hay sesgo». La correcta es «fijate si el modelo conoce esas palabras». |
| Slide 29 | Una mano a favor y una en contra por caso. | El desacuerdo real es la demostración de que la ética no es un trámite. |

---

## 4. Confusiones de principiante, y cómo desarmarlas

**1. «Buena métrica = buena medida.»**
Es la confusión que organiza la clase entera. Frase para desarmarla:
*«la métrica te dice que el modelo reproduce tus etiquetas; no te dice nada sobre si tus
etiquetas miden tu concepto».* Repetila dos veces en la clase, con diez minutos de distancia.

**2. «Entonces hay que usar un modelo mejor.»**
Aparece siempre después del gancho, y es la reacción natural. Respuesta:
*un transformer entrenado sobre el mismo corpus con las mismas etiquetas aprendería el mismo
atajo, más rápido y con un F1 más alto.* **Un modelo mejor empeora este problema**, porque
encuentra el atajo antes. Es contraintuitivo y hay que decirlo despacio.

**3. «El modelo es objetivo porque es matemático.»**
Enumerá las cinco decisiones humanas, con los dedos: qué datos, qué etiquetas, qué función de
pérdida, qué umbral, qué se reporta. **La objetividad no está en el método: está en la
explicitación.** Aparece tanto del lado del entusiasmo como del de la crítica, y a los dos
se les contesta lo mismo.

**4. «El sesgo se arregla balanceando los datos.»**
Slide 20. Balancear ataca el sesgo **del corpus**. No toca el del mundo ni el introducido.
Y encima puede distorsionar la estimación de prevalencia, que muchas veces era el objetivo.

**5. Confundir interpretabilidad con validez.**
«Uso un modelo simple, entonces es válido.» **No.** El clasificador de hoy es perfectamente
interpretable y perfectamente inválido para la afirmación que le colgamos. La
interpretabilidad **ayuda a detectar** el problema; no lo previene. Es el motivo por el que
el notebook usa una regresión logística y no un transformer.

**6. Creer que la validación es un paso final.**
La dejan para el final y no llegan. Consejo operativo, dicho con esas palabras:
**la muestra a etiquetar, los casos límite y el test de placebo se diseñan junto con el
proyecto, no después de entrenar.** Si no sabés cómo vas a validar, todavía no empezaste.

**7. «Reproducible = el código está en GitHub.»**
Sin la semilla, las versiones y los datos (o su procedencia exacta), ese código no reproduce
nada. Se demuestra solo con el `TODO 7` del notebook.

**8. La sobrecorrección: «entonces esto no sirve para nada».**
Es el fracaso pedagógico típico del final de un curso crítico, y es tan malo como el
entusiasmo acrítico. Se ataca en dos lugares: la slide 25 (el mismo instrumento que es
dañino para decidir es valioso para medir) y la slide 33, que es **corta y precisa**, no
total. Si el aula termina paralizada, la clase salió mal.

---

## 5. Si vas atrasado (y vas a ir atrasado)

El plan de la sección 2 ya viene ajustado a 120. Si **igual** te atrasás —y te vas a
atrasar— esto es lo que se recorta, **en este orden**:

1. **Slides 13 y 17** (la muestra a mano y la validación externa). Están en la lista numerada
   de la slide 12; se mencionan en veinte segundos desde ahí. **Ganás 2 minutos.**
2. **Slide 11** (contenido y externa). Una frase: «lo mismo que saben de muestreo».
   **1 minuto.**
3. **Slide 25** (el sesgo como hallazgo). Duele, pero se puede decir en una oración mientras
   se pasa. **2 minutos.**
4. **VIZ 1, caso 3.** Los casos 1 y 2 tienen datos reales; el 3 es construido. Si hay que
   cortar algo de la viz, cortá el 3. **1 minuto.**
5. **El juicio de 20 a 15 minutos**: 10 de preparación, 5 de audiencia. Se sostiene, apretado.
   **5 minutos.**
6. **Slide 39** (adónde seguir). Está todo en `referencias.md`. **1 minuto.**

Los seis juntos son **12 minutos**: alcanzan para absorber un arranque tarde o una discusión
que se fue de tiempo, sin tocar nada de la lista de abajo.

**Lo que NUNCA se recorta, aunque haya que terminar cinco minutos tarde:**

- **La pausa.** Es la última clase y hay tentación de comérsela. No.
- **El gancho completo (slides 3-6).** Sin los dos pliegues y el «el modelo no falló», el
  resto de la clase no tiene por qué existir.
- **La slide 12** (los cinco procedimientos). Es lo que se llevan escrito.
- **La slide 33** (cuándo NO usar deep learning). Es la que más credibilidad da al curso entero.
- **El cierre (slide 40).** Diez segundos, y es el final de diez clases.

**Si vas adelantado** (raro, pero pasa si el aula es chica):

- **Devolvé el juicio a 25 minutos** (15 de preparación + 10 de audiencia); si sobra más,
  hacé **dos rondas** invirtiendo los roles. Es lo más formativo de la clase.
- **Devolvé la VIZ 1 a 8 minutos** y recorré el caso 2 sin apuro: es el más difícil y el más
  valioso.
- Abrí la VIZ 3 y completala en vivo **para el proyecto de alguien del aula**. Pedí un
  voluntario. Es incómodo y es exactamente por eso que enseña.
- En la VIZ 2, escribí una plantilla del campo de ellos y probala.
- Volvé al caso 3 de la slide 29 (el clasificador de riesgo) y desarrollá el *feedback*
  invisible con un ejemplo concreto del Estado local.

---

## 6. Chistes y analogías que funcionan

- **«El revisor 2».** Es el dispositivo pedagógico de toda la clase y funciona en cualquier
  aula con posgrado. Hay que escribir para el lector más desconfiado. El chiste organiza el
  método: anticipar sus seis objeciones.
- **El termómetro y el país que hace calor.** Un termómetro mal calibrado y un país que
  realmente hace calor son dos problemas distintos. Confundirlos produce tanto negación
  («es sólo el reflejo de la realidad») como magia («arreglemos el modelo y arreglamos el
  mundo»). Es la mejor entrada a los tres sesgos.
- **El clasificador como escala de actitudes.** Nadie publicaría una escala sin reportar su
  alfa; nadie debería publicar un clasificador sin su matriz de confusión sobre una muestra
  validada. Devuelve el problema a un terreno que ellos manejan.
- **«La guía telefónica».** Para los nombres propios del top 20. Se entiende al toque.
- **«Es una bolsa de palabras: no lee, cuenta.»** Explica de una vez la negación que no mueve
  el puntaje y el barajado que da predicciones idénticas.
- **«Ausencia no es neutralidad.»** Para la slide 22. Es la frase que más se repite después,
  según la experiencia.
- El chiste malo de la slide 18 («y ahora el chiste malo») funciona porque es verdad: el test
  que recomienda toda la literatura se mueve menos que el ruido. Decilo con cara de póker.

---

## 7. Si te preguntan X — las cinco preguntas difíciles

**«Si con una regresión logística ya se ve el problema, ¿para qué hicimos nueve clases de
deep learning?»**
Es la pregunta más justa de la clase y hay que agradecerla. Respuesta honesta: por dos
razones. Primera, **no se puede auditar lo que no se entiende**: para saber qué mirarle a un
transformer hay que saber qué hace un transformer, y eso es la clase 7. Segunda, hoy usamos un
modelo interpretable **a propósito**, porque la interpretabilidad es una razón legítima para
elegir un modelo más simple — y esa decisión sólo la podés tomar con criterio si conocés las
dos opciones. El curso no es para que usen deep learning: es para que **decidan** si usarlo.

**«¿Cuántos casos hay que leer a mano? Dame un número.»**
No hay un número universal y quien te lo dé te está vendiendo algo. El rango de trabajo es
**100 a 200** para una estimación estable de precisión y recall en una tarea binaria con
prevalencia no muy baja. Con 50 podés detectar un desastre, no medir. Con prevalencia del 5 %
necesitás muchos más **positivos**, y por eso se muestrea estratificado por la predicción del
modelo y no al azar puro. Y hay una respuesta empírica en la literatura: Barberá et al. (2021)
lo miden. Lo importante es reportar el número, sea cual sea.

**«Todo esto es carísimo. En mi proyecto no hay presupuesto para nada de esto.»**
Entonces la conclusión correcta puede ser **no usar el modelo**, y eso es un resultado
profesional, no un fracaso. Pero antes de llegar ahí: los cinco procedimientos no cuestan lo
mismo. El control positivo y tres pares mínimos son **veinte minutos** y ya te dan una
afirmación defendible. La muestra leída a mano son dos tardes. La validación externa depende
de si existe la medida. Ordenalos por costo y hacé los baratos primero: si el modelo no
sobrevive el control positivo, te ahorraste las dos tardes.

**«¿No es todo esto relativismo? Si ninguna medida es perfecta, ¿cualquier cosa vale igual?»**
No, y es importante contestarlo con firmeza porque si no la clase deja un mal sabor. Que
ninguna medida sea perfecta **no** implica que todas sean iguales: una medida cuyos límites
están medidos y declarados es estrictamente mejor que una cuyos límites no se conocen. La
diferencia entre las dos no es filosófica, es empírica y se ve en la tabla. El objetivo no es
la certeza: es **saber de qué tamaño es tu incertidumbre**. Eso es exactamente lo que hacen
ustedes cuando reportan un intervalo de confianza, y nadie llama a eso relativismo.

**«¿Y si el modelo lo entrenó otro y yo sólo lo aplico? ¿Igual soy responsable?»**
Sí, y más. Cuando aplicás un modelo ajeno a tu corpus estás haciendo dos afirmaciones: que el
modelo mide lo que su ficha dice, **y** que eso sigue valiendo en tu dominio. La segunda es
tuya y nadie más la puede sostener. La regla práctica: **la validación se hace siempre en el
corpus de destino**, no en el de origen. El control positivo de hoy es exactamente eso, y
tomó cuatro líneas de código. Si el modelo no viene con ficha, escribí vos la que puedas y
declará lo que no sabés: «el modelo no documenta con qué datos se entrenó» es una limitación
publicable y a veces un hallazgo.

---

## 8. Cosas de producción, para el día

- **Los dos papers del juicio ya están escritos**: `material-el-juicio.md`, en esta misma
  carpeta. El **A** («índice de conflictividad en la prensa provincial») es defendible con
  reparos menores; el **B** («populismo con un modelo de lenguaje») tiene un problema fatal
  de validez escondido en una nota al pie. Los dos son **ficticios y están rotulados como
  material didáctico** en la primera línea; no citan datos reales y no se pueden citar.
  **Repartí uno solo por cohorte** y guardá el otro para la vez siguiente. Al final del
  archivo está la clave de corrección, con cada objeción y su gravedad: no la leas en voz
  alta antes de la actividad. Imprimilos: repartir papel es más rápido que compartir un
  archivo, y evita que la mitad del aula se distraiga con la pantalla.
- **La VIZ 3 guarda en `localStorage`.** Si vas a proyectarla en la máquina del aula, apretá
  *Vaciar* antes de empezar: si no, aparece lo que escribió el docente anterior.
- **El notebook corre entero en menos de 20 segundos** en CPU y sin red (medido con
  `nbconvert --execute`, cuatro corridas: **entre 14 y 19 s** de punta a punta según cuán
  cargada esté la máquina; el bloque más lento son las 25 particiones de la sección 4, que el
  propio notebook cronometra en **4,2 s**). No hace falta GPU ni Colab pago.
  Si el wifi del aula falla, el notebook anda igual: todos los datos salen de `datos/muestras/`.
- Los números de las slides salen de `medir-clase10.py`, y las figuras de `figuras/` las
  produce `exportar-figuras.py` **corriendo el notebook** (no copiando su código). Si tocás el
  notebook, corré los dos y actualizá las slides. Un número inventado en un curso sobre no
  inventar números es el peor error posible.
- **Dos listas viven duplicadas a propósito y tienen que quedar iguales:** los 18 nombres
  propios de la ablación y los 17 sujetos de la auditoría de sesgo están escritos tanto en
  `notebook.ipynb` como en `medir-clase10.py`. Si cambiás una, cambiá la otra: dos definiciones
  del mismo experimento son exactamente el error que denuncia la slide 27.
- **El ejemplo precargado de la VIZ 3 es la auditoría real de esta clase, agujeros incluidos.**
  Los campos «cuántos casos leíste a mano» y «acuerdo entre codificadores» dicen que no lo
  hicimos, porque no lo hicimos. Si alguien pregunta por qué el ejemplo no está «completo»,
  esa es la respuesta y es la clase entera en una línea.
- Si el aula pregunta por los datos: el corpus de prensa es **real** y CC BY 4.0; los discursos
  presidenciales son **reales** y de dominio público sin licencia declarada; Aguasclaras es
  **sintético** y hay que decirlo cada vez que aparece.
