# Referencias — Clase 5

**La forma de los datos manda (I): imágenes**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la red
> bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. **Se probó con `curl` cada URL de esta lista** (2026).
> La única que respondió va marcada `[VERIFICADA]`; el resto va marcado `[VERIFICAR URL]`:
> **nadie abrió el enlace**, y poner una URL sin haberla abierto sería inventarla. Éste es un
> curso sobre no inventar. Quien tenga red que las complete y las pase a `[VERIFICADA]` con la
> fecha.
>
> Lo mismo vale para el **volumen, las páginas y el DOI** de cada entrada: se escribieron de
> memoria y sólo se afirman los DOI de los que hay certeza; los demás llevan `DOI [VERIFICAR]`.
> Todas las obras se encuentran buscando por **autor y título**, que es lo que sí está firme.

---

## Si te quedaste con ganas

En el orden en que conviene leerlas.

**1. Jean, N., Burke, M., Xie, M., Davis, W. M., Lobell, D. B. & Ermon, S. (2016).
*Combining satellite imagery and machine learning to predict poverty*. Science, 353(6301),
790-794.** `[VERIFICAR URL]` · DOI: 10.1126/science.aaf7894
> **La lectura obligatoria de esta clase.** Es el caso de las slides 28-30, y es el mejor ejemplo
> disponible de una CNN haciendo algo que a las ciencias sociales le importa de verdad: producir
> estimaciones de bienestar en regiones donde no hay encuestas. Leelo con las tres preguntas al
> lado y prestá especial atención a **cómo describen la validación**: qué partición usaron y hasta
> dónde dicen que se puede extrapolar. No lo leas para aprender la técnica; leelo para practicar
> el modo de leer.
> *Empezá por acá.* Una hora con las notas suplementarias por encima.

**2. Documentación de PyTorch — tutorial *Training a Classifier* (parte de «Deep Learning with
PyTorch: A 60 Minute Blitz»).** `[VERIFICAR URL]`
> El mismo recorrido del notebook de hoy, escrito por los autores de la biblioteca: cargar
> imágenes, definir una CNN, entrenarla, mirar los errores. **Sólo esa página.** Buscalo como
> "PyTorch tutorial Training a Classifier". Sirve sobre todo para acostumbrar el ojo a la
> cuaterna `(batch, canales, alto, ancho)`, que es donde todo el mundo tropieza la primera semana.
> 40 minutos.

**3. Olah, C., Mordvintsev, A. & Schubert, L. (2017). *Feature Visualization*. Distill.**
`[VERIFICAR URL]` · DOI: 10.23915/distill.00007
> **Para ver de verdad lo que la viz `jerarquia.html` te muestra como esquema.** Acá están las
> imágenes reales que maximizan la activación de unidades de una red grande: bordes, texturas,
> ojos, ruedas, caras. Es un artículo interactivo y se puede *mirar* sin leer una línea, que es
> exactamente lo que recomendamos hacer la primera vez. La discusión sobre por qué estas
> visualizaciones **pueden engañar** es tan importante como las imágenes, y es material de la
> clase 10.
> Media hora mirando; una hora si lo leés.

**4. Zeiler, M. D. & Fergus, R. (2014). *Visualizing and Understanding Convolutional Networks*.
ECCV 2014, 818-833.** `[VERIFICAR URL]` · arXiv:1311.2901
> El paper que instaló la idea de la jerarquía de representaciones con evidencia. Si el artículo
> de Distill te dejó con ganas de saber de dónde salió todo eso, es éste. Podés leer sólo la
> sección 4 y mirar las figuras 2 y 4: son el origen del dibujo bordes → texturas → partes →
> objetos que usamos hoy.
> Una hora, y se puede leer salteando la matemática.

**5. Grinsztajn, L., Oyallon, E. & Varoquaux, G. (2022). *Why do tree-based models still
outperform deep learning on tabular data?* NeurIPS 2022 (Datasets and Benchmarks).**
`[VERIFICAR URL]` · arXiv:2207.08815
> **El sustento del cartel incómodo de la viz `supuestos-de-arquitectura.html`.** Comparan
> sistemáticamente redes neuronales contra modelos de árboles sobre decenas de conjuntos de datos
> tabulares, y explican *por qué* pierden las redes: las tablas no tienen la estructura que las
> arquitecturas modernas suponen. Si trabajás con encuestas o con bases administrativas —o sea,
> si sos la mayoría de esta aula—, éste es el paper que te ahorra un proyecto mal encarado.
> Leé la introducción y la sección de conclusiones; el resto es benchmark.
> 45 minutos.

---

## Si te vas a meter en serio

**6. Cantú, F. (2019). *The Fingerprints of Fraud: Evidence from Mexico's 1988 Presidential
Election*. American Political Science Review, 113(3), 710-726.** `[VERIFICAR URL]` · DOI `[VERIFICAR]`
> **El mejor ejemplo existente de una CNN haciendo ciencia política de verdad.** Entrena una red
> convolucional sobre imágenes de actas electorales escaneadas para detectar alteraciones en los
> números escritos a mano, y con eso estima el fraude en una elección disputada. Es el trabajo que
> conviene tener en la cabeza cuando alguien pregunta «¿y esto para qué sirve en mi disciplina?».
> Prestale atención a cómo construye el conjunto de entrenamiento y cómo valida: ahí está el
> oficio.
> Dos horas.

