# Bibliografía del curso

La lista consolidada de todo lo que se cita en las diez clases, sin repetir. Cada
`referencias.md` de clase es un subconjunto de esto, con el comentario específico
de por qué se lee **ahí**.

## Cómo leer las marcas

| Marca | Qué quiere decir |
|---|---|
| `[VERIFICADA · fecha]` | Alguien corrió `curl` contra esa URL exacta y devolvió 200. |
| `[ESPEJO VERIFICADO]` | La obra tiene una URL canónica que no se pudo abrir, **pero sí se abrió un archivo del repositorio oficial** (código, README). Sirve para confirmar que el proyecto existe; **no** reemplaza al enlace de la obra. |
| `[VERIFICAR URL]` | La obra existe y está bien citada, **pero nadie pudo abrir el enlace**. |
| `[VERIFICAR]` | Falta chequear algún dato de la cita (año, revista, número de página). |

> **Por qué hay tantas `[VERIFICAR]`.** El contenedor donde se construyó este
> repo tiene casi toda la red bloqueada: sólo llegan `pypi.org`,
> `files.pythonhosted.org`, `registry.npmjs.org` y `raw.githubusercontent.com`.
> No se puede abrir `arxiv.org`, `huggingface.co`, `doi.org`, YouTube ni las
> páginas HTML de GitHub. **Poner una URL sin haberla abierto sería inventarla**,
> y este es un curso sobre no inventar. Así que las citas están completas
> (autor, año, título, publicación) y los enlaces quedan marcados para que
> alguien con red los complete. Ver "Estado de las URLs" al final.

> **Regla dura del curso.** Si una obra no se puede encontrar, **se saca la cita.
> No se le inventa un enlace, y no se le inventa un DOI.** Preferimos una
> bibliografía corta y verdadera a una larga y falsa.

**Total: 66 obras.** Todas las URLs que aparecen abajo fueron probadas con `curl`
el **2026-08-29**; las que respondieron están marcadas y las que no, también.

---

## 1. Deep learning explicado con dibujos (para el estudiante)

