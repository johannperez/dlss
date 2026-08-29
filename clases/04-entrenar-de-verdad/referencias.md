# Referencias — Clase 4

**El ciclo de entrenamiento, y la diferencia entre dibujar y calcar**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la red
> bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. **Se probó con `curl` cada URL de esta lista.** Las dos que
> respondieron van marcadas `[VERIFICADA]`; el resto va marcado `[VERIFICAR URL]`: las obras
> existen, están bien citadas y se pueden buscar por título y autor, pero **nadie abrió el
> enlace**, y poner una URL sin haberla abierto sería inventarla. Éste es un curso sobre no
> inventar. Quien tenga red que las complete y las pase a `[VERIFICADA]` con la fecha.

---

## Si te quedaste con ganas

En el orden en que conviene leerlas.

**1. Yarkoni, T. & Westfall, J. (2017). *Choosing Prediction Over Explanation in Psychology:
Lessons From Machine Learning*. Perspectives on Psychological Science, 12(6), 1100-1122.**
`[VERIFICAR URL]` · DOI: 10.1177/1745691617693393
> **Si vas a leer una sola cosa de esta clase, es ésta.** Traduce toda la clase de hoy al
> vocabulario de las ciencias sociales, sin una línea de código: por qué un modelo que explica
> perfecto tus datos puede no predecir nada, por qué la validación cruzada es una idea
> metodológica y no un truco computacional, y por qué la distinción explicar/predecir cambia
> qué tenés derecho a afirmar. La sección sobre *overfitting* es literalmente la segunda mitad
> de hoy, escrita para psicólogos.
> *Empezá por acá.* Una hora, y se lee sin sufrir.

**2. Documentación oficial de PyTorch — tutorial *Learn the Basics*.** `[VERIFICAR URL]`
> Sólo **dos secciones**: *Tensors* y *Optimizing Model Parameters*. Esa segunda es el mismo
> loop de cinco líneas que escribimos hoy, explicado por sus autores. **El resto del tutorial
> es para después** (dataloaders, transformaciones, guardar modelos): si lo abrís entero te va
> a parecer que te falta muchísimo, y no es cierto. Buscalo como
> "PyTorch tutorials — Learn the Basics".
> 40 minutos, las dos secciones.

**3. StatQuest (Josh Starmer) — videos sobre *bias/variance tradeoff* y *cross validation*.**
`[VERIFICAR URL]`
> Explicaciones cortas, con dibujos hechos a mano y música tonta. El de *bias and variance*
> es exactamente el botón «otra muestra» de nuestra viz, contado en cinco minutos: por qué un
> modelo demasiado flexible cambia salvajemente de muestra a muestra. El de *cross validation*
> es la respuesta a la pregunta que vas a tener cuando te des cuenta de que tu n es chico.
> Están en inglés con subtítulos automáticos.
> 15 minutos los dos.

**4. Grimmer, J., Roberts, M. E. & Stewart, B. M. (2022). *Text as Data: A New Framework for
Machine Learning and the Social Sciences*. Princeton University Press.** `[VERIFICAR]`
> **El libro de cabecera del curso.** Para hoy: la parte sobre **validación** y sobre la
> distinción entre descubrimiento, medición y predicción. Su tesis —que ninguna medición
> automática vale sin validación humana— es la clase 10, pero el andamiaje empieza acá.
> El capítulo sobre predicción, dos horas.

---

## Si te vas a meter en serio

**5. Kapoor, S. & Narayanan, A. (2023). *Leakage and the Reproducibility Crisis in ML-based
Science*. Patterns, 4(9), 100804.** `[VERIFICAR]` · DOI: 10.1016/j.patter.2023.100804
> **La referencia de las slides 33-35 y de media clase 10.** Los autores revisaron cientos de
> papers de ciencia aplicada (medicina, ciencia política, sociología computacional) y armaron
> una **taxonomía de ocho tipos de fuga de datos**, con casos reales de resultados que no
> replicaron. Léelo con tu propio pipeline al lado: la experiencia habitual es encontrarse en
> por lo menos una de las ocho categorías. Trae además una plantilla (*model info sheets*)
> para reportar, que sirve tal cual para un apéndice metodológico.
> Dos horas, y cambia cómo leés papers.

**6. Hastie, T., Tibshirani, R. & Friedman, J. (2009). *The Elements of Statistical Learning*
(2ª ed.), capítulo 7: «Model Assessment and Selection». Springer.** `[VERIFICAR URL]`
> El tratamiento canónico y matemático de todo lo de hoy: descomposición sesgo-varianza,
> validación cruzada, bootstrap, AIC/BIC. **Es un libro técnico** y el capítulo 7 tiene
> fórmulas de verdad; no lo abras esperando la prosa de Yarkoni. Va acá porque es la
> referencia que un revisor con formación estadística espera ver citada, y porque las
> figuras 7.1 y 7.3 son la tijera y la curva capacidad/error de esta clase, hechas bien.
> El PDF de los autores es de descarga libre; buscalo por el título.
> Para consultar, no para leer de corrido.

