# Verificación adversarial — Clase 8

**Un mini-GPT propio, y la traducción a ChatGPT** · verificado el **2026-08-29** ·
segunda revisión el **2026-09-29** (§0)

---

## 0. Segunda revisión (2026-09-29): qué se cambió y qué se comprobó

Una revisión externa encontró problemas que la primera verificación no vio. Se
arreglaron; lo que sigue dice qué, y **cómo se comprobó cada cosa** (y qué no).

**Dónde se corrió.** Todo en una copia del repo fuera del repo, en una Mac con
procesador ARM (macOS, 4 hilos), **python 3.12.13, torch 2.14.0, numpy 2.5.3**. No es la
máquina de la corrida del curso (torch 2.13, x86): por eso varios números de acá difieren
de los de las slides, y eso es parte de lo que se documenta.

| Chequeo | Resultado |
|---|---|
| `nbconvert --execute`, notebook entero (51 celdas, 24 de código), CPU | **0 errores** · 1 min 54 s en total; entrenamiento 1 min 41 s (84 ms/paso) |
| Ruta con GPU (antes: `RuntimeError` en `multinomial` con un generador de CPU) | **arreglada** (el sorteo se hace en CPU) · probada **simulando la GPU con MPS**: notebook entero, 60 pasos, **0 errores**. En una T4 real **no se probó** |
| `entrenar-mini-gpt.py` completo, en la copia | **ok** · en la misma máquina da **los mismos números y las mismas muestras que el notebook** (48/60, ventana 5/15/22/26/27/24, fabricación 8 de 57) |
| `entrenar-mini-gpt.py --solo-anotar` sobre el `datos-mini-gpt.json` del repo | **ok** · agrega sólo campos que dependen del corpus y del padrón; **ninguna cifra del modelo cambió** (verificado con `diff`) |
| Las 4 viz y las slides en Chrome headless (por CDP, capturando excepciones y errores de consola) | **0 errores** · controles ejercitados por programa: slider de la ventana en 4/8/12/16/24/128 en los dos casos, los 4 prompts de la alucinación, 3 palabras en contar-letras, temperatura 1,5; capturas de la ventana (los dos casos), la alucinación y las slides 18, 19 y 36 |
| Celda de bootstrap (índice 2) | **no se tocó** · md5 del source `4c9c6d9d…` |
| Notebook guardado sin salidas | **sí** (outputs vacíos, `execution_count` null) |

**No se comprobó en esta revisión:** tema oscuro, ancho de 760 px, una GPU T4 real, ni
las 41 slides una por una (se miraron las que cambiaron de contenido visual).

### Lo que se arregló

1. **Ruta GPU rota** (notebook celdas 18, 22, 28; `entrenar-mini-gpt.py`): el sorteo se
   hace en CPU. Los hitos de las muestras son los mismos con y sin GPU (0/50/150/400/800/1200).
2. **Reproducibilidad prometida de más.** Donde decía «carácter por carácter» / «exactamente»
   ahora dice: idéntico **en la misma máquina y con las mismas versiones**; en otra, parecido.
   Las slides 14-18 dicen «corrida del curso». `notas-docente.md` §9 tiene la tabla de
   cuánto cambia (en esta máquina: 48/60 en vez de 54/60, la curva de la ventana
   5/15/22/26/27/24 en vez de 7/14/24/27/28/28, sin «Nelida Falcon»). El JSON registra
   versiones (`meta.versiones` en las corridas nuevas; la del curso tiene `meta.torch` y
   `meta.cpu`).
3. **Chequeo del momento «Nelida Falcon»:** la celda del entrenamiento lista los nombres
   que inventó *tu* modelo, y la sección 9 mide la **fabricación espontánea** sobre 60
   encabezados (en esta máquina: 8 de 57 nombres no existen). El script calcula lo mismo
   (`alucinacion.fabricacion`) en las corridas nuevas; la corrida del curso no lo tiene.
4. **«No hay lugar donde guardar el corpus» estaba al revés.** El modelo (6,4 MB) pesa
   más que el corpus (1,1 MB) y memorizó las plantillas. La sección 12 lo mide (en esta
   máquina, 5 de 6 pedazos de 40 caracteres de la muestra final están tal cual en el
   corpus) y lo contrasta con los LLM grandes (Carlini et al. 2021, agregado a
   `referencias.md`). Slides 2 y 18, notas §5-6 y solución 1 corregidas.
