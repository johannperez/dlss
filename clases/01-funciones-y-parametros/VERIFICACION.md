# Verificación adversarial — Clase 1

**«Una función es una máquina con perillas»** · verificado el 2026-08-29

Todo lo que dice acá se comprobó **corriendo el material**, no leyéndolo: `nbconvert
--execute` con las variables de proxy borradas, `nbformat.validate`, Chromium por
Playwright abriendo los archivos **en su ubicación real** con un
`context.route('**/*')` que aborta cualquier `http(s)`, y mirando los PNG con los
ojos (34 capturas de slides + 21 de las viz + 11 figuras del notebook).

---

## 1. Veredicto

**La clase está lista para darse en un aula.**

Se encontraron y **se arreglaron 15 problemas**: 2 que se veían en el proyector
(bloques de código cortados y una fila del glosario rota), 2 visualizaciones que
adentro de la slide se cortaban por la mitad, 4 defectos de las viz, 3 números o
frases que contradecían el dibujo que tenían al lado, 2 problemas del notebook y
2 del solucionario. El detalle está en la sección 3. Lo que queda abierto está en
la 5 y **nada de eso frena la clase**.

| Chequeo | Resultado |
|---|---|
| Los 6 entregables (+ 3 viz + `medir-referencias.py`) | **están los 10**, ninguno vacío ni a medias |
| `nbformat.validate(notebook.ipynb)` | **válido**, 40 celdas |
| `nbconvert --execute` | **0 errores**, 11 figuras, **8,0 s** (4 corridas: 7,7 / 7,8 / 8,0 / 8,2) |
| El notebook sin red **y sin `datos/cache/`** | **0 errores** y los mismos números (36 años, máx 0,436 % en 1998, promedio 0,155 %) |
| `slides.html` en su ruta real, 35 slides recorridas | **0 errores de consola · 0 requests externas** |
| Las 3 viz sueltas, con interacción y animación | **0 errores de consola · 0 requests externas** |
| Las 3 viz embebidas en su slide | **0 errores**, y ahora **entran enteras** en el iframe |
| Tema claro / oscuro (`prefers-color-scheme` desde la carga) | ambos, en slides y en las 3 viz |
| Proyector 1280×720 y 1024×640 · ventana angosta 900×600 y 700×900 | legible en los cuatro |
| Código de las slides idéntico al del notebook | `recta()` y `desajuste()`: **idénticos** |
| URLs de `referencias.md` | 2 afirmadas como verificadas, **las dos dan 200 por `curl`**; el resto sigue marcado |
| Números de las slides / viz / notebook / solucionario | **todos re-medidos**, ninguno estimado |

---

## 2. Los números, re-medidos

Salen de `PYTHONPATH=_shared python3 clases/01-funciones-y-parametros/medir-referencias.py`
y de una comprobación independiente contra `ssdl.datos.serie_menciones`.

| Número | Dónde aparece | Medido |
|---|---|---|
| Piso de la recta sobre «seguridad» | slides 7 y 28, viz 1, notebook, solucionario 4 y 5 | **0,014554** → `0.0146` |
| …con qué perillas | viz 1 (botón), slide 7 | `a = 0.0040`, `b = 0.085` |
| Raya horizontal en el promedio | viz 1, notebook, solucionario 4 y 5 | **0,016490** → `0.0165` |
| Arranque de la viz 1 (`a=-0.010, b=0.350`) | slide 15, viz 1 | **0,036842** → `0.0368` |
| `desajuste(0, 0.10)` (arranque del TODO 2) | notebook | **0,019505** → `0.0195` |
| Recta «inflación» suavizada vs. raya | slide 31, notebook | **0,00150** vs **0,00152** |
| Recta «educación» (ítem 8) | cuestionario y solucionario | `a = 0.0037`, `b = 0.208`, desajuste `0.0175`, +0,131 en 35 años |
| Ítem 5: R, P, Q | solucionario | `0.0146` · `0.0165` · `0.0766` |
| Techos del zoo (6 formas × 3 desafíos) | viz 3 (botón) | los 18 coinciden con `TECHOS` |
| Desafío 1: cuántas lo sacan | notas de la slide 25 | **tres**: recta (0.0000), rampa (0.0000), sigmoide (0.0092) |
| Desafío 2: cuántas lo sacan | viz 3 | **una**: la sigmoide (0.0000) |
| Desafío 3: cuántas lo sacan | viz 3, cuestionario 11 | **ninguna**; el mejor techo es el seno, **0.213** |

