# Verificación — Clase 10

**Criterio: validez, sesgo, reproducibilidad y el revisor 2**

Dos pasadas: la construcción se verificó el **2026-08-29**, y el **2026-09-29** se hizo una
segunda ronda después de una revisión externa que encontró problemas de rigor estadístico y de
coherencia. Este archivo describe el estado **después de la segunda ronda**, y dice qué se
comprobó de verdad y qué no.

---

## 1. Veredicto

**La clase es apta para dictarse.** La revisión externa encontró que la lección metodológica
central (la «banda de ruido») comparaba mal, que el diagnóstico de los nombres propios estaba
sobreafirmado, que ninguno de los dos «placebos» era un placebo y que la procedencia del corpus
estaba mal fechada. Todo eso se corrigió y los números se volvieron a medir (§2). Lo que queda
abierto está en §5; nada frena la clase.

| Chequeo (2026-09-29) | Resultado |
|---|---|
| `nbformat.validate(notebook.ipynb)` | **válido**, 63 celdas, guardado **sin salidas** |
| `nbconvert --execute` en una copia, sin red | **0 errores, 0 stderr, 5 figuras**, **11-13 s** de punta a punta (una laptop; Python 3.12.13, numpy 2.5.3, scikit-learn 1.9.1, matplotlib 3.11.2) |
| `medir-clase10.py` corrido dos veces | `datos-clase10.json`, `.js` y `pesos-clase10.js` **idénticos** entre corridas (md5), **en esta máquina y con estas versiones**. El JSON anota las versiones (clave `entorno`) |
| `exportar-figuras.py` corrido dos veces | los 5 PNG **idénticos entre corridas en el mismo entorno**. Con otra versión de matplotlib los bytes cambian aunque el dibujo sea el mismo |
| Assert de la viz 2 | la cuenta a mano da lo mismo que `predict_proba` (dif. máx. 3,5·10⁻⁶), y la tokenización a mano da las mismas fichas que scikit-learn en los 1471 documentos |
| Números de slides, notas, cuestionario y viz contra la corrida | verificados uno por uno (§3) |
| Viz en navegador | Chrome *headless*: las tres páginas cargan y se recorrieron sus estados con un script (casos 1-3 × antes/después; las 4 dimensiones con «marcar»; checklist vacío → ejemplo → modo revisor), **0 errores de JavaScript**. Capturas de pantalla de la viz 1 («después») y la viz 2 miradas a ojo |
| Slides en navegador | capturas de las slides 4, 5, 6, 13, 15, 18, 20, 22 y 38 (las que cambiaron): sin desborde. **No** se repitió la medición automática de desborde de las 40 |
| Bootstrap de Colab (celda 2) | no se tocó (md5 del source `4c9c6d9d…`, igual a los otros nueve notebooks) |

---

## 2. Qué se arregló en la segunda ronda (2026-09-29)

### Rigor

1. **La banda de ruido comparaba mal.** Ponía la diferencia de una ablación (original contra
   ablado, **sobre la misma partición**) al lado del **rango** del F1 suelto entre 25 semillas
   (0,107) y concluía «un test que se mueve menos que el ruido no es un test». Pero el error de
   una diferencia pareada no es el rango de cada número suelto, y el rango crece con la cantidad
   de semillas. *Ahora:* la sección 5 del notebook repite cada ablación sobre las 25 particiones
   y reporta la **diferencia pareada** con media, desvío e intervalo (error estándar con la
   corrección de Nadeau y Bengio, 2003, porque las particiones comparten notas). Resultado:
   sacar los 20 términos más fuertes baja el F1 −0,030 (IC −0,054 a −0,006, 22 de 25
   particiones); los 19 nombres propios, −0,014 (IC −0,030 a +0,001, 21 de 25); los 5 primeros
   y el primero no se distinguen de cero. Con **una** partición, los 5 primeros parecían
   *mejorar* el F1 (+0,033). La moraleja nueva: *no interpretes una diferencia sin su error, y
   medí el error de la comparación que hacés.* Cambió la figura 03, la slide 18, la viz 1, el
   `TODO 2`, las notas y la ficha.
