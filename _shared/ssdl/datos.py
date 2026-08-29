"""
ssdl.datos — traer los datos adentro del notebook sin sufrir.

Tres cosas viven acá:

1. CARGA. Funciones que leen `datos/muestras/` y te devuelven arrays de numpy o
   listas de diccionarios. Nunca fallan por falta de red: las muestras están
   versionadas en el repo. Si el wifi del aula es un desastre, la clase igual
   se da.

2. TEXTO. Tokenizadores a nivel carácter y a nivel palabra, escritos a mano en
   veinte líneas. En la clase 6 se abren y se leen; en la clase 8 uno de ellos
   entrena el mini-GPT.

3. JUGUETES. Datasets sintéticos chiquitos (espiral, dos lunas, círculos, XOR)
   para las clases 1 a 4, donde lo que importa es ver la forma del problema, no
   el problema.

Todo lo sintético está declarado como sintético. Siempre.

    from ssdl import datos
    anios, seguridad = datos.serie_menciones("seguridad")
"""

from __future__ import annotations

import csv
import json
import pathlib
import re
from collections import Counter

import numpy as np

from .utils import SEMILLA_DEL_CURSO, raiz_del_repo


# ---------------------------------------------------------------------------
# Dónde están los archivos
# ---------------------------------------------------------------------------

def ruta_de_datos(*partes) -> pathlib.Path:
    """
    Arma una ruta adentro de `datos/`, la encuentre donde la encuentre.

        datos.ruta_de_datos("muestras", "series", "menciones-por-tema-apertura.csv")
    """
    return raiz_del_repo().joinpath("datos", *partes)


def ruta_de_muestras(*partes) -> pathlib.Path:
    """Igual que `ruta_de_datos`, pero adentro de `datos/muestras/`."""
    return ruta_de_datos("muestras", *partes)


def _leer_csv(ruta) -> list[dict]:
    """Lee un CSV con encabezado y devuelve una lista de diccionarios."""
    ruta = pathlib.Path(ruta)
    if not ruta.exists():
        raise FileNotFoundError(
            f"No encuentro {ruta}.\n"
            "Si estás en Colab, ¿corriste la celda de bootstrap?\n"
            "Si estás local, ¿el notebook está adentro del repo?"
        )
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------------------
# 1. LA SERIE QUE ATRAVIESA LAS CLASES 1 A 4
# ---------------------------------------------------------------------------

TEMAS_DISPONIBLES = ["seguridad", "inflacion", "educacion", "trabajo", "salud"]


def serie_menciones(tema: str = "seguridad", desde: int = 1984, hasta: int = 2019,
                    suavizada: bool = False, en_porcentaje: bool = True):
    """
    El dataset del hilo conductor: qué porcentaje de las palabras del discurso
    presidencial de apertura de sesiones se dedicó a un tema, año por año.

    Datos REALES: derivados de los 108 discursos de apertura del Congreso
    argentino (1854-2019). Ver datos/README.md para la procedencia y la
    licencia. La medición es un conteo de léxico, con todas las limitaciones
    que eso tiene — y de eso justamente habla la clase 10.

    Este es el mismo dataset en las clases 1 (ajustar a ojo), 2 (rampas),
    3 (el paisaje de loss) y 4 (entrenar de verdad). Que sea el mismo es
    deliberado: reconocerlo en la clase 4 es la mitad de la sensación
    de haber avanzado.

    Parámetros
    ----------
    tema : uno de TEMAS_DISPONIBLES.
        "seguridad" es la serie de las clases 1, 3 y 4.
        "inflacion" es la de la clase 2 (tiene dos picos y un valle: imposible
        para una recta, perfecta para ocho rampas).
    desde, hasta : recorte de años (inclusive).
    suavizada : usa la media móvil de 3 años en vez de la serie cruda.
    en_porcentaje : los valores del CSV YA vienen en porcentaje (0,42 quiere
        decir "el 0,42% de las palabras del discurso"). Con False te los
        devuelve como fracción (0,0042), por si necesitás esa escala.

    Devuelve (anios, valores), los dos arrays de numpy.

    >>> anios, v = serie_menciones("seguridad")
    >>> len(anios) == len(v) and len(anios) > 30
    True
    """
    if tema not in TEMAS_DISPONIBLES:
        raise ValueError(f"Tema desconocido: {tema!r}. "
                         f"Los que hay son: {', '.join(TEMAS_DISPONIBLES)}")

    filas = _leer_csv(ruta_de_muestras("series", "menciones-por-tema-apertura.csv"))
    columna = f"{tema}_suave" if suavizada else tema

    anios, valores = [], []
    for fila in filas:
        anio = int(fila["anio"])
        if desde <= anio <= hasta:
            anios.append(anio)
            valores.append(float(fila[columna]))

    if not anios:
        raise ValueError(f"No hay datos entre {desde} y {hasta}. "
                         "La serie va de 1854 a 2019.")

    v = np.array(valores, dtype=float)
    return np.array(anios, dtype=float), v if en_porcentaje else v / 100.0


