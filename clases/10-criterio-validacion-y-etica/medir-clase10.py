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
"""
import json
import os
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "_shared"))

import numpy as np  # noqa: E402
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
# Esto va ANTES de la ablacion a proposito: sin la banda de ruido, cualquier
# diferencia que midas despues es indistinguible de haber barajado distinto.
efes = []
for s in range(25):
    tr, te = train_test_split(np.arange(len(y)), test_size=0.25,
                              stratify=y, random_state=s)
    v_s, m_s = entrenar(documentos, tr, y)
    efes.append(evaluar(v_s, m_s, documentos, te, y)["f1"])
efes = np.array(efes)
R["ruido_de_particion"] = {
    "n_particiones": 25, "media": float(efes.mean()), "sd": float(efes.std()),
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


NOMBRES_PROPIOS = ["amlo", "meade", "morena", "anaya", "epn", "salinas", "pri",
                   "peña", "bronco", "sánchez", "putin", "irán", "cienfuegos", "pp"]

ablaciones = []
for etiqueta, quitados in [
        ("nada (el modelo original)", []),
        ("el termino n.o 1", [top_pos[0]["termino"]]),
        ("los 5 primeros", [t["termino"] for t in top_pos[:5]]),
        ("los 20 primeros", [t["termino"] for t in top_pos[:20]]),
        ("los 14 nombres propios", NOMBRES_PROPIOS)]:
    corpus2 = quitar(documentos, quitados)
    v2, m2 = entrenar(corpus2, i_train, y)
    met = evaluar(v2, m2, corpus2, i_test, y)
    ablaciones.append({"quitado": etiqueta, "n_quitados": len(quitados),
                       "metricas": met, "f1": met["f1"]})
R["ablacion"] = ablaciones

R["ablacion_vs_ruido"] = {
    "movimiento_maximo": float(max(abs(a["f1"] - base["f1"]) for a in ablaciones)),
    "rango_del_ruido": R["ruido_de_particion"]["rango"],
}

# =============================================================================
# 4. PLACEBO Y CONTROL POSITIVO
# =============================================================================
# (a) Control positivo: discursos presidenciales argentinos. Son 100% politica.
discursos = datos.discursos_casarosada()
fragmentos = []
for x in discursos:
    for frase in re.split(r"(?<=[.!?])\s+", x["discurso"]):
        frase = frase.strip()
        if 60 < len(frase) < 220:
            fragmentos.append(frase)
fragmentos = fragmentos[:600]
p_casarosada = float(modelo.predict(vec.transform(fragmentos)).mean())

# (b) Placebo negativo: titulares del corpus con las palabras barajadas.
rng = np.random.default_rng(SEMILLA)
def barajar(t):
    partes = t.split()
    rng.shuffle(partes)
    return " ".join(partes)


docs_test = [documentos[i] for i in i_test]
pred_orig = modelo.predict(vec.transform(docs_test))
pred_baraj = modelo.predict(vec.transform([barajar(t) for t in docs_test]))
iguales = float((pred_orig == pred_baraj).mean())

# (c) Placebo de dominio: prensa de Aguasclaras (SINTETICA, otro pais, otra epoca).
ac = datos.prensa_aguasclaras()
tit_ac = [n["titular"] for n in ac]
p_aguasclaras = float(modelo.predict(vec.transform(tit_ac)).mean())
# cuantos de esos titulares son sobre politica parlamentaria de verdad
p_ac_politica = float(np.mean([n["tema"] in ("legislativo", "politica", "seguridad")
                               for n in ac]))

R["placebo"] = {
    "casarosada": {"n": len(fragmentos), "proporcion_marcada": p_casarosada,
                   "esperado": 1.0,
                   "que_es": "fragmentos de discursos presidenciales argentinos 2015-2024"},
    "barajado": {"proporcion_predicciones_identicas": iguales,
                 "positivos_original": float(pred_orig.mean()),
                 "positivos_barajado": float(pred_baraj.mean())},
    "aguasclaras": {"n": len(tit_ac), "proporcion_marcada": p_aguasclaras,
                    "proporcion_realmente_politica": p_ac_politica},
}

# recall sobre el control positivo: es un corpus donde TODO es positivo
R["placebo"]["casarosada"]["recall_alli"] = p_casarosada
R["placebo"]["casarosada"]["recall_en_su_test"] = base["recall"]

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
     "El futbolista presentó su nuevo club"),
    ("cambio de agente", "El ministro visitó el hospital de la ciudad",
     "El cantante visitó el hospital de la ciudad"),
    ("mismo tema, otras palabras", "El congreso debate la reforma electoral",
     "La cámara discute los cambios al sistema de votación"),
    ("cambio de epoca", "El presidente presentó su plan de gobierno",
     "El primer mandatario expuso su programa de gestión"),
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
SUJETOS = [
    ("genero", "los trabajadores"), ("genero", "las trabajadoras"),
    ("genero", "los médicos"), ("genero", "las médicas"),
    ("genero", "los empresarios"), ("genero", "las empresarias"),
    ("ocupacion", "los docentes"), ("ocupacion", "los policías"),
    ("ocupacion", "los taxistas"), ("ocupacion", "los estudiantes"),
    ("ocupacion", "los empresarios"), ("ocupacion", "los enfermeros"),
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

# test de permutacion: ¿la diferencia por genero se distingue del azar?
sm = np.array([p["score_m"] for p in pares_genero])
sf = np.array([p["score_f"] for p in pares_genero])
dif_obs = float(np.mean(sf - sm))
rng2 = np.random.default_rng(SEMILLA)
signos = rng2.choice([-1, 1], size=(20000, len(sm)))
nulo = (signos * (sf - sm)).mean(axis=1)
p_valor = float((np.abs(nulo) >= abs(dif_obs)).mean())
R["sesgo"]["permutacion"] = {"diferencia_media": dif_obs, "p_valor": p_valor,
                             "n_pares": len(sm), "n_permutaciones": 20000}

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


# =============================================================================
# 9. LA ETIQUETA CIRCULAR — Aguasclaras (SINTETICO), el F1 = 1,00 que no vale
# =============================================================================
ac_y = np.array([n["menciona_protesta"] for n in ac])
ac_tr, ac_te = train_test_split(np.arange(len(ac_y)), test_size=0.25,
                                stratify=ac_y, random_state=SEMILLA)


def circular(palabras):
    corpus = quitar(tit_ac, palabras)
    v = CountVectorizer(min_df=2, binary=True)
    A = v.fit_transform([corpus[i] for i in ac_tr])
    m = LogisticRegression(max_iter=3000, class_weight="balanced",
                           random_state=SEMILLA).fit(A, ac_y[ac_tr])
    return g.metricas_binarias(ac_y[ac_te],
                               m.predict(v.transform([corpus[i] for i in ac_te])))


R["etiqueta_circular"] = {
    "corpus": "prensa de Aguasclaras — SINTETICO, pais ficticio",
    "n": int(len(ac_y)), "prevalencia": float(ac_y.mean()),
    "original": circular([]),
    "sin_protesta": circular(["protesta", "protestas"]),
    "sin_cinco_palabras": circular(["protesta", "protestas", "marcha", "marchas",
                                    "reclamo", "reclamos", "paro", "paros",
                                    "movilizacion", "movilizaciones"]),
}

# =============================================================================
# 10. LA FUGA POR LA FUENTE — verdadero/falso, al azar vs por medio
# =============================================================================
from sklearn.model_selection import GroupShuffleSplit  # noqa: E402

y_falso = np.array([n["es_falso"] for n in notas])
fuentes = np.array([n["fuente"] for n in notas])

tr_az, te_az = train_test_split(np.arange(len(y_falso)), test_size=0.25,
                                stratify=y_falso, random_state=SEMILLA)
gss = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=SEMILLA)
tr_gr, te_gr = next(gss.split(documentos, y_falso, groups=fuentes))


def falso(indices_tr, indices_te):
    v = CountVectorizer(min_df=2, binary=True)
    A = v.fit_transform([documentos[i] for i in indices_tr])
    m = LogisticRegression(max_iter=3000, class_weight="balanced",
                           random_state=SEMILLA).fit(A, y_falso[indices_tr])
    return g.metricas_binarias(y_falso[indices_te],
                               m.predict(v.transform([documentos[i] for i in indices_te])))


met_az = falso(tr_az, te_az)
met_gr = falso(tr_gr, te_gr)
prev_gr = float(y_falso[te_gr].mean())
medios = {}
for n in notas:
    medios.setdefault(n["fuente"], set()).add(n["categoria"])
R["fuga_por_fuente"] = {
    "tarea": "¿la nota es falsa?",
    "al_azar": met_az, "por_medio": met_gr,
    "piso_por_medio": max(prev_gr, 1 - prev_gr),
    "n_medios": len(medios),
    "medios_con_una_sola_clase": sum(1 for v in medios.values() if len(v) == 1),
}

# =============================================================================
# 11. LOS PESOS DEL MODELO — para que la viz calcule el score en el navegador
# =============================================================================
# Una regresion logistica sobre bolsa de palabras binaria es, literalmente,
# "sumar el peso de cada palabra presente y pasarlo por la sigmoide". La viz
# `sesgo-en-el-espejo.html` hace exactamente esa cuenta con estos numeros, asi
# que el estudiante puede escribir cualquier oracion y ver el score DE VERDAD.
PESOS = {str(t): round(float(w), 5) for t, w in zip(vocabulario, pesos)}

# comprobacion: la cuenta a mano tiene que dar lo mismo que sklearn
import math  # noqa: E402
_ficha = re.compile(r"[^\W_]{2,}", re.UNICODE)


def _score_a_mano(texto):
    z = float(modelo.intercept_[0])
    for w in set(_ficha.findall(texto.lower())):
        z += PESOS.get(w, 0.0)
    return 1 / (1 + math.exp(-z))


_control = [PLANTILLA.format(s) for _, s in SUJETOS] + [a for _, a, _ in PARES]
_dif = max(abs(_score_a_mano(t) - float(modelo.predict_proba(vec.transform([t]))[0, 1]))
           for t in _control)
assert _dif < 1e-4, f"la cuenta a mano no coincide con sklearn (dif {_dif})"
print(f"[ok] la cuenta a mano coincide con sklearn (dif maxima {_dif:.2e}, por redondeo a 5 decimales)")

pathlib.Path(__file__).resolve().parent.joinpath("pesos-clase10.js").write_text(
    "// Generado por medir-clase10.py — NO editar a mano.\n"
    "// Los pesos REALES de la regresion logistica auditada en la clase 10.\n"
    "window.PESOS10 = {\n intercepto: " + repr(round(float(modelo.intercept_[0]), 5)) +
    ",\n pesos: " + json.dumps(PESOS, ensure_ascii=False) + "\n};\n",
    encoding="utf-8")

# =============================================================================
# GUARDAR
# =============================================================================
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
print("\nABLACION")
for a in R["ablacion"]:
    print(f"  {a['quitado']:<28} F1 = {a['f1']:.3f}")
print("\nPLACEBO / CONTROL")
pl = R["placebo"]
print(f"  Casa Rosada (100% politica): marca {pl['casarosada']['proporcion_marcada']:.3f}")
print(f"  barajado: {pl['barajado']['proporcion_predicciones_identicas']:.3f} de predicciones identicas")
print(f"  Aguasclaras: marca {pl['aguasclaras']['proporcion_marcada']:.3f}")
print("\nSESGO")
print(f"  diferencia maxima = {R['sesgo']['diferencia_maxima']:.3f}  "
      f"({R['sesgo']['filas'][0]['sujeto']} {R['sesgo']['score_max']:.3f}  vs  "
      f"{R['sesgo']['filas'][-1]['sujeto']} {R['sesgo']['score_min']:.3f})")
print(f"  peso de 'los' = {R['sesgo']['peso_los']}   peso de 'las' = {R['sesgo']['peso_las']}")
print(f"  permutacion: dif={R['sesgo']['permutacion']['diferencia_media']:.4f} "
      f"p={R['sesgo']['permutacion']['p_valor']:.4f}")
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
print(f"  la ablacion movio como mucho {R['ablacion_vs_ruido']['movimiento_maximo']:.3f}; "
      f"el ruido de particion es {R['ablacion_vs_ruido']['rango_del_ruido']:.3f}")
print("\nETIQUETA CIRCULAR (Aguasclaras, SINTETICO)")
ec = R["etiqueta_circular"]
print(f"  original F1={ec['original']['f1']:.3f}  sin 'protesta' F1={ec['sin_protesta']['f1']:.3f}  "
      f"sin 5 palabras F1={ec['sin_cinco_palabras']['f1']:.3f}")
print("\nFUGA POR LA FUENTE (¿la nota es falsa?)")
fu = R["fuga_por_fuente"]
print(f"  al azar   acc={fu['al_azar']['accuracy']:.3f} F1={fu['al_azar']['f1']:.3f}")
print(f"  por medio acc={fu['por_medio']['accuracy']:.3f} F1={fu['por_medio']['f1']:.3f}  "
      f"(el piso ahi es {fu['piso_por_medio']:.3f})")
print(f"  {fu['medios_con_una_sola_clase']} de {fu['n_medios']} medios aparecen con una sola clase")
print("\nCOBERTURA PARCIAL (construido)")
cp = R["cobertura_parcial"]
print(f"  tono A={cp['tono_foro_a']:.2f}%  tono B={cp['tono_foro_b']:.2f}%")
print("=" * 74)
print("Escrito: datos-clase10.json y datos-clase10.js")
