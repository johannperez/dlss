# Verificación adversarial — Clase 5

**«La forma de los datos manda (I): imágenes»** · `clases/05-imagenes-y-convoluciones/`

Este archivo junta tres pasadas. La **primera** fue la del equipo que construyó la
clase. La **segunda** la hizo alguien que no la construyó, con `nbconvert`,
Chromium por Playwright y capturas de pantalla (2026-08-29; resumida en §3). La
**tercera** (2026-09-29, §1 y §2) aplicó los arreglos de la revisión general del
curso. Cada afirmación dice **en qué pasada** se comprobó y **cómo**. Lo que no se
volvió a comprobar en la tercera pasada está dicho como tal.

**Veredicto: la clase se puede dar.** El argumento central (la densa no pierde
nada al barajar; la CNN sí; con la foto corrida la densa se desploma y la CNN
aguanta) se sostiene con otras semillas y en dos entornos distintos. Los
dígitos exactos, en cambio, **no** son los mismos en cualquier máquina, y la
clase ya no lo promete.

---

## 1. Lo que se midió en la tercera pasada, con el número real

Entorno: python 3.12.13 · torch 2.14.0 · numpy 2.5.3 · macOS arm64 (queda
guardado en `datos-experimentos.json`, clave `entorno`). Todo corrido sobre una
copia del repo en el scratchpad, nunca dentro del repo.

| Chequeo | Resultado |
|---|---|
| `medir-experimentos.py` (partes A-E) | corre entero, **~5 min** (A-D ≈ 1,5 min; E, las otras semillas, el resto). Dos corridas seguidas dan **los mismos números** en A-D |
| Notebook ↔ `datos-experimentos.json` | el notebook, ejecutado en el mismo entorno, da **los mismos números** que el JSON (ver §2) |
| Slides y viz ↔ JSON | los números de la slide 8, 9 y 28 y los de las viz **se leen del JSON** (`data-num` en las slides; `DATOS_EXP` en las viz). El texto fijo que queda en el HTML es sólo el valor de respaldo |
| `nbconvert --execute` del notebook | **0 errores**, **53 s** con FashionMNIST en cache; y **0 errores**, 54 s, sin red ni cache (plan B). Ver §4 |
| Slides y viz en Chrome headless | **0 errores de consola** en las 4 viz y en las slides (el único mensaje es el aviso benigno «ResizeObserver loop…» de reveal). Ver §4 |

### Los números de la clase, remedidos (semilla 1983)

| | perillas | foto normal | píxeles barajados | corrida 3 px |
|---|---|---|---|---|
| red densa | 50.890 | 85,7 % | **85,5 %** | **32,2 %** |
| CNN | 23.946 | **87,7 %** | 83,1 % | **74,4 %** |

Los publicados antes (85,8 / 85,6 / 87,8 / 83,2; 32,3 / 74,1) salían de otro
entorno (el contenedor de construcción, con otras versiones). **La diferencia es
de 0,1-0,3 puntos**, salvo la CNN con 6 píxeles de corrimiento (38,1 → 40,5) y el
mini-caso del archivo (ver abajo). O sea: la semilla fija la corrida **en la misma
máquina y con las mismas versiones de las librerías**; con otras, los números
cambian un poco.

**Con otras semillas** (parte E: 1984-1987; mismos datos y misma permutación,
cambia sólo la inicialización y el orden de los lotes):

- la densa se mueve **menos de un punto** al barajar, para arriba o para abajo
  (caídas de −0,9 a +0,6);
- la CNN pierde **entre 2 y 5 puntos** (2,0 a 4,8);
- con la foto corrida 3 px, la densa queda entre 30 y 34 % y la CNN entre 67 y 75 %.

El patrón se sostiene en las cinco semillas. Los dígitos no.

