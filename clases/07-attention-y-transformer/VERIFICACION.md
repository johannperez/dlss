# Verificación adversarial — Clase 7

**Attention: cada palabra arma su propio resumen del contexto**
Fecha: 2026-08-29 · Todo lo que dice acá se comprobó **corriendo el material**, no leyéndolo:
`nbconvert --execute` cronometrado, `nbformat.validate`, Chromium por Playwright con
`context.route` abortando **cualquier** `http(s)`, `curl` contra cada URL, y mirando los PNG
con los ojos (53 screenshots de slides, viz e interacciones).

---

## 1. Veredicto

**La clase está lista para darse.** Se encontraron **17 problemas** y **se arreglaron los 17**.
Tres eran graves: el plan de tiempos del docente sumaba **130 minutos** en vez de 120, una
solución del cuestionario afirmaba algo **falso** sobre las matrices causales, y una de las viz
le decía al aula que cuatro cabezas «hacen lo mismo» cuando sus mapas son claramente distintos.

| Chequeo | Resultado medido |
|---|---|
| `nbformat.validate` | **OK**, 50 celdas |
| `nbconvert --execute` | **0 errores**, 7 figuras · **15,2 s · 15,5 s · 16,1 s** en tres corridas |
| Notebook **sin red** | corre entero con `socket.connect`, `create_connection` y `getaddrinfo` bloqueados a nivel Python |
| Consola del navegador | **0 errores** en `slides.html` y en las 5 viz, en su ubicación real |
| Requests externas | **0** (se abortó todo `http(s)`; nada se rompió) |
| KaTeX | renderiza y **se repinta con los colores del curso**, verificado por screenshot en claro **y** oscuro |
| Iframes de viz dentro de las slides | los 5 cargan; los 4 propios **entran enteros** en su alto (antes 3 se cortaban) |
| Alto de las slides | ninguna de las 38 supera los 760 px de diseño (antes: 3 lo hacían) |
| Ventana angosta (820 px y 640 px) | ninguna viz desborda en horizontal, 0 errores |
| Reproducibilidad del modelo | `medir-atencion.py` corrido **dos veces**: `datos-atencion.json` sale **idéntico** salvo el campo `segundos` |
| URLs | **8 verificadas con `curl` (HTTP 200)**; 5 hosts confirmados inalcanzables desde acá |
| Presupuesto de tiempo | **120 min exactos**, coincide con `PROGRAMA.md` |

---

## 2. Lo que estaba mal y se arregló

### Graves

**1. El plan de tiempos de `notas-docente.md` sumaba 130 minutos.**
La tabla arrancaba bien y se desfasaba en el medio: «las tres decisiones» (15) + «el bloque
completo» (10) se comían diez minutos que la especificación no tiene, y el cierre terminaba a
las **2:10**. Un docente que siguiera esa tabla se quedaba sin la mitad del cierre, que es
justamente el `[EL LUNES]`.
*Arreglado:* la tabla ahora es 10+20+15+15+**10**+9+6+20+15 = **120**, mapeada a los números de
slide reales, con una nota que avisa que el tramo 1:10–1:25 son trece slides y hay que ensayarlo.

**2. La solución del ítem 3d afirmaba algo falso.**
Decía: *«La última columna de una matriz causal siempre suma 0 (salvo su propia diagonal, que en
este recorte no está incluida)»*. Las dos mitades son falsas: la diagonal **sí** está incluida en
las sumas que muestra el cuestionario (las recalculé sobre `datos-atencion.json`), y la última
columna vale exactamente la auto-atención de la última palabra, que en general **no** es 0 —acá
da 0,00 porque esa cabeza no se mira a sí misma, no porque lo imponga la máscara.
*Arreglado:* la respuesta ahora separa las dos cosas —la máscara **acota** cuánto puede valer una
columna; el valor exacto lo pone el modelo— que además es una distinción que el ítem 11 necesita.