- **3Blue1Brown**, serie *Essence of Calculus*, cap. 1 — intuición visual de función. Subtítulos en español. `[VERIFICAR URL]` — el código de las animaciones sí abre: `https://raw.githubusercontent.com/3b1b/videos/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 1*
- **3Blue1Brown**, *But what is a neural network?* — se anuncia en la clase 1 y se recomienda mirarlo **después de la clase 2**. `[VERIFICAR URL]` · *clases 1, 2*
- **3Blue1Brown**, *Gradient descent, how neural networks learn* (cap. 2 de la serie). `[VERIFICAR URL]` · *clase 3*
- **3Blue1Brown**, capítulos sobre transformers y attention. `[VERIFICAR URL]` · *clase 7*
- **Nielsen, M.**, *Neural Networks and Deep Learning*, cap. 4: *A visual proof that neural nets can compute any function*. `[VERIFICAR URL]` (`neuralnetworksanddeeplearning.com` da 403 desde acá) — el repositorio del libro sí abre: `https://raw.githubusercontent.com/mnielsen/neural-networks-and-deep-learning/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 2*
- **TensorFlow Playground** — juguete en el navegador: poner capas y ver la figura que dibuja. `[VERIFICAR URL]` — código: `https://raw.githubusercontent.com/tensorflow/playground/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 2*
- **Jay Alammar**, *The Illustrated Word2vec*. `[VERIFICAR URL]` · *clase 6*
- **Jay Alammar**, *The Illustrated Transformer*. `[VERIFICAR URL]` · *clase 7*
- **Jay Alammar**, *The Illustrated GPT-2*. El texto fuente del post está verificado: `https://raw.githubusercontent.com/jalammar/jalammar.github.io/master/_posts/2019-08-12-illustrated-gpt2.md` `[VERIFICADA · 2026-08-29]`; la versión con animaciones vive en su blog `[VERIFICAR URL]` · *clase 8*
- **Karpathy, A.**, *Let's build GPT: from scratch, in code, spelled out* (video) y el repo `nanoGPT`. **Es la fuente de las clases 7-8 y hay que citarla como tal.** El video `[VERIFICAR URL]`; el código `https://raw.githubusercontent.com/karpathy/ng-video-lecture/master/gpt.py` `[VERIFICADA · 2026-08-29]` · *clases 7, 8*
- **Wolfram, S.** (2023), *What Is ChatGPT Doing… and Why Does It Work?* — se recomiendan las primeras tres secciones. `[VERIFICAR URL]` · *clase 8*
- **Goh, G.** (2017), *Why Momentum Really Works*, Distill — por qué un valle alargado hace zigzaguear al descenso. Es la continuación de la última celda del notebook de la clase 3. `[VERIFICAR URL]` (`distill.pub` no responde) — fuente del artículo: `https://raw.githubusercontent.com/distillpub/post--momentum/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 3*
- **Olah, C., Mordvintsev, A. & Schubert, L.** (2017), *Feature Visualization*, Distill. DOI 10.23915/distill.00007 `[VERIFICAR URL]` — la biblioteca con la que se hicieron esas imágenes: `https://raw.githubusercontent.com/tensorflow/lucid/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 5*
- **Zeiler, M. & Fergus, R.** (2014), *Visualizing and Understanding Convolutional Networks*, ECCV 2014, 818-833 (arXiv:1311.2901). El origen del dibujo bordes → texturas → partes → objetos de la clase 5. `[VERIFICAR URL]` · *clase 5*
- **StatQuest** (Josh Starmer), videos sobre *bias/variance tradeoff* y *cross-validation*. `[VERIFICAR URL]` · *clase 4*
- **Severance, C.**, *Python para todos* (py4e), caps. 1-4, versión en castellano. `[VERIFICAR URL]` — el repositorio del proyecto sí abre: `https://raw.githubusercontent.com/csev/py4e/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 1*
- **PyTorch**, tutorial oficial *Learn the Basics* (sólo *Tensors* y *Optimizing Model Parameters*) y *Training a Classifier* (del *60 Minute Blitz*). `[VERIFICAR URL]` — el repositorio de los tutoriales sí abre: `https://raw.githubusercontent.com/pytorch/tutorials/main/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clases 4, 5*
- **Hugging Face**, curso oficial de NLP, caps. 1-3. La versión en castellano existe y está incompleta (*work in progress*). Página del curso `[VERIFICAR URL]` (`huggingface.co` está bloqueado acá); repositorio con el contenido: `https://raw.githubusercontent.com/huggingface/course/main/README.md` `[VERIFICADA · 2026-08-29]` · *clase 9*
- **`scikit-learn`**, guía de *model evaluation* (precisión, recall, F1, matriz de confusión). `[VERIFICAR URL]` — paquete: `https://pypi.org/project/scikit-learn/` `[VERIFICADA · 2026-08-29]`; código: `https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/README.rst` `[ESPEJO VERIFICADO · 2026-08-29]` · *clases 9, 10*

## 2. Ciencias sociales computacionales (el marco del curso)

