# Referencias — Clase 6

**La forma de los datos manda: texto, secuencias y embeddings**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la
> red bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org`
> y `raw.githubusercontent.com`. **Se probó con `curl` cada URL de esta lista.** Las que
> respondieron van marcadas `[VERIFICADA]` con la fecha; el resto va marcado
> `[VERIFICAR URL]`: las obras existen, están bien citadas y se encuentran buscando por
> título y autor, pero **nadie abrió el enlace**, y poner una URL sin haberla abierto
> sería inventarla. Éste es un curso sobre no inventar. Quien tenga red que las
> complete y las pase a `[VERIFICADA]` con la fecha.

---

## Si te quedaste con ganas

En el orden en que conviene leerlas.

**1. Rodriguez, P. & Spirling, A. (2022). *Word Embeddings: What Works, What Doesn't,
and How to Tell the Difference for Applied Research*. The Journal of Politics.**
`[VERIFICAR URL]`
> **Si vas a leer una sola cosa de esta clase, es ésta.** Está escrita exactamente para
> esta audiencia: gente de ciencias sociales que quiere usar embeddings en su
> investigación y necesita saber cuándo confiar. Responde con evidencia las tres
> preguntas que te vas a hacer el lunes: ¿entreno los míos o uso pre-entrenados?
> ¿cuántas dimensiones? ¿cuánto texto hace falta? Y —lo más útil— compara los métodos
> contra juicios humanos, así que las conclusiones no son de fe.
> *Empezá por acá.* Una hora larga, y se lee sin sufrir.

**2. Kozlowski, A., Taddy, M. & Evans, J. (2019). *The Geometry of Culture: Analyzing
the Meanings of Class through Word Embeddings*. American Sociological Review 84(5).**
`[VERIFICAR URL]`
> **Es literalmente el modo «eje» de la visualización que movieron hoy, convertido en
> investigación.** Definen ejes culturales (rico–pobre, culto–inculto, masculino–femenino)
> con pares de palabras y proyectan el vocabulario para medir cómo se estructura el
> significado de la clase social a lo largo del siglo XX. Leé sobre todo la sección de
> **validación**: cómo demuestran que el eje mide lo que dicen que mide, comparando
> contra encuestas. Esa parte es el modelo a imitar en tu propio trabajo.
> Segunda lectura, y la más empoderadora del curso.

**3. Garg, N., Schiebinger, L., Jurafsky, D. & Zou, J. (2018). *Word embeddings quantify
100 years of gender and ethnic stereotypes*. PNAS 115(16).** `[VERIFICAR URL]`
> El caso más claro de **«el sesgo como hallazgo»**: entrenan un embedding por década
> sobre cien años de texto y miden cómo cambiaron los estereotipos ocupacionales y
> étnicos. Lo que hace que el paper funcione es que **validan contra datos censales**:
> el embedding predice la composición real de las ocupaciones. Eso es lo que convierte
> una curiosidad en una medición.
> Corto, muy visual, y contesta solo la pregunta «¿y esto para qué sirve?».

**4. Jay Alammar, *The Illustrated Word2vec*.** `[VERIFICAR URL]`
> El mejor material visual que existe sobre embeddings, y es gratis. Explica con dibujos
> lo mismo que vimos hoy, con más detalle sobre cómo se entrena word2vec (que nosotros
> no hicimos: usamos PPMI + SVD, que llega a un resultado parecido por otro camino).
> Si algo de la clase quedó borroso, esto lo termina de acomodar.
> Buscalo como «Jay Alammar Illustrated Word2vec». 40 minutos.

**5. Grimmer, J., Roberts, M. & Stewart, B. (2022). *Text as Data: A New Framework for
Machine Learning and the Social Sciences*. Princeton University Press.** `[VERIFICAR URL]`
> **El libro de cabecera de todo este módulo.** Para hoy: los capítulos sobre
> representación de texto (por qué la bolsa de palabras funciona tanto como funciona,
> y dónde deja de funcionar) y sobre validación de medidas. El capítulo de validación
> es el que te va a salvar del revisor 2.
> No se lee entero de una: es un libro de consulta. Volvés a él en las clases 9 y 10.

---

## Si te vas a meter en serio

**6. Firth, J. R. (1957). *A synopsis of linguistic theory 1930-1955*. En *Studies in
Linguistic Analysis*, Blackwell.** `[VERIFICAR URL]`
> La fuente de la cita («*You shall know a word by the company it keeps*»). No hace
> falta leerlo entero: sirve para citarlo bien y para ver que la hipótesis distribucional
> es lingüística de mediados del siglo XX, no una ocurrencia de Silicon Valley.
> Si te interesa la discusión teórica, la pareja obligada es Wittgenstein
> (*Investigaciones filosóficas*, §43: «el significado de una palabra es su uso en el
> lenguaje»).

**7. Mikolov, T., Chen, K., Corrado, G. & Dean, J. (2013). *Efficient Estimation of Word
Representations in Vector Space*.** `[VERIFICAR URL]`
> El paper de **word2vec**, el que popularizó todo esto. Corto y legible. Ojo con la
> sección de analogías: es la que generó el entusiasmo desmedido que hoy vimos
> desinflarse (dos de diez, en nuestro corpus). Leelo sabiendo eso.

**8. Levy, O. & Goldberg, Y. (2014). *Neural Word Embedding as Implicit Matrix
Factorization*. NeurIPS.** `[VERIFICAR URL]`
> **El paper que justifica lo que hicimos en el notebook.** Demuestra que word2vec con
> muestreo negativo está factorizando implícitamente una matriz de PMI desplazada — o
> sea, que el camino «contar coocurrencias → PPMI → SVD» y el camino «entrenar una red»
> llegan al mismo lugar. Es la versión formal de la celda donde el descenso por
> gradiente y el SVD dieron 5,2 vecinas de 6 en común.
> Técnico, pero la introducción sola ya vale.

**9. Bolukbasi, T., Chang, K.-W., Zou, J., Saligrama, V. & Kalai, A. (2016). *Man is to
Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*. NeurIPS.**
`[VERIFICAR URL]`
> El paper que abrió la discusión de sesgo en embeddings, y **el que propone
> corregirlo**. Leelo junto con Garg et al. (3): uno quiere borrar el sesgo, el otro lo
> quiere medir. Esa tensión es la slide 25 de hoy, y no tiene una respuesta única.
> Leé también las críticas posteriores al método de debiasing (Gonen & Goldberg, 2019,
> *Lipstick on a Pig*): mostraron que la corrección esconde el sesgo sin eliminarlo.
> `[VERIFICAR URL]`

**10. Jurafsky, D. & Martin, J. H. *Speech and Language Processing*, 3.ª edición
(borrador gratuito online).** `[VERIFICAR URL]`
> El manual estándar de procesamiento de lenguaje natural. Para hoy: el capítulo de
> **vectores semánticos** (coocurrencia, PPMI, TF-IDF, word2vec, similitud coseno) y el
> de **embeddings**. Está escrito para enseñar, tiene ejercicios, y el borrador es
> gratis y se actualiza. Es la referencia técnica a la que volver cuando algo de la
> notación no cierre.
> Buscalo como «Jurafsky Martin Speech and Language Processing 3rd edition».

**11. Sennrich, R., Haddow, B. & Birch, A. (2016). *Neural Machine Translation of Rare
Words with Subword Units*. ACL.** `[VERIFICAR URL]`
> De dónde sale el **BPE** de la visualización del tokenizador. Explica por qué las
> sub-palabras ganaron: nunca hay palabras desconocidas y el vocabulario queda chico.
> Es el algoritmo que hoy usa GPT, en grande.
> Sólo si te picó la curiosidad del tokenizador. Media hora.

---

## Herramientas (para usar el lunes)

- **gensim** — la biblioteca clásica para entrenar y usar word2vec, fastText y
  similares en Python. `https://pypi.org/project/gensim/` **[VERIFICADA · 2026-08-29]**
  (la documentación está en `radimrehurek.com/gensim`, **[VERIFICAR URL]**).