**3. `viz/cabezas.html` decía que las cuatro cabezas «hacen lo mismo» cuando no.**
El panel comparaba los **rótulos**: si a las cuatro les tocaba el mismo, imprimía «hacen lo
mismo: cuatro juegos de perillas que terminaron en el mismo lugar». En el bloque 2 las cuatro
comparten rótulo («mezcla…») y sus mapas son bien distintos, así que la viz enseñaba lo contrario
de lo que muestra la pantalla.
*Arreglado:* ahora se **mide**. Si las cuatro cabezas se quedan con su atención en su propia
palabra (el `est.misma` del JSON) o coinciden en el 80% de las filas, dice «hacen lo mismo» y
muestra los cuatro números; si no, dice «les queda el **mismo rótulo** y sin embargo los cuatro
mapas son distintos: el rótulo es un resumen grueso, no una explicación» — que es, además, la
lección de la clase.

### Importantes

**4. La viz de `qkv` embebida cortaba justo lo que hay que mirar.** El contenido medía 674 px en
un iframe de 610: se perdían dos de las siete barras de porcentaje, que son *el* resultado de
mover la perilla. *Arreglado* con un modo compacto embebido (el plano cuadrado pasa de 400 a
340 px, el panel se aprieta) → 598 px. Suelta se ve igual de grande.

**5. La tabla de `supuestos-de-arquitectura` cortaba la fila del Transformer**, que es la razón
de existir de esa slide (616 px de contenido en 610, y antes 679). *Arreglado* con compactación
embebida + iframe de 611 px; las cuatro filas entran enteras.

**6. Tres slides desbordaban el alto de diseño** (24, 32 y 34: 827, 793 y 793 px sobre 760) y en
1280×720 se les cortaba la última línea del pie. *Arreglado* acortando los pies y el bloque de
Jain & Wallace. Ahora ninguna de las 38 supera 760.

**7. Las viz de las slides 9 y 22 se cortaban 21 y 27 px.** *Arreglado* subiendo esos dos iframes
a 530 px (hay lugar de sobra en esas slides).

**8. Los pesos del ejemplo cambiaban de una slide a la otra.** La slide 6 y la 7 repartían
0,60 · 0,20 · 0,10 y la slide 8 hacía la cuenta con 0,60 · **0,30** · 0,10 (que es lo que usa el
notebook). Misma oración, misma palabra, otro número, sin avisar. *Arreglado:* las slides 6, 7, 8
y el notebook usan **los mismos tres pesos**, y la slide 6 aprovecha para decir algo cierto:
a «recinto» y a sí misma **no les tocó nada**.

**9. La slide 25 afirmaba, al pie de la letra, algo falso.** *«Para attention pura, esas dos
oraciones son la misma entrada»*, sobre «la comisión rechazó al ministro» / «el ministro rechazó
a la comisión»: no son la misma bolsa hasta sacar los artículos (*al* vs *a la*), y la clase 6 lo
había aclarado explícitamente. No cambié el par —es la siembra de la clase 6 y romperla sería
peor—: *arreglado* reescribiendo el enunciado («attention sola no ve el orden: barajá las
palabras y sale lo mismo, reordenado») y sumando la aclaración de los artículos, con la
demostración limpia remitida al notebook (que permuta la **misma** oración: diferencia máxima
5·10⁻⁷). Lo mismo en la solución del ítem 5.

**10. El costo cuadrático no estaba en ninguna slide** y el ítem 9 del cuestionario lo pide como
«el problema nuevo que introduce attention». Estaba en el notebook y en las notas del docente, no
en la clase. *Arreglado:* recuadro en la slide 31 (10 palabras → 100 celdas; 1.000 → un millón;
100.000 → diez mil millones; por eso la ventana de contexto es finita) y las notas ahora dicen
que ése es el recuadro que no se saltea.

### De rigor numérico

**11. `viz/matriz-de-atencion.html` citaba números que no muestra.** El «qué mirar» decía que hay
columnas que «suman 4 o 5» y otras que dan «0,3»; con la oración y la cabeza que la viz abre por
defecto, la fila de sumas dice 3,67 · 3,92 · 1,35 · 0,10 · 0,00… *Arreglado:* el texto ahora cita
los números reales de esa vista.

**12. «751 s de CPU» era un número real pero engañoso.** Salía de una corrida hecha con la
máquina cargada; con la CPU libre el mismo entrenamiento tarda **51 s** (medido dos veces: 58,5 y
50,9). El notebook lo imprimía y el aula iba a entender «doce minutos». *Arreglado:* regeneré
`datos-atencion.json`/`.js` con el script sin tocar nada más —el contenido es **idéntico byte a
byte** salvo ese campo— y actualicé la docstring y las notas.

