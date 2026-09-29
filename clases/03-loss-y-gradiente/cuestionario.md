# Clase 3 — Cuestionario

**Estar equivocado es un número, y ese número tiene pendiente**

Doce preguntas. Las de opción múltiple tienen **una sola** respuesta correcta.
Las abiertas se contestan en tres o cuatro oraciones: **no hace falta ninguna fórmula**
y no se puntúa la prolijidad matemática, se puntúa el criterio.

Tiempo estimado: 35-45 minutos. Se hace **antes de la clase 4**. Se puede hacer con el
notebook abierto al lado; de hecho, para dos preguntas conviene.

---

## 1. `[opción múltiple]` ¿Qué es una función de pérdida (*loss*)?

- **a)** El error que comete el modelo en un caso particular.
- **b)** Un número que resume, en una sola cifra, qué tan mal está el modelo sobre todos
  los datos, según un criterio que elige quien modela.
- **c)** La cantidad de información que se pierde al simplificar los datos.
- **d)** El porcentaje de casos extremos que conviene sacar de la base antes de modelar.

---

## 2. `[opción múltiple]` En el mapa de contornos de la loss que vimos hoy, ¿qué representa cada punto del plano?

- **a)** Un caso de la base de datos.
- **b)** Un año de la serie.
- **c)** Una recta completa: un par de valores de las dos perillas.
- **d)** El valor de la loss en una iteración del entrenamiento.

---

## 3. `[qué pasa si...]` El caso extremo

Tenés 200 municipios y una regresión que predice cantidad de protestas. Descubrís que
cargaste mal un municipio: le pusiste 850 protestas donde iban 85.

**a)** ¿Qué le pasa al MSE cuando ese caso está en la base? ¿Y al MAE?
**b)** ¿Cuál de las dos rectas (la que minimiza MSE o la que minimiza MAE) se mueve más
al sacar ese caso? ¿Por qué?
**c)** En una oración: ¿qué te dice esto sobre qué loss usar mientras todavía estás
limpiando tus datos?

---

## 4. `[qué pasa si...]` El learning rate por diez

Entrenaste con `lr = 0.01` y la loss bajó lindo. Alguien te dice «ponele `0.1`, va a ir
diez veces más rápido».

Describí **los dos resultados posibles** y cómo distinguirías uno del otro **mirando sólo
la curva de loss**.

---

## 5. `[leer un gráfico]` Tres entrenamientos

Tres curvas de loss contra iteración, del mismo modelo con los mismos datos. Sólo cambia
el *learning rate*.

```
   A                        B                        C
loss                     loss                     loss
 |                        |                        |      /
 |________________        |\                       |     /
 |                        | \___________           |    /
 |                        |                        |___/
 +--------------> iter    +--------------> iter    +--------------> iter
   (queda alta y          (cae rápido y se         (arranca abajo y
    casi horizontal)       aplana bien abajo)       se va para arriba)
```

Apareá cada curva con su diagnóstico y **escribí qué harías con el learning rate en cada caso**:

- learning rate **bien elegido** → curva ___
- learning rate **demasiado chico** → curva ___
- learning rate **demasiado grande** → curva ___

---

## 6. `[leer un gráfico]` La flecha en el mapa

Un mapa de contornos de la loss. El punto **P** está arriba a la izquierda; el fondo del
valle (marcado con ✚) está en el centro. Desde **P** sale una flecha que apunta **hacia
arriba y hacia la izquierda**, o sea alejándose del valle.

```
        ↖ (la flecha que sale de P)
         P •
              (  (  ( ✚ )  )  )     ← curvas de nivel, el fondo en el centro
```

**a)** ¿Qué es esa flecha?
**b)** ¿Hacia dónde se va a mover **P** en el próximo paso del descenso: hacia arriba a la
izquierda, o hacia abajo a la derecha? ¿Por qué?
**c)** ¿La flecha apunta exactamente al fondo del valle? Explicá tu respuesta.

---

## 7. `[opción múltiple]` ¿Por qué no se busca el mínimo probando todas las combinaciones posibles de parámetros?

- **a)** Porque el resultado sería menos preciso que el del descenso por gradiente.
- **b)** Porque la cantidad de combinaciones crece tan rápido con la cantidad de parámetros
  que se vuelve imposible de calcular, incluso con pocas perillas.
- **c)** Porque no se sabe de antemano qué valores puede tomar cada parámetro.
- **d)** Porque probar todas las combinaciones da un mínimo local y no el global.

---

## 8. `[opción múltiple]` ¿Qué es el *learning rate*?

- **a)** La velocidad con la que la computadora hace los cálculos.
- **b)** Cuánto se mueven los parámetros en cada paso, en proporción a la pendiente.
- **c)** Cuántos datos mira el modelo antes de actualizar los parámetros.
- **d)** Qué porcentaje de los datos se usa para entrenar.

---

## 9. `[abierta]` La niebla

Explicá con tus palabras, **sin fórmulas y sin usar la palabra «derivada»**, por qué el
gradiente sirve para llegar al fondo de un valle aunque no puedas ver el paisaje completo.
Tres o cuatro oraciones.

---

## 10. `[distinción]` Descenso por gradiente y *backpropagation*

Alguien dice: «usamos backpropagation en vez de descenso por gradiente porque es más
moderno». Corregilo en dos oraciones: ¿qué hace cada una de las dos cosas y cómo se
relacionan?

---

## 11. `[aplicación sustantiva]` Protestas por mes

Estás modelando **cantidad de protestas por mes** en una serie de diez años. Hay tres meses
de conflictividad excepcional (un estallido) con valores diez veces más altos que el resto.

Elegí **MSE o MAE** y justificá tu elección **dos veces**: una vez para un objetivo de
investigación que haga preferible el MSE, y otra vez para un objetivo distinto que haga
preferible el MAE. Escribí explícitamente cuál es el objetivo en cada caso.

*(No hay respuesta correcta única. Se evalúa que el objetivo de investigación y la loss
elegida sean coherentes entre sí.)*

---

## 12. `[criterio / ética aplicada]` La beca

Un ministerio quiere usar un modelo que predice **riesgo de deserción escolar** para asignar
un número limitado de becas de retención.

**a)** ¿Qué error es más costoso: **no darle la beca a alguien que iba a desertar**, o
**dársela a alguien que no la necesitaba**? Argumentá; no hay respuesta técnica.
**b)** ¿Quién debería tomar esa decisión, y en qué parte del proceso queda escrita?
**c)** Si en el paper leés «el modelo fue optimizado para maximizar la exactitud», ¿qué
pregunta le harías al equipo?

---

## Autoevaluación

Marcá lo que puedas hacer sin mirar los apuntes:

- [ ] Explicarle a alguien qué es una loss, en una oración, sin usar la palabra «error».
- [ ] Decir en qué se diferencian MSE y MAE **y** cuándo elegirías cada una.
- [ ] Explicar qué es cada punto del mapa de la loss.
- [ ] Calcular una pendiente con una resta, en papel, con dos evaluaciones de una función.
- [ ] Mirar una curva de loss y decir si el learning rate está bien.
- [ ] Explicar por qué va un signo menos en `a = a - lr * pendiente`.
- [ ] Decir qué **no** garantiza el descenso por gradiente.