def serie_completa(desde: int = 1984, hasta: int = 2019) -> dict:
    """
    Todas las series de temas de una, más el presidente de cada año. Útil para
    la clase 10 (¿el modelo detecta el tema o detecta la época?).

    Devuelve un diccionario: {"anios": array, "presidente": lista,
    "palabras": array, "seguridad": array, "inflacion": array, ...}
    """
    filas = _leer_csv(ruta_de_muestras("series", "menciones-por-tema-apertura.csv"))
    filas = [f for f in filas if desde <= int(f["anio"]) <= hasta]
    salida = {
        "anios": np.array([int(f["anio"]) for f in filas], dtype=float),
        "presidente": [f["presidente"] for f in filas],
        "palabras": np.array([int(f["palabras"]) for f in filas], dtype=float),
    }
    for tema in TEMAS_DISPONIBLES:
        salida[tema] = np.array([float(f[tema]) for f in filas])
    return salida


# ---------------------------------------------------------------------------
# 2. TEXTO: discursos, debates, prensa
# ---------------------------------------------------------------------------

def discursos_apertura(anios=None) -> dict[int, str]:
    """
    Los discursos de apertura de sesiones que están en las muestras del repo.
    Datos REALES (documentos oficiales del Congreso argentino).

    Devuelve {anio: texto}. Ojo: en `datos/muestras/` hay una selección chica;
    el corpus completo se baja con `datos/descargar.py`.
    """
    carpeta = ruta_de_muestras("discursos-apertura")
    salida = {}
    for archivo in sorted(carpeta.glob("[0-9][0-9][0-9][0-9]-*.txt")):
        anio = int(archivo.name[:4])
        if anios is None or anio in anios:
            salida[anio] = archivo.read_text(encoding="utf-8")
    return salida


def corpus_mini_gpt(max_caracteres: int | None = None) -> str:
    """
    El texto plano preparado para entrenar el mini-GPT de la clase 8, hecho de
    discursos de apertura. Datos REALES.

    Si preferís el corpus sintético (que tiene la ventaja decisiva de que
    conocemos el proceso generador), usá `debates_aguasclaras()`.
    """
    ruta = ruta_de_muestras("discursos-apertura", "corpus-mini-gpt.txt")
    texto = ruta.read_text(encoding="utf-8")
    return texto[:max_caracteres] if max_caracteres else texto


def debates_aguasclaras(max_caracteres: int | None = None,
                        sin_encabezado: bool = True) -> str:
    """
    El Diario de Sesiones de la República de Aguasclaras.

    ⚠ CORPUS SINTÉTICO. Aguasclaras es un país que no existe. Ninguno de esos
    diputados, partidos ni leyes es real. Lo generamos nosotros con
    `datos/generar_aguasclaras.py` y semilla 1983.

    ¿Por qué inventar un corpus pudiendo usar uno real? Por tres razones, y la
    tercera es la que importa:
      1. Volumen sin depender de la red.
      2. Cero riesgo de poner frases inventadas en boca de personas reales.
      3. CONOCEMOS EL PROCESO GENERADOR. Por eso en la clase 8 podemos poner la
         verdad al lado de la alucinación y mostrar exactamente en qué momento
         el modelo se inventó un diputado que no existe. Con un corpus real, esa
         demostración es imposible.

    Parámetros
    ----------
    sin_encabezado : saca las líneas de advertencia que arrancan con '#'.
    """
    texto = ruta_de_muestras("aguasclaras", "debates.txt").read_text(encoding="utf-8")
    if sin_encabezado:
        texto = "\n".join(l for l in texto.splitlines() if not l.startswith("#")).strip()
    return texto[:max_caracteres] if max_caracteres else texto


