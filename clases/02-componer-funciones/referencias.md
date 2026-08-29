# Referencias — Clase 2

**Componer funciones: dibujar lo imposible**

> **Sobre los enlaces.** El contenedor donde se construyó este repo tiene casi
> toda la red bloqueada: sólo llegan `pypi.org`, `files.pythonhosted.org`,
> `registry.npmjs.org` y `raw.githubusercontent.com`. Se probó cada URL de esta
> lista con `curl` y **ninguna respondió**, así que van marcadas
> `[VERIFICAR URL]`: las obras existen y están bien citadas, pero nadie abrió el
> enlace. **Poner una URL sin haberla abierto sería inventarla**, y éste es un
> curso sobre no inventar. Quien tenga red que las complete y las pase a
> `[VERIFICADA]` con la fecha.
>
> La única fuente verificada acá es la del corpus, porque vive en
> `raw.githubusercontent.com`.

---

## Si te quedaste con ganas

En el orden en que conviene mirarlas.

**1. Nielsen, Michael — *Neural Networks and Deep Learning*, capítulo 4:
«A visual proof that neural nets can compute any function».** `[VERIFICAR URL]`
> **Esto es la clase de hoy, escrito por otro y con las visualizaciones adentro
> del texto.** Si sólo vas a leer una cosa, leé ésta. Nielsen construye la misma
> demostración que hicimos con `viz/rampas.html`, pero con escalones en vez de
> rampas, y llega al mismo lugar. El libro es gratuito y está online completo.
> Está en inglés, pero el capítulo 4 es más figuras que texto.
> *Empezá por acá.* Media hora.

**2. 3Blue1Brown — *But what is a neural network?* (capítulo 1 de la serie
sobre deep learning).** `[VERIFICAR URL]`
> En la clase 1 te dijimos "todavía no". **Ahora sí.** Tiene subtítulos en
> castellano. Un aviso para que no te confunda: él usa **sigmoides** donde
> nosotros usamos **rampas**, y trabaja con imágenes de dígitos en vez de una
> serie temporal. Es lo mismo con otro doblez y otros datos. Mirá el capítulo 1
> ahora; el 2 dejalo para después de la clase 3, que es de lo que habla.
> 20 minutos.

**3. TensorFlow Playground.** `[VERIFICAR URL]`
> Un juguete en el navegador: agregás capas y neuronas y ves la figura que
> dibuja, en vivo. **Advertencia para no marearte:** usa un problema de
> *clasificación en dos dimensiones* (separar puntos azules de naranjas), no de
> ajustar una curva. La figura que dibuja es una frontera, no una línea que pasa
> por los datos. Es la misma idea con otro tipo de problema, y lo vamos a ver
> así en la clase 4. Si te confunde, dejalo para entonces.
> 10 minutos de jugar.

**4. Grimmer, Roberts & Stewart (2022), *Text as Data: A New Framework for
Machine Learning and the Social Sciences*, Princeton University Press.**
`[VERIFICAR]`
> **El libro de cabecera del curso**, y no es de deep learning: es de qué se
> puede y qué no se puede afirmar cuando medís cosas sociales con máquinas. Para
> hoy, alcanza con la introducción. La idea que conecta con esta clase es que la
> flexibilidad de un método no es gratis: cuanto más flexible, más carga de
> prueba te toca a vos.
> La introducción, una hora.

---

## Si te vas a meter en serio

**5. Cybenko, G. (1989), *Approximation by superpositions of a sigmoidal
function*, Mathematics of Control, Signals and Systems 2(4), 303-314.**
`[VERIFICAR]`
> El paper original del teorema de aproximación universal, con sigmoides.
> **No hace falta leerlo** y es matemática dura. Está acá para que puedas citarlo
> correctamente cuando alguien te diga "está demostrado que las redes pueden
> aproximar cualquier cosa": ahora sabés qué dice exactamente esa demostración
> —y, más importante, qué **no** dice.

