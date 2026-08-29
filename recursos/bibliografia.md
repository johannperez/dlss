# Bibliografía del curso

La lista consolidada de todo lo que se cita en las diez clases, sin repetir. Cada
`referencias.md` de clase es un subconjunto de esto, con el comentario específico
de por qué se lee **ahí**.

## Cómo leer las marcas

| Marca | Qué quiere decir |
|---|---|
| `[VERIFICADA]` | Alguien abrió la URL y funcionaba. Se anota la fecha. |
| `[VERIFICAR URL]` | La obra existe y está bien citada, **pero nadie chequeó el enlace todavía**. |
| `[VERIFICAR]` | Falta chequear algún dato de la cita (año, revista, número). |

> **Por qué hay tantas `[VERIFICAR]`.** El contenedor donde se construyó este
> repo tiene casi toda la red bloqueada: sólo llegan `pypi.org`,
> `files.pythonhosted.org`, `registry.npmjs.org` y `raw.githubusercontent.com`.
> No se puede abrir `arxiv.org`, `huggingface.co`, `doi.org`, YouTube ni las
> páginas HTML de GitHub. **Poner una URL sin haberla abierto sería inventarla**,
> y este es un curso sobre no inventar. Así que las citas están completas
> (autor, año, título, publicación) y los enlaces quedan marcados para que
> alguien con red los complete. Ver la sección "Estado de las URLs" al final.

---

## 1. Deep learning explicado con dibujos (para el estudiante)

- **3Blue1Brown**, serie *Essence of Calculus*, cap. 1 — intuición visual de función. Subtítulos en español. `[VERIFICAR URL]` · *clase 1*
- **3Blue1Brown**, *But what is a neural network?* — se anuncia en la clase 1 y se recomienda mirarlo **después de la clase 2**. `[VERIFICAR URL]` · *clases 1, 2*
- **3Blue1Brown**, *Gradient descent, how neural networks learn* (cap. 2 de la serie). `[VERIFICAR URL]` · *clase 3*
- **3Blue1Brown**, capítulos sobre transformers y attention. `[VERIFICAR URL]` · *clase 7*
- **Nielsen, M.**, *Neural Networks and Deep Learning*, cap. 4: *A visual proof that neural nets can compute any function*. `[VERIFICAR URL]` · *clase 2*
- **TensorFlow Playground** — juguete en el navegador: poner capas y ver la figura que dibuja. `[VERIFICAR URL]` · *clase 2*
- **Jay Alammar**, *The Illustrated Word2vec*. `[VERIFICAR URL]` · *clase 6*
- **Jay Alammar**, *The Illustrated Transformer*. `[VERIFICAR URL]` · *clase 7*
- **Jay Alammar**, *The Illustrated GPT-2*. `[VERIFICAR URL]` · *clase 8*
- **Karpathy, A.**, *Let's build GPT: from scratch, in code, spelled out* (video) y el repo `nanoGPT`. **Es la fuente de las clases 7-8 y hay que citarla como tal.** `[VERIFICAR URL]` · *clases 7, 8*
- **Wolfram, S.**, *What Is ChatGPT Doing... and Why Does It Work?* — se recomiendan las primeras secciones. `[VERIFICAR URL]` · *clase 8*
- **Distill.pub**, *Why Momentum Really Works* — sólo para los muy curiosos. `[VERIFICAR URL]` · *clase 3*
- **Olah, C. et al.**, *Feature Visualization*, Distill.pub (2017). `[VERIFICAR URL]` · *clase 5*
- **StatQuest**, video sobre overfitting. `[VERIFICAR URL]` · *clase 4*
- **Severance, C.**, *Python para todos* (py4e), caps. 1-4, versión en castellano. `[VERIFICAR URL]` · *clase 1*
- **PyTorch**, tutorial oficial *Learn the Basics* (sólo las secciones que se usaron). `[VERIFICAR URL]` · *clase 4*
- **Hugging Face**, curso oficial de NLP, caps. 1-3 (hay versión en castellano). `[VERIFICAR URL]` · *clase 9*