def prensa_aguasclaras() -> list[dict]:
    """
    Titulares de los diarios de Aguasclaras, con año, diario, línea editorial,
    tema y la etiqueta `menciona_protesta` (0/1). ⚠ SINTÉTICO.

    Es el dataset de la clase 9 (clasificar) y de la clase 10 (auditar ese
    mismo clasificador). Los enteros vienen ya convertidos.
    """
    filas = _leer_csv(ruta_de_muestras("aguasclaras", "prensa.csv"))
    for f in filas:
        f["anio"] = int(f["anio"])
        f["menciona_protesta"] = int(f["menciona_protesta"])
    return filas


def verdad_aguasclaras() -> dict:
    """
    El padrón de la verdad de Aguasclaras: qué partidos, qué diputados y qué
    leyes existen realmente en ese país inventado.

    Es la columna derecha de la viz `por-que-alucina.html` de la clase 8: la
    lista contra la que se chequea si el modelo se inventó a alguien.
    """
    ruta = ruta_de_muestras("aguasclaras", "verdad.json")
    return json.loads(ruta.read_text(encoding="utf-8"))


def titulares_prensa(n: int | None = None, semilla: int = SEMILLA_DEL_CURSO,
                     con_texto: bool = False) -> list[dict]:
    """
    Titulares de prensa en castellano con etiqueta verdadero/falso, tema y
    fuente. Datos REALES (ver datos/README.md para procedencia y licencia).

    Parámetros
    ----------
    n : cuántos devolver (muestra aleatoria con semilla fija). None = todos.
    con_texto : incluir el cuerpo recortado de la nota, no sólo el titular.

    Devuelve una lista de diccionarios con las claves: id, titular, categoria
    ("Fake"/"True"), tema, fuente y (opcional) texto.
    """
    filas = _leer_csv(ruta_de_muestras("prensa", "titulares-prensa-es.csv"))
    registros = []
    for f in filas:
        r = {"id": f["id"], "titular": f["titular"], "categoria": f["categoria"],
             "tema": f["tema"], "fuente": f["fuente"],
             "es_falso": int(f["categoria"].strip().lower() == "fake")}
        if con_texto:
            r["texto"] = f.get("texto_recortado", "")
        registros.append(r)

    if n is not None and n < len(registros):
        rng = np.random.default_rng(semilla)
        indices = rng.choice(len(registros), size=n, replace=False)
        registros = [registros[i] for i in sorted(indices)]
    return registros


def discursos_casarosada(n: int | None = None) -> list[dict]:
    """
    Discursos presidenciales 2015-2024 con orador y fecha. Datos REALES.
    Útil para la clase 6 (embeddings por época) y la 10 (confusor temporal).

    Devuelve lista de diccionarios: orador, fecha, discurso.
    """
    filas = _leer_csv(ruta_de_muestras("casarosada", "discursos-muestra.csv"))
    registros = [{"orador": f["orador"], "fecha": f["fecha"],
                  "discurso": f["discurso_recortado"]} for f in filas]
    return registros[:n] if n else registros


# ---------------------------------------------------------------------------
# 3. TOKENIZAR: partir el texto en fichas
# ---------------------------------------------------------------------------

class TokenizadorCaracteres:
    """
    El tokenizador más simple que existe: cada carácter es una ficha.

    Es el de la clase 8 (el mismo que usa Karpathy en "Let's build GPT") y es el
    ideal para empezar, porque el vocabulario es chiquito (unas 90 fichas) y no
    hay ninguna decisión escondida: lo que ves es lo que hay.

        tok = datos.TokenizadorCaracteres()
        tok.ajustar(corpus)
        ids = tok.codificar("hola")        # [45, 52, 49, 38]
        tok.decodificar(ids)               # 'hola'
        len(tok)                           # tamaño del vocabulario
    """

    def __init__(self, texto: str | None = None):
        self.fichas: list[str] = []
        self.a_id: dict[str, int] = {}
        self.a_ficha: dict[int, str] = {}
        if texto is not None:
            self.ajustar(texto)

    def ajustar(self, texto: str) -> "TokenizadorCaracteres":
        """Mira el texto y arma el vocabulario: todos los caracteres, ordenados."""
        self.fichas = sorted(set(texto))
        self.a_id = {c: i for i, c in enumerate(self.fichas)}
        self.a_ficha = {i: c for c, i in self.a_id.items()}
        return self

    def codificar(self, texto: str) -> list[int]:
        """Texto -> lista de números. Los caracteres desconocidos se saltean."""
        return [self.a_id[c] for c in texto if c in self.a_id]

    def decodificar(self, ids) -> str:
        """Lista de números -> texto."""
        return "".join(self.a_ficha[int(i)] for i in ids)

    def __len__(self) -> int:
        return len(self.fichas)

    def __repr__(self) -> str:
        return f"<TokenizadorCaracteres: {len(self)} fichas distintas>"


