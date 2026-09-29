# Clase 4 — Cuestionario

**El ciclo de entrenamiento, y la diferencia entre dibujar y calcar**

Doce preguntas con puntaje, más una última para llevarse a casa. Las de opción múltiple
tienen **una sola** respuesta correcta.
Las abiertas se contestan en dos o tres oraciones: no buscamos extensión, buscamos criterio.

Podés mirar el notebook y las slides. No es un examen de memoria.

---

## 1. Qué es el sobreajuste *(opción múltiple)*

Un modelo **sobreajustado** (*overfitted*) es un modelo que:

- **A.** Tiene demasiados parámetros, sin importar cómo le vaya con los datos.
- **B.** Anda muy bien sobre los datos con los que se entrenó y mal sobre datos que no vio.
- **C.** Tiene una loss de entrenamiento alta porque no pudo aprender.
- **D.** Se entrenó durante demasiadas épocas, siempre.

---

## 2. Validación contra test *(opción múltiple)*

¿Cuál es la diferencia entre el conjunto de **validación** y el de **test**?

- **A.** Ninguna importante: son dos nombres para los datos apartados.
- **B.** La validación es más grande que el test.
- **C.** La validación se usa para **tomar decisiones** (cuántas neuronas, cuándo parar) y el
  test para **reportar** el resultado final, una sola vez.
- **D.** La validación se usa para entrenar el modelo cuando el entrenamiento no alcanza.

---

## 3. Leer la tijera *(gráfico)*

Este es el gráfico que salió del notebook: 16 rampas, 22 casos de entrenamiento.

```
 loss
0.035 ┤ o          (o = validación, naranja; · = entrenamiento, azul)
      │
0.030 ┤
      │
0.025 ┤ ·
      │    ooo                                   oooooooooooooooooooo
0.020 ┤   o   ooooooooooooooooooooooooooooooooooo
      │
0.015 ┤
      │  ▼
0.010 ┤  ·····
      │       ······················
0.005 ┤                             ································
      └┬───────────┬───────────┬───────────┬───────────┬───────────┬
       0          300         600         900         1200        1500
                                 épocas
       ▼ = el punto más bajo de la naranja: época 42, loss 0.0133
       Eje recortado arriba: en la época 1 las dos curvas arrancan mucho más
       alto (0.36 la azul, 0.18 la naranja) y entran al gráfico hacia la época 15.
```

**a.** ¿En qué época habría que haber parado el entrenamiento? ¿Por qué esa y no otra?

**b.** ¿Qué representa, en términos sustantivos, la franja que se abre entre la curva azul y
la naranja a partir de la época 50?

**c.** Un colega mira este gráfico y dice: *"la loss bajó de 0.36 a 0.006, el modelo aprendió
un montón"*. ¿Qué le contestás?

---

## 4. Cuatro diagnósticos *(apareamiento)*

Apareá cada combinación de losses con su diagnóstico: son cuatro y cuatro, uno por uno.
Ojo con el cuarto caso, que es raro y merece una nota aparte.

| | loss de entrenamiento | loss de validación |
|---|---|---|
| **I**   | alta | alta |
| **II**  | baja | alta |
| **III** | baja | baja |
| **IV**  | alta | **más baja que la de entrenamiento** |

Diagnósticos:

1. Sobreajuste: el modelo calcó la muestra.
2. Todo bien: el modelo aprendió algo que se generaliza.
3. Subajuste (*underfitting*): el modelo es demasiado rígido, o entrenó poco, o el learning
   rate está mal.
4. Algo raro pasa con la partición. Escribí **dos** cosas que podrían estar causándolo.

---

## 5. Qué pasa si… *(abierta corta)*

Tenés **30 casos** y un modelo con **5000 parámetros**.

**a.** ¿Qué esperás que pase con la loss de **entrenamiento**?

**b.** ¿Y con la de **test**?

**c.** ¿Cambiaría tu respuesta si tuvieras 30.000 casos y el mismo modelo? ¿Por qué?

---

## 6. Qué pasa si… *(opción múltiple)*

