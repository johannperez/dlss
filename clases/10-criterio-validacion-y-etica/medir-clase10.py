#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mediciones reales de la clase 10.

Todo numero que aparezca en las slides o en las visualizaciones de esta clase
sale de aca. Nada estimado, nada inventado: se corre, se guarda y se cita.

    PYTHONPATH=_shared python3 clases/10-criterio-validacion-y-etica/medir-clase10.py

Produce:
    clases/10-criterio-validacion-y-etica/datos-clase10.json
    clases/10-criterio-validacion-y-etica/datos-clase10.js     (el mismo, como global)

Corre en CPU, sin red, en menos de un minuto.

Es determinista en la misma máquina y con las mismas versiones de las
librerías; con otras versiones los números pueden cambiar un poco (en el
tercer decimal). Por eso el JSON guarda las versiones con las que se midió
(clave `entorno`): si tus números no coinciden, empezá por comparar eso.
"""
import json
import math
import pathlib
import platform
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "_shared"))

import numpy as np  # noqa: E402
import sklearn  # noqa: E402
from sklearn.feature_extraction.text import CountVectorizer  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402

from ssdl import datos, graficos as g, utils  # noqa: E402

utils.fijar_semilla(1983)
SEMILLA = 1983
R = {}


def redondear(obj, n=4):
    if isinstance(obj, dict):
        return {k: redondear(v, n) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [redondear(v, n) for v in obj]
    if isinstance(obj, (float, np.floating)):
        return round(float(obj), n)
    if isinstance(obj, (int, np.integer)):
        return int(obj)
    return obj


# =============================================================================
# 1. EL MODELO AUDITADO — "¿esta nota es sobre politica?"
# =============================================================================
notas = datos.titulares_prensa(con_texto=True)
titulares = [n["titular"] for n in notas]
documentos = [n["titular"] + " . " + n["texto"][:600] for n in notas]
y = np.array([int(n["tema"] == "Politica") for n in notas])

i_train, i_test = train_test_split(
    np.arange(len(y)), test_size=0.25, stratify=y, random_state=SEMILLA)


def entrenar(corpus, indices_train, etiquetas, min_df=2):
    vec = CountVectorizer(min_df=min_df, binary=True)
    A = vec.fit_transform([corpus[i] for i in indices_train])
    mod = LogisticRegression(max_iter=3000, class_weight="balanced",
                             random_state=SEMILLA)
    mod.fit(A, etiquetas[indices_train])
    return vec, mod


def evaluar(vec, mod, corpus, indices, etiquetas):
    pred = mod.predict(vec.transform([corpus[i] for i in indices]))
    return g.metricas_binarias(etiquetas[indices], pred)


vec, modelo = entrenar(documentos, i_train, y)
base = evaluar(vec, modelo, documentos, i_test, y)
prevalencia = float(y.mean())

pesos = modelo.coef_[0]
vocabulario = np.array(vec.get_feature_names_out())
orden = np.argsort(-pesos)
top_pos = [{"termino": str(vocabulario[i]), "peso": float(pesos[i])} for i in orden[:20]]
top_neg = [{"termino": str(vocabulario[i]), "peso": float(pesos[i])} for i in orden[-12:]]

R["modelo"] = {
    "tarea": "¿la nota de prensa es sobre politica?",
    "corpus": "Spanish Fake News Corpus 2.0 (prensa real, CC BY 4.0)",
    "n_total": len(y), "n_train": len(i_train), "n_test": len(i_test),
    "vocabulario": int(len(vocabulario)),
    "prevalencia": prevalencia,
    "piso": max(prevalencia, 1 - prevalencia),
    "metricas": base,
    "top_positivos": top_pos,
    "top_negativos": top_neg,
}


# =============================================================================
# 2. EL RUIDO DE LA PARTICION — cuanto se mueve el F1 solo por cambiar la semilla
# =============================================================================
# Esto es el ruido de UN modelo. Ojo: no es el error de una COMPARACION entre
# dos versiones evaluadas sobre la misma particion (eso es la seccion 3b).
N_SEMILLAS = 25
PARTICIONES = [train_test_split(np.arange(len(y)), test_size=0.25,
                                stratify=y, random_state=s) for s in range(N_SEMILLAS)]
efes = []
for tr, te in PARTICIONES:
    v_s, m_s = entrenar(documentos, tr, y)
    efes.append(evaluar(v_s, m_s, documentos, te, y)["f1"])
efes = np.array(efes)
R["ruido_de_particion"] = {
    "n_particiones": N_SEMILLAS, "media": float(efes.mean()), "sd": float(efes.std()),
    "minimo": float(efes.min()), "maximo": float(efes.max()),
    "rango": float(efes.max() - efes.min()),
    "valores": [float(v) for v in efes],
}

# =============================================================================
# 3. ABLACION — quitarle terminos al corpus y volver a entrenar
# =============================================================================
def quitar(corpus, palabras):
    if not palabras:
        return list(corpus)
    patron = re.compile(r"\b(" + "|".join(re.escape(p) for p in palabras) + r")\b", re.I)
    return [patron.sub(" ", t) for t in corpus]


# MISMA lista que la del notebook (celda de la seccion 3). Si cambia una,
# cambia la otra: dos definiciones del mismo experimento en un curso sobre
# reproducibilidad seria exactamente el error que la clase denuncia.
# `lopezobrador_` es la ficha que deja la cuenta @lopezobrador_: es un nombre
# propio (el TODO 1 la cuenta como tal) y antes no se sacaba en la ablacion.
NOMBRES_PROPIOS = ["amlo", "meade", "morena", "anaya", "epn", "salinas", "pri",
                   "peña", "bronco", "sánchez", "putin", "irán", "cienfuegos",
                   "pp", "lópez", "obrador", "trump", "biden", "lopezobrador_"]

ABLACIONES = [
    ("nada (el modelo original)", []),
    ("el termino n.o 1", [top_pos[0]["termino"]]),
    ("los 5 primeros", [t["termino"] for t in top_pos[:5]]),
    ("los 20 primeros", [t["termino"] for t in top_pos[:20]]),
    (f"los {len(NOMBRES_PROPIOS)} nombres propios", NOMBRES_PROPIOS)]
CORPUS_ABLADO = [quitar(documentos, q) for _, q in ABLACIONES]

# (3a) UNA sola particion: lo que haria cualquiera
ablaciones = []
for (etiqueta, quitados), corpus2 in zip(ABLACIONES, CORPUS_ABLADO):
    v2, m2 = entrenar(corpus2, i_train, y)
    met = evaluar(v2, m2, corpus2, i_test, y)
    ablaciones.append({"quitado": etiqueta, "n_quitados": len(quitados),
                       "metricas": met, "f1": met["f1"]})
R["ablacion"] = ablaciones

# (3b) La comparacion bien hecha: la MISMA intervencion repetida con cada una
# de las 25 particiones, y la diferencia PAREADA (ablado - original, sobre la
# misma particion). El error que importa es el de esa diferencia, no el rango
# del F1 suelto. Las 25 particiones comparten datos, asi que no son 25
# repeticiones independientes: el error estandar ingenuo (DE/raiz(25)) es
# optimista. Usamos la correccion de Nadeau y Bengio (2003):
#     EE = DE * raiz(1/J + n_test/n_train)
n_te, n_tr = len(PARTICIONES[0][1]), len(PARTICIONES[0][0])
factor_nb = math.sqrt(1 / N_SEMILLAS + n_te / n_tr)
pareadas = []
for (etiqueta, quitados), corpus2 in zip(ABLACIONES[1:], CORPUS_ABLADO[1:]):
    deltas = []
    for (tr, te), f0 in zip(PARTICIONES, efes):
        v2, m2 = entrenar(corpus2, tr, y)
        deltas.append(evaluar(v2, m2, corpus2, te, y)["f1"] - f0)
    deltas = np.array(deltas)
    de = float(deltas.std(ddof=1))
    ee = de * factor_nb
    pareadas.append({
        "quitado": etiqueta, "n_quitados": len(quitados),
        "deltas": [float(d) for d in deltas],
        "media": float(deltas.mean()), "de": de,
        "ee_corregido": ee,
        "ic95_bajo": float(deltas.mean() - 2 * ee), "ic95_alto": float(deltas.mean() + 2 * ee),
        "negativas": int((deltas < 0).sum()),
    })
R["ablacion_pareada"] = {
    "n_particiones": N_SEMILLAS, "factor_nadeau_bengio": factor_nb,
    "filas": pareadas,
    "de_del_f1_suelto": float(efes.std()),
}
R["ablacion_vs_ruido"] = {
    "movimiento_maximo_una_particion": float(max(abs(a["f1"] - base["f1"]) for a in ablaciones)),
    "rango_del_f1_suelto": R["ruido_de_particion"]["rango"],
    "nota": "comparar una diferencia pareada con el rango del F1 suelto es comparar mal; "
            "ver ablacion_pareada",
}

# =============================================================================
# 4. CONTROL POSITIVO, PLACEBO, INVARIANCIA Y FUERA DE DOMINIO
# =============================================================================
def oraciones(texto):
    return [f.strip() for f in re.split(r"(?<=[.!?])\s+", texto) if 60 < len(f.strip()) < 220]


# (a) Control positivo: TODAS las oraciones de 60-220 caracteres de los
# discursos presidenciales argentinos (no las primeras N, que salian casi todas
# de los discursos que aparecen primero en el archivo). Son 100 % politica.
discursos = datos.discursos_casarosada()
fragmentos, de_que_discurso = [], []
for k, x in enumerate(discursos):
    for frase in oraciones(x["discurso"]):
        fragmentos.append(frase)
        de_que_discurso.append(k)
p_casarosada = float(modelo.predict(vec.transform(fragmentos)).mean())

# (a') La referencia con el mismo largo: oraciones de 60-220 caracteres de las
# notas de politica del PROPIO test. El modelo se entreno con documentos de
# ~100 palabras y los fragmentos tienen ~20: parte de la caida es el largo.
pos_test = [i for i in i_test if y[i] == 1]
oraciones_propias = [s for i in pos_test for s in oraciones(notas[i]["texto"])]
p_oraciones_propias = float(modelo.predict(vec.transform(oraciones_propias)).mean())

# (a'') La hipotesis de los nombres propios, testeada: reentrenar sin ellos y
# volver a correr el control positivo.
corpus_sin_np = CORPUS_ABLADO[-1]
v_np, m_np = entrenar(corpus_sin_np, i_train, y)
met_np = evaluar(v_np, m_np, corpus_sin_np, i_test, y)
p_casarosada_sin_np = float(m_np.predict(v_np.transform(fragmentos)).mean())
p_oraciones_sin_np = float(m_np.predict(v_np.transform(oraciones_propias)).mean())

R["control_positivo"] = {
    "que_es": "oraciones de 60-220 caracteres de discursos presidenciales argentinos 2015-2024",
    "n": len(fragmentos), "n_discursos_con_fragmentos": len(set(de_que_discurso)),
    "n_discursos": len(discursos),
    "proporcion_marcada": p_casarosada, "esperado": 1.0,
    "recall_en_su_test": base["recall"],
    "referencia_mismo_largo": {"que_es": "oraciones de 60-220 caracteres de las notas de politica del test",
                               "n": len(oraciones_propias), "recall": p_oraciones_propias},
    "sin_nombres_propios": {"f1_test": met_np["f1"], "recall_test": met_np["recall"],
                            "proporcion_marcada": p_casarosada_sin_np,
                            "recall_oraciones_propias": p_oraciones_sin_np},
}

# (b) Placebo de verdad: donde el fenomeno NO deberia aparecer. Notas de
# Deporte y Espectaculos del test (el modelo no las vio), mismo corpus, mismo
# registro. Si el modelo mide "politica", deberia marcar casi ninguna.
TEMAS_PLACEBO = ("Deporte", "Espectaculos")
i_placebo = [i for i in i_test if notas[i]["tema"] in TEMAS_PLACEBO]
pred_placebo = modelo.predict(vec.transform([documentos[i] for i in i_placebo]))
R["placebo"] = {
    "que_es": "notas de Deporte y Espectaculos del test (no vistas en el entrenamiento)",
    "temas": list(TEMAS_PLACEBO), "n": len(i_placebo),
    "marcadas": int(pred_placebo.sum()), "proporcion_marcada": float(pred_placebo.mean()),
    "titulares_marcados": [notas[i]["titular"] for i, p in zip(i_placebo, pred_placebo) if p],
}

# (c) Test de invariancia: el mismo texto con las palabras barajadas. NO es un
# placebo (el fenomeno sigue ahi): pregunta si el modelo usa el orden.
rng = np.random.default_rng(SEMILLA)
def barajar(t):
    partes = t.split()
    rng.shuffle(partes)
    return " ".join(partes)


docs_test = [documentos[i] for i in i_test]
pred_orig = modelo.predict(vec.transform(docs_test))
pred_baraj = modelo.predict(vec.transform([barajar(t) for t in docs_test]))
R["invariancia"] = {"proporcion_predicciones_identicas": float((pred_orig == pred_baraj).mean()),
                    "positivos_original": float(pred_orig.mean()),
                    "positivos_barajado": float(pred_baraj.mean())}

# (d) Fuera de dominio: titulares de Aguasclaras (SINTETICO, pais ficticio,
# 2015-2024, sin tildes). Son en su mayoria de politica institucional
# (sesiones, bloques, leyes, protestas): funcionan como un SEGUNDO control
# positivo, no como placebo.
ac = datos.prensa_aguasclaras()
tit_ac = [n["titular"] for n in ac]
p_aguasclaras = float(modelo.predict(vec.transform(tit_ac)).mean())
VOC_LEGISLATIVO = re.compile(r"\b(ley|leyes|sesion|bloque|recinto|comision|diputad\w*|"
                             r"senad\w*|oficialismo|legislatur\w*|camara)\b", re.I)
p_ac_legislativo = float(np.mean([bool(VOC_LEGISLATIVO.search(t)) for t in tit_ac]))
R["fuera_de_dominio"] = {
    "que_es": "titulares de Aguasclaras (SINTETICO, pais ficticio, 2015-2024, sin tildes)",
    "n": len(tit_ac), "proporcion_marcada": p_aguasclaras,
    "proporcion_con_vocabulario_legislativo": p_ac_legislativo,
    "anios": [min(n["anio"] for n in ac), max(n["anio"] for n in ac)],
}

# (e) Prevalencia: el modelo entrena con class_weight="balanced". Contar
# predicciones no estima bien la prevalencia cuando FP != FN.
q = float(pred_orig.mean())
tpr = base["recall"]
fpr = base["fp"] / (base["fp"] + base["vn"])
R["prevalencia_por_conteo"] = {
    "real_en_test": float(y[i_test].mean()), "contando_predicciones": q,
    "fp": int(base["fp"]), "fn": int(base["fn"]),
    "corregida_con_tpr_fpr": float((q - fpr) / (tpr - fpr)),
    "nota": "la correccion usa TPR/FPR medidos sobre el mismo test: es circular; "
            "en un proyecto se miden en una muestra validada aparte",
}

# =============================================================================
# 5. PARES MINIMOS
# =============================================================================
PARES = [
    ("negacion", "El gobierno aprobó la ley de presupuesto",
     "El gobierno no aprobó la ley de presupuesto"),
    ("negacion", "El senado rechazó el proyecto",
     "El senado no rechazó el proyecto"),
    ("cambio de pais", "AMLO anunció una reforma al sistema de salud",
     "El presidente de Uruguay anunció una reforma al sistema de salud"),
    ("cambio de pais", "Morena ganó las elecciones en el estado",
     "El Frente Amplio ganó las elecciones en el departamento"),
    ("cambio de agente", "El diputado presentó un proyecto sobre vivienda",
     "El futbolista presentó un proyecto sobre vivienda"),
    ("cambio de agente", "El ministro visitó el hospital de la ciudad",
     "El cantante visitó el hospital de la ciudad"),
    ("paráfrasis", "El congreso debate la reforma electoral",
     "La cámara discute los cambios al sistema de votación"),
    ("sinónimo", "El presidente presentó su plan de gobierno",
     "El primer mandatario presentó su plan de gobierno"),
]
filas_pares = []
for tipo, a, b in PARES:
    sa, sb = modelo.predict_proba(vec.transform([a, b]))[:, 1]
    filas_pares.append({"tipo": tipo, "a": a, "b": b,
                        "score_a": float(sa), "score_b": float(sb),
                        "delta": float(sb - sa)})
R["pares_minimos"] = filas_pares

# =============================================================================
# 6. AUDITORIA DE SESGO — la misma oracion, distinto sujeto
# =============================================================================
PLANTILLA = "{} reclamó frente a la sede del ministerio"
# MISMA lista que la del notebook (seccion 9). 17 sujetos, ninguno repetido:
# antes "los empresarios" estaba en dos dimensiones y la auditoria decia 18.
SUJETOS = [
    ("genero", "los trabajadores"), ("genero", "las trabajadoras"),
    ("genero", "los médicos"), ("genero", "las médicas"),
    ("genero", "los empresarios"), ("genero", "las empresarias"),
    ("ocupacion", "los docentes"), ("ocupacion", "los policías"),
    ("ocupacion", "los taxistas"), ("ocupacion", "los estudiantes"),
    ("ocupacion", "los enfermeros"),
    ("origen", "los vecinos"), ("origen", "los migrantes"),
    ("origen", "los venezolanos"), ("origen", "los mexicanos"),
    ("origen", "los campesinos"), ("origen", "los indígenas"),
]
frases = [PLANTILLA.format(s) for _, s in SUJETOS]
scores = modelo.predict_proba(vec.transform(frases))[:, 1]
vocab_set = set(vocabulario)
filas_sesgo = []
for (dim, sujeto), sc in zip(SUJETOS, scores):
    palabras = sujeto.split()
    fuera = [w for w in palabras if w not in vocab_set]
    filas_sesgo.append({"dimension": dim, "sujeto": sujeto, "score": float(sc),
                        "fuera_de_vocabulario": fuera})
R["sesgo"] = {
    "plantilla": PLANTILLA,
    "filas": sorted(filas_sesgo, key=lambda f: -f["score"]),
    "diferencia_maxima": float(scores.max() - scores.min()),
    "score_max": float(scores.max()), "score_min": float(scores.min()),
}

# pares de genero: la diferencia sale del articulo, no del sustantivo
pares_genero = []
for m_, f_ in [("los trabajadores", "las trabajadoras"),
               ("los médicos", "las médicas"),
               ("los empresarios", "las empresarias"),
               ("los docentes", "las docentes"),
               ("los enfermeros", "las enfermeras"),
               ("los vecinos", "las vecinas"),
               ("los estudiantes", "las estudiantes"),
               ("los jubilados", "las jubiladas"),
               ("los abogados", "las abogadas"),
               ("los periodistas", "las periodistas")]:
    sm, sf = modelo.predict_proba(vec.transform(
        [PLANTILLA.format(m_), PLANTILLA.format(f_)]))[:, 1]
    pares_genero.append({
        "masculino": m_, "femenino": f_,
        "score_m": float(sm), "score_f": float(sf), "delta": float(sf - sm),
        "sustantivo_en_vocabulario": m_.split()[1] in vocab_set,
    })
R["sesgo"]["pares_genero"] = pares_genero
R["sesgo"]["peso_los"] = float(pesos[list(vocabulario).index("los")]) if "los" in vocab_set else None
R["sesgo"]["peso_las"] = float(pesos[list(vocabulario).index("las")]) if "las" in vocab_set else None

# ¿De donde sale la diferencia por genero? En logit (antes de la sigmoide) la
# diferencia de cada par es EXACTAMENTE: peso(las) - peso(los) + (peso del
# sustantivo femenino - peso del masculino). La parte del articulo es la misma
# en los 10 pares: no son 10 evidencias independientes.
w_art = R["sesgo"]["peso_las"] - R["sesgo"]["peso_los"]
def _peso(p):
    return float(pesos[vec.vocabulary_[p]]) if p in vec.vocabulary_ else 0.0


for p in pares_genero:
    p["logit_articulo"] = w_art
    p["logit_sustantivo"] = _peso(p["femenino"].split()[1]) - _peso(p["masculino"].split()[1])
R["sesgo"]["logit_articulo"] = w_art
R["sesgo"]["pares_solo_articulo"] = sum(1 for p in pares_genero if p["logit_sustantivo"] == 0)

# Test de signos exacto: con 10 pares hay 2**10 = 1024 patrones de signo, asi
# que se enumeran todos (muestrear 20.000 no agrega nada).
import itertools  # noqa: E402
sm = np.array([p["score_m"] for p in pares_genero])
sf = np.array([p["score_f"] for p in pares_genero])
dif_obs = float(np.mean(sf - sm))
patrones = np.array(list(itertools.product([-1, 1], repeat=len(sm))))
nulo = (patrones * (sf - sm)).mean(axis=1)
p_valor = float((np.abs(nulo) >= abs(dif_obs) - 1e-12).mean())
R["sesgo"]["permutacion"] = {"diferencia_media": dif_obs, "p_valor_exacto": p_valor,
                             "n_pares": len(sm), "n_patrones": int(len(patrones)),
                             "todas_positivas": bool((sf - sm > 0).all())}
R["sesgo"]["alguno_cruza_05"] = bool(max(float(scores.max()), float(sf.max()), float(sm.max())) >= 0.5)

# =============================================================================
# 7. CASO 2 DE LA VIZ — el confusor temporal, con datos reales
# =============================================================================
cr = [x for x in discursos if x["orador"] in ("Mauricio Macri", "Alberto Fernández")]
X_cr = [x["discurso"] for x in cr]
y_cr = np.array([int(x["orador"] == "Alberto Fernández") for x in cr])
anios_cr = np.array([int(x["fecha"][-4:]) for x in cr])

itr_cr, ite_cr = train_test_split(np.arange(len(y_cr)), test_size=0.3,
                                  stratify=y_cr, random_state=SEMILLA)
v_cr = CountVectorizer(min_df=2, binary=True, max_features=4000)
A_cr = v_cr.fit_transform([X_cr[i] for i in itr_cr])
m_cr = LogisticRegression(max_iter=3000, class_weight="balanced",
                          random_state=SEMILLA).fit(A_cr, y_cr[itr_cr])
met_cr = g.metricas_binarias(y_cr[ite_cr],
                             m_cr.predict(v_cr.transform([X_cr[i] for i in ite_cr])))

# la misma particion, pero la etiqueta es el periodo, no la persona
y_periodo = (anios_cr >= 2020).astype(int)
coincidencia = float((y_periodo == y_cr).mean())
m_per = LogisticRegression(max_iter=3000, class_weight="balanced",
                           random_state=SEMILLA).fit(A_cr, y_periodo[itr_cr])
met_per = g.metricas_binarias(y_periodo[ite_cr],
                              m_per.predict(v_cr.transform([X_cr[i] for i in ite_cr])))

anios_macri = sorted(set(anios_cr[y_cr == 0].tolist()))
anios_af = sorted(set(anios_cr[y_cr == 1].tolist()))
R["confusor_temporal"] = {
    "n": len(y_cr), "n_train": len(itr_cr), "n_test": len(ite_cr),
    "metricas_orador": met_cr,
    "metricas_periodo": met_per,
    "coincidencia_etiquetas": coincidencia,
    "anios_macri": anios_macri, "anios_fernandez": anios_af,
    "anios_solapados": sorted(set(anios_macri) & set(anios_af)),
    "n_solapados": int(np.sum(np.isin(anios_cr, list(set(anios_macri) & set(anios_af))))),
}

# =============================================================================
# 8. CASO 3 DE LA VIZ — cobertura parcial (corpus CONSTRUIDOS a mano)
# =============================================================================
# Dos foros con el MISMO tono y estructuras de interaccion opuestas.
# Estan escritos a mano para esta clase: son un ejemplo construido, no un dato.
LEXICO_TONO = ["absurdo", "vergüenza", "mentira", "fracaso", "desastre",
               "escandaloso", "inaceptable", "ridículo", "grave", "error"]
FORO_A = [  # todos se pelean con todos: estructura polarizada
    "Lo que propone el bloque de enfrente es un absurdo y una vergüenza",
    "Responder eso es un error grave, la mentira ya es un escándalo",
    "Su desastre de gestión es inaceptable, y decirlo no es ridículo",
    "El fracaso es de ellos y sostener lo contrario es una mentira",
]
FORO_B = [  # el mismo tono, pero todos le pegan al mismo tercero ausente
    "Lo que hizo la empresa es un absurdo y una vergüenza",
    "El error grave fue de la empresa, y su mentira es un escándalo",
    "Su desastre de gestión es inaceptable, coincido, y no es ridículo",
    "El fracaso es de la empresa y sostener lo contrario es una mentira",
]


def tono(corpus):
    total = sum(len(t.split()) for t in corpus)
    hits = sum(sum(1 for w in t.lower().split()
                   if any(w.startswith(l[:5]) for l in LEXICO_TONO)) for t in corpus)
    return 100.0 * hits / total


R["cobertura_parcial"] = {
    "aclaracion": "Corpus CONSTRUIDOS a mano para mostrar el mecanismo. No son datos.",
    "tono_foro_a": tono(FORO_A), "tono_foro_b": tono(FORO_B),
    "interlocutores_distintos_a": 2, "interlocutores_distintos_b": 1,
    "foro_a": FORO_A, "foro_b": FORO_B,
    "lexico": LEXICO_TONO,
}


# (Las secciones "etiqueta circular" y "fuga por la fuente" que habia aca no las
# usaba ninguna slide ni viz: se sacaron. La fuga por la fuente es tema de la
# clase 9 y esta medida en datos/README.md §1.3.)

# =============================================================================
# 11. LOS PESOS DEL MODELO — para que la viz calcule el score en el navegador
# =============================================================================
# Una regresion logistica sobre bolsa de palabras binaria es, literalmente,
# "sumar el peso de cada palabra presente y pasarlo por la sigmoide". La viz
# `sesgo-en-el-espejo.html` hace exactamente esa cuenta con estos numeros, asi
# que el estudiante puede escribir cualquier oracion y ver el score DE VERDAD.
PESOS = {str(t): round(float(w), 5) for t, w in zip(vocabulario, pesos)}

# comprobacion: la cuenta a mano tiene que dar lo mismo que sklearn
# Misma regla que CountVectorizer (r"(?u)\b\w\w+\b"): corridas de 2 o mas
# caracteres de palabra, guion bajo incluido (por eso `lopezobrador_` existe).
# La viz usa /[\p{L}\p{N}_]{2,}/gu, que es lo mismo.
_ficha = re.compile(r"\w{2,}", re.UNICODE)


def _score_a_mano(texto):
    z = float(modelo.intercept_[0])
    for w in set(_ficha.findall(texto.lower())):
        z += PESOS.get(w, 0.0)
    return 1 / (1 + math.exp(-z))


_control = ([PLANTILLA.format(s) for _, s in SUJETOS] + [a for _, a, _ in PARES] +
            [b for _, _, b in PARES] + ["Critica de @lopezobrador_ al presupuesto"])
_dif = max(abs(_score_a_mano(t) - float(modelo.predict_proba(vec.transform([t]))[0, 1]))
           for t in _control)
assert _dif < 1e-4, f"la cuenta a mano no coincide con sklearn (dif {_dif})"
print(f"[ok] la cuenta a mano coincide con sklearn (dif maxima {_dif:.2e}, por redondeo a 5 decimales)")
# y la tokenizacion a mano da las mismas fichas que sklearn en todo el corpus
_analizador = vec.build_analyzer()
_voc = vec.vocabulary_
for _t in documentos:
    assert ({w for w in _ficha.findall(_t.lower()) if w in _voc} ==
            {w for w in _analizador(_t) if w in _voc}), "la tokenizacion a mano difiere de sklearn"
print("[ok] la tokenizacion a mano da las mismas fichas que sklearn en los 1471 documentos")

pathlib.Path(__file__).resolve().parent.joinpath("pesos-clase10.js").write_text(
    "// Generado por medir-clase10.py — NO editar a mano.\n"
    "// Los pesos REALES de la regresion logistica auditada en la clase 10.\n"
    "window.PESOS10 = {\n intercepto: " + repr(round(float(modelo.intercept_[0]), 5)) +
    ",\n pesos: " + json.dumps(PESOS, ensure_ascii=False) + "\n};\n",
    encoding="utf-8")

# =============================================================================
# GUARDAR
# =============================================================================
try:
    import torch  # noqa: F401
    _torch = torch.__version__
except ImportError:
    _torch = "no instalado"
R["entorno"] = {
    "python": platform.python_version(), "numpy": np.__version__,
    "sklearn": sklearn.__version__, "torch": _torch,
    "nota": "determinista en la misma maquina y con estas versiones; "
            "con otras, los numeros pueden cambiar un poco",
}
R = redondear(R)
salida = pathlib.Path(__file__).resolve().parent
(salida / "datos-clase10.json").write_text(
    json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
(salida / "datos-clase10.js").write_text(
    "// Generado por medir-clase10.py — NO editar a mano.\n"
    "// Todos estos numeros salen de correr el codigo sobre los datos reales del curso.\n"
    "window.DATOS10 = " + json.dumps(R, ensure_ascii=False, indent=1) + ";\n",
    encoding="utf-8")

print("=" * 74)
print("MODELO AUDITADO — ¿la nota es sobre politica?")
print(f"  n={R['modelo']['n_total']}  vocab={R['modelo']['vocabulario']}  "
      f"prevalencia={R['modelo']['prevalencia']:.3f}  piso={R['modelo']['piso']:.3f}")
mt = R["modelo"]["metricas"]
print(f"  accuracy={mt['accuracy']:.3f}  precision={mt['precision']:.3f}  "
      f"recall={mt['recall']:.3f}  F1={mt['f1']:.3f}")
print("  top 8:", ", ".join(t["termino"] for t in R["modelo"]["top_positivos"][:8]))
rp = R["ruido_de_particion"]
print(f"\nRUIDO DE PARTICION (25 semillas)  F1 media={rp['media']:.3f} "
      f"sd={rp['sd']:.3f}  de {rp['minimo']:.3f} a {rp['maximo']:.3f}  "
      f"(rango {rp['rango']:.3f})")
print("\nABLACION (una particion)")
for a in R["ablacion"]:
    print(f"  {a['quitado']:<28} F1 = {a['f1']:.3f}")
ap = R["ablacion_pareada"]
print(f"\nABLACION PAREADA ({ap['n_particiones']} particiones, EE corregido x{ap['factor_nadeau_bengio']:.3f})")
for a in ap["filas"]:
    print(f"  {a['quitado']:<28} media {a['media']:+.4f}  DE {a['de']:.4f}  "
          f"IC95 [{a['ic95_bajo']:+.3f}, {a['ic95_alto']:+.3f}]  negativas {a['negativas']}/25")
print("\nCONTROLES")
cp_ = R["control_positivo"]
print(f"  control positivo ({cp_['n']} fragmentos de {cp_['n_discursos_con_fragmentos']} discursos): "
      f"marca {cp_['proporcion_marcada']:.3f}")
print(f"  referencia mismo largo ({cp_['referencia_mismo_largo']['n']} oraciones propias): "
      f"{cp_['referencia_mismo_largo']['recall']:.3f}")
sn = cp_["sin_nombres_propios"]
print(f"  sin nombres propios: F1 test {sn['f1_test']:.3f}  control {sn['proporcion_marcada']:.3f}  "
      f"oraciones propias {sn['recall_oraciones_propias']:.3f}")
pl = R["placebo"]
print(f"  placebo ({pl['n']} notas de {'/'.join(pl['temas'])}): marca {pl['marcadas']} "
      f"({pl['proporcion_marcada']:.3f})")
print(f"  invariancia: {R['invariancia']['proporcion_predicciones_identicas']:.3f} identicas")
fd = R["fuera_de_dominio"]
print(f"  Aguasclaras: marca {fd['proporcion_marcada']:.3f}; con vocabulario legislativo "
      f"{fd['proporcion_con_vocabulario_legislativo']:.3f}")
pc = R["prevalencia_por_conteo"]
print(f"  prevalencia real {pc['real_en_test']:.3f}, contando {pc['contando_predicciones']:.3f}, "
      f"corregida {pc['corregida_con_tpr_fpr']:.3f}")
print("\nSESGO")
print(f"  diferencia maxima = {R['sesgo']['diferencia_maxima']:.3f}  "
      f"({R['sesgo']['filas'][0]['sujeto']} {R['sesgo']['score_max']:.3f}  vs  "
      f"{R['sesgo']['filas'][-1]['sujeto']} {R['sesgo']['score_min']:.3f})")
print(f"  peso de 'los' = {R['sesgo']['peso_los']}   peso de 'las' = {R['sesgo']['peso_las']}")
pm = R["sesgo"]["permutacion"]
print(f"  signos exacto: dif={pm['diferencia_media']:.4f} p={pm['p_valor_exacto']:.5f} "
      f"({pm['n_patrones']} patrones); pares solo-articulo {R['sesgo']['pares_solo_articulo']}")
print("\nCONFUSOR TEMPORAL")
ct = R["confusor_temporal"]
print(f"  orador  F1={ct['metricas_orador']['f1']:.3f}   "
      f"periodo F1={ct['metricas_periodo']['f1']:.3f}")
print(f"  las dos etiquetas coinciden en {ct['coincidencia_etiquetas']:.3f} de los casos")
print(f"  años Macri={ct['anios_macri']}  Fernandez={ct['anios_fernandez']}  "
      f"solapados={ct['anios_solapados']}")
print("\nPARES MINIMOS")
for f in R["pares_minimos"]:
    print(f"  [{f['tipo']:<26}] {f['score_a']:.3f} -> {f['score_b']:.3f}  ({f['delta']:+.3f})")
print("\nCOBERTURA PARCIAL (construido)")
cp = R["cobertura_parcial"]
print(f"  tono A={cp['tono_foro_a']:.2f}%  tono B={cp['tono_foro_b']:.2f}%")
print("=" * 74)
print("Escrito: datos-clase10.json y datos-clase10.js")
