# Referencias — Clase 8

**Un mini-GPT propio, y la traducción a ChatGPT**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi toda la red
> bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`, `registry.npmjs.org` y
> `raw.githubusercontent.com`. **Se probó con `curl` cada URL de esta lista.** Las que
> respondieron van marcadas `[VERIFICADA 2026-08-29]`; el resto va marcado
> `[VERIFICAR URL]`: las obras existen, están bien citadas y se encuentran buscando por
> título y autor, pero **nadie abrió el enlace**, y poner una URL sin haberla abierto
> sería inventarla. Éste es un curso sobre no inventar, y esta clase en particular es
> sobre **por qué un modelo de lenguaje te da una referencia con formato impecable y
> datos falsos**. Sería raro hacerlo nosotros. Quien tenga red que las complete y las
> pase a `[VERIFICADA]` con la fecha.

---

## La deuda de esta clase

Esta clase es, sin vueltas, una traducción al castellano y al dominio del discurso
político de **`Let's build GPT: from scratch, in code, spelled out`, de Andrej
Karpathy**. La arquitectura del notebook, el orden de las secciones (bigrama primero,
transformer después), el tokenizador de caracteres y la idea de mirar las muestras
mientras entrena salen de ahí. Corresponde decirlo y corresponde citarlo.

---

## Si te quedaste con ganas

En el orden en que conviene leerlas.

**1. Karpathy, A. — *Let's build GPT: from scratch, in code, spelled out* (video).**
`[VERIFICAR URL]` (el video está en YouTube, canal «Andrej Karpathy»).
**El código sí está verificado:**
`https://raw.githubusercontent.com/karpathy/ng-video-lecture/master/gpt.py`
`[VERIFICADA 2026-08-29]`
> **La fuente de esta clase.** Construye exactamente lo que construimos hoy, en inglés,
> con Shakespeare en vez de debates parlamentarios. Si hiciste la clase, el video se te
> va a hacer fácil: vas a reconocer cada pieza y vas a entender por qué está ahí.
> Ese archivo `gpt.py` son 200 líneas y es todo el modelo. Abrilo aunque no veas el
> video: compará su `Block` con el `BloqueTransformer` de nuestro notebook y vas a ver
> que son el mismo.
> Dos horas de video. Vale la pena aunque tu inglés sea regular.

**2. Jay Alammar — *The Illustrated GPT-2*.**
`https://raw.githubusercontent.com/jalammar/jalammar.github.io/master/_posts/2019-08-12-illustrated-gpt2.md`
`[VERIFICADA 2026-08-29]` (ése es el texto fuente del post; la versión linda con las
animaciones está en su blog, `jalammar.github.io`, que desde acá no se pudo abrir
`[VERIFICAR URL]`)
> **Leelo después de la clase, no antes.** Es el mejor material visual sobre cómo un
> transformer genera texto de a una ficha por vez. Las animaciones de la generación
> autorregresiva —la ficha que sale vuelve a entrar— son exactamente lo que hace nuestro
> bucle de `generar()`, y verlo dibujado termina de cerrarlo.
> Cuarenta minutos.

**3. Wolfram, S. (2023). *What Is ChatGPT Doing… and Why Does It Work?*.**
`[VERIFICAR URL]`
> Largo, y no hace falta leerlo entero: **con las primeras tres secciones alcanza**.
> Es la explicación más accesible que existe de «predecir la próxima palabra» para
> alguien sin formación técnica, y usa la temperatura como ejemplo central, igual que
> nosotros. Si tenés un colega escéptico al que querés explicarle esto sin código, es
> lo que le pasás.
> Dos horas si lo leés entero; cuarenta minutos si te quedás con el principio.

**4. Bender, E., Gebru, T., McMillan-Major, A. & Shmitchell, S. (2021).
*On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?*. FAccT '21.**
`[VERIFICAR URL]`
> **La lectura de ciencias sociales de esta clase.** El argumento central —que un modelo
> entrenado sólo con forma produce texto sin referencia, y que la fluidez nos hace
> atribuirle una intención comunicativa que no tiene— es *literalmente* lo que viste al
> mirar tu mini-GPT escribir cadencia parlamentaria impecable sobre nada.
> Leelo con matices: la discusión sobre si «loro estocástico» describe bien a los
> modelos de 2026 está abierta, y el paper también habla de costo ambiental y de sesgo
> del corpus, que son otros dos temas. La parte que te toca hoy es la sección sobre
> **forma sin significado**.
> Veinte páginas. Es el paper más citado del campo en ciencias sociales y conviene
> haberlo leído vos, no leído *sobre* él.

**5. Prompt Engineering Guide (DAIR.AI).**
`https://raw.githubusercontent.com/dair-ai/Prompt-Engineering-Guide/main/README.md`
`[VERIFICADA 2026-08-29]`
> Práctico, no teórico. Sirve para una cosa concreta: si vas a usar un LLM como
> asistente de codificación en tu investigación, acá están las técnicas que
> efectivamente mejoran la consistencia (dar ejemplos, pedir un formato de salida fijo,
> separar instrucción de datos). **Leelo sabiendo lo de hoy**: ninguna de esas técnicas
> instala un verificador de verdad, todas mueven la distribución. Sirven para bajar la
> tasa de error, no para eliminar el mecanismo.
> Una hora, salteando.

---

## Si te vas a meter en serio