**13. El comentario del momento aha de `attention-como-mesa.html` decía «cinco palabras para
atrás»** cuando el arco va **dos** palabras atrás. *Arreglado.*

**14. La receta del segundo aha estaba escondida.** El «hacé clic en la “y” de la enumeración y
mirá cómo reparte 28/23/39» sólo funciona si además cambiás a la cabeza «bloque 2 · cabeza 1»
—con la cabeza que abre por defecto, la «y» mira los artículos—, y eso estaba escrito únicamente
en el pie de la viz suelta, que la slide **esconde**. *Arreglado:* los tres pasos están ahora en
las notas del orador de la slide 9, con la advertencia incluida.

**15. La numeración de slides estaba desfasada en todos lados.** Las notas, las soluciones y las
referencias citaban los números de la especificación (35 slides) y el deck tiene 38: «slide 19,
volvimos» era en realidad la slide de la **pausa**, y «slide 32, la advertencia» era la tabla de
la clase 5. *Arreglado:* 12 referencias renumeradas al deck real, más una nota que explica de
dónde salen las tres slides de diferencia.

**16. «doce minutos» para correr `medir-atencion.py`** en las notas → **menos de un minuto**.

**17. El glosario compartido contradecía la vacuna de la clase.** La entrada `multi-head` decía
«una sigue la sintaxis, otra la correferencia», que es exactamente la narrativa contra la que la
clase construyó una viz entera. *Arreglado* en `recursos/glosario.md`, remitiendo a la clase 7.

---

## 3. Lo que verifiqué y estaba bien

- **Los mapas de atención son de un modelo real y son reproducibles.** Corrí
  `medir-atencion.py` dos veces: `historial`, `oraciones` y `cabezas` salen **idénticos** al
  archivo del repo (mismos 0,77 · 0,86 · 0,95 · 0,86 de auto-atención en el bloque 1, misma
  muestra generada palabra por palabra). Lo único que cambia entre corridas es `segundos`.
- **Las cinco oraciones existen en el corpus.** Las busqué una por una en
  `datos/muestras/discursos-apertura/corpus-mini-gpt.txt`; las cinco están textuales (dos de
  ellas partidas por un salto de línea, por eso hay que normalizar los espacios antes de
  buscarlas).
- **Los números del cuestionario salen del modelo.** La fila de «y» (0,28 · 0,23 · 0,39) y las
  sumas de columna (2,02 · 1,65 · 4,03 · … · 0,00) las recalculé del JSON: coinciden hasta el
  segundo decimal, y la fila suma 1,0001.
- **El softmax de la slide 16 da lo que dice.** 2,0 · 0,6 · −0,5 · 0,8 → 0,61 · 0,15 · 0,05 ·
  0,18. Y las dos respuestas del ítem 6 también: ×3 → 0,96 · 0,01 · 0,00 · 0,03; ×0,1 → 0,28 ·
  0,25 · 0,22 · 0,25.
- **El código de la slide 29 es idéntico al del notebook** (es el único bloque de código de las
  slides), y la clase `BloqueTransformer` del notebook es la misma que la de `medir-atencion.py`,
  incluido el pre-norm que dibuja la slide 27 y que pide el ítem 10 del cuestionario.
- **Las cinco viz responden.** Cliqueé palabras, moví los dos giros, prendí y apagué la máscara,
  los values, «todas a la vez», «superponer», los dos bloques, el slider de posición y el de
  números, y las cinco oraciones. Los aha ocurren: «lo» → «algo» al 100%; al girar el aviso a
  +60° «lo» se va a la coma (36% contra 14% de «algo»); los values **no** mueven los
  porcentajes; el triángulo crece con el slider y las sumas de columna cambian con él.
- **Las 7 figuras del notebook** tienen ejes rotulados, leyenda o números en las celdas, y el pie
  «cada fila suma 1,00 · las columnas no suman nada» en todos los heatmaps.
- **Los puentes son explícitos**: slide 2 (la mochila de la clase 6) y slides 35 y 38 (el mini-GPT
  de la clase 8, con el callback a «contar las erres»).
- **Tono**: voseo sostenido, sin solemnidad, sin párrafos-muro; cada slide tiene imagen, ejemplo o
  pregunta. No encontré condescendencia ni jerga sin explicar.
