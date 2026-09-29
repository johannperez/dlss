# Clase 4 — Notas para quien da la clase

**El ciclo de entrenamiento, y la diferencia entre dibujar y calcar**
120 minutos · cierre del módulo 1 · prerrequisitos: clases 1 a 3

---

## 1. El arco narrativo en diez líneas

1. El aula vota mal a propósito: elige el modelo que acierta el 99 % y no sirve para nada.
2. Se nombra el enemigo del día: **sobreajuste**, y se dice que está en papers publicados.
3. Se conectan las tres clases anteriores en un mecanismo: **el ciclo de cinco estaciones**.
4. Se desarma la confusión número uno con la viz: **`backward` anota, `step` mueve**.
5. Practican. Escriben el loop, comprueban que `nn.Sequential` no esconde nada, y suben
   la capacidad hasta ver que la loss de entrenamiento **tiende** a bajar (con algún saltito).
6. Pausa. Vuelven con la trampa servida en bandeja: "baja, baja, baja, ¿le pongo 4000?".
7. **El calco**: 200 rampas que pasan por todos los puntos y erran los cinco que no vieron.
8. La única defensa: apartar datos. Train / validación / test, y la **tijera**.
9. **La escena**: en nuestros propios datos, 2005 y 2006 son el mismo discurso, la partición
   al azar los repartió a los dos lados, y el número que sale es 2,2 veces mejor que el honesto.
10. Cierre del módulo: perilla → composición → loss → ciclo. *"Esto es todo el deep learning."*

**Si te llevás una sola frase para repetir**: *dibujar es capturar la forma; calcar es copiar
cada manchita del original, incluidas las que son suciedad del papel.*

---

## 2. Plan de tiempos real, bloque por bloque

| Min | Slides | Bloque | Qué hacés |
|---|---|---|---|
| **0-1** | 1 | Portada | Una frase y pasás. No leas objetivos. |
| **1-5** | 2 | **Votación A vs B** | Contás los votos en voz alta y los anotás en el pizarrón. |
| **5-8** | 3 | La revelación | Mostrás la segunda fila y te callás cinco segundos. |
| **8-10** | 4 | El error de hoy | Prometés algo concreto. |
| **10-12** | 5 | Dónde quedamos | Dos minutos, no más. |
| **12-15** | 6 | El ciclo | Recorrés el círculo dos veces. Plantás la pregunta. |
| **15-20** | 7 | **VIZ anatomía** | Cinco clics de «una estación», narrando. Cerrás la pregunta. |
| **20-28** | 8-13 | Las cinco líneas | Media slide por línea. **Acá se atrasa todo el mundo.** |
| **28-30** | 14-15 | Tensor y vocabulario | Rápido. Es referencia, no contenido. |
| **30-50** | 16 | **Práctico 1** | Notebook secciones 1-4. Pasás por las mesas. |
| **50-60** | 17 | **PAUSA** | Diez minutos. **No se toca.** |
| **60-63** | 18 | El reencuentro | Le das aire. Es el pago emocional del módulo. |
| **63-65** | 19 | Más neuronas | Leés los números con entusiasmo y hacés la pregunta trampa. |
| **65-71** | 20-21 | **El calco** | La escena central de la primera mitad. |
| **71-73** | 22 | Ya conocen esto | Pedís ejemplos de su disciplina. |
| **73-78** | 23-24 | Partición + apuesta | La torta, y la votación antes de la viz. |
| **78-84** | 25 | **VIZ sobreajuste** | Capacidad despacio, y «otra muestra» cinco veces. |
| **84-88** | 26-27 | La tijera y early stopping | La radiografía y la consecuencia. |
| **88-91** | 28-29 | Más datos / otras defensas | La 29 va en un minuto, y es lo primero que se recorta. |
| **91-103** | 30 | **Práctico 2** | Partición, tijera, TODO 4. |
| **103-105** | 31 | Puesta en común | Dos personas, las que se equivocaron. |
| **105-108** | 32-33 | Regla de oro y fuga | El test una vez; partir al azar cuándo no. |
| **108-114** | 34-35 | **VIZ partición + 2005/2006** | **La mejor escena de la clase. No la apures.** |
| **114-120** | 36-40 | Cierre | En tu investigación (escriben las tres preguntas), glosario, tres ideas, módulo, puente. |

> El práctico 2 tiene 12 minutos. Es a propósito: **la escena de 2005/2006 no se puede
> recortar** y el cierre necesita sus seis minutos (antes tenía dos, y la slide 38 se leía a
> las corridas). El experimento de a dos (sección 7 del notebook, unos diez minutos) se
> termina antes de la clase 5. Si tu grupo es rápido, dale al práctico hasta el minuto 105
> y achicá la puesta en común.

---

## 3. Qué preguntar al aula, y cuándo

