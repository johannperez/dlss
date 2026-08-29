# Guía de construcción

**Para los equipos que construyen cada clase.** Acá está todo lo que necesitás para que tu
clase se vea, se lea y se comporte como las otras nueve. Leelo entero una vez; después usalo
como referencia.

Antes que esto, va `PROGRAMA.md` y tu `_shared/especificaciones/clase-NN-slug.md`.
Esta guía es el *cómo*; ahí está el *qué*.

---

## 0. Las tres reglas que rompen todo si las rompés

1. **Cero red.** Ningún `<script src="https://...">`, ninguna Google Font, ningún CDN.
   El contenedor no tiene salida y el aula tampoco la va a tener el día que se caiga el wifi.
   Todo sale de `_shared/vendor/`, `_shared/css/` y `_shared/js/` **por ruta relativa**.
2. **Todo abre con `file://`.** Si tu página necesita un servidor, está mal hecha.
   Probala haciendo doble clic en el archivo.
3. **Ninguna viz sin momento aha.** Escribí la frase exacta que querés que el estudiante
   piense, arriba de todo en el archivo, en un comentario. Si no la podés escribir, la viz
   todavía no está diseñada. No la maquilles: rehacela.

---

## 1. Qué copiar y adónde

```
_shared/plantillas/slides-plantilla.html   ->  clases/NN-slug/slides.html
_shared/plantillas/viz-plantilla.html      ->  clases/NN-slug/viz/lo-que-sea.html
_shared/plantillas/demo.html               ->  no se copia: es el banco de pruebas de viz.js
```

Las plantillas ya tienen las rutas escritas para vivir en su destino. Si abrís la plantilla
*en su lugar* (`_shared/plantillas/`) se va a ver sin estilo: es esperable, las rutas apuntan
a dos y tres niveles arriba. Copiala primero, miralá después.

Profundidades:

| Archivo | Profundidad | Prefijo |
|---|---|---|
| `clases/NN-slug/slides.html` | 2 | `../../_shared/...` |
| `clases/NN-slug/viz/algo.html` | 3 | `../../../_shared/...` |
| `index.html` (raíz) | 0 | `_shared/...` |

---

## 2. La semántica de color

**Esto no es decoración. Es una herramienta pedagógica.** El estudiante ve las mismas cuatro
ideas diez clases seguidas; si el color cambia de significado entre la clase 3 y la 7, le
estamos pidiendo que reaprenda el código cada martes.

| Token CSS | `Viz.color()` | Significa | Aparece como |
|---|---|---|---|
| `--c-datos` | `'datos'` | **Lo observado.** La nube de puntos, el corpus, los titulares. Lo que existía antes de que llegáramos con un modelo. | puntos, barras de conteo |
| `--c-verdad` | `'verdad'` | **La verdad subyacente**, cuando la conocemos (datos sintéticos). Siempre punteada. | línea gris punteada |
| `--c-modelo` | `'modelo'` | **Lo que el modelo dibuja.** La recta, la curva, la suma de rampas, la predicción, la salida del transformer. | línea azul gruesa |
| `--c-parametro` | `'parametro'` | **Las perillas** y todo lo que vive en el espacio de perillas: pesos, sesgos, el punto en el mapa de loss, gradientes, filtros. | punto arrastrable, flechas |
| `--c-error` | `'error'` | **El desajuste.** Segmentos verticales, la loss, las alturas del valle, falsos positivos, la ficha alucinada. | palitos rojos, números de loss |
| `--c-val` | `'val'` | **Lo que el modelo no vio**: validación, test, held-out. También la segunda serie de una comparación (MAE contra MSE). | línea naranja |
| `--c-ok` | `'ok'` | Correcto, aceptado, semáforo en verde. | aciertos |
| `--c-acento` | `'acento'` | El acento de marca. **No tiene significado técnico: significa "mirá acá".** Resaltados, links, interacción viva. | turquesa |

Regla operativa: si estás por elegir un color *porque queda lindo*, pará. Elegí el token que
corresponde al **rol** de esa cosa en la explicación.

