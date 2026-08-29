# Clase 3 — Para seguir

**Estar equivocado es un número, y ese número tiene pendiente**

Nada de esto es obligatorio. Está ordenado por **para qué te sirve**, no por importancia
académica.

## Cómo leer las marcas

| Marca | Qué quiere decir |
|---|---|
| `[VERIFICADA]` | Se abrió la URL desde este entorno y respondió. Se anota con qué. |
| `[VERIFICAR URL]` | La obra existe y está bien citada, **pero nadie pudo chequear el enlace**. |
| `[VERIFICAR]` | Falta chequear algún dato de la cita (año, revista, número de página). |

> **Por qué hay tantas marcas pendientes.** El contenedor donde se construyó este repositorio
> sólo llega a `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. No se puede abrir `arxiv.org`, `doi.org`, `distill.pub`,
> YouTube, Wikipedia ni las páginas HTML de GitHub: se probaron y no responden.
> **Poner una URL sin haberla abierto sería inventarla**, y éste es un curso sobre no
> inventar. Así que las citas están completas y los enlaces quedan marcados para que alguien
> con red los complete. La lista consolidada del curso está en `recursos/bibliografia.md`.

---

## Si te quedaste con ganas

*(Cosas cortas, para hacer esta semana. Están en el orden en que conviene hacerlas.)*

**1. 3Blue1Brown, *Gradient descent, how neural networks learn* (capítulo 2 de la serie
*Neural Networks*).** `[VERIFICAR URL]`
Veinte minutos de animación. El canal existe y su repositorio de código respondió desde acá:
`raw.githubusercontent.com/3b1b/manim` `[VERIFICADA — el README devolvió 200 desde este
entorno]`; los videos están en YouTube, que **no se pudo abrir**.
**Por qué te conviene:** es, literalmente, esta clase, contada por alguien que dibuja mejor
que nosotros y con la superficie de loss en tres dimensiones moviéndose. Tiene subtítulos en
español.
**En qué orden:** **primero esto, antes que cualquier otra cosa de la lista.** Si sólo vas a
hacer una cosa de esta página, que sea ésta.

**2. Volver a las cuatro visualizaciones de hoy, sin apuro.** Sin URL: están en
`clases/03-loss-y-gradiente/viz/` y abren con doble clic, sin internet.
**Por qué te conviene:** en clase las movió el docente. La diferencia entre ver mover un
slider y moverlo vos es toda la diferencia. Dedicale diez minutos a
`comparador-de-losses.html` arrastrando **un punto por vez** y mirando qué recta se mueve.
**En qué orden:** el mismo día de la clase, o al día siguiente. Después se enfría.

**3. Correr el notebook otra vez cambiando **una sola cosa**: el tema.** Sin URL: es tuyo.
En la primera celda, `datos.serie_menciones("seguridad")` → probá con `"inflacion"`,
`"educacion"`, `"trabajo"` o `"salud"`.
**Por qué te conviene:** vas a ver que el paisaje cambia de forma y que el mismo learning
rate no le sirve igual a todas las series. Es la manera más barata de entender que **el
valle depende de tus datos**, no del método.
**En qué orden:** después de haber hecho los `TODO`, no antes.

**4. Tu propia base, y una pregunta.** Sin URL, porque es tuya.
**Por qué te conviene:** agarrá el último trabajo tuyo que tenga una regresión y buscá dos
cosas: (a) qué caso tiene el residuo más grande, y (b) qué pasa con tu conclusión si lo
sacás. Es media hora y es exactamente el `[EL LUNES]` de esta clase.

---

## Si te vas a meter en serio

*(Cosas largas. No hacen falta para seguir el curso.)*

**5. Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*. MIT Press.**
Capítulo 4 (*Numerical Computation*) y capítulo 8 (*Optimization for Training Deep Models*).
El libro completo está publicado gratis por los autores en `deeplearningbook.org`
`[VERIFICAR URL — el sitio no respondió desde este entorno]`.
**Por qué te conviene:** el capítulo 4 formaliza exactamente lo que hicimos hoy a mano
(gradiente, tasa de aprendizaje, condicionamiento del problema) y el 8 explica por qué en la
práctica se usa Adam y no descenso a secas.
**En qué orden:** es **material de consulta, no de lectura seguida**. Buscá el concepto que
te quedó flojo, leé esas cuatro páginas y cerralo. Leerlo de corrido es un mal plan.

**6. Ruder, S. (2016). *An overview of gradient descent optimization algorithms*.**
`[VERIFICAR URL — arxiv.org no respondió desde este entorno]`
**Por qué te conviene:** es el recorrido más claro que existe de SGD → momento → Adagrad →
RMSprop → Adam, con la intuición de cada uno antes de la fórmula. Diez páginas.
**En qué orden:** sólo si te preguntaste «¿y por qué Adam y no otro?». Si no te lo
preguntaste, saltealo tranquilo: no lo vas a necesitar en ninguna de las diez clases.

**7. Goh, G. (2017). *Why Momentum Really Works*. Distill.**
`[VERIFICAR URL — distill.pub no respondió desde este entorno]`
**Por qué te conviene:** es visualmente hermoso y explica, moviendo las cosas, por qué un
valle alargado hace zigzaguear al descenso y qué hace el momento para arreglarlo. Es la
continuación natural de la última celda del notebook.
**Aviso honesto:** va bastante más allá de lo que necesitás para este curso, y tiene
matemática de verdad a partir de la mitad. Recomendalo sólo si el zigzagueo te dejó
picando.
**En qué orden:** después del punto 5, si es que llegaste ahí.

---

## Para el docente

**8. Stigler, S. M. (1986). *The History of Statistics: The Measurement of Uncertainty
before 1900*. Harvard University Press.** Capítulo 1. `[VERIFICAR URL]`
**Para qué:** la anécdota de la slide 8. El método de mínimos cuadrados se publica con
Legendre en 1805 y Gauss lo reclama en 1809 `[VERIFICAR — fechas y detalles de la disputa
de prioridad]`; **se impuso en buena medida porque tenía solución cerrada**, o sea porque se
podía calcular con lápiz y papel. Que el MSE sea hoy el default no es un veredicto sobre qué
error importa: es la huella de una restricción de cómputo de hace dos siglos. Dicho en
clase, en treinta segundos, cambia cómo se lee un default.

**9. Simon, H. A. (1955). *A Behavioral Model of Rational Choice*. *Quarterly Journal of
Economics*, 69(1), 99-118.** `[VERIFICAR URL]` `[VERIFICAR — número de páginas]`
**Para qué:** fundamentar la analogía de la niebla. El descenso por gradiente es, punto por
punto, un agente de racionalidad limitada: información local, capacidad de cómputo acotada,
y una regla de decisión que igual lo lleva a un buen lugar (aunque no necesariamente al
mejor). Si el aula es de sociología, ciencia política o antropología, esta conexión les
cambia el vínculo con el tema.

**10. Ragin, C. C. & Becker, H. S. (eds.) (1992). *What Is a Case? Exploring the Foundations
of Social Inquiry*. Cambridge University Press.** `[VERIFICAR URL]`
**Para qué:** la slide 8. La tradición del estudio del caso desviado es, en el vocabulario de
hoy, la decisión de **darle mucho peso al outlier**. MSE y MAE son dos maneras de saldar esa
discusión metodológica, escritas en una línea de código. Sirve para mostrar que la elección
de loss no es un tema nuevo: es un tema viejo con ropa nueva.

**11. Los propios datos del curso.** `datos/README.md`, sección de trampas.
`[VERIFICADA — está en este repositorio]`. La recopilación de los discursos es de Lucas Ariel:
`raw.githubusercontent.com/lucariel/discursos_presidenciales`
`[VERIFICADA — el README devolvió 200 desde este entorno]`.
**Para qué:** los cuatro números de la slide 4 (0,0146 / 0,0152 / 0,0880 / 0,0921) y todos
los de las visualizaciones salen de esa serie. Están calculados en `notebook.ipynb`, no
estimados. Si alguien del aula los quiere reproducir, puede.

---

## Lo que deliberadamente NO está en esta lista

- **Tutoriales de PyTorch.** Es la clase 4 y llegan la semana que viene. Si los mirás ahora
  vas a ver `loss.backward()` sin entender qué anota, que es justamente lo que hoy
  entendiste a mano.
- **Cualquier cosa que empiece con «la regla de la cadena».** No la necesitás. Backprop es
  importante que exista y no es importante que la sepas derivar.
- **Papers de arquitecturas.** Todavía no. Primero hay que saber distinguir dibujar de
  calcar, y eso es la clase 4.
