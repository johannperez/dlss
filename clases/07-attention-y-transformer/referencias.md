# Referencias — Clase 7

**Attention: cada palabra arma su propio resumen del contexto**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la red
> bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. **Se probó con `curl` cada URL de esta lista.** Las que
> respondieron van marcadas `[VERIFICADA 2026-08-29]`; el resto va marcado
> `[VERIFICAR URL]`: las obras existen, están bien citadas y se encuentran buscando por
> título y autor, pero **nadie abrió el enlace**, y poner una URL sin haberla abierto
> sería inventarla. Éste es un curso sobre no inventar. Quien tenga red que las complete
> y las pase a `[VERIFICADA]` con la fecha.

---

## Si te quedaste con ganas

En el orden en que conviene leerlas.

**1. Jay Alammar, *The Illustrated Transformer*.** `[VERIFICAR URL]`
> **Leelo después de esta clase, no antes.** Es el mejor material visual que existe sobre
> transformers, y justamente por eso es peligroso como primera lectura: si lo abrís sin
> haber hecho el promedio ponderado a mano, te llevás dibujos lindos y ninguna intuición.
> Ahora que tenés dónde colgar cada pieza, va a cerrar todo lo que hoy quedó a medias,
> sobre todo la parte de multi-head y la de las dimensiones.
> Buscalo como «Jay Alammar Illustrated Transformer». Cuarenta minutos.

**2. 3Blue1Brown, capítulos sobre *attention* y transformers de la serie de deep
learning.** `[VERIFICAR URL]`
> La animación de qué le pasa geométricamente a un vector cuando le sumás el resumen del
> contexto es lo mejor que hay para entender **por qué** la salida de attention es «la
> misma palabra, contextualizada». Es el complemento visual de la sección 3 del notebook.
> Buscalo en el canal «3Blue1Brown», serie *Neural networks*, capítulos 5 y 6.
> Veinte minutos por capítulo, y se ven dos veces.

**3. Vaswani, A. et al. (2017). *Attention Is All You Need*. NeurIPS.**
`[VERIFICAR URL]` (el preprint es arXiv:1706.03762)
> **El paper.** Te lo recomendamos por una razón puntual: para que veas que es **corto**
> —ocho páginas— y que la introducción y la sección 3.2 se leen sin doctorado. No hace
> falta que entiendas la sección de resultados de traducción. El objetivo es
> desmitificar: la ecuación que vimos hoy está en la página 4, y ya la entendés.
> Media hora, salteando lo que no se entienda sin culpa.

**4. Karpathy, A., *Let's build GPT: from scratch, in code, spelled out*.**
`[VERIFICAR URL]` (el video). **El código sí está verificado:**
`https://raw.githubusercontent.com/karpathy/ng-video-lecture/master/gpt.py`
`[VERIFICADA 2026-08-29]`
> Es el video que estructura esta clase y la que viene. Construye exactamente lo que
> construimos hoy, en inglés, con otra base de datos (Shakespeare en vez de discursos
> parlamentarios) y llegando hasta el entrenamiento. **Si viste esta clase, el video se
> te va a hacer fácil**, y eso es un buen síntoma.
> Dos horas. Vale la pena aunque tu inglés sea regular: el código habla solo.

**5. Grimmer, J., Roberts, M. & Stewart, B. (2022). *Text as Data: A New Framework for
Machine Learning and the Social Sciences*. Princeton University Press.**
`[VERIFICAR URL]`
> El libro de cabecera de todo este módulo. Para hoy no hay un capítulo de transformers
> (el libro es anterior a que fueran rutina en ciencias sociales), pero sí está el marco
> que importa: qué se puede afirmar con un modelo de texto y qué hay que validar antes de
> afirmarlo. Leé la parte de **validación** con la clase de hoy en la cabeza.

---

## Si te vas a meter en serio

