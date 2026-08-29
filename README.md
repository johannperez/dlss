# Deep Learning para Cientistas Sociales

Curso de 10 clases de 2 horas, en español rioplatense, para gente de sociología, ciencia política,
antropología, comunicación y economía que quiere **sumar esta herramienta a su caja y usarla con
criterio** — no convertirse en data scientist.

## Por dónde empezar

1. **`PROGRAMA.md`** — el programa completo: filosofía pedagógica, tabla resumen de las 10 clases,
   plan minuto a minuto de cada una, decisiones transversales de diseño y el mapa de puentes entre
   clases. **Léelo entero antes de construir nada.**
2. **`_shared/especificaciones/clase-NN-slug.md`** — la especificación detallada de cada clase:
   narrativa, guion de slides, spec de cada visualización, spec del notebook celda por celda,
   confusiones típicas, analogías, temas del cuestionario y referencias.

## Estructura

```
PROGRAMA.md                        el programa del curso
_shared/
  vendor/                          reveal.js y KaTeX vendoreados (NO hay acceso a CDNs)
  especificaciones/                spec detallada por clase (entrada para quien construye)
  css/ js/ plantillas/ ssdl/       estilos, utilidades y plantillas compartidas
clases/NN-slug/
  slides.html                      reveal.js, assets por ruta relativa, abre con file://
  notebook.ipynb                   Colab, autoinstalable, corre en CPU
  viz/*.html                       visualizaciones interactivas standalone, sin dependencias
  notas-docente.md                 guion hablado, tiempos, qué recortar si se atrasa
  cuestionario.md
  cuestionario-soluciones.md
  referencias.md                   URLs marcadas VERIFICADA o VERIFICAR
datos/                             corpus (ver PROGRAMA.md §3.1)
recursos/                          glosario.md, setup.md, bibliografia.md
```

## Reglas innegociables para quien construye

- **Todo offline.** Cero `<script src="https://...">`. Los assets se referencian por ruta relativa
  desde `_shared/vendor/`. Cada página tiene que abrir con `file://` y funcionar.
- **Nada de matemática sin una imagen al lado.** Si hay una fórmula sin figura, se borra la fórmula.
- **Ningún notebook puede fallar por falta de red.** Patrón `try: descargar() / except:
  generar_sinteticos()` obligatorio.
- **Español rioplatense, tono cercano, cero solemnidad.** Términos técnicos en inglés, explicados en
  castellano la primera vez y cargados al glosario.
- **La metáfora del dibujo atraviesa las 10 clases**, con callback explícito a la anterior.
- **Cada clase tiene un momento `[EL LUNES]`**: algo concreto que sirve en su investigación ya.
- **Cada visualización tiene declarado su "momento aha"** en la especificación. Si al construirla no
  se produce ese momento, la viz está mal y hay que rehacerla, no maquillarla.
