# Clase 9 — Cuestionario

**Usar modelos que ya existen, sin creerles**

> Doce preguntas. Las primeras son de concepto, las del medio son de leer un número o un
> gráfico, y las últimas son de criterio aplicado a tu propia investigación — esas no
> tienen una respuesta correcta única, tienen respuestas **defendibles**.
> Contestá con el notebook al lado si lo necesitás: no es una prueba de memoria.

---

## 1. Transfer learning (opción múltiple)

¿Por qué usar un modelo pre-entrenado permite trabajar con **menos** datos etiquetados
que entrenar uno desde cero?

- **a)** Porque el modelo pre-entrenado ya vio ejemplos de tu categoría.
- **b)** Porque el modelo ya aprendió regularidades generales del idioma, y sólo hay que
  ajustar una capa fina para tu distinción particular.
- **c)** Porque los modelos grandes generalizan mejor por definición, sin importar la tarea.
- **d)** Porque el pre-entrenamiento incluye una fase de validación que evita el sobreajuste.

---

## 2. Congelar capas (opción múltiple)

"Congelar" las primeras capas de un modelo pre-entrenado significa:

- **a)** Guardar el modelo en disco para no tener que bajarlo otra vez.
- **b)** Dejar sus parámetros fijos durante el entrenamiento, y ajustar sólo los de las
  capas de arriba.
- **c)** Reducir la precisión numérica de los pesos para que el modelo ocupe menos memoria.
- **d)** Impedir que el modelo vea los datos de test.

Y una segunda parte, en una línea: **¿qué tiene que ver congelar capas con la clase 4?**

---

## 3. Leer una matriz de confusión

Entrenaste un clasificador para detectar notas de prensa sobre **conflicto laboral**.
Sobre un test de 400 notas etiquetadas a mano obtenés:

|  | el modelo dijo **sí** | el modelo dijo **no** |
|---|---|---|
| **sí era** conflicto laboral | 48 | 32 |
| **no era** conflicto laboral | 24 | 296 |

- **(a)** Calculá precisión, recall y accuracy.
- **(b)** Escribí **las dos frases en castellano llano**, con los números adentro.
- **(c)** ¿Cuál es la accuracy del modelo bobo que dice siempre "no"?

---

## 4. Un número que suena bien

Un colega te muestra un clasificador que detecta **denuncias por violencia de género** en
un corpus de 20.000 notas. Reporta **96 % de accuracy** y está muy contento.
Después averiguás que en ese corpus el **4 %** de las notas son sobre el tema.

¿El resultado es bueno? Justificá en tres o cuatro oraciones y decí **qué número le
pedirías** antes de creerle.

---

## 5. Qué pasa si bajás el umbral

Tenés un clasificador que devuelve un puntaje de 0 a 1 y venís cortando en 0,5.
Lo bajás a 0,3.

- **(a)** ¿Qué le pasa a la **precisión**? ¿Y al **recall**? ¿Por qué?
- **(b)** Describí **una** situación de investigación donde te convenga bajarlo, y **una**
  donde te convenga subirlo. Que sean situaciones concretas, no "cuando querés más recall".

---

## 6. Qué estrategia elegís

- **(a)** Tenés **60** documentos etiquetados y podés producir 40 más. ¿Qué estrategia
  usás y por qué?
- **(b)** Tenés **3.000** etiquetados. ¿Cambia tu respuesta? ¿Por qué?
- **(c)** En los dos casos, ¿qué comparación **obligatoria** vas a reportar, sin importar
  la estrategia?

---

## 7. Modelos en inglés sobre texto en castellano (opción múltiple)

Un tutorial muy popular usa un modelo de sentimiento entrenado en inglés. Lo aplicás a tus
titulares en castellano. ¿Cuál es el problema principal?

- **a)** El código va a tirar un error porque el tokenizador no reconoce las tildes.
- **b)** Va a funcionar sin avisar de nada y va a andar peor de lo que creés, porque
  tokeniza mal el castellano y sus representaciones se construyeron con otro idioma.
- **c)** No hay problema real: el sentimiento es universal y no depende del idioma.
- **d)** El problema es sólo de velocidad: tarda más porque tiene que traducir internamente.

---

## 8. El procedimiento completo (aplicación)

Tenés **20.000** notas de prensa y querés identificar las que mencionan **conflicto
laboral**. Escribí el procedimiento completo, paso por paso. Tiene que incluir, como
mínimo:

- cuántas notas etiquetás a mano y **cómo las elegís**;
- quién las etiqueta y **qué medís sobre esa codificación**;
- cómo partís los datos y **por qué así**;
- contra qué comparás tu resultado;
- qué mirás **después** de tener el número.

---

## 9. El modelo y los humanos (interpretación)

El acuerdo entre tus dos codificadores humanos es **kappa 0,65**. Tu modelo, evaluado
contra las etiquetas de **uno** de ellos, saca **F1 0,92**.

- **(a)** Nombrá **dos** explicaciones posibles.
- **(b)** Para cada una, decí **qué harías** para distinguir si es esa o la otra.

---

## 10. Análisis de errores

Tu clasificador de "notas sobre **protesta**" produce estos seis falsos positivos:

1. "Los vecinos elevaron un reclamo formal al municipio por el estado de las calles"
2. "Fuerte reclamo de la oposición en el recinto por el proyecto de presupuesto"
3. "Reclamo publicitario: la marca deberá retirar el aviso por competencia desleal"
4. "El club presentó un reclamo ante la AFA por el arbitraje del domingo"
5. "Reclamo de los usuarios por los cortes de luz en el conurbano"
6. "Los accionistas presentaron un reclamo formal ante el directorio"

- **(a)** ¿Qué patrón sistemático los une?
- **(b)** ¿Qué te dice eso sobre tu definición operativa de "protesta"?
- **(c)** ¿Alguno de los seis podría estar **bien** clasificado? ¿Cuál, y de qué depende?

---

## 11. La sección de métodos (reporte)

Escribí las **tres a cinco oraciones** de la sección de métodos que reportan tu
clasificador, de manera que otro equipo pueda replicarlo. Usá números inventados
plausibles si te hace falta, pero **no puede faltar ningún elemento necesario**.

---

## 12. Criterio y ética aplicada

Un organismo público quiere usar un clasificador de **"riesgo"** sobre denuncias
ciudadanas, para priorizar cuáles atender primero. El modelo tiene un **F1 de 0,85**
medido sobre una muestra etiquetada por personal del organismo.

- **(a)** ¿Qué métrica te preocupa más, precisión o recall? ¿Por qué, en este caso?
- **(b)** ¿Qué pasa con las denuncias que el modelo despriorizó y **nadie leyó nunca**?
  ¿Cómo se entera el organismo de que se equivocó?
- **(c)** Nombrá **un mecanismo concreto** que exigirías antes de que el sistema se
  implemente, y decí qué problema resuelve.
