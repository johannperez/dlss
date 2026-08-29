# Verificación adversarial — Clase 5

**«La forma de los datos manda (I): imágenes»** · `clases/05-imagenes-y-convoluciones/`

Segunda pasada, hecha por alguien que **no** construyó la clase y que empezó
por no creerle al informe del que la construyó. Todo lo que dice acá se
comprobó **corriendo el código y mirando los PNG**, no leyendo los archivos:
`nbconvert --execute` cronometrado (cuatro veces, una de ellas con la red
cortada y la cache borrada), Chromium por Playwright con `context.route`
abortando **cualquier** `http(s)`, `curl` sobre cada URL, y **más de 60
capturas miradas con los ojos** —slides, viz antes y después de mover cada
control, y las figuras que produce el notebook—.

**Veredicto: la clase se puede dar.** Se encontraron **11 problemas** y se
arreglaron **11**. Uno era serio (el notebook afirmaba en voz alta algo falso
cuando corría sin internet); el resto eran de coherencia, de rigor fino y de
maquetación.

---

## 1. Lo que se midió, con el número real

| Chequeo | Resultado |
|---|---|
| `nbformat.validate` | **válido**, 50 celdas |
| `nbconvert --execute` (con cache, máquina tranquila) | **0 errores** · **81 s**, **86 s**, **91 s** y **116 s** en cuatro corridas |
| `nbconvert --execute` **sin red y sin cache** (plan B sintético) | **0 errores** · **170 s** |
| Slides: consola y red | **36 slides recorridas una por una: 0 errores, 0 requests externas** |
| Las 4 viz sueltas: consola y red | **0 errores, 0 requests externas** cada una |
| Los 4 `<iframe>` embebidos en las slides | **cargan y dibujan** (verificado por captura, no por inspección del HTML) |
| KaTeX | carga sin error; **la clase no usa ni una fórmula**, así que no hay nada que renderizar (es deliberado) |
| Tema oscuro | slides y viz, **correctos** (verificado por captura) |
| `medir-experimentos.py` reproduce sus propios datos | **sí: todos los números idénticos**, sólo cambian los `segundos` de reloj |
| Notebook ↔ `datos-experimentos.json` ↔ slides ↔ viz | **coinciden dígito a dígito** |
| La permutación del barajado del `.js` vs la del notebook | **la misma** (`np.random.default_rng(1983).permutation(784)`) |
| URLs de `referencias.md` | 1 responde (**200**), y es la única marcada `[VERIFICADA]`. Las otras 13 están marcadas `[VERIFICAR URL]` |
| Presupuesto de tiempo | **120 min exactos**, continuo, con la pausa entera |

### Los números de la clase, remedidos acá

Corrida real, semilla 1983, 12.000 imágenes de entrenamiento, 12 pasadas:

| | perillas | foto normal | píxeles barajados | corrida 3 px |
|---|---|---|---|---|
| red densa | 50.890 | 85,8 % | **85,6 %** | **32,3 %** |
| CNN | 23.946 | **87,8 %** | 83,2 % | **74,1 %** |

Mini-caso del archivo fotográfico sintético: **97,0 %** global, **88,5 %** en
follaje, **7 de los 12 errores** ahí. Todo verificado dos veces (notebook y
`medir-experimentos.py`, por separado).

---

## 2. Los 11 problemas encontrados, y qué se hizo

### Serio

**1. Sin internet, el notebook afirmaba algo falso.**
Con la red cortada y la cache borrada, el notebook cae a su plan B (figuras
sintéticas de numpy) y corre entero, como promete. Pero ese plan B es
**demasiado fácil**: los cuatro modelos sacan 100,0 % y el barajado no le
mueve nada a ninguno (0,0 y 0,0). El problema no era ése: era que la celda
**imprimía igual** el texto fijo *«La densa ni se enteró. La CNN sí»* — o sea,
el argumento central de la clase, afirmado sobre unos números que dicen
exactamente lo contrario. En un aula sin wifi, eso se proyecta.
*Arreglado:* (a) la narración de la caída ahora se **calcula** a partir de lo
medido y, si las dos redes quedan igual, dice que este experimento no muestra
lo que muestra en clase y por qué; (b) la rama del plan B imprime un cartel
grande que avisa lo mismo y **da los números medidos de FashionMNIST para la
discusión**. Comprobado volviendo a correrlo sin red: sale el cartel, sale la
advertencia, 0 errores.

