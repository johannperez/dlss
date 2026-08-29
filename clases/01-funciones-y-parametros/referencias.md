# Clase 1 — Para seguir

**Una función es una máquina con perillas**

Nada de esto es obligatorio. Está ordenado por **para qué te sirve**, no por
importancia académica.

## Cómo leer las marcas

| Marca | Qué quiere decir |
|---|---|
| `[VERIFICADA]` | Se abrió la URL desde este entorno y respondió. Se anota con qué. |
| `[VERIFICAR URL]` | La obra existe y está bien citada, **pero nadie pudo chequear el enlace**. |
| `[VERIFICAR]` | Falta chequear algún dato de la cita (año, revista, número de página). |

> **Por qué hay tantas marcas pendientes.** El contenedor donde se construyó este
> repositorio sólo llega a `pypi.org`, `files.pythonhosted.org`,
> `registry.npmjs.org` y `raw.githubusercontent.com`. No se puede abrir `arxiv.org`,
> `doi.org`, YouTube, Wikipedia ni las páginas HTML de GitHub. **Poner una URL sin
> haberla abierto sería inventarla**, y este es un curso sobre no inventar. Así que
> las citas están completas y los enlaces quedan marcados para que alguien con red
> los complete. La lista consolidada del curso está en `recursos/bibliografia.md`.

---

## Si te quedaste con ganas

*(Cosas cortas, en castellano cuando se puede, para hacer esta semana.)*

**1. 3Blue1Brown, *Essence of Calculus*, capítulo 1.** `[VERIFICAR URL]`
Veinte minutos de animación sobre qué es una función y qué significa que cambie.
**Por qué te conviene:** es exactamente la intuición visual de la clase de hoy,
contada por alguien que dibuja mejor que nosotros. Tiene subtítulos en español.
**En qué orden:** primero esto, antes que cualquier otra cosa de la lista.

**2. Severance, C., *Python para todos* (py4e), capítulos 1 a 4.** `[VERIFICAR URL]`
El repositorio del proyecto responde: `raw.githubusercontent.com/csev/py4e`
`[VERIFICADA — el README del repo devolvió 200 desde este entorno]`. La versión en
castellano del libro está publicada en el sitio del proyecto, cuya URL **no se pudo
verificar acá**.
**Por qué te conviene:** si te trabaste con la sintaxis del `def` y sentiste que el
problema era vos, no lo era. Estos cuatro capítulos cubren exactamente lo que hace
falta para los diez notebooks del curso, y nada más.
**En qué orden:** sólo si el notebook te costó. Si lo pudiste seguir, saltealo: no
hace falta saber Python para este curso, hace falta poder leerlo y cambiar números.

**3. 3Blue1Brown, *But what is a neural network?*** `[VERIFICAR URL]`
**Por qué te conviene:** porque te va a dar ganas de seguir.
**En qué orden: mirálo después de la clase 2, no ahora.** Lo anunciamos hoy para los
ansiosos, pero si lo ves antes de haber visto la composición de funciones vas a
entender la mitad y te vas a frustrar. Está la semana que viene igual.

**4. La documentación de tus propios datos.** Sin URL, porque es tuya.
**Por qué te conviene:** el `[EL LUNES]` de hoy es graficar una serie tuya. Antes de
hacerlo, andá a buscar cómo se construyó esa variable: quién la midió, con qué
instrumento, qué decisiones se tomaron. Es media hora y te va a servir más que
cualquier video.

---

## Si te vas a meter en serio

*(Lecturas de fondo. Ninguna es para esta semana.)*

**5. Breiman, L. (2001), *Statistical Modeling: The Two Cultures*, Statistical
Science 16(3), 199-231.** `[VERIFICAR URL]`
**Por qué te conviene:** es el paper que fundamenta la slide de «los dos caminos».
Breiman distingue la cultura del **modelo de datos** (elijo una fórmula que creo que
describe el proceso y estimo sus parámetros) de la cultura del **modelo algorítmico**
(no me pronuncio sobre el proceso, busco una función que prediga bien). Todo este
curso vive en la segunda, y el precio que se paga por vivir ahí está explicado en
este texto mejor que en ningún otro lugar.
**En qué orden:** después de la clase 4, cuando ya te haya dolido la diferencia entre
ajustar y predecir. Se lee en una tarde y no tiene una sola fórmula difícil.