**Mini-caso del archivo fotográfico sintético** (semilla 1983): **96,7 %**
global, 13 errores; follaje **85,2 %** (9 errores), multitud 98,5 % (3),
edificio 99,3 % (1). Antes se publicaba 97,0 % y «7 de 12 errores en follaje».
Con **doce semillas** (1983-1994) el follaje es el tipo con menos aciertos en
**10 de 12**; en las otras dos el que peor sale es «multitud» (el modelo se
pierde multitudes ralas), que es la misma confusión mirada del otro lado. Los
edificios fallan poco en casi todas (0-3 errores en 10 de 12; 9 y 10 en las
otras dos). Por eso el notebook, las slides y las
notas ya no dicen «7 de 12» ni «siempre el follaje»: dicen que los errores se
amontonan en las escenas con manchitas, sobre todo el follaje, y el notebook
**avisa** si en tu corrida el que peor sale es otro. El detalle por semilla está
en `datos-experimentos.json` → `otras_semillas.archivo`.

**Experimentos del cuestionario** (parte D, 6 pasadas; antes no estaban
medidos por ningún script):

- 3c, una permutación **distinta por imagen**: densa **20,7 %**, CNN **33,3 %**
  (el azar es 10 %). La solución decía que «ningún modelo puede aprender nada»;
  ahora dice que caen cerca del azar y por qué no llegan.
- 4a, entrenar centrado en un lienzo de 56×56 y probar en las esquinas: CNN
  84,6 → 73,1 / 72,4 %; densa 84,5 → 9,3 / 11,2 %.
- 4b, la CNN de la clase con la foto rotada 90°: 87,7 → **7,5 %**.

---

## 2. Qué se cambió en la tercera pasada

**Reproducibilidad honesta.**
- `medir-experimentos.py` guarda el **entorno** (python, torch, numpy,
  plataforma, fecha) en el JSON y en la cabecera del `.js`, mide los
  experimentos del cuestionario (parte D) y la variación con otras semillas
  (parte E; `--rapido` la saltea sin borrar la ya medida).
- La nota de la slide 28 decía que al aula «les tienen que haber dado
  idénticos». Ahora dice «casi iguales» y explica por qué; lo mismo en las
  notas del docente, las soluciones del cuestionario y el notebook.
- El notebook lee los números de referencia del JSON (ya no los tiene escritos a
  mano), imprime los suyos al lado de los de las slides con las dos versiones de
  torch, y **calcula** la frase del barajado, la del corrimiento y la del
  análisis de errores: si el momento clave no aparece en tu corrida, lo dice.

**Contenido.**
- «La densa saca *exactamente* lo mismo» → «prácticamente lo mismo» (notas §1).
- Slide 16: comparaba 32 filtros (288 pesos) contra la capa densa y decía «anda
  mejor» del modelo entero. Ahora usa **16 filtros (144 pesos)**, como el
  notebook, dice que la comparación es capa contra capa y da el total del modelo
  (23.946 contra 50.890).
- Invariancia y equivariancia: nota a pie en la slide 25, en las notas de las
  slides 12 y 24, en el glosario de la slide 35, en las notas del docente y en
  `referencias.md` (Goodfellow). El discurso principal no cambió.
- Slide 12 (notas): el mapa se achica en la cuenta a mano, pero la CNN usa
  `padding=1`; el 28 → 14 → 7 viene del pooling.
- TODO 2: la pista 2 da un detector de **borde** diagonal que se enciende en la
  «/» y da cero sobre `np.eye`. Se agregó la explicación (el borde es
  perpendicular al cambio de signo), el detector de **línea**
  `[[2,-1,-1],[-1,2,-1],[-1,-1,2]]` y un mensaje que dice a qué raya reacciona
  el filtro. La viz del kernel nombra igual su preset «diagonal».
- La promesa de un modelo de **imagen** preentrenado en la clase 9 (que es sólo
  de texto) se reformuló en la viz de supuestos, la slide 32, las notas y el
  notebook: la clase 9 muestra la transferencia con texto; con imágenes la receta
  es la misma, sin ejercicio prometido.
- Viz de supuestos: «el caso para el que la CNN fue inventada» → «el caso
  ideal»; «los modelos de imagen preentrenados suelen ser transformers» →
  «muchos son CNN y los más nuevos, transformers (ViT)»; la bolsa de palabras
  lleva la salvedad «sin contar las palabras vacías»; la RNN, la mochila de
  tamaño fijo que se sobrescribe; y las filas grises se desbloquean **por
  separado** con `?hasta=6` / `?hasta=7`.
