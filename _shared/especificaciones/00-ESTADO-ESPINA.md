# Estado de la espina del curso

**Verificación adversarial de la base compartida antes de construir las 10 clases.**
Todo lo que dice acá se comprobó **corriendo el código**, no leyéndolo: Chromium
vía Playwright con `page.route` interceptando cualquier salida a la red,
`unittest`, `doctest`, `nbconvert --execute`, `curl` contra cada host, y mirando
los PNG con los ojos.

> **Si construís una clase, leé por lo menos las secciones 1, 4 y 5.** La 5 es la
> lista de trampas: cada una es un error que ya cometió alguien y que, sin este
> documento, cometerías vos también.

---

## 1. Veredicto

**La base está lista para que se construyan las diez clases encima.**

Se encontraron y **se arreglaron** 10 cosas: **3 defectos de código** (1
bloqueante, 2 importantes), **4 incoherencias de contenido** que se contradecían
entre documentos, y **3 huecos** (tres archivos prometidos que no existían, el
motor de la viz central de la clase 6, y la slide de pausa). El detalle está en
la sección 2. Lo que queda abierto está en la 6 y **ninguna de esas cosas frena a
un equipo de clase**.

| Chequeo | Resultado |
|---|---|
| Assets offline (`file://`, cero CDN) | **0 requests externos** en todo el material, tema claro y oscuro |
| Consola del navegador | **0 errores** en `index.html`, `demo.html`, slides y viz **en su ubicación real** |
| KaTeX | renderiza desde el vendor, sin red (verificado por screenshot) |
| viz.js — API pública | las **85** funciones y métodos invocables se ejercitaron una por una (24 `Viz.*` + 33 de `Plano` + 16 de `Viz.M` + 6 de `Red` + 6 de `Viz.svg`) |
| viz.js — interacción | sliders, drag, tooltip, clic, select, checkbox, botones, animación: **todo responde** |
| viz.js — red en el navegador | `sin(x)` con 8 rampas: loss **6,19 → 0,026** en 800 pasos |
| Tests de Python | **119 tests, todos pasan** (incluidos doctests) |
| `preparar_corpus.py` | **28 doctests, todos pasan** + informe real sobre los datos |
| Figuras de `graficos.py` | **17 generadas y miradas**, 0 warnings |
| Notebook plantilla | `nbformat` válido · `nbconvert --execute` **0 errores, 5 figuras** |
| Datos sin red y sin cache | los **9** cargadores de `ssdl.datos` devuelven datos igual |
| Corpus para el mini-GPT | **2,2 MB** (el mínimo pedido era 400 KB) |
| Semántica de color | `curso.css` = `viz.js` = `ssdl/graficos.py`, **los 8 tokens coinciden** |
| Presupuestos de tiempo | los 10 planes suman **exactamente 120 min** y son continuos |

---

## 2. Qué se arregló

### Bloqueante

**1. `p.poligono()` reventaba la página entera.**
`{relleno: true}` terminaba en `color(true)` → `nombre.indexOf is not a function`,
una excepción sin atrapar adentro de `alDibujar`. Consecuencia: **el resto del
dibujo no se dibujaba** y la slide quedaba en blanco sin ningún mensaje útil.
Además `poligono` era el único primitivo que **ignoraba `op.color`**.
*Arreglado:* `Viz.color()` ahora devuelve el color por defecto ante cualquier
cosa que no sea texto en vez de tirar excepción; `poligono` acepta `color`,
`relleno: true|false|<color>`, `borde: true|<color>` y `opacidad`.

### Importante

**2. `scatter_clases` y `frontera_de_decision` pintaban las clases al revés.**
Con los mismos `X, y`: en una, clase 0 = azul; en la otra, clase 0 = rojo. Un
estudiante que dibuja la nube y después la frontera de su propio modelo **lee
cada acierto como un error**. Pasa en las clases 4, 5, 9 y 10.
*Arreglado:* una sola fuente, `graficos.colores_clases()`, usada por las dos, y
el fondo de la frontera ahora va del color de la clase 0 al de la clase 1, así
que puntos y fondo coinciden. Sigue el tema claro/oscuro.

