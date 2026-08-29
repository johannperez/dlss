# Cuestionario — Clase 7

**Attention: cada palabra arma su propio resumen del contexto**

> Once preguntas. No es un examen: es una manera de darte cuenta de qué se te acomodó y
> qué no. Contestá sin volver a las slides, y recién después mirá las soluciones.
> Las abiertas se responden en tres o cuatro líneas: si te sale un párrafo largo,
> probablemente todavía no está claro.

---

### 1. [múltiple choice] ¿Qué hace el mecanismo de attention?

- **A)** Recorre la oración palabra por palabra y va guardando en una memoria lo más
  importante de lo que leyó hasta ahí.
- **B)** Para cada palabra, calcula un peso hacia cada una de las otras y arma un promedio
  ponderado del contexto con esos pesos.
- **C)** Busca en un diccionario interno el significado de cada palabra y lo reemplaza por
  su definición.
- **D)** Compara la oración con todas las oraciones del corpus de entrenamiento y devuelve
  la más parecida.

---

### 2. [múltiple choice] ¿Cuál es la diferencia entre *query*, *key* y *value*?

- **A)** Son tres entradas distintas que hay que darle al modelo: el texto, el
  vocabulario y las etiquetas.
- **B)** Son tres transformaciones del **mismo** vector de entrada: lo que la palabra
  busca, el aviso que publica, y lo que aporta cuando la miran.
- **C)** `query` y `key` son lo mismo con otro nombre; `value` es el resultado final.
- **D)** Son las tres capas del transformer, en orden.

---

### 3. [leer una salida] La fila de la palabra «y»

Esta es una fila real de la matriz de atención del modelo de la clase (bloque 2, cabeza 1)
sobre la oración *«la educación, la salud, la seguridad y la justicia»*:

| a quién mira «y» | la | educación | , | la | salud | , | la | seguridad | y | la | justicia |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **peso** | 0,00 | **0,28** | 0,05 | 0,00 | **0,23** | 0,05 | 0,00 | **0,39** | 0,00 | 0,00 | 0,00 |

Y estas son las **sumas de cada columna** de esa misma matriz:

| columna | la | educación | , | la | salud | , | la | seguridad | y | la | justicia |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **suma** | 2,02 | 1,65 | **4,03** | 0,01 | 0,77 | 1,52 | 0,01 | 0,99 | 0,01 | 0,00 | 0,00 |

**a)** ¿A qué palabra le presta más atención «y»?

**b)** ¿Cuánto suma la fila de «y»? ¿Y por qué las columnas suman cualquier cosa (una
llega a 4,03 y otras dan 0,00)?

**c)** Las tres palabras que se llevan casi toda la atención de «y» son *educación*,
*salud* y *seguridad*. ¿Qué te dice eso sobre lo que está haciendo esa cabeza? Y —más
importante— ¿qué **no** te autoriza a concluir?

**d)** ¿Por qué las últimas dos columnas (*la*, *justicia*) suman exactamente 0,00?

---

### 4. [qué pasa si...] Le sacás la máscara causal

Entrenás un modelo que tiene que **generar** texto (predecir la próxima palabra) y te
olvidás de poner la máscara causal.

**a)** ¿Qué va a aprender el modelo?

**b)** ¿Por qué su loss de entrenamiento va a dar **engañosamente buena**?

**c)** ¿En qué momento te vas a dar cuenta de que algo anda mal?

---

### 5. [qué pasa si...] Le sacás el *positional encoding*

Sacás el sellito de posición y dejás sólo attention.

**a)** ¿Qué dos frases se volverían **indistinguibles** para el modelo? Dá un ejemplo
tuyo, del área que investigás (no uses el de la clase).

**b)** ¿Con qué técnica de análisis de texto que ya conocías queda equivalente el modelo?

---

### 6. [cálculo simple] Softmax

Cuatro palabras reciben estos puntajes crudos: **2,0 · 0,6 · −0,5 · 0,8**.
Después del softmax, los pesos quedan: **0,61 · 0,15 · 0,05 · 0,18**.

**a)** Verificá que los pesos suman 1 y decí cuál se lleva más atención.

**b)** Si multiplicás **todos** los puntajes por 3 (o sea: 6,0 · 1,8 · −1,5 · 2,4), ¿la
distribución se **afila** (el ganador se lleva más) o se **aplana** (se reparte más
parejo)? ¿Por qué?

**c)** ¿Y si los multiplicás por 0,1?

*(Esta pregunta prefigura una perilla de la clase 8. ¿Cuál te parece que es?)*

---

### 7. [múltiple choice] ¿Para qué sirven las cabezas múltiples?

- **A)** Para procesar varias oraciones al mismo tiempo y así entrenar más rápido.
- **B)** Para que cada cabeza mire un tipo de relación distinta entre las palabras, con su
  propio juego de perillas Q, K y V, y después se junten los resultados.
- **C)** Para tener repuesto: si una cabeza falla, las otras la reemplazan.
- **D)** Para reducir la cantidad de parámetros del modelo.

---

### 8. [múltiple choice] ¿Qué función cumple la conexión residual?

- **A)** Normaliza los números para que no se disparen.
- **B)** Suma la entrada del bloque a su salida, para que la información original no se
  pierda al apilar bloques y para que el gradiente llegue hasta abajo.
- **C)** Conecta la última capa con la primera para que el modelo pueda repasar.
- **D)** Guarda una copia de los datos de entrenamiento por si el modelo la necesita.

---

### 9. [abierta] Attention contra la memoria de las RNN

Explicá **con tus palabras y sin fórmulas** por qué attention resuelve el problema de
memoria de las RNN de la clase 6.

Y después —esta es la parte que importa— **mencioná qué problema nuevo introduce**.

---

### 10. [leer una arquitectura] Las dos piezas sin rótulo

Este es el bloque transformer que armaste hoy, con dos piezas sin nombre:

```
entrada ──► [ ??? ] ──► [ attention ] ──►( + )──► [ ??? ] ──► [ MLP ] ──►( + )──► salida
              │                            ▲                                ▲
              └────────────────────────────┘                                │
                                            └───────────────────────────────┘
```

**a)** ¿Qué son las dos piezas marcadas con `???`?

**b)** ¿Qué son las dos flechas largas que rodean los bloques y terminan en un `+`?

**c)** ¿Por qué la salida del bloque tiene **la misma forma** que la entrada, y por qué eso
importa?

---

### 11. [criterio aplicado a tu investigación]

Un paper que estás leyendo afirma:

> *«El mapa de atención muestra que el modelo se basa en la palabra "inmigrante" para
> clasificar la nota como negativa, lo que evidencia el sesgo del modelo.»*

**a)** ¿Qué parte de esa afirmación es defendible y qué parte no?

**b)** ¿Qué evidencia adicional le pedirías a quien lo escribió?

**c)** Ahora date vuelta: si **vos** quisieras sostener que un modelo usa esa palabra para
clasificar, ¿qué experimento harías? Escribilo como se lo escribirías a un revisor.