- **Grimmer, J., Roberts, M. E. & Stewart, B. M.** (2022), *Text as Data: A New Framework for Machine Learning and the Social Sciences*, Princeton University Press. **El libro de cabecera del curso.** `[VERIFICAR URL]` · *clases 1, 2, 4, 5, 6, 7, 9, 10*
- **Grimmer, J. & Stewart, B.** (2013), *Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts*, Political Analysis 21(3), 267-297. `[VERIFICAR URL]` · *clases 9, 10*
- **Molina, M. & Garip, F.** (2019), *Machine Learning for Sociology*, Annual Review of Sociology 45, 27-45. `[VERIFICAR URL]` · *clases 1, 2*
- **Breiman, L.** (2001), *Statistical Modeling: The Two Cultures*, Statistical Science 16(3), 199-231. **Fundamenta el "camino A vs camino B" de la clase 1**, y es la mejor lectura para acompañar la incomodidad que deja la clase 2. `[VERIFICAR URL]` · *clases 1, 2*
- **Yarkoni, T. & Westfall, J.** (2017), *Choosing Prediction Over Explanation in Psychology: Lessons From Machine Learning*, Perspectives on Psychological Science 12(6), 1100-1122. DOI 10.1177/1745691617693393. **La mejor lectura para traducir la distinción ajuste/predicción al vocabulario de las ciencias sociales.** `[VERIFICAR URL]` · *clase 4*
- **Salganik, M. et al.** (2020), *Measuring the predictability of life outcomes with a scientific mass collaboration*, PNAS 117(15), 8398-8403. DOI 10.1073/pnas.1915006117. 160 equipos, los mismos datos de panel, y **ninguno predijo bien**. `[VERIFICAR URL]` · *clases 4, 9, 10*
- **Lundberg, I., Brand, J. E. & Jeon, N.** (2022), *Researcher reasoning meets computational capacity: Machine learning for social science*, Social Science Research 108, 102807. Cuándo el aprendizaje automático agrega algo a una pregunta social y cuándo es un adorno caro. `[VERIFICAR URL]` · *clases 4, 10*
- **Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z. & Yang, D.** (2024), *Can Large Language Models Transform Computational Social Science?*, Computational Linguistics 50(1). `[VERIFICAR URL]` · *clases 8, 9*
- **Barberá, P., Boydstun, A. E., Linn, S., McMahon, R. & Nagler, J.** (2021), *Automated Text Classification of News Articles: A Practical Guide to Probabilistic Machine Learning*, Political Analysis 29(1), 19-42. **Es prácticamente el manual de la clase 9**, incluida la respuesta empírica a cuántos documentos hay que etiquetar. `[VERIFICAR URL]` · *clases 9, 10*
- **Barrie, C., Palmer, A. & Spirling, A.** (2024), *Replication for Language Models: Problems, Principles, and Best Practice for Political Science*. `[VERIFICAR URL]` · *clase 8*
- **Simon, H. A.** (1955), *A Behavioral Model of Rational Choice*, Quarterly Journal of Economics 69(1), 99-118 — para fundamentar la analogía de la niebla y la discusión sobre elegir la función de pérdida. `[VERIFICAR URL]` `[VERIFICAR — páginas]` · *clase 3*
- **Ragin, C. C. & Becker, H. S.** (eds.) (1992), *What Is a Case? Exploring the Foundations of Social Inquiry*, Cambridge University Press — la tradición del caso desviado es, dicha en el vocabulario de hoy, la decisión de darle mucho peso al outlier: MSE contra MAE. `[VERIFICAR URL]` · *clase 3*
- **Stigler, S. M.** (1986), *The History of Statistics: The Measurement of Uncertainty before 1900*, Harvard University Press, cap. 1 — de dónde sale que el MSE sea el default: tenía solución cerrada. `[VERIFICAR URL]` · *clase 3*

## 3. Estudios empíricos que usamos como caso

- **Jean, N., Burke, M., Xie, M., Davis, W. M., Lobell, D. B. & Ermon, S.** (2016), *Combining satellite imagery and machine learning to predict poverty*, Science 353(6301), 790-794. DOI 10.1126/science.aaf7894. **Es el caso del `[EL LUNES]` de la clase 5.** `[VERIFICAR URL]` · *clase 5*
- **Rolf, E., Proctor, J., Carleton, T., Bolliger, I., Shankar, V., Ishihara, M., Recht, B. & Hsiang, S.** (2021), *A generalizable and accessible approach to machine learning with global satellite imagery*, Nature Communications 12, 4392. La continuación crítica de Jean et al.: discute explícitamente la **generalización entre regiones**. `[VERIFICAR URL]` · *clases 5, 10*
- **Cantú, F.** (2019), *The Fingerprints of Fraud: Evidence from Mexico's 1988 Presidential Election*, American Political Science Review 113(3), 710-726. **El mejor ejemplo existente de una CNN haciendo ciencia política de verdad.** `[VERIFICAR URL]` · *clase 5*
- **Torres, M. & Cantú, F.** (2022), *Learning to See: Convolutional Neural Networks for the Analysis of Social Science Data*, Political Analysis 30(1), 113-131. **La mejor introducción a CNN escrita para cientistas sociales.** `[VERIFICAR URL]` · *clase 5*
- **Kozlowski, A., Taddy, M. & Evans, J.** (2019), *The Geometry of Culture: Analyzing the Meanings of Class through Word Embeddings*, American Sociological Review 84(5). `[VERIFICAR URL]` · *clase 6*
- **Garg, N., Schiebinger, L., Jurafsky, D. & Zou, J.** (2018), *Word embeddings quantify 100 years of gender and ethnic stereotypes*, PNAS 115(16). **El caso de "el sesgo como hallazgo".** `[VERIFICAR URL]` · *clases 6, 10*
- **Rodriguez, P. & Spirling, A.** (2022), *Word Embeddings: What Works, What Doesn't, and How to Tell the Difference for Applied Research*, The Journal of Politics. `[VERIFICAR URL]` · *clase 6*