**6. Jain, S. & Wallace, B. (2019). *Attention is not Explanation*. NAACL.**
`[VERIFICAR URL]` (el preprint es arXiv:1902.10186). **El código sí está verificado:**
`https://raw.githubusercontent.com/successar/AttentionExplanation/master/README.md`
`[VERIFICADA 2026-08-29]`
> **Es el paper que sostiene las slides 34 y 35 y el ítem 11 del cuestionario.** El
> argumento es limpio y te lo podés llevar entero: construyen mapas de atención
> *adversarios* —muy distintos del original— que producen **casi la misma predicción**
> (dentro de un margen chico). Si dos mapas contradictorios dan casi la misma salida, el
> mapa no determina la salida y no puede explicarla por sí solo.
> **Un matiz al citarlo:** lo estudiaron sobre todo en atención aditiva encima de redes
> recurrentes (BiLSTM) para clasificar, no en transformers de muchas capas. En un
> transformer el argumento no se debilita: la información además se mezcla entre capas.
> **Si vas a citar una sola cosa de esta clase en un paper tuyo, es ésta.**

**7. Wiegreffe, S. & Pinter, Y. (2019). *Attention is not not Explanation*. EMNLP.**
`[VERIFICAR URL]`
> La réplica, y hay que leerla. Sostienen que el resultado anterior depende de qué
> entendamos por «explicación» y de cómo se construyan los mapas adversarios, y proponen
> pruebas más exigentes. **Leé las dos.** No para quedarte con una: para ver cómo se
> discute en el campo, que es exactamente lo que ustedes hacen en el suyo. Que el debate
> siga abierto es un dato sobre el estado del conocimiento, no una falla.

**8. Jesse Vig, *BertViz* — herramienta de visualización de atención.**
`https://raw.githubusercontent.com/jessevig/bertviz/master/README.md`
`[VERIFICADA 2026-08-29]`
> La herramienta estándar para mirar la atención de un modelo pre-entrenado de verdad,
> capa por capa y cabeza por cabeza, adentro de un notebook. En la clase 9 vas a tener
> modelos pre-entrenados a mano: éste es el visor. **Usalo para explorar, con la
> advertencia de la slide 34 puesta.**
> Se instala con `pip install bertviz` y corre en Colab.

**9. Karpathy, A., *nanoGPT* — el código del modelo, comentado.**
`https://raw.githubusercontent.com/karpathy/nanoGPT/master/model.py`
`[VERIFICADA 2026-08-29]` · README:
`https://raw.githubusercontent.com/karpathy/nanoGPT/master/README.md`
`[VERIFICADA 2026-08-29]`
> Trescientas líneas que son un GPT completo y entrenable. **Comparalo con la clase
> `BloqueTransformer` del notebook de hoy**: vas a reconocer cada pieza, con otros
> nombres y en inglés. Es el mejor ejercicio de lectura de código del curso, y sirve para
> convencerse de que no hay nada escondido.
> Su hermano didáctico, *minGPT*, es todavía más chico:
> `https://raw.githubusercontent.com/karpathy/minGPT/master/README.md`
> `[VERIFICADA 2026-08-29]`

**10. Rush, A. et al., *The Annotated Transformer*.**
`https://raw.githubusercontent.com/harvardnlp/annotated-transformer/master/README.md`
`[VERIFICADA 2026-08-29]`
> El paper de 2017 línea por línea, con el código al lado de cada párrafo. Es la
> referencia para cuando quieras entender un detalle puntual (el `√d`, el positional
> encoding con senos y cosenos, el decoder que nosotros no vimos). **No es para leer de
> corrido**: es para consultar.

**11. Elhage, N. et al. (2021). *A Mathematical Framework for Transformer Circuits*.
Anthropic.** `[VERIFICAR URL]`
> Sólo si te agarró la curiosidad de interpretabilidad y tenés tiempo. Es duro y es
> hermoso: desarma un transformer de una y dos capas y muestra circuitos concretos (por
> ejemplo, cabezas que copian la palabra que sigue a una aparición anterior del token
> actual). **No se asigna en el curso.** Está acá porque es la respuesta seria a la
> pregunta «¿entonces nunca vamos a poder explicar lo que hace?».

---

## Sobre los datos y el modelo de esta clase

