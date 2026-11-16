# Clase 9 · Material extra

En clase hicimos transfer learning en dos niveles con `notebook.ipynb`: congelar el
modelo prestado y poner una regresión logística arriba (nivel 1), y descongelarlo para
hacer *fine-tuning* (nivel 2). Esta carpeta tiene lo que no entró en 75 minutos.

**Si vas a hacer una sola cosa, que sea la receta 4 con un CSV tuyo.**

---

## Por dónde empezar

| orden | archivo | qué tiene | cuánto lleva | necesita |
|---|---|---|---|---|
| 1 | [`recetas-transfer-learning.ipynb`](recetas-transfer-learning.ipynb) | **Implementaciones cortas, una por receta, para copiar.** Cada una corre sola después de la sección 0. | 1 hora | red (baja modelos) |
| 2 | [`notebook-completo.ipynb`](notebook-completo.ipynb) | La clase de dos horas: lo que sigue después de hacerlo andar, que es **saber si anda**. | 2 horas | nada (con red, mejor) |
| 3 | [`../viz/`](../viz/) | Las tres visualizaciones, sin internet: la curva de etiquetas, la búsqueda semántica y la matriz de confusión con umbral. | 15 min | nada |
| 4 | [`../referencias.md`](../referencias.md) | Qué leer y en qué orden. Empezá por Barberá et al. (2021). | — | — |

Los dos notebooks abren en Colab igual que el de la clase: la primera celda clona el
repo y deja todo listo.

---

## Las recetas (`recetas-transfer-learning.ipynb`)

Todas usan la misma tarea, la misma partición y el mismo test que el notebook de la
clase, así que los números se comparan directo con la tabla de la sección 7.

| receta | qué es | cuándo usarla | lo que medimos (200 etiquetas) |
|---|---|---|---|
| **1 · `sentence-transformers`** | El nivel 1 de la clase en tres líneas: `encode()` + regresión logística. | **Siempre primero.** De 50 a 500 etiquetas. | F1 0.64, igual que a mano |
| **2 · `Trainer` de Hugging Face** | Fine-tuning de BETO (BERT en castellano) con la herramienta que usan los tutoriales. Separa validación del train y no toca el test hasta el final. | Con 300 etiquetas o más, y midiendo contra la receta 1 con varias semillas. | F1 0.56-0.58; 13 s en CPU con 2 hilos |
| **3 · Zero-shot** | Clasificar describiendo la categoría ("Esta nota es sobre política."), sin ejemplos de entrenamiento. | Cuando no tenés etiquetas para entrenar. **Igual necesitás 100-300 para evaluar.** | F1 0.39, casi lo mismo que un diccionario de palabras (0.40) |
| **4 · Tu propio CSV** | De un archivo con tus textos (algunos etiquetados) a una tabla con el puntaje de cada uno, más la evaluación honesta. | Cuando lo uses de verdad. | — |

Medido el 2026-11-13 con `transformers` 5.23 y `torch` 2.15. Con otra máquina u otra
versión, el segundo decimal puede cambiar.

---

## El notebook completo (`notebook-completo.ipynb`)

Es el notebook original de la clase de dos horas, sin cambios. Lo que tiene y en clase
no vimos:

- **§4 Búsqueda semántica:** buscar en tu corpus por significado y no por palabra clave,
  con sus falsos positivos.
- **§8 La curva:** cuántas etiquetas hacen falta, con cinco semillas por tamaño.
- **§9 El umbral:** el modelo devuelve un puntaje, y dónde cortás es una decisión de
  investigación, no técnica.
- **§10 Leer los errores** (`TODO 6`): leer 30 errores enseña más sobre tu categoría que
  300 aciertos. Varios "errores" van a ser etiquetas humanas equivocadas.
- **§11 La trampa del corpus:** un "detector de desinformación" con F1 0,68 que en
  realidad detecta el estilo de dos sitios de sátira. **Si leés una sola sección, que sea
  esta.** Es el puente a la clase 10.
- **§12 El techo humano:** el acuerdo entre dos codificadores, medido con la misma
  métrica que el modelo.

Las slides que acompañan esa versión están en el mismo archivo de la clase:
abrí `../slides.html?completo`.

---

## Para ver más implementaciones

| qué | dónde |
|---|---|
| Curso de Hugging Face, capítulo 3 (fine-tuning), **en castellano** | https://huggingface.co/learn/llm-course/es/chapter3/1 |
| Clasificación de texto con `transformers`, guía oficial | https://huggingface.co/docs/transformers/tasks/sequence_classification |
| `sentence-transformers` | https://sbert.net/docs/sentence_transformer/usage/usage.html |
| SetFit: fine-tuning con muy pocas etiquetas | https://github.com/huggingface/setfit |
| Zero-shot en el Hub | https://huggingface.co/tasks/zero-shot-classification |
| `pysentimiento`: modelos ya afinados en castellano | https://github.com/pysentimiento/pysentimiento |
| Transfer learning con imágenes en PyTorch (la clase 5, con un modelo prestado) | https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html |

Todos verificados el 2026-11-13.