**6. Hornik, K. (1991), *Approximation capabilities of multilayer feedforward
networks*, Neural Networks 4(2), 251-257.** `[VERIFICAR]`
> La generalización del resultado de Cybenko: la propiedad no depende de la
> forma exacta del doblez, sino de que **haya** un doblez. Es exactamente la
> lección de `viz/sin-no-linealidad.html`, escrita como teorema. Misma
> advertencia: se cita, no se lee, salvo que te guste el análisis funcional.

**7. McCulloch, W. & Pitts, W. (1943), *A logical calculus of the ideas immanent
in nervous activity*, Bulletin of Mathematical Biophysics 5, 115-133.**
`[VERIFICAR]`
> **De dónde salió la palabra «neurona».** Vale la pena hojearlo por razones
> históricas y sociológicas más que técnicas: se ve que la analogía biológica era
> razonable con lo que se sabía en 1943, y se ve por qué hoy confunde. Si alguna
> vez tenés que explicarle a alguien por qué el nombre es engañoso, tener leído
> el original te da autoridad para decirlo sin sonar despectivo.

**8. Goodfellow, I., Bengio, Y. & Courville, A. (2016), *Deep Learning*, MIT
Press, capítulo 6 («Deep Feedforward Networks»), secciones 6.1 a 6.4.**
`[VERIFICAR URL]`
> El tratamiento canónico y riguroso de lo de hoy: composición, activaciones,
> arquitectura. Es un libro de posgrado en ciencias de la computación y se nota;
> **no** empieces por acá. Pero si en algún momento necesitás la versión formal
> de algo que viste en esta clase, está en esas cuatro secciones. Disponible
> gratis en la web de los autores.

**9. Breiman, L. (2001), *Statistical Modeling: The Two Cultures*, Statistical
Science 16(3), 199-231.** `[VERIFICAR URL]`
> No habla de redes neuronales y es de lo mejor que podés leer esta semana.
> Breiman distingue dos formas de usar modelos: para **explicar** un mecanismo o
> para **predecir** un resultado. La clase de hoy construyó una máquina
> descaradamente del segundo tipo, y buena parte de la incomodidad legítima que
> podés estar sintiendo tiene nombre en este paper. Se lee en una tarde y
> reordena la cabeza.
> **Si te vas a meter en serio, empezá por acá y no por el 5.**

**10. Molina, M. & Garip, F. (2019), *Machine Learning for Sociology*, Annual
Review of Sociology 45, 27-45.** `[VERIFICAR]`
> El puente entre lo que estás aprendiendo y tu disciplina, escrito para
> sociólogos y con ejemplos de investigación real. Contesta la pregunta que
> probablemente te estés haciendo: *¿esto para qué me sirve a mí?*

---

## Los datos de esta clase

**Discursos presidenciales de apertura de sesiones (Argentina, 1854-2019).**
Recopilación y digitalización de **Lucas Ariel**, en
`github.com/lucariel/discursos_presidenciales`, inspirada en Bercholc &
Bercholc (2012), *Los discursos presidenciales en la Argentina democrática*.
**[VERIFICADA]** el archivo `raw.githubusercontent.com/lucariel/discursos_presidenciales/master/README.md`
respondió `200` en el contenedor de construcción (la página HTML de GitHub, no:
da 403).
> Los textos son actos oficiales del Estado argentino; **la recopilación no
> declara licencia**. Uso educativo con cita. Si el curso se publica, hay que
> escribirle al autor. Ver `datos/README.md` §1.1.

**La serie que usamos hoy** (`inflacion_suave`, 1984-2019, media móvil de 3 años)
sale de aplicarle a ese corpus el léxico que está en
`datos/preparar_corpus.py`, a la vista y versionado. **Ese léxico lo escribimos
nosotros**: la serie mide *ese* léxico, no «la inflación». Cambiar la lista de
palabras cambia la serie, y eso es un tema de la clase 10 sembrado desde acá.

---

## Lo que se prometió para más adelante

- **El sobreajuste** (lo que viste al apretar «32 rampas»): clase 4.
- **Cómo se encuentran los pesos solos**: clase 3.
- **Por qué la rampa y no la sigmoide, en serio**: clase 3, cuando se vea qué le
  pasa a la señal al bajar por muchas capas.
- **Ancho contra profundo, con imágenes**: clase 5.