- **Los mapas de atención de las cuatro visualizaciones son reales.** Salen de un
  transformer de ~0,5 M de parámetros entrenado en CPU sobre los discursos de apertura de
  sesiones ordinarias del Congreso argentino (1984-2019), con el script
  `clases/07-attention-y-transformer/medir-atencion.py` de esta misma carpeta. La semilla
  está fija y el resultado es **determinista en la misma máquina y con las mismas
  versiones de las librerías**; con otra versión de torch los mapas cambian (y se pueden
  perder los dos momentos aha: el script avisa y no sobrescribe). Las versiones de la
  corrida que está en el repo no quedaron registradas; las corridas nuevas las guardan en
  `meta.versiones`.
- **Los rótulos de las cabezas** (`viz/cabezas.html`) se miden sobre las cinco oraciones de
  las viz, sin la primera palabra de cada una. Son un resumen de esas oraciones, no del
  modelo entero.
- **Recopilación del corpus:** Lucas Ariel, *discursos_presidenciales*.
  `https://raw.githubusercontent.com/lucariel/discursos_presidenciales/master/README.md`
  `[VERIFICADA 2026-08-29]`. Los textos son documentos oficiales del Congreso; la
  recopilación **no declara licencia** (ver `datos/README.md`, sección 1.1).
- **Los vectores de `viz/qkv.html` no son reales**: son de juguete, de dos dimensiones y
  puestos a mano, para poder dibujarlos como flechas. Está rotulado en la propia página.
  Un modelo de verdad usa 64 o más dimensiones por cabeza, y ahí no hay dibujo posible.

---

## Las salvedades de esta clase, con su fuente

Todas `[VERIFICAR URL]`: se encuentran buscando por título. No se asignan; están para quien
quiera saber de dónde sale cada matiz de las slides y las notas.

- **Dong, Y., Cordonnier, J.-B. & Loukas, A. (2021). *Attention is not all you need: pure
  attention loses rank doubly exponentially with depth*. ICML.** (arXiv:2103.03404) — sin
  conexión residual, apilar attention hace que todas las posiciones converjan al mismo
  vector. Es lo que mide el `TODO 4`.
- **Haviv, A., Ram, O., Press, O., Izsak, P. & Levy, O. (2022). *Transformer Language
  Models without Positional Encodings Still Learn Positional Information*. Findings of
  EMNLP.** (arXiv:2203.16634) — por qué «sin posiciones es una bolsa de palabras» vale
  para attention **sin máscara**: con máscara causal, el modelo recupera algo del orden.
- **Kobayashi, G., Kuribayashi, T., Yokoi, S. & Inui, K. (2020). *Attention is Not Only a
  Weight: Analyzing Transformers with Vector Norms*. EMNLP.** (arXiv:2004.10102) — un
  peso de atención alto sobre un *value* chico aporta poco: la salvedad de la slide 34.
- **Voita, E., Talbot, D., Moiseev, F., Sennrich, R. & Titov, I. (2019). *Analyzing
  Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be
  Pruned*. ACL.** (arXiv:1905.09418) y **Clark, K., Khandelwal, U., Levy, O. & Manning,
  C. D. (2019). *What Does BERT Look At? An Analysis of BERT's Attention*. BlackboxNLP.**
  (arXiv:1906.04341) — unas pocas cabezas especializadas, muchas prescindibles: el matiz
  de `viz/cabezas.html`.
- **Su, J. et al. (2021). *RoFormer: Enhanced Transformer with Rotary Position
  Embedding*.** (arXiv:2104.09864) — las posiciones rotativas (RoPE) que usa hoy la
  mayoría de los LLM.
- **Grinsztajn, L., Oyallon, E. & Varoquaux, G. (2022). *Why do tree-based models still
  outperform deep learning on tabular data?* NeurIPS (Datasets and Benchmarks).**
  (arXiv:2207.08815) — el cartel de datos tabulares de `viz/supuestos-de-arquitectura.html`
  (la ficha completa está en el `referencias.md` de la clase 5).

---

## Lo que NO conviene leer todavía

- Papers de **eficiencia de attention** (*Linformer*, *Performer*, *FlashAttention*,
  atención dispersa). Son excelentes y no aportan nada a lo que necesitás: resuelven el
  costo cuadrático, no el mecanismo. Volvé cuando el cuadrado sea tu problema.
- Papers de **arquitecturas nuevas que reemplazan attention** (Mamba y compañía). Están
  buenísimos y cambian cada seis meses. Primero conviene tener firme lo que hoy es rutina.