**6. Molina, M. & Garip, F. (2019), *Machine Learning for Sociology*, Annual Review
of Sociology 45, 27-45.** `[VERIFICAR]`
**Por qué te conviene:** es un panorama del campo escrito para **exactamente** esta
audiencia: gente que investiga sociedad y quiere saber qué le sirve de todo esto.
Contesta la pregunta «¿y esto para qué me sirve a mí?» con casos concretos.
**En qué orden:** cuando quieras convencer a alguien de tu equipo de que esto no es
una moda. También sirve para escribir la justificación metodológica de un proyecto.

**7. Grimmer, J., Roberts, M. & Stewart, B. (2022), *Text as Data: A New Framework
for Machine Learning and the Social Sciences*, Princeton University Press.**
`[VERIFICAR]`
**Por qué te conviene:** es el libro de cabecera del curso entero. Para la clase 1
alcanza con el capítulo introductorio y, sobre todo, con la discusión sobre
**medición y validez**: la pregunta de si el «% de palabras dedicadas a seguridad»
mide la prioridad del gobierno es literalmente el problema que ese capítulo plantea.
**En qué orden:** el capítulo 1 ahora si tenés tiempo; el resto acompaña las clases
6, 9 y 10.

**8. Jacobs, A. Z. & Wallach, H. (2021), *Measurement and Fairness*, FAccT '21.**
`[VERIFICAR]`
**Por qué te conviene:** pone nombre técnico a lo incómodo de hoy. Entre el
constructo que querés medir («prioridad del gobierno») y el número que sale
(«0,44 % de palabras») hay una cadena de decisiones, y cada eslabón puede romperse.
El artículo da un vocabulario para discutir eso que se puede usar tal cual en la
sección de métodos de un paper.
**En qué orden:** después de la clase 10, o antes si vas a escribir metodología esta
semana.

---

## Los datos de esta clase

**Discursos presidenciales de apertura de sesiones (Argentina, 1854-2019).**
Recopilación y digitalización de **Lucas Ariel**, repositorio
`lucariel/discursos_presidenciales` en GitHub.
`[VERIFICADA — el README del repositorio se descargó desde raw.githubusercontent.com]`
Inspirado en Bercholc & Bercholc (2012), *Los discursos presidenciales en la
Argentina democrática*. `[VERIFICAR]`

Los textos fuente son actos oficiales del Estado argentino. **La recopilación no
declara licencia**: se usa acá con fines educativos y se cita. Si el curso se
publica, hay que escribirle al autor. Los detalles, las trampas y las cinco series
derivadas están en `datos/README.md`, sección 1.1.

**El léxico de 23 palabras** con el que se construyó la serie de «seguridad» está
en `datos/preparar_corpus.py`, en el diccionario `LEXICO`. **Está a la vista a
propósito.** Cambialo y mirá cómo se mueve la conclusión: es el ejercicio más barato
y más honesto de todo el curso.

**Los números de referencia** que aparecen en las slides y en las visualizaciones
(el piso de la recta, los techos de cada forma del zoo) están medidos por
`medir-referencias.py`, en esta misma carpeta. Corrélo si tocás algo.

---

## Lo que queda prometido para las próximas clases

| Se abrió hoy | Se paga en |
|---|---|
| El número de «desajuste» sin nombre técnico | clase 3 (*loss*) |
| «Mover una perilla por vez» como estrategia | clase 3 (descenso por coordenadas y por gradiente) |
| La línea que pasa por todos los puntos (slide 6) | clase 4 (sobreajuste) |
| Ninguna forma sola puede con el desafío 3 | clase 2 (composición y suma de rampas) |
| La sigmoide y su techo | clases 2, 3 y 9 |
| «¿La medida mide lo que dice medir?» | clase 10 (validez de constructo) |