**3. `{tipo:'botones'}` se dibujaba pero no guardaba nada.**
Se lee como un selector segmentado (es lo que parece), pero sólo era una fila de
botones de acción: no registraba valor en `ctl.valores` ni marcaba el activo.
*Arreglado:* con `valor` es un selector de verdad (guarda, marca `activo`,
responde a `ctl.set`); sin `valor` sigue siendo una fila de acciones.

### Contenido

**4. `PROGRAMA.md` y dos especificaciones se contradecían.**
En la clase 3, el programa ponía el paisaje de la loss antes del primer bloque
práctico y el guion de slides lo ponía después. En la clase 6, el mapa de
palabras estaba antes de tokenizar. *Arreglado:* los dos planes se reescribieron
para seguir el orden del guion (que es el correcto: no podés mirar el mapa antes
de tokenizar), y ahora los 10 suman 120 min exactos.

**5. La clase 8 declaraba tres tamaños distintos para el mismo modelo.**
3 millones de parámetros en la slide 3, ~1,5M en la spec del notebook, y las
clases 3, 7 y 9 citaban "3M". *Arreglado:* **~1,5M en todo el curso**, que es lo
que da la configuración del notebook. También el bloque práctico 2 decía "30
minutos" cuando su casilla es de 25.

**6. La plantilla de viz enseñaba una escala imposible.**
Dibujaba "menciones a inflación" llegando al **14 % de las palabras del
discurso**, cuando la serie real va de 0 a 0,44 %. Diez equipos iban a copiar
esa escala. *Arreglado:* el ejemplo usa ahora la escala real, y el número de
referencia del panel ("lo mejor con una sola rampa") se **midió por barrido**
(0,00165) en vez de estimarse.

**7. La afirmación del `md5sum` de 2005/2006 era verificable-falsa en `muestras/`.**
Es cierta en el corpus fuente (mismo hash, comprobado), pero las dos muestras
llevan cabeceras distintas, así que un estudiante que corriera `md5sum` sobre
`muestras/` obtenía hashes distintos. *Arreglado* en el archivo y en
`datos/README.md`.

### Faltaban

**8.** `index.html`, `recursos/glosario.md` y `recursos/bibliografia.md`, los tres
prometidos en `README.md` y en `PROGRAMA.md`. **Escritos.** El glosario viene
sembrado con los ~110 términos de las diez clases, organizados por clase en que
aparecen, más una tabla de falsos amigos (*bias* parámetro vs sesgo social,
validación vs test, precisión vs exactitud).

**9.** `ssdl.datos.embeddings_ppmi_svd()` y `vecinos()`, **el motor de la viz
central de la clase 6**, no existían: el informe de datos los medía en un script
que no quedó en el repo. **Escritos, testeados (5 tests nuevos) y verificados**:
4.000 palabras del corpus real en ~25 s en CPU, con los vecinos que el informe
prometía. Son además el plan B de la clase 9 si Hugging Face no está.

**10.** La slide de pausa. Las diez clases reservan 10 minutos de pausa y ninguna
tenía dónde marcarla. **Agregada** al CSS (`section.pausa`, clara y oscura) y a
la plantilla de slides.

---

## 3. La API que vas a usar

### `viz.js` — verificada función por función

Todo esto se ejercitó en una página de prueba que llamó a cada método con y sin
opciones. **Cero errores.**

**Plano** · `Viz.plano(cont, {xmin,xmax,ymin,ymax,ejeX,ejeY,titulo,alto,margen,cuadrado})`
```
p.fondo p.grilla p.ejes p.curva p.linea p.poligono p.puntos p.punto p.segmento
p.flecha p.texto p.textoPx p.barras p.celdas p.mapaDeCalor p.contornos p.leyenda
p.px p.py p.aMundo p.escalaX p.escalaY p.limites p.autoescala p.limpiar
p.alDibujar p.redibujar p.redibujarYa p.redimensionar
```

**Interacción** · `p.arrastrables(pts,{radio,fijarX,fijarY,acotarX,acotarY,alArrastrar,alSoltar})` · `p.tooltip(fn)` · `p.alClic(fn)` · `p.alMover(fn)` · `Viz.mostrarTooltip` · `Viz.ocultarTooltip`

**Controles** · `Viz.controles(cont, defs, alCambio)` → `.valores .set(id,v[,silencioso]) .get(id) .on(fn) .texto(id,html) .medidor(id,t,etiq) .disparar() .nodos`
Tipos: `slider` (con `escala:'log'`, `sub`, `formato`, `color`, `decimales`), `checkbox`, `select`, `boton`, **`botones`** (selector si lleva `valor`), `titulo`, `texto`, `medidor`.

