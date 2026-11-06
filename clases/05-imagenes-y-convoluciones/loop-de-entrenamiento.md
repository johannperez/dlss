# El loop de entrenamiento en PyTorch

**Son cinco líneas. Son las mismas en la clase 4 y en la clase 5, con una red
densa o con una CNN.**

---

## Las cinco líneas

```python
prediccion = modelo(x)            # 1. PREDECIR
perdida = criterio(prediccion, y) # 2. COMPARAR
optimizador.zero_grad()           # 3. BORRAR
perdida.backward()                # 4. ANOTAR
optimizador.step()                # 5. MOVER
```

| estación | qué hace | ¿cambian las perillas? |
|---|---|---|
| **1. Predecir** | Pasa los datos por el modelo. | no |
| **2. Comparar** | Resume en un número qué tan mal le fue. Esa es la loss. | no |
| **3. Borrar** | Borra las pendientes de la vuelta anterior. Si no, se acumulan. | no |
| **4. Anotar** | Calcula la pendiente de la loss respecto de cada perilla. | no |
| **5. Mover** | Mueve cada perilla en contra de su pendiente. | **sí, recién acá** |

---

## Lo que hay que preparar antes

```python
modelo = RedDensa().to(device)                               # la máquina, en su lugar
criterio = nn.CrossEntropyLoss()                             # qué es "estar mal"
optimizador = torch.optim.Adam(modelo.parameters(), lr=1e-3) # cómo moverse
```

- **La loss depende del problema.** Para predecir un número, `nn.MSELoss` (clase
  4). Para elegir entre clases, `nn.CrossEntropyLoss` (clase 5), que recibe los
  puntajes crudos: no hay que aplicarles `softmax` antes.
- **El optimizador recibe las perillas.** Por eso `step()` y `zero_grad()` no
  necesitan que les digas sobre qué trabajar.
- **Primero `.to(device)`, después el optimizador.** Es el orden que usa el
  notebook.

---

## El loop completo, con lotes y validación

Esta es la forma que vas a ver en casi cualquier tutorial. Las cinco líneas están
en el medio; lo demás las rodea.

```python
for epoca in range(epocas):

    # --- entrenar: se mueven las perillas ---------------------------
    modelo.train()
    for x, y in cargador_train:               # un lote por vuelta
        x, y = x.to(device), y.to(device)     # al mismo lugar que el modelo

        prediccion = modelo(x)                # 1. PREDECIR
        perdida = criterio(prediccion, y)     # 2. COMPARAR
        optimizador.zero_grad()               # 3. BORRAR
        perdida.backward()                    # 4. ANOTAR
        optimizador.step()                    # 5. MOVER

    # --- medir: sólo miramos ----------------------------------------
    modelo.eval()
    suma, aciertos = 0.0, 0
    with torch.no_grad():
        for x, y in cargador_val:
            x, y = x.to(device), y.to(device)
            prediccion = modelo(x)
            suma += criterio(prediccion, y).item() * len(y)
            aciertos += (prediccion.argmax(dim=1) == y).sum().item()

    n = len(cargador_val.dataset)
    print(f"época {epoca}: loss val {suma / n:.3f}, aciertos {100 * aciertos / n:.1f} %")
```

---

## Qué agrega cada pieza

| pieza | para qué está |
|---|---|
| `for x, y in cargador_train` | El `DataLoader` reparte los datos en lotes. Hay **un paso por lote**, no uno por época. |
| `x.to(device), y.to(device)` | Los datos tienen que estar donde está el modelo (CPU o GPU). |
| `modelo.train()` / `modelo.eval()` | Avisan si estamos entrenando o midiendo. Importa en capas como `Dropout`, que se comportan distinto en cada modo. |
| `with torch.no_grad():` | No registra las cuentas: es más rápido y gasta menos memoria. |
| `.item()` | Saca el número del tensor. Sin esto, acumularías tensores en vez de números. |
| `* len(y)` | Pondera por el tamaño del lote, porque el último puede ser más chico. |

**La diferencia con la clase 4.** Allá cada época usaba todos los datos de una vez:
un paso por época. En MNIST, con 50.000 fotos de entrenamiento y lotes de 64, cada
época da **782 pasos**.

---

## Tres confusiones comunes

1. **`eval()` y `no_grad()` no son lo mismo, y se usan juntas.** `eval()` cambia
   cómo se comportan algunas capas, pero PyTorch sigue registrando las cuentas.
   `no_grad()` deja de registrarlas, pero no cambia el comportamiento de las capas.
2. **`backward()` no entrena.** Sólo anota pendientes. Si te olvidás de `step()`,
   el modelo no cambia nunca, y no hay ningún error que te avise.
3. **`zero_grad()` puede ir en otro lugar.** Muchos tutoriales lo ponen al principio
   de la vuelta. Da lo mismo: lo que importa es que esté antes de `backward()`.

---

## Cómo saber que anda

- **La loss de entrenamiento baja.** Si sube, probá dividir el `lr` por 10.
- **La loss de validación también baja.** Si la de entrenamiento baja y la de
  validación sube, el modelo está memorizando (clase 4).

---

## Para leer más

- Tutorial: [*Optimizing Model Parameters*](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- En el notebook de esta clase: `entrenar_una_epoca`, `evaluar` y `entrenar`, en la sección 2