- **spaCy** — tokenización, lematización y entidades **en castellano** hechas en serio.
  Lo que hoy hicimos con una regex de una línea, con reglas de verdad.
  `https://pypi.org/project/spacy/` **[VERIFICADA · 2026-08-29]**. Los modelos en
  castellano se llaman `es_core_news_sm` / `es_core_news_lg`. `[VERIFICAR URL]`
- **`ssdl.datos`** (este curso) — `embeddings_ppmi_svd()`, `vecinos()` y
  `matriz_de_coocurrencia()`. Sin dependencias, sin red, cuatro segundos sobre 350.000
  palabras. Suficiente para explorar un corpus propio, y es el código que leíste.

## Los datos de hoy

- **Discursos de apertura de sesiones (Argentina, 1854-2019).** Recopilación de
  **Lucas Ariel**. Los archivos que baja el curso viven en
  `https://raw.githubusercontent.com/lucariel/discursos_presidenciales/master/data/sesiones_ordinarias/`
  — **ojo: esa ruta es un directorio y `raw.githubusercontent.com` no lista
  directorios, así que sola devuelve 404. Lo que se verifica es cada archivo**:
  `.../sesiones_ordinarias/1984-raul_alfonsin.txt` → 200
  y el README en `.../master/README.md` → 200, las dos **[VERIFICADA · 2026-08-29]**.
  La portada del repo (`github.com/lucariel/discursos_presidenciales`) no se pudo
  abrir desde acá: `github.com` en HTML da 403. `[VERIFICAR URL]`.
  Los textos son mensajes presidenciales al Congreso de la Nación: documentos públicos. **La recopilación no declara licencia**; se usa acá
  con fines educativos y se cita. Las trampas del corpus (los agujeros son los golpes
  de Estado; 2005 y 2006 son el mismo discurso; el largo varía por un factor de 9)
  están documentadas en `datos/README.md` §1.1, y **hay que leerlas antes de sacar
  cualquier conclusión sustantiva de este material**.

---

## Lo que NO hace falta que leas ahora

Dicho explícitamente, porque la tentación es real y no ayuda:

- **El paper original de las LSTM** (Hochreiter & Schmidhuber, 1997). Las RNN están en
  esta clase sólo como motivación de attention. Si te ponés a estudiar compuertas, vas
  a gastar una semana en una arquitectura que ya casi nadie usa.
- **Cualquier cosa sobre t-SNE o UMAP.** Son mejores que PCA para dibujar nubes, sí, y
  también son mucho más fáciles de sobreinterpretar: las distancias entre grupos en un
  t-SNE **no significan nada**. Antes de usarlos, que quede firme la idea de que el
  dibujo es una sombra.
- **La documentación de Hugging Face.** Llega en la clase 9, con su propia guía.