**Animación** · `Viz.animacion({paso,reset,cadaMs,hasta})` → `.play() .pausa() .alternar() .unPaso() .reset() .corriendo() .iteracion() .on(fn)` · `Viz.controlesAnimacion(cont, anim, textos)`

**Colores** · `Viz.color(n)` `Viz.colores()` `Viz.recargarColores()` `Viz.alfa(c,a)` `Viz.mezclarColor(a,b,t)` `Viz.paleta('loss'|'divergente'|'acento'|'grises')`

**SVG** · `Viz.svg.crear` `.el` `.arco` `.limpiar` — **Matriz DOM** · `Viz.matrizCalor`

**Álgebra** · `Viz.M`: `matmul transponer ceros aleatoria dot norma coseno softmax(v,T) sigmoid dsigmoid tanh dtanh relu drelu mse mae`

**Red** · `new Viz.Red([1,8,1],{activacion,semilla,escala})` → `.adelante(x) .predecir(X) .perdida(X,Y) .paso(X,Y,lr) .rampas() .reiniciar(semilla)`

**Utilidades** · `Viz.azar(s) Viz.gauss(s) Viz.linspace Viz.rango Viz.acotar Viz.mezclar Viz.num Viz.el Viz.nodo Viz.botonTema() Viz.detectarEmbebido()`

### `ssdl` — Python, 119 tests en verde

`utils` · `fijar_semilla` `elegir_device` `contar_parametros` `medir_tiempo` `estamos_en_colab` `estamos_en_notebook` `raiz_del_repo` `resumen_del_entorno` `formatear_cantidad` `formatear_duracion` · `SEMILLA_DEL_CURSO = 1983`

`datos` — **carga** (nunca falla por red): `serie_menciones` `serie_completa` `discursos_apertura` `corpus_mini_gpt` `discursos_casarosada` `titulares_prensa` `debates_aguasclaras` `prensa_aguasclaras` `verdad_aguasclaras`
**texto**: `TokenizadorCaracteres` `TokenizadorPalabras` `vocabulario`
**embeddings propios (nuevo)**: `matriz_de_coocurrencia` `embeddings_ppmi_svd` `vecinos`
**splits**: `particion` `particion_temporal` `particion_por_grupo` `diagnostico_de_fuga`
**juguetes**: `espiral` `dos_lunas` `circulos_concentricos` `xor` `recta_con_ruido` `curva_de_dos_picos` `a_tensores`
**alias**: `prensa_titulares` `corpus_discursos_texto`

`graficos` · `estilo_curso` `figura` `guardar` `paleta` **`colores_clases`** `plot_funcion` `plot_familia` `plot_serie` `plot_ajuste` `scatter_clases` `frontera_de_decision` `superficie_de_loss` `plot_loss_1d` `curvas_de_entrenamiento` `matriz_de_confusion` `metricas_binarias` `frase_de_metricas` `proyeccion_de_embeddings` `mapa_de_atencion` `grilla_de_filtros` `mostrar_imagenes` · constantes `DATOS VERDAD MODELO PARAMETRO ERROR VAL OK ACENTO COLORES_CLASES`

`entrenamiento` · `entrenar` `evaluar` `predecir` `Historial` `ParadaTemprana` `BarraDeProgreso` `exactitud` `error_absoluto_medio` `r_cuadrado` `descenso_a_mano`

### La semántica de color, confirmada en las tres capas

| Token | Significa | Claro |
|---|---|---|
| `--c-datos` | lo observado: la nube, el corpus, los titulares | `#33302c` |
| `--c-verdad` | la verdad subyacente cuando la conocemos | `#9a9089` |
| `--c-modelo` | lo que el modelo dibuja | `#1f6fb5` |
| `--c-parametro` | las perillas: pesos, gradientes, el punto en el mapa | `#8244c4` |
| `--c-error` | el desajuste: palitos, loss, falsos positivos | `#cf3b28` |
| `--c-val` | lo que el modelo no vio: val/test/held-out | `#e08519` |
| `--c-ok` | correcto | `#2f8a56` |
| `--c-acento` | "mirá acá". Sin significado técnico | `#0d9488` |