Todos los colores están además en tema oscuro. Nunca escribas un `#hex` a mano en una viz:
usá `Viz.color('modelo')`. Si hardcodeás, el tema oscuro se rompe y nadie se entera hasta el aula.

---

## 3. Las clases utilitarias del CSS

Todas funcionan igual adentro de reveal y en una página suelta.

```html
<div class="intuicion">La idea, en castellano, antes de cualquier fórmula.</div>
<div class="ojo">La confusión típica. Lo que sale mal todos los años.</div>
<div class="manos">Momento de hacer, no de mirar. Notebook, slider, discusión.</div>
<div class="aha">La revelación. Va DESPUÉS de que movieron el control, nunca antes.</div>
<div class="ss">El puente al oficio: un paper, un dato real, algo para el lunes.</div>
```

Cada una se rotula sola (`LA IDEA`, `OJO CON ESTO`, `A LAS MANOS`, `MOMENTO AHA`,
`EN CIENCIAS SOCIALES`). Agregá `class="ojo compacta"` si la slide viene apretada.

```html
<!-- término en inglés + traducción, inline -->
<span class="glosario"><span class="en">loss</span><span class="es">pérdida</span></span>

<!-- la slide de glosario del final -->
<ul class="glosario-lista">
  <li><b>overfitting</b><span>sobreajuste — calcar la muestra en vez de dibujar la forma</span></li>
</ul>

<!-- dos columnas enfrentadas -->
<div class="comparacion">
  <div><h4>Dibujar</h4><p>...</p></div>
  <div><h4>Calcar</h4><p>...</p></div>
</div>
<!-- .comparacion.tres para tres columnas; .comparacion.contra pinta verde/rojo -->

<!-- viz embebida por iframe -->
<div class="viz-frame" data-alto="grande">
  <iframe src="viz/rampas.html" title="suma de rampas" loading="lazy"></iframe>
</div>
<p class="viz-pie"><b>Qué mirar:</b> ...</p>

<!-- viz inline con viz.js: dibujo a la izquierda, perillas a la derecha -->
<div class="viz-con-panel">
  <div class="viz-frame" style="padding:8px" id="caja"></div>
  <div class="panel" id="panel"></div>
</div>
```

Otras que vas a usar: `.tarjetas` (grilla de 3, `.dos` / `.cuatro`), `.chip`,
`.chip.sintetico`, `.numero-vivo`, `.leyenda`, `.barra-medidor`, `.lectura`,
`.resaltado`, y `.c-datos` / `.c-modelo` / `.c-error` / … para pintar texto suelto.

En las slides: `section.portada` (portada de clase, se centra sola),
`section.pregunta` (la apuesta a pantalla completa, con `.opciones`),
`<span class="marca">viz</span>` (el rótulo chiquito arriba a la derecha),
`<p class="bajada">` (la frase debajo del título).

---

## 4. viz.js — la API

Se carga con un `<script src="../../../_shared/js/viz.js"></script>` y deja el global `Viz`.
Cero dependencias. `_shared/plantillas/demo.html` ejercita todo: si dudás de algo, abrilo.

### 4.1 El plano cartesiano

```js
const p = Viz.plano('#lienzo', {
  xmin: 1983, xmax: 2023, ymin: 0, ymax: 12,
  ejeX: 'año', ejeY: '% de palabras',
  titulo: 'menciones a "seguridad"',
  alto: 380            // si no lo ponés, usa relación 0.62 sobre el ancho
});

p.alDibujar(() => {
  p.fondo();                      // papel + marco + título
  p.grilla();
  p.ejes({ formatoX: v => String(Math.round(v)) });
  p.puntos(datos,     { color: 'datos', r: 4 });
  p.curva(x => a*x+b, { color: 'modelo', grosor: 3 });
  p.leyenda([{ color:'datos', texto:'observado' },
             { color:'modelo', texto:'modelo', forma:'linea' }], { pos:'ai' });
});
p.redibujar();
```

