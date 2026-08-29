# Cuestionario — Clase 5

**La forma de los datos manda (I): imágenes**

Doce preguntas. Las de opción múltiple tienen **una** respuesta correcta.
Las abiertas se responden en tres o cuatro oraciones: no se busca extensión, se busca criterio.

Podés tener el notebook abierto. De hecho, para algunas conviene.

---

### 1. (opción múltiple)

¿Qué supuesto sobre el mundo incorpora una CNN que una red densa **no** tiene?

- **A.** Que hay más datos de entrenamiento disponibles.
- **B.** Que los valores de entrada están entre 0 y 1.
- **C.** Que los datos tienen una vecindad: lo que está cerca se relaciona, y un patrón vale
  igual en cualquier posición.
- **D.** Que la relación entre entrada y salida es no lineal.

---

### 2. (opción múltiple)

En una CNN, **un filtro (o *kernel*)** es:

- **A.** La imagen de salida que muestra qué detectó la capa.
- **B.** Un pequeño conjunto de números —por ejemplo nueve, en un filtro de 3×3— que se
  multiplican por cada pedacito de la imagen y se suman.
- **C.** Una función que descarta los píxeles poco importantes.
- **D.** La capa que decide a qué clase pertenece la imagen.

---

### 3. (qué pasa si…)

Tomás las 12.000 imágenes de entrenamiento y las 4.000 de prueba y le aplicás a **todas** la
**misma** permutación de los 784 píxeles. Reentrenás desde cero.

**a)** ¿Qué le pasa a la exactitud de la red densa? ¿Por qué?
**b)** ¿Qué le pasa a la de la CNN? ¿Por qué la diferencia?
**c)** ¿Qué pasaría si en vez de una permutación fija usaras **una permutación distinta para
cada imagen**? (Esta parte no la corrimos en clase: pensala.)

---

### 4. (qué pasa si…)

Entrenás una CNN con fotos donde el objeto está siempre centrado, y después la aplicás a fotos
donde el objeto está en una esquina.

**a)** ¿Anda? ¿Por qué?
**b)** ¿Y si las fotos de prueba están rotadas 90°? ¿Cambia la respuesta? Justificá en términos
de qué supone y qué **no** supone la arquitectura.

---

### 5. (leer una figura)

Cuatro filtros de 3×3 y cuatro mapas de activación. Emparejá cada filtro con su mapa.

```
FILTRO A            FILTRO B            FILTRO C            FILTRO D
 1   0  -1          1   2   1          0.11 0.11 0.11      0   0   0
 2   0  -2          0   0   0          0.11 0.11 0.11      0   1   0
 1   0  -1         -1  -2  -1          0.11 0.11 0.11      0   0   0
```

```
MAPA 1: la imagen sale igual que la original.
MAPA 2: se encienden los contornos horizontales (el borde de arriba y el de abajo del objeto).
MAPA 3: la imagen sale borroneada, sin detalles finos.
MAPA 4: se encienden los contornos verticales (los costados del objeto).
```

Escribí los cuatro pares y, en una oración, **cómo te diste cuenta** en cada caso.

---

### 6. (cuenta)

**a)** ¿Cuántos parámetros tiene una capa convolucional con **16 filtros de 3×3** sobre una
imagen en escala de grises, contando los sesgos (un sesgo por filtro)?

**b)** ¿Cuántos tiene una capa densa que va de 784 entradas a 16 salidas, contando sesgos?

**c)** ¿Cuántas veces más grande es la segunda? ¿Y por qué la primera puede alcanzar igual?

---

### 7. (opción múltiple)

¿Por qué las capas profundas de una CNN detectan cosas más complejas que las primeras?

- **A.** Porque tienen filtros más grandes.
- **B.** Porque tienen más parámetros.
- **C.** Porque no miran la imagen: miran los mapas de activación de la capa anterior, así que
  cada nivel **combina** las piezas del nivel de abajo.
- **D.** Porque se entrenan durante más épocas.

---

### 8. (aplicación)

Tenés una base de encuesta con 60 columnas (edad, ingreso, provincia, nivel educativo, respuestas
a 40 ítems de una escala…) y 3.000 casos. Alguien te sugiere usar una CNN «porque es lo más
moderno».

Justificá tu respuesta **en términos de supuestos**, no de moda. ¿Qué estaría afirmando esa CNN
sobre tus datos? ¿Es cierto? ¿Qué probarías en su lugar?

---

### 9. (aplicación)

Querés clasificar 5.000 fotos de un archivo histórico en tres categorías (acto partidario /
movilización / retrato oficial).

Enumerá **lo mínimo** que necesitás tener resuelto **antes** de escribir una línea de código, y
explicá por qué cada cosa es imprescindible.

---

### 10. (lectura crítica)

> Un estudio predice el nivel de consumo de los hogares a partir de imágenes satelitales diurnas
> en un país africano, usando luminosidad nocturna como señal intermedia. Reporta R² = 0,75
> contra los datos de una encuesta de hogares. Los autores concluyen que el método permite
> «producir estimaciones de pobreza en regiones sin datos de encuesta».

Escribí **las tres preguntas de la clase** aplicadas a este caso, y para cada una **la duda
concreta** que te queda con lo que dice el resumen.

---

### 11. (criterio / ética aplicada)

Una ONG propone usar imágenes satelitales y un modelo como el de la pregunta 10 para **decidir a
qué zonas mandar ayuda social**, en regiones donde no hay encuestas recientes.

Mencioná **dos riesgos concretos** y **una salvaguarda** que exigirías antes de que el sistema se
implemente. No alcanza con «puede tener sesgo»: decí *qué* sesgo, *a quién* perjudicaría y *cómo*
lo detectarías.

---

### 12. (criterio, sobre tu propia investigación)

Pensá en los datos con los que trabajás vos.

**a)** ¿Tienen alguna forma —espacio, tiempo, secuencia, red, jerarquía— o son una tabla de casos
por variables?
**b)** Escribí **una** afirmación sobre el mundo que estarías haciendo si eligieras un modelo que
supone esa forma.
**c)** ¿Cómo comprobarías si esa afirmación es cierta en tu caso? Pensá una prueba concreta,
del estilo de la que hicimos hoy con el barajado.

*(Esta pregunta no tiene una respuesta correcta. Tiene respuestas honestas y respuestas
apuradas.)*
