# Recursos prácticos de PyTorch que repasan las clases 1 a 4 (línea → red → descenso de gradiente → bucle de PyTorch → sobreajuste)

Researched 2026-11-05. "Verified" means the URL returned HTTP 200 and its content was checked this session, either by WebFetch or by downloading the notebook and listing its section headings or API calls. YouTube titles, channels, durations and publish dates come from YouTube's oEmbed endpoint and the watch-page metadata.

## Q1: Which single resource best mirrors the course path (same dataset: line → network → gradient descent → PyTorch loop → overfitting)?

### Takeaway
No single free resource covers the whole path. The closest is Daniel Godoy's *PyTorch Step-by-Step*, chapters 0–1 (and 2). It uses one synthetic line dataset (y = 1 + 2x + noise) for everything: manual gradient descent in five named steps, then NumPy, then tensors, autograd, optimizer, `nn.MSELoss`, `nn.Linear` and `nn.Sequential`, then a train/validation split. The notebooks open in Colab. It has no ReLU network and no early stopping, and the Spanish edition is paid. Daniel Bourke's learnpytorch.io chapters 01+02 are the best free English alternative. Chapter 01 fits a straight line with a train/test loop and loss curves. Chapter 02 shows that a linear model fails on non-linear data and adds `nn.ReLU`.