| Método | Para qué |
|---|---|
| `p.fondo(op)` / `p.grilla(op)` / `p.ejes(op)` | el andamiaje. Siempre en ese orden. |
| `p.curva(f, op)` | dibuja `y = f(x)` muestreando 400 puntos |
| `p.linea(pts, op)` | polilínea por `[{x,y}]` o `[[x,y]]` |
| `p.puntos(pts, op)` | nube de puntos (cada punto puede traer su `color`, `r`, `etiqueta`) |
| `p.punto(x, y, op)` | un punto solo, con `halo:true` para el arrastrable |
| `p.segmento(x1,y1,x2,y2,op)` | los palitos del error |
| `p.flecha(x1,y1,x2,y2,op)` | vectores; el `−gradiente` |
| `p.poligono(pts, op)` | áreas, bandas. `{color:'modelo'}` lo tiñe con transparencia; `{relleno:'#rgba'}` fija el color a mano; `{relleno:false}` sólo borde |
| `p.barras(items, op)` | `[{etiqueta, valor, color}]`, `horizontal:true` |
| `p.celdas(M, op)` | matriz como grilla de celdas en el canvas (un filtro 3×3) |
| `p.mapaDeCalor(f, op)` | superficie `z=f(x,y)`, devuelve `{min,max}` |
| `p.contornos(f, op)` | curvas de nivel encima del mapa (marching squares) |
| `p.texto(x,y,t,op)` / `p.textoPx(X,Y,t,op)` | rótulos; `caja:true` les pone fondo |
| `p.leyenda(items, op)` | `pos: 'ai' \| 'ad' \| 'bi' \| 'bd'` |
| `p.px(x)` / `p.py(y)` / `p.aMundo(px,py)` | mundo ↔ pixel |
| `p.limites(...)` / `p.autoescala(pts)` | cambiar el encuadre |
| `p.alDibujar(fn)` / `p.redibujar()` | registrar y disparar el dibujo (agrupado en un frame) |

Opciones comunes de trazo: `color`, `grosor`, `punteada` (`true` o `[6,5]`), `opacidad`, `n`.

### 4.2 Interacción

```js
p.arrastrables(nube, {                 // los puntos se modifican en el lugar
  radio: 16, acotarX: [1984, 2022], fijarY: true,
  alArrastrar: () => recalcular(),     // se llama MIENTRAS arrastrás
  alSoltar:    () => guardar()
});

p.tooltip(w => `año ${Math.round(w.x)}\nvalor ${Viz.num(w.y, 2)}`);
p.alClic(w => { a = w.x; b = w.y; });
p.alMover(w => cursor = w);
```

> El redibujo durante el arrastre es **obligatorio**, no un lujo. Está en varias specs con
> mayúsculas: el panel de la derecha se actualiza mientras se arrastra, no al soltar.

### 4.3 El panel de controles

```js
const ctl = Viz.controles('#panel', [
  { tipo:'titulo', texto:'Las perillas' },
  { tipo:'slider', id:'a', etiqueta:'qué tan empinada', sub:'puntos por año',
    min:-0.3, max:0.4, paso:0.005, valor:0.05, decimales:3, color:'parametro' },
  { tipo:'slider', id:'lr', etiqueta:'tasa de aprendizaje',
    min:0.0001, max:2.0, escala:'log', valor:0.08, formato: v => v.toFixed(4) },
  { tipo:'checkbox', id:'errores', etiqueta:'mostrar los errores', valor:true },
  { tipo:'select', id:'estrategia', etiqueta:'cómo partir',
    opciones:[{valor:'azar',texto:'al azar'},{valor:'tiempo',texto:'por tiempo'}] },
  { tipo:'botones', id:'vista', etiqueta:'qué mostrar', valor:'nube',
    opciones:[{valor:'nube',texto:'la nube'},{valor:'ajuste',texto:'el ajuste'}] },
  { tipo:'medidor', id:'des', etiqueta:'desajuste' },
  { tipo:'boton', texto:'Reiniciar', principal:true, alClic: () => reset() },
  { tipo:'texto', id:'lectura', html:'' }
], (v, id) => { a = v.a; p.redibujar(); });

ctl.set('a', 1.2);              // cambiar por código (tercer argumento true = sin avisar)
ctl.get('a');
ctl.texto('lectura', 'El MSE está mirando al caso <b>#7</b>.');
ctl.medidor('des', 0.7, '18.4');
ctl.disparar();                 // llamalo una vez al final, para el primer dibujo
```

