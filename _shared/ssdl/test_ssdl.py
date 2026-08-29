"""
test_ssdl.py — los tests del paquete.

Se corren así, parado en cualquier lado:

    python3 _shared/ssdl/test_ssdl.py

Y para generar además las figuras de muestra (una por cada función de
graficos.py, para mirarlas con los ojos y confirmar que no salieron feas):

    python3 _shared/ssdl/test_ssdl.py --figuras /tmp/ssdl-check

Esto no es burocracia. Cuarenta visualizaciones y diez notebooks van a
apoyarse en este paquete: si `serie_menciones` devuelve la columna equivocada,
se rompe en silencio en cinco clases a la vez.
"""

from __future__ import annotations

import os
import pathlib
import sys
import unittest

import numpy as np

# Para poder correr este archivo directamente, sin instalar nada.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import matplotlib
matplotlib.use("Agg")  # sin ventanas: sólo archivos
import matplotlib.pyplot as plt

from ssdl import datos, entrenamiento as ent, graficos as g, utils

try:
    import torch
    HAY_TORCH = True
except ImportError:
    HAY_TORCH = False


# ===========================================================================
# utils
# ===========================================================================

class TestUtils(unittest.TestCase):

    def test_encuentra_la_raiz_del_repo(self):
        raiz = utils.raiz_del_repo()
        self.assertTrue((raiz / "_shared" / "ssdl").is_dir())
        self.assertTrue((raiz / "datos" / "muestras").is_dir())

    def test_la_semilla_hace_reproducible(self):
        utils.fijar_semilla(1983)
        a = np.random.rand(5)
        utils.fijar_semilla(1983)
        b = np.random.rand(5)
        np.testing.assert_array_equal(a, b)

    def test_semillas_distintas_dan_cosas_distintas(self):
        utils.fijar_semilla(1)
        a = np.random.rand(5)
        utils.fijar_semilla(2)
        b = np.random.rand(5)
        self.assertFalse(np.allclose(a, b))

    @unittest.skipUnless(HAY_TORCH, "sin torch")
    def test_la_semilla_alcanza_a_torch(self):
        utils.fijar_semilla(7)
        a = torch.randn(4)
        utils.fijar_semilla(7)
        np.testing.assert_allclose(a.numpy(), torch.randn(4).numpy())

    @unittest.skipUnless(HAY_TORCH, "sin torch")
    def test_contar_parametros(self):
        # una capa 3->2 tiene 3*2 pesos + 2 sesgos = 8 perillas
        modelo = torch.nn.Linear(3, 2)
        self.assertEqual(utils.contar_parametros(modelo), 8)

    @unittest.skipUnless(HAY_TORCH, "sin torch")
    def test_contar_parametros_respeta_lo_congelado(self):
        modelo = torch.nn.Sequential(torch.nn.Linear(3, 2), torch.nn.Linear(2, 1))
        for p in modelo[0].parameters():
            p.requires_grad = False
        self.assertEqual(utils.contar_parametros(modelo, solo_entrenables=True), 3)
        self.assertEqual(utils.contar_parametros(modelo, solo_entrenables=False), 11)

    def test_formatear_cantidad(self):
        self.assertEqual(utils.formatear_cantidad(3_141_592), "3,1 M")
        self.assertEqual(utils.formatear_cantidad(950), "950")
        self.assertEqual(utils.formatear_cantidad(2_500), "2,5 mil")

    def test_formatear_duracion(self):
        self.assertEqual(utils.formatear_duracion(0.042), "42 ms")
        self.assertEqual(utils.formatear_duracion(125.4), "2 min 5 s")

    def test_medir_tiempo(self):
        with utils.medir_tiempo("test", verboso=False) as crono:
            sum(range(10_000))
        self.assertGreater(crono.segundos, 0)

    def test_estamos_en_colab_devuelve_bool(self):
        self.assertIsInstance(utils.estamos_en_colab(), bool)

    def test_elegir_device_no_explota(self):
        if HAY_TORCH:
            self.assertIn(utils.elegir_device().type, ("cpu", "cuda", "mps"))
            self.assertEqual(utils.elegir_device(preferir_gpu=False).type, "cpu")


# ===========================================================================
# datos — carga
# ===========================================================================

class TestCargaDeDatos(unittest.TestCase):

    def test_serie_menciones_forma_y_rango(self):
        anios, valores = datos.serie_menciones("seguridad")
        self.assertEqual(len(anios), len(valores))
        self.assertGreaterEqual(len(anios), 30)
        self.assertEqual(int(anios[0]), 1984)
        self.assertEqual(int(anios[-1]), 2019)
        # son porcentajes de palabras del discurso: chicos pero no negativos
        self.assertTrue((valores >= 0).all())
        self.assertLess(valores.max(), 100)

    def test_serie_menciones_recorte(self):
        anios, _ = datos.serie_menciones("inflacion", desde=2000, hasta=2010)
        self.assertTrue((anios >= 2000).all() and (anios <= 2010).all())

    def test_serie_menciones_suavizada_es_mas_suave(self):
        _, cruda = datos.serie_menciones("seguridad")
        _, suave = datos.serie_menciones("seguridad", suavizada=True)
        # la variación de un año al siguiente tiene que ser menor
        self.assertLess(np.abs(np.diff(suave)).mean(), np.abs(np.diff(cruda)).mean())

    def test_serie_menciones_en_fraccion(self):
        _, pct = datos.serie_menciones("seguridad")
        _, frac = datos.serie_menciones("seguridad", en_porcentaje=False)
        np.testing.assert_allclose(pct / 100, frac)

    def test_tema_inexistente_avisa_bien(self):
        with self.assertRaises(ValueError) as caso:
            datos.serie_menciones("berenjenas")
        self.assertIn("seguridad", str(caso.exception))  # sugiere los que sí hay

    def test_serie_completa(self):
        d = datos.serie_completa()
        self.assertEqual(len(d["anios"]), len(d["presidente"]))
        for tema in datos.TEMAS_DISPONIBLES:
            self.assertEqual(len(d[tema]), len(d["anios"]))

    def test_debates_aguasclaras(self):
        texto = datos.debates_aguasclaras()
        self.assertGreater(len(texto), 500_000)
        # el encabezado de advertencia se saca por defecto
        self.assertFalse(texto.startswith("#"))
        self.assertIn("presidente", texto.lower())

    def test_debates_aguasclaras_recortado(self):
        self.assertEqual(len(datos.debates_aguasclaras(max_caracteres=1000)), 1000)

    def test_verdad_aguasclaras_declara_que_es_ficticio(self):
        verdad = datos.verdad_aguasclaras()
        self.assertIn("_ADVERTENCIA", verdad)
        self.assertIn("FICTICIOS", verdad["_ADVERTENCIA"].upper())
        self.assertEqual(verdad["semilla"], 1983)
        self.assertGreater(len(verdad["partidos"]), 2)

    def test_prensa_aguasclaras(self):
        filas = datos.prensa_aguasclaras()
        self.assertGreater(len(filas), 1000)
        self.assertIsInstance(filas[0]["anio"], int)
        self.assertIn(filas[0]["menciona_protesta"], (0, 1))

    def test_titulares_prensa(self):
        filas = datos.titulares_prensa(n=50)
        self.assertEqual(len(filas), 50)
        self.assertIn("titular", filas[0])
        self.assertIn(filas[0]["es_falso"], (0, 1))

    def test_titulares_prensa_es_reproducible(self):
        a = [f["id"] for f in datos.titulares_prensa(n=20)]
        b = [f["id"] for f in datos.titulares_prensa(n=20)]
        self.assertEqual(a, b)

    def test_discursos_apertura(self):
        d = datos.discursos_apertura()
        self.assertGreater(len(d), 3)
        for anio, texto in d.items():
            self.assertIsInstance(anio, int)
            self.assertGreater(len(texto), 100)

    def test_corpus_mini_gpt(self):
        self.assertGreater(len(datos.corpus_mini_gpt()), 10_000)

    def test_discursos_casarosada(self):
        d = datos.discursos_casarosada(n=5)
        self.assertEqual(len(d), 5)
        self.assertIn("orador", d[0])

    def test_mensaje_de_archivo_faltante_es_util(self):
        with self.assertRaises(FileNotFoundError) as caso:
            datos._leer_csv(datos.ruta_de_muestras("no-existe.csv"))
        self.assertIn("bootstrap", str(caso.exception))


