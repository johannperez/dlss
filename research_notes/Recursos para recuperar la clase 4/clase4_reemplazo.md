# Recursos para recuperar la Clase 4 (ciclo de entrenamiento; dibujar vs calcar)

Verification method (2026-11-05): every YouTube video was checked through YouTube oEmbed (original title and channel) and through the watch page (`lengthSeconds`, publish date, caption tracks). Web pages were fetched with curl (HTTP 200 plus `<title>`) and/or WebFetch for content. "Verified" below means it loaded and its content matched the description.

## Q1: Spanish-language resources that explain the training loop, overfitting and train/val/test intuitively

### Takeaway
There is strong Spanish coverage for the concepts: overfitting (DotCSV, Codificando Bits), the train/val/test split (Codificando Bits), reading loss curves (Codificando Bits, 2026), gradient descent (DotCSV, the Spanish dub of 3Blue1Brown), and the whole "datasets, generalization, overfitting" module of Google's MLCC, which is officially translated (es-419). I found no beginner-friendly Spanish resource for the PyTorch training loop itself.

### Cited Findings
- **DotCSV, "Las Redes Neuronales... ¿Aprenden o Memorizan? - Overfitting y Underfitting - Parte 1".** 10:18, published 2019-01-19, Spanish (Spain). Description: "Uno de los conceptos más importantes ... cuando entrenes a tus modelos ... es el del Overfitting". Only auto-generated Spanish captions (a.es). — [YouTube](https://www.youtube.com/watch?v=7-6X3DTt3R8)
- **DotCSV, "Cómo identificar el OVERFITTING en tu RED NEURONAL - Parte 2".** 12:15, published 2019-03-10. Description: "te contaré uno de los métodos para poder identificarlo". — [YouTube](https://www.youtube.com/watch?v=ZmLKqZYlYUI)
- **DotCSV, "¿Qué es el Descenso del Gradiente? Algoritmo de Inteligencia Artificial".** 9:24, published 2018-02-04. Covers "la intuición detrás de este algoritmo". — [YouTube](https://www.youtube.com/watch?v=A6FiCDoz8_4)
- **Codificando Bits (Miguel Sotaquirá), "Los sets de entrenamiento, validación y prueba".** 10:33, published 2023-06-16. Chapters: parámetros e hiperparámetros (00:55), set de entrenamiento (03:06), set de validación (04:18), set de prueba (06:40). Latin American Spanish. — [YouTube](https://www.youtube.com/watch?v=79K93XBOsIg)
- **Codificando Bits, "¿Por qué mi Red Neuronal NO APRENDE?: las curvas de pérdida".** 19:11, published 2026-04-20. "cómo diagnosticar el entrenamiento de una Red Neuronal usando las curvas de pérdida". Chapters: repaso del entrenamiento (01:37), "¿Cómo 'leer' las curvas de pérdida?" (05:32–17:41). — [YouTube](https://www.youtube.com/watch?v=sEh39tFaoFQ)
- **Codificando Bits, "Underfitting y Overfitting en las Redes Neuronales".** 5:28, published 2019-08-27. Explains both behaviors and their link to "la complejidad del modelo". — [YouTube](https://www.youtube.com/watch?v=hBFff9l-AlE)
- **Codificando Bits, "Validación cruzada y k-fold cross-validation".** 12:45, published 2023-07-31. Chapters include capacidad de generalización (01:56), sets de train/val/test (02:50) and k-fold (04:30). — [YouTube](https://www.youtube.com/watch?v=bpZa2mAiXS8)
- **3Blue1Brown Español, "Descenso de Gradiente. Cómo Aprenden las Redes Neuronales | Aprendizaje Profundo. Capítulo 2".** 21:27, Spanish dub. Chapter 1, "¿Qué es una Red Neuronal?", also exists (about 20 min, 2020-09-21). — [Cap. 2](https://www.youtube.com/watch?v=mwHiaTrQOiI); [Cap. 1](https://www.youtube.com/watch?v=jKCQsndqEGQ)
- **Universidad de Oviedo (Grado en Ciencia e Ingeniería de Datos), "Aprendizaje Profundo - 3 - 10 - Parada temprana (Early Stopping)".** 9:25, published 2023-06-23. University lecture clip with a course page. — [YouTube](https://www.youtube.com/watch?v=kTK5eq6jmLc); [course page](https://pglez82.github.io/DeepLearningWeb/)
- **Google MLCC module "Conjuntos de datos, generalización y sobreajuste", officially in Spanish (es-419).** All of these returned HTTP 200 with Spanish titles:
  - [Módulo](https://developers.google.com/machine-learning/crash-course/overfitting?hl=es-419)
  - [Sobreajuste](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting?hl=es-419)
  - ["Conjuntos de datos: división del conjunto de datos original"](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets?hl=es-419)
  - ["Sobreajuste: Interpretación de curvas de pérdida"](https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves?hl=es-419)
  - ["Sobreajuste: Complejidad del modelo"](https://developers.google.com/machine-learning/crash-course/overfitting/model-complexity?hl=es-419)
- **What MLCC says, in its own Spanish text:**
  - On reusing the test set: "Cuanto más uses el mismo conjunto de prueba, más probabilidades habrá de que el modelo se ajuste estrechamente al conjunto de prueba. Al igual que un profesor que 'enseña para la prueba'..." This matches Clase 4's "test se toca una sola vez". — [MLCC división](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets?hl=es-419)
  - On model complexity: it uses Occam's razor and says "los modelos complejos superan a los simples en el conjunto de entrenamiento. Sin embargo, los modelos simples suelen tener un mejor rendimiento ... en el conjunto de prueba". It recommends starting with a simple baseline ("un modelo de referencia a partir de un par de atributos"). — [MLCC complejidad](https://developers.google.com/machine-learning/crash-course/overfitting/model-complexity?hl=es-419)
  - The English module page gives an estimated time of 105 minutes for the whole module. — [MLCC module (EN)](https://developers.google.com/machine-learning/crash-course/overfitting)
  - The loss-curves page has figures of an ideal curve, oscillation, spikes, and validation loss rising while training loss converges (Exercise 3 / Figure 23, labeled overfitting). Suggested fixes include a simpler model and more regularization. — [MLCC curvas](https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves)
- **MLCC "Regresión lineal: Hiperparámetros" (es-419).** Covers learning rate, batch size (SGD, mini-batch, full batch) and epochs, with loss-curve figures for too small and too large learning rates. It has multiple-choice checks but no interactive tool. — [MLCC hiperparámetros](https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters?hl=es-419)
- **MLCC "Regresión lineal: descenso de gradientes" (es-419)** also loads. — [MLCC descenso](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent?hl=es-419)
- **Other Spanish options found but not reviewed in depth:**
  - Codigo Maquina, "Ni muy muy, Ni tan tan: Subajuste y Sobreajuste" (20:34). — [YouTube](https://www.youtube.com/watch?v=cXLOZqWg01k)
  - Codigo Maquina, "Datos de Entrenamiento, Validación y Prueba" (about 27 min, 2021). — [YouTube](https://www.youtube.com/watch?v=vdYzm4xC7mc)
  - Ringa Tech, "Tu primera red neuronal en Python y Tensorflow" (16:25; TensorFlow/Keras, not PyTorch). — [YouTube](https://www.youtube.com/watch?v=iX_on3VxZzk)

### Inferences
- The Spanish core for students is: DotCSV Parte 1 (concept) → Codificando Bits sets (split) → Codificando Bits curvas de pérdida (reading curves) → MLCC es-419 pages (reading, with exercises).
- The DotCSV overfitting pair matches "dibujar vs calcar" closely in spirit: Parte 1 asks whether networks learn or memorize. Its title and description suggest Parte 2 covers identification via a validation set or curves, but I did not watch it to confirm.
- DotCSV and 3Blue1Brown cover gradient descent and the "knobs" intuition, which is the "why" behind `optimizer.step()`. They do not cover PyTorch code.
- MLCC's examples are mostly classification and linear models, and the complexity page discusses regularization (L2). That goes beyond Clase 4, so students should read selectively.

### Gaps
- I did not watch the videos. Content claims rest on titles, descriptions and chapter lists. In particular, whether DotCSV Parte 2 shows train vs validation curves is unconfirmed.
- I found no Spanish beginner video or notebook that walks through a PyTorch training loop (`zero_grad` / `backward` / `step`). YouTube searches in Spanish for PyTorch training-loop or regression tutorials returned nothing usable.
- Dive into Deep Learning has no Spanish edition: es.d2l.ai did not resolve.
- I did not find Spanish material on AIC/BIC aimed at this audience.

## Q2: The best English resources, and whether they have Spanish subtitles or translations

### Takeaway
StatQuest (bias/variance, cross-validation) and the MLU-Explain interactive essays are the best short, visual English options for overfitting, splits and cross-validation. TensorFlow Playground is a no-code toy that shows training vs test loss diverging. StatQuest has no human Spanish captions, only YouTube auto-translation. MLU-Explain and Playground are English only. The PyTorch official tutorial is English only and uses classification, not regression.

### Cited Findings
- **StatQuest, "Machine Learning Fundamentals: Bias and Variance".** 6:36, published 2018-09-17. Description: "two examples that make these concepts super easy to understand". Human caption tracks: English and pt-BR. No Spanish track, so Spanish would be YouTube auto-translate only. — [YouTube](https://www.youtube.com/watch?v=EuBBz3bI-aA)
  - Third-party summaries say it uses a mouse weight/height example, compares a straight line with a "squiggly line" and splits the data into training and testing. (Secondary source.) — [chaindesk summary](https://chaindesk.ai/tools/youtube-summarizer/machine-learning-fundamentals-bias-and-variance-EuBBz3bI-aA)
- **StatQuest, "Machine Learning Fundamentals: Cross Validation".** 6:05. Human caption tracks: en, pt, tr (no Spanish). — [YouTube](https://www.youtube.com/watch?v=fSytzGwwBVw)
- **MLU-Explain (Amazon; author Jared Wilber), "Train, Test, and Validation Sets".** Short interactive essay with a cats-vs-dogs toy example and draggable points. It says the validation set is for comparing models and hyperparameters, and warns that peeking at the test set early "is a form of overfitting"; the test set is for the final estimate only. — [MLU-Explain](https://mlu-explain.github.io/train-test-validation/)
- **MLU-Explain companion essays (both load, HTTP 200):**
  - "Bias Variance Tradeoff" — [MLU-Explain](https://mlu-explain.github.io/bias-variance/)
  - "Cross-Validation" — [MLU-Explain](https://mlu-explain.github.io/cross-validation/)
- **TensorFlow Playground, "A Neural Network Playground".** Browser toy with no code. The page includes the controls "Ratio of training to test data", "Noise", "Batch size", "Learning rate", "Epoch", a "Regression" problem type, and live "Training loss" / "Test loss" readouts. — [playground.tensorflow.org](https://playground.tensorflow.org/)
- **PyTorch official tutorial, "Learn the Basics → Optimizing Model Parameters".**
  - Covers hyperparameters (epochs, batch size, learning rate: 1e-3, 64, 10 epochs), loss, `torch.optim.SGD`, and the three steps `zero_grad()` / `backward()` / `step()`, with separate `train_loop` and `test_loop`.
  - Uses FashionMNIST classification (about 70% test accuracy), has a "Run in Google Colab" link, and is English only.
  - [PyTorch docs](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- **3Blue1Brown's neural network series** is available as an official Spanish dub (see Q1), so the English originals are not needed. — [3Blue1Brown Español Cap. 2](https://www.youtube.com/watch?v=mwHiaTrQOiI)

### Inferences
- For this audience, MLU-Explain plus TensorFlow Playground are probably the most "drawing machine" friendly. In Playground, a student can raise noise, lower the training ratio and add neurons, then watch test loss rise while training loss falls. That is "calcar" made visible, with no code. Caveat: the interface is English, though its few controls are easy to explain in one line each.
- For the PyTorch side, the official tutorial is a good reference for the loop's anatomy. Its classification and image data make it less like the class's 1-D regression, and it has no validation set.
- StatQuest's teaching style (cartoon plots, "squiggly line") fits the "formulas later or never" philosophy. The language barrier is the main caveat.

### Gaps
- I did not check fast.ai, Karpathy, Raschka or MIT 6.S191 in detail. Typical lectures in those courses run 45–90+ minutes and are pitched at programmers, so they are unlikely to suit this audience. This is a judgment, not verified per item.
- I did not confirm whether YouTube's auto-translate to Spanish is enabled on the StatQuest videos (it normally is when English captions exist).
- MLU-Explain has no Spanish translation that I could find.

## Q3: A single beginner video or notebook that walks through a PyTorch training loop for a tiny regression with train/test curves

### Takeaway
The closest match is Zero to Mastery's "01. PyTorch Workflow Fundamentals" (Daniel Bourke, learnpytorch.io): a straight-line regression with a full training loop, a test loop and train/test loss curves, with a Colab notebook. It is English only, uses a hand-written linear model rather than `nn.Linear` + ReLU, and has train/test but no validation set.

### Cited Findings
- **Zero to Mastery, "01. PyTorch Workflow Fundamentals" (learnpytorch.io).**
  - Data and model: a synthetic line (weight 0.7, bias 0.3, 50 points, 80/20 train/test split) fit with a custom `nn.Module`, using `nn.L1Loss` and `torch.optim.SGD(lr=0.01)` for 100 epochs.
  - Loop: forward → loss → `zero_grad()` → `loss.backward()` → `optimizer.step()`, plus a test loop under `torch.inference_mode()`.
  - Plots predictions before and after training, and training vs test loss curves against epochs.
  - Has a Colab badge, slides, a YouTube walkthrough, and a link to an "unofficial PyTorch optimization loop song" as a memory aid.
  - [learnpytorch.io](https://www.learnpytorch.io/01_pytorch_workflow/)
- **PyTorch "Optimizing Model Parameters"** is the official alternative: same loop anatomy, but classification on FashionMNIST. — [PyTorch docs](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)

### Inferences
- The learnpytorch.io page is long (more than 170k characters of text). Students should be pointed to the sections on building the model, the training loop and the loss-curve plot, not the whole page.
- Its straight-line regression is simpler than Clase 4's nonlinear 1-D regression. It shows the loop and the curves, but it cannot show overfitting, since a two-parameter line can't "calcar". Pair it with Playground or the DotCSV videos for the overfitting part.
- The course's own Clase 4 notebook is probably still the best "tiny nonlinear regression + train/val curves + early stopping" artifact. External resources mainly fill in the narration that was lost.

### Gaps
- I did not identify the exact URL or timestamp of the learnpytorch.io YouTube walkthrough for section 01. It is likely a segment of a much longer full-course video, which I did not verify.
- I found no resource in Spanish or English that combines all of the following in one short beginner piece: `nn.Sequential` + ReLU, a 1-D nonlinear regression, a train/val/test split, early stopping and honest reporting.
- I found no short, gentle resource on "honest reporting of a small experiment" or baselines specifically. MLCC's model-complexity page touches on baselines ("modelo de referencia").

## Q4: Exact URLs and durations (verification status)

### Takeaway
Every resource recommended above was verified to load and match its title. Video durations come from YouTube's `lengthSeconds` field. Suggested shortlist of 9: DotCSV P1, DotCSV P2, CB sets, CB curvas, MLCC es-419 (división + curvas + complejidad + hiperparámetros), MLU-Explain train/test/val, TF Playground, StatQuest Bias & Variance, learnpytorch.io 01. CB = Codificando Bits.

### Cited Findings

| # | Resource | Lang | Length | Clase 4 topics | Level | Source |
|---|---|---|---|---|---|---|
| 1 | DotCSV, ¿Aprenden o Memorizan? Overfitting y Underfitting P1 | ES (España) | 10:18 | overfitting vs generalization ("dibujar vs calcar"), capacity | gentle | [link](https://www.youtube.com/watch?v=7-6X3DTt3R8) |
| 2 | DotCSV, Cómo identificar el overfitting P2 | ES | 12:15 | detecting overfitting (likely via validation; unconfirmed) | gentle/intermediate | [link](https://www.youtube.com/watch?v=ZmLKqZYlYUI) |
| 3 | Codificando Bits, Los sets de entrenamiento, validación y prueba | ES (LatAm) | 10:33 | train/val/test, hyperparameters | gentle | [link](https://www.youtube.com/watch?v=79K93XBOsIg) |
| 4 | Codificando Bits, ¿Por qué mi red neuronal NO APRENDE?: las curvas de pérdida | ES (LatAm) | 19:11 (core 05:32–17:41) | training recap, reading loss curves | gentle/intermediate | [link](https://www.youtube.com/watch?v=sEh39tFaoFQ) |
| 5 | Google MLCC es-419: división de datos, curvas de pérdida, complejidad, hiperparámetros | ES (official translation) | module about 105 min total; individual pages shorter | split, test used once, loss curves, capacity/Occam, baseline, LR/batch/epoch | gentle, with quizzes | [división](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets?hl=es-419), [curvas](https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves?hl=es-419), [complejidad](https://developers.google.com/machine-learning/crash-course/overfitting/model-complexity?hl=es-419), [hiperparámetros](https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters?hl=es-419) |
| 6 | MLU-Explain, Train, Test, and Validation Sets (+ Bias-Variance, Cross-Validation) | EN | short interactive essay | split, why not peek at test, CV | gentle, visual | [link](https://mlu-explain.github.io/train-test-validation/) |
| 7 | TensorFlow Playground | EN UI (few words) | open-ended toy | capacity vs data, noise, train vs test loss, LR, batch, epochs | gentle, no code | [link](https://playground.tensorflow.org/) |
| 8 | StatQuest, Bias and Variance (+ Cross Validation 6:05) | EN (human captions en/pt; no es) | 6:36 | overfitting, train/test, complexity; CV | gentle | [B&V](https://www.youtube.com/watch?v=EuBBz3bI-aA), [CV](https://www.youtube.com/watch?v=fSytzGwwBVw) |
| 9 | learnpytorch.io, 01 PyTorch Workflow Fundamentals | EN | long page; use the loop and curves sections | the PyTorch loop (forward/loss/zero_grad/backward/step), epochs, LR, train/test loss curves | beginner coder | [link](https://www.learnpytorch.io/01_pytorch_workflow/) |
| opt | DotCSV, Descenso del Gradiente | ES | 9:24 | why turning the knobs works | gentle | [link](https://www.youtube.com/watch?v=A6FiCDoz8_4) |
| opt | 3Blue1Brown Español, Cap. 2 Descenso de gradiente | ES (dub) | 21:27 | gradient descent intuition | gentle-to-mid (some math) | [link](https://www.youtube.com/watch?v=mwHiaTrQOiI) |
| opt | Codificando Bits, Validación cruzada y k-fold | ES | 12:45 | CV (the brief mention) | gentle | [link](https://www.youtube.com/watch?v=bpZa2mAiXS8) |
| opt | U. Oviedo, Parada temprana (Early Stopping) | ES (España) | 9:25 | early stopping | intermediate (university lecture) | [link](https://www.youtube.com/watch?v=kTK5eq6jmLc) |
| opt | PyTorch, Optimizing Model Parameters | EN | short tutorial + Colab | loop anatomy, hyperparameters | beginner coder | [link](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) |

### Inferences
- The DotCSV and older Codificando Bits videos are from 2018–2019 but are about timeless concepts. Their code, where any appears, is likely Keras or TensorFlow rather than PyTorch.
- DotCSV speaks peninsular Spanish and Codificando Bits speaks Latin American Spanish. Both should be comfortable for Rioplatense students.

### Gaps
- I did not verify that the course's own "drawing machine with knobs" framing appears in any external resource (unlikely). The linking narrative will have to come from the instructor.
- AIC/BIC: I found no short, gentle resource and did not search deeply.
