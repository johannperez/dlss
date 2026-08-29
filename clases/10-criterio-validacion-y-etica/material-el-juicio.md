# El juicio — material para repartir

> ### ⚠ MATERIAL DIDÁCTICO. LOS DOS «PAPERS» SON FICTICIOS.
>
> **No existen.** No hay autores, no hay revista, no hay datos: están escritos para esta
> clase, a mano, con los errores puestos a propósito. Ninguna cifra de estas dos páginas
> describe el mundo, y **ninguna se puede citar**. Se reparten impresos, sin nombres, para
> que la discusión sea sobre el método y no sobre quién lo firma.
>
> Los números **sí** son internamente coherentes: si un grupo los revisa con cuidado, las
> cuentas cierran o no cierran por las razones que la clase enseñó, no por descuido de quien
> los escribió.

**Cómo se usa.** Son dos. **Se reparte uno solo por cohorte** y el otro queda para la vez
siguiente, así la actividad se puede repetir con otro grupo sin que corra el boca a boca.
El **A** es defendible con reparos; el **B** tiene un problema fatal de validez. Si tenés
un aula grande y querés partirla en cuatro, podés dar los dos a la vez y comparar veredictos:
es más caótico y más divertido.

- **15 min** (12 si vas justo): la mitad del aula prepara **la defensa**, la otra mitad
  **la revisión**. Los dos bandos usan el mismo checklist (slide 34 / `viz/checklist-revisor.html`).
- **10 min** (8 si vas justo): audiencia. El docente modera y anota las objeciones en el pizarrón.
- Al final, **slide 32**: se ordenan las objeciones en dos columnas, *fatal* y *menor*.

---

## PAPER A — «Un índice automático de conflictividad en la prensa provincial»

*(resumen extendido de un trabajo ficticio, escrito para esta clase)*

**Pregunta.** ¿Aumentó la cobertura de conflicto social en la prensa de una provincia entre
2016 y 2023, y ese aumento acompaña a los ciclos de protesta registrados?

**Datos.** 41.200 notas de las secciones «Política» y «Sociedad» de cuatro diarios
provinciales, bajadas de sus sitios entre marzo y mayo de 2024. Se excluyeron 3.100 notas
que el sitio devolvió sin cuerpo (7,0 %); el anexo A muestra que esas notas se reparten
parejo por año y por diario. El corpus, los identificadores y el código están en un
repositorio público con DOI.

**Medida.** Un clasificador binario «la nota informa un episodio de conflicto colectivo».
La definición operativa es explícita: *hay conflicto colectivo si la nota informa una acción
de un colectivo identificable —paro, movilización, corte, toma, olla popular— con un
destinatario identificable*. Dos codificadores etiquetaron **600 notas** siguiendo esa regla;
el acuerdo fue **kappa de Cohen = 0,71** y los desacuerdos se resolvieron discutiendo.
Con esas 600 se ajustó una regresión logística sobre bolsa de palabras (bigramas, mínimo 5
apariciones) y se aplicó al resto.

**Evaluación.** Partición **por diario y por año** (se entrena con tres diarios y se prueba
en el cuarto, rotando). Sobre las 150 notas de test: precisión 0,79, recall 0,74, F1 0,76.
Piso: decir siempre «no hay conflicto» acierta 0,81 de *accuracy* (la prevalencia es 19 %),
y el modelo llega a 0,90. Repitiendo la partición con 30 semillas, el F1 va de **0,71 a 0,80**.
Se leyeron los 32 falsos positivos: 19 son notas deportivas con vocabulario de enfrentamiento
(«marcha», «choque», «reclamo»), 8 son conflictos internos de partidos —que la definición
excluye a propósito— y 5 son desacuerdos genuinos entre los codificadores. Se reportan los
20 términos de mayor peso; ninguno es un nombre propio ni un nombre de diario.

**Validación externa.** La serie mensual del índice se contrasta con el registro de conflictos
laborales que publica el ministerio de trabajo provincial: correlación de 0,63, y los tres
picos del registro oficial aparecen en el índice con un mes de desfasaje.

**Resultado.** El índice sube 38 % entre 2016 y 2023. La banda de las 30 semillas no explica
un movimiento de ese tamaño.

**Lo que el paper NO dice.** No hay auditoría por subgrupo. No se justifica el umbral de 0,5.
No se informa qué versión de la biblioteca se usó. Y la conclusión final del artículo dice:
*«la prensa provincial amplificó el conflicto social del período»*.

---

## PAPER B — «Midiendo populismo en el discurso legislativo con un modelo de lenguaje»

*(resumen extendido de un trabajo ficticio, escrito para esta clase)*

**Pregunta.** ¿Creció el populismo en los discursos de la cámara baja entre 2011 y 2023?

**Datos.** 128.000 intervenciones taquigráficas. No se informa cómo se obtuvieron ni qué
período cubre cada fuente; el repositorio «estará disponible a pedido».