Los sliders **siempre** llevan el número al lado y el nombre en castellano sustantivo
(`"qué tan empinada"`, `"dónde está el codo"`), no `a` y `b`.

`tipo:'botones'` tiene dos usos y la diferencia es una sola clave:

- **con `valor`** es un **selector segmentado**: guarda el elegido en
  `ctl.valores[id]`, marca el activo con la clase `activo`, y `ctl.set(id, v)`
  lo cambia por código. Es lo que querés casi siempre.
- **sin `valor`** es una fila de **botones de acción**, cada uno con su `alClic`
  y sin valor asociado. Si le ponés `opciones` con `valor` pero te olvidás el
  `valor` del grupo, el control se dibuja pero **no guarda nada**.

### 4.4 Animación

```js
const anim = Viz.animacion({
  cadaMs: 45,                                   // 0 = un paso por frame
  paso: (i) => { unPasoDeDescenso(); p.redibujar(); return i < 160; },  // false = frenar
  reset: () => { a = 0; b = 0; p.redibujar(); }
});
Viz.controlesAnimacion('#panel', anim, {
  textoPlay: 'Soltar la pelota', textoPausa: 'Frenar',
  textoPaso: 'Un paso', textoReset: 'Reiniciar'
});
// también: anim.play() anim.pausa() anim.unPaso() anim.reset() anim.corriendo() anim.iteracion()
```

### 4.5 SVG (arcos, diagramas de red)

```js
const s = Viz.svg.crear('#caja', { ancho: 940, alto: 190 });
Viz.svg.arco(s, x1, y1, x2, y2, { curva:.55, grosor: 1 + peso*16, color:'acento', opacidad:.7 });
Viz.svg.el('rect', { x, y, width, height, rx:7, fill: Viz.color('papel2') }, s);
Viz.svg.limpiar(s);
```

### 4.6 Matriz de calor con etiquetas (la matriz de atención)

```js
Viz.matrizCalor('#mapa', A, {
  etiquetas: palabras, paleta:'acento', celda: 26, min: 0, max: 1,
  alHover: (f, c, v) => leer(`"${palabras[f]}" le presta ${(v*100)|0}% de su atención a "${palabras[c]}"`),
  alSalir: () => leer('Pasá el mouse por una celda.')
});
```

### 4.7 Colores y paletas

```js
Viz.color('modelo')            // resuelve el token; si le pasás '#abc' lo devuelve igual
Viz.colores()                  // el objeto entero
Viz.alfa('error', .15)         // el mismo color, transparente
Viz.mezclarColor('ok','error',.5)
const pal = Viz.paleta('loss');        // 'loss' | 'divergente' | 'acento' | 'grises'
Viz.recargarColores();                 // si cambiaste el tema a mano
```

### 4.8 Matemática

```js
Viz.M.matmul(A,B)  Viz.M.transponer(A)  Viz.M.dot(a,b)  Viz.M.norma(a)  Viz.M.coseno(a,b)
Viz.M.softmax(v, T)                     // T = temperatura, opcional
Viz.M.sigmoid  Viz.M.tanh  Viz.M.relu   // y sus derivadas: dsigmoid, dtanh, drelu
Viz.M.mse(pred, y)  Viz.M.mae(pred, y)
Viz.M.ceros(f,c)  Viz.M.aleatoria(f,c,escala,semilla)
```

### 4.9 Una red entrenando adentro de la slide