5. **Absolutos sobre ChatGPT:** «no hay casillero para "no sé"», «incontestable», «ninguna
   unidad que sume», «entrenada, no emergente», «los modelos de 2030…» → reformulados
   (nada adentro *detecta* que no sabe; contar letras es frágil, no imposible; la adulación
   asoma sin RLHF y el RLHF la refuerza —Perez et al. 2022, Sharma et al. 2023—; la escala
   compensa pero no cambia el mecanismo). GPT-4: «OpenAI no publicó el número».
6. **Viz de la ventana:** línea de base mayoritaria (cerca: siempre «FCA» 7/30; lejos:
   siempre PUN 8/24, **más** que los 6/24 del modelo), la pista del caso cerca es el
   **apellido** (con el nombre completo, el cartel aparecía con el modelo acertando), el
   cartel dice lo que pasa en los cuatro casos (afuera/adentro × acierta/erra), y la curva
   «sube de a poco» en vez de «corte». *Lost in the middle* como curva en U (principio o
   final). Los campos nuevos salen de `--solo-anotar`, no de editar el JSON a mano.
7. **TODO 4 venía resuelto** y demostraba lo contrario. Ahora arranca con el encabezado
   adentro, el estudiante tiene que alargar el relleno, y el prompt termina con el
   apellido solo («Diputado Falcon (»: hay 4 Falcon). En esta máquina el modelo contesta
   «FCA — Sierra Mansa» adentro y afuera: no usa el encabezado.
8. **Alucinación:** se separa *aceptar una premisa falsa* (los tres casos falsos: la
   entidad la pone el prompt; la «cita» se recita de memoria, está 124 veces en el corpus)
   de *fabricar* (medido aparte). El caso «existe» del notebook usa el mismo criterio que
   el script (bloque **y** provincia), y la celda de los 60 muestra un caso de media verdad.
9. **Menores:** log 71 como «punto de partida», no «piso»; «ya empató al bigrama» →
   «ya está cerca»; seis cronometrajes (no cinco) en todos lados; 6,4 MB en disco; 36
   puntos (no 40); «ferrocarril» son 6 fichas con el tokenizador del curso; muestra
   validada de **al menos 200** casos en notebook, notas y soluciones; soluciones 4
   (error de API o recorte), 6 (la brecha como señal robusta, 400-900) y 7; comentarios
   JS de slides renumerados (19, 27); `revisar()` del TODO 3 ahora chequea algo; el
   ejemplo de la sección 8 no se rompe si ningún caso cumple el criterio.
10. **`[EL LUNES]` → `[EN TU INVESTIGACIÓN]`** en slides (marca y título de la 40,
    asides), notebook, notas y referencias; el desafío que no se termina pasa a
    «opcional, antes de la clase 9».
11. **Accesibilidad:** `role="img"` y `aria-label` que describen el dato en los 4 canvas
    de las slides y en los de las 4 viz; lo que antes se decía sólo con color ahora tiene
    también signo o trazo (✓/✗ junto a la respuesta y en la primera barra, subrayado recto
    u ondulado para confirmado/inventado, val punteada en la curva de loss, trazos
    distintos para cada línea de base). En contar-letras, el fin de palabra es «▸» (antes
    «⏎», que en otra viz significa salto de renglón) y la fila 2 dice «tokenizador de
    sub-palabras (el chiquito de la clase 6)», con la respuesta del mini-GPT a
    «¿cuántas R?».

Lo que sigue (§1 a §6) es la verificación original del 2026-08-29, con notas donde una
afirmación resultó exagerada.

> Todo lo que dice acá se comprobó **corriendo el código y mirando las imágenes**, no
> leyendo los archivos: `nbconvert --execute` cuatro veces de punta a punta, Chromium
> por Playwright con `context.route` abortando **cualquier** URL `http(s)`, `curl` contra
> cada enlace, y los números recalculados uno por uno contra las logits y el padrón que
> los producen. Donde dice «no lo pudimos medir», no hay número inventado: hay un pedido.

---

## 1. Veredicto

**La clase está lista para darse.** Estaba bien escrita y bien pensada; lo que faltaba era
que alguien la corriera con las manos. **Se encontraron 16 problemas y se arreglaron los
16.** Cinco eran serios —dos de ellos hacían que lo proyectado y lo que el estudiante ve
en su pantalla **no coincidieran**— y uno era un error de dato en la celda que enseña,
justamente, por qué el modelo cuenta mal las letras.

| Chequeo | Resultado |
|---|---|
| `nbformat` valida el `.ipynb` | **sí** · 49 celdas (23 de código) |
| `nbconvert --execute`, notebook entero | **4 corridas, EXIT=0, cero errores** en las 49 celdas · la última, después de todos los arreglos |
| Reproducibilidad del modelo | **al cuarto decimal** entre corridas **en la misma máquina y con las mismas versiones**: train 0,1852 · val 0,1858. *(Nota 2026-09: en otra máquina, no; ver §0.)* |
| Corre sin red | **sí** · el corpus sale de `datos/muestras/`, `torch.cuda.is_available()` es `False` |
| Consola del navegador (41 slides + 4 viz, claro y oscuro) | **0 errores** |
| Requests externas (todo `http(s)` abortado) | **0**, incluidas las viz embebidas en las slides |
| KaTeX | renderiza desde `_shared/vendor` · 4 nodos `.katex`, verificado por screenshot |
| `<iframe>` de las viz dentro de las slides | **cargan y son interactivos** (verificado apretando los botones) |
| URLs de `referencias.md` marcadas `[VERIFICADA]` | **7 de 7 dan 200** |
| Números de las slides contra el código que los produce | **todos recalculados** (ver §4) |
| Presupuesto de tiempo | **114,5 min** declarados sobre 120 · antes sumaban 167,5 |

---

## 2. Lo que estaba roto y se arregló

### Serio — lo proyectado no coincidía con lo que ve el estudiante

**1. Las seis muestras del entrenamiento eran otras.**
`entrenar-mini-gpt.py` sortea cada muestra con semilla `1983 + paso`; el notebook usaba
`1983` fijo. **Los pesos eran los mismos** (la loss coincide al cuarto decimal), pero el
texto generado era distinto en los pasos 50, 150, 400, 800 y 1200. O sea: el docente
proyecta la slide 18 diciendo *«es el párrafo del principio de la clase»* y en la pantalla
del estudiante hay otro párrafo. Es el momento más lindo de la clase y estaba desincronizado.
*Arreglado:* `muestra(paso)` usa `1983 + paso`, con el comentario que explica por qué.
**Verificado:** las **seis** muestras coinciden ahora carácter por carácter con
`datos-mini-gpt.json` y con las slides 14-18 **en el contenedor de construcción**. *(Nota
2026-09: con otra versión de torch u otra CPU, las de los pasos 150, 400 y 800 son otras;
ver §0.)*

**2. La ventana de ejemplo de la slide 7 no era la del notebook.**
La slide muestra `«S» → «e»`, `«Se» → «ñ»`, … sobre «Señor pr». El notebook arrancaba en
`inicio = 41234` y imprimía `«        e» → « »`, `«       e » → «l»`… sobre « e la pena»:
un pedazo cortado en el medio de una palabra, que además se lee peor.
*Arreglado:* `inicio = texto.index("Señor presidente", 30_000)`. **Verificado:** la salida
de la celda es ahora, línea por línea, la de la slide.

**3. Los bloques de código de las slides se dibujaban rotos.**
El plugin de highlight de reveal marca el `<code>` pero **no se carga su hoja de estilo**
(a propósito, para no romper la paleta del curso). Sin ella el `<code>` se queda en
`display:inline`, el padding se le va para arriba y el bloque **se sale de su caja con la
primera línea cortada al medio**. Pasaba en las slides 7 y 25 y se ve horrible en un
proyector. *Arreglado* con tres líneas de CSS en la propia clase.
⚠ **Es un defecto del marco compartido: las 10 clases lo tienen** (ver §5).

**4. El caso «elegido a dedo» de la ventana fallaba con la ventana entera.**
La celda de la sección 8 elige un encabezado que falle con ventana 8 y acierte con 24 —
pero no comprobaba la 128. En la corrida real salía `ventana 128 · contesta «PUN» ✗`,
justo debajo de un markdown que dice *«en cuanto el nombre entra en la ventana, la
proporción de aciertos pega un salto y se queda arriba»*. El ejemplo suelto contradecía a
la vista lo que decía el texto. *Arreglado:* el criterio exige acertar también con 128.
**Verificado:** ahora sale Beatriz Aguirre (FCA), ✓ desde la ventana 12 hasta la 128.

**5. Error de dato en la celda que enseña por qué cuenta mal las letras.**
El notebook imprimía: *«aunque en "ferrocarril" una de las fichas sea justo una "r"
suelta, **las otras dos** erres están escondidas adentro de "fer" y de "ri"»*.
«ferrocarril» tiene **cuatro** erres y las fichas son `['fer','r','oc','ar','ri','l']`:
las otras son **tres**, y están en `fer`, `ar` y `ri`. *Arreglado.* En una clase sobre
verificar números, éste era el peor lugar posible para tener uno mal.

### El número grande: el tiempo de entrenamiento

Era el pendiente #4 de `00-ESTADO-ESPINA.md`. La clase declaraba *«entre 4 y 6 minutos y
medio; contá con seis»*, apoyado en cinco mediciones que **mezclaban dos cosas distintas**
(dos del script `entrenar-mini-gpt.py`, que sólo entrena, y tres del notebook entero).

Se cronometró de nuevo, separando las dos cosas:

| qué se mide | mediciones (s) | rango |
|---|---|---|
| **la celda de entrenamiento sola** (1200 pasos) | 243 · 267 · **280** · **297** · **360** · **432** | **4 a 7 min** |
| **el notebook entero** (`nbconvert --execute`) | **322** · **339** · 361 · 368 · 376 · **404** · **480** | **5 min 20 s a 8 min** |

(en **negrita**, las medidas en esta verificación.) La dispersión no es ruido: el mismo
notebook, en la misma máquina de 4 hilos, tarda **un 40-80 % más** si tenés el navegador
con las viz abierto al lado — que es exactamente lo que va a pasar en el aula.
*Arreglado:* las **ocho** afirmaciones de tiempo (portada, tarjeta de la slide 3, caja de
la 12, título de la 18, título del gráfico de la 19, notas del puente, `notas-docente` §1
y §9, y las dos celdas del notebook) dicen ahora **«entre 4 y 7 minutos, planificá con
siete»**, con las cinco mediciones a la vista.

### Presupuesto de tiempo: no cerraba

Los minutos declarados en los `aside` de las slides sumaban **167,5** (o **138,5**
descontando los totales de bloque). El caso grave: **el bloque de la traducción declaraba
39 minutos de slides para una casilla de 25.** Un docente que siguiera los números se
comía el cierre entero, que es —según sus propias notas— «lo que paga el módulo».
*Arreglado:* se rebalancearon los minutos de las slides 3, 4, 6-11 y 21-33.

| bloque | antes | ahora | casilla |
|---|---|---|---|
| Gancho (1-5) | 11 | **10** | 10 |
| El objetivo más tonto (6-11) | 13 | **10** | 10 |
| Manos 1 (12) + muestras (14-18, adentro) | 20 + 7 | **20 + 7** | 20 |
| Pausa (13) | 10 | **10** | 10 |
| La traducción (19-33) | 41,5 | **24,5** | 25 |
| Manos 2 (34) | 25 | **25** | 25 |
| Cierre (35-41) | 15 | **15** | 20 |
| **Total** | **167,5** | **114,5** | **120** |

`notas-docente.md` §3 se reescribió con los mismos números y con la advertencia de que no
hay aire.

### Presentación

**8.** **Slide 24 se cortaba abajo:** la última línea —*«Cambiarlo es cambiar el
instrumento: los resultados dejan de ser comparables»*, o sea el punto metodológico de la
slide— quedaba partida al medio por el borde de la pantalla. *Arreglado* (806 → 719 px de
760).
**9.** **Slide 5** (el callback grande del curso) llegaba a 811 px de 760 y su remate
—*«Es la misma máquina»*— chocaba con las flechas de navegación. *Arreglado* (→ 659).
**10.** **Las viz embebidas dejaban los botones abajo del corte.** El `<iframe>` mide
~560 px y las viz miden 750-900. En `temperatura.html` quedaban afuera **los dos botones
que las notas del docente le dicen que apriete delante de todos** («Generar 200 fichas» y
«5 veces con el mismo prompt»); en `ventana-de-contexto.html`, el botón «Romperla
(ventana 8)». *Arreglado:* esos botones subieron en el panel y las cuatro viz llevan un
bloque `body.embebido` que aprieta el panel. Verificado por screenshot en la slide real.

### Rigor: afirmaciones que no daban

**11.** `slides.html`, pie de la viz de la ventana: *«la medición sobre 30 pasajes reales»*.
Son **30 en el caso "cerca" y 24 en el "lejos"**. *Corregido.*
**12.** `notas-docente.md` §7: *«los 7 diputados a los que el modelo les erra el bloque»*.
Son **6** (60 − 54). *Corregido*, y con una pista que ahora **está comprobada**: cinco de
los seis comparten nombre o apellido con otro diputado (Osvaldo **Y**barra del VVA con
Osvaldo **I**barra del MPR es el mejor caso); el único sin colisión es Fabián Heredia.
**13.** *«En los modelos grandes pasa lo mismo y tiene nombre: lost in the middle»*
(en la viz y en el notebook). Es **más fuerte de lo que la medición aguanta**: en un
modelo grande el dato lejano **podría** usarse y se usa peor; acá el mini-GPT nunca
aprendió esa dependencia. *Reescrito* en los dos lugares, con la diferencia dicha.
**14.** `viz/por-que-alucina.html`: el «momento aha» mandaba a mirar *«las barras de abajo
a la izquierda»* y *«el gráfico de la derecha»*. El gráfico de las cuatro seguridades está
en la **columna del medio**, también a 1280 px. *Reescrito* nombrando los gráficos por su
título, que además no depende del layout.
**15.** `cuestionario` ítem 6 y `notas-docente` §9: los números de la tijera sobre 25 KB se
presentaban como exactos. Se **volvió a correr**: la forma sale idéntica (train 0,107 vs
val 0,80: tijera de libro), pero con 2.500 fichas de validación **la loss tiene un ruido de
±0,1** y el mínimo se movió del paso 900 al 700. *Documentado en los dos archivos*, con la
aclaración de que si un estudiante contesta «700» está bien igual.
**16.** `notebook.ipynb`: el aviso de arriba decía *«la sección 4 entrena el modelo»* (es
la **5**) y *«la sección 5 está puesta para llenar ese rato»* (es la **6**). *Corregido*, y
verificado que las demás referencias a secciones apuntan a donde dicen.

**Extra sin número:** los comentarios `<!-- N. TÍTULO -->` de `slides.html` estaban
desfasados en 1 desde la slide 19 (quedaron viejos al agregarse la pausa). Renumerados,
para que el próximo que edite no se vuelva loco.

---

## 3. Lo que se miró con los ojos

**Las 41 slides se recorrieron** de punta a punta en claro y en oscuro; **33 se
capturaron** y **20 se miraron de a una** con la herramienta de imagen —las cuatro con viz
embebida entre ellas, antes y después de cada arreglo.
**25 screenshots de viz**: las cuatro sueltas, después de mover el slider a los dos
extremos, después de apretar cada botón, en tema oscuro **por el botón real** (no seteando
el atributo a mano), embebidas a 1203×564 y a 760 px de ancho.
**La figura del notebook** (la curva de loss): ejes rotulados —«mediciones (una cada 50
pasos de descenso)» y «loss»—, leyenda de tres entradas, título que dice la lectura. Se
entiende sin el texto de al lado.

Además se ejercitaron **todos** los controles de las cuatro viz por programa (1 slider ×
3 posiciones, 21 botones, 1 select), en claro y en oscuro: **cero errores de consola**.

**Los momentos aha se ven de verdad**, y esto se comprobó apretando, no leyendo:

- **temperatura** — el slider va de 0 a 2, las barras se aplastan (39,4 % → 20,4 % la
  primera) y **el orden no cambia nunca**; no es un truco de dibujo: el softmax con
  temperatura es monótono y las barras se ordenan una sola vez con las logits crudas.
  El botón de las cinco tiradas cierra el aha: a T=0 las cinco son **idénticas**, de T=0,8
  para arriba son **cinco textos distintos** (comprobado sobre los 4 prompts × 21
  temperaturas del JSON).
- **ventana de contexto** — 28/30 con ventana 128, **14/30 con ventana 8**, con el nombre
  tachado en gris y el cartel rojo. Y el segundo caso, con la curva plana (6/24) **aun con
  la pista adentro**: es una medición, no una promesa, y contradice el plan original de la
  viz. Está contado en `notas-docente` §9 bis y vale la clase. *(Nota 2026-09: faltaba la
  línea de base mayoritaria —8/24 en el caso lejos, más que el modelo— y el cartel
  aparecía con el modelo acertando; corregido, ver §0.)*
- **por qué alucina** — las cuatro seguridades (94 % acertando, 92 % inventando una
  diputada, 97 % una ley falsa, 100 % una cita falsa) con el padrón al lado. No hay
  ninguna señal observable que separe acertar de fabricar.
- **contar letras** — escribís «carro» y la doble R queda adentro de una sola ficha
  (`arr`); el modelo ve `[4, 414, 20]`. Cierra la siembra de la clase 6, que **existe**
  (comprobado: `clases/06-.../viz/tokenizador.html`, líneas 13-14 y 80-81).

---

## 4. Los números, recalculados uno por uno

Ninguno se aceptó por estar escrito. Cada uno se volvió a sacar de la fuente que lo produce.

| número | dónde aparece | cómo se comprobó | ✓ |
|---|---|---|---|
| **1.541.056** perillas | slides 3, 5, 35; las 4 viz; notas; cuestionario 9 | `assert` del notebook, 4 corridas | ✓ |
| vocabulario **71** · log 71 = **4,26** | slide 11 y notebook | `len(tok)` y `math.log` | ✓ |
| loss inicial **4,23** | slides 14, 18, 19 | corrida real: train 4,23 · val 4,23 | ✓ |
| loss del bigrama **2,24** | slides 8, 19 | corrida real: **2,242** | ✓ |
| loss final **0,19** (train 0,185 · val 0,186) | slides 18, 19 | 4 corridas en la misma máquina, idéntico al 4.º decimal (en otra: 0,183 · 0,184) | ✓ |
| **54 de 60** aciertos de bloque | slide 23, viz, notas | recontado sobre `padron_detalle` **y** en la corrida (en otra máquina: 48) | ✓ |
| **33 de 60** de provincia | viz | recontado sobre `padron_detalle` | ✓ |
| 7/30 · 14/30 · 24/30 · 28/30 (ventana) | viz y slide 26 | reproducido por el notebook, mismos valores | ✓ |
| 6/24 con la pista lejos | viz | del paquete exportado (no re-entrenado); la línea de base mayoritaria da 8/24 | ✓ |
| 0,891/0,095/0,007/0,003/0,001 (T=1,0) | cuestionario ítem 5 | softmax recalculado sobre las 71 logits | ✓ |
| 0,586/0,180/0,045/0,027/0,017 (T=1,9) | cuestionario ítem 5 | ídem | ✓ |
| «ferrocarril» = **4** erres, 6 fichas | notebook y viz | `[184, 6, 133, 36, 54, 240]` | ✓ |
| Nélida Falcón **no existe** | slide 17 | no está entre los 60 (sí «Raúl Falcón», «Nélida Villalba») | ✓ |
| Puerto Bermejo, Ley 7841: no existen | viz | contra las 10 provincias y las 14 leyes | ✓ |
| P·V·M·F·B·U = iniciales de los 6 bloques | slide 10 | PUN, VVA, MPR, FCA, BST, UAP | ✓ |
| corpus **1,1 MB**, checkpoint **6,4 MB** en disco | slides y notebook | 1.098.206 caracteres · 6,2 MB son los pesos, el resto máscaras y vocabulario | ✓ |
| 7 URLs `[VERIFICADA 2026-08-29]` | `referencias.md` | `curl`: **200** las 7 | ✓ |
| **6** (no 7) diputados con el bloque errado | notas §7 | 60 − 54 | corregido |
| 30 pasajes (24 en el 2.º caso) | slide 26 | `datos-mini-gpt.json` | corregido |
| tijera sobre 25 KB | cuestionario 6 | re-entrenado: forma ✓, decimales con ±0,1 | matizado |

**Las citas bibliográficas se revisaron una por una** (autores, año, publicación): Karpathy,
Alammar, Wolfram, Bender et al. 2021 FAccT, Ziems et al. 2024 *Computational Linguistics*
50(1), Ouyang et al. 2022, Liu et al. *Lost in the Middle*, Barrie/Palmer/Spirling 2024,
Grimmer/Roberts/Stewart 2022, Bajtín. **Ninguna es inventada y ninguna tiene el año o el
autor cambiado.** No se sacó ninguna.

---

## 5. Lo que queda abierto

1. **El tiempo en GPU T4 sigue sin medir** (y la ruta con GPU, que estaba rota, sólo se
   probó simulada con MPS; ver §0). Este contenedor no tiene GPU
   (`torch.cuda.is_available()` → `False`, no hay `nvidia-smi`). El notebook y
   `notas-docente.md` §9 lo dicen y le piden el número a quien dé la clase en Colab.
   **No se inventó ninguno**, que es lo mínimo en la clase que enseña a no inventar.
2. **El arreglo del `<pre><code>` está sólo en la clase 8.** La causa está en
   `_shared/css/curso.css` (`.reveal pre code` no fija `display:block`) y **afecta a las
   10 clases**: 16 bloques de código en total, en las clases 1, 2, 4, 6, 7, 8 y 10. No se
   tocó el archivo compartido porque hay equipos trabajando en paralelo (hay commits
   concurrentes en el repo mientras se escribía esto). **Una línea lo arregla para todos**:
   `.reveal pre code { display: block; overflow: auto; }`.
3. **Las viz embebidas siguen sin entrar enteras en el `<iframe>`.** Después de apretarlas
   miden 711-835 px contra los ~560 del marco. Se arreglaron los controles que el docente
   necesita; lo que queda abajo del corte es texto de cierre. **No es de esta clase**:
   se midieron **30 viz del curso** (hasta tres por clase) y **22 desbordan igual** (la peor,
   `checklist-revisor` de la clase 10, mide 2.596 px). El `<iframe>` scrollea, así que nada se pierde.
4. **Quedan 9 marcas `[VERIFICAR URL]`** en `referencias.md` (Karpathy en video, Wolfram,
   Stochastic Parrots, Ziems, InstructGPT, Lost in the Middle, Barrie/Palmer/Spirling,
   *Text as Data*, Bajtín). Las obras existen y están bien citadas; los hosts (YouTube,
   arXiv, DOI, ACL) están **bloqueados** desde acá. Las 7 que sí se pudieron abrir se
   revalidaron con `curl` en esta verificación: 200 las 7.
5. **`00-ESTADO-ESPINA.md` §6 sigue listando como abiertos dos ítems de la clase 8 que ya
   no lo están:** el **#2** (falta la slide de glosario — está, es la **38**) y el **#4**
   (el tiempo de CPU sin medir — medido ocho veces, §2 de este archivo). No se editó ese
   archivo para no pisar a los otros equipos; **conviene que alguien lo actualice.**
6. **El ítem 6 del cuestionario tiene un mínimo que se mueve.** Con 25 KB, la validación
   son 2.500 fichas y la loss medida sobre ellas tiene ±0,1: en una corrida el mínimo cayó
   en el paso 900 y en otra en el 700. La tabla que ve el estudiante es una corrida real y
   la respuesta que la pregunta mide sigue siendo la misma; está anotado en la solución.
7. **A 760 px de ancho las cuatro viz desbordan 4 px en horizontal.** Idéntico en las
   clases 1, 3 y 4: es el marco compartido, no la clase. La clase se da en proyector.
8. **El cierre declara 15 minutos para una casilla de 20.** Se dejó así a propósito: es el
   único colchón del deck y las notas del docente avisan que el cierre es lo primero que se
   come el reloj.

---

## 6. Cómo reproducir esta verificación

```bash
cd clases/08-mini-gpt-y-los-llm
python3 -c "import nbformat; nbformat.validate(nbformat.read('notebook.ipynb', as_version=4))"
time python3 -m nbconvert --to notebook --execute --output /tmp/out.ipynb notebook.ipynb
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
ejecutable en `/opt/pw-browsers/chromium`), abriendo por `file://` con un
`context.route('**/*')` que **aborta toda URL `http(s)`** y falla si alguna sale. Se
recorren las 41 slides con `Reveal.slide(i,0,0)` en tema claro y oscuro, y las cuatro viz
se ejercitan control por control (slider a los dos extremos y al medio, cada botón, cada
opción de cada select), sueltas y embebidas, a 1280 y a 760 px.
