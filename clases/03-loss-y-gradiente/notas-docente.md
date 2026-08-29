# Clase 3 — Notas para quien la da

**Estar equivocado es un número, y ese número tiene pendiente** · 120 minutos · 36 slides
Prerrequisitos: clases 1 y 2. Nivel de matemática de la audiencia: la palabra «derivada»
todavía no se pronunció, y hoy se pronuncia **una sola vez, en el minuto 60**.

> **Lo único que no se puede perder hoy:** que se vayan entendiendo que **la loss es una
> decisión que toman ellos**, no un default del software. El gradiente es el instrumento;
> la loss es el tema. Si el gradiente se explica bien y la loss queda como un detalle
> técnico, la clase salió mal aunque todos se hayan reído.

---

## 1. El arco narrativo en diez líneas

1. Dos rectas sobre la misma nube. «¿Cuál es mejor?» El aula se divide, y se divide **con razón**.
2. La pregunta está mal formulada: no hay «mejor» hasta que alguien escribe el criterio.
3. Ese criterio se llama *loss*, y hay más de uno. MSE castiga el cuadrado; MAE, el error a secas.
4. Se arrastra un caso extremo y la recta azul lo persigue mientras la naranja lo ignora.
   **Dos conclusiones sustantivas distintas, con los mismos datos.** Este es el corazón.
5. Se reformula el problema: encontrar la mejor recta = minimizar un número.
6. Salto conceptual: cada par de perillas **es** una recta, así que hay un mapa de rectas
   y cada punto tiene una altura. Es el momento más difícil de la clase.
7. Probamos todas. Funciona. Y se muere en la tercera línea de una tabla.
8. La niebla: no ves el paisaje, pero podés tantear con el pie. Eso se calcula con una resta,
   y recién ahí se dice la palabra «derivada».
9. Se suelta la pelota. Los pasos se acortan solos. Se rompe el learning rate a propósito
   y se aprenden las tres firmas de la curva de loss.
10. La honestidad del final: los paisajes reales no son este pozo lindo, el descenso no
    garantiza nada, y funciona igual. Nadie sabe del todo por qué.

`[CALLBACK DIBUJO]`, en la slide 2: *«hasta ahora nosotros movíamos la mano para dibujar.
Hoy le enseñamos a la máquina a mover la mano sola. La figura la sigue eligiendo el que arma
el modelo; el pulso lo pone el gradiente.»*

---

## 2. Plan de tiempos real

| Min | Slides | Bloque | Qué pasa |
|---|---|---|---|
| 0:00 | 1-2 | Apertura | Portada + «dónde quedamos». **3 minutos, no más.** |
| 0:03 | 3-4 | **Gancho** | Las dos rectas, la votación a mano alzada, «están todos en lo cierto». |
| 0:10 | 5-6 | Idea 1a | El número gris tiene nombre. Las dos formas del castigo: parábola y V. |
| 0:17 | 7 | **Viz 1** | `comparador-de-losses.html`. El docente arrastra. 5 minutos. |
| 0:22 | 8-9 | Idea 1b | Decisión metodológica (3 escenarios) y decisión política (la siembra). |
| 0:25 | 10 | **Manos 1a** | Notebook sección 1 + `TODO 1`. **15 minutos de trabajo.** |
| 0:40 | 11-13 | Idea 2a | Reformular el problema · **el salto conceptual** · el mapa de altura. |
| 0:48 | 14-15 | **Viz 2** + apuesta | `valle-de-loss.html` en modo arrastrar. Se vota antes de mover. |
| 0:54 | 16-18 | Idea 2b | Fuerza bruta, la tabla que la mata, la niebla. |
| 0:57 | 19 | **Viz 3** | `loss-1d.html`. **Acá se dice «derivada» por primera vez.** |
| **1:00** | 20 | **PAUSA** | **10 minutos. No se toca.** |
| 1:10 | 21 | El gradiente | La flecha y el signo menos, en el pizarrón, con un número. |
| 1:13 | 22-23 | **Viz 2 y 4** | Soltá la pelota · las tres tasas de aprendizaje en paralelo. |
| 1:25 | 24 | Las tres firmas | La slide de la que hay que sacar foto. |
| 1:28 | 25 | **Manos 2** | Notebook secciones 4 a 6, de a dos. **20 minutos.** |
| 1:48 | 26 | Volvimos | Se proyecta una curva rota del aula. |
| 1:50 | 27-30 | Cierre conceptual | Censo/muestra · backprop · la honestidad · optimizadores. |
| 1:57 | 31-36 | Salida | `[EL LUNES]` · la escalera · qué te llevás · glosario · el puente. |