## 4. Crítica, validez y ética

- **Cronbach, L. J. & Meehl, P. E.** (1955), *Construct Validity in Psychological Tests*, Psychological Bulletin 52(4), 281-302. **La fuente clásica de la validez de constructo**, y vale citarla en el aula para marcar que el problema tiene setenta años y es de las ciencias sociales, no del machine learning. `[VERIFICAR URL]` · *clase 10*
- **Jacobs, A. Z. & Wallach, H.** (2021), *Measurement and Fairness*, FAccT '21, 375-385. Pone nombre a la distancia entre el constructo que querés medir y el número que sale; **se cita ya en la clase 1** y se cobra en la 10. `[VERIFICAR URL]` · *clases 1, 10*
- **Kapoor, S. & Narayanan, A.** (2023), *Leakage and the Reproducibility Crisis in ML-based Science*, Patterns 4(9), 100804. DOI 10.1016/j.patter.2023.100804. Revisan 294 artículos de 17 campos. `[VERIFICAR URL]` · *clases 4, 10*
- **Narayanan, A. & Kapoor, S.** (2024), *AI Snake Oil* (libro y blog homónimo). Lo más legible que hay sobre qué promete y qué no promete la IA. **Se recomienda leerlo después del curso, no antes.** `[VERIFICAR URL]` · *clase 10*
- **Bender, E., Gebru, T., McMillan-Major, A. & Shmitchell, S.** (2021), *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?*, FAccT '21. **Lectura fundamental del bloque de criterio**, a presentar con matices. `[VERIFICAR URL]` · *clases 8, 10*
- **Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D. & Gebru, T.** (2019), *Model Cards for Model Reporting*, FAccT '19, 220-229. La plantilla de la ficha del modelo de la clase 10. `[VERIFICAR URL]` · *clase 10*
- **Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H. & Crawford, K.** (2021), *Datasheets for Datasets*, Communications of the ACM 64(12), 86-92. La ficha, pero para los **datos**: `datos/README.md` de este curso está escrito con esa forma. `[VERIFICAR URL]` · *clases 9, 10*
- **Selbst, A. D., boyd, d., Friedler, S. A., Venkatasubramanian, S. & Vertesi, J.** (2019), *Fairness and Abstraction in Sociotechnical Systems*, FAccT '19, 59-68. Por qué «arreglar el modelo» no arregla el sistema. `[VERIFICAR URL]` · *clase 10*
- **Salganik, M.** (2018), *Bit by Bit: Social Research in the Digital Age*, Princeton University Press (disponible online). Capítulo 6 (ética) y capítulo 2 (observar comportamiento). `[VERIFICAR URL]` · *clases 4, 10*
- **Krippendorff, K.**, *Content Analysis: An Introduction to Its Methodology* — marco de fiabilidad entre codificadores (kappa, alpha). `[VERIFICAR URL]` · *clases 9, 10*
- **Jain, S. & Wallace, B.** (2019), *Attention is not Explanation*, NAACL (preprint arXiv:1902.10186). **Sustenta la advertencia contra la sobreinterpretación de la clase 7.** `[VERIFICAR URL]` — el código sí abre: `https://raw.githubusercontent.com/successar/AttentionExplanation/master/README.md` `[VERIFICADA · 2026-08-29]` · *clase 7*
- **Wiegreffe, S. & Pinter, Y.** (2019), *Attention is not not Explanation*, EMNLP — la réplica. Mencionar las dos es parte del punto. `[VERIFICAR URL]` · *clase 7*
- **Bolukbasi, T., Chang, K.-W., Zou, J., Saligrama, V. & Kalai, A.** (2016), *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*, NeurIPS. `[VERIFICAR URL]` — el código sí abre: `https://raw.githubusercontent.com/tolga-b/debiaswe/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clases 6, 10*
- **Gonen, H. & Goldberg, Y.** (2019), *Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings*, NAACL. La réplica a Bolukbasi: la corrección esconde el sesgo sin eliminarlo. `[VERIFICAR URL]` · *clases 6, 10*
- **Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P.** (2023), *Lost in the Middle: How Language Models Use Long Contexts*, TACL. `[VERIFICAR URL]` · *clase 8*
- **Grinsztajn, L., Oyallon, E. & Varoquaux, G.** (2022), *Why do tree-based models still outperform deep learning on tabular data?*, NeurIPS 2022 Datasets & Benchmarks (arXiv:2207.08815). **Es la referencia honesta para decir "acá no uses deep learning"**, y sustenta el cartel de `viz/supuestos-de-arquitectura.html` cuando elegís «una tabla de encuesta». `[VERIFICAR URL]` · *clases 5, 10*

## 5. Técnico (para el docente, no para el aula)

- **Vaswani, A. et al.** (2017), *Attention Is All You Need*, NeurIPS (arXiv:1706.03762). Se muestra la primera página, no se lee. `[VERIFICAR URL]` · *clase 7*
- **Goodfellow, I., Bengio, Y. & Courville, A.** (2016), *Deep Learning*, MIT Press (gratis online). Cap. 4 y 8 para la clase 3; cap. 5 y 7 para la 4; cap. 6 §6.1-6.4 para la 2; cap. 9 para la 5. `[VERIFICAR URL]` · *clases 2, 3, 4, 5*
- **Hastie, T., Tibshirani, R. & Friedman, J.** (2009), *The Elements of Statistical Learning* (2ª ed.), cap. 7: *Model Assessment and Selection*. Springer. `[VERIFICAR URL]` · *clase 4*
- **Cybenko, G.** (1989), *Approximation by superpositions of a sigmoidal function*, Mathematics of Control, Signals and Systems 2(4), 303-314. Sólo la referencia: **no se dicta el teorema.** `[VERIFICAR URL]` · *clase 2*
- **Hornik, K.** (1991), *Approximation capabilities of multilayer feedforward networks*, Neural Networks 4(2), 251-257. `[VERIFICAR URL]` · *clase 2*
- **McCulloch, W. & Pitts, W.** (1943), *A Logical Calculus of the Ideas Immanent in Nervous Activity*, Bulletin of Mathematical Biophysics 5, 115-133 — para la anécdota histórica del nombre "neurona". `[VERIFICAR URL]` · *clase 2*
- **Krizhevsky, A., Sutskever, I. & Hinton, G. E.** (2012), *ImageNet Classification with Deep Convolutional Neural Networks*, NeurIPS. El paper que arrancó todo esto. **Para la anécdota, no como lectura.** `[VERIFICAR URL]` · *clase 5*
- **LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P.** (1998), *Gradient-based learning applied to document recognition*, Proceedings of the IEEE 86(11), 2278-2324. LeNet-5, la CNN original, leyendo cheques bancarios. `[VERIFICAR URL]` · *clase 5*
- **Ruder, S.** (2016), *An overview of gradient descent optimization algorithms* (arXiv:1609.04747) — el recorrido más claro de SGD → momento → Adagrad → RMSprop → Adam, con la intuición antes de la fórmula. `[VERIFICAR URL]` · *clase 3*
- **Ouyang, L. et al.** (2022), *Training Language Models to Follow Instructions with Human Feedback* (InstructGPT), NeurIPS. Cómo se pasa de autocompletador a asistente. `[VERIFICAR URL]` · *clase 8*
- **Elhage, N. et al.** (2021), *A Mathematical Framework for Transformer Circuits*, Anthropic — sólo para el docente y sólo si le agarró la curiosidad de interpretabilidad. `[VERIFICAR URL]` · *clase 7*
- **Firth, J. R.** (1957), *A synopsis of linguistic theory 1930-1955*, en *Studies in Linguistic Analysis*, Blackwell. La fuente de «*You shall know a word by the company it keeps*». `[VERIFICAR URL]` · *clase 6*
- **Mikolov, T., Chen, K., Corrado, G. & Dean, J.** (2013), *Efficient Estimation of Word Representations in Vector Space*. El paper de word2vec. **Ojo con su sección de analogías: es la que generó el entusiasmo desmedido que la clase 6 desinfla con datos propios.** `[VERIFICAR URL]` — el código original: `https://raw.githubusercontent.com/tmikolov/word2vec/master/README.txt` `[ESPEJO VERIFICADO · 2026-08-29]` · *clase 6*
- **Levy, O. & Goldberg, Y.** (2014), *Neural Word Embedding as Implicit Matrix Factorization*, NeurIPS. **Justifica formalmente lo que hace el notebook de la clase 6**: contar coocurrencias + PPMI + SVD y entrenar una red llegan al mismo lugar. `[VERIFICAR URL]` · *clase 6*
- **Sennrich, R., Haddow, B. & Birch, A.** (2016), *Neural Machine Translation of Rare Words with Subword Units*, ACL. De acá sale el BPE de `viz/tokenizador.html`. `[VERIFICAR URL]` — el código: `https://raw.githubusercontent.com/rsennrich/subword-nmt/master/README.md` `[ESPEJO VERIFICADO · 2026-08-29]` · *clases 6, 8*
- **Reimers, N. & Gurevych, I.** (2019), *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*, EMNLP (preprint arXiv:1908.10084). `[VERIFICAR URL]` — la biblioteca: `https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/README.md` `[VERIFICADA · 2026-08-29]` y `https://pypi.org/project/sentence-transformers/` `[VERIFICADA · 2026-08-29]` · *clase 9*
- **Jurafsky, D. & Martin, J. H.**, *Speech and Language Processing*, 3.ª ed. (borrador gratuito). Los capítulos de vectores semánticos y de embeddings son la referencia técnica de la clase 6. `[VERIFICAR URL]` · *clases 6, 7, 9*
- **Karpathy, A.**, *nanoGPT* — 300 líneas que son un GPT entrenable; se compara pieza por pieza con el `BloqueTransformer` del notebook de la clase 7. `https://raw.githubusercontent.com/karpathy/nanoGPT/master/model.py` y `/train.py` `[VERIFICADA · 2026-08-29]`. Su hermano didáctico *minGPT*: `https://raw.githubusercontent.com/karpathy/minGPT/master/README.md` `[VERIFICADA · 2026-08-29]` · *clases 7, 8*
- **Karpathy, A.**, *build-nanogpt* — reproducir GPT-2 (124M) desde cero. Está para que se vea **cuánto cuesta**: es el argumento cuantitativo del puente de la clase 8 a la 9. `https://raw.githubusercontent.com/karpathy/build-nanogpt/master/train_gpt2.py` `[VERIFICADA · 2026-08-29]` · *clases 8, 9*
- **Karpathy, A.**, *minbpe* — el BPE de la clase 6 en 200 líneas comentadas. `https://raw.githubusercontent.com/karpathy/minbpe/master/README.md` `[VERIFICADA · 2026-08-29]` · *clases 6, 8*
- **`tiktoken`** (OpenAI) — tres líneas para ver en qué fichas parte un modelo real cualquier texto tuyo. El castellano se parte en más fichas que el inglés, y eso tiene consecuencias de costo y de calidad. `https://raw.githubusercontent.com/openai/tiktoken/main/README.md` `[VERIFICADA · 2026-08-29]` · *clases 6, 8*
- **Prompt Engineering Guide** (DAIR.AI) — práctico, no teórico: qué técnicas bajan la tasa de error al usar un LLM como asistente de codificación. Leerlo sabiendo que ninguna instala un verificador de verdad. `https://raw.githubusercontent.com/dair-ai/Prompt-Engineering-Guide/main/README.md` `[VERIFICADA · 2026-08-29]` · *clases 8, 9*
- **Rush, A. et al.**, *The Annotated Transformer* — el paper de 2017 línea por línea, con el código al lado. Para consultar un detalle, no para leer de corrido. `https://raw.githubusercontent.com/harvardnlp/annotated-transformer/master/README.md` `[VERIFICADA · 2026-08-29]` · *clase 7*
- **Vig, J.**, *BertViz* — el visor estándar de atención de modelos pre-entrenados, capa por capa y cabeza por cabeza, adentro de un notebook. Se usa **con** la advertencia de la clase 7 puesta. `https://raw.githubusercontent.com/jessevig/bertviz/master/README.md` `[VERIFICADA · 2026-08-29]` · *clases 7, 9*