La serie de emergencia escrita a mano en el notebook (por si no hay corpus)
coincide **dígito por dígito** con `serie_menciones("seguridad", 1984, 2019)`, y la
de inflación con la versión **suavizada**, que es la que el notebook pide.

Las dos URLs que `referencias.md` declara verificadas responden:

```
raw.githubusercontent.com/csev/py4e/master/README.md                        -> 200
raw.githubusercontent.com/lucariel/discursos_presidenciales/master/README.md -> 200
```

---

## 3. Los 15 problemas que había, y qué se hizo

### Se veían en el proyector

**1. Los bloques de código aparecían cortados** (slides 16 y 27). `curso.css`
estiliza `.reveal pre code` pero **no le pone `display:block`**, y `reveal.css`
tampoco: el `<code>` quedaba *inline*, el `<pre>` medía una sola línea de alto y el
`def recta(...)` se veía partido por la mitad. *Arreglado* con una regla local en
`slides.html`. **Es un defecto de `_shared/css/curso.css`**, no de esta clase: ver
sección 5.

**2. La fila «ajustar» del glosario (slide 34) estaba rota.** `.glosario-lista li`
es un grid de dos columnas y la fila traía tres hijos (`<b>`, `<i>(to fit)</i>`,
`<span>`): la definición se caía a la columna del término. *Arreglado*: el
`(to fit)` va adentro del `<span>`.

### Las viz embebidas se cortaban

**3. La viz 1, adentro de la slide 12, desbordaba el iframe en 256 px.** Se perdía
la frase que dice el piso medido y el veredicto — o sea, el segundo momento aha
entero. *Arreglado*: modo compacto para `body.embebido` (el plano baja de 400 a
288, el dibujo de la máquina se muda a la columna izquierda con más lugar, la
lectura se acorta y se saca el botón redundante). **Suelta se ve igual que antes.**

**4. La viz 3, adentro de la slide 25, desbordaba el iframe en 384 px:** la fila de
abajo —**sigmoide, seno y rampa**— quedaba invisible. Justo las tres que hacen
falta para el aha («comparar qué forma puede y qué forma no»). *Arreglado*: en modo
embebido las tarjetas se compactan (mini-plano de 88 px, sin la frase ni la fórmula
de cada forma) y **entran las seis**. Suelta —que es como las notas piden
proyectarla— sigue completa.

Los tres iframes miden hoy exactamente `scrollHeight = 610 = innerHeight`.

### Defectos de las visualizaciones

**5. Los números de las perillas se montaban sobre la caja** en el SVG de la viz 1.
*Arreglado*: la caja se calcula a partir de la posición de las perillas en vez de
estar clavada en coordenadas fijas.

**6. El rótulo `(x , f(x))` de la viz 2 se cortaba** contra el borde derecho del
panel izquierdo apenas `x > 1,5` — o sea, en la mitad del recorrido del slider.
*Arreglado*: el rótulo se da vuelta hacia la izquierda cuando el punto está a la
derecha.

**7. En la animación de la viz 2, el dibujo iba un frame atrás del texto.** El
canvas decía `f(2) = 3.84` y la frase de abajo, `3.96`. Dos números distintos para
lo mismo, en pantalla, al mismo tiempo. *Arreglado*: `redibujarYa()` en vez de
`redibujar()`.

**8. El desafío 3 del zoo se spoileaba solo.** Apenas lo elegías, el panel ya decía
«ninguna de las seis la saca». La frustración hay que ganársela. *Arreglado*: ahora
el panel invita a probar, y el «ninguna la saca, y no es culpa tuya: está medido»
aparece **recién al apretar «mostrar el techo de cada forma»**.