`curso.css` manda. `viz.js` los lee del CSS en vivo (con respaldo idéntico para
`file://`), y `graficos.py` los tiene copiados **con un test que falla si
divergen**. En clasificación, clase 0 = `modelo`, clase 1 = `error`, y eso vale
para la nube y para la frontera.

---

## 4. Cómo arranca tu clase

1. Leé `PROGRAMA.md` entero, y después tu `clase-NN-*.md`.
2. **Tu presupuesto de tiempo está en la sección 1.5 de tu spec.** Sale del plan
   minuto a minuto de `PROGRAMA.md` y ya está mapeado a los números de slide. Si
   tu bloque no entra, recortá el bloque; **la pausa no se toca**.
3. Copiá las plantillas:
   - `slides-plantilla.html` → `clases/NN-slug/slides.html`
   - `viz-plantilla.html` → `clases/NN-slug/viz/loquesea.html`
   - `notebook-plantilla.ipynb` → `clases/NN-slug/notebook.ipynb` (la celda de
     bootstrap es canónica: **no la edites**)
   Las rutas relativas de las plantillas están escritas para esa profundidad y
   **están verificadas ahí**. Si abrís una plantilla en `_shared/plantillas/`
   para espiarla, se ve igual (hay un `onerror` de contención), pero la consola
   muestra un par de 404 inofensivos.
4. Cargá tus términos nuevos a `recursos/glosario.md` y tus lecturas a
   `recursos/bibliografia.md`.
5. Antes de dar tu clase por terminada, corré el checklist final de
   `GUIA-CONSTRUCCION.md` §7.

---

## 5. Las trampas que descubrí (leelas, cuestan una hora cada una)

### Del código

1. **`Viz.mezclar(a,b,t)` es interpolación lineal, no barajar un array.**
   `Viz.mezclar(0,10,.25)` → `2.5`. Para barajar usá `Viz.azar` con Fisher-Yates.
2. **`red.adelante(x)` devuelve `{A, Z, salida}`, no un array.** El vector de
   salida es `.salida`. `.predecir(X)` sí devuelve la lista de vectores.
3. **`serie_menciones` devuelve PORCENTAJE, no fracción.** La serie de
   `seguridad` va de 0 a **0,44 por ciento**. Rotulá el eje `% de palabras` y no
   multipliques por 100 otra vez. La plantilla de viz ya usa esta escala.
4. **`ssdl.datos` y `datos/descargar.py` nombran dos cosas al revés**
   (`titulares_prensa` vs `prensa_titulares`, `corpus_mini_gpt` vs
   `corpus_discursos_texto`). Ahora hay alias en `ssdl.datos`, así que cualquiera
   de los dos anda, pero no te asustes si ves los dos nombres en la documentación.
5. **`graficos.plot_*` devuelve `ax`, no `fig`.** Para guardar: `guardar(ax.figure, ruta)`
   o `fig, ax = figura(); plot_funcion(..., ax=ax)`. Las que arman varios ejes
   (`superficie_de_loss`, `grilla_de_filtros`, `mostrar_imagenes`) devuelven
   `(fig, ejes)`.
6. **El vocabulario de embeddings respeta las tildes.** `"educación"` está,
   `"educacion"` no. `vecinos()` levanta `KeyError` con un mensaje que lo dice.
7. **Los modos embebido y standalone son el mismo archivo.** `viz.js` detecta el
   `<iframe>` solo y le pone `class="embebido"` al `<body>`; el CSS esconde
   título, pie y botón de tema. No dupliques archivos.

### De los datos

8. **Sin red, `discursos_apertura()` devuelve 6 discursos, no 108**, y
   `discursos_casarosada()` devuelve 123, no 1311. Todo corre igual, pero **no
   escribas en las slides un número que dependa de haber bajado el corpus
   completo** sin decir de dónde sale. Con red (sólo `raw.githubusercontent.com`
   pasa) baja todo y los números del `README` de datos son exactos.
9. **La fuente predice la etiqueta al 96 %** en el corpus de prensa: 332 de 346
   medios aparecen con una sola clase, y las "falsas" vienen sobre todo de
   sitios de **sátira**, no de desinformación. Un clasificador entrenado ahí
   detecta registro humorístico. Es un regalo para la clase 10 y una trampa para
   la 9 si no se dice.