## 6. Modelos y herramientas en castellano

- **Cañete, J., Chaperon, G., Fuentes, R., Ho, J.-H., Kang, H. & Pérez, J.** (2020), *Spanish Pre-Trained BERT Model and Evaluation Data* (BETO), PML4DC @ ICLR 2020. Repositorio `https://raw.githubusercontent.com/dccuchile/beto/master/README.md` `[VERIFICADA · 2026-08-29]`; el preprint `[VERIFICAR URL]`. Identificadores exactos: `dccuchile/bert-base-spanish-wwm-uncased` y `-cased`. · *clase 9*
- **Pérez, J. M. et al.**, *pysentimiento: A Python toolkit for Sentiment Analysis and Social NLP tasks* — sentimiento, emoción, ironía y discurso de odio en castellano (modelo base RoBERTuito, entrenado en tuits, con variantes rioplatenses). Repositorio `https://raw.githubusercontent.com/pysentimiento/pysentimiento/master/README.md` `[VERIFICADA · 2026-08-29]`; paquete `https://pypi.org/project/pysentimiento/` `[VERIFICADA · 2026-08-29]`. **Sus propios números: 70,2 de macro-F1 en sentimiento en castellano.** · *clase 9*
- **spaCy** — tokenización, lematización y entidades en castellano hechas en serio. `https://pypi.org/project/spacy/` `[VERIFICADA · 2026-08-29]` · *clase 6*
- **gensim** — la biblioteca clásica para entrenar word2vec sobre tu propio corpus. `https://pypi.org/project/gensim/` `[VERIFICADA · 2026-08-29]` · *clase 6*
- **`transformers`** (Hugging Face) — la biblioteca de la clase 9. `https://pypi.org/project/transformers/` `[VERIFICADA · 2026-08-29]` · *clase 9*
- **PyTorch** — la biblioteca de las clases 4 a 8. `https://pypi.org/project/torch/` `[VERIFICADA · 2026-08-29]` · *clases 4-8*