Suma: 120 minutos exactos, con la pausa adentro.

**Ojo con el minuto 57.** La viz `loss-1d` está *justo antes* de la pausa a propósito: es la
que hace que nadie necesite haber estudiado cálculo, y conviene que la digieran con un café
en la mano. Si vas dos minutos tarde, entrá igual a la pausa: la recuperás en el bloque 21-24.

---

## 3. Qué preguntar al aula, y cuándo

### Minuto 4 — «¿Cuál de las dos es mejor?» (slide 3)

**Es LA pregunta de la clase.** Votación a mano alzada, con tres opciones: azul, naranja,
«no se puede decidir». **Contá los votos en voz alta y anotalos en el pizarrón**: se usan
en la slide siguiente y otra vez en el cierre.

| Lo que dicen | Qué hacer con eso |
|---|---|
| «La azul, porque pasa más por el medio» | Perfecto. Traducilo: «vos estás priorizando no equivocarte mucho en ningún caso». Eso es MSE, y todavía no lo sabe. |
| «La naranja, porque sigue mejor la subida del final» | También perfecto: «vos le estás dando peso a los años recientes». Anotalo. |
| «Depende de qué te importe» | **Regalo. Paralo todo y repetilo para el aula.** Esa persona acaba de decir la clase entera. Preguntale «¿qué te podría importar?» y dejá que arme la lista. |
| «Faltan datos / no se puede decidir» | «Tenés razón, y sin embargo la mitad del aula votó. Guardá esa incomodidad.» |
| Silencio | Votá vos por la azul en voz alta con un argumento tonto («es más linda») y esperá. Alguien te va a corregir. |

### Minuto 20 — «¿Cuál de los dos investigadores mintió?» (slide 7, después de plantar el outlier)

La respuesta es **ninguno**. Aguantá el silencio hasta que alguien lo diga. Después, la frase:
*«los dos hicieron bien las cuentas, los dos usaron los mismos datos y los dos publicaron
conclusiones distintas. La diferencia está en una línea de código que ninguno de los dos
discutió en el paper.»*

### Minuto 24 — «¿Alguien tiene en su base un caso que es *el* caso?» (slide 8)

Casi siempre hay una mano. Dejá que lo cuente en treinta segundos y preguntale:
*«¿vos querés un modelo que lo explique, o un modelo que describa a los otros doscientos?»*.
No hay respuesta correcta y ése es el punto.

### Minuto 44 — La pregunta de control del salto conceptual (slide 12)

**No la saltees.** *«Si agrego un dato nuevo a la nube de la izquierda, ¿aparece un punto
nuevo en el mapa de la derecha?»*

- Respuesta correcta: **no**. Cambia la altura de **todo** el mapa.
- Si contestan «sí», el salto no está dado. Volvé a la slide 12 y decilo con otras palabras.
  Cuesta dos minutos ahora y cuesta media clase si lo arrastrás.

### Minuto 52 — La apuesta (slide 15)

*«Estoy parado arriba a la izquierda. Si me muevo hacia la derecha, ¿la loss sube o baja?»*
A, B o C, a mano alzada, **antes** de tocar nada.

La respuesta es **C: depende de cuánto me mueva**, y casi nadie la vota. Un poquito a la
derecha baja; si me paso de largo, vuelve a subir. Y ésa es *exactamente* la razón por la
que dentro de veinte minutos el tamaño del paso va a importar tanto. Sin esta apuesta, la
viz del learning rate es un dibujito lindo.

### Minuto 78 — «¿Por qué se acortan los pasos, si nadie los acortó?» (slide 22)

Aguantá el silencio quince segundos. La respuesta: **el paso es proporcional a la pendiente,
y cerca del fondo el terreno se aplana**. La pelota frena sola. Nadie la frenó.

