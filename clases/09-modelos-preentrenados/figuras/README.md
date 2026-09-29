# Figuras de la clase 9

**Estas tres las genera el notebook al correr.** No se editan a mano: si cambiás algo del
notebook, se regeneran solas la próxima vez que lo corras entero. Por eso conviene correrlo
sobre una copia del repo (o en Colab, que es un clon): adentro del repo las pisa, y aunque
el contenido sea el mismo, los bytes cambian (metadatos de matplotlib).

Están versionadas por una sola razón: para que quien prepare la clase pueda ver **qué
tiene que salir** sin tener que correr nada, y darse cuenta rápido si algo cambió.

| archivo | de qué celda sale | qué muestra |
|---|---|---|
| `matriz-de-confusion.png` | sección 5, `reportar()` | 214 / 51 / 29 / 74 · precisión 59 % · recall 72 % · F1 0,65 |
| `curva-de-etiquetas.png` | sección 8 | las dos curvas medidas + la línea del diccionario en 0,40 |
| `umbral.png` | sección 9 | precisión, recall y F1 **en validación** (validación cruzada sobre train); el F1 máximo en umbral 0,50 |

Todas salen de la tarea **«¿es una nota sobre política?»** sobre el corpus de prensa del
curso (1471 notas reales), con la semilla 1983 y el camino offline (PPMI+SVD, camino B).
Con Hugging Face (camino A) los números son **otros, no necesariamente mejores**: medido
el 28-09-2026, la matriz da precisión 56 % y recall 78 % con el mismo F1 0,65; la curva de
embeddings arranca más arriba (0,53 con 25 etiquetas); el umbral elegido en validación es
0,55. La tabla completa está en `notas-docente.md` §10.
