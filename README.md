# Deep Learning para Cientistas Sociales

**Diez clases de dos horas, en castellano rioplatense, para gente que investiga
sociedad y no quiere convertirse en data scientist.** Sociología, ciencia
política, antropología, comunicación, economía. Gente que programa poquito o
nada, que le tiene respeto a la matemática, y que quiere **una herramienta más en
la caja** y quiere usarla **con criterio**: saber cuándo sirve, cuándo te está
mintiendo, y cómo demostrarle a un revisor que no te mintió.

Todo el material **abre con `file://` y funciona sin internet**. Los notebooks
corren en Colab gratis, en CPU.

👉 **Empezá abriendo [`index.html`](index.html)** con doble clic. Es el índice del
curso entero.

---

## La filosofía, en un párrafo

Una red neuronal es una **máquina de dibujar figuras** que tiene un montón de
perillas, y entrenarla es girar las perillas hasta que la figura que dibuja se
parezca a los datos. Eso es todo, y esa misma frase se repite diez clases a
escalas cada vez más grandes: en la clase 1 dibujamos una recta con dos perillas
y en la 8 dibujamos una distribución de probabilidad sobre 71 fichas con un
millón y medio. La intuición va primero, la fórmula va después, y a veces la
fórmula no va: si escribís una ecuación y no tenés al lado una figura que muestre
qué hace, se borra la ecuación, no se la mueve de lugar. Cada concepto abstracto
tiene un objeto concreto que se puede manosear con el dedo, y en varias
visualizaciones el aula **apuesta primero y se equivoca**, porque la predicción
fallida es el momento en que se aprende. Todos los ejemplos viven en discurso
político y en prensa: no hay precios de casas en Boston ni flores iris. Y cada
clase tiene un **`[EN TU INVESTIGACIÓN]`**: algo chiquito y concreto que ya sirve
en la investigación de ellos, desde ya.

---

## El mapa de las diez clases

| # | Clase | La única idea | El notebook tarda |
|---|---|---|---|
| **1** | [Una función es una máquina con perillas](clases/01-funciones-y-parametros/) | Las entradas te mueven a lo largo de la figura; los parámetros deforman la figura. Aprender es mover parámetros. | 8 s |
| **2** | [Componer funciones: dibujar lo imposible](clases/02-componer-funciones/) | Apilando rampas con un doblez en el medio se dibuja *cualquier* figura. Eso, y nada más, es una red neuronal. | 9 s |
| **3** | [Estar equivocado es un número, y tiene pendiente](clases/03-loss-y-gradiente/) | Si podés medir cuán mal dibujás, podés bajar por esa medida hasta el fondo del valle. | 9 s |
| **4** | [El ciclo de entrenamiento: dibujar vs. calcar](clases/04-entrenar-de-verdad/) | Un modelo con demasiada libertad memoriza tu muestra. Por eso existe la validación. | 29 s |
| **5** | [La forma de los datos manda: imágenes](clases/05-imagenes-y-convoluciones/) | La arquitectura es una teoría sobre cómo está hecho el mundo. Y puede ser falsa. | 1 min 21 s |
| **6** | [La forma de los datos manda: texto](clases/06-texto-secuencias-embeddings/) | El orden es información, y cada palabra necesita un lugar en un mapa. | 19 s |
| **7** | [Attention: cada palabra arma su resumen](clases/07-attention-y-transformer/) | En vez de leer en orden y olvidarse, cada palabra mira a todas y decide a cuál prestarle atención. | 15 s |
| **8** | [Un mini-GPT propio, y la traducción a ChatGPT](clases/08-mini-gpt-y-los-llm/) | Un LLM dibuja la distribución de la próxima ficha. Todo lo raro que hace ChatGPT sale de ahí. | 5 min 29 s |
| **9** | [Usar modelos que ya existen, sin creerles](clases/09-modelos-preentrenados/) | Un modelo pre-entrenado es un informante clave: sabe muchísimo y tiene sus sesgos. | 17 s |
| **10** | [Criterio: validez, sesgo, reproducibilidad y el revisor 2](clases/10-criterio-validacion-y-etica/) | El modelo mide *algo*. Tu trabajo es demostrar que ese algo es lo que decís que es. | 15 s |

Los tiempos son **medidos**, no estimados: `nbconvert --execute` de punta a punta
en CPU, sin GPU, el 2026-08-29. En Colab gratis (2 vCPU) contá entre una y dos
veces eso.

Cada clase abre una puerta y la siguiente la cruza. El mapa completo de esos
puentes está en [`PROGRAMA.md` §4](PROGRAMA.md).

---

## Cómo se usa

### Si vas a **dictar** el curso

1. **[`recursos/GUIA-DEL-DOCENTE.md`](recursos/GUIA-DEL-DOCENTE.md)** — es tu
   punto de partida. Cómo preparar cada clase y con cuánta anticipación, qué
   equipamiento hace falta, cómo manejar un aula con niveles muy distintos de
   programación, cómo evaluar, y **los diez momentos del curso donde el aula
   típicamente se pierde y cómo rescatarla**.
