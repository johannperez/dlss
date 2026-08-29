# Referencias — Clase 10

**Criterio: validez, sesgo, reproducibilidad y el revisor 2**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la red
> bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. `doi.org`, `arxiv.org`, las páginas HTML de GitHub y los
> sitios de las editoriales dan 403 o no responden.
> **Se probó con `curl` cada URL de esta lista el 2026-08-29.** Las que respondieron van
> `[VERIFICADA 2026-08-29]`; el resto va `[VERIFICAR URL]`: **las obras existen y están
> bien citadas** —autor, año, título, publicación— y se encuentran buscando por título,
> pero nadie abrió el enlace, y poner una URL sin haberla abierto sería inventarla.
> Este es un curso sobre no inventar. Quien tenga red, que las complete.

---

## Si te quedaste con ganas

Cinco lecturas, en el orden en que conviene hacerlas.

**1. Grimmer, J. & Stewart, B. (2013). *Text as Data: The Promise and Pitfalls of Automatic
Content Analysis Methods for Political Texts*. Political Analysis 21(3), 267-297.**
`[VERIFICAR URL]`
> **Empezá por acá.** Tiene más de una década y sigue siendo la mejor síntesis de qué se
> puede y qué no se puede afirmar con estas herramientas. Su consigna —*«validate, validate,
> validate»*— es literalmente el título de esta clase. Leelo con el gancho de hoy en la
> cabeza: te da el vocabulario para nombrar lo que le pasó al clasificador de política.
> **Dos horas, y se relee.** Si sólo vas a leer una cosa de esta lista, que sea ésta.

**2. Narayanan, A. & Kapoor, S., *AI Snake Oil* (libro, 2024) y el blog del mismo nombre.**
`[VERIFICAR URL]`
> Lo más legible que hay sobre qué promete y qué no promete la IA, escrito por dos
> investigadores de Princeton para lectores no técnicos. **Leelo después de la clase, no
> antes**: si lo leés antes te llevás el escepticismo sin el mecanismo, y el escepticismo sin
> mecanismo no se puede defender en una discusión. El blog es gratis y los posts sueltos
> funcionan solos. Una semana leyendo de a ratos.

**3. Kapoor, S. & Narayanan, A. (2023). *Leakage and the Reproducibility Crisis in
ML-based Science*. Patterns 4(9).** `[VERIFICAR URL]`
> **La lectura central de esta clase.** Revisan 294 artículos de 17 campos y encuentran fuga
> de datos en casi todos. Es la clase 4 (particiones) y la clase 10 (validez) en un solo
> paper, con la taxonomía de ocho tipos de fuga que conviene tener a mano cuando revisás algo.
> Va después de Grimmer & Stewart porque es más técnico y pega más fuerte si ya tenés el
> marco. **Tres horas, y la taxonomía se fotografía.**

**4. Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B.,
Spitzer, E., Raji, I. D. & Gebru, T. (2019). *Model Cards for Model Reporting*.
FAccT '19, 220-229.** `[VERIFICAR URL]`
> El paper que inventó la ficha del modelo que completaste en el `TODO 8`. Es corto y es
> sobre todo una **plantilla**: lo importante son las secciones, no el argumento. Leelo con
> tu propia ficha al lado y completá lo que te falte. **Cuarenta minutos.**

**5. Salganik, M. (2018). *Bit by Bit: Social Research in the Digital Age*. Princeton
University Press. Disponible online.** `[VERIFICAR URL]`
> Capítulo 6 (ética) y capítulo 2 (observar comportamiento) son los que van con esta clase.
> El capítulo 6 es la mejor discusión de ética de investigación digital escrita para
> cientistas sociales, con casos reales y sin sermón: es el material del que salen los cuatro
> casos de la slide 29. El libro entero está online y en abierto. **Dos capítulos, una tarde
> cada uno.**

---

## Si te vas a meter en serio

**6. Jacobs, A. Z. & Wallach, H. (2021). *Measurement and Fairness*. FAccT '21, 375-385.**
`[VERIFICAR URL]`
> **Es la tesis de esta clase, escrita por gente del campo técnico.** El puente explícito
> entre la teoría de la medición de las ciencias sociales —constructo, operacionalización,
> validez— y la literatura de *fairness* en machine learning. Si vas a discutir con
> ingenieros, este es el paper que te da el terreno común: no tenés que traducir tu
> vocabulario, tenés que mostrarles que el suyo ya existía. **Leelo con Cronbach al lado.**

**7. Cronbach, L. J. & Meehl, P. E. (1955). *Construct Validity in Psychological Tests*.
Psychological Bulletin 52(4), 281-302.** `[VERIFICAR URL]`
> **La fuente.** Setenta años, y vale citarlo en clase justamente para marcar que el problema
> no lo inventó el machine learning. Es más filosófico y más difícil que el resto de esta
> lista, y no hace falta leerlo entero: las primeras diez páginas alcanzan para tener la
> definición de primera mano. Va **después** de Jacobs & Wallach, que funciona como puerta
> de entrada.