10. **Los agujeros del corpus de discursos son los golpes de Estado.** Faltan 19
    de 28 años entre 1955 y 1982. Interpolar ahí es inventar discursos que nadie
    dio: *missing not at random* de manual.
11. **2005 y 2006 son el mismo discurso** (mismo `md5sum` en el corpus fuente).
    Partir al azar mete 5 presidentes compartidos y 1 duplicado exacto entre
    train y test; partir por tiempo o por grupo da 0. Es la demostración de la
    clase 4 con datos propios. En `muestras/` los hashes difieren por las
    cabeceras: comparalos sin las líneas que empiezan con `#`.
12. **Aguasclaras es sintético y hay que decirlo cada vez.** Vocabulario de 849
    palabras (10-20× más pobre que el real), así que **el modelo aprende más
    fácil de lo que debería**. Su etiqueta `menciona_protesta` es circular
    (F1 ≈ 1,00 que no significa nada), y su `prensa.csv` tiene 246 titulares
    duplicados idénticos: útil como ejemplo de fuga, veneno si reportás métricas.
    La doble codificación para kappa está marcada **SIMULADA** en el nombre del
    archivo porque no hubo dos personas codificando.
13. **Los dos corpus de discursos no declaran licencia.** Los textos son actos
    oficiales del Estado argentino y el uso educativo es defendible, pero si el
    curso se publica hay que escribirle a los recopiladores. El de prensa sí es
    CC BY 4.0.

### Del entorno

14. **Desde este contenedor sólo se llega a `raw.githubusercontent.com`,
    `pypi.org`, `files.pythonhosted.org` y `registry.npmjs.org`.** `github.com`
    (HTML) da 403; `huggingface.co`, `arxiv.org`, `doi.org`, YouTube y Wikipedia
    no responden. Por eso las referencias están marcadas `[VERIFICAR URL]` en vez
    de tener enlaces inventados. **Verificá con `curl` antes de afirmar que una
    URL anda.**
15. **Las clases 9 y 10 necesitan Hugging Face en el aula, y acá no se puede
    probar.** El plan B está escrito y **el motor existe y está testeado**:
    `embeddings_ppmi_svd` + regresión logística, más TF-IDF como piso. Ver
    `datos/README.md` §3.

---

## 6. Lo que queda abierto (nada de esto frena a un equipo)

| # | Qué | Para quién |
|---|---|---|
| 1 | Las 56 marcas `[VERIFICAR]` de `recursos/bibliografia.md` (68 contando las repetidas en los `referencias.md` de clase). Las citas están completas; faltan los enlaces. **Si una obra no aparece, se saca la cita: no se le inventa un enlace.** | quien tenga red |
| 2 | Las clases 4, 8 y 10 no tienen slide "Glosario de hoy"; las otras siete sí. Conviene uniformar. | equipos 4, 8, 10 |
| 3 | Nadie probó el flujo real de Hugging Face (no hay conexión). El primer equipo que corra la clase 9 en Colab tiene que confirmar los nombres de modelo en castellano (BETO, pysentimiento). | equipo 9 |
| 4 | El notebook de la clase 8 declara ~10 min de entrenamiento en CPU con ~1,5M de parámetros. Lo medido acá fue un modelo de 640 K en 45 s; **el número grande hay que medirlo** cuando el notebook exista. | equipo 8 |
| 5 | La clase 6 es la más apretada: 36 slides y un bloque de contenido nuevo (el orden, las RNN) después del segundo práctico. Si se atrasa, se recorta "las RNN en 30 segundos", **nunca el puente**. Ya está anotado en el plan. | equipo 6 |
| 6 | La licencia de los dos corpus de discursos (trampa 13). | el docente |

---

## 7. Cómo reproducir esta verificación

```bash
python3 _shared/ssdl/test_ssdl.py                 # 119 tests
python3 datos/preparar_corpus.py                  # 28 doctests + informe sobre los datos
python3 datos/descargar.py --solo-muestras        # el curso entero, sin red
python3 -m nbconvert --to notebook --execute \
        --output /tmp/out.ipynb _shared/plantillas/notebook-plantilla.ipynb
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
`NODE_PATH=/opt/node22/lib/node_modules`), abriendo por `file://` con un
`context.route('**/*')` que **aborta cualquier URL `http(s)`** y falla si alguna
sale. Copiá las plantillas a un `clases/00-prueba/` descartable para probarlas a
la profundidad real, y borralo después.