### Minuto 108 — «¿Quién lo rompió mejor?» (slide 26)

Que lo cuente quien lo rompió, no vos. Y si nadie hizo la pregunta del mínimo global,
hacela vos: *«¿siempre llega al mismo lugar?»*. Es la puerta a la slide 29.

---

## 4. Las confusiones que van a aparecer, y cómo desarmarlas

### 4.1 Confundir el espacio de datos con el espacio de parámetros
**La confusión número uno de esta clase.** Se manifiesta como: «¿el eje x del mapa son los
años?». No: en el mapa **no hay ningún año y ningún porcentaje; hay rectas**.
*Cómo se desarma:* los dos paneles sincronizados de `valle-de-loss.html`, arrastrados
despacio, más la pregunta de control de la slide 12. Frase útil, textual:
**«cada punto de ese mapa es una recta entera».** Decila tres veces con distintas palabras.

### 4.2 «El gradiente apunta al mínimo»
Se manifiesta como: alguien traza con el dedo la flecha hasta el fondo del valle.
*Cómo se desarma:* la flecha señala la **subida más empinada acá nomás**. Es local y es
ciega. En el valle redondo de hoy da la casualidad de que apunta bastante al fondo; en la
última celda del notebook (la zanja diagonal) **no apunta ni cerca**, y el descenso zigzaguea
de pared a pared. Esa figura del notebook es la prueba: mostrala si insisten.

### 4.3 «Entonces siempre encuentra la mejor solución»
*Cómo se desarma:* `valle-de-loss.html`, botón **«uno con dos pozos»**, soltar desde dos
lugares distintos. Terminan en pozos distintos, con alturas 0,106 y 0,065. Treinta segundos
y la confianza excesiva se cae sola. Slide 29.

### 4.4 Pánico ante la palabra «derivada»
*Cómo se desarma:* **la palabra no se dice hasta la slide 19**, después de que ya la
calcularon con una resta. Y cuando se dice, se dice así: *«esa resta que acabamos de hacer
tiene un nombre elegante»*. No al revés. Si se te escapa antes, no pasa nada, pero perdés
el efecto.

### 4.5 «MSE es el correcto; MAE es una alternativa rara»
Toman el default como verdad.
*Cómo se desarma:* la viz 1 más los tres escenarios de la slide 8. Y el dato histórico:
**el MSE se popularizó en buena medida porque tenía solución cerrada** —se podía resolver
con lápiz y papel a principios del siglo XIX— y no porque represente mejor el error que a
vos te importa. Es una decisión de comodidad de cálculo que quedó como norma.

### 4.6 Comparar el número del MSE con el del MAE
**Aparece en el práctico 1a, sin falta.** «El MSE me dio 0,014 y el MAE 0,090, así que el MSE
es mejor.» No: están en unidades distintas (puntos al cuadrado contra puntos). Es como
comparar metros con metros cuadrados. Cada loss se compara **consigo misma** cuando movés
las perillas.

### 4.7 Creer que el learning rate se calcula
Piden la fórmula del lr óptimo. No hay.
*Respuesta honesta:* **«se prueba, se mira la curva, se ajusta. Es artesanía y la hacemos
todos.»** Dales el rango práctico (0,1 a 0,0001) y la heurística: si la loss sube, dividí
por diez.

### 4.8 Perderse en el signo menos
`a = a - lr * pendiente`: no entienden por qué menos.
*Cómo se desarma:* **en el pizarrón, con un número, una sola vez.** «La pendiente da +3:
subir la perilla sube la loss. Entonces bajo la perilla. Resto.» Con números alcanza; con
palabras, no.

### 4.9 Pensar que backprop reemplaza al descenso
*Cómo se desarma:* son dos piezas distintas del mismo mecanismo. **El descenso decide hacia
dónde y cuánto; backprop es sólo la manera eficiente de calcular el gradiente.** Slide 28.

### 4.10 (Bonus, del práctico) «Con lr=1.5 el número se congela»
Van a ver que la loss explota y después se queda quieta en 2,67e+25 en vez de seguir
creciendo. **No es un bug de ellos.** Es que la derivada-por-resta se rompe con números
gigantescos: `loss(a+h)` y `loss(a-h)` dejan de distinguirse en punto flotante. Está
explicado en el notebook, arriba del `TODO 4`, y es un puente perfecto a la slide de
backpropagation: *«por eso las bibliotecas de verdad no usan restas».*

