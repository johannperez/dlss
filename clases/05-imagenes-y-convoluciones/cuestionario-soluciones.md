# Cuestionario — Clase 5 · Soluciones comentadas

**Para quien corrige.** No alcanza con marcar la correcta: lo útil es saber **qué confusión
revela cada distractor**, porque esa confusión reaparece en las clases 6, 7 y 10. Cada ítem trae
la respuesta, por qué cada opción incorrecta es tentadora, y qué hacer con quien la eligió.

Los números que se citan son los de la corrida real de la clase
(`medir-experimentos.py`, semilla 1983): densa 85,8 % / barajada 85,6 %; CNN 87,8 % / barajada
83,2 %; con la foto corrida 3 píxeles, densa 32,3 % y CNN 74,1 %.

---

### 1. Correcta: **C**

Que los datos tienen vecindad y que un patrón vale igual en cualquier posición: localidad e
invariancia traslacional.

- **A («más datos disponibles»)** confunde un supuesto sobre *el mundo* con una condición sobre
  *el dataset*. Es tentadora porque en clase se dijo que la CNN «necesita menos datos» — pero eso
  es una **consecuencia** del supuesto, no el supuesto. Quien elige A todavía no separa
  «qué afirma la arquitectura» de «qué le conviene al entrenamiento».
- **B («entre 0 y 1»)** es normalización: plomería, no teoría. Aparece porque en el notebook
  dividimos por 255. Buena ocasión para repetir la distinción entre *preprocesamiento* y
  *arquitectura*.
- **D («no lineal»)** es tentadora y **es cierta de las dos**: la red densa de la clase 4 también
  tiene ReLU. No distingue a la CNN de nada. Quien elige D está contestando «qué tiene de
  especial una red neuronal», no «qué tiene de especial una CNN».

---

### 2. Correcta: **B**

El filtro son los números. El pincel.

- **A («la imagen de salida»)** es **el error del año** y hay que corregirlo en voz alta: eso es
  el **mapa de activación**, el cuadro, no el pincel. Si más de un cuarto del curso elige A,
  volvé a proyectar la viz `kernel-deslizante.html` y señalá los paneles 2 y 3 con el dedo
  mientras nombrás cada uno. Esta confusión no se cura leyendo, se cura señalando.
- **C («descarta píxeles poco importantes»)** describe vagamente el *pooling* y además le mete
  intención al filtro. Ojo con esa palabra: el filtro no «decide» nada, multiplica y suma.
- **D («la capa que decide la clase»)** es la capa densa del final. Quien elige D mezcló las dos
  mitades de la arquitectura: la convolucional **extrae**, la densa **decide**.

---

### 3.

**a) La red densa queda prácticamente igual: 85,8 % → 85,6 %.**
La razón: para una capa densa, cada píxel de entrada es una variable con su propio peso, y el
orden en que estén las variables no significa nada. Aplicar siempre la misma permutación equivale
a renombrar las variables; la red aprende los mismos pesos, sólo que en otras posiciones. La
información está intacta —la permutación es reversible— y la densa nunca usó la vecindad, así que
no tiene nada que perder.

**b) La CNN baja: 87,8 % → 83,2 %.**
Baja porque sus filtros de 3×3 miran **vecinos en la grilla**, y después del barajado los nueve
píxeles de una ventana son nueve píxeles cualesquiera de la foto. Esos puntos de caída son,
literalmente, lo que la CNN estaba sacando de la estructura espacial.

*Se acepta —y se valora— que noten que la caída es chica.* La lectura honesta es: lo contundente
no es cuánto pierde la CNN, sino que la densa **no pierde nada**. La prueba más fuerte de que la
CNN usa la grilla es la foto corrida: 32,3 % contra 74,1 %.

**c) Con una permutación distinta por imagen, se caen las dos, y muchísimo.**
Ahí sí se destruye la relación entre posición y contenido: la variable número 30 ya no significa
lo mismo en dos imágenes distintas. Ningún modelo que reciba un vector puede aprender nada
estable. Es la mejor forma de mostrar la diferencia entre *cambiar de nombre a las variables*
(inocuo) y *cambiarles el significado caso por caso* (letal).

> **Qué revela cada error.** Quien contesta que la densa «empeora un poco» no terminó de aceptar
> el resultado y está razonando desde su propia visión (a nosotros el revoltijo nos parece ruido).
> Quien contesta que la CNN «queda igual» confundió cuál es cuál. Quien en (c) contesta «lo mismo
> que en (a)» no entendió que lo que importaba era que la permutación fuera **la misma para todas**.