2. **[`PROGRAMA.md`](PROGRAMA.md)** — el plan minuto a minuto de las diez clases
   y las decisiones transversales de diseño.
3. **`clases/NN-slug/notas-docente.md`** — el guion hablado de esa clase: los
   tiempos reales, las preguntas para el aula, qué recortar si te atrasás y qué
   hacer si te sobra tiempo. **Leelo la noche anterior, entero.**
4. **[`datos/README.md`](datos/README.md)** — de dónde salen los datos y, sobre
   todo, **qué trampa esconde cada corpus**. Media hora que te ahorra una clase
   entera de decir cosas que no son.

### Si sos **estudiante**

1. **[`recursos/setup.md`](recursos/setup.md)** — cómo abrir los notebooks en
   Colab y qué hacer si algo explota. Quince minutos, antes de la clase 1.
2. **[`recursos/glosario.md`](recursos/glosario.md)** — tenelo abierto siempre.
   La mitad de la sensación de "no entiendo nada" en deep learning es
   vocabulario, no conceptos.
3. Después de cada clase: `clases/NN-slug/cuestionario.md` (se resuelve en 15
   minutos, no lleva nota: es para conversar) y las visualizaciones de esa clase,
   sin apuro. En clase las movió el docente; la diferencia entre ver mover un
   slider y moverlo vos es enorme.
4. **[`recursos/bibliografia.md`](recursos/bibliografia.md)** — todo lo que se
   cita en las diez clases, ordenado por para qué te sirve.

### Cómo se abre cada cosa

| Qué | Cómo |
|---|---|
| **Las slides** | Doble clic en `clases/NN-slug/slides.html`. Es reveal.js: flechas para moverte, `S` abre las notas del docente en otra ventana, `F` pantalla completa, `Esc` la vista de conjunto. No necesita servidor ni internet. |
| **Las visualizaciones** | Doble clic en `clases/NN-slug/viz/*.html`. Van embebidas en las slides, pero **proyectalas sueltas**: sueltas tienen el título, el pie con la explicación y el botón de tema claro/oscuro (abajo a la derecha). |
| **Los notebooks** | En Colab: subir el `.ipynb` o abrirlo desde GitHub. La primera celda (la de *bootstrap*) instala lo que haga falta y trae el paquete `ssdl`; **es canónica, no se edita**. También corren local con Jupyter, o de una: `python3 -m nbconvert --to notebook --execute clases/NN-slug/notebook.ipynb`. |
| **El índice** | Doble clic en `index.html`. |

---

## La estructura del repo

```
index.html                       el índice del curso: abrilo con doble clic
PROGRAMA.md                      el programa: filosofía, plan minuto a minuto, mapa de puentes
README.md                        este archivo

clases/NN-slug/
  slides.html                    reveal.js, 35-41 slides, notas del docente adentro
  notebook.ipynb                 Colab, autoinstalable, corre entero en CPU
  viz/*.html                     visualizaciones interactivas standalone (39 en total)
  notas-docente.md               el guion hablado, los tiempos, qué recortar
  cuestionario.md                8-12 ítems · cuestionario-soluciones.md
  referencias.md                 las lecturas de esa clase, con las URLs marcadas
  VERIFICACION.md                qué se verificó y qué quedó abierto en esa clase
  medir-*.py / datos-*.js        los números de las slides y las viz, medidos y guardados

_shared/
  css/curso.css                  la identidad visual y la semántica de color. Manda esta hoja.
  js/viz.js                      la biblioteca de visualización del curso, sin dependencias
  vendor/                        reveal.js y KaTeX vendoreados (NO hay acceso a CDNs)
  ssdl/                          el paquete de Python del curso (datos, gráficos, entrenamiento)
  plantillas/                    slides, viz y notebook de referencia + GUIA-CONSTRUCCION.md
  especificaciones/              la spec de cada clase y los dos informes de estado

datos/                           corpus, descarga con fallback, y el README con las trampas
recursos/                        setup.md · glosario.md · bibliografia.md · GUIA-DEL-DOCENTE.md
```

Dos archivos de estado, y conviene saber cuál es cuál:

- **`_shared/especificaciones/00-ESTADO-ESPINA.md`** — la verificación de la base
  compartida *antes* de construir las clases. Su sección 5 es la lista de trampas
  del entorno y de los datos.
- **`_shared/especificaciones/00-ESTADO-CURSO.md`** — el estado final medido del
  curso entero, después de construirlo. **Ese es el que hay que leer hoy.**

---

## Los datos, y de dónde salen

Todo ejemplo del curso vive en **discurso político** o en **prensa**. Hay dos
capas:

| Corpus | Qué es | Licencia |
|---|---|---|
| **Discursos de apertura de sesiones** (Argentina, 1854-2019) | El hilo conductor de las clases 1 a 4 y el corpus del mini-GPT. Recopilación de Lucas Ariel. | Los textos son actos oficiales del Estado argentino. **La recopilación no declara licencia.** |
| **Discursos de Casa Rosada** (2015-2024) | Complemento reciente. | **Sin licencia declarada.** |
| **Fake News Corpus Spanish** (FakeDeS @ IberLEF 2021) | 1.471 notas de prensa reales con etiqueta. Es el corpus de las clases 9 y 10. | **CC BY 4.0** |
| **Fashion-MNIST** | El sandbox técnico de la clase 5, declarado como tal. | **MIT** |
| **Aguasclaras** | Corpus **sintético** de un país que no existe, generado por `datos/generar_aguasclaras.py` con semilla fija. Se usa para todo lo que necesita volumen. | Del curso. Usalo. |

> **Pendiente, y es serio.** Los **dos** corpus de discursos no declaran licencia
> en sus repositorios. El uso educativo es defendible porque los textos son actos
> oficiales, pero **si este curso se publica hay que escribirles a los
> recopiladores primero**. Está anotado en `datos/README.md`, en
> `recursos/bibliografia.md` y en los `referencias.md` de las clases que los usan.

**Aguasclaras se rotula como sintético cada vez que aparece.** País ficticio,
proceso generador conocido, cero frases inventadas en boca de gente real. Y tiene
una ventaja pedagógica que el curso explota: como conocemos el proceso generador,
podemos auditar exactamente qué aprendió el modelo y qué se inventó.

Nada de esto puede romper una clase: si no hay red, los cargadores caen a
`datos/muestras/` (5,2 MB versionados) y **todo corre igual**. Cambian algunos
números exactos, no cambia ninguna clase. Las trampas de cada corpus —los
agujeros del corpus de discursos son los golpes de Estado; 2005 y 2006 son el
mismo discurso; la fuente predice la etiqueta al 96 % en el corpus de prensa—
están documentadas una por una en [`datos/README.md`](datos/README.md), y **son
contenido del curso, no notas al pie**.

---

## Cómo reproducir la verificación

Todo esto corre sin red y sin GPU.

```bash
# el paquete de Python: 119 tests, incluidos los doctests
python3 _shared/ssdl/test_ssdl.py

# los datos: 28 doctests + un informe sobre los datos reales
python3 datos/preparar_corpus.py
python3 datos/descargar.py --solo-muestras     # ni intenta la red

# los diez notebooks, de punta a punta (unos 8 minutos en total)
for d in clases/*/; do
  python3 -m nbconvert --to notebook --execute --output /tmp/out.ipynb "$d/notebook.ipynb"
done

# los números de las slides y las viz, remedidos
python3 clases/01-funciones-y-parametros/medir-referencias.py
python3 clases/05-imagenes-y-convoluciones/medir-experimentos.py
# … y los medir-*.py de las clases 4, 6, 7, 9 y 10
```

Para el HTML: Chromium por Playwright, abriendo por `file://` con un
`context.route('**/*')` que **aborta cualquier URL `http(s)`** y falla si alguna
sale. Así se comprobó que las 10 slides y las 39 visualizaciones no hacen ni una
sola request externa. Los resultados de cada clase están en su `VERIFICACION.md`,
y el índice, en `_shared/especificaciones/00-ESTADO-CURSO.md`.

---

## Si vas a tocar el material

Leé, en este orden: `_shared/especificaciones/00-ESTADO-CURSO.md` (qué está
medido y qué quedó abierto), `_shared/especificaciones/00-ESTADO-ESPINA.md` §5
(las trampas, cada una cuesta una hora si la descubrís solo) y
`_shared/plantillas/GUIA-CONSTRUCCION.md` (la API de `viz.js` y las
convenciones).

Las reglas que rompen todo si las rompés:

- **Cero red.** Ningún `<script src="https://…">`, ninguna Google Font, ningún
  CDN. Todo sale de `_shared/vendor/` por ruta relativa.
- **Todo abre con `file://`.** Si tu página necesita un servidor, está mal hecha.
- **Nada de matemática sin una imagen al lado.** Si hay una fórmula sin figura,
  se borra la fórmula.
- **Ningún notebook puede fallar por falta de red.** Patrón
  `try: descargar() / except: generar_sinteticos()`, obligatorio.
- **La semántica de color no es decoración.** `--c-datos` es lo observado,
  `--c-modelo` lo que el modelo dibuja, `--c-error` el desajuste, `--c-val` lo
  que el modelo no vio. Nunca escribas un `#hex` a mano en una viz: usá
  `Viz.color('modelo')`.
- **Ninguna viz sin momento aha.** Si no podés escribir la frase exacta que
  querés que el estudiante piense, la viz todavía no está diseñada.
- **Semillas fijas siempre.** La del curso es **1983**.
- **Cada término nuevo en inglés va a `recursos/glosario.md`**, en la clase donde
  aparece por primera vez.
- **No inventes una URL.** Si no la pudiste abrir, la cita queda sin enlace y
  marcada `[VERIFICAR URL]`. Es un curso sobre no inventar.

---

*Lo que aprendés acá no es a usar una biblioteca. Es a no dejarte impresionar.*
