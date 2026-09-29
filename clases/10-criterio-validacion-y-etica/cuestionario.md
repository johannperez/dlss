# Cuestionario — Clase 10

**Criterio: validez, sesgo, reproducibilidad y el revisor 2**

> Doce preguntas. Las primeras son de reconocer una idea; las últimas son de **usarla**, que
> es lo único que importa. Las tres finales no tienen respuesta única: se evalúan por el
> argumento, no por la conclusión.
>
> **Dos usos, y hay que elegir uno.**
>
> - **En el aula, 15 minutos** (como en el resto del curso): la **1, la 2, la 4 y la 5**. Son
>   las de reconocer y leer una salida, y se corrigen en el momento.
> - **Como integrador final, unos 50 minutos** para las doce. Es la última clase: no hay
>   clase siguiente, así que esto no es una tarea «para la próxima». Sirve como cierre fuera
>   del horario o como una parte del proyecto final (`recursos/GUIA-DEL-DOCENTE.md` §6). Si
>   hay media hora, la 1, la 4, la 5, la 9 y la 12.
>
> Es el único cuestionario del curso que tiene la versión larga, y es a propósito: los tres
> últimos ítems son de diseño y el doce es de una página. La desviación está declarada en
> `PROGRAMA.md` §3.4.

---

## 1. [Multiple choice] Desempeño y validez

Un clasificador de «discurso de odio» obtiene F1 = 0,91 sobre un conjunto de test que nunca
vio. ¿Cuál de estas afirmaciones está **justificada** por ese número?

- **A.** El modelo detecta discurso de odio con un 91 % de eficacia.
- **B.** El modelo reproduce las etiquetas de ese corpus con un F1 de 0,91.
- **C.** El modelo es mejor que un humano codificando discurso de odio.
- **D.** El modelo va a funcionar bien en otro corpus del mismo idioma.

---

## 2. [Multiple choice] Validez de constructo

«Validez de constructo», aplicada a un clasificador, quiere decir:

- **A.** Que el modelo está bien construido y no tiene errores de programación.
- **B.** Que el modelo generaliza bien a datos nuevos del mismo tipo.
- **C.** Que lo que el modelo mide es efectivamente el concepto del que habla el paper.
- **D.** Que el modelo usa una arquitectura apropiada para el tipo de dato.

---

## 3. [Qué pasa si…] El clasificador que envejece

Entrenaste un clasificador de «populismo» con textos de 2010-2015 y lo aplicás a 2020-2024.
Los resultados muestran una caída fuerte del populismo a partir de 2019.

**(a)** ¿Qué tipo de validez está en juego?
**(b)** Nombrá **dos** explicaciones posibles del resultado, una sustantiva y una instrumental.
**(c)** Escribí **un test concreto** que permita distinguir entre las dos. Decí qué datos
necesitás y qué resultado esperarías bajo cada explicación.

---

## 4. [Leer una salida de código] Los términos más influyentes

Un clasificador de «conflictividad» sobre prensa local devuelve estos pesos:

```
+1,41  paro          +0,88  reclamo       +0,71  clarín
+1,12  corte         +0,84  gremio        +0,68  jueves
+0,96  marcha        +0,79  ruta          +0,64  fotogalería
```

**(a)** Separá los términos en dos columnas: **señales del concepto** y **atajos**.
**(b)** Explicá, para **cada** atajo, por qué separa las clases sin medir el concepto.
**(c)** ¿Qué le pasaría a este modelo aplicado a prensa de otra provincia? ¿Y a prensa de 2015?

---

## 5. [Leer una tabla] Una auditoría de sesgo

Es el clasificador de «nota sobre política» de la clase, con la plantilla
«[SUJETO] reclamó frente a la sede del ministerio». Alguien te muestra esta tabla y te dice:
*«el modelo no discrimina por ocupación: enfermeras y obreras sacan exactamente lo mismo. Y
el sesgo de género es chico y parejo»*.