---

## Fuentes de datos (citarlas siempre que se muestren los datos)

Detalle completo, licencias y trampas en **`datos/README.md`**.

| Corpus | Fuente | Licencia | Verificado |
|---|---|---|---|
| Discursos de apertura de sesiones (Argentina, 1854-2019) | `github.com/lucariel/discursos_presidenciales` | **sin licencia declarada**; los textos son actos oficiales | `[VERIFICADA · 2026-08-29]` vía `raw.githubusercontent.com/…/README.md` |
| Discursos de Casa Rosada (2015-2024) | `github.com/jmdieguez/discursos` | **sin licencia declarada** | `[VERIFICADA · 2026-08-29]` vía `raw.githubusercontent.com/…/README.md` |
| Fake News Corpus Spanish (FakeDeS @ IberLEF 2021) | `github.com/jpposadas/FakeNewsCorpusSpanish` | **CC BY 4.0** | `[VERIFICADA · 2026-08-29]` vía `raw.githubusercontent.com/…/README.md` |
| Fashion-MNIST | Zalando Research | **MIT** | `[VERIFICADA · 2026-08-29]` |
| **Aguasclaras** | **sintético, generado para este curso** | del curso, usalo | — |

Citas formales de los corpus:

- **Ariel, L.** — *discursos_presidenciales*: recopilación y digitalización de los mensajes presidenciales de apertura de sesiones al Congreso de la Nación Argentina. Sin licencia declarada. `[VERIFICADA · 2026-08-29]`
- **Gómez-Adorno, H., Posadas-Durán, J. P., Bel-Enguix, G. & Porto-Capetillo, C.** (2021), *Overview of FakeDeS at IberLEF 2021: Fake News Detection in Spanish Shared Task*, Procesamiento del Lenguaje Natural 67, 223-231. **CC BY 4.0.** `[VERIFICAR URL]` — el repositorio del corpus sí abre `[VERIFICADA · 2026-08-29]` · *clases 4, 9, 10*
- **Xiao, H., Rasul, K. & Vollgraf, R.** (2017), *Fashion-MNIST: a Novel Image Dataset for Benchmarking Machine Learning Algorithms* (arXiv:1708.07747), Zalando Research. **MIT.** `https://raw.githubusercontent.com/zalandoresearch/fashion-mnist/master/README.md` `[VERIFICADA · 2026-08-29]` · *clase 5*