2. **«Detector de nombres de la coyuntura mexicana» estaba sobreafirmado.** Salía de leer
   coeficientes. *Ahora* es una hipótesis (`TODO 1`, slide 4) que el notebook **testea**:
   reentrenado sin nombres propios, el F1 casi no cambia (0,680 → 0,667) y el control positivo
   sube de 22 a 32 %. Los nombres explican una parte de la falla; el resto es dominio y género
   textual.
3. **Ninguno de los dos «placebos» era un placebo.** El barajado es un **test de invariancia**
   y Aguasclaras (titulares de política institucional) es un **segundo control positivo fuera de
   dominio**; el texto decía además «sesiones parlamentarias» y «otra época», y ninguna de las
   dos cosas era cierta. *Ahora* están renombrados y hay un **placebo de verdad**: las 65 notas
   de Deporte y Espectáculos del test, de las que marca 7 (11 %), cuatro de ellas con nombres de
   políticos. En el JSON, las claves pasaron a `control_positivo`, `placebo`, `invariancia` y
   `fuera_de_dominio`.
4. **El control positivo mezclaba largo y dominio**, y los 600 fragmentos salían de los primeros
   discursos del archivo (sobre todo Fernández). *Ahora* usa **todas** las oraciones de 60-220
   caracteres de los 123 discursos (824, de 120 discursos) y agrega la referencia del mismo largo:
   oraciones de las notas de política del propio test. Recall: 0,64 en notas enteras, **0,49**
   en oraciones sueltas de sus notas, **0,22** en oraciones de discursos (antes 0,21 sobre los
   600 primeros).
5. **Test de permutación con pseudo-replicación.** Las 10 diferencias de género comparten el
   mismo coeficiente del artículo (+0,204 en logit) y en 6 de los 10 pares es lo único que
   cambia. *Ahora* la celda descompone cada diferencia en artículo + sustantivo, enumera los
   1024 patrones de signo (p exacto 0,0020, el mínimo posible) y dice por qué ese p no agrega
   nada.
6. **La procedencia del corpus estaba mal fechada** («nov-2020 a mar-2021», «cinco meses de
   pandemia», y la ficha se contradecía sola con «2018-2021»). *Ahora* dice lo que está en
   `datos/README.md` §1.3: 971 notas de enero a julio de 2018 y 500 de noviembre de 2020 a marzo
   de 2021. Notebook, ficha, slides, viz 2 y 3, soluciones.
7. **Prevalencia.** El modelo entrena con `class_weight="balanced"` y el ejemplo del checklist
   justificaba el umbral «porque nos interesa estimar prevalencia». Contando predicciones da
   24,7 % donde hay 28,0 %. *Ahora* hay una celda que lo muestra con la corrección
   *classify-and-count* (con la salvedad de que hacerla sobre el mismo test es circular), una
   limitación nueva en la ficha, y el ejemplo del checklist y la slide 20 lo dicen.
8. **Cuestionario, ítem 5.** La tabla ponía «las enfermeras» = «los enfermeros» = 0,265, contra
   el mecanismo del artículo que enseña la clase, y la solución decía que 0,265 era la oración
   sin sujeto (es 0,336). *Ahora* la tabla usa los puntajes reales del modelo de la clase
   (0,346 / 0,275 / 0,307 / 0,265) y la solución descompone artículo y sustantivo.
9. **Juicio, Paper A.** Las cuentas no cerraban (32 falsos positivos con 150 notas de test), la
   partición decía «por diario y por año» y describía sólo por diario, y había «notas deportivas»
   en un corpus de Política y Sociedad. *Ahora* cierran: 600 notas en cuatro rotaciones, 84
   verdaderos positivos, 22 falsos, *accuracy* 0,91; el intervalo del F1 y del aumento es por
   *bootstrap*; y la cuenta está escrita en el recuadro inicial para quien quiera verificarla.
10. **`TODO 7` tenía una pista falsa** (con bolsa de palabras el barajado da siempre lo mismo;
    no había azar suelto que encontrar). *Ahora* hay una celda con una fuente de azar suelta
    **puesta a propósito** (el sorteo de cinco falsos positivos) para encontrarla y arreglarla.