- Slide 31, punto 3: en vez de «hay literatura que muestra que se degrada», la
  limitación que reporta el propio Jean et al. (el modelo distingue mal entre
  los más pobres) y Rolf et al. (2021) para la generalización. Lo mismo en la
  solución 10 y en `referencias.md`.
- Cuestionario 10: el estudio es ahora explícitamente inventado «del estilo del
  de la clase», con R² = 0,45 (0,75 se parecía más a los de activos que a los de
  consumo de Jean et al.).
- El puente a la clase 6: las dos frases «usan las mismas palabras con
  contenido», no «exactamente las mismas palabras» («al» es «a» + «el»).

**Calendario.** `[EL LUNES]` → «En tu investigación» (marca de la slide 32,
título «Qué te llevás a tu investigación», notebook «En tu propia
investigación, desde ya»). Se sacaron «esta semana» y «el lunes». Carga para la
clase que viene, dicha en el notebook y en el cuestionario: terminar la sección 5
y las preguntas 1-7 y 10 (menos de una hora). Jean et al. pasa de «lectura
obligatoria» a recomendada.

**Tiempos.** La slide 27 decía «veinte minutos» y el plan le daba 13; las notas
de cada slide sumaban más de 120. Ahora la tabla de `notas-docente.md` §2, las
notas de cada slide y la slide 27 dicen lo mismo (práctico 2: **13 minutos**) y
suman 120.

**Accesibilidad.** Todas las figuritas de canvas de las slides y de las viz
tienen `role="img"` y `aria-label` (el del mapa de la viz del kernel se
actualiza con el filtro y la imagen). Los signos ya no se dicen sólo con color:
leyenda «rojo = positivo, azul = negativo» en la slide 12 y en el panel 3 del
kernel (los números de la cuenta llevan su signo); ✓ y ✗ en la tabla de la
slide 28 y en los veredictos de la viz de supuestos; «pierde» o «gana» en
palabras en la viz del barajado; marca en el rótulo de la unidad elegida y de sus
piezas en la viz de la jerarquía (además de `aria-pressed`).

**Otros.** Los comentarios `<!-- n · … -->` de `slides.html` usan ahora la
numeración del contador (la pausa es la 18). `kernel-deslizante.html` escribe
con coma decimal, como las slides. El notebook decía que la viz del kernel trae
«cinco imágenes» (son ocho); las notas, «cinco opciones de datos» (son seis) y
«el `assert`» (es un `revisar()`).

**Lo que se verificó de todo esto, y cómo:** ver el final de §4 («Qué se
corrió en la tercera pasada»).

---

## 3. La segunda pasada (2026-08-29), resumida

Se encontraron 11 problemas y se arreglaron 11; la lista completa está en la
historia de git de este archivo. Los que siguen importando:

1. **Sin internet, el notebook afirmaba algo falso.** El plan B (figuras
   sintéticas) es demasiado fácil y el barajado no mueve nada; el notebook
   imprimía igual «la densa ni se enteró, la CNN sí». Se arregló calculando la
   frase a partir de lo medido. (En la tercera pasada se agregó que el
   experimento de la **foto corrida sí** se ve en el plan B.)
2. «La red densa es *exactamente* la de la clase 4» → «la misma máquina»
   (dos capas densas con un doblez); ahora también en el docstring de
   `medir-experimentos.py`.
3. «Cuánta *materia*» → «cuánta luz».
4. El notebook mandaba a la sección 6 por el mini-caso, que está en la 5.
5. Tiempos del notebook medidos: 81-116 s en aquel contenedor.
6. El cuestionario tiene doce preguntas, no once.
7. `notas-docente.md` numeraba las slides sin contar la pausa.
8. Coma decimal en la viz del barajado.
9. La viz de supuestos dejaba un recuadro vacío embebida.
10. El rótulo del máximo global se salía de su caja (slide 24).
11. `.viz-frame` sin `box-sizing`: parche local en los cinco HTML.

En aquella pasada también se revisaron las citas una por una (autor, año,
revista) y no se encontró ninguna inventada; eso no cambió.

---

## 4. Lo que queda abierto

1. **Los `[VERIFICAR URL]` y los `DOI [VERIFICAR]` de `referencias.md`.** Nadie
   abrió esos enlaces; las obras se encuentran por autor y título.