class TokenizadorPalabras:
    """
    Una ficha por palabra. Más intuitivo que el de caracteres, pero con dos
    problemas que en la clase 6 se ven en vivo:

      1. El vocabulario explota (decenas de miles de fichas).
      2. Toda palabra que no viste en el entrenamiento se convierte en <desc>
         ("desconocida") y el modelo pierde la información. "Kirchnerismo" y
         "berenjena" pasan a ser la misma cosa: nada.

    Por eso los modelos de verdad usan sub-palabras, que es el punto medio.

        tok = datos.TokenizadorPalabras(minimo=2)
        tok.ajustar(corpus)
        tok.codificar("la sesion continua")
    """

    PATRON = re.compile(r"\w+|[^\w\s]", re.UNICODE)
    DESCONOCIDA = "<desc>"

    def __init__(self, texto: str | None = None, minimo: int = 1,
                 minusculas: bool = True):
        self.minimo = minimo
        self.minusculas = minusculas
        self.fichas: list[str] = []
        self.a_id: dict[str, int] = {}
        self.a_ficha: dict[int, str] = {}
        self.frecuencias = Counter()
        if texto is not None:
            self.ajustar(texto)

    def partir(self, texto: str) -> list[str]:
        """Parte el texto en palabras y signos. Sin magia: una expresión regular."""
        if self.minusculas:
            texto = texto.lower()
        return self.PATRON.findall(texto)

    def ajustar(self, texto: str) -> "TokenizadorPalabras":
        """Arma el vocabulario con las palabras que aparecen al menos `minimo` veces."""
        self.frecuencias = Counter(self.partir(texto))
        frecuentes = sorted(p for p, c in self.frecuencias.items() if c >= self.minimo)
        self.fichas = [self.DESCONOCIDA] + frecuentes
        self.a_id = {p: i for i, p in enumerate(self.fichas)}
        self.a_ficha = {i: p for p, i in self.a_id.items()}
        return self

    def codificar(self, texto: str) -> list[int]:
        """Texto -> números. Lo que no está en el vocabulario va a <desc> (el 0)."""
        return [self.a_id.get(p, 0) for p in self.partir(texto)]

    def decodificar(self, ids) -> str:
        """Números -> texto. No recupera los espacios originales: los inventa."""
        return " ".join(self.a_ficha[int(i)] for i in ids)

    def cobertura(self, texto: str) -> float:
        """
        Qué proporción de las palabras de `texto` SÍ está en el vocabulario.
        Si te da 0.82, una de cada cinco palabras se le convirtió en <desc>.
        """
        palabras = self.partir(texto)
        if not palabras:
            return 1.0
        return sum(1 for p in palabras if p in self.a_id) / len(palabras)

    def __len__(self) -> int:
        return len(self.fichas)

    def __repr__(self) -> str:
        return (f"<TokenizadorPalabras: {len(self)} fichas "
                f"(min. {self.minimo} apariciones)>")


def vocabulario(texto: str, minimo: int = 1, top: int | None = None) -> Counter:
    """
    Cuenta palabras. Devuelve un Counter, así que `vocabulario(t).most_common(20)`
    te da las 20 más frecuentes.
    """
    tok = TokenizadorPalabras(minusculas=True)
    conteo = Counter(tok.partir(texto))
    conteo = Counter({p: c for p, c in conteo.items() if c >= minimo})
    if top:
        return Counter(dict(conteo.most_common(top)))
    return conteo