11. Menores: pares mínimos que no cambiaban una sola cosa (el del futbolista; el de «cambio de
    época», ahora «sinónimo»); el par de control del `TODO 5` que cambiaba dos cosas; el cociente
    «×1,89» (ahora diferencia en puntos); «Diez clases en cinco viñetas» (van nueve); la afirmación
    como hecho de que un transformer aprendería el mismo atajo; «desempeño perfecto y validez
    nula»; la reponderación del muestreo estratificado; `lopezobrador_` faltaba en la lista de
    nombres propios de la ablación (ahora son 19); la métrica rota `proporcion_realmente_politica`
    y las secciones sin uso `etiqueta_circular` y `fuga_por_fuente` salieron de
    `medir-clase10.py`.

### Calendario

12. **«El lunes»** en la última clase: el bloque se llama ahora *en tu investigación* (slide 38,
    notebook, notas, comentario de la viz 3) y habla de «después del curso»; la slide 34 dice «lo
    usan en su próximo paper».
13. **El cuestionario** declara los dos usos: 15 minutos en el aula (ítems 1, 2, 4 y 5) o
    integrador final de unos 50 minutos. Como es la última clase, no es una tarea para la próxima.

### Viz y accesibilidad

14. Portapapeles: `navigator.clipboard.writeText` devuelve una promesa y el `try/catch` no
    atajaba el rechazo (decía «Copiada» aunque fallara). Ahora usa `.then/.catch` (viz 2 y 3).
15. Viz 3: lo que escribe el usuario se escapa antes de ir a `innerHTML` (probado: un
    `<img onerror>` queda como texto). El ejemplo precargado usa las versiones exactas del JSON
    en vez de «scikit-learn 1.x» y «Python 3.11», y el modo revisor distingue las respuestas que
    dicen «0» / «no» como **limitación declarada** en vez de mostrar «Ningún hueco».
16. Viz 2: el tokenizador incluye el guion bajo, como scikit-learn (`lopezobrador_`).
17. Viz 1, caso 3: cada barra lleva su lectura; antes el formato la adivinaba por el valor.
18. **Accesibilidad:** los dos canvas llevan `role="img"` y un `aria-label` que se actualiza con
    lo que dibujan. Lo que antes se codificaba sólo por color ahora tiene además una marca: ★ en
    los nombres propios (viz 1, slide 4, figura 02, con rayado), «(?)» en las palabras que el
    modelo no conoce (viz 2, figura 05, con rayado), y línea llena/punteada en los pares mínimos
    (figura 04).
19. Las slides ya no cargan KaTeX (no hay fórmulas).

---

## 3. Los números, verificados contra la corrida

Todos salen de `medir-clase10.py` y del notebook, en la corrida del 2026-09-29.

- Panel del gancho: `0,83 / 0,73 / 0,64 / 0,68`, piso `0,72`, ganancia `+0,11`, `1471` notas,
  `368` de test, `1103` de train, vocabulario `6.534`. Top 16 de la slide 4 (5 nombres propios);
  6 de 20 en el top completo.
- Control positivo: `824` oraciones de los 123 discursos (120 tienen alguna del largo pedido),
  marca `0,225` → «22 %»; referencia del mismo largo `0,493` (136 oraciones); sin nombres
  propios: F1 `0,667`, control `0,320`, oraciones propias `0,551`.
- Ruido: F1 `0,680 ± 0,026` (25 particiones), de `0,626` a `0,733`. Ablación con una partición:
  `+0,007 / +0,033 / +0,003 / −0,014`. Pareada (media, IC): `−0,002 [−0,015; +0,012]`,
  `−0,010 [−0,035; +0,014]`, `−0,030 [−0,054; −0,006]`, `−0,014 [−0,030; +0,001]`; desvíos de la
  diferencia `0,011` a `0,020`; factor de corrección `0,611`.
- Placebo `7 de 65`; invariancia `100 %`; Aguasclaras `19 %` marcado, `48 %` con vocabulario
  legislativo; prevalencia `28,0 %` real contra `24,7 %` contando.
- Pares mínimos: `0,800/0,759`, `0,773/0,516`, `0,542/0,370`, `0,546/0,392`, `0,713/0,317`,
  `0,853/0,736`. `TODO 5` precargado: `+0,122`, `+0,092`, `−0,158`.
- Sesgo: `0,346 … 0,183` (diferencia `0,163`), los cuatro `0,265`, «las»/«los» sin sustantivo
  `0,307`/`0,265`, pesos `−0,339` y `−0,1355`, artículo `+0,204` en logit, 6 de 10 pares sólo
  artículo, p exacto `0,0020`. Viz 2: género `0,346`/`0,257`, origen `0,344`/`0,183`.