# ===========================================================================
# datos — tokenizadores
# ===========================================================================

class TestTokenizadores(unittest.TestCase):

    def test_caracteres_ida_y_vuelta(self):
        tok = datos.TokenizadorCaracteres("hola mundo parlamentario")
        texto = "hola mundo"
        self.assertEqual(tok.decodificar(tok.codificar(texto)), texto)

    def test_caracteres_tamano_de_vocabulario(self):
        tok = datos.TokenizadorCaracteres("aabbc")
        self.assertEqual(len(tok), 3)
        self.assertEqual(tok.fichas, ["a", "b", "c"])

    def test_caracteres_ignora_lo_desconocido(self):
        tok = datos.TokenizadorCaracteres("abc")
        self.assertEqual(tok.decodificar(tok.codificar("abcZ")), "abc")

    def test_caracteres_sobre_el_corpus_de_verdad(self):
        corpus = datos.debates_aguasclaras(max_caracteres=200_000)
        tok = datos.TokenizadorCaracteres(corpus)
        self.assertLess(len(tok), 200)     # vocabulario chico: eso es lo bueno
        muestra = corpus[:5000]
        self.assertEqual(tok.decodificar(tok.codificar(muestra)), muestra)

    def test_palabras_ida_y_vuelta(self):
        tok = datos.TokenizadorPalabras("la sesion continua")
        self.assertEqual(tok.decodificar(tok.codificar("la sesion")), "la sesion")

    def test_palabras_desconocida_es_cero(self):
        tok = datos.TokenizadorPalabras("la sesion continua")
        self.assertEqual(tok.codificar("berenjena"), [0])
        self.assertEqual(tok.a_ficha[0], tok.DESCONOCIDA)

    def test_palabras_minimo_de_frecuencia(self):
        texto = "voto voto voto quorum"
        self.assertIn("quorum", datos.TokenizadorPalabras(texto, minimo=1).a_id)
        self.assertNotIn("quorum", datos.TokenizadorPalabras(texto, minimo=2).a_id)

    def test_palabras_cobertura(self):
        tok = datos.TokenizadorPalabras("la sesion continua")
        self.assertAlmostEqual(tok.cobertura("la sesion"), 1.0)
        self.assertAlmostEqual(tok.cobertura("la berenjena"), 0.5)

    def test_palabras_separa_signos(self):
        tok = datos.TokenizadorPalabras("hola, mundo")
        self.assertEqual(tok.partir("hola, mundo"), ["hola", ",", "mundo"])

    def test_vocabulario(self):
        conteo = datos.vocabulario("voto voto quorum")
        self.assertEqual(conteo["voto"], 2)
        self.assertEqual(datos.vocabulario("voto voto quorum", top=1).most_common(1),
                         [("voto", 2)])


# ===========================================================================
# datos — particiones
# ===========================================================================

class TestEmbeddingsPropios(unittest.TestCase):
    """
    Los embeddings PPMI+SVD son el corazón de la clase 6 y el plan B de la
    clase 9 si Hugging Face no está disponible. Tienen que salir del corpus
    real, con numpy solo y sin red.
    """

    @classmethod
    def setUpClass(cls):
        # Un pedazo del corpus real: alcanza para que los vecinos tengan
        # sentido y el test no tarde media hora.
        cls.texto = datos.corpus_mini_gpt(400_000)
        cls.V, cls.pal = datos.embeddings_ppmi_svd(
            cls.texto, dim=50, top=1200, minimo=5)

    def test_forma_y_normalizacion(self):
        self.assertEqual(self.V.shape, (len(self.pal), 50))
        normas = np.linalg.norm(self.V, axis=1)
        self.assertTrue(np.allclose(normas, 1.0, atol=1e-4),
                        "los vectores tienen que venir normalizados: el "
                        "producto punto ES la similitud coseno")

    def test_coocurrencia_es_simetrica_y_no_vacia(self):
        M, pal = datos.matriz_de_coocurrencia(self.texto, top=300, ventana=3)
        self.assertEqual(M.shape, (len(pal), len(pal)))
        self.assertTrue(M.sum() > 0)
        self.assertTrue(np.allclose(M, M.T),
                        "la ventana es simétrica, la matriz también")

    def test_los_vecinos_tienen_sentido(self):
        # No pedimos una palabra puntual (el corpus puede cambiar), pedimos que
        # la vecindad de «educación» sea temática y no ruido.
        vecinas = [p for p, _ in datos.vecinos("educación", self.V, self.pal, k=12)]
        tematicas = {"salud", "cultura", "primaria", "secundaria", "escuelas",
                     "escuela", "docentes", "universidad", "técnica",
                     "enseñanza", "alumnos", "educativa", "educativo"}
        self.assertTrue(tematicas & set(vecinas),
                        f"vecinos de «educación» sin ninguna temática: {vecinas}")

    def test_similitud_ordenada_y_acotada(self):
        pares = datos.vecinos("ley", self.V, self.pal, k=5)
        sims = [s for _, s in pares]
        self.assertEqual(sims, sorted(sims, reverse=True))
        self.assertTrue(all(-1.001 <= s <= 1.001 for s in sims))

    def test_palabra_desconocida_avisa_bien(self):
        with self.assertRaises(KeyError):
            datos.vecinos("zzzzinexistente", self.V, self.pal)