| Momento | La pregunta | Para qué |
|---|---|---|
| Slide 2 | **"¿A o B? Voten."** | Que se equivoquen en público y sin costo. Es el motor de toda la clase. |
| Slide 2 | "¿Por qué elegiste A?" | Que digan en voz alta "porque acierta más". Esa frase vuelve en la slide 25. |
| Slide 6 | "¿En qué estación exactamente se mueven las perillas?" | Que lo anoten. Se cobra en la slide 7. |
| Slide 7 | "¿Quién había anotado *backward*?" | Manos arriba, risas, confusión desarmada. |
| Slide 19 | "¿Entonces le pongo 4000?" | Que alguien diga "no" y **no lo corrijas**: su razón es tu material. |
| Slide 22 | "¿Cómo se llama esto en su disciplina?" | Que la clase deje de ser "de computación". |
| Slide 24 | **"¿Qué le pasa a la loss de entrenamiento?"** | Sin esta apuesta, la viz de sobreajuste es decoración. |
| Slide 26 | "¿En qué época habrías parado?" | Que señalen la pantalla. Es el ítem 3 del cuestionario. |
| Slide 31 | "¿A quién le dio distinto de lo que esperaba?" | Los errores son el contenido. |
| Slide 33 | "¿Sus casos son independientes?" | La pregunta que se llevan escrita. |

---

## 4. Las respuestas típicas y cómo usarlas

**"Elijo A porque acierta más."**
Perfecto, y no es ingenuo: es exactamente lo que hace un modelo cuando elige por la loss de
entrenamiento. Guardá la frase y devolvésela en la slide 25: *"la curva azul piensa igual
que ustedes hace cuarenta minutos"*.

**"Se aprendió los datos de memoria" (alguien lo dice solo, en la slide 3).**
Regalo. Pedile que lo diga más fuerte y escribilo en el pizarrón. Toda la clase queda
colgada de esa frase.

**"¿Entonces le pongo 4000?" → "No, porque se sobreajusta."**
Alguien que ya leyó. **No lo dejes resolver la clase.** Contestá: *"¿y cómo te darías
cuenta, mirando sólo los números que tenés?"* — no puede. Ahí está el punto: no es que la
solución sea difícil, es que **el problema es invisible sin datos apartados**.

**"¿Entonces con más neuronas siempre es peor?"**
No. Y hay que decirlo o después se sienten estafados. La regla es la **relación capacidad /
datos**. En la viz: capacidad 60 con 25 casos es un escándalo; capacidad 60 con 300 casos
está bien. Por eso los modelos gigantes funcionan: tienen datos gigantes.

**"En mi disciplina eso se llama…"**
Anotalo. Aparecen siempre dos o tres buenos: el índice construido y validado con la misma
muestra, la tipología derivada de los mismos casos que después clasifica, el modelo con
tantos controles que el R² no significa nada.

**"¿Y si me da mal el test?"**
Lo reportás. Y si querés seguir probando, o conseguís datos nuevos o decís cuántas
configuraciones probaste. Las dos son aceptables; esconderlo no.

---

## 5. Confusiones de principiante y cómo desarmarlas

| Confusión | Cómo se manifiesta | Cómo la desarmás |
|---|---|---|
| **`backward` mueve las perillas** | "Ah, entonces ahí se entrena" | Viz de anatomía, parando en ANOTAR: los gradientes aparecen y las perillas **no cambian**. Treinta segundos, en vivo. |
| **Más capacidad siempre es mejor** | Es la intuición por defecto, reforzada por el marketing de los modelos grandes | Viz de sobreajuste + «otra muestra» ×5. Y **el matiz honesto** (ver arriba). |
| **"La loss de entrenamiento baja siempre, es una ley"** | Aparece al revés en el TODO 2, si 256 da un poco más que 64 | *Tiende* a bajar: con un número fijo de épocas el entrenamiento no siempre llega al fondo. No sube de forma sistemática, y por eso no avisa nada. (En la viz de sobreajuste la azul no sube porque cada modelo contiene al anterior y se resuelve exacto.) |
| **Olvidarse `zero_grad()`** | La loss hace cosas raras y no saben por qué | Anticipado en la slide 11. Contá tu propia vez. Es un rito de iniciación, no un fracaso. |
| **Confundir epoch con iteración** | "Entrené 1000 iteraciones" queriendo decir epochs | Slide 15 con el ejemplo numérico. Hoy son lo mismo (36 casos, un solo lote) y lo decís. |
| **"La validación mide qué tan bueno es el modelo"** | Reportan el número de validación como resultado | *"Validación es para **decidir**. Test es para **reportar**. Si decidiste con un número, ese número ya no te sirve para reportar."* |
| **Mirar el test varias veces** | "Probé cinco configuraciones y me quedé con la mejor en test" | El paralelo con el **p-hacking**, dicho con esas palabras. Esta audiencia lo entiende de inmediato. |
| **Partir al azar datos temporales o de panel** | El más frecuente y el más difícil de ver | Viz de partición + los 36 discursos. La pregunta operativa: *"al predecir un caso del test, ¿el modelo usa información que en la vida real no habría tenido todavía?"* |
| **"El modelo entendió"** | Atribución de comprensión cuando ajusta bien | La curva de 200 rampas: ajuste perfecto y erra los cinco años nuevos. La evidencia visual alcanza. |
| **"¿Cuántos epochs hay que hacer?"** | Buscan una regla | *"Hasta que la validación deje de mejorar. La respuesta la da el gráfico, no una tabla."* |
| **Pánico ante `nn.Sequential`** | "Apareció magia nueva" | La celda del notebook con la red escrita a mano al lado y el chequeo que da ✓. Corré esa celda vos, en la pantalla grande, si hace falta. |
| **"Mi n es 40, entonces no puedo hacer nada"** | Desánimo, y es legítimo | Sí podés: podés hacer un modelo chico, partir honestamente y **reportar que no le ganás al baseline**. Eso es buen trabajo. Lo que no podés es entrenar un modelo grande y publicar el número de entrenamiento. |