**7. Torres, M. & Cantú, F. (2022). *Learning to See: Convolutional Neural Networks for the
Analysis of Social Science Data*. Political Analysis, 30(1), 113-131.** `[VERIFICAR URL]` · DOI `[VERIFICAR]`
> **Ojo:** el título exacto y el número de páginas de esta entrada están sin verificar.
> **Si vas a usar imágenes en tu investigación, empezá por acá y no por un tutorial técnico.**
> Es una introducción a CNN escrita para cientistas sociales, con el vocabulario de la disciplina
> y con la discusión metodológica que los tutoriales no tienen: qué se puede afirmar, cómo se
> valida, qué reportar. Cubre casi exactamente el arco de esta clase, con más profundidad y con
> ejemplos de ciencia política.
> Dos horas.

**8. Grimmer, J., Roberts, M. E. & Stewart, B. M. (2022). *Text as Data: A New Framework for
Machine Learning and the Social Sciences*. Princeton University Press.** `[VERIFICAR URL]`
> **El libro de cabecera del curso.** Es sobre texto, no sobre imágenes, pero el marco de
> **medición** —qué significa que un procedimiento automático mida un concepto, y qué validación
> hace falta para poder afirmarlo— se aplica igual a lo que hicimos hoy, y es lo que hace falta
> para contestar bien la pregunta 10 del cuestionario. Se retoma entero en la clase 10.
> El capítulo sobre medición y validación: dos horas.

**9. Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*, capítulo 9:
*Convolutional Networks*. MIT Press.** `[VERIFICAR URL]`
> El tratamiento canónico, con matemática. **Sólo si querés la formalización.** Las secciones 9.1
> a 9.3 explican con precisión las tres ideas de la clase de hoy —conexiones dispersas, parámetros
> compartidos, representaciones equivariantes— y verlas escritas con símbolos, *después* de
> haberlas manoseado con el slider, es una experiencia distinta a verlas antes.
> Tres horas si lo trabajás.

**10. Rolf, E., Proctor, J., Carleton, T., Bolliger, I., Shankar, V., Ishihara, M., Recht, B. &
Hsiang, S. (2021). *A generalizable and accessible approach to machine learning with global
satellite imagery*. Nature Communications, 12, 4392.** `[VERIFICAR URL]` · DOI `[VERIFICAR]`
> **La continuación crítica del punto 1.** Proponen un método mucho más simple y barato para
> predecir variables socioeconómicas desde satélites, y —lo que a nosotros nos importa— discuten
> explícitamente **la generalización entre regiones**, que es la pregunta 3 de la slide 29.
> Leelo después de Jean et al. y la conversación se te arma sola.
> Dos horas.

---

## Datos y herramientas

**11. FashionMNIST — Xiao, H., Rasul, K. & Vollgraf, R. (2017), Zalando Research.**
`[VERIFICADA]` · https://raw.githubusercontent.com/zalandoresearch/fashion-mnist/master/README.md
> El sandbox técnico del notebook: 70.000 imágenes de 28×28 de prendas de ropa, licencia MIT.
> El README explica de dónde salió y por qué reemplaza al MNIST de dígitos (demasiado fácil).
> **Es un sandbox y hay que decirlo cada vez que aparece:** no es un dato de ciencias sociales y
> ninguna conclusión sustantiva sale de ahí.
> Diez minutos.

**12. El corpus visual de la sección 6 del notebook.** *No hay enlace: se genera en el notebook.*
> Es **sintético**, hecho con numpy, y está a la vista en la función `archivo_visual`. País
> ficticio, proceso generador conocido, cero fotos de personas reales. Se usa precisamente porque
> **sabemos la verdad**: por eso podemos mostrar que los errores del modelo se concentran en las
> copas de árboles, y no simplemente afirmarlo. Si querés adaptarlo a tu propio archivo, la
> función es corta y está comentada.

---

## Para el docente

**13. Krizhevsky, A., Sutskever, I. & Hinton, G. E. (2012). *ImageNet Classification with Deep
Convolutional Neural Networks*. NeurIPS 2012.** `[VERIFICAR URL]`
> El paper que arrancó todo esto. No lo pongas como lectura del curso —es técnico y de 2012—,
> pero conviene tener presente la escena: en un año se pasó de un error del 26 % al 15 % en una
> competencia estancada, y eso reorientó un campo entero. Sirve para contestar «¿por qué ahora?»
> sin mitología.

**14. LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. (1998). *Gradient-based learning applied to
document recognition*. Proceedings of the IEEE, 86(11), 2278-2324.** `[VERIFICAR URL]`
> LeNet-5, la CNN original, aplicada a reconocer cheques bancarios. Útil para la anécdota
> honesta: **la idea es de los ochenta y noventa, no de 2012**. Lo que cambió fue la cantidad de
> datos y el poder de cómputo, no la idea. Sirve para bajarle la temperatura al «esto es
> revolucionario y nuevo».
