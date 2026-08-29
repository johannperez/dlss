/* =============================================================================
   viz.js — mini biblioteca de visualización del curso
   Deep Learning para Cientistas Sociales

   JS puro. Canvas 2D + SVG. CERO dependencias, CERO CDN, funciona con file://.

   Todo lo público cuelga del global `Viz`. Las funciones están documentadas en
   castellano y con un ejemplo de uso al lado.

   Los colores NO se hardcodean: se leen de las variables CSS de curso.css, así
   que la semántica de color del curso (datos / modelo / parámetro / error /
   validación) se hereda sola y el tema oscuro funciona sin tocar una línea.

     Viz.color('datos')      -> el color de "lo observado"
     Viz.color('modelo')     -> el color de "lo que el modelo dibuja"
     Viz.color('#ff0000')    -> pasa de largo, es un color literal

   Uso mínimo:
     const p = Viz.plano('#lienzo', { xmin:0, xmax:10, ymin:-1, ymax:1 });
     p.alDibujar(() => { p.fondo(); p.grilla(); p.ejes();
                         p.curva(x => Math.sin(x), { color:'modelo' }); });
     p.redibujar();
   ============================================================================= */

(function (global) {
  'use strict';

  /* =========================================================================
     0. UTILIDADES CHICAS
     ========================================================================= */

  /** Devuelve un elemento del DOM. Acepta selector CSS o el elemento mismo.
   *  @example const c = Viz.nodo('#lienzo'); */
  function nodo(sel) {
    if (!sel) return null;
    return typeof sel === 'string' ? document.querySelector(sel) : sel;
  }

  /** Crea un elemento con atributos, texto y padre opcionales.
   *  @example Viz.el('button', { class:'boton', texto:'Soltar la pelota' }, panel); */
  function el(tag, attrs, padre) {
    const n = document.createElement(tag);
    if (attrs) for (const k in attrs) {
      if (k === 'texto') n.textContent = attrs[k];
      else if (k === 'html') n.innerHTML = attrs[k];
      else if (k === 'estilo') Object.assign(n.style, attrs[k]);
      else n.setAttribute(k, attrs[k]);
    }
    if (padre) padre.appendChild(n);
    return n;
  }

  /** Recorta v al intervalo [a,b].  @example Viz.acotar(1.4, 0, 1) // 1 */
  function acotar(v, a, b) { return v < a ? a : (v > b ? b : v); }

  /** Interpolación lineal entre a y b.  @example Viz.mezclar(0, 10, .5) // 5 */
  function mezclar(a, b, t) { return a + (b - a) * t; }

  /** Array [0,1,...,n-1].  @example Viz.rango(3) // [0,1,2] */
  function rango(n) { const r = new Array(n); for (let i = 0; i < n; i++) r[i] = i; return r; }

  /** n valores equiespaciados de a a b (incluidos).
   *  @example Viz.linspace(0, 1, 5) // [0,.25,.5,.75,1] */
  function linspace(a, b, n) {
    const r = new Array(n);
    for (let i = 0; i < n; i++) r[i] = n === 1 ? a : a + (b - a) * i / (n - 1);
    return r;
  }

  /** Generador pseudoaleatorio con semilla fija (mulberry32). Reproducibilidad
   *  desde la clase 1: la misma semilla da siempre la misma nube de puntos.
   *  @example const rnd = Viz.azar(42); rnd(); // 0.6011... siempre */
  function azar(semilla) {
    let a = (semilla >>> 0) || 1;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  /** Ruido gaussiano con semilla (Box-Muller).
   *  @example const g = Viz.gauss(7); g(); // ~N(0,1) */
  function gauss(semilla) {
    const rnd = typeof semilla === 'function' ? semilla : azar(semilla);
    return function () {
      let u = 0, v = 0;
      while (u === 0) u = rnd();
      while (v === 0) v = rnd();
      return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
    };
  }

  /** Formatea un número para mostrarlo al lado de un slider.
   *  @example Viz.num(3.14159, 2) // "3.14" */
  function num(v, dec) {
    if (!isFinite(v)) return '—';
    if (dec === undefined) {
      const a = Math.abs(v);
      dec = a >= 100 ? 0 : a >= 10 ? 1 : a >= 1 ? 2 : a >= 0.01 ? 3 : 4;
    }
    if (Math.abs(v) >= 1e5 || (Math.abs(v) < 1e-4 && v !== 0)) return v.toExponential(2);
    return v.toFixed(dec);
  }

  /* =========================================================================
     1. COLORES — se leen de curso.css para heredar la semántica del curso
     ========================================================================= */

  const RESPALDO = {
    papel: '#fbf4e8', papel2: '#f4ead9', papel3: '#ece0cb',
    tinta: '#2a2521', tinta2: '#59504a', tinta3: '#8c8079', borde: '#d9c9ae',
    datos: '#33302c', verdad: '#9a9089', modelo: '#1f6fb5', parametro: '#8244c4',
    error: '#cf3b28', val: '#e08519', ok: '#2f8a56', acento: '#0d9488',
    fondo: '#fffaf1', grilla: '#e6d9c0', eje: '#6f645c', texto: '#3a342f',
    fuente: 'system-ui, sans-serif', mono: 'monospace'
  };

  const MAPA_VARS = {
    papel: '--papel', papel2: '--papel-2', papel3: '--papel-3',
    tinta: '--tinta', tinta2: '--tinta-2', tinta3: '--tinta-3', borde: '--borde',
    datos: '--c-datos', verdad: '--c-verdad', modelo: '--c-modelo',
    parametro: '--c-parametro', error: '--c-error', val: '--c-val',
    ok: '--c-ok', acento: '--c-acento',
    fondo: '--viz-fondo', grilla: '--viz-grilla', eje: '--viz-eje', texto: '--viz-texto',
    fuente: '--f-texto', mono: '--f-mono'
  };

  let _cache = null;

  /** Devuelve el objeto de colores del curso, leído de las variables CSS.
   *  Claves: papel, papel2, papel3, tinta, tinta2, tinta3, borde, datos, verdad,
   *  modelo, parametro, error, val, ok, acento, fondo, grilla, eje, texto.
   *  @example Viz.colores().error // "#cf3b28" */
  function colores(recargar) {
    if (_cache && !recargar) return _cache;
    const c = Object.assign({}, RESPALDO);
    try {
      const cs = getComputedStyle(document.documentElement);
      for (const k in MAPA_VARS) {
        const v = cs.getPropertyValue(MAPA_VARS[k]).trim();
        if (v) c[k] = v;
      }
    } catch (e) { /* file:// sin CSS: nos quedamos con el respaldo */ }
    _cache = c;
    return c;
  }

  /** Vuelve a leer los colores (llamalo si cambiaste el tema claro/oscuro).
   *  @example Viz.recargarColores(); */
  function recargarColores() { return colores(true); }

  /** Resuelve un nombre semántico a color. Si ya es un color literal, lo devuelve.
   *  @example Viz.color('error')   // "#cf3b28"
   *  @example Viz.color('#123456') // "#123456" */
  function color(nombre) {
    if (!nombre) return colores().tinta;
    // Si llega algo que no es texto (true, un numero, un objeto) no reventamos
    // la pagina entera: devolvemos el color por defecto. Un dibujo feo se ve;
    // una excepcion aca corta el resto del alDibujar y la slide queda en blanco.
    if (typeof nombre !== 'string') return colores().tinta;
    if (nombre[0] === '#' || nombre.indexOf('rgb') === 0 || nombre.indexOf('hsl') === 0) return nombre;
    const c = colores();
    return c[nombre] !== undefined ? c[nombre] : nombre;
  }

  function _rgb(c) {
    c = color(c);
    if (c[0] === '#') {
      let h = c.slice(1);
      if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
      return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
    }
    const m = c.match(/[\d.]+/g);
    return m ? [+m[0], +m[1], +m[2]] : [0, 0, 0];
  }

  /** Mismo color con transparencia.  @example Viz.alfa('modelo', .2) */
  function alfa(c, a) { const r = _rgb(c); return 'rgba(' + r[0] + ',' + r[1] + ',' + r[2] + ',' + a + ')'; }

  /** Mezcla dos colores.  @example Viz.mezclarColor('ok','error',.5) */
  function mezclarColor(c1, c2, t) {
    const a = _rgb(c1), b = _rgb(c2);
    return 'rgb(' + Math.round(mezclar(a[0], b[0], t)) + ',' +
      Math.round(mezclar(a[1], b[1], t)) + ',' + Math.round(mezclar(a[2], b[2], t)) + ')';
  }

  /** Paletas para mapas de calor. Devuelve función t∈[0,1] -> color css.
   *  - 'loss'        : papel -> val -> error  (para superficies de pérdida)
   *  - 'divergente'  : modelo <- blanco -> error (para pesos con signo)
   *  - 'acento'      : papel -> acento (para atención, similitud)
   *  - 'grises'
   *  @example const pal = Viz.paleta('loss'); pal(0.8) */
  function paleta(nombre) {
    const c = colores();
    if (nombre === 'divergente') {
      return function (t) {
        t = acotar(t, 0, 1);
        return t < .5 ? mezclarColor(c.modelo, c.papel, t * 2)
                      : mezclarColor(c.papel, c.error, (t - .5) * 2);
      };
    }
    if (nombre === 'acento') {
      return function (t) { return mezclarColor(c.papel, c.acento, acotar(t, 0, 1)); };
    }
    if (nombre === 'grises') {
      return function (t) { return mezclarColor(c.papel, c.tinta, acotar(t, 0, 1)); };
    }
    // 'loss' por defecto: fondo claro en el valle, rojo en las alturas
    return function (t) {
      t = acotar(t, 0, 1);
      if (t < .35) return mezclarColor(c.papel, c.ok, t / .35 * .55);
      if (t < .7)  return mezclarColor(mezclarColor(c.papel, c.ok, .55), c.val, (t - .35) / .35);
      return mezclarColor(c.val, c.error, (t - .7) / .3);
    };
  }

  /* =========================================================================
     2. TOOLTIP GLOBAL
     ========================================================================= */
  let _tt = null;
  function _tooltipEl() {
    if (!_tt) { _tt = el('div', { class: 'viz-tooltip' }); document.body.appendChild(_tt); }
    return _tt;
  }
  /** Muestra el tooltip flotante.  @example Viz.mostrarTooltip(ev, "x=3\ny=8") */
  function mostrarTooltip(ev, texto) {
    const t = _tooltipEl();
    t.textContent = texto;
    t.classList.add('visible');
    t.style.left = (ev.clientX + 14) + 'px';
    t.style.top = (ev.clientY - 10) + 'px';
  }
  /** Esconde el tooltip.  @example Viz.ocultarTooltip(); */
  function ocultarTooltip() { if (_tt) _tt.classList.remove('visible'); }

  /* =========================================================================
     3. PLANO CARTESIANO
     ========================================================================= */

  /**
   * Crea un plano cartesiano sobre un canvas dentro del contenedor dado.
   * Maneja retina (devicePixelRatio), redimensionado, mapeo mundo<->pixel,
   * interacción (hover, clic, arrastre) y el redibujado.
   *
   * Opciones: {ancho, alto, xmin, xmax, ymin, ymax, margen:{i,d,a,b},
   *            ejeX, ejeY, titulo, cuadrado}
   *
   * @example
   *   const p = Viz.plano('#lienzo', { xmin:1983, xmax:2023, ymin:0, ymax:12,
   *                                    ejeX:'año', ejeY:'% de palabras' });
   *   p.alDibujar(() => { p.fondo(); p.grilla(); p.ejes();
   *                       p.puntos(datos, { color:'datos' }); });
   *   p.redibujar();
   */
  function Plano(contenedor, op) {
    op = op || {};
    const cont = nodo(contenedor);
    if (!cont) throw new Error('Viz.plano: no encontré el contenedor ' + contenedor);
    this.cont = cont;
    this.canvas = el('canvas', { class: 'viz-canvas' }, cont);
    this.canvas.style.display = 'block';
    this.canvas.style.width = '100%';
    this.ctx = this.canvas.getContext('2d');

    this.xmin = op.xmin !== undefined ? op.xmin : 0;
    this.xmax = op.xmax !== undefined ? op.xmax : 1;
    this.ymin = op.ymin !== undefined ? op.ymin : 0;
    this.ymax = op.ymax !== undefined ? op.ymax : 1;
    this.ejeX = op.ejeX || '';
    this.ejeY = op.ejeY || '';
    this.titulo = op.titulo || '';
    this.cuadrado = !!op.cuadrado;
    this.altoFijo = op.alto || null;
    this.relacion = op.relacion || 0.62;   // alto/ancho si no hay alto fijo
    const m = op.margen || {};
    this.margen = {
      i: m.i !== undefined ? m.i : (this.ejeY ? 64 : 40),
      d: m.d !== undefined ? m.d : 16,
      a: m.a !== undefined ? m.a : (this.titulo ? 30 : 14),
      b: m.b !== undefined ? m.b : (this.ejeX ? 46 : 32)
    };

    this._dibujo = null;
    this._arrastrables = null;
    this._tooltip = null;
    this._clic = null;
    this._mover = null;
    this._activo = null;
    this._pendiente = false;

    this.redimensionar();
    this._conectarEventos();

    const self = this;
    if (global.ResizeObserver) {
      this._ro = new ResizeObserver(function () { self.redimensionar(); self.redibujar(); });
      this._ro.observe(cont);
    } else {
      global.addEventListener('resize', function () { self.redimensionar(); self.redibujar(); });
    }
  }

  Plano.prototype.redimensionar = function () {
    const dpr = global.devicePixelRatio || 1;
    let w = this.cont.clientWidth || 600;
    let h = this.altoFijo || Math.round(w * this.relacion);
    if (this.cuadrado) h = this.altoFijo || w;
    this.ancho = w; this.alto = h;
    this.canvas.width = Math.round(w * dpr);
    this.canvas.height = Math.round(h * dpr);
    this.canvas.style.height = h + 'px';
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.L = this.margen.i;
    this.R = w - this.margen.d;
    this.T = this.margen.a;
    this.B = h - this.margen.b;
    return this;
  };

  /** Cambia los límites del mundo.  @example p.limites(-2, 2, -1, 5) */
  Plano.prototype.limites = function (xmin, xmax, ymin, ymax) {
    this.xmin = xmin; this.xmax = xmax; this.ymin = ymin; this.ymax = ymax;
    return this;
  };

  /** Ajusta los límites para que entren los puntos dados, con margen.
   *  @example p.autoescala(datos, { margen:.12 }); */
  Plano.prototype.autoescala = function (pts, op) {
    op = op || {};
    if (!pts || !pts.length) return this;
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    for (const p of pts) {
      const x = p.x !== undefined ? p.x : p[0], y = p.y !== undefined ? p.y : p[1];
      if (x < x0) x0 = x; if (x > x1) x1 = x;
      if (y < y0) y0 = y; if (y > y1) y1 = y;
    }
    const mg = op.margen !== undefined ? op.margen : 0.1;
    const dx = (x1 - x0) || 1, dy = (y1 - y0) || 1;
    this.xmin = op.xmin !== undefined ? op.xmin : x0 - dx * mg;
    this.xmax = op.xmax !== undefined ? op.xmax : x1 + dx * mg;
    this.ymin = op.ymin !== undefined ? op.ymin : y0 - dy * mg;
    this.ymax = op.ymax !== undefined ? op.ymax : y1 + dy * mg;
    return this;
  };

  /** Mundo -> pixel (coordenada x).  @example p.px(2015) */
  Plano.prototype.px = function (x) {
    return this.L + (x - this.xmin) / (this.xmax - this.xmin) * (this.R - this.L);
  };
  /** Mundo -> pixel (coordenada y).  @example p.py(3.5) */
  Plano.prototype.py = function (y) {
    return this.B - (y - this.ymin) / (this.ymax - this.ymin) * (this.B - this.T);
  };
  /** Pixel -> mundo. Devuelve {x,y}.  @example p.aMundo(120, 80) */
  Plano.prototype.aMundo = function (px, py) {
    return {
      x: this.xmin + (px - this.L) / (this.R - this.L) * (this.xmax - this.xmin),
      y: this.ymin + (this.B - py) / (this.B - this.T) * (this.ymax - this.ymin)
    };
  };
  /** Cuántos pixeles mide una distancia del mundo en x.  @example p.escalaX(1) */
  Plano.prototype.escalaX = function (d) { return d / (this.xmax - this.xmin) * (this.R - this.L); };
  /** Ídem en y.  @example p.escalaY(1) */
  Plano.prototype.escalaY = function (d) { return d / (this.ymax - this.ymin) * (this.B - this.T); };

  /** Borra todo el canvas.  @example p.limpiar(); */
  Plano.prototype.limpiar = function () {
    this.ctx.clearRect(0, 0, this.ancho, this.alto);
    return this;
  };

  /** Pinta el fondo de papel del área de dibujo.  @example p.fondo(); */
  Plano.prototype.fondo = function (op) {
    op = op || {};
    const c = this.ctx;
    this.limpiar();
    c.fillStyle = color(op.color || 'fondo');
    c.fillRect(0, 0, this.ancho, this.alto);
    if (op.marco !== false) {
      c.strokeStyle = alfa('borde', .9); c.lineWidth = 1;
      c.strokeRect(this.L + .5, this.T + .5, this.R - this.L - 1, this.B - this.T - 1);
    }
    if (this.titulo) {
      c.fillStyle = color('tinta3');
      c.font = '600 11px ' + colores().fuente;
      c.textAlign = 'left'; c.textBaseline = 'alphabetic';
      c.fillText(this.titulo.toUpperCase(), this.L, this.T - 10);
    }
    return this;
  };

  function _ticks(a, b, objetivo) {
    const span = b - a;
    if (!(span > 0)) return [a];
    const bruto = span / (objetivo || 6);
    const mag = Math.pow(10, Math.floor(Math.log10(bruto)));
    const norm = bruto / mag;
    const paso = (norm < 1.5 ? 1 : norm < 3 ? 2 : norm < 7 ? 5 : 10) * mag;
    const t = [];
    for (let v = Math.ceil(a / paso) * paso; v <= b + paso * 1e-9; v += paso) {
      t.push(Math.abs(v) < paso * 1e-9 ? 0 : v);
    }
    return t;
  }

  function _decTicks(t) {
    if (!t || t.length < 2) return 2;
    const paso = Math.abs(t[1] - t[0]);
    if (!(paso > 0)) return 2;
    return Math.min(6, Math.max(0, -Math.floor(Math.log10(paso) + 1e-9)));
  }
  function _fmtEje(ticks) {
    const d = _decTicks(ticks);
    return function (v) {
      if (Math.abs(v) >= 1e5) return v.toExponential(1);
      return (Math.abs(v) < Math.pow(10, -d) / 2 ? 0 : v).toFixed(d);
    };
  }

  /** Grilla de fondo.  @example p.grilla({ x:8, y:5 }); */
  Plano.prototype.grilla = function (op) {
    op = op || {};
    const c = this.ctx;
    c.save();
    c.strokeStyle = color(op.color || 'grilla');
    c.lineWidth = 1;
    const tx = op.ticksX || _ticks(this.xmin, this.xmax, op.x || 7);
    const ty = op.ticksY || _ticks(this.ymin, this.ymax, op.y || 5);
    c.beginPath();
    for (const v of tx) { const X = Math.round(this.px(v)) + .5; c.moveTo(X, this.T); c.lineTo(X, this.B); }
    for (const v of ty) { const Y = Math.round(this.py(v)) + .5; c.moveTo(this.L, Y); c.lineTo(this.R, Y); }
    c.stroke();
    c.restore();
    this._tx = tx; this._ty = ty;
    return this;
  };

  /** Ejes con ticks, números y nombres.  @example p.ejes({ formatoX: v=>v|0 }); */
  Plano.prototype.ejes = function (op) {
    op = op || {};
    const c = this.ctx, col = colores();
    const tx = op.ticksX || this._tx || _ticks(this.xmin, this.xmax, 7);
    const ty = op.ticksY || this._ty || _ticks(this.ymin, this.ymax, 5);
    const fX = op.formatoX || _fmtEje(tx);
    const fY = op.formatoY || _fmtEje(ty);
    c.save();
    c.strokeStyle = color('eje'); c.lineWidth = 1.4;
    c.beginPath();
    c.moveTo(this.L, this.B + .5); c.lineTo(this.R, this.B + .5);
    c.moveTo(this.L + .5, this.T); c.lineTo(this.L + .5, this.B);
    c.stroke();

    // eje x=0 / y=0 más marcados si caen adentro
    c.strokeStyle = alfa('eje', .55); c.lineWidth = 1.6;
    c.beginPath();
    if (this.ymin < 0 && this.ymax > 0) { const Y = this.py(0); c.moveTo(this.L, Y); c.lineTo(this.R, Y); }
    if (this.xmin < 0 && this.xmax > 0) { const X = this.px(0); c.moveTo(X, this.T); c.lineTo(X, this.B); }
    c.stroke();

    c.fillStyle = color('tinta3');
    c.font = '11px ' + col.mono;
    c.textAlign = 'center'; c.textBaseline = 'top';
    for (const v of tx) {
      const X = this.px(v); if (X < this.L - 1 || X > this.R + 1) continue;
      c.strokeStyle = color('eje'); c.beginPath();
      c.moveTo(X, this.B); c.lineTo(X, this.B + 4); c.stroke();
      c.fillText(fX(v), X, this.B + 7);
    }
    c.textAlign = 'right'; c.textBaseline = 'middle';
    for (const v of ty) {
      const Y = this.py(v); if (Y < this.T - 1 || Y > this.B + 1) continue;
      c.strokeStyle = color('eje'); c.beginPath();
      c.moveTo(this.L - 4, Y); c.lineTo(this.L, Y); c.stroke();
      c.fillText(fY(v), this.L - 7, Y);
    }
    c.fillStyle = color('tinta2');
    c.font = '600 11px ' + col.fuente;
    if (this.ejeX) {
      c.textAlign = 'right'; c.textBaseline = 'bottom';
      c.fillText(this.ejeX, this.R, this.alto - 4);
    }
    if (this.ejeY) {
      c.save();
      c.translate(13, this.T);
      c.rotate(-Math.PI / 2);
      c.textAlign = 'right'; c.textBaseline = 'top';
      c.fillText(this.ejeY, 0, 0);
      c.restore();
    }
    c.restore();
    return this;
  };

  Plano.prototype._recorte = function () {
    const c = this.ctx;
    c.save(); c.beginPath();
    c.rect(this.L, this.T, this.R - this.L, this.B - this.T);
    c.clip();
  };

  /** Dibuja la curva y = f(x).
   *  @example p.curva(x => a*x + b, { color:'modelo', grosor:3 }); */
  Plano.prototype.curva = function (f, op) {
    op = op || {};
    const c = this.ctx, n = op.n || 400;
    this._recorte();
    c.strokeStyle = color(op.color || 'modelo');
    c.lineWidth = op.grosor || 2.5;
    c.lineJoin = 'round'; c.lineCap = 'round';
    if (op.punteada) c.setLineDash(op.punteada === true ? [6, 5] : op.punteada);
    if (op.opacidad !== undefined) c.globalAlpha = op.opacidad;
    c.beginPath();
    let arranco = false;
    for (let i = 0; i <= n; i++) {
      const x = this.xmin + (this.xmax - this.xmin) * i / n;
      const y = f(x);
      if (!isFinite(y)) { arranco = false; continue; }
      const X = this.px(x), Y = this.py(y);
      const fuera = Y < this.T - 3000 || Y > this.B + 3000;
      if (fuera) { arranco = false; continue; }
      if (!arranco) { c.moveTo(X, Y); arranco = true; } else c.lineTo(X, Y);
    }
    c.stroke();
    c.restore();
    return this;
  };

  /** Polilínea por una lista de puntos ([{x,y}] o [[x,y]]).
   *  @example p.linea(historia, { color:'error', grosor:2 }); */
  Plano.prototype.linea = function (pts, op) {
    op = op || {};
    if (!pts || pts.length < 2) return this;
    const c = this.ctx;
    this._recorte();
    c.strokeStyle = color(op.color || 'modelo');
    c.lineWidth = op.grosor || 2;
    c.lineJoin = 'round'; c.lineCap = 'round';
    if (op.punteada) c.setLineDash(op.punteada === true ? [6, 5] : op.punteada);
    if (op.opacidad !== undefined) c.globalAlpha = op.opacidad;
    c.beginPath();
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      const x = p.x !== undefined ? p.x : p[0], y = p.y !== undefined ? p.y : p[1];
      const X = this.px(x), Y = this.py(y);
      if (i === 0) c.moveTo(X, Y); else c.lineTo(X, Y);
    }
    c.stroke();
    c.restore();
    return this;
  };

  /** Polígono relleno (área bajo una curva, banda de confianza, etc.).
   *  `color` tiñe el relleno con transparencia (lo habitual). `relleno` acepta
   *  un color css explícito, `true` (usa `color`) o `false` (no rellena).
   *  @example p.poligono(pts, { color:'modelo' });
   *  @example p.poligono(pts, { relleno: Viz.alfa('modelo',.15), borde:'modelo' }); */
  Plano.prototype.poligono = function (pts, op) {
    op = op || {};
    const c = this.ctx;
    this._recorte();
    c.beginPath();
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      const x = p.x !== undefined ? p.x : p[0], y = p.y !== undefined ? p.y : p[1];
      const X = this.px(x), Y = this.py(y);
      if (i === 0) c.moveTo(X, Y); else c.lineTo(X, Y);
    }
    c.closePath();
    if (op.relleno !== false) {
      const base = op.color || 'modelo';
      const tinte = (op.relleno && op.relleno !== true) ? color(op.relleno)
        : alfa(base, op.opacidad !== undefined ? op.opacidad : .18);
      c.fillStyle = tinte;
      c.fill();
    }
    if (op.borde) {
      c.strokeStyle = color(op.borde === true ? (op.color || 'modelo') : op.borde);
      c.lineWidth = op.grosor || 1.5;
      c.stroke();
    }
    c.restore();
    return this;
  };

  /** Nube de puntos.  Acepta [{x,y,color?,r?}] o [[x,y]].
   *  @example p.puntos(datos, { color:'datos', r:5 }); */
  Plano.prototype.puntos = function (pts, op) {
    op = op || {};
    const c = this.ctx;
    const r = op.r || 4.5;
    this._recorte();
    for (const p of pts) {
      const x = p.x !== undefined ? p.x : p[0], y = p.y !== undefined ? p.y : p[1];
      const X = this.px(x), Y = this.py(y);
      const col = color(p.color || op.color || 'datos');
      const rr = p.r || r;
      c.beginPath(); c.arc(X, Y, rr, 0, 6.2832);
      if (op.hueco) {
        c.strokeStyle = col; c.lineWidth = op.grosor || 2; c.stroke();
      } else {
        c.fillStyle = col; c.fill();
        if (op.borde !== false) {
          c.strokeStyle = color(op.borde || 'fondo'); c.lineWidth = op.grosorBorde || 1.5; c.stroke();
        }
      }
      if (p.etiqueta) {
        c.fillStyle = color('tinta2'); c.font = '10px ' + colores().mono;
        c.textAlign = 'center'; c.textBaseline = 'bottom';
        c.fillText(p.etiqueta, X, Y - rr - 3);
      }
    }
    c.restore();
    return this;
  };

  /** Un punto solo, con halo opcional (el punto arrastrable del mapa de loss).
   *  @example p.punto(a, b, { color:'parametro', r:8, halo:true }); */
  Plano.prototype.punto = function (x, y, op) {
    op = op || {};
    const c = this.ctx, X = this.px(x), Y = this.py(y), r = op.r || 7;
    c.save();
    if (op.halo) {
      c.beginPath(); c.arc(X, Y, r * 2.4, 0, 6.2832);
      c.fillStyle = alfa(op.color || 'parametro', .18); c.fill();
    }
    c.beginPath(); c.arc(X, Y, r, 0, 6.2832);
    c.fillStyle = color(op.color || 'parametro'); c.fill();
    c.strokeStyle = color(op.borde || 'fondo'); c.lineWidth = op.grosorBorde || 2.5; c.stroke();
    c.restore();
    return this;
  };

  /** Segmento entre dos puntos del mundo (los palitos rojos del error).
   *  @example p.segmento(x, yDato, x, yPred, { color:'error', punteada:true }); */
  Plano.prototype.segmento = function (x1, y1, x2, y2, op) {
    op = op || {};
    const c = this.ctx;
    this._recorte();
    c.strokeStyle = color(op.color || 'error');
    c.lineWidth = op.grosor || 2;
    c.lineCap = 'round';
    if (op.punteada) c.setLineDash(op.punteada === true ? [4, 4] : op.punteada);
    if (op.opacidad !== undefined) c.globalAlpha = op.opacidad;
    c.beginPath(); c.moveTo(this.px(x1), this.py(y1)); c.lineTo(this.px(x2), this.py(y2)); c.stroke();
    c.restore();
    return this;
  };

  /** Flecha / vector (el −gradiente en el mapa de loss).
   *  @example p.flecha(a, b, a-ga, b-gb, { color:'parametro', cabeza:11 }); */
  Plano.prototype.flecha = function (x1, y1, x2, y2, op) {
    op = op || {};
    const c = this.ctx;
    const X1 = this.px(x1), Y1 = this.py(y1), X2 = this.px(x2), Y2 = this.py(y2);
    const ang = Math.atan2(Y2 - Y1, X2 - X1);
    const largo = Math.hypot(X2 - X1, Y2 - Y1);
    if (largo < 1) return this;
    const cab = Math.min(op.cabeza || 10, largo * .5);
    c.save();
    c.strokeStyle = color(op.color || 'parametro');
    c.fillStyle = color(op.color || 'parametro');
    c.lineWidth = op.grosor || 2.5; c.lineCap = 'round';
    c.beginPath();
    c.moveTo(X1, Y1); c.lineTo(X2 - Math.cos(ang) * cab * .8, Y2 - Math.sin(ang) * cab * .8);
    c.stroke();
    c.beginPath();
    c.moveTo(X2, Y2);
    c.lineTo(X2 - Math.cos(ang - .42) * cab, Y2 - Math.sin(ang - .42) * cab);
    c.lineTo(X2 - Math.cos(ang + .42) * cab, Y2 - Math.sin(ang + .42) * cab);
    c.closePath(); c.fill();
    if (op.etiqueta) {
      c.fillStyle = color('tinta2'); c.font = '600 11px ' + colores().fuente;
      c.textAlign = 'left'; c.textBaseline = 'middle';
      c.fillText(op.etiqueta, X2 + 8, Y2);
    }
    c.restore();
    return this;
  };

  /** Texto en coordenadas del mundo.
   *  @example p.texto(2000, 9, 'acá pasa algo', { color:'acento', tam:14 }); */
  Plano.prototype.texto = function (x, y, txt, op) {
    op = op || {};
    const c = this.ctx;
    c.save();
    c.fillStyle = color(op.color || 'tinta');
    c.font = (op.peso || '500') + ' ' + (op.tam || 12) + 'px ' + (op.mono ? colores().mono : colores().fuente);
    c.textAlign = op.alinear || 'left';
    c.textBaseline = op.base || 'middle';
    const X = this.px(x) + (op.dx || 0), Y = this.py(y) + (op.dy || 0);
    if (op.caja) {
      const w = c.measureText(txt).width, h = (op.tam || 12) * 1.4;
      const bx = op.alinear === 'center' ? X - w / 2 - 5 : (op.alinear === 'right' ? X - w - 5 : X - 5);
      c.fillStyle = color(op.caja === true ? 'fondo' : op.caja);
      c.globalAlpha = .88;
      c.fillRect(bx, Y - h / 2, w + 10, h);
      c.globalAlpha = 1;
      c.fillStyle = color(op.color || 'tinta');
    }
    c.fillText(txt, X, Y);
    c.restore();
    return this;
  };

  /** Texto en pixeles (para rótulos fijos en una esquina).
   *  @example p.textoPx(p.R-10, p.T+10, 'loss = 0.42', { alinear:'right' }); */
  Plano.prototype.textoPx = function (X, Y, txt, op) {
    op = op || {};
    const c = this.ctx;
    c.save();
    c.fillStyle = color(op.color || 'tinta');
    c.font = (op.peso || '500') + ' ' + (op.tam || 12) + 'px ' + (op.mono ? colores().mono : colores().fuente);
    c.textAlign = op.alinear || 'left';
    c.textBaseline = op.base || 'top';
    if (op.caja) {
      const w = c.measureText(txt).width, h = (op.tam || 12) * 1.5;
      const bx = c.textAlign === 'right' ? X - w - 6 : (c.textAlign === 'center' ? X - w / 2 - 6 : X - 6);
      const by = c.textBaseline === 'bottom' ? Y - h : (c.textBaseline === 'middle' ? Y - h / 2 : Y - 2);
      c.fillStyle = alfa(op.caja === true ? 'fondo' : op.caja, op.opacidadCaja !== undefined ? op.opacidadCaja : .88);
      if (c.roundRect) { c.beginPath(); c.roundRect(bx, by, w + 12, h, 5); c.fill(); }
      else c.fillRect(bx, by, w + 12, h);
      c.fillStyle = color(op.color || 'tinta');
    }
    c.fillText(txt, X, Y);
    c.restore();
    return this;
  };

  /** Barras. items = [{etiqueta, valor, color?}]. Escala sola.
   *  Sirve para la viz de temperatura (horizontal) y para F1 por clase (vertical).
   *  @example p.barras(fichas, { horizontal:true, formato: v => (v*100).toFixed(1)+'%' }); */
  Plano.prototype.barras = function (items, op) {
    op = op || {};
    const c = this.ctx;
    const max = op.max !== undefined ? op.max : Math.max.apply(null, items.map(function (d) { return d.valor; }).concat([1e-9]));
    const n = items.length;
    const fmt = op.formato || function (v) { return num(v); };
    const col = colores();
    c.save();
    if (op.horizontal) {
      const h = (this.B - this.T) / n, bh = h * (op.grosor || .68);
      for (let i = 0; i < n; i++) {
        const d = items[i], Y = this.T + h * (i + .5);
        const w = Math.max(0, d.valor / max) * (this.R - this.L - 160);
        c.fillStyle = color(d.color || op.color || 'acento');
        c.globalAlpha = op.opacidad || 1;
        c.fillRect(this.L + 96, Y - bh / 2, w, bh);
        c.globalAlpha = 1;
        c.fillStyle = color('tinta'); c.font = '12px ' + col.fuente;
        c.textAlign = 'right'; c.textBaseline = 'middle';
        c.fillText(d.etiqueta, this.L + 88, Y);
        c.fillStyle = color('tinta2'); c.font = '600 11px ' + col.mono;
        c.textAlign = 'left';
        c.fillText(fmt(d.valor), this.L + 96 + w + 6, Y);
      }
    } else {
      const w = (this.R - this.L) / n, bw = w * (op.grosor || .66);
      for (let i = 0; i < n; i++) {
        const d = items[i], X = this.L + w * (i + .5);
        const h = Math.max(0, d.valor / max) * (this.B - this.T - 18);
        c.fillStyle = color(d.color || op.color || 'acento');
        c.fillRect(X - bw / 2, this.B - h, bw, h);
        c.fillStyle = color('tinta2'); c.font = '11px ' + col.fuente;
        c.textAlign = 'center'; c.textBaseline = 'top';
        c.fillText(d.etiqueta, X, this.B + 6);
        c.fillStyle = color('tinta'); c.font = '600 11px ' + col.mono;
        c.textBaseline = 'bottom';
        c.fillText(fmt(d.valor), X, this.B - h - 3);
      }
    }
    c.restore();
    return this;
  };

  /** Mapa de calor de una superficie z = f(x,y) sobre todo el plano.
   *  Devuelve {min,max} por si querés poner una escala.
   *  @example p.mapaDeCalor((a,b) => loss(a,b), { n:110, paleta:'loss' }); */
  Plano.prototype.mapaDeCalor = function (f, op) {
    op = op || {};
    const n = op.n || 90, m = op.m || Math.round(n * (this.B - this.T) / (this.R - this.L));
    const W = this.R - this.L, H = this.B - this.T;
    const z = new Float64Array(n * m);
    let zmin = Infinity, zmax = -Infinity;
    for (let j = 0; j < m; j++) {
      const y = this.ymax - (j + .5) / m * (this.ymax - this.ymin);
      for (let i = 0; i < n; i++) {
        const x = this.xmin + (i + .5) / n * (this.xmax - this.xmin);
        let v = f(x, y);
        if (!isFinite(v)) v = NaN;
        z[j * n + i] = v;
        if (v < zmin) zmin = v; if (v > zmax) zmax = v;
      }
    }
    if (op.min !== undefined) zmin = op.min;
    if (op.max !== undefined) zmax = op.max;
    const pal = typeof op.paleta === 'function' ? op.paleta : paleta(op.paleta || 'loss');
    const tr = op.transformar || (op.log ? function (t) { return Math.log(1 + 9 * t) / Math.log(10); } : null);
    const off = document.createElement('canvas');
    off.width = n; off.height = m;
    const oc = off.getContext('2d');
    const img = oc.createImageData(n, m);
    for (let k = 0; k < n * m; k++) {
      let t = (z[k] - zmin) / ((zmax - zmin) || 1);
      if (tr) t = tr(acotar(t, 0, 1));
      const rgbv = _rgb(pal(acotar(t, 0, 1)));
      img.data[k * 4] = rgbv[0]; img.data[k * 4 + 1] = rgbv[1];
      img.data[k * 4 + 2] = rgbv[2]; img.data[k * 4 + 3] = isFinite(z[k]) ? 255 : 0;
    }
    oc.putImageData(img, 0, 0);
    const c = this.ctx;
    c.save();
    c.imageSmoothingEnabled = op.suavizar !== false;
    c.drawImage(off, this.L, this.T, W, H);
    c.restore();
    this._ultimaSuperficie = { z: z, n: n, m: m, min: zmin, max: zmax };
    return { min: zmin, max: zmax };
  };

  /** Curvas de nivel (marching squares) sobre z = f(x,y). Se dibuja ENCIMA del
   *  mapa de calor para que el valle se lea como un mapa topográfico.
   *  @example p.contornos(loss, { niveles:12, color:'tinta3' }); */
  Plano.prototype.contornos = function (f, op) {
    op = op || {};
    const n = op.n || 70, m = op.m || 55;
    const xs = linspace(this.xmin, this.xmax, n), ys = linspace(this.ymin, this.ymax, m);
    const z = [];
    let zmin = Infinity, zmax = -Infinity;
    for (let j = 0; j < m; j++) {
      z.push([]);
      for (let i = 0; i < n; i++) {
        const v = f(xs[i], ys[j]);
        z[j].push(v);
        if (isFinite(v)) { if (v < zmin) zmin = v; if (v > zmax) zmax = v; }
      }
    }
    let niveles = op.niveles;
    if (typeof niveles === 'number' || niveles === undefined) {
      const k = niveles || 10;
      niveles = [];
      const escLog = op.log !== false;
      for (let i = 1; i <= k; i++) {
        const t = i / (k + 1);
        niveles.push(zmin + (zmax - zmin) * (escLog ? t * t : t));
      }
    }
    const c = this.ctx;
    this._recorte();
    c.strokeStyle = alfa(op.color || 'tinta3', op.opacidad !== undefined ? op.opacidad : .45);
    c.lineWidth = op.grosor || 1;
    c.beginPath();
    const self = this;
    function pt(x, y) { return [self.px(x), self.py(y)]; }
    for (const niv of niveles) {
      for (let j = 0; j < m - 1; j++) {
        for (let i = 0; i < n - 1; i++) {
          const v = [z[j][i], z[j][i + 1], z[j + 1][i + 1], z[j + 1][i]];
          const px = [xs[i], xs[i + 1], xs[i + 1], xs[i]];
          const py = [ys[j], ys[j], ys[j + 1], ys[j + 1]];
          const cortes = [];
          for (let e = 0; e < 4; e++) {
            const a = v[e], b = v[(e + 1) % 4];
            if (!isFinite(a) || !isFinite(b)) continue;
            if ((a - niv) * (b - niv) < 0) {
              const t = (niv - a) / (b - a);
              cortes.push(pt(mezclar(px[e], px[(e + 1) % 4], t), mezclar(py[e], py[(e + 1) % 4], t)));
            }
          }
          if (cortes.length >= 2) {
            c.moveTo(cortes[0][0], cortes[0][1]); c.lineTo(cortes[1][0], cortes[1][1]);
            if (cortes.length === 4) { c.moveTo(cortes[2][0], cortes[2][1]); c.lineTo(cortes[3][0], cortes[3][1]); }
          }
        }
      }
    }
    c.stroke();
    c.restore();
    return this;
  };

  /** Grilla de celdas coloreadas (un filtro 3x3, una matriz de atención, one-hot).
   *  M es un array de arrays. Se dibuja en coordenadas del mundo.
   *  @example p.celdas(K, { x0:0, y0:0, ancho:3, alto:3, paleta:'divergente', texto:true }); */
  Plano.prototype.celdas = function (M, op) {
    op = op || {};
    const filas = M.length, cols = M[0].length;
    const x0 = op.x0 !== undefined ? op.x0 : this.xmin;
    const y0 = op.y0 !== undefined ? op.y0 : this.ymin;
    const W = op.ancho !== undefined ? op.ancho : (this.xmax - this.xmin);
    const H = op.alto !== undefined ? op.alto : (this.ymax - this.ymin);
    let mn = Infinity, mx = -Infinity;
    for (const f of M) for (const v of f) { if (v < mn) mn = v; if (v > mx) mx = v; }
    if (op.min !== undefined) mn = op.min;
    if (op.max !== undefined) mx = op.max;
    if (op.simetrico) { const a = Math.max(Math.abs(mn), Math.abs(mx)); mn = -a; mx = a; }
    const pal = typeof op.paleta === 'function' ? op.paleta : paleta(op.paleta || 'acento');
    const c = this.ctx;
    const cw = this.escalaX(W / cols), ch = this.escalaY(H / filas);
    c.save();
    for (let j = 0; j < filas; j++) {
      for (let i = 0; i < cols; i++) {
        const X = this.px(x0 + W * i / cols), Y = this.py(y0 + H * (filas - j) / filas);
        const t = (M[j][i] - mn) / ((mx - mn) || 1);
        c.fillStyle = pal(acotar(t, 0, 1));
        c.fillRect(X, Y, cw + .5, ch + .5);
        if (op.borde !== false) {
          c.strokeStyle = alfa('borde', .8); c.lineWidth = 1;
          c.strokeRect(X + .5, Y + .5, cw, ch);
        }
        if (op.texto) {
          const fmt = typeof op.texto === 'function' ? op.texto : function (v) { return num(v, 2); };
          c.fillStyle = t > .62 ? color('papel') : color('tinta');
          c.font = '600 ' + Math.max(8, Math.min(13, cw * .32)) + 'px ' + colores().mono;
          c.textAlign = 'center'; c.textBaseline = 'middle';
          c.fillText(fmt(M[j][i], j, i), X + cw / 2, Y + ch / 2);
        }
      }
    }
    if (op.resaltar) {
      const [rj, ri] = op.resaltar;
      const X = this.px(x0 + W * ri / cols), Y = this.py(y0 + H * (filas - rj) / filas);
      c.strokeStyle = color('acento'); c.lineWidth = 3;
      c.strokeRect(X + 1, Y + 1, cw - 2, ch - 2);
    }
    c.restore();
    return this;
  };

  /** Leyenda dentro del canvas. items = [{color, texto}].
   *  @example p.leyenda([{color:'datos',texto:'observado'},{color:'modelo',texto:'modelo'}]); */
  Plano.prototype.leyenda = function (items, op) {
    op = op || {};
    const c = this.ctx, col = colores();
    c.save();
    c.font = '11px ' + col.fuente;
    let w = 0;
    for (const it of items) w = Math.max(w, c.measureText(it.texto).width);
    const anchoCaja = w + 30, altoCaja = items.length * 17 + 10;
    let X = op.x !== undefined ? op.x : (this.R - anchoCaja - 10);
    let Y = op.y !== undefined ? op.y : (this.T + 10);
    if (op.pos === 'ai') { X = this.L + 10; Y = this.T + 10; }
    if (op.pos === 'bi') { X = this.L + 10; Y = this.B - altoCaja - 10; }
    if (op.pos === 'bd') { X = this.R - anchoCaja - 10; Y = this.B - altoCaja - 10; }
    c.fillStyle = alfa('fondo', .9);
    c.strokeStyle = alfa('borde', .9); c.lineWidth = 1;
    c.beginPath();
    if (c.roundRect) c.roundRect(X, Y, anchoCaja, altoCaja, 8);
    else c.rect(X, Y, anchoCaja, altoCaja);
    c.fill(); c.stroke();
    c.textAlign = 'left'; c.textBaseline = 'middle';
    items.forEach(function (it, i) {
      const y = Y + 14 + i * 17;
      c.fillStyle = color(it.color);
      if (it.forma === 'linea') {
        c.strokeStyle = color(it.color); c.lineWidth = 3;
        if (it.punteada) c.setLineDash([4, 3]); else c.setLineDash([]);
        c.beginPath(); c.moveTo(X + 8, y); c.lineTo(X + 20, y); c.stroke();
        c.setLineDash([]);
      } else {
        c.beginPath(); c.arc(X + 14, y, 5, 0, 6.2832); c.fill();
      }
      c.fillStyle = color('tinta2');
      c.fillText(it.texto, X + 26, y);
    });
    c.restore();
    return this;
  };

  /* ------------------------------- interacción ---------------------------- */

  Plano.prototype._pos = function (ev) {
    const r = this.canvas.getBoundingClientRect();
    return { px: ev.clientX - r.left, py: ev.clientY - r.top };
  };

  Plano.prototype._conectarEventos = function () {
    const self = this;
    const cv = this.canvas;
    cv.style.touchAction = 'none';

    cv.addEventListener('pointerdown', function (ev) {
      const q = self._pos(ev);
      if (self._arrastrables) {
        const hit = self._buscarArrastrable(q.px, q.py);
        if (hit) {
          self._activo = hit;
          cv.setPointerCapture(ev.pointerId);
          cv.style.cursor = 'grabbing';
          ev.preventDefault();
          return;
        }
      }
      if (self._clic) { const w = self.aMundo(q.px, q.py); self._clic(w, ev, self); self.redibujar(); }
    });

    cv.addEventListener('pointermove', function (ev) {
      const q = self._pos(ev);
      const w = self.aMundo(q.px, q.py);
      if (self._activo) {
        const cfg = self._arrastrables;
        const p = self._activo;
        if (!cfg.fijarX) p.x = cfg.acotarX ? acotar(w.x, cfg.acotarX[0], cfg.acotarX[1]) : w.x;
        if (!cfg.fijarY) p.y = cfg.acotarY ? acotar(w.y, cfg.acotarY[0], cfg.acotarY[1]) : w.y;
        if (cfg.alArrastrar) cfg.alArrastrar(p, self);
        self.redibujar();     // en vivo, no al soltar
        return;
      }
      let cursor = 'default';
      if (self._arrastrables && self._buscarArrastrable(q.px, q.py)) cursor = 'grab';
      if (self._tooltip) {
        const t = self._tooltip(w, ev, self);
        if (t) { mostrarTooltip(ev, t); cursor = cursor === 'default' ? 'crosshair' : cursor; }
        else ocultarTooltip();
      }
      if (self._mover) self._mover(w, ev, self);
      cv.style.cursor = cursor;
    });

    function soltar(ev) {
      if (self._activo) {
        const cfg = self._arrastrables;
        if (cfg && cfg.alSoltar) cfg.alSoltar(self._activo, self);
        self._activo = null;
        self.canvas.style.cursor = 'grab';
        self.redibujar();
      }
    }
    cv.addEventListener('pointerup', soltar);
    cv.addEventListener('pointercancel', soltar);
    cv.addEventListener('pointerleave', function () { ocultarTooltip(); });
  };

  Plano.prototype._buscarArrastrable = function (px, py) {
    const cfg = this._arrastrables;
    if (!cfg) return null;
    const r = cfg.radio || 14;
    let mejor = null, dmin = r * r;
    const pts = typeof cfg.puntos === 'function' ? cfg.puntos() : cfg.puntos;
    for (const p of pts) {
      const dx = this.px(p.x) - px, dy = this.py(p.y) - py;
      const d = dx * dx + dy * dy;
      if (d <= dmin) { dmin = d; mejor = p; }
    }
    return mejor;
  };

  /** Hace arrastrables una lista de puntos {x,y}. Se modifican en el lugar.
   *  Opciones: {radio, fijarX, fijarY, acotarX:[a,b], acotarY:[a,b], alArrastrar, alSoltar}
   *  @example p.arrastrables(nube, { alArrastrar: () => recalcularRectas() }); */
  Plano.prototype.arrastrables = function (puntos, op) {
    this._arrastrables = Object.assign({ puntos: puntos, radio: 14 }, op || {});
    return this;
  };

  /** Tooltip al pasar el mouse. La función recibe {x,y} del mundo y devuelve
   *  el texto (o null para no mostrar nada).
   *  @example p.tooltip(w => `año ${Math.round(w.x)}`); */
  Plano.prototype.tooltip = function (fn) { this._tooltip = fn; return this; };

  /** Clic sobre el canvas, en coordenadas del mundo.
   *  @example p.alClic(w => { a = w.x; b = w.y; }); */
  Plano.prototype.alClic = function (fn) { this._clic = fn; return this; };

  /** Movimiento del mouse (sin tooltip).  @example p.alMover(w => cursor = w); */
  Plano.prototype.alMover = function (fn) { this._mover = fn; return this; };

  /** Registra la función de dibujo. Se llama en cada redibujo.
   *  @example p.alDibujar(() => { p.fondo(); p.grilla(); p.ejes(); }); */
  Plano.prototype.alDibujar = function (fn) { this._dibujo = fn; return this; };

  /** Redibuja (agrupado en un requestAnimationFrame).  @example p.redibujar(); */
  Plano.prototype.redibujar = function () {
    if (!this._dibujo || this._pendiente) return this;
    this._pendiente = true;
    const self = this;
    requestAnimationFrame(function () {
      self._pendiente = false;
      self._dibujo(self);
    });
    return this;
  };

  /** Redibuja YA, sin esperar el frame (para exportar o medir).
   *  @example p.redibujarYa(); */
  Plano.prototype.redibujarYa = function () { if (this._dibujo) this._dibujo(this); return this; };

  /** Crea un plano. Ver la doc de Plano.
   *  @example const p = Viz.plano('#lienzo', { xmin:0, xmax:1, ymin:0, ymax:1 }); */
  function plano(cont, op) { return new Plano(cont, op); }

  /* =========================================================================
     4. PANEL DE CONTROLES
     ========================================================================= */

  /**
   * Genera un panel de controles ligados a parámetros. Devuelve un objeto con
   * `.valores` (el estado vivo), `.set(id, v)`, `.get(id)` y `.on(fn)`.
   * Cada cambio dispara `alCambio(valores, id)`.
   *
   * Tipos: 'slider' (con escala 'lineal'|'log'), 'checkbox', 'select',
   *        'boton', 'botones', 'titulo', 'texto', 'medidor'.
   *
   * @example
   *   const ctl = Viz.controles('#panel', [
   *     { tipo:'titulo', texto:'Las perillas' },
   *     { tipo:'slider', id:'a', etiqueta:'pendiente', sub:'cuánto sube por año',
   *       min:-2, max:2, paso:.01, valor:.3 },
   *     { tipo:'checkbox', id:'errores', etiqueta:'mostrar errores', valor:true },
   *     { tipo:'boton', texto:'Reiniciar', principal:true, alClic: () => reset() }
   *   ], v => { a = v.a; p.redibujar(); });
   */
  function controles(contenedor, defs, alCambio) {
    const cont = nodo(contenedor);
    if (!cont) throw new Error('Viz.controles: no encontré ' + contenedor);
    const valores = {};
    const oyentes = [];
    const nodos = {};
    if (alCambio) oyentes.push(alCambio);

    function avisar(id) { for (const f of oyentes) f(valores, id); }

    function logAValor(t, d) { return d.min * Math.pow(d.max / d.min, t); }
    function valorALog(v, d) { return Math.log(v / d.min) / Math.log(d.max / d.min); }

    for (const d of defs) {
      if (d.tipo === 'titulo') {
        el('h2', { texto: d.texto }, cont);
        continue;
      }
      if (d.tipo === 'texto') {
        const n = el('div', { class: 'lectura', html: d.html || d.texto || '' }, cont);
        if (d.id) nodos[d.id] = n;
        continue;
      }
      if (d.tipo === 'medidor') {
        const w = el('div', { class: 'ctrl' }, cont);
        const fila = el('div', { class: 'ctrl-fila' }, w);
        el('span', { class: 'ctrl-etiqueta', texto: d.etiqueta || '' }, fila);
        const val = el('span', { class: 'ctrl-valor', texto: '—' }, fila);
        const barra = el('div', { class: 'barra-medidor' }, w);
        const relleno = el('i', { estilo: { width: '0%' } }, barra);
        nodos[d.id] = { valor: val, relleno: relleno, def: d };
        continue;
      }
      if (d.tipo === 'boton') {
        let grupo = cont.lastElementChild;
        if (!grupo || !grupo.classList.contains('grupo-botones')) {
          grupo = el('div', { class: 'grupo-botones ctrl' }, cont);
        }
        const b = el('button', { texto: d.texto, class: d.principal ? 'principal' : '' }, grupo);
        b.addEventListener('click', function () { if (d.alClic) d.alClic(valores); avisar(d.id || null); });
        if (d.id) nodos[d.id] = b;
        continue;
      }
      if (d.tipo === 'botones') {
        // Dos usos. (a) Sin `valor`: fila de botones de accion, cada uno con su
        // alClic. (b) Con `valor`: selector segmentado, guarda el elegido en
        // valores[id] y marca el activo con la clase `activo`.
        const esSelector = d.valor !== undefined;
        const w = el('div', { class: 'ctrl' }, cont);
        if (d.etiqueta) {
          const fila = el('div', { class: 'ctrl-fila' }, w);
          el('span', { class: 'ctrl-etiqueta', texto: d.etiqueta }, fila);
        }
        const grupo = el('div', { class: 'grupo-botones' }, w);
        const botones = [];
        if (esSelector) valores[d.id] = d.valor;
        function pintar() {
          for (const par of botones) {
            par.bt.classList.toggle('activo', par.v === valores[d.id]);
          }
        }
        for (const b of d.opciones) {
          const v = b.valor !== undefined ? b.valor : b;
          const bt = el('button', {
            texto: b.texto !== undefined ? b.texto : String(v),
            class: b.principal ? 'principal' : ''
          }, grupo);
          botones.push({ bt: bt, v: v });
          bt.addEventListener('click', function () {
            if (esSelector) { valores[d.id] = v; pintar(); }
            if (b.alClic) b.alClic(valores);
            avisar(d.id || null);
          });
        }
        if (esSelector) { pintar(); nodos[d.id] = { grupo: grupo, botones: botones, def: d, pintar: pintar }; }
        else if (d.id) nodos[d.id] = { grupo: grupo, botones: botones, def: d };
        continue;
      }
      if (d.tipo === 'checkbox') {
        valores[d.id] = !!d.valor;
        const w = el('div', { class: 'ctrl tipo-checkbox' }, cont);
        const lab = el('label', {}, w);
        const inp = el('input', { type: 'checkbox' }, lab);
        inp.checked = !!d.valor;
        el('span', { texto: d.etiqueta }, lab);
        inp.addEventListener('change', function () { valores[d.id] = inp.checked; avisar(d.id); });
        nodos[d.id] = inp;
        continue;
      }
      if (d.tipo === 'select') {
        valores[d.id] = d.valor !== undefined ? d.valor : (d.opciones[0].valor !== undefined ? d.opciones[0].valor : d.opciones[0]);
        const w = el('div', { class: 'ctrl' }, cont);
        el('div', { class: 'ctrl-etiqueta', texto: d.etiqueta || '' }, w);
        const s = el('select', {}, w);
        for (const o of d.opciones) {
          const v = o.valor !== undefined ? o.valor : o;
          const t = o.texto !== undefined ? o.texto : o;
          const op = el('option', { value: v, texto: t }, s);
          if (v == valores[d.id]) op.selected = true;
        }
        s.addEventListener('change', function () { valores[d.id] = s.value; avisar(d.id); });
        nodos[d.id] = s;
        continue;
      }
      // slider por defecto
      const log = d.escala === 'log';
      valores[d.id] = d.valor !== undefined ? d.valor : (log ? d.min : (d.min + d.max) / 2);
      const w = el('div', { class: 'ctrl tipo-slider' }, cont);
      const fila = el('div', { class: 'ctrl-fila' }, w);
      const lab = el('span', { class: 'ctrl-etiqueta' }, fila);
      lab.appendChild(document.createTextNode(d.etiqueta || d.id));
      if (d.sub) el('span', { class: 'sub', texto: d.sub }, lab);
      const val = el('span', { class: 'ctrl-valor' }, fila);
      const inp = el('input', { type: 'range' }, w);
      if (d.color) { inp.style.setProperty('accent-color', color(d.color)); }
      if (log) { inp.min = 0; inp.max = 1000; inp.step = 1; inp.value = Math.round(valorALog(valores[d.id], d) * 1000); }
      else { inp.min = d.min; inp.max = d.max; inp.step = d.paso || (d.max - d.min) / 100; inp.value = valores[d.id]; }
      const fmt = d.formato || function (v) { return num(v, d.decimales); };
      val.textContent = fmt(valores[d.id]);
      inp.addEventListener('input', function () {
        valores[d.id] = log ? logAValor(+inp.value / 1000, d) : +inp.value;
        val.textContent = fmt(valores[d.id]);
        avisar(d.id);
      });
      nodos[d.id] = { input: inp, valor: val, def: d, fmt: fmt };
    }

    const api = {
      valores: valores,
      elemento: cont,
      nodos: nodos,
      /** Cambia un valor por código y refresca el control.
       *  @example ctl.set('a', 1.2); */
      set: function (id, v, silencioso) {
        const n = nodos[id];
        if (n === undefined) return api;
        valores[id] = v;
        if (n.input) {
          const d = n.def;
          n.input.value = d.escala === 'log' ? Math.round(Math.log(v / d.min) / Math.log(d.max / d.min) * 1000) : v;
          n.valor.textContent = n.fmt(v);
        } else if (n.pintar) { n.pintar(); }
        else if (n.tagName === 'INPUT' && n.type === 'checkbox') { n.checked = !!v; }
        else if (n.tagName === 'SELECT') { n.value = v; }
        if (!silencioso) avisar(id);
        return api;
      },
      /** Lee un valor.  @example ctl.get('a') */
      get: function (id) { return valores[id]; },
      /** Agrega un oyente de cambios.  @example ctl.on(v => p.redibujar()); */
      on: function (fn) { oyentes.push(fn); return api; },
      /** Actualiza una caja de texto del panel.  @example ctl.texto('lectura', '<b>loss</b> 0.42'); */
      texto: function (id, html) { if (nodos[id]) nodos[id].innerHTML = html; return api; },
      /** Actualiza un medidor 0..1.  @example ctl.medidor('desajuste', .7, '18.4'); */
      medidor: function (id, t, etiqueta) {
        const n = nodos[id];
        if (!n) return api;
        n.relleno.style.width = (acotar(t, 0, 1) * 100) + '%';
        n.valor.textContent = etiqueta !== undefined ? etiqueta : num(t);
        return api;
      },
      /** Dispara los oyentes a mano (útil para el primer dibujo).
       *  @example ctl.disparar(); */
      disparar: function () { avisar(null); return api; }
    };
    return api;
  }

  /* =========================================================================
     5. ANIMACIÓN
     ========================================================================= */

  /**
   * Loop de animación con play / pausa / reset / paso a paso.
   * `paso(i)` se llama una vez por cuadro (o cada `cadaMs`); si devuelve false,
   * la animación se detiene sola (por ejemplo, cuando convergió).
   *
   * @example
   *   const anim = Viz.animacion({
   *     paso: i => { descensoUnPaso(); p.redibujar(); return i < 200; },
   *     reset: () => { a = 0; b = 0; p.redibujar(); },
   *     cadaMs: 40
   *   });
   *   Viz.controlesAnimacion('#panel', anim);
   */
  function animacion(op) {
    op = op || {};
    let corriendo = false, i = 0, ultimo = 0, raf = null;
    const cada = op.cadaMs || 0;
    const oyentes = [];

    function avisar() { for (const f of oyentes) f(api); }

    function cuadro(t) {
      if (!corriendo) return;
      if (!cada || t - ultimo >= cada) {
        ultimo = t;
        const seguir = op.paso ? op.paso(i, api) : true;
        i++;
        if (seguir === false || (op.hasta && i >= op.hasta)) { pausa(); return; }
      }
      raf = requestAnimationFrame(cuadro);
    }
    function play() {
      if (corriendo) return api;
      corriendo = true; ultimo = 0;
      raf = requestAnimationFrame(cuadro);
      avisar(); return api;
    }
    function pausa() {
      corriendo = false;
      if (raf) cancelAnimationFrame(raf);
      raf = null; avisar(); return api;
    }
    const api = {
      /** Arranca.  @example anim.play(); */
      play: play,
      /** Frena.  @example anim.pausa(); */
      pausa: pausa,
      /** Alterna play/pausa.  @example anim.alternar(); */
      alternar: function () { return corriendo ? pausa() : play(); },
      /** Un solo paso, sin arrancar el loop.  @example anim.unPaso(); */
      unPaso: function () { if (op.paso) op.paso(i, api); i++; avisar(); return api; },
      /** Vuelve al estado inicial.  @example anim.reset(); */
      reset: function () { pausa(); i = 0; if (op.reset) op.reset(api); avisar(); return api; },
      /** ¿está corriendo?  @example anim.corriendo() */
      corriendo: function () { return corriendo; },
      /** Número de paso actual.  @example anim.iteracion() */
      iteracion: function () { return i; },
      /** Oyente de cambios de estado (para refrescar botones).
       *  @example anim.on(a => boton.textContent = a.corriendo() ? 'Pausa' : 'Play'); */
      on: function (f) { oyentes.push(f); return api; }
    };
    return api;
  }

  /** Botonera estándar para una animación: play/pausa, un paso, reset.
   *  @example Viz.controlesAnimacion('#panel', anim, { textoPlay:'Soltar la pelota' }); */
  function controlesAnimacion(contenedor, anim, op) {
    op = op || {};
    const cont = nodo(contenedor);
    const grupo = el('div', { class: 'grupo-botones ctrl' }, cont);
    const bPlay = el('button', { class: 'principal', texto: op.textoPlay || 'Play' }, grupo);
    const bPaso = el('button', { texto: op.textoPaso || 'Un paso' }, grupo);
    const bReset = el('button', { texto: op.textoReset || 'Reiniciar' }, grupo);
    bPlay.addEventListener('click', function () { anim.alternar(); });
    bPaso.addEventListener('click', function () { anim.pausa(); anim.unPaso(); });
    bReset.addEventListener('click', function () { anim.reset(); });
    anim.on(function (a) {
      bPlay.textContent = a.corriendo() ? (op.textoPausa || 'Pausa') : (op.textoPlay || 'Play');
    });
    return { grupo: grupo, play: bPlay, paso: bPaso, reset: bReset };
  }

  /* =========================================================================
     6. SVG — para arcos de atención, diagramas de red, flechas curvas
     ========================================================================= */

  const NS = 'http://www.w3.org/2000/svg';

  const svg = {
    /** Crea un <svg> dentro del contenedor.
     *  @example const s = Viz.svg.crear('#caja', { ancho:600, alto:200 }); */
    crear: function (contenedor, op) {
      op = op || {};
      const cont = nodo(contenedor);
      const s = document.createElementNS(NS, 'svg');
      const w = op.ancho || cont.clientWidth || 600, h = op.alto || 200;
      s.setAttribute('viewBox', '0 0 ' + w + ' ' + h);
      s.setAttribute('width', '100%');
      s.style.display = 'block';
      s.style.height = op.altoCss || (h + 'px');
      s.dataset.ancho = w; s.dataset.alto = h;
      cont.appendChild(s);
      return s;
    },
    /** Crea un elemento SVG con atributos.
     *  @example Viz.svg.el('circle', { cx:10, cy:10, r:4, fill: Viz.color('datos') }, s); */
    el: function (tag, attrs, padre) {
      const n = document.createElementNS(NS, tag);
      if (attrs) for (const k in attrs) {
        if (k === 'texto') n.textContent = attrs[k];
        else n.setAttribute(k, attrs[k]);
      }
      if (padre) padre.appendChild(n);
      return n;
    },
    /** Arco curvo entre dos puntos (los arcos de attention).
     *  @example Viz.svg.arco(s, 100, 40, 300, 40, { curva:.6, grosor:5, color:'acento' }); */
    arco: function (padre, x1, y1, x2, y2, op) {
      op = op || {};
      const k = op.curva !== undefined ? op.curva : .5;
      const mx = (x1 + x2) / 2, dy = Math.abs(x2 - x1) * k * (op.abajo ? 1 : -1);
      const d = 'M ' + x1 + ' ' + y1 + ' Q ' + mx + ' ' + (y1 + dy) + ' ' + x2 + ' ' + y2;
      return svg.el('path', {
        d: d, fill: 'none',
        stroke: color(op.color || 'acento'),
        'stroke-width': op.grosor || 2,
        'stroke-opacity': op.opacidad !== undefined ? op.opacidad : .8,
        'stroke-linecap': 'round'
      }, padre);
    },
    /** Limpia el contenido de un <svg>.  @example Viz.svg.limpiar(s); */
    limpiar: function (s) { while (s.firstChild) s.removeChild(s.firstChild); return s; }
  };

  /* =========================================================================
     7. MATRIZ DOM (heatmap con etiquetas — la matriz de atención de la clase 7)
     ========================================================================= */

  /**
   * Dibuja una matriz como tabla de celdas coloreadas, con etiquetas en los dos
   * ejes y hover que resalta fila y columna.
   * @example
   *   Viz.matrizCalor('#mapa', A, { etiquetas: palabras, paleta:'acento',
   *     alHover: (f,c,v) => leer(`"${palabras[f]}" le presta ${(v*100)|0}% a "${palabras[c]}"`) });
   */
  function matrizCalor(contenedor, M, op) {
    op = op || {};
    const cont = nodo(contenedor);
    cont.innerHTML = '';
    const filas = M.length, cols = M[0].length;
    const etF = op.etiquetasF || op.etiquetas || rango(filas);
    const etC = op.etiquetasC || op.etiquetas || rango(cols);
    let mn = Infinity, mx = -Infinity;
    for (const f of M) for (const v of f) { if (v < mn) mn = v; if (v > mx) mx = v; }
    if (op.min !== undefined) mn = op.min;
    if (op.max !== undefined) mx = op.max;
    const pal = typeof op.paleta === 'function' ? op.paleta : paleta(op.paleta || 'acento');
    const tabla = el('table', { class: 'viz-matriz' }, cont);
    tabla.style.borderCollapse = 'collapse';
    tabla.style.fontSize = '11px';
    tabla.style.fontFamily = colores().fuente;
    const thead = el('thead', {}, tabla);
    const tr0 = el('tr', {}, thead);
    el('th', {}, tr0);
    etC.forEach(function (t) {
      const th = el('th', { texto: t }, tr0);
      Object.assign(th.style, {
        writingMode: 'vertical-rl', transform: 'rotate(180deg)',
        padding: '3px 1px', color: color('tinta2'), fontWeight: '500',
        whiteSpace: 'nowrap', border: 'none'
      });
    });
    const tbody = el('tbody', {}, tabla);
    for (let j = 0; j < filas; j++) {
      const tr = el('tr', {}, tbody);
      const th = el('th', { texto: etF[j] }, tr);
      Object.assign(th.style, {
        textAlign: 'right', padding: '1px 6px', color: color('tinta2'),
        fontWeight: '500', whiteSpace: 'nowrap', border: 'none'
      });
      for (let i = 0; i < cols; i++) {
        const td = el('td', {}, tr);
        const t = (M[j][i] - mn) / ((mx - mn) || 1);
        Object.assign(td.style, {
          width: (op.celda || 26) + 'px', height: (op.celda || 26) + 'px',
          background: pal(acotar(t, 0, 1)),
          border: '1px solid ' + alfa('borde', .6), cursor: 'crosshair'
        });
        if (op.texto) {
          td.textContent = num(M[j][i], 2);
          td.style.textAlign = 'center';
          td.style.color = t > .6 ? color('papel') : color('tinta');
          td.style.fontFamily = colores().mono;
        }
        td.dataset.f = j; td.dataset.c = i;
        td.addEventListener('mouseenter', function () {
          tabla.querySelectorAll('td').forEach(function (o) {
            o.style.outline = (o.dataset.f === td.dataset.f || o.dataset.c === td.dataset.c)
              ? '2px solid ' + color('acento') : 'none';
            o.style.outlineOffset = '-2px';
          });
          if (op.alHover) op.alHover(j, i, M[j][i]);
        });
      }
    }
    tabla.addEventListener('mouseleave', function () {
      tabla.querySelectorAll('td').forEach(function (o) { o.style.outline = 'none'; });
      if (op.alSalir) op.alSalir();
    });
    return tabla;
  }

  /* =========================================================================
     8. ÁLGEBRA MÍNIMA
     ========================================================================= */

  const M = {
    /** Matriz de ceros f x c.  @example Viz.M.ceros(2,3) */
    ceros: function (f, c) { const A = []; for (let i = 0; i < f; i++) A.push(new Array(c).fill(0)); return A; },
    /** Matriz aleatoria con semilla, escala dada.  @example Viz.M.aleatoria(3,2,.5,7) */
    aleatoria: function (f, c, escala, semilla) {
      const g = gauss(semilla === undefined ? 1 : semilla);
      const A = [];
      for (let i = 0; i < f; i++) { const r = []; for (let j = 0; j < c; j++) r.push(g() * (escala || 1)); A.push(r); }
      return A;
    },
    /** Producto de matrices A(f×k) · B(k×c).  @example Viz.M.matmul(A,B) */
    matmul: function (A, B) {
      const f = A.length, k = B.length, c = B[0].length;
      const R = M.ceros(f, c);
      for (let i = 0; i < f; i++) for (let t = 0; t < k; t++) {
        const a = A[i][t]; if (!a) continue;
        for (let j = 0; j < c; j++) R[i][j] += a * B[t][j];
      }
      return R;
    },
    /** Transpuesta.  @example Viz.M.transponer([[1,2],[3,4]]) */
    transponer: function (A) {
      const R = M.ceros(A[0].length, A.length);
      for (let i = 0; i < A.length; i++) for (let j = 0; j < A[0].length; j++) R[j][i] = A[i][j];
      return R;
    },
    /** Producto punto de dos vectores.  @example Viz.M.dot([1,2],[3,4]) // 11 */
    dot: function (a, b) { let s = 0; for (let i = 0; i < a.length; i++) s += a[i] * b[i]; return s; },
    /** Norma euclídea.  @example Viz.M.norma([3,4]) // 5 */
    norma: function (a) { return Math.sqrt(M.dot(a, a)); },
    /** Similitud coseno (la de la clase 6 y la 9).
     *  @example Viz.M.coseno(emb['protesta'], emb['movilizacion']) */
    coseno: function (a, b) { const d = M.norma(a) * M.norma(b); return d ? M.dot(a, b) / d : 0; },
    /** Softmax estable: convierte puntajes en probabilidades que suman 1.
     *  @example Viz.M.softmax([2,1,0]) // [.665,.245,.090] */
    softmax: function (v, temperatura) {
      const T = temperatura === undefined ? 1 : Math.max(1e-6, temperatura);
      let mx = -Infinity;
      for (const x of v) if (x > mx) mx = x;
      const e = v.map(function (x) { return Math.exp((x - mx) / T); });
      let s = 0; for (const x of e) s += x;
      return e.map(function (x) { return x / s; });
    },
    /** Sigmoide.  @example Viz.M.sigmoid(0) // 0.5 */
    sigmoid: function (x) { return 1 / (1 + Math.exp(-x)); },
    /** Derivada de la sigmoide (dado y = sigmoid(x)). */
    dsigmoid: function (y) { return y * (1 - y); },
    /** Tangente hiperbólica.  @example Viz.M.tanh(1) */
    tanh: function (x) { return Math.tanh(x); },
    /** Derivada de tanh (dado y = tanh(x)). */
    dtanh: function (y) { return 1 - y * y; },
    /** ReLU: el doblez. La no linealidad de la clase 2.
     *  @example Viz.M.relu(-3) // 0 */
    relu: function (x) { return x > 0 ? x : 0; },
    /** Derivada de ReLU. */
    drelu: function (x) { return x > 0 ? 1 : 0; },
    /** Error cuadrático medio entre dos vectores.
     *  @example Viz.M.mse(pred, y) */
    mse: function (a, b) { let s = 0; for (let i = 0; i < a.length; i++) s += (a[i] - b[i]) * (a[i] - b[i]); return s / a.length; },
    /** Error absoluto medio.  @example Viz.M.mae(pred, y) */
    mae: function (a, b) { let s = 0; for (let i = 0; i < a.length; i++) s += Math.abs(a[i] - b[i]); return s / a.length; }
  };

  /* =========================================================================
     9. RED FEED-FORWARD MÍNIMA (forward + backward a mano)
        Para entrenar EN VIVO dentro de una slide. Es la misma cuenta que hace
        PyTorch, escrita a mano para que se pueda mirar.
     ========================================================================= */

  /**
   * Red densa chiquita. capas: [entradas, ocultas..., salidas].
   * Activación 'relu' o 'tanh' en las ocultas; salida lineal.
   *
   * @example
   *   const red = new Viz.Red([1, 8, 1], { activacion:'relu', semilla:3 });
   *   for (let i = 0; i < 500; i++) red.paso(X, Y, 0.05);
   *   red.predecir([[2.5]]);            // [[valor]]
   *   red.rampas();                     // las rampas individuales, para dibujarlas
   */
  function Red(capas, op) {
    op = op || {};
    this.capas = capas.slice();
    this.act = op.activacion || 'tanh';
    this.W = []; this.b = [];
    const g = gauss(op.semilla === undefined ? 7 : op.semilla);
    for (let l = 0; l < capas.length - 1; l++) {
      const nIn = capas[l], nOut = capas[l + 1];
      const esc = (op.escala || 1) * Math.sqrt(2 / nIn);
      const W = [];
      for (let j = 0; j < nOut; j++) {
        const fila = [];
        for (let i = 0; i < nIn; i++) fila.push(g() * esc);
        W.push(fila);
      }
      this.W.push(W);
      this.b.push(new Array(nOut).fill(0).map(function () { return g() * .3; }));
    }
  }

  Red.prototype._f = function (x) { return this.act === 'relu' ? M.relu(x) : Math.tanh(x); };
  Red.prototype._df = function (z, a) { return this.act === 'relu' ? (z > 0 ? 1 : 0) : (1 - a * a); };

  /** Pasada hacia adelante de UN vector. Devuelve {a, z} de todas las capas.
   *  @example red.adelante([2.0]).salida */
  Red.prototype.adelante = function (x) {
    const A = [x.slice()], Z = [null];
    for (let l = 0; l < this.W.length; l++) {
      const W = this.W[l], b = this.b[l], prev = A[l];
      const z = [], a = [];
      for (let j = 0; j < W.length; j++) {
        let s = b[j];
        for (let i = 0; i < prev.length; i++) s += W[j][i] * prev[i];
        z.push(s);
        a.push(l === this.W.length - 1 ? s : this._f(s));   // salida lineal
      }
      Z.push(z); A.push(a);
    }
    return { A: A, Z: Z, salida: A[A.length - 1] };
  };

  /** Predice un lote. X es [[x1],[x2],...]. Devuelve [[y1],[y2],...].
   *  @example red.predecir([[0],[1],[2]]) */
  Red.prototype.predecir = function (X) {
    const self = this;
    return X.map(function (x) { return self.adelante(x).salida.slice(); });
  };

  /** Pérdida MSE sobre un lote.  @example red.perdida(X, Y) */
  Red.prototype.perdida = function (X, Y) {
    let s = 0;
    for (let n = 0; n < X.length; n++) {
      const o = this.adelante(X[n]).salida;
      for (let j = 0; j < o.length; j++) s += (o[j] - Y[n][j]) * (o[j] - Y[n][j]);
    }
    return s / (X.length * Y[0].length);
  };

  /** Un paso de descenso por gradiente sobre todo el lote. Devuelve la loss ANTES
   *  del paso (que es la que querés graficar).
   *  @example const l = red.paso(X, Y, 0.05); */
  Red.prototype.paso = function (X, Y, lr) {
    const L = this.W.length;
    const gW = [], gb = [];
    for (let l = 0; l < L; l++) {
      gW.push(this.W[l].map(function (f) { return f.map(function () { return 0; }); }));
      gb.push(this.b[l].map(function () { return 0; }));
    }
    let perdida = 0;
    const N = X.length;
    for (let n = 0; n < N; n++) {
      const fw = this.adelante(X[n]);
      const A = fw.A, Z = fw.Z;
      let delta = [];
      const out = A[L];
      for (let j = 0; j < out.length; j++) {
        const e = out[j] - Y[n][j];
        perdida += e * e / out.length;
        delta.push(2 * e / out.length);
      }
      for (let l = L - 1; l >= 0; l--) {
        const prev = A[l];
        for (let j = 0; j < this.W[l].length; j++) {
          gb[l][j] += delta[j];
          for (let i = 0; i < prev.length; i++) gW[l][j][i] += delta[j] * prev[i];
        }
        if (l > 0) {
          const nueva = new Array(prev.length).fill(0);
          for (let i = 0; i < prev.length; i++) {
            let s = 0;
            for (let j = 0; j < this.W[l].length; j++) s += this.W[l][j][i] * delta[j];
            nueva[i] = s * this._df(Z[l][i], A[l][i]);
          }
          delta = nueva;
        }
      }
    }
    for (let l = 0; l < L; l++) {
      for (let j = 0; j < this.W[l].length; j++) {
        this.b[l][j] -= lr * gb[l][j] / N;
        for (let i = 0; i < this.W[l][j].length; i++) this.W[l][j][i] -= lr * gW[l][j][i] / N;
      }
    }
    return perdida / N;
  };

  /** Para una red [1, H, 1]: devuelve las H rampas individuales como funciones,
   *  para dibujar "la suma de rampas" de la clase 2.
   *  @example red.rampas().forEach((r,i) => p.curva(r, { color: paleta(i) })); */
  Red.prototype.rampas = function () {
    if (this.capas.length !== 3 || this.capas[0] !== 1 || this.capas[2] !== 1) return [];
    const self = this, H = this.capas[1], out = [];
    for (let j = 0; j < H; j++) {
      out.push((function (j) {
        return function (x) {
          const z = self.W[0][j][0] * x + self.b[0][j];
          return self.W[1][0][j] * self._f(z);
        };
      })(j));
    }
    return out;
  };

  /** Vuelve a inicializar los pesos con otra semilla.
   *  @example red.reiniciar(99); */
  Red.prototype.reiniciar = function (semilla) {
    const nueva = new Red(this.capas, { activacion: this.act, semilla: semilla });
    this.W = nueva.W; this.b = nueva.b;
    return this;
  };

  /* =========================================================================
     10. HERRAMIENTAS DE PÁGINA
     ========================================================================= */

  /** Marca el <body> con la clase `embebido` si la página está adentro de un
   *  iframe (es decir, metida en una slide). curso.css esconde el título, el pie
   *  y el botón de tema: el mismo archivo sirve standalone y embebido.
   *  Se llama sola al cargar viz.js.
   *  @example Viz.detectarEmbebido(); */
  function detectarEmbebido() {
    let dentro = false;
    try { dentro = global.self !== global.top; } catch (e) { dentro = true; }
    if (dentro && document.body) document.body.classList.add('embebido');
    return dentro;
  }

  /** Botón flotante para alternar tema claro / oscuro. Recuerda la elección
   *  en localStorage (envuelto en try/catch: file:// a veces no deja).
   *  @example Viz.botonTema(); */
  function botonTema() {
    let guardado = null;
    try { guardado = localStorage.getItem('dlss-tema'); } catch (e) { }
    if (guardado) document.documentElement.setAttribute('data-tema', guardado);
    const b = el('button', { class: 'toggle-tema', texto: 'Tema' }, document.body);
    b.addEventListener('click', function () {
      const actual = document.documentElement.getAttribute('data-tema');
      const oscuroSistema = global.matchMedia && global.matchMedia('(prefers-color-scheme: dark)').matches;
      const proximo = actual ? (actual === 'oscuro' ? 'claro' : 'oscuro')
                             : (oscuroSistema ? 'claro' : 'oscuro');
      document.documentElement.setAttribute('data-tema', proximo);
      try { localStorage.setItem('dlss-tema', proximo); } catch (e) { }
      recargarColores();
      global.dispatchEvent(new Event('viz:tema'));
    });
    return b;
  }

  /** Redibuja todos los planos registrados cuando cambia el tema.
   *  Se engancha solo: cada Plano se registra al crearse. */
  const _planos = [];
  if (global.addEventListener) global.addEventListener('viz:tema', function () {
    recargarColores();
    for (const p of _planos) p.redibujar();
  });
  if (global.matchMedia) {
    try {
      global.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        recargarColores();
        for (const p of _planos) p.redibujar();
      });
    } catch (e) { }
  }
  const _crear = plano;
  function planoRegistrado(cont, op) {
    const p = _crear(cont, op);
    _planos.push(p);
    return p;
  }

  /* =========================================================================
     EXPORT
     ========================================================================= */
  const Viz = {
    // utilidades
    nodo: nodo, el: el, acotar: acotar, mezclar: mezclar, rango: rango,
    linspace: linspace, azar: azar, gauss: gauss, num: num,
    // colores
    colores: colores, recargarColores: recargarColores, color: color,
    alfa: alfa, mezclarColor: mezclarColor, paleta: paleta,
    // plano
    plano: planoRegistrado, Plano: Plano,
    // interacción de página
    controles: controles, animacion: animacion, controlesAnimacion: controlesAnimacion,
    mostrarTooltip: mostrarTooltip, ocultarTooltip: ocultarTooltip,
    matrizCalor: matrizCalor, svg: svg, botonTema: botonTema,
    detectarEmbebido: detectarEmbebido,
    // matemática
    M: M, Red: Red,
    version: '1.0'
  };

  global.Viz = Viz;

  // el modo embebido se detecta solo, apenas hay <body>
  if (typeof document !== 'undefined') {
    if (document.body) detectarEmbebido();
    else document.addEventListener('DOMContentLoaded', detectarEmbebido);
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = Viz;

})(typeof window !== 'undefined' ? window : this);
