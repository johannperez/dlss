# Figuras de la clase 9

**Estas tres las genera el notebook al correr.** No se editan a mano: si cambiás algo del
notebook, se regeneran solas la próxima vez que lo corras entero.

Están versionadas por una sola razón: para que quien prepare la clase pueda ver **qué
tiene que salir** sin tener que correr nada, y darse cuenta rápido si algo cambió.

| archivo | de qué celda sale | qué muestra |
|---|---|---|
| `matriz-de-confusion.png` | sección 5, `reportar()` | 214 / 51 / 29 / 74 · precisión 59 % · recall 72 % · F1 0,65 |
| `curva-de-etiquetas.png` | sección 8 | las dos curvas medidas + la línea del diccionario en 0,40 |
| `umbral.png` | sección 9 | precisión y recall cruzándose; el F1 máximo en umbral 0,40 |

Todas salen de la tarea **«¿es una nota sobre política?»** sobre el corpus de prensa del
curso (1471 notas reales), con la semilla 1983 y el camino offline (PPMI+SVD).
Con Hugging Face disponible los números son otros —mejores— y hay que actualizarlos.
