# Figuras de la clase 10

Las cinco figuras que dibuja `notebook.ipynb`, guardadas acá para que el docente las pueda
proyectar sin abrir el notebook.

| archivo | de qué sección del notebook sale |
|---|---|
| `01-matriz-de-confusion.png` | §2 — el modelo que vamos a auditar |
| `02-terminos-influyentes.png` | §3 — qué está usando el modelo (en rojo, rayados y con ★, los nombres propios) |
| `03-ablacion-vs-ruido.png` | §5 — cada ablación repetida en 25 particiones: la diferencia pareada de F1, con su media ± 2 EE, y lo que decía una sola partición |
| `04-pares-minimos.png` | §8 — qué mueve el puntaje y qué no (línea llena y roja: se movió más de 0,15) |
| `05-sesgo-por-sujeto.png` | §9 — la misma oración, distinto sujeto (en gris, rayado y con «(?)», fuera de vocabulario) |

## Cómo se regeneran

```bash
python3 clases/10-criterio-validacion-y-etica/exportar-figuras.py    # ~15 s, CPU, sin red
```

Ese script **no copia el código del notebook: lo corre**. Lee `notebook.ipynb`, ejecuta sus
celdas en orden y guarda cada figura que aparece. Por eso es imposible que estos PNG digan
una cosa y el notebook otra — que es exactamente el problema del que habla la clase.

Los PNG salen iguales en corridas sucesivas **en la misma máquina y con las mismas
versiones** (matplotlib incluida). Con otra versión los bytes cambian aunque el dibujo sea
el mismo: compará mirando, no con `md5sum`.

Si cambiás el notebook, corré también `medir-clase10.py`: de ahí salen los números que citan
las slides y las visualizaciones.