2. **`.viz-frame { box-sizing: border-box }` tiene que ir a
   `_shared/css/curso.css`.** Sigue parchado local. Es para el equipo de la espina.
3. **La slide 3 usa un esquema sintético de multitud.** Se lee como un montón de
   crucecitas, no como una foto; una foto real con licencia libre funcionaría
   mejor (`notas-docente.md` §11).
4. **El plan B sin internet no reproduce el barajado** (sí el corrimiento). Para
   que cierre también sin red haría falta un conjunto sintético que una red densa
   no pueda resolver sin mirar la grilla.
5. **Los números dependen del entorno.** Si se cambian `N_TRAIN`, `EPOCAS` o la
   versión de torch del entorno de referencia, hay que volver a correr
   `medir-experimentos.py`; las slides y las viz toman los números del JSON, pero
   los textos de `notas-docente.md`, `cuestionario-soluciones.md` y este archivo
   los citan escritos.
6. **La viz de supuestos embebida puede recortar la última fila** (el `iframe`
   tiene alto fijo). Suelta se ve entera. No se volvió a mirar en la tercera
   pasada.
7. **El mini-caso del archivo depende de la semilla** más que el resto (ver §1).
   Si se quiere que el follaje sea siempre el que peor sale, hay que rediseñar el
   generador sintético; no se hizo.

### Qué se corrió en la tercera pasada

Todo sobre copias del repo en el scratchpad, con `PYTHONDONTWRITEBYTECODE=1`:

- `medir-experimentos.py` completo, dos veces (la segunda, con la parte E
  ampliada): partes A-D idénticas entre corridas; ~5 min cada una. Los
  `datos-experimentos.json/.js` del repo son los de la segunda.
- El notebook con `jupyter nbconvert --execute`, **con** FashionMNIST en cache:
  0 errores, 53 s. Sus números son los del JSON, dígito a dígito (85,7 / 85,5 /
  87,7 / 83,1; corrimiento; archivo 96,7 % con 9 de 13 errores en follaje). Las
  frases calculadas salen bien: «la densa ni se enteró», «la densa se cae mucho
  más que la CNN», la comparación con la corrida de las slides. Los TODO sin
  resolver dan «Todavía no» sin explotar.
- El notebook **sin red y sin cache** (proxy a un puerto cerrado): cae al plan
  B, imprime el cartel con los números del JSON, 0 errores, 54 s. El barajado da
  100 / 100 y lo dice; el corrimiento sí aparece (densa 100 → 91,9 % a 3 px y
  71,5 % a 6 px; CNN 100 % en todos).
- Los filtros de la pista del TODO 2, a mano: `[[2,1,0],[1,0,-1],[0,-1,-2]]` da
  0 sobre `np.eye(9)` y 44 sobre la otra diagonal; el detector de línea
  `[[2,-1,-1],[-1,2,-1],[-1,-1,2]]`, 76 contra 44. Los dos pasan el chequeo.
- Chrome headless (`--dump-dom`, consola a stderr) sobre las slides y las 4 viz:
  0 errores de consola; los `data-num` de las slides se llenan desde el JSON
  (85,7 / 85,5 / 87,7 / 83,1 / 32,2 / 74,4) con el entorno al pie de la slide 28;
  la viz de supuestos abre sólo la RNN con `?hasta=6`, las dos filas con
  `?hasta=7` y ninguna sin parámetro, con los veredictos «✓ / ~ / ✗»; la viz
  del barajado con `#correr` escribe «pierde 53,5 puntos» / «pierde 13,3
  puntos»; el `aria-label` del mapa del kernel se actualiza con el filtro.
- Capturas (Chrome headless, 1280×760) de las slides que cambiaron de tamaño
  de texto: 16, 25, 28 y 32. Entran en pantalla; en la 25 la nota al pie queda
  pegada a las flechas de navegación, sin taparse.
- **No** se volvió a mirar con capturas el resto (tema oscuro, recortes del
  `iframe`, la marca ★/↳ de la jerarquía): lo que dice §3 sobre eso es de la
  segunda pasada. Tampoco se probaron los clics de la viz de
  la jerarquía en el navegador.

*Tercera pasada: 2026-09-29.*