- **Las citas existen y están bien atribuidas** (Vaswani 2017 NeurIPS; Jain & Wallace 2019 NAACL;
  Wiegreffe & Pinter 2019 EMNLP; Grimmer, Roberts & Stewart 2022; Elhage et al. 2021). No hay
  ninguna inventada, y las 8 URLs marcadas `[VERIFICADA]` devuelven 200.

---

## 4. Lo que queda abierto

| # | Qué | Para quién |
|---|---|---|
| 1 | Siete lecturas siguen con `[VERIFICAR URL]`: Alammar, 3Blue1Brown, Vaswani, el video de Karpathy, Wiegreffe & Pinter, Elhage y Grimmer. Confirmé que `arxiv.org`, `jalammar.github.io`, `youtube.com`, `transformer-circuits.pub` y `3blue1brown.com` **no responden** desde este contenedor: la marca es honesta, no pereza. | quien tenga red |
| 2 | **El modelo tiene la atención muy afilada** (varias filas dan 1,00 en una sola celda) y el bloque 1 colapsado en auto-atención. Está contado como contenido en las tres viz, en el notebook y en las notas. **Probé la corrida larga que sugería el equipo anterior** (`--pasos 6000`, lr 1,2e-3): la loss de validación mejora (4,60 → 4,23) y **la clase empeora** — las cabezas se vuelven difusas, «lo» se mira sobre todo a sí misma (35-41%) y en la enumeración la atención se va a los artículos. Se pierden los dos aha. **Recomendación: no cambiar el modelo.** Queda anotado en `medir-atencion.py`. | equipo 8, si reusa el modelo |
| 3 | En la viz de las cabezas embebida, los rótulos de los heatmaps quedan en 8,6 px (se achicaron para que las cuatro matrices entraran). Se leen en un proyector de 1280, pero en un aula grande conviene abrir la viz suelta, donde van a 9,5 px y con celdas más grandes. | el docente |
| 4 | El notebook **corre sin red** (lo probé bloqueando los sockets de Python), pero **nadie lo corrió en Colab de verdad**. La celda de bootstrap y la ruta de descarga siguen sin probarse contra internet. | el primer equipo que lo abra en Colab |
| 5 | En `qkv.html`, con el aviso girado a +60°, la coma (36%) y la propia «lo» (36%) quedan empatadas al redondeo. El panel elige bien —nombra a la coma, que es la que gana entre las **otras** palabras— pero si alguien mira sólo las barras puede ver un empate. No lo toqué porque los números son los que son. | el docente, si se lo preguntan |
| 6 | El entorno hace *snapshots* automáticos con `git commit`. Uno de ellos alcanzó a llevarse un directorio temporal que usé para reproducir el entrenamiento (`clases/00-verif/`). **Lo borré del working tree**; el borrado está sin commitear, porque el encargo prohíbe commitear. Que el próximo snapshot lo levante, o que alguien lo confirme a mano. | quien mantenga el repo |

---

## 5. Cómo reproducir esta verificación

```bash
# notebook
python3 -c "import nbformat; nbformat.validate(nbformat.read('clases/07-attention-y-transformer/notebook.ipynb', as_version=4))"
python3 -m nbconvert --to notebook --execute --output /tmp/out.ipynb \
        clases/07-attention-y-transformer/notebook.ipynb          # ~16 s, 0 errores, 7 figuras

# el modelo de las viz (tiene que dar EXACTAMENTE el mismo JSON, salvo `segundos`)
PYTHONPATH=_shared python3 clases/07-attention-y-transformer/medir-atencion.py   # ~51 s

# sin red: bloquear los sockets de Python y correr el notebook como script
python3 -m nbconvert --to script --output-dir /tmp/sinred clases/07-attention-y-transformer/notebook.ipynb
# (con un sitecustomize.py que hace socket.socket.connect = raise)
```

Para el HTML: Chromium por Playwright (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`,
`executablePath:'/opt/pw-browsers/chromium'`), abriendo por `file://` con
`context.route('**/*', r => /^https?:/.test(r.request().url()) ? r.abort() : r.continue())`.
Para el alto de las slides: `Reveal.getCurrentSlide().scrollHeight` contra
`Reveal.getConfig().height` (760). Para los iframes: `document.body.scrollHeight` adentro del
frame contra `window.innerHeight`.