## 2. Ciencias sociales computacionales (el marco del curso)

- **Grimmer, J., Roberts, M. & Stewart, B.** (2022), *Text as Data: A New Framework for Machine Learning and the Social Sciences*, Princeton University Press. **El libro de cabecera del curso.** `[VERIFICAR]` · *clases 1, 2, 5, 6, 9, 10*
- **Grimmer, J. & Stewart, B.** (2013), *Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts*, Political Analysis 21(3). `[VERIFICAR]` · *clases 9, 10*
- **Molina, M. & Garip, F.** (2019), *Machine Learning for Sociology*, Annual Review of Sociology 45. `[VERIFICAR]` · *clases 1, 2*
- **Breiman, L.** (2001), *Statistical Modeling: The Two Cultures*, Statistical Science 16(3). **Fundamenta el "camino A vs camino B" de la clase 1**, y es la mejor lectura para acompañar la incomodidad que deja la clase 2. `[VERIFICAR URL]` · *clases 1, 2*
- **Yarkoni, T. & Westfall, J.** (2017), *Choosing Prediction Over Explanation in Psychology*, Perspectives on Psychological Science. **La mejor lectura existente para traducir la distinción ajuste/predicción al vocabulario de las ciencias sociales; se asigna en la clase 4.** `[VERIFICAR]` · *clase 4*
- **Salganik, M. et al.** (2020), *Measuring the predictability of life outcomes with a scientific mass collaboration*, PNAS 117(15). 160 equipos, los mismos datos de panel, y **ninguno predijo bien**: pone en escala la lección de la clase 4 (a veces el fenómeno no es predecible, y eso también se reporta). `[VERIFICAR]` · *clases 4, 10*
- **Lundberg, I., Brand, J. E. & Jeon, N.** (2022), *Researcher reasoning meets computational capacity: Machine learning for social science*, Social Science Research 108. Cuándo el aprendizaje automático agrega algo a una pregunta social y cuándo es un adorno caro. `[VERIFICAR]` · *clases 4, 10*
- **Ziems, C. et al.** (2024), *Can Large Language Models Transform Computational Social Science?*, Computational Linguistics. `[VERIFICAR]` · *clase 8*
- **Barberá, P. et al.** (2021), *Automated Text Classification of News Articles: A Practical Guide*, Political Analysis. `[VERIFICAR]` · *clase 9*
- **Barrie, C., Palmer, A. & Spirling, A.** (2024), sobre reproducibilidad con LLMs en investigación. `[VERIFICAR]` · *clase 8*
- **Simon, H.** (1955), *A Behavioral Model of Rational Choice*, QJE — para fundamentar la discusión sobre elegir la función de pérdida. `[VERIFICAR]` · *clase 3*
- **Ragin, C. & Becker, H.** (eds.) (1992), *What Is a Case? Exploring the Foundations of Social Inquiry*, Cambridge University Press — la tradición del caso desviado es, dicha en el vocabulario de hoy, la decisión de darle mucho peso al outlier: MSE contra MAE. `[VERIFICAR]` · *clase 3*

## 3. Estudios empíricos que usamos como caso

- **Jean, N. et al.** (2016), *Combining satellite imagery and machine learning to predict poverty*, Science 353(6301). **Es el caso de la clase 5.** `[VERIFICAR]` · *clase 5*
- **Cantú, F.** (2019), *The Fingerprints of Fraud: Evidence from Mexico's 1988 Presidential Election*, American Political Science Review. `[VERIFICAR]` · *clase 5*
- **Torres, J. & Cantú, F.** (2022), sobre imágenes satelitales y visión por computadora en ciencia política. `[VERIFICAR]` · *clase 5*
- **Kozlowski, A., Taddy, M. & Evans, J.** (2019), *The Geometry of Culture: Analyzing the Meanings of Class through Word Embeddings*, American Sociological Review 84(5). `[VERIFICAR]` · *clase 6*
- **Garg, N., Schiebinger, L., Jurafsky, D. & Zou, J.** (2018), *Word embeddings quantify 100 years of gender and ethnic stereotypes*, PNAS 115(16). **El caso de "el sesgo como hallazgo".** `[VERIFICAR]` · *clases 6, 10*