def matriz_de_coocurrencia(texto: str, top: int = 4000, ventana: int = 5,
                           minimo: int = 5):
    """
    Cuenta cuántas veces cada par de palabras aparece cerca (dentro de una
    ventana de `ventana` palabras a cada lado).

    Es la materialización de la **hipótesis distribucional** de la clase 6:
    "sabrás una palabra por la compañía que tiene". La matriz ES la compañía.

    Devuelve `(M, palabras)` donde `M[i, j]` es cuántas veces `palabras[j]`
    apareció cerca de `palabras[i]`.

        M, pal = datos.matriz_de_coocurrencia(datos.corpus_mini_gpt())
        M.shape                                  # (n, n)
    """
    tok = TokenizadorPalabras(minusculas=True)
    fichas = [f for f in tok.partir(texto) if f.isalpha()]
    conteo = Counter(fichas)
    conteo = Counter({p: c for p, c in conteo.items() if c >= minimo})
    palabras = [p for p, _ in conteo.most_common(top)]
    idx = {p: i for i, p in enumerate(palabras)}
    n = len(palabras)
    M = np.zeros((n, n), dtype=np.float32)
    ids = [idx.get(f, -1) for f in fichas]
    for k, i in enumerate(ids):
        if i < 0:
            continue
        ini = max(0, k - ventana)
        fin = min(len(ids), k + ventana + 1)
        for m in range(ini, fin):
            if m == k:
                continue
            j = ids[m]
            if j >= 0:
                M[i, j] += 1.0
    return M, palabras


