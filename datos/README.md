# Datos del curso

> **Leé esto antes de tocar un notebook.** No es documentación burocrática:
> la mitad de lo que este curso quiere enseñar está en la sección
> [Trampas](#trampas-la-parte-importante). Un modelo que anda con datos que no
> mirás con desconfianza es un modelo que te va a mentir en el paper.

---

## 0. Lo primero: nada de esto puede romper una clase

Todos los datasets siguen el mismo patrón, y los notebooks también:

```
1. ¿está en datos/cache/?   -> se usa
2. si no, se descarga       -> se cachea
3. si la descarga falla     -> se usa datos/muestras/, que está en el repo
4. nunca se levanta una excepción por falta de red
```

`datos/muestras/` pesa **5,2 MB** y está versionado. Si mañana desaparece
GitHub, si el wifi del aula es un desastre, o si una fuente se cae para
siempre, **el curso entero corre igual**. Cambian los números exactos de
algunos ejemplos, no cambia ninguna clase.

Probalo vos:

```bash
python3 datos/descargar.py --solo-muestras    # ni intenta la red
python3 datos/descargar.py --verificar-urls   # solo prueba conectividad
python3 datos/descargar.py                    # baja todo y reporta
python3 datos/preparar_corpus.py              # doctests + informe sobre los datos reales
```

---

## 1. Catálogo

| # | Dataset | Qué es | Real / sintético | Tamaño | Clases |
|---|---------|--------|------------------|--------|--------|
| 1 | `discursos-apertura` | 108 discursos presidenciales de apertura de sesiones (Argentina, 1854-2019) | **real** | 8,2 MB completo · 2,7 MB en muestras | 1, 2, 3, 4, 6, 7, 8 |
| 2 | `series` | La serie de % de palabras por tema y por año, derivada de (1) | **real** (derivado) | 14 KB | 1, 2, 3, 4 |
| 3 | `prensa` | 1471 notas de prensa en castellano con etiqueta verdadera/falsa, tema y fuente | **real** | 4,2 MB completo · 1,1 MB en muestras | 4, 9, 10 |
| 4 | `casarosada` | 1311 discursos presidenciales 2015-2024 con orador y fecha | **real** | 10,5 MB completo · 300 KB en muestras | 6, 10 |
| 5 | `aguasclaras` | Debates parlamentarios y prensa de un país que no existe, **con el padrón de la verdad** | **SINTÉTICO** | 1,3 MB | 8 (y fallback general) |
| 6 | `fashion-mnist` | 70.000 imágenes de prendas, 28×28 | **real** (sandbox técnico) | 30 MB, no se versiona | 5 |

---

### 1.1 `discursos-apertura` — el hilo conductor del curso

**Qué es.** Los mensajes que el presidente o la presidenta de la Nación
Argentina lee ante la Asamblea Legislativa al abrir las sesiones ordinarias
del Congreso, cada 1 de marzo. Es el documento más comparable que existe en
la política argentina: mismo emisor institucional, mismo auditorio, misma
fecha, misma función (rendir cuentas del Estado de la Nación), durante
165 años. Por eso es el hilo del curso.

**Quién lo hizo.** Los textos son documentos oficiales del Congreso argentino.
La recopilación y digitalización la hizo **Lucas Ariel** en
[github.com/lucariel/discursos_presidenciales](https://github.com/lucariel/discursos_presidenciales),
inspirada en *Los discursos presidenciales en la Argentina democrática*
(Bercholc & Bercholc, 2012). Los anteriores a 1984 los pasó por OCR él mismo.

**Licencia.** Los textos fuente son actos oficiales del Estado argentino.
El repositorio de la recopilación **no declara licencia**. Se usa acá con
fines educativos y se cita la recopilación. Si el curso se publica, hay que
escribirle al autor.

**Formato.** Un `.txt` por año, UTF-8, nombre `AAAA-nombre_del_presidente.txt`.

**Cómo se baja.**
```python
import descargar
d = descargar.discursos_apertura()          # {anio: {presidente, texto}}
t = descargar.corpus_discursos_texto()      # un string de 2,2 MB (1984-2019)
```

**Estado de la URL:** `raw.githubusercontent.com/lucariel/...` → **VERIFICADA-OK**
(los 108 archivos bajaron en el contenedor de construcción y quedaron en cache).

**Verificado que sirve para lo que decimos que sirve.** No es una promesa:

- *Mini-GPT (clase 8).* Corpus de 2.184.070 caracteres, vocabulario de 112
  caracteres. Un transformer de 640.240 parámetros (3 bloques, 4 cabezas,
  contexto 128) entrenado **en CPU** baja la loss de 4,87 a 1,67 en
  **400 pasos y 45 segundos**, y ya genera castellano reconocible
  ("El Estado nacional … de la Argentina, … dependir en …"). En la GPU T4
  gratis de Colab sobra tiempo para llegar a algo mucho mejor dentro de la
  clase. El entrenamiento puede arrancar en el minuto 20, como pide el programa.
- *Embeddings (clase 6).* PPMI + SVD con numpy, sin dependencias, sobre el
  mismo corpus: 347.668 tokens, vocabulario útil de 3.745 palabras
  (frecuencia ≥ 8), **22 segundos**. Los vecinos salen bien de verdad:
  `docentes` → investigadores, universitarios, maestros, alumnos;
  `provincias` → misiones, santiago, estero, formosa, corrientes, chaco;
  `mujeres` → hombres, jóvenes, niños, embarazadas.
  O sea: la viz central de la clase 6 puede correr con **datos reales**,
  sin Hugging Face y sin red.

#### Trampas de este dataset

**(a) Los agujeros no son al azar: son los golpes de Estado.**
Faltan 58 de los 166 años. Pero mirá dónde faltan:

| período | años sin discurso |
|---|---|
| 1854-1929 | 30 de 76 |
| 1930-1942 | 4 de 13 |
| 1943-1954 | 4 de 12 |
| **1955-1982** | **19 de 28** |
| 1983-2019 | 1 de 37 |

Faltan 1976, 1977, 1978, 1979, 1980, 1981, 1982 y 1983 seguidos. No es que
se perdió el archivo: **el Congreso estaba cerrado**. Lo mismo 1967-1972.
Si hacés una serie temporal 1854-2019 y "completás los faltantes" con
interpolación, estás inventando discursos que nadie dio en años en los que
no había Parlamento. Es el caso de manual de *missing not at random*: la
ausencia del dato **es** el dato. Por eso el curso trabaja sobre 1984-2019,
que es el único tramo continuo.

**(b) Los discursos anteriores a 1984 pasaron por OCR.**
El propio autor lo dice: usó un OCR web para los escaneados. Eso deja
números de página en medio del texto, palabras cortadas, tildes perdidas y
"1" donde iba "l". `preparar_corpus.limpiar()` saca lo peor, pero **no lo
arregla todo**. Si comparás vocabulario entre 1916 y 2016, una parte de la
diferencia que vas a medir es diferencia de OCR, no diferencia de época.
El archivo `muestras/discursos-apertura/1916-victorino_dela_plaza.txt` está
en la muestra justamente para que se vea.

**(c) 2005 y 2006 son el mismo discurso, palabra por palabra.**
Verificado con `md5sum` **sobre los archivos del corpus fuente** (los que baja
`descargar.py` a `datos/cache/`): `2005-nestor_kirchner.txt` y
`2006-nestor_kirchner.txt` tienen el mismo hash. Es un error del corpus fuente.
Los dos están en `muestras/` **a propósito**, porque son la evidencia física de
la trampa.

> **Ojo con reproducirlo sobre `muestras/`.** Ahí el `md5sum` da **distinto**,
> porque a cada muestra el script le agrega una cabecera de comentarios `#`
> propia. Lo idéntico es el texto del discurso, no el archivo con su cabecera.
> Para verificarlo vos mismo: `python3 datos/preparar_corpus.py` lo comprueba
> sobre el corpus completo y lo imprime. `preparar_corpus.diagnostico_de_fuga()` los detecta, y
`corpus_discursos_texto()` excluye 2006.
Esto no es una anécdota: si partís al azar, ese par cae de los dos lados de
la partición y tu modelo "predice" perfecto un caso que ya vio. Es la clase 4
en vivo, con datos reales del curso.

**(d) El largo cambia por un factor de 9.**
De 2.873 palabras (1996) a 25.217 (2013). Contar menciones crudas mediría
elocuencia, no agenda. Por eso todas las series son **porcentaje de palabras
del discurso**, nunca conteo. Es la decisión de normalización más importante
del módulo 1-4.

**(e) El discurso no lo escribe el presidente.**
Lo escribe un equipo, se negocia con ministerios y se corrige hasta la noche
anterior. Cuando decís "Menem hablaba más de seguridad", lo que medís es
**la agenda que la Presidencia decidió mostrarle al Congreso ese año**. Eso
es un objeto legítimo y valioso de estudio. No es "lo que el presidente
pensaba". Escribí la frase correcta en el paper.

**(f) Un solo país, un solo idioma, un solo régimen.**
Todo lo que aprendas acá vale para Argentina post-1983. No lo extrapoles
sin decirlo.

---

### 1.2 `series` — la serie que atraviesa las clases 1 a 4

**Qué es.** Una tabla derivada de (1.1): una fila por año, con el porcentaje
de palabras del discurso que pertenecen al léxico de cada tema.

```
anio, presidente, palabras, seguridad, inflacion, educacion, trabajo, salud,
                            seguridad_suave, inflacion_suave, ...
```

- `muestras/series/menciones-por-tema-apertura.csv` — 107 filas, 1854-2019.
- `muestras/series/menciones-democracia-1984-2019.csv` — 36 filas. **Esta es
  la de las clases 1 a 4.**

Las columnas `_suave` son una media móvil centrada de 3 años.

**Por qué hay dos versiones y cuál usar en cada clase:**

| clase | columna | por qué |
|---|---|---|
| 1 | `seguridad` (cruda) | La recta nunca ajusta del todo. El "desajuste" no llega a cero. Eso es lo que motiva la clase 2. |
| 2 | `inflacion_suave` | Tiene dos picos y un valle claros. Es imposible para una recta y queda linda con 8 rampas. |
| 3 | `seguridad` (cruda) | Mismo problema de la clase 1, ahora con el paisaje de loss. |
| 4 | `seguridad` (cruda) | El ruido **es** el punto: con 32 rampas lo calcás. |

Números reales, por si el equipo de la clase 1 quiere saber qué le va a pasar:
la recta sobre `seguridad` tiene pendiente **+0,0042 puntos porcentuales por
año** y **r = +0,34**. O sea: hay una tendencia creciente y es débil. Esto es
bueno. Un `r = 0,95` haría la clase 2 innecesaria.

#### Trampas de este dataset

**(a) El léxico es el instrumento de medición, y lo escribimos nosotros.**
Está en `preparar_corpus.LEXICO`, a la vista, versionado. `seguridad` tiene
23 palabras. Si sacás "policía", la serie cambia. Si agregás "orden", cambia
más. **Ninguna de esas listas es neutral.** Es exactamente el problema que
Jacobs & Wallach (2021) llaman medición: entre el constructo "cuánto le
importa la seguridad a este gobierno" y el número que sale hay una lista de
palabras que escribió una persona un martes. Cambiala en clase y mostrá que
la conclusión se mueve. Eso es la clase 10, sembrada desde la clase 1.

**(b) Hay ceros exactos y no significan lo que parece.**
2002 y 2009 dan `seguridad = 0.000`. No quiere decir que no hubo inseguridad
en 2002. Quiere decir que en ese discurso, con ese léxico, no apareció
ninguna de esas 23 palabras. Un cero en una serie de proporciones casi
siempre es un problema de instrumento, no un hallazgo.

**(c) Suavizar cambia la pregunta.**
La serie cruda responde "cuánto habló de esto **ese año**". La suavizada
responde "en qué parte del período **el tema estaba en agenda**". Las dos
son legítimas; usar una y reportar la otra, no. Está documentado en el
docstring de `media_movil()`.

**(d) n = 36.** Treinta y seis observaciones. Cualquier cosa que ajustes con
más de un puñado de parámetros va a sobreajustar, y esa es precisamente la
lección de la clase 4. No es un defecto del dataset: es la escala real a la
que trabaja muchísima investigación social.

---

### 1.3 `prensa` — noticias en castellano con etiquetas

**Qué es.** El **Spanish Fake News Corpus 2.0**: notas de prensa en
castellano recolectadas entre noviembre de 2020 y marzo de 2021, etiquetadas
como verdaderas o falsas, con tema, medio, titular, texto completo y enlace.
Cubre variantes de castellano de México, Argentina, España, Colombia, Chile,
Perú, Uruguay y otros.

**Quién lo hizo.** Gómez-Adorno, Posadas-Durán, Bel-Enguix y Porto-Capetillo
(UNAM / IPN), para la tarea compartida **FakeDeS @ IberLEF 2021**.
Repositorio: [github.com/jpposadas/FakeNewsCorpusSpanish](https://github.com/jpposadas/FakeNewsCorpusSpanish)

**Licencia.** **CC BY 4.0.** Se puede usar y redistribuir citando. Citas
obligatorias en `recursos/bibliografia.md`.

**Tamaño.** 1543 notas en el original; **1471** después de tirar las que no
tienen titular. 694 falsas / 777 verdaderas.

**Formato.** `muestras/prensa/titulares-prensa-es.csv`, con columnas:
`id, categoria, categoria_original, tema, tema_original, fuente, titular,
frac_mayusculas, largo_texto, texto_recortado, particion_original`.

**Estado de la URL:** `raw.githubusercontent.com/jpposadas/...` →
**VERIFICADA-OK** (los tres `.xlsx` bajaron y se leyeron).

#### Trampas de este dataset — leé esta sección entera

Este dataset es el mejor material de la clase 10 que hay en el curso, y lo es
porque **sus trampas son espectaculares**. Todos los números de acá se
calcularon sobre el corpus, no son estimaciones.

**(a) LA GRANDE: la fuente predice la etiqueta casi perfecto.**
Hay 346 medios distintos. **332 de ellos (96%) aparecen con una sola clase.**
Las notas "falsas" vienen sobre todo de *El Dizque*, *El Ruinaversal*,
*Hay noticia*, *Censura 0*. Las "verdaderas", de *El País*, *El Universal*,
*Excélsior*, *Milenio*, *Forbes*.

Ahora bien: **El Dizque y El Ruinaversal son sitios de sátira**, no de
desinformación. Publican noticias falsas a propósito y con eso hacen humor.

Entonces, ¿qué aprende un clasificador entrenado acá? Casi seguro:
*"¿esto está escrito con el estilo de un sitio de sátira mexicano?"*.
Y va a dar un F1 hermoso. Y no va a ser un detector de desinformación:
va a ser un detector de registro humorístico. Ese es el hueco entre el
constructo que querés medir y lo que el modelo efectivamente usa.
Es el Caso 1 de `viz/validez-de-constructo.html` con datos reales.

> **Regla para el notebook de la clase 9:** entrenar una vez con la fuente
> disponible y otra vez sin ella, y mostrar la caída. Si no cae, algo está mal
> en tu evaluación.

**(b) LAS MAYÚSCULAS.** 103 titulares están escritos en más del 90% de
mayúsculas. **92 son falsos y 11 verdaderos.** Una regla de una línea
—"si grita, es falso"— ya te da más que el azar. Por eso el CSV trae la
columna `frac_mayusculas` calculada: para que la trampa esté a la vista y no
haya que descubrirla con un debugger.

**(c) EL LARGO.** Mediana del texto: 1.622 caracteres en las falsas, 2.581 en
las verdaderas. Otro atajo que no tiene nada que ver con la verdad de la nota.

**(d) Las etiquetas venían inconsistentes entre archivos.**
`train.xlsx` y `development.xlsx` usan `Fake`/`True`; `test.xlsx` usa
`False`/`True`. Si concatenás los tres sin mirar, te quedan **tres** clases
donde hay dos. Los temas, peor: inglés en train/dev (`Politics`, `Society`)
y castellano en test (`Política`, `Sociedad`), con y sin tilde. Sin
normalizar aparecen 16 temas donde hay 12.
`descargar.py` lo unifica **y guarda el valor original al lado**
(`categoria_original`, `tema_original`) para que la corrección sea auditable.
Esto no es una anécdota de programación: es lo que pasa siempre que juntás
archivos que armó gente distinta en momentos distintos.

**(e) Ventana temporal de cinco meses, y esos meses son la pandemia.**
Noviembre 2020 a marzo 2021. `Covid-19` es el segundo tema más frecuente
(192 notas). Un modelo entrenado acá aprende, entre otras cosas, el
vocabulario de esa coyuntura. No lo apliques a 2026 sin revalidar.

**(f) Desbalance de temas.** `Politica` 413, `Sociedad` 322, `Covid-19` 192…
y `Ambiental` 3. Con tres casos no se estima nada.

**(g) El corpus está balanceado en clases, el mundo no.**
694 falsas contra 777 verdaderas: casi mitad y mitad. En la circulación real
de noticias la desinformación es **muchísimo** más rara. Esa es exactamente
la situación que muestra el slider de prevalencia de
`viz/matriz-de-confusion.html`: el mismo modelo, la misma calidad, y la
precisión se desploma cuando el fenómeno es raro. Este corpus es el caso de
laboratorio; tu campo es el otro.

**(h) `*NUMBER*`.** El corpus fuente reemplazó algunos números por el
literal `*NUMBER*`. Aparece en ~13% de los titulares de las dos clases.
Si tokenizás sin mirar, `*NUMBER*` se convierte en tokens raros.

#### La submuestra doblemente codificada

`muestras/prensa/doble-codificacion-SIMULADA-100.csv` — 100 casos con dos
columnas de codificación para practicar el cálculo de kappa de Cohen.

> **Está en el nombre del archivo y lo repetimos acá: los dos codificadores
> son SIMULADOS.** No hubo dos personas codificando. Se generaron con
> `random.Random(1983)` y tasas de acierto de 0,88 y 0,82 contra la etiqueta
> del corpus. Da acuerdo observado 0,73 y **kappa = 0,46**.
>
> Sirve para que el aula calcule kappa con datos que tienen la forma correcta
> y para discutir qué significa un kappa de 0,46 (respuesta corta: "moderado",
> y en muchas revistas, insuficiente para publicar sin discutirlo).
> **No sirve** para afirmar nada sobre la confiabilidad del corpus real.
> Si alguien reporta este kappa como si fuera de codificadores humanos,
> es fraude.

---

### 1.4 `casarosada` — discursos presidenciales recientes

**Qué es.** 1311 discursos presidenciales argentinos, 2015-2024, con orador y
fecha, scrapeados del sitio oficial de la Casa Rosada.

**Quién lo hizo.** [github.com/jmdieguez/discursos](https://github.com/jmdieguez/discursos)

**Licencia.** **Sin licencia declarada.** Los textos son discursos públicos de
funcionarios en ejercicio, publicados por el Estado. Se usa con fines
educativos. Marcado como riesgo: si el curso se publica, verificar.

**Tamaño.** 10,5 MB completo. En `muestras/` van 123 discursos recortados a
2500 caracteres (300 KB).

**Estado de la URL:** `raw.githubusercontent.com/jmdieguez/...` →
**VERIFICADA-OK**.

**Para qué sirve.** Complementa a (1.1) con la década reciente y con **varios
discursos del mismo orador**, que es lo que hace falta para la partición por
grupo de la clase 4 y para el modo "dos épocas" de la viz de embeddings.

#### Trampas de este dataset

**(a) Tres oradores, y uno tiene 13 discursos.**
Macri 655, Alberto Fernández 643, Milei 13. Cualquier clasificador de
"quién habla" que entrenes acá va a ignorar a Milei. La muestra versionada
incluye **los 13** a propósito, para que el desbalance se vea en pantalla en
vez de esconderse en una media.

**(b) Orador y período están confundidos casi perfecto.**
Macri habla en 2015-2019, Fernández en 2019-2023, Milei en 2023-2024. Un
modelo que "detecta al orador" puede estar detectando el año: cambió el
vocabulario de coyuntura, cambió la pandemia, cambiaron los temas.
**Este es literalmente el Caso 2 de `viz/validez-de-constructo.html`**
(el confusor temporal), disponible con datos reales del curso.

**(c) Es lo que el gobierno decidió publicar.**
Un sitio oficial no sube todo. Faltan las declaraciones informales, lo que se
dijo y después se bajó, y todo lo que no pasó por el equipo de comunicación.
Sesgo de selección del emisor, no del recolector.

**(d) El repo original trae columnas de sentimiento (POS/NEG/joy/anger…).**
**Esas columnas no son datos: son la salida de un modelo** (pysentimiento).
Están excluidas de nuestra muestra. Si alguien las usa como variable
dependiente sin decir que las produjo un modelo, cometió el error que la
clase 10 entera intenta evitar. Mencionalo: es un ejemplo perfecto y está
a un clic.

---

### 1.5 `aguasclaras` — el corpus sintético, y por qué existe

> **PAÍS FICTICIO. PERSONAS FICTICIAS. PARTIDOS Y LEYES FICTICIOS.**
> Rotulado como sintético en la slide, en el notebook y al pie de todo
> gráfico que salga de acá. Sin excepciones.

**Qué es.** Debates parlamentarios de la República de Aguasclaras, un país
que no existe: 159 sesiones, 1,10 MB de texto, 60 diputadas y diputados,
6 partidos, 10 provincias, 14 leyes. Más 1400 titulares de prensa de sus
cinco diarios. Generado por `datos/generar_aguasclaras.py` con semilla fija
(1983) a partir de gramáticas y plantillas.

**Quién lo hizo.** El equipo del curso.
**Licencia.** Es nuestro. Usalo.

**Por qué existe, si tenemos 8 MB de discursos reales.**
Por una sola razón, y es decisiva. La demostración central de la clase 8 es
poner **la verdad al lado de la invención**:

> El modelo genera "el diputado Berrutti, del Frente Ribereño, presentó el
> proyecto…". Abrimos `verdad.json`. Berrutti no está. El Frente Ribereño
> no existe. Y abajo se ve la distribución de probabilidad en el momento
> exacto de la invención, mostrando que el modelo estaba **muy seguro**.

Eso es **imposible con un corpus real**, porque nadie en el aula puede
verificar en cinco segundos si un diputado argentino existe o no. Acá sí:
`verdad.json` tiene el padrón completo, porque lo escribimos nosotros.
Conocer el proceso generador es todo el argumento.

Segundo uso: red de seguridad. `aguasclaras()` **no toca la red nunca**. Si
falta, se regenera.

**Archivos.**
- `debates.txt` — 1,10 MB, 159 sesiones.
- `verdad.json` — el padrón: 60 diputados, 6 partidos, 14 leyes, 5 diarios.
- `prensa.csv` — 1400 titulares con `menciona_protesta` (34,7% positivos).

#### Trampas de este dataset — o sea, qué se pierde por ser sintético

**(a) El vocabulario es pobre.** 849 palabras distintas en 176.000 tokens.
Un corpus real de ese tamaño tendría 10 a 20 veces más. Consecuencia
concreta: **el mini-GPT va a aprender más rápido y mejor de lo que
aprendería con texto real, y eso da una impresión falsa de lo fácil que es.**
Decilo en clase. El antídoto está a mano: `corpus-mini-gpt.txt` es texto
real y se puede entrenar el mismo modelo encima para comparar.

**(b) No hay ironía, ni chicanas espontáneas, ni erratas, ni las frases
raras que hacen que el castellano real sea difícil.** Sale de plantillas.
Se nota si lo leés con atención, y está bien que se note.

**(c) Las posiciones ideológicas son caricaturas legibles.** Elegidas para
que el aula pueda distinguir bloques sin ser especialista. La política real
no se ordena tan prolijamente.

**(d) NUNCA sirve para una conclusión sustantiva.** Ni una. Sirve para
entender **la máquina**, no para estudiar **la sociedad**. Si alguien saca
un gráfico de "polarización en Aguasclaras" y lo interpreta, entendió al
revés para qué está.

**(e) La etiqueta `menciona_protesta` es circular.** Se derivó por palabras
clave de las mismas plantillas que generaron el titular. Un clasificador va
a dar casi 1,00 de F1 y eso **no significa nada**: está redescubriendo la
regla con la que se armó la etiqueta. Es un buen ejercicio de humildad y un
pésimo benchmark. Para clasificación de verdad está (1.3), que es real.

---

### 1.6 `fashion-mnist` — el sandbox de la clase 5

**Qué es.** 70.000 imágenes de 28×28 en escala de grises, 10 categorías de
prendas. **Es un sandbox técnico explícitamente rotulado como tal**: sirve
para ver qué hace una convolución en dos minutos de CPU, y después se vuelve
al dominio. No es un dato de ciencias sociales y no hay que pretender que lo sea.

**Quién lo hizo.** Zalando Research. **Licencia: MIT.**

**Cómo se baja.** Desde `raw.githubusercontent.com/zalandoresearch/fashion-mnist`,
que es la única puerta abierta. **VERIFICADA-OK** (26,4 MB el archivo de train).
No se versiona en `muestras/`: 30 MB es demasiado.

> **Ojo con torchvision.** `torchvision.datasets.FashionMNIST` baja de
> `fashion-mnist.s3-website.eu-central-1.amazonaws.com`, que está
> **BLOQUEADO en el contenedor de construcción** (en Colab suele andar).
> Por eso `descargar.fashion_mnist()` no usa torchvision: baja los `.gz`
> de GitHub y los parsea con numpy en seis líneas. Que además es mejor
> pedagogía: se ve que un dataset de imágenes es un array de bytes.

#### Trampas de este dataset
**(a) Es demasiado fácil y demasiado limpio.** Centrado, mismo tamaño, mismo
fondo, sin oclusiones, balanceado perfecto. Ninguna foto que vayas a analizar
en tu investigación se parece a esto. La distancia entre "anda en
FashionMNIST" y "anda en fotos de archivo" es la mitad del trabajo real.

**(b) Las clases se confunden entre sí de manera sistemática**
(camisa / remera / pullover / abrigo). Eso está bueno: es la excusa para
mirar la matriz de confusión antes de la clase 9.

---

## 2. Estado de las URLs (verificado con `curl`, no de memoria)

Probado el 2026-08-29 desde el contenedor de construcción con
`curl -sS -o /dev/null -w '%{http_code}' <url> --max-time 20`.

| Host | Estado | Nota |
|---|---|---|
| `raw.githubusercontent.com` | **VERIFICADA-OK** (200) | Es la puerta por la que entra **todo** el curso. |
| `api.github.com` (scoped) | parcial | Solo endpoints del repo propio. No se usa. |
| `pypi.org`, `files.pythonhosted.org` | **VERIFICADA-OK** (200) | `pip install` funciona. |
| `ossci-datasets.s3.amazonaws.com` | **VERIFICADA-OK** (200) | MNIST clásico, por si hace falta. |
| `storage.googleapis.com` | **VERIFICADA-OK** (200) | |
| `github.com` (web) | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | Andá por `raw.` |
| `codeload.github.com` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | Sin tarballs. |
| `huggingface.co` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | **Probablemente ande en Colab.** Ver §3. |
| `datasets-server.huggingface.co` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | idem |
| `es.wikipedia.org`, `dumps.wikimedia.org` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | |
| `www.hcdn.gob.ar` (Diputados) | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | Fuente primaria de (1.1). |
| `www.casarosada.gob.ar` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | Fuente primaria de (1.4). |
| `zenodo.org`, `dataverse.harvard.edu` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | |
| `www.gutenberg.org`, `archive.org` | **BLOQUEADA-EN-ESTE-CONTENEDOR** (403) | |
| `fashion-mnist.s3-website...amazonaws.com` | **BLOQUEADA-EN-ESTE-CONTENEDOR** | El default de torchvision. Ver §1.6. |

**Regla de la casa:** ninguna URL entra a un `referencias.md` sin `curl`
exitoso o sin la marca `[VERIFICAR URL]` bien visible.

---

## 3. Las clases 9 y 10 necesitan Hugging Face

Las clases 9 y 10 usan modelos pre-entrenados en castellano (BETO,
RoBERTuito, modelos de embeddings de oración). **`huggingface.co` está
bloqueado en el contenedor de construcción**, así que no pudimos verificar
esas descargas acá.

En **Colab sí anda** (es el uso normal de Colab), pero el equipo de las
clases 9 y 10 tiene que **verificarlo con un Colab real antes de dar la
clase**, y dejar anotado en su `referencias.md` qué modelo, qué versión y
qué revisión usaron. Citar un modelo sin su versión es como citar un libro
sin edición.

**Plan B si HF no está disponible el día de la clase:** hay dos caminos y
los dos enseñan lo mismo, que es evaluación.
1. Embeddings propios entrenados sobre `corpus-mini-gpt.txt` (PPMI + SVD con
   numpy, sin dependencias) + regresión logística de scikit-learn. Es la
   curva "embeddings + regresión logística" de
   `viz/zero-shot-vs-finetune.html` y **da mejor que fine-tuning con pocas
   etiquetas**, que es justamente el aha de esa viz.
2. TF-IDF + regresión logística como piso de comparación. Obligatorio de
   todos modos: sin un piso, un F1 de 0,82 no significa nada.

---

## 4. De dónde saca los datos cada clase

> **Desde un notebook usá `ssdl.datos`, no `descargar` directamente.**
> `datos/descargar.py` es la capa de abajo: baja, cachea y cae a muestras.
> `ssdl.datos` la envuelve y te devuelve arrays de numpy listos. La tabla de
> acá abajo nombra las funciones de la capa de abajo; el equivalente en
> `ssdl.datos` es casi siempre el mismo nombre. Las dos excepciones tienen
> **alias**, así que cualquiera de los dos nombres funciona:
>
> | `datos/descargar.py` | `ssdl.datos` |
> |---|---|
> | `prensa_titulares()` | `titulares_prensa()` *(y `prensa_titulares()`)* |
> | `corpus_discursos_texto()` | `corpus_mini_gpt()` *(y `corpus_discursos_texto()`)* |


| Clase | Dataset | Llamada |
|---|---|---|
| 1 · funciones y parámetros | serie de `seguridad`, cruda | `descargar.serie_menciones()` |
| 2 · componer funciones | serie de `inflacion_suave` | `descargar.serie_menciones()` |
| 3 · loss y gradiente | **la misma serie de la clase 1** | `descargar.serie_menciones()` |
| 4 · entrenar de verdad | **la misma otra vez**, ahora particionada · + titulares para el gancho | `serie_menciones()` · `prensa_titulares()` |
| 5 · imágenes | FashionMNIST (sandbox) | `descargar.fashion_mnist()` |
| 6 · texto y embeddings | discursos 1984-2019, por décadas | `corpus_discursos_texto()` |
| 7 · attention | oraciones del corpus de la clase 6 · pesos del modelo de la clase 8 | `corpus_discursos_texto()` |
| 8 · mini-GPT | **Aguasclaras** (para la alucinación) · discursos reales (para comparar) | `aguasclaras()` · `corpus_discursos_texto()` |
| 9 · pre-entrenados | 1471 notas de prensa reales | `prensa_titulares()` |
| 10 · criterio y ética | **el clasificador de la clase 9, ahora como objeto de auditoría** · discursos de Casa Rosada para el confusor temporal | `prensa_titulares()` · `discursos_casarosada()` |

La continuidad de las clases 1 a 4 **sobre el mismo dataset** no es una
comodidad: es el pago emocional del módulo. El estudiante ve el mismo
problema resuelto cuatro veces, cada vez mejor. No lo cambien.

---

## 5. Archivos de este directorio

```
datos/
  README.md                  este archivo
  descargar.py               una función por dataset, con cache y fallback
  preparar_corpus.py         limpieza, medición, particiones (28 doctests + informe)
  generar_aguasclaras.py     el corpus sintético, con su justificación adentro
  cache/                     descargas (NO versionado)
  muestras/                  5,2 MB versionados — la red de seguridad
    series/
      menciones-por-tema-apertura.csv        107 filas, 1854-2019
      menciones-democracia-1984-2019.csv     36 filas — clases 1 a 4
    discursos-apertura/
      corpus-mini-gpt.txt                    2,2 MB, 1984-2019 — clases 6 a 8
      1869-…, 1916-…, 1989-…, 2018-…         un discurso por razón documentada
      2005-…, 2006-…                         el par duplicado, como evidencia
    prensa/
      titulares-prensa-es.csv                1471 notas reales, CC BY 4.0
      doble-codificacion-SIMULADA-100.csv    para practicar kappa (simulado)
    casarosada/
      discursos-muestra.csv                  123 discursos 2015-2024
    aguasclaras/
      debates.txt  verdad.json  prensa.csv   SINTÉTICO
```

Cada `.txt` suelto de `discursos-apertura/` arranca con dos líneas de
comentario que dicen **por qué ese discurso está en la muestra**. No hay
archivos ahí "porque sí".

---

## 6. Cómo se cita

- **Discursos de apertura:** recopilación de lucariel,
  `github.com/lucariel/discursos_presidenciales`; textos: mensajes
  presidenciales al Congreso de la Nación Argentina. Sin licencia declarada.
- **Prensa:** Gómez-Adorno, H., Posadas-Durán, J. P., Bel-Enguix, G., &
  Porto-Capetillo, C. (2021). *Overview of FakeDeS at IberLEF 2021*.
  Procesamiento del Lenguaje Natural, 67, 223-231. **CC BY 4.0.**
- **Casa Rosada:** `github.com/jmdieguez/discursos`. Sin licencia declarada.
- **FashionMNIST:** Xiao, H., Rasul, K., & Vollgraf, R. (2017).
  *Fashion-MNIST: a novel image dataset…* arXiv:1708.07747. **MIT.**
- **Aguasclaras:** corpus sintético del curso, `datos/generar_aguasclaras.py`,
  semilla 1983. **Declararlo sintético siempre.**
