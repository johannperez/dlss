# Referencias — Clase 9

**Usar modelos que ya existen, sin creerles**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la red
> bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. **Notablemente, `huggingface.co` da 403**, así que ninguna
> página del Hub se pudo abrir desde acá.
> **Se probó con `curl` cada URL de esta lista.** Las que respondieron van marcadas
> `[VERIFICADA 2026-08-29]`; el resto va `[VERIFICAR URL]`: las obras existen, están bien
> citadas y se encuentran buscando por título y autor, pero **nadie abrió el enlace**, y
> poner una URL sin haberla abierto sería inventarla. Éste es un curso sobre no inventar.
> Quien tenga red que las complete y las pase a `[VERIFICADA]` con la fecha.
> (En la revisión del 28-09-2026 sí hubo red hacia el Hub: se bajaron los modelos y se
> anotaron sus revisiones exactas, más abajo. Las URL marcadas `[VERIFICAR URL]` no se
> volvieron a probar.)

---

## Si te quedaste con ganas

En el orden en que conviene leerlas.

**1. Barberá, P., Boydstun, A. E., Linn, S., McMahon, R. & Nagler, J. (2021).
*Automated Text Classification of News Articles: A Practical Guide to Probabilistic
Machine Learning*. Political Analysis 29(1), 19-42.** `[VERIFICAR URL]`
> **Empezá por acá, y si sólo vas a leer una cosa, que sea ésta.** Es prácticamente el
> manual de esta clase escrito para tu disciplina: qué estrategia usar, **cuántos
> documentos etiquetar** (la respuesta empírica a la pregunta que hicimos hoy), cómo
> validar, y qué reportar. Está escrito para gente que estudia prensa, que es exactamente
> el corpus con el que trabajamos. Una tarde.

**2. Grimmer, J. & Stewart, B. (2013). *Text as Data: The Promise and Pitfalls of
Automatic Content Analysis Methods for Political Texts*. Political Analysis 21(3),
267-297.** `[VERIFICAR URL]`
> Tiene más de una década y sigue siendo la mejor síntesis de por qué estas herramientas
> ayudan y por qué no reemplazan nada. **Su consigna —«validate, validate, validate»— es
> el lema de esta clase.** Leelo pensando en la trampa del corpus de prensa: el paper te
> da el vocabulario para nombrar lo que vimos hoy con el detector de sátira.
> Dos horas, y se relee.

**3. Hugging Face, *NLP Course*, capítulos 1 a 3.**
Página del curso: `huggingface.co/learn/nlp-course` `[VERIFICAR URL]` ·
Repositorio con el contenido: `https://raw.githubusercontent.com/huggingface/course/main/README.md`
`[VERIFICADA 2026-08-29]` · **hay versión en castellano**, en `chapters/es` del mismo
repositorio `[VERIFICADA 2026-08-29]` (marcada como *work in progress*: está incompleta y
algunos capítulos siguen en inglés).
> El tutorial oficial. Los capítulos 1 y 2 explican `pipeline` y los tokenizadores; el 3
> es el fine-tuning. **Leelo después de esta clase**: si lo abrís antes, te vas a llevar
> la biblioteca sin el criterio, que es justo lo que pasa siempre. Tres o cuatro horas.

**4. `scikit-learn`, guía de *model evaluation*.**
`scikit-learn.org/stable/modules/model_evaluation.html` `[VERIFICAR URL]` ·
paquete: `https://pypi.org/project/scikit-learn/` `[VERIFICADA 2026-08-29]`
> La documentación es sorprendentemente buena como material didáctico, sobre todo las
> secciones de `precision_recall_fscore_support` y de curvas precisión-recall. Usala como
> referencia mientras escribís tu propio `reportar()`. Media hora, salteando.

**5. Cañete, J., Chaperon, G., Fuentes, R., Ho, J.-H., Kang, H. & Pérez, J. (2020).
*Spanish Pre-Trained BERT Model and Evaluation Data* (BETO). PML4DC @ ICLR 2020.**
Repositorio: `https://raw.githubusercontent.com/dccuchile/beto/master/README.md`
`[VERIFICADA 2026-08-29]` · preprint arXiv `[VERIFICAR URL]`
> El modelo en castellano más usado, hecho en la Universidad de Chile. Leé la tabla de
> *benchmarks* del README: compara BETO con BERT multilingüe tarea por tarea, y es el
> argumento empírico de por qué conviene un modelo dedicado al idioma.
> Identificadores exactos, verificados contra ese README:
> `dccuchile/bert-base-spanish-wwm-uncased` y `dccuchile/bert-base-spanish-wwm-cased`.
> Revisión del `uncased` que cita el notebook (el ejemplo de `Trainer`):
> `d1c9c4565c9d6731e57ed7f027b802697bad861e` (anotada el 28-09-2026).
> Media hora.