| sujeto | puntaje | ¿en el vocabulario del modelo? |
|---|---|---|
| las médicas | 0,346 | sí |
| los médicos | 0,275 | sí |
| las enfermeras | 0,307 | **no** |
| los enfermeros | 0,265 | **no** |
| las obreras | 0,307 | **no** |
| los obreros | 0,265 | **no** |

*Dato que vas a necesitar:* en este modelo, «los» pesa −0,34 y «las» −0,14.

**(a)** ¿Qué se puede concluir de esta tabla?
**(b)** Y —más importante— **¿qué NO se puede concluir?** Escribí las dos cosas que la persona
que te la mostró está afirmando de más.
**(c)** ¿Qué le pedirías antes de aceptar cualquier conclusión?

---

## 6. [Diseño] Tres pares mínimos

Diseñá **tres pares mínimos** para poner a prueba un clasificador de «crítica al gobierno».
Para cada uno, escribí las dos oraciones y explicá **qué testea**:

- uno donde el modelo **debería** cambiar de lado;
- uno donde **no debería** cambiar nada;
- uno **límite**, de esos que a vos mismo te costaría codificar.

---

## 7. [Diseño] Un test de placebo

Diseñá un test de placebo para un detector de discurso de odio.

**(a)** ¿Qué corpus usarías?
**(b)** ¿Qué resultado esperarías si el modelo es válido?
**(c)** ¿Qué resultado te haría sospechar, y de qué exactamente?
**(d)** Diseñá además su **control positivo**: ¿dónde el fenómeno tiene que aparecer sí o sí?

---

## 8. [Reproducibilidad] El apéndice mínimo

Enumerá los **seis** elementos mínimos que tiene que tener el apéndice metodológico de un
paper que usa un clasificador, y para cada uno escribí en una línea **qué se rompe si falta**.

---

## 9. [Distinción] Tres explicaciones de la misma tabla

Un modelo asigna puntajes más altos de «agresividad» a textos que mencionan cierta región del
país.

**(a)** Distinguí las **tres** explicaciones posibles: sesgo del mundo, del corpus, e
introducido por el modelado.
**(b)** Para cada una, decí **cómo la distinguirías empíricamente** de las otras dos. No basta
con nombrarlas: hace falta el dato que irías a buscar.
**(c)** Si las tres estuvieran operando a la vez, ¿cambia lo que reportás?

---

## 10. [Criterio] Cuándo no

Mencioná **tres situaciones concretas de tu propia investigación** en las que **no** usarías
deep learning, y qué usarías en su lugar. Situaciones concretas: no «cuando hay pocos datos»,
sino «en mi capítulo 3, donde tengo 180 entrevistas codificadas».

---

## 11. [Revisión] Tres comentarios de revisor

> **Resumen recibido.** *«Analizamos 2,4 millones de tuits de la campaña 2023 con un modelo
> de lenguaje de última generación para medir la polarización afectiva. El modelo alcanza una
> exactitud del 94 % en la tarea. Encontramos que la polarización aumentó un 31 % durante la
> campaña, con un pico en la semana previa a la elección. Los resultados sugieren que las
> redes sociales amplifican la hostilidad política.»*

Escribí **tres comentarios de revisor**, ordenados por gravedad. Para cada uno indicá:
qué falta, por qué importa, y **si es fatal o se arregla con una revisión menor**.

---

## 12. [Ética aplicada] La consulta del municipio

Un municipio quiere usar un modelo entrenado con reclamos ciudadanos (formularios web, líneas
telefónicas) para **priorizar** cuáles se atienden primero. Te consultan **antes** de
implementarlo.

Escribí una respuesta de **una página** que cubra:

- **qué preguntarías** antes de opinar;
- **qué exigirías** como condición para que se implemente;
- **qué monitorearías** después de la implementación, y con qué frecuencia;
- **en qué caso recomendarías directamente no hacerlo.**

*No hay una respuesta correcta. Se evalúa si la respuesta identifica quién soporta el costo
del error, si prevé cómo se van a detectar los errores del sistema, y si distingue las
condiciones técnicas de las institucionales.*