class TestParticiones(unittest.TestCase):

    def test_particion_tamanos_y_sin_solape(self):
        tr, va, te = datos.particion(100)
        self.assertEqual((len(tr), len(va), len(te)), (70, 15, 15))
        self.assertEqual(len(set(tr) & set(va)), 0)
        self.assertEqual(len(set(tr) & set(te)), 0)
        self.assertEqual(len(set(tr) | set(va) | set(te)), 100)

    def test_particion_es_reproducible(self):
        np.testing.assert_array_equal(datos.particion(50)[0], datos.particion(50)[0])

    def test_particion_temporal_respeta_el_tiempo(self):
        anios = np.arange(1990, 2020)
        tr, va, te = datos.particion_temporal(anios, corte_val=2010, corte_test=2015)
        self.assertTrue((anios[tr] < 2010).all())
        self.assertTrue(((anios[va] >= 2010) & (anios[va] < 2015)).all())
        self.assertTrue((anios[te] >= 2015).all())

    def test_particion_por_grupo_no_parte_grupos(self):
        grupos = [f"diario_{i % 10}" for i in range(200)]
        tr, va, te = datos.particion_por_grupo(grupos)
        g_tr = {grupos[i] for i in tr}
        g_te = {grupos[i] for i in te}
        self.assertEqual(len(g_tr & g_te), 0)
        self.assertEqual(len(tr) + len(va) + len(te), 200)

    def test_diagnostico_de_fuga_detecta_indices(self):
        informe = datos.diagnostico_de_fuga([1, 2, 3], [3, 4])
        self.assertEqual(informe["indices_repetidos"], [3])

    def test_diagnostico_de_fuga_detecta_grupos(self):
        grupos = ["a", "a", "b", "b"]
        informe = datos.diagnostico_de_fuga([0, 2], [1, 3], grupos=grupos)
        self.assertEqual(sorted(informe["grupos_cruzados"]), ["a", "b"])

    def test_diagnostico_de_fuga_limpio(self):
        informe = datos.diagnostico_de_fuga([0, 1], [2, 3], grupos=["a", "a", "b", "b"])
        self.assertFalse(informe["indices_repetidos"])
        self.assertFalse(informe["grupos_cruzados"])

    def test_diagnostico_de_fuga_detecta_textos_duplicados(self):
        textos = ["hola", "chau", "hola"]
        informe = datos.diagnostico_de_fuga([0, 1], [2], textos=textos)
        self.assertEqual(informe["textos_cruzados"], 1)


# ===========================================================================
# datos — juguetes
# ===========================================================================

class TestDatasetsDeJuguete(unittest.TestCase):

    def test_todos_devuelven_lo_que_prometen(self):
        for nombre, funcion in [("espiral", datos.espiral),
                                ("dos_lunas", datos.dos_lunas),
                                ("circulos", datos.circulos_concentricos),
                                ("xor", datos.xor)]:
            with self.subTest(dataset=nombre):
                X, y = funcion(n=200)
                self.assertEqual(X.shape[1], 2)
                self.assertEqual(len(X), len(y))
                self.assertEqual(set(np.unique(y).tolist()), {0, 1})
                self.assertTrue(np.isfinite(X).all())

    def test_son_reproducibles(self):
        np.testing.assert_array_equal(datos.espiral(100)[0], datos.espiral(100)[0])

    def test_semillas_distintas_dan_nubes_distintas(self):
        self.assertFalse(np.allclose(datos.espiral(100, semilla=1)[0],
                                     datos.espiral(100, semilla=2)[0]))

    def test_espiral_con_tres_clases(self):
        X, y = datos.espiral(n=300, clases=3)
        self.assertEqual(set(np.unique(y).tolist()), {0, 1, 2})

    def test_circulos_el_de_adentro_esta_adentro(self):
        X, y = datos.circulos_concentricos(400, ruido=0.01, factor=0.4)
        radio = np.hypot(X[:, 0], X[:, 1])
        self.assertLess(radio[y == 1].mean(), radio[y == 0].mean())

    def test_xor_las_diagonales_comparten_clase(self):
        X, y = datos.xor(400, ruido=0.05)
        # la clase se corresponde con el signo del producto de las coordenadas
        mismo_signo = (X[:, 0] * X[:, 1]) > 0
        self.assertGreater((mismo_signo == (y == 0)).mean(), 0.95)

    def test_recta_con_ruido_recupera_la_verdad(self):
        x, y = datos.recta_con_ruido(n=400, a=2.0, b=1.0, ruido=0.5)
        pendiente, ordenada = np.polyfit(x, y, 1)
        self.assertAlmostEqual(pendiente, 2.0, delta=0.15)
        self.assertAlmostEqual(ordenada, 1.0, delta=0.4)

    def test_curva_de_dos_picos_tiene_dos_picos(self):
        x, y, verdad = datos.curva_de_dos_picos(n=200, ruido=0.0)
        v = verdad(x)
        # contamos los máximos locales de la verdad, sin ruido
        picos = np.sum((v[1:-1] > v[:-2]) & (v[1:-1] > v[2:]))
        self.assertEqual(picos, 2)

    @unittest.skipUnless(HAY_TORCH, "sin torch")
    def test_a_tensores(self):
        X, y = datos.espiral(50)
        X_t, y_t = datos.a_tensores(X, y)
        self.assertEqual(X_t.dtype, torch.float32)
        self.assertEqual(y_t.dtype, torch.long)   # las etiquetas quedan enteras
        self.assertEqual(tuple(X_t.shape), (50, 2))