**El código de las slides es el del notebook:** las líneas del control positivo (slide 15) y la
llamada a `bloque_de_reproducibilidad` (slide 27) están copiadas de las celdas correspondientes.

---

## 4. Cómo reproducir esta verificación

```bash
# en una COPIA del repo, no en el repo
export PYTHONDONTWRITEBYTECODE=1
cd clases/10-criterio-validacion-y-etica
python -c "import nbformat; nbformat.validate(nbformat.read('notebook.ipynb', as_version=4))"
python -m jupyter nbconvert --to notebook --execute --output /tmp/out.ipynb notebook.ipynb
md5 -q datos-clase10.json datos-clase10.js pesos-clase10.js figuras/*.png > /tmp/a.md5
python medir-clase10.py && python exportar-figuras.py
md5 -q datos-clase10.json datos-clase10.js pesos-clase10.js figuras/*.png | diff - /tmp/a.md5
```

El `diff` vacío vale **en la misma máquina y con las mismas versiones**. En otro entorno,
compará los números impresos (y las figuras a ojo), no los bytes.

---

## 5. Lo que queda abierto

| # | Qué | Para quién | ¿Frena la clase? |
|---|---|---|---|
| 1 | **El juicio dura 20 minutos, no los 25 de `PROGRAMA.md`.** Desviación deliberada; `notas-docente.md` §5 dice cómo devolverlos. | quien dé la clase | no |
| 2 | **Nadie lo probó con estudiantes.** El reparto de 120 minutos es una estimación. En particular, el práctico 1 (secciones 1-9 en 20 minutos) es ajustado: lo realista es llegar al `TODO 5`. | quien dé la clase | no |
| 3 | Las marcas **`[VERIFICAR URL]`** de `referencias.md` (ahora 11, con Nadeau y Bengio 2003). Las citas están completas; faltan los enlaces abiertos. | quien tenga red | no |
| 4 | La **licencia de los dos corpus de discursos** sigue sin declarar. Dicho en `referencias.md` y en las notas. | el docente | no |
| 5 | Fuera de esta carpeta todavía se citan los números viejos del control positivo («600 fragmentos», «21 de cada 100»): `PROGRAMA.md` (gancho de la clase 10), `recursos/glosario.md` (*shortcut learning*) y la espec de la clase 10. `PROGRAMA.md` §3.4 habla de «cinco preguntas mínimas»; el cuestionario ahora propone cuatro para los 15 minutos. | quien mantenga esos archivos | no |
| 6 | La verificación en navegador de esta ronda fue con Chrome *headless* y un script propio, no con la batería completa de la primera pasada (Playwright con red bloqueada, 44 capturas). No se probó en Colab. | quien tenga tiempo | no |
| 7 | `material-el-juicio.md` **nunca se usó en un aula**. | quien dé la clase | no |
| 8 | Con otra versión de scikit-learn los números pueden moverse en el tercer decimal. Las slides citan la corrida de referencia; `notas-docente.md` §8 pide proyectar la propia. | quien dé la clase | no |

---

## 6. Los archivos de la clase

```
clases/10-criterio-validacion-y-etica/
  slides.html                 40 slides
  notebook.ipynb              63 celdas · 0 errores · 5 figuras · ~12 s · sin salidas
  viz/validez-de-constructo.html   3 casos × 2 vistas (caso 1: control positivo + ablación pareada)
  viz/sesgo-en-el-espejo.html      4 dimensiones + plantilla editable + tabla markdown
  viz/checklist-revisor.html       22 preguntas · 13 fatales · limitaciones declaradas
  notas-docente.md            plan de 120 min + qué recortar
  cuestionario.md · cuestionario-soluciones.md      12 ítems (15 min: 1, 2, 4, 5)
  referencias.md              11 lecturas · 4 URLs verificadas
  material-el-juicio.md       los dos papers del práctico 2 (ficticios, rotulados)
  medir-clase10.py            de acá sale cada número de las slides y las viz
  exportar-figuras.py         corre el notebook y guarda sus 5 figuras
  datos-clase10.json · datos-clase10.js · pesos-clase10.js
  figuras/                    5 PNG + README
  VERIFICACION.md             este archivo
```