---

### 4.

**a) Sí, anda razonablemente bien**, y eso es precisamente la invariancia traslacional: los mismos
nueve números recorren toda la imagen, así que un patrón aprendido en el centro se detecta en la
esquina. En nuestra medición, corriendo la foto 3 píxeles la CNN pasó de 87,8 % a 74,1 %, mientras
que la densa se desplomó de 85,8 % a 32,3 %.

**Matiz que hay que premiar:** la CNN **también** baja. La invariancia no es perfecta ni infinita
—el *pooling* y el máximo global la dan de a poco, y si el objeto se sale del encuadre no hay
arquitectura que lo salve—. Es un supuesto que se cumple *hasta cierto punto*, no una garantía.

**b) Con las fotos rotadas 90° la respuesta cambia: la CNN se cae.**
La arquitectura supone que un patrón vale igual **trasladado**, no **rotado**. Un detector de
bordes verticales rotado 90° es un detector de bordes horizontales: es otro filtro. La invariancia
rotacional **no viene gratis**; se compra con datos (*data augmentation*: entrenar con copias
rotadas) o con arquitecturas diseñadas para eso.

> Esta pregunta separa a quien memorizó «la CNN es invariante» de quien entendió **a qué**.
> Quien contesta «anda igual porque es invariante» merece exactamente esta repregunta:
> *«¿invariante a qué, específicamente?»*.

---

### 5. Pares: **A–4, B–2, C–3, D–1**

- **A → mapa 4 (contornos verticales).** Columna izquierda positiva, columna derecha negativa: la
  cuenta da grande donde hay un cambio de claro a oscuro **de izquierda a derecha**, o sea en un
  borde vertical.
- **B → mapa 2 (contornos horizontales).** Es el mismo filtro traspuesto: fila de arriba positiva,
  fila de abajo negativa.
- **C → mapa 3 (borroneada).** Los nueve números son iguales y suman 1: es un promedio de la
  vecindad, y promediar borronea.
- **D → mapa 1 (igual).** Un 1 en el centro y ceros alrededor: se queda con el píxel del medio.
  Es el `TODO 3` del notebook.

**Los dos errores frecuentes:**
1. **Confundir A con B.** Revela que están leyendo el filtro como «tiene positivos y negativos»
   sin mirar *en qué dirección* está el cambio de signo. Se arregla en diez segundos en la viz:
   poner el preset vertical y el horizontal uno detrás del otro.
2. **Emparejar C con el mapa 1** («no hace nada»). Confunden *no cambiar* con *suavizar*. Buena
   ocasión para señalar que los dos filtros suman 1, pero uno concentra todo el peso en el centro
   y el otro lo reparte: **la suma no es lo único que importa, importa la forma**.

---

### 6.

**a) 16 × 9 + 16 = 160 parámetros.** Nueve pesos por filtro, dieciséis filtros, más un sesgo por
filtro.

**b) 784 × 16 + 16 = 12.560 parámetros.**

**c) 78,5 veces más grande.** La convolucional alcanza igual porque **reusa los mismos nueve
números en todas las posiciones de la imagen** (*parameter sharing*): en vez de aprender «qué pasa
en el píxel 342» aprende «qué pasa cuando aparece este patrón», y eso vale en las 784 posiciones.

> **Error típico: olvidarse los sesgos** (144 y 12.544). No es grave y no cambia la conclusión;
> anotalo y seguí. **Error grave: multiplicar por 784 en (a)**, dando 16×9×784. Quien hace eso
> está pensando que hay un filtro distinto por posición, que es exactamente lo contrario del
> supuesto de la clase. Volvé a la slide 12 con esa persona: *los mismos nueve números*.

---

### 7. Correcta: **C**

Porque cada capa mira los mapas de la anterior, no la imagen: los niveles **componen**.

- **A («filtros más grandes»)** es falsa en nuestra red —los tres son de 3×3— pero es tentadora
  porque intuitivamente «para ver más grande hay que mirar más grande». La respuesta elegante:
  el *campo receptivo* crece por apilamiento y por *pooling*, no porque el filtro crezca.
  Si alguien elige A, es un momento perfecto para explicar eso; no es una tontería, es una
  hipótesis razonable.
- **B («más parámetros»)** confunde tamaño con estructura. Es la misma confusión de la clase 4:
  más capacidad no es mejor por sí sola.