### De rigor

**2. «La red densa es *exactamente* la de la clase 4» no era cierto.**
La clase 4 entrena `Linear(1,16) → ReLU → Linear(16,1)` sobre una serie de
números; acá es `Flatten → Linear(784,64) → ReLU → Linear(64,10)`. Es la
**misma forma de máquina**, no la misma red, y un estudiante que vuelva a la
clase 4 a buscar el 784→64 no lo encuentra. Aparecía tres veces (slide 6,
slide 16 y dos celdas del notebook).
*Arreglado:* se dice lo que es —«la misma máquina de la clase 4: dos capas
densas con un doblez en el medio; lo único que cambia es que ahora entran 784
números en vez de uno»—, que además es más útil para el argumento.

**3. «Cada casilla es un número de 0 a 255: cuánta *materia* hay ahí».**
No es nada: el número es luz, y encima la slide la dibuja invertida (tinta
sobre papel) y lo aclara dos líneas abajo. Las notas del docente decían
«cuánta luz» y la slide decía otra cosa.
*Arreglado:* dice «cuánta luz hay en ese punto», que es lo que es y lo que
coincide con las notas.

**4. El notebook mandaba a la sección 6 y el mini-caso está en la 5.**
La celda del cartel de FashionMNIST prometía «en la sección 6 volvemos al
dominio», y `referencias.md` hablaba del «corpus visual de la sección 6». La 6
es «qué te llevás». *Arreglado en los dos.*

**5. Tiempos declarados optimistas.** El notebook decía «menos de 4 minutos» y
«unos 70 segundos» los cuatro entrenamientos; las notas del docente decían
«~1 minuto». Medido: **81-116 s** el notebook entero, y ~90 s los cuatro
entrenamientos. *Arreglado con los números medidos y con la advertencia de que
en Colab y con la máquina cargada es más.*

**6. El cuestionario decía «Once preguntas» y tiene doce.** *Arreglado.*

### De coherencia

**7. `notas-docente.md` numeraba las slides sin contar la pausa.**
El mazo muestra `n / 36` con la pausa como slide 18; las notas venían de la
especificación, donde la pausa no está numerada, así que **todo lo posterior a
la pausa estaba corrido en uno**: «las slides 24-25» eran la 25-26 en pantalla,
«el bloque 28-30» era el 29-31, y los cuatro números que el docente tiene que
saber de memoria estaban en «la slide 27», que en pantalla es la 28. Con el
proyector prendido eso hace perder treinta segundos cada vez.
*Arreglado:* la tabla de tiempos y las quince referencias sueltas pasan a la
numeración del mazo, y arriba de la tabla quedó dicho cuál es cuál.
Lo mismo en `referencias.md` («el caso de las slides 28-30» → 29-31).

**8. Punto y coma decimales mezclados.** Las slides escriben **85,6 %** y la
viz embebida al lado, en la misma pantalla, escribía **85.6 %** (`Viz.num`
devuelve punto). *Arreglado local en `vecindad-de-pixeles.html`*, con un
ayudante de una línea; no se tocó la biblioteca compartida, que usan las otras
nueve clases.

### De maquetación

**9. La viz de supuestos dejaba un recuadro vacío en la slide 26.**
El archivo escondía el *texto* de la ayuda «cómo se lee» cuando va embebida,
pero no la **caja ni su rótulo**: en el proyector se veía un cartel con título
y nada adentro. *Arreglado:* ahora se esconde la ayuda entera (título + caja),
y de paso entra más de la fila del Transformer. Verificado por captura.