---

## 5. Si vas atrasado

Lo que se recorta, **en este orden**:

1. **Slide 30 (optimizadores, «los nombres que vas a ver»).** Un renglón: «van a ver `Adam`
   en todos lados; es la pelota con inercia y con paso que se autorregula». Y seguís.
   **Ojo: la 30 se recorta, la 29 no.** La 29 es la honestidad y está en la lista de abajo.
2. **Slide 27 (censo o muestra).** Se puede decir en veinte segundos sin la figura:
   «calcular con todos los datos es un censo, con unos pocos es una muestra». Vuelve en la clase 4.
3. **Slide 16 (la grilla de fuerza bruta).** Se salta y se va directo a la tabla de la 17,
   que es la que hace el trabajo.
4. **La segunda mitad de la viz 4** (el quiz de aparear firmas): se manda como tarea.
5. **Cinco minutos del práctico 2**: que hagan `TODO 3` y `TODO 5`, y `TODO 4` en casa.

Lo que **NUNCA** se recorta, pase lo que pase:

- **La pausa.** Diez minutos. Si te atrasaste, te atrasaste; la pausa va igual.
- **La votación de la slide 3.** Sin la división del aula, todo lo demás es una clase de cálculo.
- **La viz 1 (arrastrar el outlier).** Es el corazón sustantivo de la clase para esta audiencia.
- **La slide 12 y su pregunta de control.** Si el salto conceptual no está dado, la segunda
  mitad de la clase no se entiende.
- **La viz 3 (`loss-1d`).** Es lo que hace que nadie necesite haber estudiado cálculo.
- **La slide 29 (la honestidad).** Dos minutos. Vacuna contra la mistificación y genera
  confianza. Es lo primero que uno tiende a recortar y es un error.

---

## 6. Si vas adelantado

- **El barrido de MAE en vivo.** En `comparador-de-losses.html`, arrastrá el punto de 2002
  (el que vale cero) hasta arriba de todo, despacio, y narrá cómo la azul lo sigue y la
  naranja no. Cinco minutos y no cansa.
- **El quiz de firmas** de `tasa-de-aprendizaje.html`, de a dos, con las tres curvas sin
  etiquetar. Convierte la viz en evaluación formativa y sale muy bien.
- **La última celda del notebook** (el año centrado contra el año crudo). Proyectala: la
  zanja diagonal es una imagen que se acuerdan. Y explica por qué todo el mundo estandariza
  sus variables antes de entrenar: **no es higiene estadística, es la forma del valle**.
- **La pregunta abierta:** «¿y si la loss que te importa no se puede escribir como una
  cuenta? Por ejemplo: “que el modelo no discrimine”». Los deja pensando y es la clase 10.

---

## 7. Los chistes y las analogías que funcionan

- **«Se acabó la fuerza bruta en la línea 3 de esta tabla.»** Pausa después de leer los 115
  días. Funciona porque es un número real, no una exageración.
- **El learning rate como velocidad de reforma.** Cambios muy chicos: no pasa nada en una
  generación. Cambios enormes de golpe: el sistema se desestabiliza y termina peor que antes.
  Se ríen, y después se acuerdan.
- **Censo contra muestra.** *«Calcular el gradiente con todos los datos es un censo; con un
  mini-batch es una muestra. La muestra es ruidosa y muchísimo más barata, y con suficientes
  iteraciones llegás igual. Todo lo que ya saben de muestreo aplica.»* **Es la mejor analogía
  de la clase para esta audiencia.** Señalá el temblor del rastro naranja y decí «eso es error
  de muestreo».
- **Mínimo local = *lock-in* institucional.** Path dependence: el sistema se estabiliza en una
  configuración que nadie elegiría de cero, y salir cuesta. La analogía es exacta, no decorativa.
- **La niebla y el conocimiento situado.** No ves el paisaje completo; ves tu entorno inmediato
  y decidís con eso. Si el aula es de sociología o antropología, mencioná a Simon y el
  *satisficing*: el descenso por gradiente es un agente de racionalidad limitada que igual
  llega a buen puerto.
