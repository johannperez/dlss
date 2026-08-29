# Figuras de la clase 10

Las cinco figuras que dibuja `notebook.ipynb`, guardadas acá para que el docente las pueda
proyectar sin abrir el notebook.

| archivo | de qué sección del notebook sale |
|---|---|
| `01-matriz-de-confusion.png` | §2 — el modelo que vamos a auditar |
| `02-terminos-influyentes.png` | §3 — qué está usando el modelo (en rojo, los nombres propios) |
| `03-ablacion-vs-ruido.png` | §5 — las ablaciones adentro de la banda de ruido de la partición |
| `04-pares-minimos.png` | §8 — qué mueve el puntaje y qué no |
| `05-sesgo-por-sujeto.png` | §9 — la misma oración, distinto sujeto (en gris, fuera de vocabulario) |

## Cómo se regeneran

```bash
python3 clases/10-criterio-validacion-y-etica/exportar-figuras.py    # ~15 s, CPU, sin red
```

Ese script **no copia el código del notebook: lo corre**. Lee `notebook.ipynb`, ejecuta sus
celdas en orden y guarda cada figura que aparece. Por eso es imposible que estos PNG digan
una cosa y el notebook otra — que es exactamente el problema del que habla la clase.

Si cambiás el notebook, corré también `medir-clase10.py`: de ahí salen los números que citan
las slides y las visualizaciones.