- **D («más épocas»)** confunde la arquitectura con el entrenamiento. Todas las capas se entrenan
  a la vez, la misma cantidad de pasos.

---

### 8.

**Respuesta esperada: no, y el argumento es de supuestos.**

Poner una CNN sobre una tabla es afirmar que **la columna 12 es vecina de la columna 13** y que
un patrón que aparece entre las columnas 12-13-14 significa lo mismo si aparece entre las
columnas 40-41-42. En una encuesta eso es **falso**: el orden de las columnas del CSV es
arbitrario, y si las reordenás no cambió nada del mundo. La arquitectura estaría afirmando algo
que sabemos que no es cierto.

Qué probaría en su lugar, en este orden: (1) una regresión o un modelo lineal, que además se
interpreta; (2) **un modelo de árboles** —random forest, gradient boosting—, que para datos
tabulares suele ganarle a una red neuronal con menos datos, menos tiempo y más facilidad para
explicar; (3) recién después, si hace falta, una red densa.

**Matiz que merece nota alta:** que alguien diga *«a menos que las columnas SÍ tengan un orden
con significado —por ejemplo 40 mediciones mensuales de la misma variable, o una escala ordenada—,
en cuyo caso hay una secuencia y ahí sí puede tener sentido una arquitectura que la aproveche»*.
Eso es exactamente el criterio que la clase quiere instalar.

> **Respuesta que hay que corregir:** «no, porque las CNN son para imágenes». Es la conclusión
> correcta por la razón equivocada, y no se transfiere a ningún problema nuevo. Repreguntá:
> *«¿y por qué son para imágenes?»*.

---

### 9.

Lo mínimo, con su porqué:

1. **Etiquetas.** Un conjunto de fotos codificadas a mano —del orden de 100 a 300 por categoría
   para empezar— con un criterio escrito. Sin esto no hay proyecto: no es un detalle de
   implementación, es la definición operativa de tus categorías.
2. **Un criterio de codificación explícito, y ojalá dos codificadores.** ¿Un acto partidario al
   aire libre con mucha gente es «acto» o «movilización»? Si dos personas no coinciden, el modelo
   tampoco va a poder, y la culpa no va a ser del modelo.
3. **Una partición honesta, decidida antes.** Si las fotos vienen de distintos fondos, fotógrafos,
   décadas o diarios, hay que partir **por ahí** y no al azar (clase 4): fotos del mismo rollo en
   train y test es fuga.
4. **Un baseline.** ¿Qué acierta la regla trivial «siempre la clase más frecuente»? Si tus clases
   están 70/20/10, un modelo del 72 % no es una noticia.
5. **Saber qué error te importa más.** No es lo mismo perderte movilizaciones (falsos negativos)
   que inflar el conteo (falsos positivos), y eso depende de tu pregunta, no de la métrica.

> Se acepta que no aparezca (5). **Si no aparecen (1) y (3), la respuesta está incompleta**, y
> conviene devolverla: son las dos cosas que hunden proyectos reales.

---

### 10.

**Pregunta 1 — ¿Qué está midiendo realmente?**
No mide pobreza: mide **lo que se ve desde arriba y correlaciona con pobreza en ese país**:
material de los techos, densidad y regularidad de la construcción, presencia de caminos
pavimentados, tipo de cultivo, y —vía la señal intermedia— cuánta luz eléctrica hay de noche.
La duda concreta: **el resumen no dice qué está midiendo**, y sin eso no se puede saber en qué
condiciones se rompe. Es exactamente el problema del `TODO 5` del notebook, donde el modelo
aprendió «muchas manchitas chiquitas» en vez de «gente».

**Pregunta 2 — ¿Valen acá los supuestos de la arquitectura?**
La invariancia traslacional sí: un techo de chapa es un techo de chapa esté en cualquier parte de
la imagen. La invariancia de **escala** y de **región** no vienen de regalo: si el norte y el sur
del país se ven distinto por razones climáticas o de tipo de vivienda que no son las que interesan,
el modelo puede estar leyendo geografía y no pobreza. La duda concreta: **¿el R² se calculó sobre
regiones que el modelo no vio, o sobre regiones parecidas a las de entrenamiento?**