**10. El rótulo del máximo global se salía de su caja** en el diagrama de la
CNN (slide 24): «máx de cada mapa → 64» pisaba el borde derecho.
*Arreglado:* «máx por mapa → 64».

**11. `.viz-frame` de `curso.css` no tiene `box-sizing`** y con padding propio
se monta sobre el panel. El equipo anterior lo parchó local en los cinco HTML
de esta clase. **Se confirma que el parche funciona** (la jerarquía embebida ya
no corta la primera letra de los rótulos) y **se confirma que el defecto es del
CSS compartido**: sigue abierto para el equipo de la espina.

---

## 3. Lo que se revisó y está bien (no se tocó)

- **Los cuatro momentos aha existen y se ven.** Se movió cada control y se
  miró el resultado:
  - *Barajar*: la animación de los píxeles mudándose, las dos tiras con los
    mismos 784 números, y las barras 85,8 → 85,6 contra 87,8 → 83,2. La
    segunda pestaña («correrla») da 85,8 → 32,3 contra 87,8 → 74,1 y el slider
    de 0 a 6 píxeles responde en vivo.
  - *Kernel deslizante*: con «borde vertical» sobre el afiche se encienden
    **sólo** los palotes verticales de las letras; «todo cero» deja el panel 3
    vacío; «identidad» devuelve la imagen; «filtro al azar» da porquería una y
    otra vez. Las ocho imágenes cargan y la cuenta de los nueve productos se
    actualiza.
  - *Jerarquía*: clic en «la rueda» enciende arco + círculo + unión en T de la
    capa 2 y los bordes de la capa 1, con las líneas de composición dibujadas.
    «La multitud» baja a cabeza y pancarta. El rótulo de «esquema ilustrativo»
    está puesto.
  - *Supuestos*: con «una tabla de encuesta» **no se pone verde ninguna fila** y
    aparece el cartel de los modelos de árboles. Las seis opciones de datos
    funcionan; RNN y Transformer quedan grises para las clases 6 y 7.
- **Las figuras del notebook** (13, todas miradas): ejes rotulados, leyendas,
  y la de los errores del mini-caso muestra la confusión follaje/multitud sin
  necesidad del texto.
- **Las citas.** Se revisó una por una: Jean et al. 2016 *Science* 353(6301)
  790-794 con su DOI, Olah et al. *Distill* con su DOI, Zeiler & Fergus ECCV
  2014, Grinsztajn et al. NeurIPS 2022, Cantú 2019 APSR 113(3), Torres & Cantú
  2022 *Political Analysis* 30(1), Rolf et al. 2021 *Nat. Commun.* 12,
  Krizhevsky 2012 (el 26 %→15 % es top-5, y está bien dicho), LeCun et al. 1998
  *Proc. IEEE* 86(11). **No se encontró ninguna cita inventada ni ningún autor
  o año mal.** Ninguna URL se afirma sin haberla abierto.
- **El cuestionario.** Las doce preguntas se contestan con lo que se dio.
  Las soluciones son correctas —incluidas las cuentas: 16·9+16 = 160,
  784·16+16 = 12.560, y 78,5 veces— y los distractores son tentadores, no
  absurdos (el de la pregunta 2, «la imagen de salida», es literalmente la
  confusión que la clase viene a desarmar).
- **Tono.** Voseo sostenido, humor sin chiste forzado, cero condescendencia,
  ningún párrafo-muro. No hay una sola slide sin imagen, ejemplo o pregunta.
- **Los puentes.** Hacia atrás: slide 2 (el módulo 1 entero) y los callbacks a
  las clases 2, 3 y 4 en las slides 6, 15, 16 y 22. Hacia adelante: la fila
  gris de RNN en la viz de supuestos, la clase 9 en las slides 32 y 33, y la
  slide 36 con la frase de la comisión y el ministro.