# ===========================================================================
# entrenamiento
# ===========================================================================

@unittest.skipUnless(HAY_TORCH, "sin torch")
class TestEntrenamiento(unittest.TestCase):

    def setUp(self):
        utils.fijar_semilla(1983)
        x, y = datos.recta_con_ruido(n=60, a=2.0, b=1.0, ruido=0.6)
        self.x = torch.tensor(x, dtype=torch.float32).reshape(-1, 1)
        self.y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)

    def modelo_lineal(self):
        return torch.nn.Linear(1, 1)

    def test_la_loss_baja(self):
        modelo = self.modelo_lineal()
        h = ent.entrenar(modelo, self.x, self.y, lr=0.01, epocas=200, verboso=0)
        self.assertLess(h.train[-1], h.train[0])
        self.assertEqual(len(h), 200)

    def test_encuentra_la_verdad(self):
        # el test que importa: ¿recupera la pendiente y la ordenada de verdad?
        modelo = self.modelo_lineal()
        ent.entrenar(modelo, self.x, self.y, optimizador=None, lr=0.02,
                     epocas=1500, verboso=0)
        self.assertAlmostEqual(float(modelo.weight.item()), 2.0, delta=0.2)
        self.assertAlmostEqual(float(modelo.bias.item()), 1.0, delta=0.6)

    def test_historial_registra_validacion(self):
        modelo = self.modelo_lineal()
        h = ent.entrenar(modelo, self.x[:40], self.y[:40],
                         x_val=self.x[40:], y_val=self.y[40:],
                         lr=0.01, epocas=50, verboso=0)
        self.assertEqual(len(h.val), 50)
        epoca, valor = h.mejor()
        self.assertTrue(1 <= epoca <= 50)
        self.assertAlmostEqual(valor, min(h.val))

    def test_como_dict_es_serializable(self):
        import json
        modelo = self.modelo_lineal()
        h = ent.entrenar(modelo, self.x, self.y, epocas=5, verboso=0)
        json.dumps(h.como_dict())   # si no es serializable, esto explota

    def test_parada_temprana_frena_y_restaura(self):
        modelo = self.modelo_lineal()
        # loss de validación constante -> nunca mejora -> tiene que frenar
        h = ent.entrenar(modelo, self.x[:40], self.y[:40],
                         x_val=self.x[40:], y_val=self.y[40:],
                         lr=0.0, epocas=200, paciencia=5, verboso=0)
        self.assertTrue(h.detenido_temprano)
        self.assertLess(len(h), 200)

    def test_parada_temprana_sin_validacion_avisa_y_sigue(self):
        modelo = self.modelo_lineal()
        h = ent.entrenar(modelo, self.x, self.y, epocas=10, paciencia=3, verboso=0)
        self.assertEqual(len(h), 10)

    def test_lotes_cubren_todos_los_datos(self):
        vistos = []
        for xb, _ in ent._lotes(self.x, self.y, tam_lote=16, barajar=True):
            vistos.append(len(xb))
        self.assertEqual(sum(vistos), 60)

    def test_un_solo_lote_cuando_tam_lote_es_none(self):
        lotes = list(ent._lotes(self.x, self.y, tam_lote=None, barajar=False))
        self.assertEqual(len(lotes), 1)

    def test_entrena_por_lotes(self):
        modelo = self.modelo_lineal()
        h = ent.entrenar(modelo, self.x, self.y, tam_lote=16, epocas=100,
                         lr=0.01, semilla=1983, verboso=0)
        self.assertLess(h.train[-1], h.train[0])

    def test_acepta_numpy_sin_quejarse(self):
        x, y = datos.recta_con_ruido(n=40)
        modelo = self.modelo_lineal()
        h = ent.entrenar(modelo, x.reshape(-1, 1), y.reshape(-1, 1),
                         epocas=20, lr=0.005, verboso=0)
        self.assertEqual(len(h), 20)

    def test_modo_explicar_narra_e_imprime_las_cinco_estaciones(self):
        import io
        from contextlib import redirect_stdout
        modelo = self.modelo_lineal()
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            ent.entrenar(modelo, self.x, self.y, epocas=3, lr=0.01,
                         verboso=0, explicar=1)
        salida = buffer.getvalue()
        for estacion in ("1. PREDECIR", "2. COMPARAR", "3. BORRAR",
                         "4. ANOTAR", "5. MOVER"):
            self.assertIn(estacion, salida)
        self.assertIn("zero_grad", salida)
        # narra sólo el primer paso, no los tres
        self.assertEqual(salida.count("1. PREDECIR"), 1)

    def test_entrenar_no_tira_warnings(self):
        """Un UserWarning en cada notebook parece un bug y distrae. Cero ruido."""
        import warnings
        modelo = self.modelo_lineal()
        with warnings.catch_warnings(record=True) as capturados:
            warnings.simplefilter("always")
            ent.entrenar(modelo, self.x, self.y, x_val=self.x, y_val=self.y,
                         epocas=5, lr=0.01, verboso=0)
        mensajes = [str(w.message) for w in capturados]
        self.assertEqual(mensajes, [], f"el entrenamiento tiró warnings: {mensajes}")

    def test_evaluar_no_deja_gradientes(self):
        modelo = self.modelo_lineal()
        loss, metrica = ent.evaluar(modelo, self.x, self.y)
        self.assertGreater(loss, 0)
        self.assertIsNone(metrica)
        for p in modelo.parameters():
            self.assertIsNone(p.grad)

    def test_predecir_devuelve_numpy_si_se_lo_pedis(self):
        modelo = self.modelo_lineal()
        salida = ent.predecir(modelo, self.x, como_numpy=True)
        self.assertIsInstance(salida, np.ndarray)
        self.assertEqual(salida.shape, (60, 1))

    def test_exactitud(self):
        logits = torch.tensor([[2.0, 0.0], [0.0, 2.0], [2.0, 0.0]])
        y = torch.tensor([0, 1, 1])
        self.assertAlmostEqual(ent.exactitud(logits, y), 2 / 3, places=5)

    def test_exactitud_binaria_con_una_sola_salida(self):
        salida = torch.tensor([[1.0], [-1.0], [1.0]])
        y = torch.tensor([1, 0, 0])
        self.assertAlmostEqual(ent.exactitud(salida, y), 2 / 3, places=5)

    def test_r_cuadrado_perfecto_es_uno(self):
        y = torch.tensor([1.0, 2.0, 3.0])
        self.assertAlmostEqual(ent.r_cuadrado(y.clone(), y), 1.0, places=6)

    def test_error_absoluto_medio(self):
        p = torch.tensor([1.0, 2.0])
        y = torch.tensor([2.0, 4.0])
        self.assertAlmostEqual(ent.error_absoluto_medio(p, y), 1.5, places=6)

    def test_clasificacion_entera(self):
        X, y = datos.dos_lunas(n=300, ruido=0.15)
        X_t, y_t = datos.a_tensores(X, y)
        modelo = torch.nn.Sequential(torch.nn.Linear(2, 16), torch.nn.ReLU(),
                                     torch.nn.Linear(16, 2))
        h = ent.entrenar(modelo, X_t, y_t, perdida=torch.nn.CrossEntropyLoss(),
                         optimizador=torch.optim.Adam(modelo.parameters(), lr=0.05),
                         epocas=300, metrica=ent.exactitud,
                         x_val=X_t, y_val=y_t, verboso=0)
        self.assertGreater(h.metricas["métrica"][-1], 0.9)

    def test_descenso_a_mano_llega_al_fondo(self):
        # un valle con el mínimo en (3, -1)
        def loss(p):
            return (p[0] - 3.0) ** 2 + (p[1] + 1.0) ** 2

        trayectoria, losses = ent.descenso_a_mano(loss, [0.0, 0.0],
                                                  lr=0.1, pasos=100)
        self.assertEqual(len(trayectoria), 101)
        self.assertLess(losses[-1], losses[0])
        np.testing.assert_allclose(trayectoria[-1], [3.0, -1.0], atol=1e-3)

    def test_descenso_a_mano_con_paso_gigante_diverge(self):
        # la firma del fracaso de la clase 3: paso enorme -> sale despedido
        def loss(p):
            return (p[0] - 3.0) ** 2

        _, losses = ent.descenso_a_mano(loss, [0.0], lr=1.5, pasos=30)
        self.assertGreater(losses[-1], losses[0])

    def test_barra_de_progreso_no_explota(self):
        import io
        salida = io.StringIO()
        barra = ent.BarraDeProgreso(10, etiqueta="test", salida=salida)
        for i in range(1, 11):
            barra.actualizar(i, "loss 0.1", forzar=True)
        barra.cerrar()
        self.assertIn("test", salida.getvalue())
        self.assertIn("10/10", salida.getvalue())