**7. Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*, capítulo 5:
«Machine Learning Basics» y capítulo 7: «Regularization». MIT Press.** `[VERIFICAR URL]`
> El libro está completo y gratis en la web de los autores. El capítulo 5 formaliza
> capacidad, sobreajuste y el compromiso sesgo-varianza; el 7 es el desarrollo de la slide 29
> (regularización, dropout, augmentation, y por qué todas hacen lo mismo). Es denso y no hace
> falta para el curso: está acá para cuando quieras la versión completa.
> A demanda.

**8. Salganik, M. et al. (2020). *Measuring the predictability of life outcomes with a
scientific mass collaboration*. PNAS, 117(15), 8398-8403.** `[VERIFICAR]` · DOI: 10.1073/pnas.1915006117
> 160 equipos, los mismos datos de panel (Fragile Families), la misma tarea predictiva, y
> **ninguno predijo bien**, ni siquiera con los métodos más sofisticados. Es la lectura que
> pone en escala todo lo de hoy: no alcanza con partir bien los datos; a veces el fenómeno
> simplemente no es predecible con lo que tenés, y eso también hay que poder decirlo. Es
> además una demostración de que el error no está en el analista.
> Una hora, y conviene leerlo después de Yarkoni.

**9. Lundberg, I., Brand, J. E. & Jeon, N. (2022). *Researcher reasoning meets computational
capacity: Machine learning for social science*. Social Science Research, 108, 102807.**
`[VERIFICAR]`
> Escrito para sociología: cuándo el aprendizaje automático agrega algo a una pregunta social
> y cuándo es un adorno caro. Buen contrapeso al entusiasmo y buena fuente de argumentos para
> el momento en que alguien de tu equipo proponga "meterle machine learning".
> Una hora.

---

## Las fuentes de los datos de esta clase

**10. Ariel, L. — *discursos_presidenciales* (recopilación de los mensajes presidenciales de
apertura de sesiones, Argentina).**
`https://github.com/lucariel/discursos_presidenciales` · **[VERIFICADA]**
(comprobada con `curl` sobre `raw.githubusercontent.com/lucariel/discursos_presidenciales/master/README.md`, código 200)
> Es el corpus de las clases 1 a 4, y el que trae la trampa de la clase de hoy: **2005 y 2006
> son el mismo archivo**. El propio README aclara que los discursos anteriores a 1984 se
> digitalizaron con un OCR web. La recopilación se inspira en Bercholc & Bercholc (2012),
> *Los discursos presidenciales en la Argentina democrática*, Lajouane.
> **El repositorio no declara licencia**: los textos son actos oficiales del Estado argentino
> y el uso educativo es defendible, pero si publicás algo con esto, escribile al autor.
> Ver `datos/README.md` §1.1 para el detalle de las seis trampas de este corpus.

**11. Gómez-Adorno, H., Posadas-Durán, J. P., Bel-Enguix, G. & Porto-Capetillo, C. —
*The Spanish Fake News Corpus 2.0* (FakeDeS @ IberLEF 2021).**
`https://github.com/jpposadas/FakeNewsCorpusSpanish` · **[VERIFICADA]**
(comprobada con `curl`, código 200) · Licencia **CC BY 4.0**
> Es el corpus de prensa de las clases 9 y 10, y el que inspira el ejemplo del gancho de hoy
> (modelo A vs modelo B sobre tono de titulares). **Sus trampas son espectaculares** y están
> medidas en `datos/README.md` §1.3: la fuente predice la etiqueta al 96 %, 103 titulares
> están escritos casi todo en mayúsculas y 92 de ésos son falsos. Si querés ver un caso real
> de "el modelo aprendió el atajo y no el fenómeno", empezá por ahí.

---

## Nota sobre los números del gancho

Las cifras de la slide 2 (**modelo A: 99 % / 61 %; modelo B: 84 % / 82 %**) son un **ejemplo
construido**, no una corrida guardada. Están elegidas con los órdenes de magnitud que aparecen
de verdad cuando se entrena un clasificador de titulares sobre el corpus (11) dejando la fuente
adentro y después se evalúa con una partición honesta. **Decilo en el aula si alguien pregunta.**
Los números del resto de la clase —el reencuentro, las tres capacidades, el calco, la tijera y
la comparación de particiones— **sí** salen de una corrida real y reproducible: los genera
`medir-figuras.py` con la semilla 1983, y son los mismos que produce `notebook.ipynb`.
