# Cuestionario — Clase 8

**Un mini-GPT propio, y la traducción a ChatGPT**

> Doce preguntas. No es un examen: es una manera de darte cuenta de qué se te acomodó y
> qué no. Contestá sin volver a las slides, y recién después mirá las soluciones.
> Las abiertas se responden en tres o cuatro líneas. Las dos últimas son de criterio y
> son las que más importan: si sólo vas a hacer dos, hacé esas.

---

### 1. [múltiple choice] ¿Cuál es el objetivo de entrenamiento de un modelo de lenguaje?

- **A)** Aprender la definición de cada palabra a partir de un diccionario grande.
- **B)** Para cada posición del texto, ponerle una probabilidad a cada ficha posible de
  ser la que sigue, y que esa probabilidad sea alta para la que efectivamente venía.
- **C)** Comprimir el corpus de entrenamiento para poder recuperarlo después.
- **D)** Clasificar cada oración según su tema, y aprender a relacionar los temas.

---

### 2. [múltiple choice] ¿Por qué alucina un LLM?

- **A)** Porque le faltan datos sobre ese tema en particular. Con un corpus más grande
  dejaría de hacerlo.
- **B)** Porque hay un error en el código de generación que todavía no se resolvió.
- **C)** Porque su salida es **siempre** una distribución de probabilidad sobre la
  próxima ficha, no tiene un mecanismo que verifique verdad, y nada adentro detecta que
  no sabe: entonces produce la continuación más plausible, exista o no.
- **D)** Porque la temperatura está demasiado alta y sortea opciones improbables.

---

### 3. [qué pasa si] Ponés temperatura 0

Un colega te dice: «puse temperatura 0 así el modelo es más preciso y sabe más».

**a)** ¿Qué cambia efectivamente en el texto generado?
**b)** ¿Qué **no** cambia respecto de lo que el modelo sabe?
**c)** Nombrá una cosa que **mejora** y una que **empeora** al poner T=0.

---

### 4. [qué pasa si] El prompt de 10.000 palabras

Escribiste un prompt de 10.000 palabras: al principio pusiste las instrucciones de
codificación (tu libro de códigos) y al final pegaste los 200 titulares a clasificar.
La ventana de contexto del modelo es de 4.000 fichas.

**a)** ¿Qué pasa con las instrucciones del principio? (Puede depender de la
herramienta: pensá qué opciones hay.)
**b)** ¿El modelo «se olvidó» de ellas? Explicá con precisión qué pasó.
**c)** ¿Cómo lo mitigarías, sin cambiar de modelo?

---

### 5. [leer un gráfico] Dos distribuciones

El mismo modelo, el mismo prompt, dos temperaturas distintas. Estas son las cinco fichas
más probables en cada caso:

| ficha | distribución **A** | distribución **B** |
|---|---|---|
| «s» | 0,891 | 0,586 |
| «y» | 0,095 | 0,180 |
| «l» | 0,007 | 0,045 |
| «p» | 0,003 | 0,027 |
| «c» | 0,001 | 0,017 |
| *las otras 66 juntas* | 0,003 | 0,144 |

**a)** ¿Cuál corresponde a la temperatura más alta?
**b)** ¿Qué tipo de texto va a producir cada una?
**c)** Mirando las dos columnas: ¿en qué se parecen? ¿Qué te dice ese parecido sobre lo
que la temperatura **no** hace?

---

### 6. [leer un gráfico] Una curva de loss

Un compañero entrenó el mismo mini-GPT pero con un corpus **cuarenta veces más chico**
(25 KB en vez de 1,1 MB). Éstas son sus curvas:

| paso | loss de train | loss de validación |
|---|---|---|
| 100 | 2,21 | 2,25 |
| 300 | 0,56 | 1,01 |
| 500 | 0,17 | 0,80 |
| 700 | 0,12 | 0,75 |
| 900 | 0,12 | **0,70** |
| 1200 | 0,10 | 0,79 |

Para comparar: con el corpus entero, al paso 1200 la loss de train fue **0,185** y la de
validación **0,186**.

**a)** ¿Qué está pasando? Ponele el nombre que aprendiste en la clase 4.
**b)** ¿En qué paso, más o menos, habrías frenado?
**c)** Nombrá dos maneras distintas de arreglarlo.
**d)** Si sólo te hubieran mostrado la columna de train, ¿qué habrías concluido?

---

### 7. [mecanismo] Explicá con tus palabras por qué un LLM cuenta mal las letras

Tres o cuatro líneas. Tiene que aparecer la palabra **ficha** (o *token*).
Y una segunda parte: ¿por qué a veces **acierta**?

---

### 8. [mecanismo] El mismo prompt, dos respuestas distintas

**a)** ¿Por qué el mismo prompt puede dar dos respuestas distintas?
**b)** ¿Cómo lo evitarías si necesitás reproducibilidad para un paper?
**c)** ¿Por qué eso **no alcanza del todo**? Nombrá al menos una razón.

---

### 9. [distinción] Tu mini-GPT y ChatGPT

Nombrá **tres** diferencias entre el modelo de 1.541.056 parámetros que entrenaste y un
modelo como ChatGPT.

**a)** Las tres diferencias.
**b)** ¿Cuál de ellas es la que lo convierte en **asistente** y no en
**autocompletador**?
**c)** Nombrá **dos** propiedades del mini-GPT que ChatGPT sigue teniendo igual.

---

### 10. [aplicación] Clasificar 3.000 titulares

Querés usar un LLM para clasificar 3.000 titulares de prensa según si mencionan protesta
social. Describí el **procedimiento mínimo aceptable** para que el resultado sea
publicable en una revista con referato.

Escribilo como una lista de pasos, no como un párrafo. Pensá qué te pediría un revisor.

---

### 11. [criterio] Las diez referencias

Un colega te dice, contento, que le pidió a ChatGPT las diez referencias principales
sobre su tema y que las va a citar en el paper que está por mandar.

Escribí lo que le decís. **Tiene que incluir el mecanismo**, no sólo la recomendación:
explicale *por qué* pasa lo que pasa, en términos de lo que viste hoy. Y decile también
qué **sí** puede hacer con esa lista.

---

### 12. [criterio / revisión de pares] Sos revisor

Una revista te manda a revisar un paper. En la sección de métodos dice, textualmente:

> *«Clasificamos 5.000 documentos con GPT-4, obteniendo una tasa de acuerdo del 91% con
> nuestras expectativas teóricas.»*

No reporta el prompt, ni la versión exacta del modelo, ni la fecha, ni la temperatura, ni
ninguna validación humana independiente.

Escribí tu comentario de revisor (unas 10 líneas):

**a)** Qué falta, punto por punto.
**b)** **Por qué importa cada cosa** — un revisor que sólo pide cosas sin explicar por
qué no ayuda a nadie.
**c)** Qué le pedirías **como mínimo** para poder evaluar el trabajo.
**d)** Y la trampa: hay una frase en esa cita de métodos que es un problema aparte, más
grave que todo lo anterior. ¿Cuál es y por qué?