**6. Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z. & Yang, D. (2024).
*Can Large Language Models Transform Computational Social Science?*.
Computational Linguistics 50(1).** `[VERIFICAR URL]`
> **La evaluación sistemática más seria que existe** de LLMs en tareas de ciencias
> sociales: 24 tareas, 13 modelos, comparados contra codificadores humanos. La
> conclusión es la que sostiene este curso, y viene con números: sirven como
> **asistentes de anotación con validación humana**, no como reemplazo, y su desempeño
> es muy desparejo según la tarea. Si vas a escribir una sección de métodos que use un
> LLM, este es el trabajo que citás para justificar tu diseño.
> Léelo entero. Es la referencia de la clase 9 también.

**7. Ouyang, L. et al. (2022). *Training Language Models to Follow Instructions with
Human Feedback* (InstructGPT). NeurIPS.** `[VERIFICAR URL]`
> El paper que explica la slide 35: **cómo se pasa de autocompletador a asistente.**
> Leé la sección de método (las tres etapas: supervisado, modelo de recompensa, PPO) y
> saltate los detalles de RL. Lo que importa para vos es entender que hay una etapa
> donde **humanos contratados ordenan respuestas por preferencia**, y que la amabilidad,
> la verborragia y la adulación del modelo salen de ahí — o sea, son una decisión de
> producto, no una propiedad del lenguaje.
> Media hora leyendo el método.

**8. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. &
Liang, P. (2023). *Lost in the Middle: How Language Models Use Long Contexts*. TACL.**
`[VERIFICAR URL]`
> El sustento empírico del panel práctico de `viz/ventana-de-contexto.html`. Muestra que
> en los modelos grandes el problema no es sólo la ventana finita: **la información que
> queda en el medio de un contexto largo se usa peor que la de las puntas**, incluso
> estando adentro. La recomendación práctica de la viz («poné lo importante al final»)
> sale de acá.
> Diez páginas y los gráficos se entienden solos.

**9. Barrie, C., Palmer, A. & Spirling, A. (2024). *Replication for Language Models:
Problems, Principles, and Best Practice for Political Science*.** `[VERIFICAR URL]`
> **Leelo antes de escribir tu sección de métodos.** Es el argumento, hecho por
> politólogos y para politólogos, de por qué un resultado producido con un modelo
> cerrado que cambia sin aviso **no es reproducible**, y qué se puede hacer al respecto
> (modelos abiertos con versión fija, temperatura 0, prompt en el apéndice, reporte de
> fecha). Es la versión rigurosa de la última slide de esta clase.
> Se retoma entero en la clase 10.

**10. Karpathy, A. — `nanoGPT`.**
`https://raw.githubusercontent.com/karpathy/nanoGPT/master/model.py`
`[VERIFICADA 2026-08-29]` ·
`https://raw.githubusercontent.com/karpathy/nanoGPT/master/train.py`
`[VERIFICADA 2026-08-29]`
> Si querés entrenar algo más serio que el juguete de hoy, este es el repositorio.
> `model.py` es el mismo modelo del notebook con las optimizaciones que hacen falta para
> escalar; `train.py` tiene todo lo que nosotros salteamos (checkpoints, acumulación de
> gradientes, learning rate schedule, entrenamiento en varias GPU). **Mirá primero
> cuánto de `model.py` ya entendés**: es más de lo que esperás.

**11. Karpathy, A. — `build-nanogpt` (reproducir GPT-2 desde cero).**
`https://raw.githubusercontent.com/karpathy/build-nanogpt/master/train_gpt2.py`
`[VERIFICADA 2026-08-29]`
> El paso siguiente: reproducir GPT-2 (124M) de verdad. Está acá para que veas, con
> números, **cuánto cuesta**: horas de GPU, decenas de miles de millones de fichas, y
> todos los detalles de ingeniería que a esta escala dejan de ser opcionales. Es el
> argumento cuantitativo del puente a la clase 9: *entrenar el tuyo casi nunca es lo que
> necesitás*.

**12. `tiktoken` — el tokenizador de los modelos de OpenAI.**
`https://raw.githubusercontent.com/openai/tiktoken/main/README.md`
`[VERIFICADA 2026-08-29]`
> Para el que quedó picado con `viz/contar-letras.html`. Son tres líneas de código para
> ver **exactamente** en qué fichas parte un modelo real cualquier texto tuyo. Probá con
> palabras en castellano largas y con nombres propios de tu corpus: vas a encontrar que
> el castellano se parte en más fichas que el inglés, y eso tiene consecuencias
> concretas (más costo por texto, ventana efectiva más chica, peor desempeño). Es un
> buen dato para una nota al pie de tu paper.

---

## Para el docente

- **Grimmer, J., Roberts, M. & Stewart, B. (2022). *Text as Data*. Princeton UP.**
  `[VERIFICAR URL]` — El marco general del módulo. Para esta clase, el capítulo de
  validación es el que arma el `[EL LUNES]`.
- **Bajtín, M. (1979). *El problema de los géneros discursivos*.** `[VERIFICAR URL]` —
  Si tenés en el aula gente de análisis del discurso, la analogía del género discursivo
  (el modelo aprende la forma del debate antes que cualquier contenido) les cierra al
  instante y vale la pena nombrar la fuente.
- **`datos/README.md` §1.5** — Por qué el corpus Aguasclaras es sintético y qué se gana
  y qué se pierde con eso. Leelo antes de dar la clase: la pregunta «¿por qué no usaron
  discursos reales?» sale siempre y la respuesta es buena.