## 4. Crítica, validez y ética

- **Bender, E., Gebru, T., McMillan-Major, A. & Shmitchell, S.** (2021), *On the Dangers of Stochastic Parrots*, FAccT. **Lectura fundamental del bloque de criterio**, a presentar con matices. `[VERIFICAR]` · *clases 8, 10*
- **Kapoor, S. & Narayanan, A.** (2023), *Leakage and the Reproducibility Crisis in ML-based Science*, Patterns. `[VERIFICAR]` · *clases 4, 10*
- **Jain, S. & Wallace, B.** (2019), *Attention is not Explanation*, NAACL. **Sustenta la advertencia contra la sobreinterpretación de la clase 7.** `[VERIFICAR]` · *clase 7*
- **Wiegreffe, S. & Pinter, Y.** (2019), *Attention is not not Explanation*, EMNLP — la réplica. Mencionar las dos es parte del punto. `[VERIFICAR]` · *clase 7*
- **Bolukbasi, T. et al.** (2016), *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*, NeurIPS. `[VERIFICAR]` · *clases 6, 10*
- **Rodriguez, P. & Spirling, A.** (2022), *Word Embeddings: What Works, What Doesn't, and How to Tell the Difference for Applied Research*, Journal of Politics. `[VERIFICAR]` · *clase 6*
- **Jacobs, A. Z. & Wallach, H.** (2021), *Measurement and Fairness*, FAccT '21. Pone nombre a la distancia entre el constructo que querés medir y el número que sale; **se cita ya en la clase 1** (el «% de palabras dedicadas a seguridad») y se cobra en la 10. `[VERIFICAR]` · *clases 1, 10*
- **Krippendorff, K.**, *Content Analysis: An Introduction to Its Methodology* — marco de fiabilidad entre codificadores (kappa, alpha). `[VERIFICAR]` · *clases 9, 10*
- **Liu, N. et al.** (2023), *Lost in the Middle: How Language Models Use Long Contexts*, TACL. `[VERIFICAR]` · *clase 8*

## 5. Técnico (para el docente, no para el aula)

- **Vaswani, A. et al.** (2017), *Attention Is All You Need*, NeurIPS. Se muestra la primera página, no se lee. `[VERIFICAR URL]` · *clase 7*
- **Goodfellow, I., Bengio, Y. & Courville, A.**, *Deep Learning*, MIT Press (gratis online). El cap. 6 (§6.1-6.4) es la versión formal de la clase 2. `[VERIFICAR URL]` · *clases 2, 3*
- **Hastie, T., Tibshirani, R. & Friedman, J.**, *The Elements of Statistical Learning*, cap. 7 (model assessment and selection). `[VERIFICAR URL]` · *clase 4*
- **Cybenko, G.** (1989), *Approximation by superpositions of a sigmoidal function*, MCSS 2(4). Sólo la referencia: **no se dicta el teorema.** `[VERIFICAR]` · *clase 2*
- **Hornik, K.** (1991), *Approximation capabilities of multilayer feedforward networks*, Neural Networks 4(2). `[VERIFICAR]` · *clase 2*
- **McCulloch, W. & Pitts, W.** (1943), *A Logical Calculus of the Ideas Immanent in Nervous Activity* — para la anécdota histórica del nombre "neurona". `[VERIFICAR]` · *clase 2*
- **Ouyang, L. et al.** (2022), *Training language models to follow instructions with human feedback*, NeurIPS. `[VERIFICAR]` · *clase 8*
- **Elhage, N. et al.**, *A Mathematical Framework for Transformer Circuits* — sólo para el docente. `[VERIFICAR URL]` · *clase 7*
- **Grinsztajn, L., Oyallon, E. & Varoquaux, G.** (2022), *Why do tree-based models still outperform deep learning on tabular data?*, NeurIPS. **Es la referencia honesta para decir "acá no uses deep learning".** `[VERIFICAR]` · *clases 5, 10*
- **Firth, J.R.** (1957), para la cita de la hipótesis distribucional. `[VERIFICAR]` · *clase 6*
- **Ruder, S.** (2016), *An overview of gradient descent optimization algorithms* — el recorrido más claro de SGD → momento → Adagrad → RMSprop → Adam, con la intuición antes de la fórmula. `[VERIFICAR URL]` · *clase 3*
- **Goh, G.** (2017), *Why Momentum Really Works*, Distill — por qué un valle alargado hace zigzaguear al descenso. Es la continuación de la última celda del notebook de la clase 3. `[VERIFICAR URL]` · *clase 3*
- **Stigler, S. M.** (1986), *The History of Statistics*, Harvard University Press, cap. 1 — de dónde sale que el MSE sea el default: tenía solución cerrada. La anécdota de la slide 8 de la clase 3. `[VERIFICAR]` · *clase 3*