### Notebook

**9. El `TODO 3` venía resuelto.** El `if` de adentro del `for` ya estaba escrito,
así que no había nada que hacer. *Arreglado*: ahora el hueco es real (`if False:`,
con la pista de qué comparación va) y **el notebook sigue corriendo entero** aunque
nadie lo complete: avisa en castellano y `revisar()` da la pista.

**10. La anotación «acá arranca» se dibujaba encima de la recta.** *Arreglado*:
se corrió abajo del punto, donde no hay nada.

### Números y frases que contradecían el dibujo de al lado

**11. «Cuarenta años de algo»** (slide 3) sobre una serie de **36** años
(1984-2019). Lo mismo en `notas-docente.md` («cuarenta puntos») y en el desafío 3
de la viz 3 («cuarenta años de discursos»). *Arreglado* en los tres lugares.

**12. «Empatan»** para 0,00150 contra 0,00152 (slide 31 y notebook). Es cierto al
cuarto decimal, pero conviene decir cuál es la precisión. *Arreglado*: «empatan
hasta el cuarto decimal (0.00150 contra 0.00152)».

**13. Las tres frases de la slide 26 no describían las curvas dibujadas.** Decía
«tardó **veinte** años en completarse» sobre un eje que llega a 12 (la sigmoide con
`k=0.45` tarda **diez**), y «todavía está a mitad de camino» sobre una curva que a
los 12 años va por el 86 % (cruza la mitad a los **ocho**). *Arreglado*: las tres
frases ahora son verdad sobre el gráfico que tienen al lado.

### Solucionario

**14. El ítem 8 estaba resuelto con la pendiente al revés.** El enunciado da
`a = +0.0037` (la serie **sube**) y las respuestas modelo hablaban de «les haya
importado **menos**», «la **baja** haya sido pareja», «*La educación bajó*».
Un docente que leyera el solucionario en el aula habría enseñado lo contrario del
dato. *Arreglado*.

**15. Dos «errores típicos» del ítem 8 habían quedado huérfanos debajo de (c),**
cuando son de (b). *Arreglado*.

---

## 4. Lo que se miró y estaba bien

- **Coherencia con la especificación.** Están las 32 slides del guion, con los
  mismos títulos y en el mismo orden, más las 3 que el equipo agregó y declaró
  («De dónde venimos», la pausa, «Qué te llevás»). El presupuesto de
  `notas-docente.md` §2 **suma 120 minutos exactos** y respeta las casillas de la
  spec §1.5, con la pausa de 10 minutos en su slide propia (17).
- **El puente hacia atrás y hacia adelante son explícitos.** La clase 1 no tiene
  clase anterior: la slide 2 hace el puente hacia lo que la audiencia ya sabe
  hacer (leer un coeficiente). Hacia adelante hay tres siembras declaradas —el
  desafío 3, la rampa y la sigmoide— y la slide 35 nombra la clase 2.
- **Tono.** Voseo sostenido, humor, cero solemnidad, y ni una sola aparición de
  «no se asusten» ni de «esto es fácil» (las notas §7 los prohíben explícitamente).
  La palabra «derivada» no aparece en ninguna slide. Cada slide tiene figura,
  ejemplo concreto o pregunta.
- **El aha de cada viz se ve de verdad.** Se movió cada control, se corrió cada
  animación y se miró la captura: en la viz 1 el desajuste baja de 0,0368 a 0,0146
  y frena ahí; en la viz 2 el rastro violeta dibuja la familia; en la viz 3 el
  desafío 1 lo sacan tres formas, el 2 una y el 3 ninguna.
- **Las figuras del notebook** tienen ejes rotulados, leyendas y unidades («% de
  palabras del discurso»), y se entienden sin el texto.
- **El cuestionario se puede contestar con lo que se dio.** Los distractores no son
  absurdos: el 1-A y el 1-D son la confusión real de la clase, el 2-B («las letras
  del principio del alfabeto») es tentador porque **funciona casi siempre**, y el
  solucionario explica qué confusión revela cada uno.