# ===========================================================================
# graficos
# ===========================================================================

class TestGraficos(unittest.TestCase):

    def tearDown(self):
        plt.close("all")

    def test_la_paleta_tiene_todos_los_roles(self):
        p = g.paleta()
        for rol in ("datos", "verdad", "modelo", "parametro", "error", "val",
                    "ok", "acento"):
            self.assertIn(rol, p)
            self.assertTrue(p[rol].startswith("#"))

    def test_los_colores_coinciden_con_curso_css(self):
        """La semántica de color no puede divergir entre las slides y las figuras."""
        css = (utils.raiz_del_repo() / "_shared" / "css" / "curso.css").read_text(
            encoding="utf-8")
        for rol, color in [("datos", g.DATOS), ("modelo", g.MODELO),
                           ("parametro", g.PARAMETRO), ("error", g.ERROR),
                           ("val", g.VAL), ("ok", g.OK), ("acento", g.ACENTO)]:
            with self.subTest(rol=rol):
                self.assertIn(f"--c-{rol}:", css)
                self.assertIn(color, css)

    def test_titulo_y_etiquetas_sobreviven_a_pasar_un_ax(self):
        """El bug clásico: armás una grilla de subplots y los títulos desaparecen."""
        fig, ejes = g.figura(10, 3, filas=1, columnas=2)
        g.plot_serie([1, 2, 3], [1, 2, 3], ax=ejes[0], titulo="izquierda")
        g.scatter_clases(*datos.xor(40), ax=ejes[1], titulo="derecha")
        self.assertEqual(ejes[0].get_title(), "izquierda")
        self.assertEqual(ejes[1].get_title(), "derecha")
        self.assertEqual(ejes[0].get_xlabel(), "año")
        plt.close(fig)

    def test_figura_devuelve_ejes(self):
        fig, ax = g.figura(titulo="t", xlabel="x", ylabel="y")
        self.assertEqual(ax.get_title(), "t")
        self.assertEqual(ax.get_xlabel(), "x")

    def test_plot_funcion_dibuja_algo(self):
        ax = g.plot_funcion(lambda x: x ** 2, x=(-3, 3))
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(len(ax.lines[0].get_xdata()), 400)

    def test_plot_familia_una_curva_por_valor(self):
        ax = g.plot_familia(lambda x, a: a * x ** 2, valores=[0.5, 1, 2],
                            destacar=1)
        self.assertEqual(len(ax.lines), 3)
        # la destacada va en azul (color del modelo) y más gruesa
        gruesas = [l for l in ax.lines if l.get_linewidth() > 3]
        self.assertEqual(len(gruesas), 1)

    def test_plot_serie(self):
        anios, valores = datos.serie_menciones("seguridad")
        ax = g.plot_serie(anios, valores)
        self.assertEqual(len(ax.collections), 1)   # el scatter

    def test_plot_ajuste_dibuja_un_error_por_punto(self):
        x, y = datos.recta_con_ruido(n=12)
        ax = g.plot_ajuste(x, y, modelo=lambda x: 2 * x + 1)
        # 12 segmentos de error + 1 curva del modelo
        self.assertEqual(len(ax.lines), 13)

    def test_plot_ajuste_sin_errores(self):
        x, y = datos.recta_con_ruido(n=12)
        ax = g.plot_ajuste(x, y, modelo=lambda x: 2 * x + 1, mostrar_errores=False)
        self.assertEqual(len(ax.lines), 1)

    def test_plot_ajuste_dibuja_la_verdad_punteada(self):
        """La verdad subyacente va SIEMPRE punteada: es una cortesía del simulador."""
        x, y = datos.recta_con_ruido(n=10)
        ax = g.plot_ajuste(x, y, modelo=lambda t: 2 * t, verdad=lambda t: 2 * t + 1,
                           mostrar_errores=False)
        self.assertEqual(len(ax.lines), 2)                    # verdad + modelo
        verdad, modelo = ax.lines[0], ax.lines[1]
        self.assertNotEqual(verdad.get_linestyle(), "-")      # punteada
        self.assertEqual(verdad.get_color(), g.VERDAD)
        self.assertEqual(modelo.get_linestyle(), "-")         # el modelo, sólido
        self.assertEqual(modelo.get_color(), g.MODELO)

    def test_scatter_clases(self):
        X, y = datos.dos_lunas(120)
        ax = g.scatter_clases(X, y)
        self.assertEqual(len(ax.collections), 2)   # una colección por clase

    def test_frontera_de_decision(self):
        X, y = datos.dos_lunas(120)
        ax = g.frontera_de_decision(lambda XX: (XX[:, 0] > 0.5).astype(float), X, y)
        self.assertGreater(len(ax.collections), 2)

    def test_superficie_de_loss_los_tres_modos(self):
        def loss(a, b):
            return (a - 1) ** 2 + (b + 2) ** 2

        for modo, n_ejes in [("contorno", 1), ("3d", 1), ("ambos", 2)]:
            with self.subTest(modo=modo):
                fig, ejes = g.superficie_de_loss(loss, (-2, 4), (-4, 2), n=25,
                                                 modo=modo)
                self.assertEqual(len(ejes), n_ejes)
                plt.close(fig)

    def test_superficie_de_loss_con_trayectoria(self):
        def loss(a, b):
            return (a - 1) ** 2 + (b + 2) ** 2

        tray, _ = ent.descenso_a_mano(lambda p: loss(p[0], p[1]), [-1.5, 1.5],
                                      lr=0.1, pasos=30)
        fig, ejes = g.superficie_de_loss(loss, (-2, 4), (-4, 2), n=25,
                                         trayectoria=tray, modo="contorno",
                                         optimo=(1, -2))
        self.assertGreater(len(ejes[0].lines), 0)
        plt.close(fig)

    def test_plot_loss_1d(self):
        ax = g.plot_loss_1d(lambda a: (a - 2) ** 2, rango=(-2, 6), punto=0.0)
        self.assertGreaterEqual(len(ax.lines), 2)   # la parábola y la secante

    def test_curvas_de_entrenamiento_desde_historial(self):
        h = ent.Historial()
        for e in range(1, 21):
            h.registrar(e, train=1.0 / e, val=1.0 / e + 0.01 * e)
        ax = g.curvas_de_entrenamiento(h)
        self.assertEqual(len(ax.lines), 3)   # train, val, y la vertical del mejor

    def test_curvas_de_entrenamiento_solo_train(self):
        ax = g.curvas_de_entrenamiento(train=[3, 2, 1])
        self.assertEqual(len(ax.lines), 1)

    def test_metricas_binarias(self):
        y_true = [1, 1, 1, 0, 0, 0, 0, 0]
        y_pred = [1, 1, 0, 1, 0, 0, 0, 0]
        m = g.metricas_binarias(y_true, y_pred)
        self.assertEqual((m["vp"], m["fp"], m["fn"], m["vn"]), (2, 1, 1, 4))
        self.assertAlmostEqual(m["precision"], 2 / 3)
        self.assertAlmostEqual(m["recall"], 2 / 3)
        self.assertAlmostEqual(m["f1"], 2 / 3)
        self.assertAlmostEqual(m["accuracy"], 6 / 8)
        self.assertAlmostEqual(m["prevalencia"], 3 / 8)

    def test_metricas_binarias_no_divide_por_cero(self):
        m = g.metricas_binarias([0, 0], [0, 0])
        self.assertEqual(m["precision"], 0.0)
        self.assertEqual(m["f1"], 0.0)

    def test_frase_de_metricas_dice_los_numeros_en_castellano(self):
        frase = g.frase_de_metricas([1, 1, 0, 0], [1, 0, 0, 0],
                                    fenomeno="protesta", imprimir=False)
        self.assertIn("De cada 100", frase)
        self.assertIn("protesta", frase)
        self.assertIn("precisión", frase)

    def test_matriz_de_confusion(self):
        y_true = [0, 0, 1, 1, 1]
        y_pred = [0, 1, 1, 1, 0]
        ax = g.matriz_de_confusion(y_true, y_pred, etiquetas=["no", "sí"])
        self.assertEqual([t.get_text() for t in ax.get_xticklabels()], ["no", "sí"])
        textos = [t.get_text() for t in ax.texts]
        self.assertIn("2", textos)   # los verdaderos positivos

    def test_proyeccion_de_embeddings_reduce_dimensiones(self):
        rng = np.random.default_rng(0)
        V = rng.normal(size=(30, 50))
        palabras = [f"p{i}" for i in range(30)]
        ax = g.proyeccion_de_embeddings(V, palabras, resaltar=["p0"])
        self.assertGreaterEqual(len(ax.collections), 1)
        self.assertIn("p0", [t.get_text() for t in ax.texts])

    def test_proyeccion_de_embeddings_acepta_2d(self):
        V = np.random.default_rng(0).normal(size=(10, 2))
        ax = g.proyeccion_de_embeddings(V, [f"p{i}" for i in range(10)])
        self.assertGreaterEqual(len(ax.collections), 1)

    def test_mapa_de_atencion(self):
        rng = np.random.default_rng(0)
        W = rng.random((6, 6))
        W = W / W.sum(axis=1, keepdims=True)
        tokens = ["el", "diputado", "que", "habló", "se", "fue"]
        ax = g.mapa_de_atencion(W, tokens, mascara_causal=False)
        self.assertEqual([t.get_text() for t in ax.get_yticklabels()], tokens)

    def test_mapa_de_atencion_causal_no_anota_el_futuro(self):
        W = np.tril(np.ones((5, 5)))
        W = W / W.sum(axis=1, keepdims=True)
        ax = g.mapa_de_atencion(W, list("abcde"), mascara_causal=True)
        # 1+2+3+4+5 = 15 celdas anotadas (el triángulo inferior)
        anotaciones = [t for t in ax.texts if t.get_text().startswith(".")
                       or t.get_text()[0].isdigit()]
        self.assertLessEqual(len(anotaciones), 15)

    def test_grilla_de_filtros(self):
        filtros = np.random.default_rng(0).normal(size=(8, 3, 3))
        fig, ejes = g.grilla_de_filtros(filtros, ncols=4)
        self.assertEqual(ejes.shape, (2, 4))
        plt.close(fig)

    @unittest.skipUnless(HAY_TORCH, "sin torch")
    def test_grilla_de_filtros_acepta_un_conv_de_torch(self):
        conv = torch.nn.Conv2d(3, 6, kernel_size=3)
        fig, _ = g.grilla_de_filtros(conv.weight, ncols=3)
        plt.close(fig)

    def test_mostrar_imagenes_marca_los_errores(self):
        X = np.random.default_rng(0).random((4, 8, 8))
        fig, ejes = g.mostrar_imagenes(X, etiquetas=["a", "b", "c", "d"],
                                       predicciones=["a", "b", "c", "X"], ncols=4)
        colores = [ejes[0][i].title.get_color() for i in range(4)]
        self.assertEqual(colores.count(g.OK), 3)
        self.assertEqual(colores.count(g.ERROR), 1)
        plt.close(fig)

    def test_guardar_crea_el_archivo(self):
        import tempfile
        fig, ax = g.figura()
        ax.plot([1, 2, 3])
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = g.guardar(fig, os.path.join(carpeta, "sub", "figura.png"))
            self.assertTrue(os.path.exists(ruta))
            self.assertGreater(os.path.getsize(ruta), 1000)
        plt.close(fig)

    def test_estilo_oscuro_cambia_la_paleta_y_vuelve(self):
        claro = g.paleta()["modelo"]
        g.estilo_curso(oscuro=True)
        self.assertNotEqual(g.paleta()["modelo"], claro)
        g.estilo_curso()   # dejamos todo como estaba
        self.assertEqual(g.paleta()["modelo"], claro)