## 6. Modelos y herramientas en castellano

- **Cañete, J. et al.** (2020), *Spanish Pre-Trained BERT Model and Evaluation Data* (BETO), PML4DC @ ICLR. `[VERIFICAR]` · *clase 9*
- **Pérez, J.M. et al.**, *pysentimiento* / *RoBERTuito* — análisis de texto en castellano. `[VERIFICAR]` · *clase 9*

---

## Fuentes de datos (citarlas siempre que se muestren los datos)

Detalle completo, licencias y trampas en **`datos/README.md`**.

| Corpus | Fuente | Licencia | Verificado |
|---|---|---|---|
| Discursos de apertura de sesiones (Argentina, 1854-2019) | `github.com/lucariel/discursos_presidenciales` | sin licencia declarada; los textos son actos oficiales | `[VERIFICADA]` vía `raw.githubusercontent.com` |
| Discursos de Casa Rosada (2015-2024) | `github.com/jmdieguez/discursos` | sin licencia declarada | `[VERIFICADA]` vía `raw.githubusercontent.com` |
| Fake News Corpus Spanish | `github.com/jpposadas/FakeNewsCorpusSpanish` | **CC BY 4.0** | `[VERIFICADA]` vía `raw.githubusercontent.com` |
| Fashion-MNIST | Zalando Research | MIT | `[VERIFICADA]` |
| **Aguasclaras** | **sintético, generado para este curso** | del curso | — |

> **Pendiente para el docente.** Los dos corpus de discursos no declaran licencia
> en sus repositorios. Los textos fuente son actos oficiales del Estado argentino,
> así que el uso educativo es defendible, pero **si el curso se publica hay que
> escribirle a los recopiladores**.

---

## Estado de las URLs (medido, no supuesto)

Chequeado con `curl` desde el contenedor de construcción:

| Host | Estado | Consecuencia |
|---|---|---|
| `raw.githubusercontent.com` | **200** | Por acá entran todos los datos reales del curso. |
| `pypi.org`, `files.pythonhosted.org` | **200** | `pip install` funciona. |
| `registry.npmjs.org` | **200** | — |
| `github.com` (páginas HTML) | **403** | No se pueden verificar los repos desde acá, sólo los archivos crudos. |
| `huggingface.co` | **sin conexión** | **Las clases 9 y 10 necesitan HF en el aula.** Ver el plan B en `datos/README.md` §3. |
| `arxiv.org`, `doi.org`, YouTube, Wikipedia | **sin conexión** | De ahí salen las marcas `[VERIFICAR URL]`. |

**Tarea abierta para quien tenga red:** abrir cada `[VERIFICAR URL]`, pegar el
enlace y cambiar la marca a `[VERIFICADA · aaaa-mm-dd]`, tanto acá como en el
`referencias.md` de la clase que la usa. Si una obra no aparece, **se saca la
cita en vez de inventarle un enlace.**