- **Las citas.** Breiman (2001, *Statistical Science* 16(3), 199-231), Molina &
  Garip (2019, *Annual Review of Sociology* 45, 27-45), Grimmer, Roberts & Stewart
  (2022, Princeton UP), Jacobs & Wallach (2021, FAccT '21): las cuatro existen y
  están bien citadas. **No hay ninguna URL inventada.**
- **Cero red.** Ni un `https://` en el `src`/`href` de las slides ni de las tres
  viz; ninguna ruta absoluta.

---

## 5. Lo que queda abierto

| # | Qué | Para quién |
|---|---|---|
| 1 | **`.reveal pre code` no tiene `display:block` en `curso.css`.** Está parcheado a mano en las clases 1 y 4; las clases **2, 6, 7, 8, 9 y 10 también usan `<pre><code>`** y probablemente muestran el código cortado. Conviene arreglarlo **una vez** en `_shared/css/curso.css` y sacar los parches. | quien mantenga la espina |
| 2 | 6 de las 8 referencias siguen `[VERIFICAR URL]` / `[VERIFICAR]`. Las citas son correctas; faltan los enlaces, y desde este contenedor no se llega a 3blue1brown, projecteuclid, annualreviews ni doi.org. **No se inventó ninguno.** | quien tenga red |
| 3 | La slide 19 muestra el **escalón** como sexta forma del zoo y la viz 3 muestra la **rampa**; el escalón no se explica en ninguna slide. Las dos cosas las pide la spec (§2 slide 17 y §3.3), pero al aula le puede quedar la duda. Se arregla con una frase en la slide 19 o cambiando la miniatura. | equipo 1 o 2 |
| 4 | La slide 16 dice «abrí `notebook.ipynb`». Si el curso se publica con un link corto de Colab, hay que ponerlo ahí y en `notas-docente.md` §9. | el docente |
| 5 | Los dos corpus de discursos **no declaran licencia** (trampa 13 del ESTADO-ESPINA). `referencias.md` y `datos/README.md` §1.1 lo dicen; si el curso se publica hay que escribirle al recopilador. | el docente |
| 6 | `medir-referencias.py` no está enganchado a ningún test. Si cambian los datos o los pasos de los sliders, hay que correrlo a mano y actualizar los números en los cuatro archivos que lista su docstring. | equipo 1 |
| 7 | El ítem 6 del cuestionario **describe** la familia de curvas con palabras en vez de mostrarla. Se contesta igual, pero una imagen lo mediría mejor. | equipo 1 |
| 8 | KaTeX se carga y el plugin inicializa sin error, pero **la clase no usa ninguna fórmula con delimitadores**: la única, `f(x) = a·x + b`, está escrita como HTML monoespaciado con las partes coloreadas. Es una decisión buena para esta audiencia; queda anotado para que nadie busque un renderizado que no existe. | — |
| 9 | Embebidas en la slide, la viz 1 y la viz 3 van en **modo compacto** (la 3 esconde la frase y la fórmula de cada tarjeta). Es a propósito: no entran de otra forma en 610 px. Las notas ya piden **proyectarlas sueltas**, y sueltas están completas. | — |

---

## 6. Cómo reproducir esta verificación

```bash
# los números
PYTHONPATH=_shared python3 clases/01-funciones-y-parametros/medir-referencias.py

# el notebook, sin red y sin cache
mv datos/cache /tmp/cache_bak
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy \
  python3 -m nbconvert --to notebook --execute \
  --output /tmp/out.ipynb clases/01-funciones-y-parametros/notebook.ipynb
mv /tmp/cache_bak datos/cache
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
`NODE_PATH=/opt/node22/lib/node_modules`), abriendo por `file://`
**desde `clases/01-funciones-y-parametros/`** (la profundidad importa: las rutas son
`../../` en las slides y `../../../` en las viz), con un
`context.route('**/*')` que aborta toda URL `http(s)` y falla si sale alguna.
Para el tema oscuro, `newContext({ colorScheme: 'dark' })`: así se prueba el caso
real, que es alguien con el sistema en oscuro abriendo la página.