# ===========================================================================
# Doctests de los módulos
# ===========================================================================

def load_tests(loader, tests, ignore):
    """unittest corre también los ejemplos de los docstrings."""
    import doctest
    for modulo in (utils, datos, g):
        tests.addTests(doctest.DocTestSuite(modulo))
    return tests


# ===========================================================================
# Las figuras de muestra, para mirarlas con los ojos
# ===========================================================================

def generar_figuras(carpeta: str = "/tmp/ssdl-check") -> list[str]:
    """
    Genera una figura por cada función de graficos.py y las guarda en `carpeta`.

    No es un test automático: es para ABRIRLAS Y MIRARLAS. Un gráfico puede
    pasar todos los asserts y ser ilegible.
    """
    os.makedirs(carpeta, exist_ok=True)
    utils.fijar_semilla(1983)
    hechas = []

    def registrar(fig, nombre):
        ruta = g.guardar(fig, os.path.join(carpeta, nombre))
        plt.close(fig)
        hechas.append(ruta)
        print("  ·", ruta)

    # --- 1. familia de funciones (clase 1) ---
    ax = g.plot_familia(lambda x, a: a * x ** 2, valores=[-1, -0.4, 0.4, 1, 2, 3],
                        x=(-4, 4), nombre_parametro="a", destacar=1,
                        titulo="La misma función, seis perillas distintas",
                        xlabel="x  (la variable: dónde miro)",
                        ylabel="f(x) = a · x²")
    registrar(ax.figure, "01-plot_familia.png")

    # --- 2. función suelta ---
    ax = g.plot_funcion(lambda x: np.maximum(0, x - 2) - np.maximum(0, x - 6) * 0.7,
                        x=(0, 10), etiqueta="dos rampas sumadas",
                        titulo="Una función hecha de rampas",
                        xlabel="x", ylabel="f(x)")
    registrar(ax.figure, "02-plot_funcion.png")

    # --- 3. la serie de las clases 1 a 4 ---
    anios, seguridad = datos.serie_menciones("seguridad")
    ax = g.plot_serie(anios, seguridad, etiqueta="menciones a seguridad",
                      titulo="El dataset que nos acompaña de la clase 1 a la 4")
    registrar(ax.figure, "03-plot_serie.png")

    # --- 4. el ajuste con los errores (LA figura del curso) ---
    x, y = datos.recta_con_ruido(n=25, a=1.8, b=2.0, ruido=1.6)
    ax = g.plot_ajuste(x, y, modelo=lambda t: 1.2 * t + 4.0,
                       verdad=lambda t: 1.8 * t + 2.0,
                       titulo="Datos, modelo y errores",
                       xlabel="x", ylabel="y", etiqueta_modelo="mi recta (a=1,2  b=4,0)")
    registrar(ax.figure, "04-plot_ajuste.png")

    # --- 5. nubes de clases ---
    fig, ejes = g.figura(13, 3.6, filas=1, columnas=4,
                         titulo="Los cuatro datasets de juguete")
    for ax, (nombre, funcion) in zip(ejes, [
            ("espiral", datos.espiral), ("dos lunas", datos.dos_lunas),
            ("círculos", datos.circulos_concentricos), ("XOR", datos.xor)]):
        X, yy = funcion(n=240)
        g.scatter_clases(X, yy, ax=ax, titulo=nombre, s=16)
        ax.legend().set_visible(False)
    registrar(fig, "05-scatter_clases.png")

    # --- 6. frontera de decisión ---
    X, yy = datos.dos_lunas(240, ruido=0.14)
    # Una regresión logística a ojo: alta en la luna de abajo, que es la clase 1.
    ax = g.frontera_de_decision(
        lambda XX: 1 / (1 + np.exp(-(1.4 * XX[:, 0] - 2.6 * XX[:, 1] + 0.5))),
        X, yy, titulo="Lo que el modelo decide en cada punto del plano",
        etiquetas=["clase 0 (luna de arriba)", "clase 1 (luna de abajo)"])
    registrar(ax.figure, "06-frontera_de_decision.png")

    # --- 7. el paisaje de loss con la trayectoria (clase 3) ---
    # x centrada en cero: con x sin centrar, a y b quedan correlacionadas y el
    # valle es una zanja diagonal donde el descenso zigzaguea eternamente.
    xs, ys = datos.recta_con_ruido(n=30, a=2.0, b=1.0, ruido=1.2,
                                   x_min=-3, x_max=3)

    def loss_ab(a, b):
        return float(np.mean((ys - (a * xs + b)) ** 2))

    tray, _ = ent.descenso_a_mano(lambda p: loss_ab(p[0], p[1]), [-1.0, 5.0],
                                  lr=0.06, pasos=60)
    fig, _ = g.superficie_de_loss(loss_ab, rango_a=(-1.5, 5), rango_b=(-3, 6),
                                  trayectoria=tray, modo="ambos", optimo=(2.0, 1.0),
                                  titulo="Soltar la pelota en el paisaje de la loss")
    registrar(fig, "07-superficie_de_loss.png")

    fig, _ = g.superficie_de_loss(loss_ab, rango_a=(-1.5, 5), rango_b=(-3, 6),
                                  trayectoria=tray, modo="contorno",
                                  optimo=(2.0, 1.0), titulo="El mapa, solo")
    registrar(fig, "07b-superficie_de_loss-contorno.png")

    # --- 8. la loss en 1D con la pendiente medida a resta (clase 3) ---
    ax = g.plot_loss_1d(lambda a: loss_ab(a, 1.0), rango=(-1, 5), punto=0.2,
                        paso_de_prueba=0.4, nombre_parametro="a",
                        titulo="La pendiente, medida con una resta")
    registrar(ax.figure, "08-plot_loss_1d.png")

    # --- 9. curvas de entrenamiento con sobreajuste (clase 4) ---
    epocas = np.arange(1, 81)
    train = 1.6 * np.exp(-epocas / 14) + 0.05
    val = 1.6 * np.exp(-epocas / 11) + 0.14 + 0.010 * np.maximum(0, epocas - 26)
    ax = g.curvas_de_entrenamiento(train=train, val=val,
                                   titulo="Cuando la naranja se despega, eso es sobreajuste")
    registrar(ax.figure, "09-curvas_de_entrenamiento.png")

    # --- 10. matriz de confusión (clase 9) ---
    rng = np.random.default_rng(1983)
    y_true = rng.binomial(1, 0.28, size=500)
    ruido = rng.random(500)
    y_pred = np.where(y_true == 1, (ruido < 0.72).astype(int),
                      (ruido < 0.11).astype(int))
    ax = g.matriz_de_confusion(y_true, y_pred,
                               etiquetas=["no menciona protesta", "menciona protesta"],
                               nombre_positivo="menciona protesta",
                               titulo="¿En qué se equivoca el clasificador?")
    registrar(ax.figure, "10-matriz_de_confusion.png")

    # --- 11. embeddings (clase 6) ---
    palabras = ["diputado", "senador", "banca", "recinto", "sesión", "quórum",
                "ley", "decreto", "veto", "reglamento", "artículo", "inciso",
                "inflación", "salario", "jubilación", "presupuesto", "déficit",
                "protesta", "marcha", "reclamo", "sindicato", "paro",
                "escuela", "universidad", "docente", "beca", "matrícula",
                "hospital", "vacuna", "médico", "salud"]
    grupos = (["parlamento"] * 12 + ["economía"] * 5 + ["conflicto"] * 5
              + ["educación"] * 5 + ["salud"] * 4)
    centros = {"parlamento": [3.2, 1.0], "economía": [-2.4, 2.2],
               "conflicto": [-1.4, -2.8], "educación": [2.0, -2.4],
               "salud": [-3.0, -0.4]}
    V = np.array([np.array(centros[gr] + [0.0] * 6)
                  + rng.normal(0, 0.55, size=8) for gr in grupos])
    ax = g.proyeccion_de_embeddings(V, palabras, grupos=grupos,
                                    resaltar=["diputado", "protesta"],
                                    titulo="El mapa donde viven las palabras")
    registrar(ax.figure, "11-proyeccion_de_embeddings.png")

    # --- 12. mapa de atención (clase 7) ---
    tokens = ["el", "diputado", "que", "presentó", "el", "proyecto",
              "dijo", "que", "él", "lo", "iba", "a", "defender"]
    n = len(tokens)
    W = rng.random((n, n)) * 0.25
    W += np.eye(n) * 0.5
    for i in range(1, n):
        W[i, i - 1] += 0.6
    W[8, 1] += 2.6          # "él" mira a "diputado": el antecedente
    W[7, 6] += 1.0
    W = np.tril(W)
    W = W / W.sum(axis=1, keepdims=True)
    ax = g.mapa_de_atencion(W, tokens, mascara_causal=True,
                            titulo="Quién mira a quién (cabeza 3, capa 2)")
    registrar(ax.figure, "12-mapa_de_atencion.png")

    # --- 13. grilla de filtros (clase 5) ---
    base = np.zeros((8, 5, 5))
    base[0, :, :2], base[0, :, 3:] = -1, 1           # borde vertical
    base[1, :2, :], base[1, 3:, :] = -1, 1           # borde horizontal
    base[2] = np.eye(5) * 2 - 0.4                    # diagonal
    base[3] = 1 / 25                                 # blur
    base[4] = -0.2; base[4, 2, 2] = 2.4              # realce del centro
    base[5] = rng.normal(0, 0.6, (5, 5))             # uno al azar: porquería
    base[6] = np.outer(np.hanning(5), np.hanning(5)) - 0.3
    base[7] = np.fliplr(np.eye(5)) * 2 - 0.4
    titulos = ["borde vertical", "borde horizontal", "diagonal", "blur",
               "realce", "al azar (porquería)", "mancha", "anti-diagonal"]
    fig, _ = g.grilla_de_filtros(base, ncols=4, titulos=titulos)
    registrar(fig, "13-grilla_de_filtros.png")

    # --- 14. grilla de imágenes con aciertos y errores (clase 5) ---
    imgs = rng.random((8, 12, 12)) * 0.4
    for k in range(8):
        imgs[k, 3:9, 4:8] += 0.6
    etiquetas = ["remera", "pantalón", "buzo", "vestido",
                 "abrigo", "sandalia", "camisa", "zapatilla"]
    predicciones = list(etiquetas)
    predicciones[2], predicciones[6] = "vestido", "remera"
    fig, _ = g.mostrar_imagenes(imgs, etiquetas=etiquetas,
                                predicciones=predicciones, ncols=4,
                                titulo="Análisis de errores: dónde se confunde")
    registrar(fig, "14-mostrar_imagenes.png")

    return hechas


if __name__ == "__main__":
    if "--figuras" in sys.argv:
        i = sys.argv.index("--figuras")
        destino = sys.argv[i + 1] if len(sys.argv) > i + 1 else "/tmp/ssdl-check"
        print(f"Generando figuras de muestra en {destino}/ ...")
        rutas = generar_figuras(destino)
        print(f"\n{len(rutas)} figuras. Ahora ABRILAS Y MIRALAS.")
    else:
        unittest.main(verbosity=2)