- **«Se fue a la mierda».** Alguien lo va a decir en voz alta cuando subas el learning rate a
  1,5. Está bien. Reíte y seguí: es el momento en que el concepto quedó.

**Un chiste que NO conviene hacer:** ninguno sobre que la matemática es difícil, ni «no se
asusten». No se anuncia el susto.

---

## 8. Si te preguntan X

### «¿Cómo elijo la loss para mi problema, entonces?»
Honestamente: casi nunca la elegís de cero, elegís de una lista corta y bien conocida
(MSE, MAE, entropía cruzada para clasificar). **Lo que sí hacés siempre es dos cosas:
saber cuál elegiste y por qué, y correr la alternativa para ver si tu conclusión cambia.**
Si cambia, eso es un hallazgo y va en el paper. Si no cambia, también, y te ahorra una
objeción de revisor. La regla operativa es esa, no una fórmula.

### «¿Esto es lo mismo que mínimos cuadrados de toda la vida?»
Para el caso de hoy, **sí, exactamente**: la recta que minimiza el MSE es la recta de
mínimos cuadrados que ya conocen, y hay una fórmula cerrada que la da de una. La diferencia
es el **método**: mínimos cuadrados resuelve la fórmula; el descenso por gradiente la busca
tanteando. ¿Por qué usar el método peor? Porque la fórmula cerrada **sólo existe para casos
así de simples**. Para una red con un millón y medio de perillas no hay fórmula, y el
tanteo sigue funcionando igual. Ésa es toda la razón de ser de esta clase.

### «¿Y si la loss que me importa no se puede escribir como una cuenta?»
Buena pregunta, y la respuesta honesta es: **entonces vas a optimizar otra cosa y esperar que
se le parezca**. Casi todo lo que le importa a una ciencia social —que una medida sea justa,
que una clasificación no reproduzca un estereotipo— no tiene una fórmula obvia. Lo que se hace
es elegir un *proxy* y **declararlo**. La clase 10 es entera sobre eso, y sobre lo que pasa
cuando el proxy se aleja de lo que en realidad querías.

### «¿Por qué el gradiente y no otra cosa? ¿Es lo óptimo?»
No, no es óptimo: es **barato**. Hay métodos que usan más información (la curvatura, no sólo
la pendiente) y convergen en muchísimos menos pasos. Pero cuestan carísimo por paso cuando
hay millones de parámetros. El gradiente ganó por eficiencia computacional, no por elegancia
matemática. Es una decisión de ingeniería, y está bien saberlo.

### «Si nadie entiende del todo por qué funciona, ¿cómo confío en un resultado?»
Separá dos cosas. Lo que **no** está bien entendido es por qué el descenso encuentra
soluciones tan buenas en paisajes tan feos: es una pregunta abierta de teoría. Lo que **sí**
está perfectamente entendido y es verificable es si *tu* modelo funciona en *tus* datos: para
eso existen la validación, el conjunto de test y las métricas, que son las clases 4, 9 y 10.
**No confiás en el método: verificás el resultado.** Y ésa es exactamente la actitud de
cualquier método empírico que ya usan.

### «¿Y si mis datos son categóricos / mi variable dependiente es binaria?»
Cambia la loss, no cambia nada más del mecanismo. Para clasificar se usa *entropía cruzada*
en vez de MSE, y por la misma razón de siempre: castiga lo que te interesa castigar (estar
muy seguro y equivocado). El paisaje, el gradiente, el paso y las tres firmas de la curva de
loss son idénticos. Lo van a ver en la clase 4.

---

## 9. Checklist de cinco minutos antes de entrar

- [ ] `slides.html` abierto y probado **en el proyector**, no en tu monitor.
- [ ] Las cuatro viz abren solas (`viz/*.html`), por si el iframe se pone lento.
- [ ] El notebook corrido de punta a punta **en tu máquina**, así conocés los números.
- [ ] Pizarrón o papelógrafo a mano: el signo menos se hace ahí, no en la slide.
- [ ] Los números de la votación de la clase 2 (si los tenés) anotados para la slide 2.
- [ ] Cronómetro a la vista. La pausa a los 60 minutos, en serio.
