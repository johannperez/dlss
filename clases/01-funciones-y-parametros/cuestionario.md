# Clase 1 — Cuestionario

**Una función es una máquina con perillas**

No es un examen. Es para que veas qué te quedó y qué conviene volver a mirar antes de
la clase 2. Se hace en unos 20 minutos; el bonus del final es
opcional. Las soluciones están en
`cuestionario-soluciones.md`: **mirálas recién después de haber contestado todo**,
incluso lo que te salió mal, porque ahí está lo interesante.

Las preguntas 8 y 10 no tienen una única respuesta correcta y así están pensadas.

---

## 1. ¿Cuál es un parámetro?

En el modelo `f(x) = a·x + b`, donde `x` es el año y `f(x)` es el porcentaje de
palabras dedicadas a seguridad:

- **A.** `x`, porque es lo que va cambiando.
- **B.** `a`, porque es el mismo número para todos los años de la base.
- **C.** `f(x)`, porque es el resultado del modelo.
- **D.** Depende de qué le estés preguntando a la base.

---

## 2. ¿Qué distingue a un parámetro de una variable?

- **A.** El parámetro es un número decimal y la variable es un número entero.
- **B.** El parámetro se escribe con letras del principio del alfabeto y la variable
  con letras del final.
- **C.** El parámetro es el mismo para todos los casos de la base; la variable cambia
  de un caso a otro.
- **D.** El parámetro lo calcula la computadora y la variable la mide la persona que
  investiga.

---

## 3. Qué pasa si…

Tenés `f(x) = a·x + b` con `a = 0.5` y `b = 10`.

**(a)** Si duplicás `a` (pasa a 1.0), ¿qué le pasa al dibujo? ¿La recta se mueve
entera o gira? ¿Alrededor de qué punto?

**(b)** Si duplicás `b` (pasa a 20), ¿qué le pasa al dibujo?

**(c)** ¿Cuál de los dos cambios modifica el valor de `f(0)`?

---

## 4. Qué pasa si ponés `a = 0`

**(a)** ¿Qué figura queda dibujada?

**(b)** Ese modelo, traducido a una oración en castellano sobre el fenómeno,
¿qué está afirmando? (Escribí la oración, sin usar la palabra «pendiente».)

**(c)** ¿Es una afirmación tonta? Justificá en una línea.

---

## 5. Leer un gráfico: ordenar tres rectas

Sobre la misma nube de 36 puntos (menciones a seguridad, 1984-2019, que va de 0 a
0,44 % con un promedio de 0,155 %) se dibujan tres rectas:

- **Recta P:** horizontal a la altura 0,155.
- **Recta Q:** horizontal a la altura 0,40.
- **Recta R:** arranca en 0,085 en 1984 y sube 0,004 por año.

Ordenalas **de menor a mayor desajuste** (de la que mejor ajusta a la que peor) y
justificá en una oración, sin hacer ninguna cuenta.

---

## 6. Leer un gráfico: ¿qué se movió?

Ves una figura con **ocho curvas superpuestas**, todas con la misma forma de S, todas
saturando en el mismo techo, pero cada una hace su salto en un año distinto: la
primera en 1990, la última en 2015.

**(a)** ¿Se movió una variable o un parámetro para generar esa familia?

**(b)** ¿Cuál de las dos perillas de la sigmoide se movió: la que controla lo
empinado del salto, o la que controla dónde está el salto?

**(c)** ¿Qué representa el conjunto de las ocho curvas juntas?

---

## 7. Reconocer la forma

Apareá cada descripción sustantiva con la forma del zoo que le corresponde.
Cada forma se usa una sola vez.

| # | Descripción |
|---|---|
| 1 | «La adopción de la tecnología arrancó despacio, se aceleró y en los últimos años ya casi no crece: está todo el mundo adentro.» |
| 2 | «El tema aparece cada cuatro años, sin falta.» |
| 3 | «Crece siempre lo mismo: dos puntos por año, desde el primero hasta el último.» |
| 4 | «Subió durante veinte años, llegó a un máximo y desde entonces baja.» |
| 5 | «Los primeros meses casi no se notó, y después se disparó sin freno.» |

| Letra | Forma |
|---|---|
| A | recta |
| B | parábola |
| C | exponencial |
| D | sigmoide |
| E | seno |

---

## 8. Traducción sustantiva

La mejor recta sobre las menciones a **educación** en los mismos discursos
(1984-2019) da `a = 0.0037` y `b = 0.208`, donde `x` son los años desde 1984 y el
resultado está en porcentaje de palabras del discurso. *(Estos dos números están
medidos sobre los datos del curso, no inventados para el ejercicio.)*

**(a)** Escribí en **una oración, sin jerga**, qué dice ese modelo.

**(b)** Escribí **otra oración** sobre algo que ese modelo **no** dice, aunque
alguien podría creer que sí.

**(c)** Si `a` hubiera dado `-0.0037` en vez de `+0.0037`, ¿qué cambiaría en tu
oración de la parte (a)? ¿Y qué **no** cambiaría?

---

## 9. Encontrar el error en el código

Esta función tenía que devolver el valor de una recta, pero algo le falta.
¿Qué está mal y qué habría que escribir?

```python
def recta(x, a, b):
    """Debería devolver a*x + b."""
    resultado = a * x + b
```

Y esta otra corre sin dar error, pero devuelve siempre lo mismo aunque le cambies
`x`. ¿Por qué?

```python
def recta_rara(x, a, b):
    return a * b + b
```

---

## 10. Criterio: ¿la medida mide lo que dice medir?

Se propone el «porcentaje de palabras del discurso presidencial de apertura dedicadas
al léxico de seguridad» como medida de **«la prioridad del gobierno en materia de
seguridad»**.

Dá **dos razones distintas** por las que esa medida podría no capturar lo que dice
capturar. Para cada una, escribí en una línea qué evidencia adicional te haría dudar
menos.

*(Esta pregunta no tiene una respuesta única y no está buscando una. Está buscando
que puedas escribir dos objeciones que un revisor te haría.)*

---

## 11. Bonus (opcional), para pensar hasta la clase que viene

En el zoo hay seis formas. El **desafío 3** (dos picos y un valle) no lo saca
ninguna: está medido, el mejor techo es 0,213 y se ve mal.

¿Qué harías vos para dibujar esa figura? Escribí tu idea en dos líneas **antes** de
la clase 2. No importa si está bien: importa que la hayas pensado.