def embeddings_ppmi_svd(texto: str, dim: int = 100, top: int = 4000,
                        ventana: int = 5, minimo: int = 5):
    """
    Embeddings de palabra **con numpy y nada más**: sin Hugging Face, sin red,
    sin entrenar nada. Coocurrencia → PPMI → SVD.

    Por qué existe. La clase 6 necesita que el mapa de palabras salga del
    corpus real que los estudiantes acaban de tokenizar, no de un modelo bajado
    que hay que creerle. Y la clase 9 lo usa como **plan B** si Hugging Face no
    está disponible el día de la clase.

    Las tres líneas que importan, y que se pueden leer en clase:

      1. **Coocurrencia**: cuántas veces dos palabras aparecen cerca.
      2. **PPMI** (*positive pointwise mutual information*): cuánto más de lo
         esperado por azar aparecen juntas. Descuenta que "de" está cerca de
         todo simplemente porque "de" está en todos lados.
      3. **SVD**: quedarse con las `dim` direcciones que más variación explican.

    Devuelve `(V, palabras)`: `V[i]` es el vector de `palabras[i]`, normalizado
    a norma 1 (así el producto punto ya es la similitud coseno).

        V, pal = datos.embeddings_ppmi_svd(datos.corpus_mini_gpt())
        datos.vecinos("provincias", V, pal)
    """
    M, palabras = matriz_de_coocurrencia(texto, top=top, ventana=ventana,
                                         minimo=minimo)
    total = M.sum()
    if total == 0:
        raise ValueError("El texto no alcanza para construir coocurrencias.")
    fila = M.sum(axis=1, keepdims=True)
    col = M.sum(axis=0, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        pmi = np.log((M * total) / (fila * col))
    ppmi = np.nan_to_num(pmi, nan=0.0, posinf=0.0, neginf=0.0)
    ppmi[ppmi < 0] = 0.0                      # la P de PPMI: sólo lo positivo
    U, sv, _ = np.linalg.svd(ppmi, full_matrices=False)
    V = U[:, :dim] * sv[:dim]
    normas = np.linalg.norm(V, axis=1, keepdims=True)
    normas[normas == 0] = 1.0
    return (V / normas).astype(np.float32), palabras


def vecinos(palabra: str, vectores, palabras, k: int = 8):
    """
    Las `k` palabras más parecidas a `palabra`, con su similitud coseno.

    Es la herramienta de lectura de la clase 6: los vecinos cuentan una
    historia sobre el corpus, no sobre el idioma. Si `provincias` tiene de
    vecinas a `misiones`, `formosa` y `corrientes`, eso dice algo sobre de qué
    provincias habla este corpus.

    Devuelve una lista de `(palabra, similitud)`, de más a menos parecida.

        V, pal = datos.embeddings_ppmi_svd(texto)
        datos.vecinos("docentes", V, pal, k=5)
    """
    vectores = np.asarray(vectores)
    if palabra not in palabras:
        raise KeyError(
            f"«{palabra}» no está en el vocabulario. Probá con una más "
            f"frecuente, o bajá el `minimo` al construir los embeddings.")
    i = list(palabras).index(palabra)
    sim = vectores @ vectores[i]
    orden = np.argsort(-sim)
    return [(palabras[j], float(sim[j])) for j in orden if j != i][:k]


# ---------------------------------------------------------------------------
# Alias hacia los nombres de datos/descargar.py
#
# `datos/descargar.py` es la capa de abajo (baja, cachea, cae a muestras) y usa
# otro orden de palabras en dos nombres. Si venís leyendo `datos/README.md` y
# escribís el nombre de allá, funciona igual en vez de darte un AttributeError
# a mitad de la clase.
# ---------------------------------------------------------------------------

prensa_titulares = titulares_prensa          # datos/descargar.py lo llama así
corpus_discursos_texto = corpus_mini_gpt     # ídem


# ---------------------------------------------------------------------------
# 4. PARTIR LOS DATOS (la clase 4)
# ---------------------------------------------------------------------------

def particion(n: int, p_train: float = 0.7, p_val: float = 0.15,
              semilla: int = SEMILLA_DEL_CURSO):
    """
    Parte `n` casos al azar en train / validación / test.

    ATENCIÓN, y esto es la clase 4: partir al azar SÓLO es correcto si tus casos
    son independientes. Si tenés datos de panel (la misma persona medida cinco
    veces), o series de tiempo, partir al azar es hacer trampa sin darte cuenta:
    el modelo ve a la misma persona en train y en test y parece adivino.
    Para esos casos están `particion_temporal` y `particion_por_grupo`.

    Devuelve tres arrays de índices (train, val, test).

    >>> tr, va, te = particion(100)
    >>> len(tr), len(va), len(te)
    (70, 15, 15)
    >>> len(set(tr) & set(te))
    0
    """
    rng = np.random.default_rng(semilla)
    indices = rng.permutation(n)
    corte_1 = int(round(n * p_train))
    corte_2 = int(round(n * (p_train + p_val)))
    return indices[:corte_1], indices[corte_1:corte_2], indices[corte_2:]


def particion_temporal(anios, corte_val: int, corte_test: int):
    """
    Parte por tiempo: entreno con el pasado, valido con el medio, testeo con el
    futuro. Es la partición honesta cuando tu pregunta es predictiva ("¿sirve
    para el año que viene?").

        tr, va, te = particion_temporal(anios, corte_val=2010, corte_test=2015)
        # train: < 2010, val: 2010-2014, test: >= 2015

    Devuelve tres arrays de índices.
    """
    anios = np.asarray(anios)
    return (np.where(anios < corte_val)[0],
            np.where((anios >= corte_val) & (anios < corte_test))[0],
            np.where(anios >= corte_test)[0])


def particion_por_grupo(grupos, p_train: float = 0.7, p_val: float = 0.15,
                        semilla: int = SEMILLA_DEL_CURSO):
    """
    Parte de modo que un mismo grupo (persona, diario, provincia, sesión) caiga
    ENTERO de un solo lado. Es la partición que evita la fuga más común en
    ciencias sociales.

        tr, va, te = particion_por_grupo([f["diario"] for f in notas])

    Devuelve tres arrays de índices.
    """
    grupos = np.asarray(grupos, dtype=object)
    unicos = np.array(sorted(set(grupos.tolist())), dtype=object)
    rng = np.random.default_rng(semilla)
    orden = rng.permutation(len(unicos))
    corte_1 = int(round(len(unicos) * p_train))
    corte_2 = int(round(len(unicos) * (p_train + p_val)))

    def indices_de(bloque):
        conjunto = set(unicos[orden[bloque]].tolist())
        return np.array([i for i, gr in enumerate(grupos) if gr in conjunto], dtype=int)

    return (indices_de(slice(0, corte_1)),
            indices_de(slice(corte_1, corte_2)),
            indices_de(slice(corte_2, None)))


def diagnostico_de_fuga(indices_train, indices_test, grupos=None, textos=None) -> dict:
    """
    Revisa si tu partición tiene fugas (leakage) y te lo dice en castellano.

    Chequea dos cosas:
      - que ningún índice esté en los dos lados;
      - que ningún grupo (si le pasás `grupos`) aparezca de los dos lados;
      - que ningún texto idéntico esté duplicado cruzando la partición.

    Devuelve un diccionario con el diagnóstico e imprime el veredicto.
    """
    tr, te = set(np.asarray(indices_train).tolist()), set(np.asarray(indices_test).tolist())
    informe = {"indices_repetidos": sorted(tr & te),
               "grupos_cruzados": [], "textos_cruzados": 0}

    if grupos is not None:
        grupos = list(grupos)
        g_tr = {grupos[i] for i in tr}
        g_te = {grupos[i] for i in te}
        informe["grupos_cruzados"] = sorted(g_tr & g_te, key=str)

    if textos is not None:
        textos = list(textos)
        t_tr = {textos[i] for i in tr}
        informe["textos_cruzados"] = sum(1 for i in te if textos[i] in t_tr)

    problemas = (informe["indices_repetidos"] or informe["grupos_cruzados"]
                 or informe["textos_cruzados"])
    if problemas:
        print("⚠ HAY FUGA. Tu test no es un test.")
        if informe["indices_repetidos"]:
            print(f"  · {len(informe['indices_repetidos'])} casos están en train Y en test.")
        if informe["grupos_cruzados"]:
            print(f"  · {len(informe['grupos_cruzados'])} grupos aparecen de los dos "
                  f"lados: {informe['grupos_cruzados'][:5]}...")
            print("    Usá particion_por_grupo().")
        if informe["textos_cruzados"]:
            print(f"  · {informe['textos_cruzados']} textos idénticos duplicados "
                  "cruzando la partición.")
    else:
        print("✓ Sin fugas detectadas: train y test no comparten casos, "
              "grupos ni textos.")
    return informe


# ---------------------------------------------------------------------------
# 5. DATASETS DE JUGUETE (clases 1 a 4)
# ---------------------------------------------------------------------------
# Todos son SINTÉTICOS y todos están escritos a mano con numpy, para que se
# puedan leer. Existen para ver la FORMA de un problema, no el problema.

def recta_con_ruido(n: int = 40, a: float = 2.0, b: float = 1.0,
                    ruido: float = 1.0, x_min: float = 0, x_max: float = 10,
                    semilla: int = SEMILLA_DEL_CURSO):
    """
    Puntos alrededor de una recta. Sabemos LA VERDAD (a y b), que es la ventaja
    de los datos sintéticos: podemos comparar lo que el modelo encontró contra
    lo que realmente había.

    Devuelve (x, y).
    """
    rng = np.random.default_rng(semilla)
    x = np.linspace(x_min, x_max, n)
    y = a * x + b + rng.normal(0, ruido, size=n)
    return x, y


def curva_de_dos_picos(n: int = 60, ruido: float = 0.06,
                       semilla: int = SEMILLA_DEL_CURSO):
    """
    La curva objetivo de la clase 2: dos picos y un valle. Elegida a propósito
    porque es IMPOSIBLE para una recta y perfectamente alcanzable con ocho
    rampas. Tiene la misma forma que la serie de menciones a inflación.

    Devuelve (x, y, verdad), donde `verdad` es la función sin ruido: en la
    clase 4 se dibuja en gris punteado y es lo que el modelo debería recuperar.
    """
    rng = np.random.default_rng(semilla)

    def verdad(x):
        return (np.exp(-((x - 2.0) ** 2) / 0.8) * 1.0
                + np.exp(-((x - 7.0) ** 2) / 1.4) * 0.75
                + 0.05 * x)

    x = np.linspace(0, 10, n)
    y = verdad(x) + rng.normal(0, ruido, size=n)
    return x, y, verdad


def espiral(n: int = 300, clases: int = 2, ruido: float = 0.18,
            vueltas: float = 1.6, semilla: int = SEMILLA_DEL_CURSO):
    """
    Dos (o más) brazos de espiral entrelazados. El dataset de juguete más lindo
    que hay: es obviamente separable para un ojo humano y absolutamente
    imposible para una recta. Perfecto para la clase 2.

    Devuelve (X, y) con X de forma (n, 2) e y de forma (n,).

    >>> X, y = espiral(120, clases=2)
    >>> X.shape, set(y.tolist()) == {0, 1}
    ((120, 2), True)
    """
    rng = np.random.default_rng(semilla)
    por_clase = n // clases
    X, Y = [], []
    for c in range(clases):
        t = np.linspace(0.25, 1.0, por_clase)
        radio = t * 4.5
        angulo = t * vueltas * 2 * np.pi + c * (2 * np.pi / clases)
        angulo = angulo + rng.normal(0, ruido, size=por_clase)
        X.append(np.c_[radio * np.sin(angulo), radio * np.cos(angulo)])
        Y.append(np.full(por_clase, c))
    return np.vstack(X), np.concatenate(Y).astype(int)


def dos_lunas(n: int = 300, ruido: float = 0.16,
              semilla: int = SEMILLA_DEL_CURSO):
    """
    Dos medialunas encastradas. Como la espiral pero más suave: la frontera es
    curva pero no dramática.

    Devuelve (X, y).
    """
    rng = np.random.default_rng(semilla)
    m = n // 2
    t = np.linspace(0, np.pi, m)
    luna_a = np.c_[np.cos(t), np.sin(t)]
    luna_b = np.c_[1 - np.cos(t), 0.5 - np.sin(t)]
    X = np.vstack([luna_a, luna_b]) + rng.normal(0, ruido, size=(2 * m, 2))
    y = np.concatenate([np.zeros(m), np.ones(m)]).astype(int)
    return X, y


def circulos_concentricos(n: int = 300, ruido: float = 0.08, factor: float = 0.5,
                          semilla: int = SEMILLA_DEL_CURSO):
    """
    Un anillo adentro de otro. Ninguna recta puede separarlos, y sin embargo la
    regla es facilísima de decir: "los de adentro y los de afuera".

    Devuelve (X, y).
    """
    rng = np.random.default_rng(semilla)
    m = n // 2
    angulo_ext = rng.uniform(0, 2 * np.pi, m)
    angulo_int = rng.uniform(0, 2 * np.pi, m)
    X = np.vstack([
        np.c_[np.cos(angulo_ext), np.sin(angulo_ext)],
        np.c_[np.cos(angulo_int), np.sin(angulo_int)] * factor,
    ]) + rng.normal(0, ruido, size=(2 * m, 2))
    y = np.concatenate([np.zeros(m), np.ones(m)]).astype(int)
    return X, y


def xor(n: int = 300, ruido: float = 0.28, semilla: int = SEMILLA_DEL_CURSO):
    """
    Cuatro cúmulos en las cuatro esquinas, con las diagonales de la misma clase.
    Es el ejemplo histórico: el problema que hundió a los perceptrones en 1969 y
    que se resuelve con UNA capa escondida. Diez líneas de código, década de
    invierno de la IA.

    Devuelve (X, y).
    """
    rng = np.random.default_rng(semilla)
    centros = np.array([[-1, -1], [1, 1], [-1, 1], [1, -1]], dtype=float)
    etiquetas = np.array([0, 0, 1, 1])
    por_centro = n // 4
    X, Y = [], []
    for centro, etiqueta in zip(centros, etiquetas):
        X.append(centro + rng.normal(0, ruido, size=(por_centro, 2)))
        Y.append(np.full(por_centro, etiqueta))
    return np.vstack(X), np.concatenate(Y).astype(int)


# ---------------------------------------------------------------------------
# 6. PUENTE A PYTORCH
# ---------------------------------------------------------------------------

def a_tensores(*arrays, device=None, tipo=None):
    """
    Convierte arrays de numpy en tensores de PyTorch, de una.

        x_t, y_t = datos.a_tensores(x, y)
        X_t, y_t = datos.a_tensores(X, y, device=utils.elegir_device())

    Los enteros quedan como enteros (que es lo que las etiquetas de clase
    necesitan) y todo lo demás se pasa a float32, que es el tipo con el que
    trabaja PyTorch. Si `tipo` está seteado, manda ese para todos.
    """
    import torch
    salida = []
    for a in arrays:
        if isinstance(a, torch.Tensor):
            t = a
        else:
            a = np.asarray(a)
            destino = tipo or (torch.long if np.issubdtype(a.dtype, np.integer)
                               else torch.float32)
            t = torch.tensor(a, dtype=destino)
        salida.append(t.to(device) if device is not None else t)
    return salida[0] if len(salida) == 1 else tuple(salida)


if __name__ == "__main__":
    import doctest
    fallas, corridos = doctest.testmod()
    print(f"doctests: {corridos - fallas}/{corridos} OK")