```js
const red = new Viz.Red([1, 8, 1], { activacion:'relu', semilla: 4 });
const l = red.paso(X, Y, 0.035);   // un paso de descenso sobre todo el lote; devuelve la loss
red.predecir([[2.5]]);             // [[valor]]
red.adelante([2.5]).salida;        // ojo: adelante() devuelve {A, Z, salida}, no un array
red.perdida(X, Y);
red.rampas();                      // para [1,H,1]: las H rampas sueltas, como funciones
red.reiniciar(99);                 // otros pesos, otra semilla
```

Forward y backward están escritos a mano, sin trucos, en `viz.js`. Es la misma cuenta que
hace PyTorch. Sirve para la clase 2 (suma de rampas), la 3 (descenso) y la 4 (loop y sobreajuste).

### 4.10 Utilidades varias

```js
Viz.azar(42)      // generador con semilla: SIEMPRE con semilla, nunca Math.random pelado
Viz.gauss(42)     // ruido normal con semilla
Viz.linspace(0,1,50)   Viz.rango(8)   Viz.acotar(v,0,1)
Viz.mezclar(0, 10, .25)   // interpolación lineal -> 2.5. NO baraja un array.
Viz.num(3.14159, 2)    // "3.14"
Viz.el('button', { class:'boton', texto:'Otra muestra' }, padre)
Viz.botonTema()        // el botón flotante claro/oscuro (poné uno por página standalone)
```

**Modo embebido.** `viz.js` detecta solo si la página está adentro de un `<iframe>` y le pone
`class="embebido"` al `<body>`. El CSS esconde el título, el pie y el botón de tema, porque eso
ya lo dice la slide. **Un archivo, dos presentaciones**: no hagas dos versiones de la misma viz.

---

## 5. Cómo se escribe

- **Español rioplatense neutro-informal.** Voseo suave: *"vos podés"*, *"fijate"*, *"mirá qué pasa"*.
  Cero solemnidad académica. Se puede tener humor; se debe tener humor.
- **Los términos técnicos van en inglés** (*loss*, *gradient descent*, *embedding*, *attention*,
  *overfitting*) y **se explican en castellano la primera vez** que aparecen, con
  `<span class="glosario">`. Después van a `recursos/glosario.md` con la clase donde salieron.
- **Nunca "no se asusten".** No se anuncia el susto. Tampoco *"esto es fácil"*: si al que no le
  sale se entera de que era fácil, la pasa peor.
- **Ninguna métrica sin su frase en castellano llano.** Si no podés decir
  *"de cada 100 que el modelo llamó protesta, 78 lo eran"*, no la entendiste y no la ponés.
- **El parámetro se traduce a afirmación sustantiva.** No *"la pendiente es 0.4"*, sino
  *"cada año sube 0.4 puntos"*.
- **Los datos sintéticos se rotulan siempre.** El corpus Aguasclaras lleva su
  `<span class="chip sintetico">sintético</span>` cada vez que aparece. País ficticio,
  proceso generador conocido, cero frases inventadas en boca de gente real.
- **Semillas fijas, siempre**, en el notebook y en la viz. Desde la clase 4 se explica por qué;
  desde la 1 se hace.

---

## 6. Errores a evitar

**Técnicos**

- Rutas absolutas (`/home/...`, `/_shared/...`). Todo relativo, siempre.
- Cualquier `https://` en un `src` o un `href` de hoja de estilo. Cero CDNs, cero Google Fonts.
- Hardcodear `#1f6fb5` en vez de `Viz.color('modelo')`: rompe el tema oscuro y rompe la semántica.
- `Math.random()` sin semilla: la clase de al lado ve otra nube y el docente queda explicando ruido.
- Canvas sin `alDibujar` / `redibujar`: se dibuja una vez, no se redibuja al cambiar el tema ni
  al redimensionar, y en el proyector aparece cortado.
- `localStorage` sin `try/catch`: con `file://` a veces tira excepción y te mata la página entera.
- Notebooks que dependen de la red: patrón `try: descargar() / except: generar_sinteticos()`,
  obligatorio, sin excepciones.