### Cited Findings
**A. Daniel Godoy, "Deep Learning with PyTorch Step-by-Step" (Part I), notebooks Chapter00 and Chapter01 (EN, Colab)**
- The repository has an "Open in Colab" link for every chapter: Chapter 0 "Visualizing Gradient Descent", Chapter 1 "A Simple Regression Problem", Chapter 2 "Rethinking the Training Loop" and Chapter 3 "A Simple Classification Problem" — [GitHub dvgodoy/PyTorchStepByStep](https://github.com/dvgodoy/PyTorchStepByStep)
  - Colab: https://colab.research.google.com/github/dvgodoy/PyTorchStepByStep/blob/master/Chapter00.ipynb and …/Chapter01.ipynb (the raw .ipynb files return HTTP 200)
- Chapter01 notebook section headings, checked by downloading the notebook: Synthetic Data Generation → Gradient Descent "Step 0: Random Initialization … Step 1: Compute Model's Predictions … Step 2: Compute the Loss … Step 3: Compute the Gradients … Step 4: Update the Parameters … Step 5: Rinse and Repeat!" → Linear Regression in Numpy → PyTorch Tensor → Creating Parameters → Autograd (backward, grad, zero_, no_grad) → Dynamic Computation Graph → Optimizer (step / zero_grad) → Loss → Model (parameters, state_dict, forward, train) → Nested Models → Sequential Models → Putting It All Together — [Chapter01.ipynb](https://github.com/dvgodoy/PyTorchStepByStep/blob/master/Chapter01.ipynb)
- API counts in Chapter01: `nn.Linear` 7, `nn.Sequential` 4, `MSELoss` 5, `optim.SGD` 5, `requires_grad` 37, `nn.ReLU` 0, `optim.Adam` 0. Chapter 02 adds `DataLoader` (9 mentions), evaluation and saving with `torch.save` — [Chapter02.ipynb](https://github.com/dvgodoy/PyTorchStepByStep/blob/master/Chapter02.ipynb)
- Caveats: the first code cell detects Colab, downloads `config.py` from the repo and imports helper modules such as plots and data_generation. The extra setup works but may confuse students. Chapter 2 moves quickly to DataLoader, TensorBoard, and a `StepByStep` class in Chapter 2.1.
- **Single-notebook condensed version (EN, Colab):** "A Beginner-Friendly PyTorch Tutorial: Build and Train Your First Model" (Hugging Face blog, 20 Jan 2025, D. V. Godoy). It uses synthetic y = 1 + 2x + noise with 100 points split 80 train / 20 validation. It covers manual MSE gradients in NumPy, autograd (`backward`, `zero_`, `no_grad`), `nn.Linear(1,1)` in a custom class and then in `Sequential`, `nn.MSELoss`, `optim.SGD`, a training-step helper, a `DataLoader`, a `random_split` train/val split, and a validation loop under `no_grad()`/`eval()`. Losses are collected but **not plotted** — [HF blog](https://huggingface.co/blog/dvgodoy/beginner-pytorch-tutorial)
  - Colab: https://colab.research.google.com/github/dvgodoy/AccompanyingNotebooks/blob/main/A%20Beginner-Friendly%20PyTorch%20Tutorial.ipynb (raw file HTTP 200)
- **Spanish edition (paid):** "Aprendizaje Profundo con PyTorch Paso a Paso – Volumen I: Fundamentos", Leanpub, pay-what-you-want with a US$9.95 minimum and $14.95 suggested; a free sample is available. Its table of contents: Cap. 0 "Visualizando el Descenso de Gradiente" (pasos 0–5); Cap. 1 "Un Problema Sencillo de Regresión" (Regresión Lineal en Numpy, PyTorch, Autograd, Grafo Computacional Dinámico, Optimizador, Pérdida, Modelo); Cap. 2 "Repensar el Bucle de Entrenamiento" (Dataset, DataLoader, Evaluación, TensorBoard, Guardar y Cargar Modelos) — [Leanpub pytorch_ES](https://leanpub.com/pytorch_ES). The page does not say whether the notebooks themselves are translated.

**B. Daniel Bourke, learnpytorch.io "01. PyTorch Workflow Fundamentals" (EN, Colab, free)**
- Synthetic straight line (weight 0.7, bias 0.3, X from 0 to 1 in steps of 0.02, 50 points) with an 80/20 train/test split (40 and 10 points) and a plotting helper. Model is an `nn.Module` subclass with hand-made `nn.Parameter` weight and bias. Uses `nn.L1Loss` (MAE, **not MSE**) and `torch.optim.SGD(lr=0.01)`, a 100-epoch training and test loop, **train/test loss curves are plotted**, and `torch.inference_mode()` — [learnpytorch.io/01](https://www.learnpytorch.io/01_pytorch_workflow/)
- Section headings, checked in the notebook: 1 Data / Split data into training and test sets; 2 Build model; 3 Train model (loss function and optimizer; optimization loop); 4 Inference; 5 Saving and loading a model's `state_dict()`; 6 Putting it all together (6.2 "Building a PyTorch linear model" uses `nn.Linear`) — [01_pytorch_workflow.ipynb](https://github.com/mrdbourke/pytorch-deep-learning/blob/main/01_pytorch_workflow.ipynb). Colab badge on page.
- Video: the chapter is part of "Learn PyTorch for deep learning in a day. Literally." (Daniel Bourke, YouTube). The full video runs about 25.6 h; the page links chapter 01 at t=15419 s (about 4 h 17 min in) — [YouTube Z_ikDlimN6A](https://www.youtube.com/watch?v=Z_ikDlimN6A?t=15419)
- **Chapter 02 complements it.** Its section headings include "5.1 Preparing data to see if our model can model a straight line", "5.2 Adjusting model_1 to fit a straight line", "6. The missing piece: non-linearity", "6.2 Building a model with non-linearity" and "7. Replicating non-linear activation functions". The notebook uses `nn.ReLU` (6 mentions) and `nn.Sequential` (9). The main dataset is `make_circles` **classification**, not regression — [learnpytorch.io/02](https://www.learnpytorch.io/02_pytorch_classification/), [02 notebook](https://github.com/mrdbourke/pytorch-deep-learning/blob/main/02_pytorch_classification.ipynb)
- Caveats: it builds models as classes from the start, and a lot of time goes to boilerplate such as device handling and `inference_mode`. It uses MAE loss where the course uses MSE. No early stopping, though section 5 shows saving and loading a `state_dict`.

### Inferences
- For a "recover class 4" assignment: Godoy Ch.01 (or the single HF notebook) for line → gradient descent → autograd → `nn.Linear`/`MSELoss`/SGD, then Bourke Ch.01 section 3 for the train/test loop with loss curves, then Bourke Ch.02 sections 5–6 for "a line can't fit curves; add ReLU". None of them covers early stopping by saving the best weights. That piece has to come from course material or a short addition.

### Gaps
- I found no free resource that combines a tiny ReLU regression network, MSE, Adam, a train/val/test split by index selection, and early stopping on a single dataset.

## Q2: Official PyTorch tutorials ("Learn the Basics", "Learning PyTorch with Examples"): fit and Colab availability

### Takeaway
"Learning PyTorch with Examples" follows the course's progression closely (NumPy by hand → tensors → autograd → `nn.Sequential` + `MSELoss` → `optim`) and runs in Colab. It fits sin(x) with a cubic polynomial rather than a line or ReLU net, and it is dense text. "Learn the Basics" is useful only in pieces (Tensors, Autograd); its Optimization page uses FashionMNIST, DataLoader and an nn.Module class.

### Cited Findings
- **Learning PyTorch with Examples** fits y = sin(x) on [-π, π] with a third-order polynomial (4 coefficients) by gradient descent on squared error. Sections: NumPy warm-up with gradients computed by hand → PyTorch tensors (manual) → Autograd (`requires_grad`, `loss.backward()`, plus a custom `autograd.Function` with a Legendre polynomial) → nn module (`nn.Sequential` of Linear + Flatten, `nn.MSELoss`, custom `nn.Module`, dynamic control flow and weight sharing) → optim (RMSprop, SGD with momentum). It has a "Run in Google Colab" link, and the page itself calls it an older tutorial and points to "Learn the Basics" — [docs.pytorch.org pytorch_with_examples](https://docs.pytorch.org/tutorials/beginner/pytorch_with_examples.html)
- **Learn the Basics – Optimization**: FashionMNIST via torchvision, `DataLoader(batch_size=64)`, an `nn.Module` class with Flatten + 3 Linear + ReLU, and `CrossEntropyLoss`. It explains that `optimizer.zero_grad()` resets gradients because they accumulate, then `loss.backward()` and `optimizer.step()`; it mentions `nn.MSELoss` for regression. Has a "Run in Google Colab" button — [optimization_tutorial](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- Learn the Basics – Tensors and Autograd pages load (HTTP 200) — [tensorqs](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html), [autogradqs](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html). (I did not re-read their content this session; from prior knowledge, Autograd covers `requires_grad`, `backward`, `.grad`, `torch.no_grad`/`detach`, and an optional note on gradient accumulation. Spot-check before assigning.)
- The official "Introduction to PyTorch – YouTube Series" (English videos with companion notebooks covering tensors, autograd, building models and training) loads — [introyt index](https://docs.pytorch.org/tutorials/beginner/introyt/introyt_index.html). I found no Spanish dub or subtitles.

### Inferences
- For non-programmers, the best official assignment is the Tensors and Autograd pages (selected sections) plus "Learning PyTorch with Examples" read only up to the `nn` + `optim` sections. Tell students to skip the custom autograd Function, Legendre polynomial and weight-sharing parts.

### Gaps
- I did not measure section lengths or reading times for the official tutorials.

## Q3: Other English candidates (Raschka, d2l.ai, Karpathy, freeCodeCamp/Jovian, fast.ai)

### Takeaway
Raschka's "PyTorch in One Hour" is a good, recent text recap of tensors, autograd and the training loop, but it targets LLM learners: it uses classification, `Dataset`/`DataLoader` and multi-GPU sections, and has no notebook link. d2l.ai depends on its own `d2l` wrapper classes. Karpathy's micrograd video is excellent but runs 2 h 26 min and is about building autograd, not using PyTorch. The freeCodeCamp/Jovian linear-regression video is a 2 h 5 min livestream from 2020.

### Cited Findings
- **Raschka, "PyTorch in One Hour"** (1 Jul 2025). Sections: tensors (`.shape`, `.reshape`/`.view`, `.T`, `@`), computation graphs, autograd (`requires_grad`, `.grad`, `.backward()`), `nn.Module` MLP plus `Sequential` and `torch.no_grad()`, a custom `Dataset` and `DataLoader`, a training loop (SGD, cross-entropy, 3 epochs, `zero_grad`/`backward`/`step`), `state_dict` saving, and GPU and DDP training. No tutorial-specific notebook or Colab link on the page — [sebastianraschka.com/teaching/pytorch-1h](https://sebastianraschka.com/teaching/pytorch-1h/)
- **d2l.ai 3.4 "Linear Regression Implementation from Scratch"**: synthetic data (w = [2, −3.4], b = 4.2) built with `d2l.SyntheticRegressionData`, `d2l.Module`, `d2l.Trainer`, `@d2l.add_to_class`, and a custom SGD. Has Colab links for PyTorch, MXNet, JAX and TF. The wrapper classes hide the raw PyTorch API — [d2l.ai linear-regression-scratch](https://d2l.ai/chapter_linear-regression/linear-regression-scratch.html). The concise version also loads — [linear-regression-concise](https://d2l.ai/chapter_linear-regression/linear-regression-concise.html)
- **Karpathy, "The spelled-out intro to neural networks and backpropagation: building micrograd"**: 8,752 s (about 2 h 26 min), published 16 Aug 2022 — [YouTube VMj-3S1tku0](https://www.youtube.com/watch?v=VMj-3S1tku0)
- **freeCodeCamp, "Deep Learning with PyTorch Live Course – Tensors, Gradient Descent & Linear Regression (Part 1 of 6)"**: 7,524 s (about 2 h 5 min), published 23 May 2020 — [YouTube vo_fUOk-IKk](https://www.youtube.com/watch?v=vo_fUOk-IKk). Its companion Jovian notebook "02-linear-regression" loads (HTTP 200) — [jovian.com/aakashns/02-linear-regression](https://jovian.com/aakashns/02-linear-regression). According to a search snippet, Jovian notebooks offer "Run on Colab". Jovian's long-term availability is uncertain.

### Inferences
- Of these, use Raschka sections 2–4 and 7 only as optional reading for stronger students. Recommend micrograd only as an optional "why does backward() work" video. Avoid d2l for this audience because of its wrapper classes.

### Gaps
- fast.ai: not verified this session, so it is unconfirmed whether a current lesson notebook fits. From memory, Lesson 3 "How does a neural net really work?" builds ReLUs and gradient descent in a spreadsheet and a Kaggle notebook, but this needs checking.

## Q4: Spanish-language practical resources

### Takeaway
Spanish material is thin. I found no Spanish translation of d2l: es.d2l.ai does not resolve and github.com/d2l-ai/d2l-es returns 404. The usable options are two older YouTube intros (DotCSV Lab, 2020, 69 min livestream; Atecnea, 2023, 20 min), a partially paywalled Platzi course with short lessons, and Godoy's paid Spanish book, which mirrors the course path best.

### Cited Findings
- **DotCSV Lab, "HORA 5 – ¡Introducción a PyTorch! (Parte 1) – #100HorasDeML"**: Spanish (Spain), 4,157 s (about 69 min), published 22 Mar 2020; a livestream format — [YouTube 5YyDu5rO3kE](https://www.youtube.com/watch?v=5YyDu5rO3kE). Description and contents not retrievable; search snippet says it works from the docs and covers the basics.
- **Atecnea, "Introducción a Pytorch pt.1"**: Spanish, 1,228 s (about 20 min), published 23 Jan 2023 — [YouTube 8z_nCLy4WHc](https://www.youtube.com/watch?v=8z_nCLy4WHc). Content not verified beyond the title.
- **Platzi, "Curso de Redes Neuronales con PyTorch"**, lesson 8/24 "Regresión lineal desde cero en PyTorch": Spanish, 12:07 video. Covers `nn.Module`, `nn.Parameter`, `forward`, `manual_seed`, `state_dict()` and `inference_mode`. This lesson plays for free but most others say "Suscríbete para ver más"; no Colab link on the page and no instructor named — [Platzi lesson](https://platzi.com/cursos/pytorch/regresion-lineal-desde-cero-en-pytorch/). Related lessons: [Entrenamiento y visualización de pérdida](https://platzi.com/cursos/pytorch/entrenamiento-y-visualizacion-de-perdida/) and [Bucle de entrenamiento con SGD](https://platzi.com/cursos/pytorch/bucle-de-entrenamiento-con-sgd-en-pytorc/) (pages found via search; access not checked individually). The structure looks closely modeled on Bourke's chapter 01 (L1/inference_mode/state_dict). That is an inference.
- **Godoy, Spanish book** (paid, Leanpub): see Q1 — [Leanpub pytorch_ES](https://leanpub.com/pytorch_ES)
- learnpytorch.io can be read in Spanish through Google Translate, which is machine translation (search result: [translate.google.com proxy of learnpytorch.io](https://translate.google.com/translate?u=https%3A%2F%2Fwww.learnpytorch.io%2F&hl=es&sl=en&tl=es&client=srp)). Code cells stay in English.
- Google's ML Crash Course has Spanish (es-419) exercises, but they are not PyTorch — [developers.google.com MLCC ejercicios](https://developers.google.com/machine-learning/crash-course/exercises?hl=es-419)

### Inferences
- For a Rioplatense audience, a practical option is an English Colab notebook (Godoy HF notebook or Bourke 01) with machine-translated text or a course-made Spanish wrapper, plus at most one short Spanish video (Atecnea, 20 min) as orientation. The DotCSV stream is long and from 2020; PyTorch basics haven't changed much, but it is a live stream rather than a targeted lesson.

### Gaps
- I found no Spanish university GitHub repo with Colab-ready PyTorch intro notebooks in the searches (two searches). One may exist; a targeted GitHub search ("pytorch" "regresión" language:Spanish) was not done.
- Contents of the DotCSV and Atecnea videos were not verified, because YouTube pages returned only metadata.

## Q5: Which resources open directly in Colab, and summary table

### Takeaway
Godoy's notebooks, Bourke's notebooks, the official PyTorch tutorials and d2l open in Colab with one click. Raschka's page and the Platzi lessons do not have a Colab link.

### Cited Findings
| # | Resource | Lang | Format | Length | Colab? | Covers | Caveats |
|---|---|---|---|---|---|---|---|
| 1 | Godoy HF "Beginner-Friendly PyTorch Tutorial" ([blog](https://huggingface.co/blog/dvgodoy/beginner-pytorch-tutorial)) | EN | text + notebook | 1 notebook | Yes | NumPy GD, autograd, no_grad, nn.Linear, Sequential, MSELoss, SGD, train/val split | DataLoader/random_split; no plot of curves; no ReLU |
| 2 | Godoy Ch00–01 ([repo](https://github.com/dvgodoy/PyTorchStepByStep)) | EN (book ES paid) | notebooks | 2 chapters | Yes | 5-step GD, NumPy, tensors, autograd, optimizer, loss, model, Sequential | helper/config setup cell; no ReLU |
| 3 | Bourke 01 Workflow ([page](https://www.learnpytorch.io/01_pytorch_workflow/)) | EN | text + notebook + video | ~25.6 h full video; chapter is one section | Yes | line data, train/test split, SGD, train/test loop, loss-curve plot, state_dict save/load, nn.Linear (sec. 6) | nn.Module classes; L1 loss; inference_mode |
| 4 | Bourke 02 sec. 5–6 ([page](https://www.learnpytorch.io/02_pytorch_classification/)) | EN | text + notebook | sections | Yes | line→non-linearity, nn.ReLU, nn.Sequential | classification (circles), not regression |
| 5 | PyTorch "Learning PyTorch with Examples" ([page](https://docs.pytorch.org/tutorials/beginner/pytorch_with_examples.html)) | EN | text + notebook | — | Yes | NumPy manual grads → tensors → autograd → nn.Sequential + MSELoss → optim | cubic fit to sin; dense; advanced detours |
| 6 | PyTorch Learn the Basics: Tensors, Autograd ([tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html), [autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)) | EN | text + notebook | — | Yes | tensor ops, requires_grad/backward/grad/no_grad | Optimization page jumps to FashionMNIST + DataLoader |
| 7 | Raschka "PyTorch in One Hour" ([page](https://sebastianraschka.com/teaching/pytorch-1h/)) | EN | text | ~1 h | No link | tensors, autograd, nn.Module, training loop, save | classification, Dataset/DataLoader, GPU/DDP |
| 8 | Atecnea "Introducción a Pytorch pt.1" ([video](https://www.youtube.com/watch?v=8z_nCLy4WHc)) | ES | video | 20 min | ? | intro (unverified) | content unverified |
| 9 | DotCSV Lab "HORA 5 Introducción a PyTorch" ([video](https://www.youtube.com/watch?v=5YyDu5rO3kE)) | ES (Spain) | livestream | 69 min | ? | basics (unverified) | 2020, long |
| 10 | Platzi lesson ([page](https://platzi.com/cursos/pytorch/regresion-lineal-desde-cero-en-pytorch/)) | ES | video | 12 min | No | nn.Module linear regression, state_dict | mostly paywalled |
| — | Karpathy micrograd ([video](https://www.youtube.com/watch?v=VMj-3S1tku0)) | EN | video | 2 h 26 min | n/a | how backprop works from scratch | too long; optional |

### Inferences
- A short recommended path: (1) Godoy HF notebook (or Ch01), which covers classes 2–3 plus PyTorch autograd/nn/optim on a line; (2) Bourke 01 section 3, the loop with train/test loss curves; (3) Bourke 02 sections 5–6, adding ReLU; (4) the PyTorch Autograd page for no_grad and gradient accumulation; (5) optionally Atecnea's 20-min video in Spanish.

### Gaps
- None of the resources covers early stopping by saving the best weights (`copy.deepcopy(model.state_dict())`). Adam is also missing from the core picks: Bourke 01 mentions `optim.Adam` once, and the Godoy notebooks have none.
