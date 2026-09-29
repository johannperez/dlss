# Estado del curso

> Revisión del 2026-09-29, después de la ronda de arreglos de todas las clases.
> Este archivo es un **índice**: lo medido en detalle está en el `VERIFICACION.md`
> de cada clase (§0 de cada uno: qué se arregló, qué se volvió a correr y qué no).
> `00-ESTADO-ESPINA.md` es histórico (la base compartida antes de construir las clases).

## 1. Dónde está lo medido

| Clase | Verificación | Script que regenera los números |
|---|---|---|
| 01 funciones y parámetros | `clases/01-funciones-y-parametros/VERIFICACION.md` | `medir-referencias.py` |
| 02 componer funciones | `clases/02-componer-funciones/VERIFICACION.md` | el script de `notas-docente.md` §10 |
| 03 loss y gradiente | `clases/03-loss-y-gradiente/VERIFICACION.md` | (el notebook) |
| 04 entrenar de verdad | `clases/04-entrenar-de-verdad/VERIFICACION.md` | `medir-figuras.py` |
| 05 imágenes y convoluciones | `clases/05-imagenes-y-convoluciones/VERIFICACION.md` | `medir-experimentos.py` |
| 06 texto, secuencias, embeddings | `clases/06-texto-secuencias-embeddings/VERIFICACION.md` | `medir-embeddings.py` |
| 07 attention y transformer | `clases/07-attention-y-transformer/VERIFICACION.md` | `medir-atencion.py` (`--verificar`) |
| 08 mini-GPT y los LLM | `clases/08-mini-gpt-y-los-llm/VERIFICACION.md` | `entrenar-mini-gpt.py` |
| 09 modelos preentrenados | `clases/09-modelos-preentrenados/VERIFICACION.md` | `medir-clase09.py` |
| 10 criterio, validación y ética | `clases/10-criterio-validacion-y-etica/VERIFICACION.md` | `medir-clase10.py`, `exportar-figuras.py` |

Los datos compartidos están documentados en `datos/README.md`, y la biblioteca del
curso (`_shared/ssdl/`) tiene su suite: `python -m unittest _shared/ssdl/test_ssdl.py`
(121 tests).

## 2. Reglas transversales que quedaron fijadas

- **Calendario:** lunes, miércoles y viernes; plazos por número de clase, nunca por
  día ni por semana; tarea entre clases de hasta 1 h (2 h en 3→4, 6→7 y 9→10). El
  bloque de cierre se llama `[EN TU INVESTIGACIÓN]` (`PROGRAMA.md` §0.2).
- **Reproducibilidad:** todo es determinista **en la misma máquina y con las mismas
  versiones de las librerías**; con otras versiones los números cambian un poco. Los
  `datos-*.json` que lo permiten guardan las versiones con que se generaron. C7 y C8
  tienen chequeos que avisan si el momento pedagógico («aha», «Nelida Falcon») no
  apareció en la corrida propia.
- **Datos:** léxico de seguridad de 24 palabras; 36 puntos (1984-2019) y 35 discursos
  distintos (2005 = 2006); apertura el 1 de mayo hasta 1994 y el 1 de marzo desde
  1995; media móvil por años calendario; corpus de noticias en dos recolecciones
  (971 notas de ene-jul 2018, 500 de nov 2020 a mar 2021).
- **Entre clases:** 3 perillas por rampa de la red (3K+1 en total); learning rate
  como multiplicador de la pendiente; «si la tendencia de la loss sube»; softmax en
  C7; C8 entrena un mini-GPT de caracteres de 4 bloques; RoPE como posiciones de hoy;
  la RNN como mochila de tamaño fijo; C9 sólo de texto.

## 3. Cómo volver a verificar

1. Copiá el repo al scratch (`cp -R`) y trabajá sobre la copia, con
   `PYTHONDONTWRITEBYTECODE=1`. Correr notebooks dentro del repo regenera figuras
   versionadas.
2. `jupyter nbconvert --to notebook --execute` sobre cada `notebook.ipynb` de la copia.
3. Los scripts de la tabla de §1, comparando su salida con los `datos-*` versionados.
4. Las slides y las visualizaciones en Chrome sin conexión, mirando la consola.
5. En el repo, los notebooks se guardan **sin outputs** y con `execution_count` null;
   la celda de bootstrap (celda 2) es idéntica en los diez y en la plantilla.

## 4. Qué quedó abierto

1. **El repositorio tiene que ser público** (`github.com/johannperez/dlss`, rama
   `main`) para que la celda de bootstrap clone en Colab. Mientras tanto, el camino
   es subir el `.zip` (`recursos/setup.md`). No se probó en un Colab real.
2. **Licencia de los corpus de discursos:** escribirles a los recopiladores.
3. **URLs marcadas `[VERIFICAR URL]`** en las referencias (entre otras, Leshno et al.
   1993, Landis y Koch 1977, Nadeau y Bengio 2003, Eckart y Young 1936).
4. **C7:** los mapas de atención no se pueden regenerar con torch 2.14 sin perder los
   dos «aha»; no hay pesos guardados para ejecutar la intervención del TODO 5.
5. **C8:** los `datos-mini-gpt.*` publicados son la corrida del curso (torch 2.13,
   x86) y no traen `meta.versiones` ni `alucinacion.fabricacion`; si se republica con
   una corrida nueva, hay que actualizar las slides 14-18, 23 y 26 y las notas §9.
6. **Sin probar a mano:** tema oscuro, anchos angostos, iframes embebidos uno por uno,
   GPU T4 real.