- **Inventar la escala de los datos.** `serie_menciones` devuelve **porcentaje de
  palabras del discurso**, y son números chicos: la serie real de `seguridad` va
  de 0 a 0,44 **por ciento**. Si tu eje llega a 14 %, el número es fantasía.
  Rotulá el eje `% de palabras` y usá los valores que devuelve la función.
- **Poner un número de referencia sin medirlo.** Si tu panel dice "lo mejor que se
  consigue ronda 2,6", hacé el barrido y comprobalo. Un número inventado en un
  curso sobre no inventar es el peor error posible.
- **Olvidarse la slide de pausa.** Cada clase tiene 10 minutos de pausa en su
  presupuesto de tiempo y una `<section class="pausa">` que la marca. Si no está
  en las slides, la pausa se la come el entusiasmo y la segunda mitad se atropella.

**Pedagógicos** (peores)

- **Una viz que no dice nada.** Mover un slider y que cambie un dibujito lindo no es aprender.
  Tiene que haber una creencia que se rompe. Si la spec dice que hay que **apostar antes**
  (slide de votación a mano alzada), la slide de la apuesta va antes de la viz. Sin la predicción
  fallida, el slider es decoración.
- **Mostrar sólo los éxitos.** La aritmética de embeddings tiene botón *"ejemplos que NO funcionan"*;
  la búsqueda semántica tiene *"mostrar los falsos positivos"*; una de las cuatro cabezas de
  atención es deliberadamente no interpretable; los filtros al azar dan porquería.
  El entusiasmo mágico es el enemigo principal del criterio.
- **Fórmula sin figura al lado.** Si escribís una ecuación y no tenés al lado una figura, una
  animación o un slider que muestre qué hace: borrá la fórmula. No la muevas de lugar, borrala.
- **Romper una siembra.** El botón *"32 rampas"* de la clase 2 se cobra en la clase 4; el panel
  *"¿cuántas R tiene?"* del tokenizador de la 6 se cierra en la 8 con el cartel
  *"prometido en la clase 6, cumplido"*; `viz/supuestos-de-arquitectura.html` se construye en la
  clase 5 con dos filas grises y se reutiliza en la 7 con esas filas desbloqueadas.
  Están puestas a propósito. Coordiná con el equipo de la otra clase antes de tocarlas.
- **Números inventados en una viz.** Si la viz muestra el resultado de un experimento (el
  barajado de píxeles, la curva de cuántas etiquetas hacen falta), esos números tienen que salir
  de una corrida real guardada en el notebook de esa clase. Coherencia viz–notebook, obligatoria.
- **Abstracción antes de haber hecho a mano lo que esconde.** El descenso se escribe con
  derivadas numéricas antes de `autograd`; `nn.Sequential` aparece con la versión a mano al lado
  y un `assert`; `Conv2d` se verifica contra el doble `for`; el `Trainer` de HF se muestra junto
  al loop de la clase 4.

---

## 7. Antes de dar tu clase por terminada

- [ ] `slides.html` abre con `file://` y **no tira ni un error en la consola**.
- [ ] Cada `viz/*.html` abre suelta **y** embebida en la slide, y en las dos se ve bien.
- [ ] Probaste con tema claro **y** oscuro (botón abajo a la derecha en las viz).
- [ ] Probaste a 1280×720 (proyector) y en una ventana angosta.
- [ ] Cada viz tiene su momento aha escrito en un comentario arriba de todo, y al mover el
      control **efectivamente pasa eso**.
- [ ] Ningún color hardcodeado; todo por `Viz.color()` o por variable CSS.
- [ ] Todos los términos nuevos en inglés están en `recursos/glosario.md` con su clase.
- [ ] `referencias.md` no tiene ninguna URL sin `VERIFICADA` o `[VERIFICAR URL]`.
- [ ] El notebook corre en CPU, de punta a punta, sin red, en minutos.
- [ ] Hay un `[EL LUNES]`: algo concreto que le sirve en su investigación esta semana.

Para probar rápido que `viz.js` anda: abrí `_shared/plantillas/demo.html`. Si ahí se ve bien y
en tu página no, el problema es tuyo, no de la biblioteca.
