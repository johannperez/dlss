# Clase 6 — Cuestionario

**La forma de los datos manda: texto, secuencias y embeddings**

Doce preguntas. Las de opción múltiple tienen **una sola** respuesta correcta.
Las abiertas se contestan en dos o tres oraciones: no buscamos extensión, buscamos criterio.

Podés mirar el notebook, las slides y las visualizaciones. No es un examen de memoria.

---

## 1. Qué es un token *(opción múltiple)*

Un **token** (ficha) es:

- **A.** Una palabra del texto, siempre.
- **B.** Cada uno de los pedacitos en que se parte el texto, que a veces coincide con
  una palabra y a veces no.
- **C.** Un número entre 0 y 1 que mide la importancia de una palabra.
- **D.** Una palabra que el modelo no conoce.

---

## 2. El problema del one-hot *(opción múltiple)*

¿Cuál es el **problema principal** de representar cada palabra con un vector one-hot?

- **A.** Ocupa demasiada memoria.
- **B.** Los números no son enteros y eso complica el entrenamiento.
- **C.** Todas las palabras quedan exactamente igual de lejos entre sí: no hay
  ninguna noción de parecido.
- **D.** No sirve para textos largos.

---

## 3. Qué captura un embedding *(opción múltiple)*

Cuando decimos que dos palabras están **cerca** en un espacio de embeddings, lo que
sabemos es que:

- **A.** Significan aproximadamente lo mismo, como en un diccionario de sinónimos.
- **B.** Aparecen en contextos parecidos dentro del corpus con el que se entrenó.
- **C.** Aparecen la misma cantidad de veces en el corpus.
- **D.** Pertenecen a la misma categoría gramatical.

---

## 4. Qué pasa si… cambiás de corpus

Entrenás embeddings sobre discursos parlamentarios de **1950** y, por separado, sobre
discursos de **2020**.

**(a)** ¿Esperás que la palabra `familia` tenga los mismos vecinos en los dos?
**(b)** Si no, ¿qué estarías **midiendo** con esa diferencia? Nombrá el fenómeno.
**(c)** Mencioná **un** motivo por el que la diferencia que ves podría *no* ser el
fenómeno que creés que es.

---

## 5. Qué pasa si… tu corpus es chico

Tu corpus son **200 notas de prensa** de 400 palabras cada una (80.000 palabras en total).
Querés entrenar embeddings propios como hicimos hoy.

**(a)** ¿Qué problema concreto vas a tener? Dalo en términos de lo que viste en clase.
**(b)** ¿Qué alternativa tenés?

---

## 6. Leer un gráfico

Esta es la proyección 2D de un espacio de embeddings entrenado sobre debates
parlamentarios. Se ven cuatro grupos:

```
        dimensión 2
            │
   escuela  │              inflación
   docentes │              precios      dólar
   alumnos  │   OBRA         déficit
   maestros │  PÚBLICA
  ──────────┼──────────────────────────────  dimensión 1
   senadores│
   diputados│    hospital   médicos
   cámara   │    salud      enfermeras
   sesión   │
```

**(a)** Nombrá los cuatro grupos en una palabra cada uno.
**(b)** Hay una palabra mal ubicada. ¿Cuál es y en qué grupo esperarías encontrarla?
**(c)** Proponé **una hipótesis** de por qué el modelo la puso ahí.
**(d)** El pie del gráfico dice *«estas 2 dimensiones muestran el 15 % de la
variación»*. ¿Qué recaudo te obliga a tomar ese número al interpretar el dibujo?

---

## 7. Leer una salida de código

Corriste esto en tu propio corpus:

```
>>> datos.vecinos("protesta", V, palabras, k=6)
[('marcha', 0.71), ('movilización', 0.68), ('de', 0.66),
 ('reclamo', 0.64), ('represión', 0.61), ('la', 0.59)]
```

**(a)** ¿Qué hacen ahí `de` y `la`? ¿Es un error del código?
**(b)** ¿Qué harías al respecto, y qué tenés que declarar en tu paper si lo hacés?
**(c)** `represión` aparece como vecina de `protesta`. ¿Qué **no** podés concluir de eso?

---

## 8. Los antónimos

En el corpus de discursos de apertura, la similitud coseno entre `importaciones` y
`exportaciones` es **0,78**, y entre `público` y `privado` es **0,67**. Son de las más
altas de todo el vocabulario.

**(a)** ¿Por qué quedan tan cerca dos palabras que significan lo contrario?
**(b)** Un colega quiere usar la similitud coseno entre dos discursos como medida de
**acuerdo político**. ¿Qué le decís? Una oración.

---

## 9. Aplicación en cuatro pasos

Querés medir si el discurso público sobre **inmigración** se volvió más *securitario*
entre 2000 y 2020. Tenés un corpus de notas de prensa de esos veinte años.

Describí en **cuatro pasos** cómo lo harías con lo que viste hoy. Para cada paso, decí
qué decisión estás tomando y por qué alguien podría discutirla.

---

## 10. La RNN *(opción múltiple)*

¿Por qué una RNN tiene problemas con dependencias largas (por ejemplo, un sujeto que
está a treinta palabras del verbo)?

- **A.** Porque no tiene suficientes parámetros.
- **B.** Porque arrastra un estado de tamaño fijo que se va sobrescribiendo con cada
  palabra nueva, y la información vieja se degrada.
- **C.** Porque promedia los vectores de todas las palabras de la oración, y un
  promedio no tiene orden.
- **D.** Porque las palabras lejanas suelen quedar fuera de su vocabulario y se pierden.

---

## 11. Lo que pierde el promedio

Promediar los embeddings de las palabras de una frase da un vector para la frase entera.

**(a)** ¿Qué información se pierde en ese promedio?
**(b)** ¿Por qué esa información le importa específicamente a un cientista social?
Dá **un ejemplo de tu propia área** donde perderla te arruinaría el resultado.

---

## 12. Criterio y ética aplicada

Una empresa usa embeddings entrenados sobre currículums para ordenar candidatos. Alguien
descubre que, en ese espacio, ciertas ocupaciones caen sistemáticamente más cerca de
nombres masculinos que de femeninos.

**(a)** ¿De dónde viene ese sesgo? Sé preciso: ¿del algoritmo, de los datos, de las dos
cosas?
**(b)** ¿Alcanza con quitarle a los currículums el nombre y el género explícito?
Justificá.
**(c)** ¿Cambia tu respuesta si el objetivo, en vez de ordenar candidatos, fuera
**estudiar la segregación ocupacional por género** en un mercado de trabajo?
Explicá por qué sí o por qué no.