---

## 6. Si vas atrasado

**Se recorta, en este orden:**

1. **Slide 29** (las otras defensas: regularización, dropout, augmentation). Entera. Se
   menciona en una frase: *"hay tres técnicas más para lo mismo; están en las referencias
   (Goodfellow et al., capítulo 7)"*. El notebook no las usa.
2. **Slides 9-13** (una línea de PyTorch por slide). Se hacen de corrido sobre la slide 8,
   señalando con el dedo. Ahorra cuatro minutos.
3. **Slide 14** (tensores). Una frase: *"un tensor es una tabla de números, nada más"*.
4. **Slide 31** (puesta en común) baja de tres personas a una.
5. El **experimento libre** del práctico 2 se termina antes de la clase 5. El notebook ya
   está preparado para eso.

**NUNCA se recorta:**

- **La pausa.** Si la comés, la segunda mitad se atropella y la segunda mitad es la que importa.
- **La votación de la slide 2** y **la apuesta de la slide 24.** Sin la predicción fallida,
  las dos vizes son dibujitos lindos.
- **La escena de 2005/2006** (slides 34-35). Es el momento en que el curso deja de ser una
  clase de programación.
- **El cierre del módulo** (slide 39). Mucha gente cree, a esta altura, que todavía le falta
  lo importante. Decirle que no le falta cambia cómo entra a la clase 5.

## 7. Si vas adelantado

- Abrí la viz de sobreajuste y **dejala en manos del aula**: que alguien venga a mover los
  sliders y explique en voz alta qué está mirando. Cinco minutos bien gastados.
- Corré **en vivo** la celda opcional sin `zero_grad()` (después del TODO 3). La loss no se
  asienta: oscila entre ~0.02 y ~0.06, se pasa de largo y vuelve. Aprender el bug
  produciéndolo vale más que la slide 11.
- Poné la viz de partición en «120 titulares» + «por tiempo» y preguntá por qué siguen
  quedando fugas de grupo. (Respuesta: cada diario publica todos los años, así que partir por
  tiempo no separa diarios. Hay problemas que necesitan **las dos** particiones a la vez.)
- Discutan un paper que hayan traído: *¿dice cómo partió los datos?* Casi nunca dice.

---

## 8. Chistes y analogías que funcionan

- **El calco con la mancha de café.** Dibujá una carita en el pizarrón, ponele una mancha al
  lado, y pedí que la calquen. *"¿Copian la mancha? No. El modelo sí. Para el modelo, la
  mancha y la boca son exactamente lo mismo."*
- **`zero_grad`.** *"Esta es la línea que todos se olvidan. Yo también me la olvido, todavía."*
  Contá tu propia versión. Que se rían ahora es que no se frustren después.
- **El ciclo aburrido.** *"Sí, es aburridísimo: millones de veces lo mismo. Por eso lo hace
  una computadora y no ustedes."*
- **El test es el preregistro.** La analogía más potente de la clase para esta audiencia.
  Usala tal cual: *"el conjunto de test es el preregistro del aprendizaje automático"*.
- **El codificador malacostumbrado.** *"Todos conocemos a alguien que se entrenó con el corpus
  piloto y quedó convencido de que cuando dice «compañeros» es peronismo."*
- **Dentro y fuera de la muestra.** *"El sobreajuste es ajuste perfecto dentro de la muestra
  y capacidad predictiva nula fuera de ella: no replica ni en otra muestra de la misma
  población."* Después de esa frase, media clase entiende el resto sola. **No** lo digas como
  "validez interna contra externa": para esta audiencia esas palabras son identificación causal
  y generalizar a otras poblaciones, y alguien lo va a objetar con razón.