**6. Pérez, J. M. et al., *pysentimiento*: A Python toolkit for Sentiment Analysis and
Social NLP tasks.**
Repositorio: `https://raw.githubusercontent.com/pysentimiento/pysentimiento/master/README.md`
`[VERIFICADA 2026-08-29]` · tabla de tareas y resultados:
`.../master/docs/TASKS.md` `[VERIFICADA 2026-08-29]` ·
paquete: `https://pypi.org/project/pysentimiento/` `[VERIFICADA 2026-08-29]`
> **La herramienta más pertinente para esta audiencia**: sentimiento, emoción, ironía y
> discurso de odio en castellano, con modelos pre-entrenados sobre tuits en castellano de
> muchos países (RoBERTuito). El de sentimiento se ajustó con el corpus TASS 2020, que trae
> tuits de España, México, Perú, Costa Rica y Uruguay: rioplatense hay poco, y conviene
> saberlo. `pip install pysentimiento` y tres líneas. Ojo: la biblioteca preprocesa los
> tuits (usuarios, enlaces, emojis) antes de clasificar; el notebook usa el modelo "pelado"
> con `pipeline`, sin ese paso.
> Leé `docs/TASKS.md` y quedate con los números: el mejor modelo saca **70,2 de macro-F1**
> en sentimiento. **Setenta, no noventa y cinco.** Es la mejor vacuna contra el
> entusiasmo, y es de la propia gente que hizo la herramienta.
> Identificador verificado contra el código fuente de la biblioteca:
> `pysentimiento/robertuito-sentiment-analysis`. Revisión fijada en el notebook:
> `a2cc0f67ebd705c55191e25a05ba23d885fcc09b` (bajada y corrida el 28-09-2026).

---

## Si te vas a meter en serio

**7. Grimmer, J., Roberts, M. E. & Stewart, B. M. (2022). *Text as Data: A New Framework
for Machine Learning and the Social Sciences*. Princeton University Press.**
`[VERIFICAR URL]`
> **El libro de cabecera de todo el módulo.** Para esta clase, las partes que importan son
> las de clasificación supervisada y, sobre todo, las de **validación**: qué se puede
> afirmar con un modelo de texto y qué hay que demostrar antes de afirmarlo. La sección
> sobre *"no hay un mejor método, hay un método adecuado a tu pregunta"* es la versión
> larga y con evidencia de nuestra tabla de tres estrategias.

**8. Krippendorff, K., *Content Analysis: An Introduction to Its Methodology*.**
`[VERIFICAR URL]`
> Para el marco de fiabilidad entre codificadores. Si vas a reportar acuerdo, leé esto y
> no un blog: la discusión sobre por qué el porcentaje de acuerdo crudo no alcanza, y
> sobre las diferencias entre kappa y alfa, tiene consecuencias prácticas.
> **Lo que te llevás:** el acuerdo inter-codificador no es un trámite de calidad, es un
> **límite epistemológico** sobre lo que tu categoría puede medir.

**9. Reimers, N. & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese
BERT-Networks*. EMNLP.** Preprint arXiv:1908.10084 `[VERIFICAR URL]` ·
biblioteca: `https://raw.githubusercontent.com/UKPLab/sentence-transformers/master/README.md`
`[VERIFICADA 2026-08-29]` · paquete: `https://pypi.org/project/sentence-transformers/`
`[VERIFICADA 2026-08-29]`
> Identificador del modelo multilingüe que usa el camino A del notebook, verificado
> contra `docs/sentence_transformer/pretrained_models.md` de ese mismo repositorio
> `[VERIFICADA 2026-08-29]`: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`,
> revisión fijada en el notebook `e8f8c211226b894fcb81acc59f3b34ba3efd5f42` (bajada y
> corrida el 28-09-2026).
> El paper que explica **por qué** promediar las salidas de BERT no es una buena manera de
> representar una oración, y qué hay que hacer en cambio. Es directamente relevante para
> lo que hicimos hoy: nuestro camino B promedia vectores de palabra, y esto te dice
> cuánto se gana haciéndolo bien. Léelo si la búsqueda semántica te va a quedar en el
> pipeline de trabajo.

**10. Gómez-Adorno, H., Posadas-Durán, J. P., Bel-Enguix, G. & Porto-Capetillo, C. (2021).
*Overview of FakeDeS at IberLEF 2021: Fake News Detection in Spanish Shared Task*.
Procesamiento del Lenguaje Natural 67, 223-231.**
Corpus: `https://raw.githubusercontent.com/jpposadas/FakeNewsCorpusSpanish/master/README.md`
`[VERIFICADA 2026-08-29]` · **CC BY 4.0**
> **El corpus con el que trabajaste hoy.** Son dos recolecciones: la versión 1.0 (971 notas,
> enero a julio de 2018, las particiones `train` y `dev`) y la de FakeDeS 2021 (500 notas,
> noviembre de 2020 a marzo de 2021, la partición `test`, donde están todas las de
> Covid-19). Citalo si usás estos datos, y leé el *overview* con los ojos de la clase: cuando veas los F1 que reportaron los equipos participantes,
> preguntate cuántos de esos puntos vienen de detectar la fuente y no la desinformación.
> No es una crítica al corpus —es un corpus excelente y sus autores documentan lo que
> hicieron—, es la lectura que esta clase te enseñó a hacer.