**8. Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H. &
Crawford, K. (2021). *Datasheets for Datasets*. Communications of the ACM 64(12), 86-92.**
`[VERIFICAR URL]`
> El hermano de la ficha del modelo, para los **datos**: cómo se recolectaron, quién los
> etiquetó, con qué instrucciones, qué se excluyó. Si trabajás armando corpus —y casi todos
> los proyectos de esta audiencia empiezan armando un corpus— esto es más útil que la ficha
> del modelo. Leelo junto con `datos/README.md` de este curso, que está escrito con esa forma.

**9. Selbst, A. D., boyd, d., Friedler, S. A., Venkatasubramanian, S. & Vertesi, J. (2019).
*Fairness and Abstraction in Sociotechnical Systems*. FAccT '19, 59-68.** `[VERIFICAR URL]`
> Por qué «arreglar el modelo» no arregla el sistema. Las cinco trampas de abstracción que
> describen son exactamente los errores que comete un equipo técnico bien intencionado sin
> nadie de ciencias sociales adentro. **Es el paper que explica por qué te van a contratar.**
> Corto y denso.

**10. Barberá, P., Boydstun, A. E., Linn, S., McMahon, R. & Nagler, J. (2021).
*Automated Text Classification of News Articles: A Practical Guide to Probabilistic Machine
Learning*. Political Analysis 29(1), 19-42.** `[VERIFICAR URL]`
> Ya apareció en la clase 9 y vuelve acá por una razón distinta: tiene la **respuesta
> empírica** a la pregunta «¿cuántos casos hay que etiquetar a mano?», que es la que más se
> hace en esta clase y la que menos respuesta tiene. Andá directo a esa sección.

---

## Herramientas y material del propio curso

**El corpus de prensa que auditamos hoy.**
Gómez-Adorno, H., Posadas-Durán, J. P., Bel-Enguix, G. & Porto-Capetillo, C. (2021).
*Overview of FakeDeS at IberLEF 2021*. Procesamiento del Lenguaje Natural 67, 223-231.
**CC BY 4.0.** Repositorio:
`https://raw.githubusercontent.com/jpposadas/FakeNewsCorpusSpanish/master/README.md`
`[VERIFICADA 2026-08-29]`
> Leé el README del repositorio: la descripción de cómo se recolectó y se etiquetó es
> justamente la información que la clase te enseñó a pedir. Y después mirá `datos/README.md`
> §1.3, donde están medidas las trampas del corpus: la fuente que predice la etiqueta al
> 96 %, las mayúsculas, el largo. **Es el mejor ejercicio de lectura crítica de datos del
> curso, porque los dos textos hablan del mismo corpus con distinto nivel de sospecha.**

**Los discursos presidenciales del control positivo.**
Recopilación de J. M. Diéguez, discursos de Casa Rosada 2015-2024:
`https://raw.githubusercontent.com/jmdieguez/discursos/main/README.md` `[VERIFICADA 2026-08-29]`
· y los discursos de apertura de sesiones recopilados por L. Ariel:
`https://raw.githubusercontent.com/lucariel/discursos_presidenciales/master/README.md`
`[VERIFICADA 2026-08-29]`
> **Sin licencia declarada** en ninguno de los dos. Los textos son actos oficiales del Estado
> argentino y el uso educativo es defendible, pero si vas a publicar algo con ellos,
> escribile a los recopiladores. Que esa frase esté en un `referencias.md` en vez de estar
> escondida también es parte de lo que enseña la clase.

**`medir-clase10.py`** y **`exportar-figuras.py`** — en esta misma carpeta.
> Todos los números de las slides y de las visualizaciones salen del primero, y las cinco
> figuras salen del segundo, que **corre el notebook** en vez de copiarle el código. Los dos
> tardan menos de un minuto. **Es el modelo de lo que tu propio proyecto debería tener**: un archivo que
> reproduce cada número que afirmás, y que se puede correr de nuevo para comprobarlo. Abrilo
> aunque no vayas a modificarlo.

**`scikit-learn`, guía de *model evaluation*.**
`scikit-learn.org/stable/modules/model_evaluation.html` `[VERIFICAR URL]` ·
paquete: `https://pypi.org/project/scikit-learn/` `[VERIFICADA 2026-08-29]`
> Como referencia, mientras escribís tu propio bloque de métricas. Las secciones de
> `precision_recall_fscore_support` y de curvas precisión-recall son las que vas a usar.

---

## Y una cosa que no es una lectura

**Hacé un proyecto chico con tus datos.** Uno que puedas terminar en un mes, con su semilla,
su ficha del modelo y su párrafo de métodos completo. Va a enseñarte más que los diez títulos
de arriba juntos, porque las decisiones difíciles de esta clase —qué es un atajo, cuántos
casos leer, qué reportar— sólo aparecen cuando el corpus es tuyo y la pregunta te importa.

Y cuando lo termines, pasale el checklist de `viz/checklist-revisor.html`. Si lo podés
completar entero, está listo.