- **La escala.** Cuando alguien diga "pero GPT tiene millones de parámetros":
  *"y millones de textos. Vos tenés 36 discursos. Es la relación, no el número."*

---

## 9. Si te preguntan X

**1. "Si el sobreajuste es tan obvio, ¿por qué está en papers publicados?"**
Porque no es obvio: **la loss de entrenamiento se ve idéntica en los dos casos**. Sin datos
apartados no hay señal de alarma; el modelo no avisa. Y porque el incentivo empuja para el
otro lado: un número más alto es más publicable. Kapoor & Narayanan (2023) catalogaron
tipos de fuga en cientos de papers de ciencia aplicada; no son descuidos de gente distraída,
son errores sistemáticos que la revisión por pares no está entrenada para detectar.

**2. "Mi n es 40 casos. ¿Esto no me sirve para nada, entonces?"**
Te sirve para **saber que no te sirve**, que es muchísimo. Con 40 casos, un modelo flexible
va a calcar; podés (a) usar un modelo chico y reportarlo honestamente contra un baseline,
(b) usar validación cruzada en vez de una partición fija — la idea es la misma, repetida
varias veces —, o (c) usar deep learning como **instrumento de medición** (por ejemplo, un
modelo pre-entrenado que codifica tus textos) y hacer la inferencia con las herramientas de
siempre. Esa tercera opción es la clase 9 y probablemente sea la respuesta para la mayoría
del aula.

**3. "¿No es hacer trampa elegir el modelo con la validación? También estás mirando datos."**
Sí, y por eso hacen falta tres montones. La validación **se contamina** cada vez que la usás
para decidir; el test se mantiene limpio porque no se toca. Y sí: si probás doscientas
configuraciones, hasta el test empieza a contaminarse por selección. La respuesta profesional
es reportar cuántas configuraciones probaste. No hay pureza, hay contabilidad honesta.

**4. "¿Cuánto tengo que apartar? ¿20 %? ¿30 %?"**
No hay número mágico y desconfiá de quien te lo dé. Lo que importa es que el test tenga
**suficientes casos para que su número signifique algo**: con 7 casos de test, cambiar un
acierto mueve el resultado 14 puntos. Con muestras chicas, validación cruzada. Y siempre:
reportá **cuántos casos** tiene tu test, no sólo el porcentaje. En esta clase el test honesto
por grupo queda con 4 discursos, y decirlo en voz alta es parte de la lección.

**5. "Esto que hicimos hoy, ¿es lo que hace ChatGPT?"**
El ciclo, sí: exactamente estas cinco líneas, con muchísimos más datos, muchísimas más
perillas y una arquitectura distinta (clases 7 y 8). Y el sobreajuste también existe ahí, con
otra cara: se llama **memorización** y es la razón por la que a veces un modelo grande
reproduce textual un párrafo de su corpus. La diferencia no es de naturaleza, es de escala —
y la escala hace que la relación capacidad/datos les juegue a favor, no en contra.

**6 (bonus). "¿Por qué la red no le gana al baseline en el notebook? ¿Está mal hecho?"**
No. Está bien hecho y el resultado es negativo, que es distinto. Con 36 observaciones y una
serie ruidosa, predecir el promedio es difícil de superar. Que el notebook de una clase
termine en un resultado negativo bien reportado es deliberado: es el estándar que le pedimos
a los demás, y sería incoherente no aplicárnoslo.

---

## 10. Preparativos antes de entrar al aula

- [ ] Abrí `slides.html` y probá que las tres vizes embebidas cargan (no hay internet en el aula).
- [ ] Abrí `viz/anatomia-del-loop.html` **suelta** en otra pestaña: la vas a proyectar más grande.
- [ ] Corré el notebook entero una vez, con tu máquina, para que el kernel esté caliente y
      sepas cuánto tarda ahí (acá tardó entre 5 y 30 s según la máquina).
- [ ] **Compará tus números con los de las slides.** Las slides leen `datos-figuras.js`, que
      se generó con torch 2.14 (las versiones quedan anotadas en ese archivo). Todo es
      determinista en la misma máquina y con las mismas versiones; con otras, los números
      cambian un poco, sobre todo el par 64/256 del TODO 2 y el calco de la slide 20. Si los
      tuyos no coinciden, proyectá los tuyos y decilo en voz alta: es un anticipo de la
      clase 10. Si querés que las slides muestren tu corrida, corré `medir-figuras.py`.
- [ ] Tené a mano la foto o la captura del **ajuste a ojo de la clase 1**, si la guardaste.
      La slide 18 la reproduce, pero la de ellos es mejor.
- [ ] Pizarrón o papelógrafo para anotar los votos de la slide 2 y los números del TODO 2.