- **Coherencia con la especificación.** Están los 34 bloques del guion, en su
  orden, más la slide de pausa (obligatoria) y la de «tres ideas». Las dos
  desviaciones que declaró el equipo constructor —la arquitectura con máximo
  global y el experimento del corrimiento— **se verificaron midiendo**: son
  mejoras, no atajos, y sin ellas el aha se cae (con conv→pool→conv→pool→densa
  el barajado casi no mueve la aguja).

---

## 4. Lo que queda abierto

1. **Los 13 `[VERIFICAR URL]` y los `DOI [VERIFICAR]`.** Desde este contenedor
   sólo responde `raw.githubusercontent.com`. Se confirmó con `curl`: la única
   URL de la lista que devuelve 200 es la del README de FashionMNIST, y es la
   única marcada `[VERIFICADA]`. **Nada de esto frena la clase**: las obras se
   encuentran por autor y título, y todas existen.
2. **`.viz-frame { box-sizing: border-box }` tiene que ir a
   `_shared/css/curso.css`.** Está parchado local en los cinco HTML de la clase
   5, pero el defecto afecta a cualquier `.viz-frame` con padding propio de las
   otras nueve clases. Es para el equipo de la espina.
3. **La slide 3 usa un esquema sintético de multitud dibujado con numpy.**
   Funciona y está rotulado, pero se lee como un montón de crucecitas, no como
   una foto: una foto real de una movilización con licencia libre funcionaría
   mejor. Es lo primero que conviene reemplazar; está anotado en
   `notas-docente.md` §11.
4. **El plan B sin internet no reproduce el experimento del barajado.** Ahora
   lo dice en voz alta (problema 1), pero sigue siendo un plan B degradado: si
   se quiere que el argumento cierre también sin red, hay que diseñar un
   conjunto sintético con estructura espacial que un modelo denso no pueda
   resolver de memoria. No es trivial y no se intentó acá.
5. **El tiempo del notebook depende mucho de la carga de la máquina.** Medido:
   81 s, 86 s, 91 s y 116 s en este contenedor. En Colab (2 vCPU) hay que contar
   3-4 minutos. Las palancas son `N_TRAIN` (12.000) y `EPOCAS` (12) en la celda
   de configuración, **pero si se tocan hay que volver a correr
   `medir-experimentos.py`**, porque las slides y las viz muestran esos números
   exactos.
6. **La viz de supuestos embebida sigue recortando la última fila** (el alto
   del `iframe` es fijo, 610 px). Suelta —que es como la proyecta el docente—
   se ve entera. Si alguien quiere que entre también embebida, hay que acortar
   los textos de la fila del Transformer.
7. **La clase 7 tiene que desbloquear las filas de RNN y Transformer** de
   `viz/supuestos-de-arquitectura.html`. Está anotado en el pie de la propia
   viz y en las notas del docente.

---

## 5. Cómo reproducir esta verificación

```bash
# el notebook, cronometrado
time python3 -m nbconvert --to notebook --execute --output /tmp/out.ipynb \
     clases/05-imagenes-y-convoluciones/notebook.ipynb

# el notebook SIN red y SIN cache (hay que mover datos/cache/fashion-mnist y devolverlo)
HTTPS_PROXY=http://127.0.0.1:9 python3 -m nbconvert --to notebook --execute ...

# que los números de las slides salgan de una corrida real
PYTHONPATH=_shared python3 clases/05-imagenes-y-convoluciones/medir-experimentos.py
git diff clases/05-imagenes-y-convoluciones/datos-experimentos.json   # sólo cambian los segundos

# el HTML, a la profundidad real, con la red abortada
#   PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers  NODE_PATH=/opt/node22/lib/node_modules
#   chromium.launch({executablePath:'/opt/pw-browsers/chromium'})
#   ctx.route('**/*', r => /^https?:/i.test(r.request().url()) ? r.abort() : r.continue())
```

*Verificado el 2026-08-29.*