**Pregunta 3 — ¿Qué pasa fuera de donde se entrenó?**
La duda concreta: **¿la partición fue geográfica?** Un R² alto con una partición al azar de
puntos vecinos es casi seguro optimista, porque los vecinos se parecen (es fuga espacial: la
versión geográfica de 2005/2006 de la clase 4). Y transferir el modelo a otro país es una apuesta
mucho más fuerte todavía.

> **Cómo se corrige.** Se busca que las tres preguntas estén y que cada una venga con una duda
> **concreta y verificable**, no con una queja general. «Puede tener sesgo» no cuenta.
> «¿La partición fue geográfica o al azar?» sí. Premiá la especificidad.
>
> **Respuesta a desactivar:** el rechazo global («esto no sirve, la pobreza es multidimensional»).
> El punto de la clase no es descartar: es **saber qué preguntar**. Un R² de 0,75 en una región sin
> ninguna encuesta puede ser muchísimo mejor que no tener nada, siempre que se diga qué es.

---

### 11.

**Riesgos concretos (dos, cualesquiera de estos):**

- **El proxy se rompe donde más importa.** El modelo aprendió a leer techos y construcción en las
  regiones donde había encuestas para entrenar. En una región con otro tipo de vivienda —adobe,
  vivienda dispersa, otra forma de asentamiento— puede subestimar sistemáticamente la pobreza y
  dejar sin ayuda justo a la población más distinta de la de entrenamiento.
- **Los errores no se reparten al azar.** Se concentran en subgrupos: zonas rurales dispersas,
  poblaciones móviles, asentamientos bajo cobertura vegetal densa, regiones con nubosidad
  frecuente en las imágenes. Son grupos ya desfavorecidos: el error del modelo **refuerza** la
  desigualdad que dice medir.
- **Incentivo perverso y falta de recurso.** Si la asignación depende del modelo, aparece la
  presión por «verse pobre desde arriba», y sobre todo: **una persona mal clasificada no tiene a
  quién reclamarle**, porque no hay una regla escrita que se pueda discutir.
- **Congelamiento temporal.** El modelo se entrenó con imágenes de un momento; una crisis, una
  inundación o una migración reciente no aparecen hasta que alguien reentrene.

**Salvaguardas aceptables (una alcanza, bien argumentada):**

- **Validación en terreno en la región donde se va a aplicar**, antes de aplicar: una muestra de
  hogares visitados de verdad, y reportar el desempeño **por subgrupo**, no sólo el global.
- **Mecanismo de apelación humana**: una vía para que una comunidad mal clasificada pida revisión,
  con alguien obligado a responder. Un sistema que asigna recursos sin recurso no es aceptable,
  ande bien o ande mal.
- **Uso como complemento y no como reemplazo**: el modelo prioriza dónde ir a medir, y la
  asignación final la decide la medición.

> **Cómo se corrige.** Se busca **especificidad**: qué sesgo, a quién perjudica, cómo se
> detectaría. «Puede discriminar» sin nombrar a quién es media respuesta.
> **También se corrige el otro extremo:** quien contesta «no se debe usar nunca» tiene que decir
> qué propone en cambio en una región donde la alternativa real es no tener ningún dato.
> El curso no busca tecnófilos ni tecnófobos: busca gente que sepa qué exigir.

---

### 12.

No tiene respuesta correcta. **Sí tiene un criterio de corrección**, y son tres cosas:

1. **En (a), que la descripción de la forma sea concreta.** «Datos de panel: mismos municipios,
   diez años» es una forma. «Datos sociales» no es nada.
2. **En (b), que la afirmación esté escrita como afirmación sobre el mundo**, no como
   especificación técnica. Bien: *«estoy afirmando que lo que pasó el año pasado importa más que
   lo que pasó hace ocho»*. Mal: *«uso una RNN»*.
3. **En (c), que la prueba sea del mismo tipo que la del barajado**: romper deliberadamente la
   estructura supuesta y ver si el modelo se entera. Ejemplos que aparecen y funcionan:
   barajar el orden temporal de las observaciones de cada unidad; reordenar las columnas;
   permutar las etiquetas de los grupos; entrenar en una región y evaluar en otra.

> **La respuesta que más se repite y que hay que devolver:** «mis datos son una tabla, así que
> esto no me sirve». Media respuesta. Falta el (b): la tabla también tiene supuestos —que las
> filas son independientes, que las variables son intercambiables, que un caso es un caso—, y
> algunos son falsos (¡datos de panel!). La pregunta no es si tus datos tienen *esta* forma:
> es si tenés claro **qué forma les estás atribuyendo**.