Duplicás la cantidad de datos de entrenamiento y dejás el modelo exactamente igual.
¿Qué le pasa, típicamente, a la **brecha** entre la loss de entrenamiento y la de validación?

- **A.** Se agranda, porque hay más datos que memorizar.
- **B.** Se achica, porque el mismo número de perillas ahora tiene que servir para más casos.
- **C.** No cambia: la brecha depende sólo del modelo.
- **D.** Desaparece del todo: con suficientes datos no hay sobreajuste posible.

---

## 7. Ordenar el loop *(código)*

Estas cinco líneas están desordenadas. Ponelas en el orden correcto y escribí al lado, en
castellano, qué hace cada una.

```python
optimizador.step()
perdida = criterio(prediccion, y)
optimizador.zero_grad()
prediccion = modelo(x)
perdida.backward()
```

---

## 8. El bug clásico *(código)*

Este loop tiene un problema:

```python
for epoca in range(500):
    prediccion = modelo(x)
    perdida = criterio(prediccion, y)
    perdida.backward()
    optimizador.step()
```

**a.** ¿Qué línea falta?

**b.** ¿Qué síntoma esperarías ver en la curva de loss?

**c.** ¿Por qué produce ese síntoma? (Una oración.)

---

## 9. Vocabulario con números *(abierta corta)*

Tenés **1200 casos** y entrenás con lotes (*batches*) de **200**.

**a.** ¿Cuántas iteraciones hay en una época?

**b.** Si entrenás 15 épocas, ¿cuántas veces se actualizaron las perillas en total?

**c.** Alguien dice "entrené 3000 iteraciones". ¿Cuántas épocas hizo?

---

## 10. Aplicación: datos de panel *(abierta)*

Tenés discursos de **50 diputados**, **20 discursos de cada uno** (1000 en total), y querés
entrenar un modelo que prediga el **partido** a partir del texto.

**a.** ¿Cómo partirías los datos? Sé específico.

**b.** ¿Por qué **no** al azar? Explicá qué aprendería el modelo si partieras al azar.

**c.** Si partís bien y el desempeño cae mucho respecto de partir al azar, ¿eso significa que
tu modelo empeoró?

---

## 11. Aplicación: serie temporal *(abierta)*

Tenés una serie **mensual de 2010 a 2023** (168 meses) con un índice de conflictividad social,
y querés predecir la conflictividad del mes siguiente.

**a.** ¿Cómo partís los datos?

**b.** ¿Qué pregunta de investigación contesta esa partición, y cuál **no** contesta?

**c.** Nombrá una cosa concreta que podría filtrarse desde el futuro hacia el pasado sin que
te des cuenta. *(Pista: pensá en cómo se construyó el índice.)*

---

## 12. Criterio: el revisor 2 *(abierta, la importante)*

Estás revisando un artículo. Dice:

> *"Entrenamos un clasificador de tono sobre 2.400 noticias y obtuvimos un **94 % de accuracy**,
> lo que muestra que el método es adecuado para el análisis de encuadres mediáticos a gran escala."*

No dice nada más sobre datos ni evaluación.

Escribí las **tres preguntas** que le harías al autor, en el tono en que se las escribirías en
un informe de revisión (o sea: exigente y educado, no agresivo). Para cada una, agregá una
línea diciendo **qué problema estás buscando**.

*Bonus:* hay una cuarta pregunta que casi nadie hace y que después de esta clase deberías
poder formular. ¿Cuál es?

---

## 13. Tu propia investigación *(abierta, sin puntaje)*

Tomá el último conjunto de datos con el que trabajaste — el que sea, aunque no pienses usar
deep learning con él — y contestá:

**a.** ¿Tus casos son independientes, o hay una unidad que se repite (persona, medio,
provincia, sesión, hogar)?

**b.** Si quisieras hacer una afirmación **predictiva**, ¿cómo partirías los datos?

**c.** ¿Cuál sería tu **baseline tonto**, ese que hay que ganarle antes de festejar nada?

Traé la respuesta a la próxima clase. No hay respuesta correcta: hay respuestas escritas y
respuestas no escritas.