**Medida.** Se le pidió a un modelo de lenguaje comercial, vía API, que puntuara cada
intervención de 0 a 100 en «populismo», con la instrucción: *«¿Qué tan populista es este
discurso? Respondé con un número»*. El prompt exacto no está en el apéndice. El modelo se
nombra por su familia, sin versión ni fecha de corrida. No hay definición operativa de
populismo: el artículo remite a «la literatura».

**Evaluación.** El modelo alcanza **94 % de exactitud** en una tarea de validación en la que
se le pidió distinguir 200 discursos «de líderes ampliamente reconocidos como populistas» de
200 discursos «de líderes tecnocráticos», seleccionados por los autores. No se reporta
prevalencia, ni precisión, ni recall, ni piso. No hubo codificación humana de las
intervenciones: «la coincidencia con el juicio experto se considera establecida por el 94 %».

**Resultado.** El puntaje medio sube de 31 a 47 puntos entre 2011 y 2023 (+52 %). La serie
tiene un salto de 9 puntos entre febrero y marzo de 2021.

**Discusión del artículo.** *«El populismo legislativo creció de manera sostenida. La magnitud
del cambio sugiere una transformación del estilo de representación política.»* Se recomienda
el índice como insumo para observatorios de calidad democrática.

**Dato que el artículo menciona al pasar, en una nota al pie.** Las taquigráficas cambiaron de
proveedor de transcripción en **febrero de 2021**; el formato nuevo conserva las
interrupciones y los aplausos, que antes se borraban.

---

## Para el docente — dónde está cada cosa

**No leas esto en voz alta antes de la actividad.** Es para moderar, y para que el veredicto
de la slide 32 no dependa de tu memoria.

### Paper A — defendible, con reparos menores

| objeción | gravedad | por qué |
|---|---|---|
| No hay auditoría por subgrupo | **menor** | El índice describe un corpus, no decide sobre personas. Se pide, no se exige. |
| El umbral 0,5 no se justifica | **menor** | Se arregla con un párrafo y un análisis de sensibilidad. |
| Falta la versión de la biblioteca | **menor** | Se arregla escribiendo. |
| «La prensa amplificó el conflicto» | **serio, y se arregla escribiendo** | Es un salto de la medida a una afirmación causal sobre el efecto de la prensa. La medida sostiene «subió la cobertura», no «amplificó». Reformular la conclusión alcanza. |
| El 7 % excluido | **menor, ya contestado** | Está declarado y hay evidencia de que no se correlaciona con el año ni con el diario. |

**Lo que la defensa tiene que saber usar:** partición por diario y por año (no hay fuga),
600 casos codificados con kappa reportado, banda de 30 semillas, análisis de los 32 falsos
positivos, y validación externa contra un registro independiente. **Ese conjunto es más de lo
que hace el 95 % de los papers**, y decirlo es una jugada legítima.

**La trampa para los revisores:** hay tentación de marcar como fatal la falta de auditoría por
subgrupo. No lo es acá, y explicar por qué —*mide, no decide*— es exactamente la distinción de
la slide 25.

### Paper B — fatal

| objeción | gravedad | por qué |
|---|---|---|
| **El salto de 2021 coincide con el cambio de transcripción** | **FATAL** | El confusor está en el propio artículo, en una nota al pie. El instrumento cambió en el mismo mes que el resultado. Es el caso 2 de la VIZ 1 con otra ropa. |
| **El constructo no está definido** | **FATAL** | «Remite a la literatura» no es una definición operativa. Sin ella no hay nada que validar. |
| **La «validación» del 94 % no valida nada** | **FATAL** | Distinguir populistas famosos de tecnócratas famosos es una tarea distinta —y mucho más fácil— que puntuar una intervención cualquiera. Además el conjunto lo eligieron los autores. |
| **Cero codificación humana de las intervenciones** | **FATAL** | El 94 % mide acuerdo con la selección de los propios autores. |
| **Modelo cerrado, sin versión, sin prompt, sin fecha** | **FATAL** | El resultado no se puede reproducir ni hoy. Slide 28. |
| No hay piso, ni prevalencia, ni precisión/recall | fatal por acumulación | Un puntaje continuo reportado sólo como media no permite juzgar nada. |
| Datos «a pedido» | menor | Malo, pero se arregla. |

**Lo que la defensa puede hacer honestamente:** no defender el hallazgo. La jugada fuerte es
proponer qué habría que hacer para salvarlo —definir el constructo, codificar a mano una
muestra estratificada por año, y **volver a correr todo sobre las transcripciones viejas
re-procesadas con el formato nuevo**, que es el único test que separa el instrumento del
fenómeno. Si un grupo llega solo a esa propuesta, la actividad salió perfecta.

**La trampa para la defensa:** el reflejo de decir «pero el modelo es del estado del arte».
Es irrelevante y conviene dejar que lo digan: la respuesta —*«un modelo mejor encuentra el
mismo atajo más rápido»*— es la slide 6.

### Cómo cerrar

Escribí en el pizarrón las objeciones tal como salen y ordenalas con el aula en las dos
columnas de la slide 32. **La pregunta con la que se cierra no es «¿está bien o está mal?»
sino «¿qué habría que hacer, y cuánto cuesta?».** Un revisor que sólo sabe rechazar sirve
para la mitad del trabajo.