> **Pendiente para el docente (bloqueante si el curso se publica).** Los **dos**
> corpus de discursos no declaran licencia en sus repositorios. Los textos fuente
> son actos oficiales del Estado argentino, así que el uso educativo es
> defendible, pero **hay que escribirles a los recopiladores** (Lucas Ariel y el
> del repositorio `jmdieguez/discursos`) antes de publicar. Es la trampa 13 de
> `_shared/especificaciones/00-ESTADO-ESPINA.md` y sigue abierta.

---

## Citas que se revisaron y quedaron con una advertencia

Este curso enseña a no inventar. Lo que sigue es lo que encontramos al auditar la
bibliografía entera y no pudimos cerrar:

- **Bercholc, J. & Bercholc, D.** (2012), *Los discursos presidenciales en la
  Argentina democrática* — se cita en los `referencias.md` de las clases 1, 2 y 4
  como inspiración de la serie de menciones. **No se pudo confirmar la cita
  exacta** (título, editorial y año) desde este entorno, y ninguna afirmación del
  curso depende de ella. `[VERIFICAR — cita no confirmada]`
  **Si quien tenga red no la encuentra, se saca**: es la única entrada de esta
  bibliografía en esa situación.
- Ninguna otra referencia se eliminó por sospecha de invención. Los 66 títulos
  tienen autores, año y publicación completos y verificables; lo que falta son
  los enlaces, no los datos.