**11. Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z. & Yang, D. (2024).
*Can Large Language Models Transform Computational Social Science?* Computational
Linguistics 50(1).** `[VERIFICAR URL]`
> La evaluación seria de la pregunta que alguien del aula va a hacer: *"¿puedo usar un LLM
> para etiquetar mis datos?"*. Respuesta corta: a veces, para algunas tareas, y **siempre
> con validación humana**. Da los números por tipo de tarea y es honesto sobre dónde falla.
> Es el puente entre la clase 8 y ésta.

**12. Landis, J. R. & Koch, G. G. (1977). *The Measurement of Observer Agreement for
Categorical Data*. Biometrics 33(1), 159-174.** `[VERIFICAR URL]`
> De acá sale la escala de lectura del kappa que usa el notebook (leve, regular, moderado,
> sustancial, casi perfecto). Leé cómo la justifican los autores: es una convención
> propuesta "para la discusión", no un criterio de calidad. Diez minutos, y te ahorra
> citarla como si fuera una ley.

**13. Salganik, M. et al. (2020). *Measuring the predictability of life outcomes with a
scientific mass collaboration*. PNAS 117(15).** `[VERIFICAR URL]`
> No es sobre texto, y es la mejor lectura de humildad que hay: 160 equipos, los mismos
> datos de panel, todas las técnicas disponibles, y **ninguno predijo bien**. Leelo cuando
> te entusiasmes con un F1.

---

## Los datos de esta clase

Todo lo que usamos hoy está documentado en **`datos/README.md`**, con procedencia,
licencia y —lo importante— la lista de trampas de cada corpus. Para esta clase, leé
sobre todo:

- **§1.3 `prensa`** — el corpus de 1471 notas: la fuente predice la etiqueta al 96 %, las
  "falsas" son sobre todo sátira, las mayúsculas delatan, y el largo del texto también.
  **La sección (a) es la clase de hoy en una página.** La (e) cuenta que son dos épocas
  pegadas (2018 y 2020-21) y que tema y época están confundidos.
- **§3** — por qué las clases 9 y 10 necesitan Hugging Face y cuál es el plan B.
- **La submuestra doblemente codificada** (`doble-codificacion-SIMULADA-100.csv`): los dos
  codificadores son **simulados**, está en el nombre del archivo, y usarlo como si fuera
  codificación humana real sería fraude.

## Reproducir los números de esta clase

```bash
# las curvas de las viz y los números de las slides (sin red; al final chequea que
# los momentos de las slides 16 y 32 sigan apareciendo)
PYTHONPATH=_shared python3 clases/09-modelos-preentrenados/medir-clase09.py

# el notebook entero, sobre una COPIA del repo (guarda figuras en figuras/ y, adentro
# del repo, las pisaría). Sin red va por el camino B: medido, entre 6 y 20 s con la
# máquina libre, hasta 2 min si está cargada.
cp -R . /tmp/dlss-copia && cd /tmp/dlss-copia/clases/09-modelos-preentrenados
python3 -m nbconvert --to notebook --execute --output nb-09-ejecutado.ipynb notebook.ipynb
```

Semilla **1983** en todo. Los resultados son deterministas en la misma máquina y con las
mismas versiones de las librerías; con otras versiones algún número puede moverse en el
4.º decimal (el JSON guarda con qué versiones se generó). Si cambiás el corpus o la
semilla, volvé a correr el script y **actualizá las slides**: un número desactualizado en
un curso sobre no inventar es el peor error posible.