---

## Estado de las URLs (medido con `curl` el 2026-08-29, no supuesto)

| Host | Estado | Consecuencia |
|---|---|---|
| `raw.githubusercontent.com` | **200** | Por acá entran todos los datos reales del curso y **28 de las 28 URLs verificadas** de esta bibliografía. |
| `pypi.org`, `files.pythonhosted.org` | **200** | `pip install` funciona; las páginas de paquete sirven como cita verificable. |
| `registry.npmjs.org` | **200** | — |
| `github.com` (páginas HTML) | **403** | No se pueden verificar los repos desde acá, sólo los archivos crudos. |
| `huggingface.co` | **sin conexión** | **Las clases 9 y 10 necesitan HF en el aula.** Ver el plan B en `datos/README.md` §3. |
| `arxiv.org`, `doi.org`, YouTube, Wikipedia, `distill.pub`, `deeplearningbook.org`, `neuralnetworksanddeeplearning.com`, `3blue1brown.com`, `jalammar.github.io`, `transformer-circuits.pub`, sitios de editoriales | **sin conexión o 403** | De ahí salen todas las marcas `[VERIFICAR URL]`. |

**Tarea abierta para quien tenga red** (media hora de trabajo, y es lo único que
le falta a este archivo):

1. Abrir cada `[VERIFICAR URL]`, pegar el enlace y cambiar la marca a
   `[VERIFICADA · aaaa-mm-dd]`, **acá y en el `referencias.md` de la clase**.
2. Confirmar o descartar la única cita marcada `[VERIFICAR — cita no confirmada]`.
3. Si una obra no aparece, **se saca la cita en vez de inventarle un enlace**.
