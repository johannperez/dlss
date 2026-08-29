#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_aguasclaras.py — Corpus SINTETICO de debates parlamentarios y prensa
de la Republica de Aguasclaras, un pais que no existe.

======================================================================
POR QUE EXISTE ESTE ARCHIVO
======================================================================
El curso usa datos REALES siempre que puede (ver datos/README.md). Pero hay
una cosa que ningun corpus real puede darnos, y es la demostracion central
de la clase 8:

    poner LA VERDAD al lado de LA INVENCION del modelo.

Cuando un mini-GPT entrenado sobre discursos reales se inventa un diputado,
nadie en el aula puede verificar en 5 segundos que ese diputado no existe.
Con Aguasclaras si: el padron completo de diputados, partidos y leyes esta
en `verdad.json`, porque lo escribimos nosotros. Si el modelo dice
"el diputado Berrutti del Frente Ribereño", abrimos el padron y mostramos
que Berrutti no esta. Esa es toda la clase 8.

Ademas sirve de RED DE SEGURIDAD: si manana el repo de discursos reales
desaparece, este archivo regenera un corpus del tamaño necesario sin red.

======================================================================
QUE SE PIERDE POR SER SINTETICO (decilo en clase, no lo escondas)
======================================================================
- La distribucion de palabras es mas pobre y mas regular que la real.
  El modelo aprende mas rapido de lo que aprenderia con texto real.
- No hay ironia, ni chicanas espontaneas, ni errores de tipeo, ni las
  frases raras que hacen que el castellano real sea dificil.
- Las posiciones ideologicas son caricaturas legibles, no posiciones reales.
- NUNCA sirve para sacar una conclusion sustantiva sobre politica.
  Sirve para entender la MAQUINA, no para estudiar la SOCIEDAD.

REGLA INNEGOCIABLE: siempre rotulado como sintetico, en la slide, en el
notebook y en el pie de cualquier grafico que salga de aca.

Uso:
    python3 generar_aguasclaras.py --salida muestras/aguasclaras --mb 1.1
"""
from __future__ import annotations

import argparse
import json
import os
import random
import unicodedata

SEMILLA = 1983  # fija y declarada: la reproducibilidad se siembra desde la clase 4

# ----------------------------------------------------------------------
# EL PADRON: esto es LA VERDAD. La clase 8 la pone al lado de la invencion.
# ----------------------------------------------------------------------

PARTIDOS = [
    {"sigla": "PUN", "nombre": "Partido de la Union Nacional", "eje": "centro-derecha",
     "temas": ["orden", "inversion", "exportaciones", "seguridad"]},
    {"sigla": "MPR", "nombre": "Movimiento Popular Ribereño", "eje": "centro-izquierda",
     "temas": ["trabajo", "salud", "vivienda", "distribucion"]},
    {"sigla": "FCA", "nombre": "Frente Civico de Aguasclaras", "eje": "centro",
     "temas": ["instituciones", "transparencia", "educacion", "federalismo"]},
    {"sigla": "UAP", "nombre": "Union Agraria y Productiva", "eje": "derecha",
     "temas": ["campo", "impuestos", "infraestructura", "exportaciones"]},
    {"sigla": "BST", "nombre": "Bloque Socialista del Trabajo", "eje": "izquierda",
     "temas": ["salarios", "sindicatos", "salud", "vivienda"]},
    {"sigla": "VVA", "nombre": "Vecinos y Vecinas de Aguasclaras", "eje": "local",
     "temas": ["ambiente", "transporte", "agua", "municipios"]},
]

PROVINCIAS = [
    "Ribera Alta", "Ribera Baja", "San Telmo del Sur", "Cerro Verde",
    "Puerto Nuevo", "Valle Hondo", "Los Juncales", "Costa Azul",
    "Sierra Mansa", "Tres Lagunas",
]

# 60 diputadas y diputados. Nombres verosimiles en castellano rioplatense,
# deliberadamente NO coincidentes con politicos reales.
_NOMBRES_F = ["Marcela", "Silvina", "Roxana", "Adriana", "Lorena", "Miriam", "Alicia",
              "Estela", "Carina", "Vanina", "Norma", "Griselda", "Analia", "Mabel",
              "Fabiana", "Claudia", "Rosana", "Beatriz", "Nelida", "Ivana"]
_NOMBRES_M = ["Osvaldo", "Ruben", "Hector", "Aldo", "Ariel", "Gustavo", "Fabian",
              "Marcelo", "Julio", "Ramon", "Ernesto", "Eduardo", "Anibal", "Horacio",
              "Nestor", "Alberto", "Raul", "Oscar", "Carlos", "Jorge"]
_APELLIDOS = ["Zabaleta", "Iriarte", "Quiroga", "Mendez", "Aguirre", "Bordon", "Cifuentes",
              "Duarte", "Escalante", "Ferreyra", "Godoy", "Herrera", "Ibarra", "Juarez",
              "Kaufman", "Lezcano", "Maidana", "Nuñez", "Olmedo", "Peralta", "Quintana",
              "Rivas", "Sosa", "Toledo", "Urbina", "Valdez", "Wenceslao", "Ybarra",
              "Zunino", "Almiron", "Barreto", "Cabral", "Dominguez", "Ezcurra", "Falcon",
              "Gimenez", "Hidalgo", "Insaurralde", "Jaramillo", "Krause", "Larrosa",
              "Molinari", "Navarro", "Ocampo", "Pineda", "Ramallo", "Suarez", "Tejerina",
              "Ugarte", "Villalba", "Yañez", "Zeballos", "Arrieta", "Benitez", "Correa",
              "Delgado", "Espinoza", "Figueroa", "Galvan", "Heredia"]

TEMAS = {
    "presupuesto":   ["presupuesto", "partida presupuestaria", "gasto publico", "recursos fiscales",
                      "deficit", "superavit primario", "endeudamiento", "coparticipacion",
                      "ejecucion presupuestaria", "credito publico"],
    "seguridad":     ["seguridad", "delito", "policia", "prevencion del delito", "carceles",
                      "violencia urbana", "narcotrafico", "sistema penitenciario",
                      "patrullaje", "estadistica criminal"],
    "salud":         ["salud", "hospitales", "medicamentos", "atencion primaria", "vacunas",
                      "cobertura medica", "enfermeria", "salud mental", "emergencias sanitarias",
                      "obras sociales"],
    "educacion":     ["educacion", "escuelas", "docentes", "universidad", "becas",
                      "formacion tecnica", "alfabetizacion", "infraestructura escolar",
                      "curriculum", "evaluacion educativa"],
    "trabajo":       ["trabajo", "empleo", "salarios", "convenios colectivos", "informalidad",
                      "desocupacion", "seguridad e higiene", "jubilaciones", "aportes patronales",
                      "capacitacion laboral"],
    "ambiente":      ["ambiente", "cuenca", "residuos solidos", "humedales", "agua potable",
                      "contaminacion", "areas protegidas", "cambio climatico", "saneamiento",
                      "impacto ambiental"],
    "transporte":    ["transporte", "colectivos", "ferrocarril", "rutas provinciales", "peajes",
                      "movilidad urbana", "puertos", "aeropuertos", "logistica", "subsidios al transporte"],
    "vivienda":      ["vivienda", "alquileres", "credito hipotecario", "urbanizacion", "barrios populares",
                      "deficit habitacional", "loteos", "servicios domiciliarios", "regularizacion dominial"],
    "campo":         ["produccion agropecuaria", "retenciones", "exportaciones", "cosecha", "riego",
                      "ganaderia", "agroindustria", "arrendamiento rural", "sanidad animal", "silos"],
    "instituciones": ["transparencia", "acceso a la informacion", "justicia", "control externo",
                      "federalismo", "etica publica", "designaciones", "auditoria",
                      "reforma politica", "consulta popular"],
}

# Sustantivos y verbos de relleno para ensanchar el vocabulario del corpus.
# Se usan siempre precedidos por "el", asi que la lista es de genero masculino.
# (Las femeninas viven en el vocabulario general via TEMAS y las plantillas.)
SUSTANTIVOS = ["informe", "expediente", "dictamen", "articulado", "convenio", "presupuesto",
               "relevamiento", "diagnostico", "cronograma", "financiamiento", "padron",
               "registro", "recinto", "quorum", "veto", "decreto", "municipio", "ministerio",
               "organismo", "programa", "plan", "pliego", "contrato", "aporte", "subsidio",
               "indicador", "texto", "proyecto", "regimen", "esquema", "criterio", "calculo",
               "tramite", "procedimiento", "mecanismo", "antecedente", "compromiso"]

# Femeninos, para los huecos que van tras "la" / "una".
SUSTANTIVOS_F = ["reglamentacion", "auditoria", "contrapartida", "estadistica", "comision",
                 "mocion", "enmienda", "sancion", "audiencia", "acta", "resolucion",
                 "ordenanza", "secretaria", "obra", "licitacion", "tarifa", "encuesta",
                 "muestra", "cobertura", "brecha", "trayectoria", "partida", "norma",
                 "clausula", "prorroga", "meta"]

VERBOS = ["contempla", "prevé", "establece", "deroga", "modifica", "incorpora", "suprime",
          "faculta", "obliga", "habilita", "restringe", "amplia", "posterga", "reasigna",
          "garantiza", "condiciona", "delega", "transfiere", "audita", "supervisa",
          "reconoce", "excluye", "prioriza", "financia", "regula"]

ADJETIVOS_M = ["insuficiente", "razonable", "urgente", "postergado", "prioritario", "regresivo",
               "progresivo", "transitorio", "definitivo", "parcial", "integral", "vinculante",
               "declarativo", "operativo", "acotado", "ambicioso", "prudente", "irregular",
               "sostenido", "erratico", "federal", "centralizado", "consensuado", "unilateral"]

ADJETIVOS_F = ["insuficiente", "razonable", "urgente", "postergada", "prioritaria", "regresiva",
               "progresiva", "transitoria", "definitiva", "parcial", "integral", "vinculante",
               "declarativa", "operativa", "acotada", "ambiciosa", "prudente", "irregular",
               "sostenida", "erratica", "federal", "centralizada", "consensuada", "unilateral"]

LEYES = [
    ("Ley 4412", "de Presupuesto General de la Administracion", "presupuesto", 1994),
    ("Ley 4780", "de Emergencia Habitacional", "vivienda", 1996),
    ("Ley 5103", "de Proteccion de la Cuenca del Rio Manso", "ambiente", 1999),
    ("Ley 5266", "de Financiamiento Educativo", "educacion", 2001),
    ("Ley 5540", "de Riesgos del Trabajo", "trabajo", 2004),
    ("Ley 5771", "de Seguridad Interior y Prevencion del Delito", "seguridad", 2006),
    ("Ley 6012", "de Acceso a la Informacion Publica", "instituciones", 2009),
    ("Ley 6188", "de Movilidad y Transporte Interurbano", "transporte", 2011),
    ("Ley 6340", "de Cobertura Universal de Salud", "salud", 2013),
    ("Ley 6502", "de Promocion de las Economias Regionales", "campo", 2015),
    ("Ley 6699", "de Alquileres Urbanos", "vivienda", 2017),
    ("Ley 6845", "de Gestion Integral de Residuos", "ambiente", 2019),
    ("Ley 7001", "de Emergencia Sanitaria", "salud", 2020),
    ("Ley 7150", "de Regimen Federal de Coparticipacion", "instituciones", 2022),
]

DIARIOS = [
    {"nombre": "El Litoral de Aguasclaras", "linea": "centro-derecha"},
    {"nombre": "La Voz del Puerto", "linea": "popular"},
    {"nombre": "Cronica Ribereña", "linea": "centro"},
    {"nombre": "El Debate Nacional", "linea": "centro-izquierda"},
    {"nombre": "Diario Sierra Mansa", "linea": "regional"},
]


def construir_padron(rng: random.Random) -> dict:
    """Arma el padron completo. Es LA VERDAD contra la que se contrasta el modelo."""
    diputados = []
    usados = set()
    for i in range(60):
        while True:
            fem = rng.random() < 0.42
            nom = rng.choice(_NOMBRES_F if fem else _NOMBRES_M)
            ape = rng.choice(_APELLIDOS)
            if (nom, ape) not in usados:
                usados.add((nom, ape))
                break
        p = PARTIDOS[i % len(PARTIDOS)]
        diputados.append({
            "id": i + 1,
            "nombre": f"{nom} {ape}",
            "tratamiento": "diputada" if fem else "diputado",
            "partido": p["sigla"],
            "provincia": rng.choice(PROVINCIAS),
            "desde": rng.choice([2015, 2017, 2019, 2021, 2023]),
        })
    return {
        "_ADVERTENCIA": "PAIS Y PERSONAS FICTICIOS. Corpus sintetico del curso "
                        "'Deep Learning para Cientistas Sociales'. Ninguna de estas "
                        "personas, partidos o leyes existe. No usar para investigacion "
                        "sustantiva.",
        "semilla": SEMILLA,
        "pais": "Republica de Aguasclaras",
        "partidos": PARTIDOS,
        "provincias": PROVINCIAS,
        "diputados": diputados,
        "leyes": [{"numero": n, "titulo": t, "tema": tema, "anio": a}
                  for n, t, tema, a in LEYES],
        "diarios": DIARIOS,
    }


# ----------------------------------------------------------------------
# PLANTILLAS DE ORATORIA
# Variedad deliberada de registros: tecnico, epico, de chicana, de cita.
# ----------------------------------------------------------------------

APERTURAS = [
    "Señor presidente, señores diputados:",
    "Gracias, señor presidente.",
    "Señora presidenta, pido la palabra.",
    "Muchas gracias, señor presidente. Voy a ser breve.",
    "Señor presidente, y por su intermedio a los señores diputados:",
    "Gracias, presidente. Antes de entrar en el fondo de la cuestion,",
]

CIERRES = [
    "Nada mas, señor presidente.",
    "Es cuanto tengo para decir. Muchas gracias.",
    "Por eso vamos a acompañar el proyecto. Gracias, presidente.",
    "Por las razones expuestas, adelanto mi voto negativo. Gracias.",
    "Dejo constancia de mi posicion en el acta. Nada mas.",
    "Solicito la insercion del resto de mi exposicion en el Diario de Sesiones.",
]

CONECTORES = [
    "En primer lugar,", "En segundo termino,", "Ahora bien,", "Sin embargo,",
    "Por otro lado,", "Quiero ser claro:", "Vale la pena recordar que",
    "Permitanme insistir:", "Y aca esta el punto:", "Dicho esto,",
    "No es un detalle menor:", "Voy a dar un ejemplo concreto:",
]

# Marcos ideologicos: la misma noticia contada desde dos lados.
MARCOS = {
    "izquierda": [
        "la desigualdad sigue siendo el problema de fondo de este pais",
        "sin inversion publica no hay derecho que se realice",
        "los que menos tienen no pueden seguir esperando",
        "el mercado por si solo nunca resolvio esto",
        "hay que discutir quien paga el costo del ajuste",
    ],
    "derecha": [
        "sin equilibrio fiscal no hay politica social que se sostenga",
        "el sector privado es el que genera el empleo genuino",
        "la presion impositiva ahoga a los que producen",
        "hace falta previsibilidad para que llegue la inversion",
        "el gasto sin control termina siempre en mas inflacion",
    ],
    "centro": [
        "necesitamos acuerdos que duren mas que un periodo legislativo",
        "las politicas de Estado no se construyen por decreto",
        "hay que mirar la evidencia antes que la consigna",
        "la calidad institucional no es un tema de elites",
        "podemos discutir los medios sin discutir el objetivo",
    ],
}
MARCOS["centro-izquierda"] = MARCOS["izquierda"] + MARCOS["centro"]
MARCOS["centro-derecha"] = MARCOS["derecha"] + MARCOS["centro"]
MARCOS["local"] = MARCOS["centro"] + [
    "los vecinos de mi provincia vienen reclamando esto hace años",
    "desde el interior se ve distinto que desde la capital",
]

CUERPOS = [
    "El proyecto que estamos tratando modifica el regimen vigente en materia de {tema}. "
    "{conector} conviene recordar que la {ley_num} {ley_tit} fue sancionada en {ley_anio} "
    "y desde entonces la realidad de {provincia} cambio de manera sustantiva.",

    "Segun los datos que nos acerco la Direccion de Estadistica, el indicador de {tema} "
    "en {provincia} paso de {n1} por ciento en {a1} a {n2} por ciento en {a2}. "
    "{conector} eso no se explica solo por el ciclo economico.",

    "Quiero referirme puntualmente al articulo {art}. Tal como esta redactado, deja "
    "librada a la reglamentacion una cuestion central: quien controla y con que recursos. "
    "{conector} sin control, la mejor ley del mundo es una declaracion de buenas intenciones.",

    "En mi provincia, {provincia}, la situacion de {tema} es critica. He recorrido los "
    "municipios y escuchado a los vecinos. {conector} {marco}.",

    "El bloque del {partido_nombre} viene sosteniendo una posicion conocida sobre {tema}. "
    "{conector} {marco}. No es una posicion nueva ni improvisada.",

    "Se ha dicho en este recinto que el proyecto resuelve el problema de {tema}. "
    "Yo no comparto ese diagnostico. {conector} {marco}, y este texto no lo contempla.",

    "Voy a citar textualmente el dictamen de mayoria: \"la presente iniciativa procura "
    "ordenar el regimen de {tema_nombre} garantizando el acceso equitativo\". "
    "{conector} entre lo que dice el dictamen y lo que dice el articulado hay una distancia.",

    "La comision de {tema_nombre} trabajo durante {meses} meses. Recibimos a {n_expo} expositores, "
    "entre ellos representantes de los municipios de {provincia}. "
    "{conector} el dictamen recoge buena parte de esas observaciones.",

    "Quiero hacer una aclaracion, porque se dijo lo contrario y no es asi. "
    "El aumento de partidas para {tema} no fue del {n1} por ciento sino del {n2} por ciento. "
    "{conector} las cifras estan publicadas y cualquiera puede verificarlas.",

    "Este debate no es tecnico, es politico, y esta bien que lo sea. "
    "{conector} {marco}. Lo que no corresponde es presentar una decision politica "
    "como si fuera una necesidad tecnica.",

    "Solicito que se incorpore al expediente la nota que remitieron los intendentes de "
    "{provincia} respecto de {tema}. {conector} es la voz de quienes van a tener que "
    "aplicar esta norma.",

    "Voy a votar en contra, y quiero explicar por que. No estoy en contra del objetivo. "
    "Estoy en contra del instrumento. {conector} {marco}.",

    "Cuando discutimos la {ley_num} {ley_tit}, en {ley_anio}, varios de los que hoy estan "
    "sentados aca sostenian exactamente lo contrario. {conector} el Diario de Sesiones "
    "es un documento publico.",

    "Los numeros del ultimo informe son claros: {n1} por ciento de los hogares de {provincia} "
    "no accede a un servicio adecuado de {tema}. {conector} {marco}.",
]

# Plantillas adicionales: registros distintos (tecnico, territorial, de chicana,
# de cita, de dato). La variedad de registro es lo que hace que un mini-GPT
# entrenado aca produzca algo que se lee como parlamento y no como un loop.
CUERPOS += [
    "El articulo {art} {verbo} un mecanismo que en la practica va a ser {adjetivo_m}. "
    "Lo digo con conocimiento: el {sustantivo} que elaboro la comision lo advierte "
    "en la pagina {art}. {conector} nadie puede decir despues que no estaba avisado.",

    "Vengo de recorrer {provincia}. Hable con el intendente, con los gremios y con "
    "los usuarios. Todos coinciden en algo: la respuesta del Estado en materia de "
    "{tema} llega tarde y llega incompleta. {conector} {marco}.",

    "Se nos pide votar un {sustantivo} que no tuvo tratamiento en comision. "
    "Yo entiendo la urgencia, pero la urgencia no puede ser la regla. "
    "{conector} este cuerpo ya cometio ese error con la {ley_num}.",

    "Hay una diferencia entre lo que este proyecto {verbo} y lo que se anuncio "
    "en conferencia de prensa. El texto {verbo} una obligacion {adjetivo_f}; "
    "el anuncio hablaba de otra cosa. {conector} las leyes se leen, no se escuchan.",

    "Quiero reconocer el trabajo de la diputada preopinante. Discrepamos en el "
    "diagnostico sobre {tema}, pero no en la honestidad del planteo. "
    "{conector} {marco}.",

    "El {sustantivo} de {a1} mostraba una cobertura de {n1} por ciento en {provincia}. "
    "El de {a2} muestra {n2} por ciento. Alguien tiene que explicar esa diferencia, "
    "porque el presupuesto asignado a {tema} no bajo. {conector} o los datos estan mal, "
    "o la ejecucion estuvo mal.",

    "Voy a hacer una propuesta concreta, presidente. Que se incorpore un articulo "
    "que {verbo} la publicacion trimestral de la ejecucion en materia de {tema}, "
    "abierta y en formato reutilizable. {conector} sin datos publicos no hay control.",

    "Escuche decir que quienes objetamos este texto estamos en contra del interes "
    "general. Rechazo esa forma de discutir. {conector} {marco}, y eso tambien es "
    "defender el interes general.",

    "El bloque del {partido_nombre} pidio hace {meses} meses un informe sobre {tema} "
    "y todavia no llego. {conector} el articulo 100 de la Constitucion no es una "
    "sugerencia: es una obligacion del Poder Ejecutivo.",

    "Este proyecto tiene una virtud y un defecto. La virtud es que {verbo} un problema "
    "real. El defecto es que la solucion es {adjetivo_f} para la escala del problema. "
    "{conector} vamos a acompañar en general y a proponer cambios en particular.",

    "Me voy a permitir una digresion, presidente. Cuando uno mira la serie de "
    "{tema} desde {a1} hasta {a2}, lo que ve no es una linea: son ciclos. "
    "{conector} legislar para el pico de un ciclo es legislar mal.",

    "Los intendentes de {provincia} nos mandaron una nota. Dice, textual: "
    "\"la transferencia de la competencia sin la transferencia de los recursos "
    "convierte una politica publica en un problema municipal\". "
    "{conector} esa frase resume el debate de hoy.",

    "Se ha invocado la experiencia comparada. Bien: en la region hay tres modelos "
    "distintos de {tema}, y los tres tienen resultados dispares. "
    "{conector} copiar sin adaptar no es modernizar.",

    "Termino, presidente. Voy a votar afirmativamente porque entiendo que el "
    "{sustantivo} mejoro respecto del texto original. {conector} dejo constancia "
    "de que el financiamiento sigue siendo {adjetivo_m}.",

    "No voy a repetir los argumentos del miembro informante. Quiero agregar un dato "
    "que no se menciono: {n1} por ciento de los municipios de {provincia} no tiene "
    "personal tecnico para aplicar esta norma. {conector} sin capacidad estatal "
    "no hay implementacion.",
]

INTERRUPCIONES = [
    "—No es asi, señor diputado.",
    "—Le pido que no me interrumpa, presidente.",
    "—Que se lea el articulo.",
    "—Eso no figura en el dictamen.",
    "—Solicito una interrupcion.",
    "—Tiene razon el diputado preopinante.",
]

PRESIDENCIA = [
    "Tiene la palabra {el_la} {trat} por {provincia}, {nombre}.",
    "Tiene la palabra {el_la} {senor} {trat} {nombre}.",
    "Se va a votar en general. Los que esten por la afirmativa, sirvanse indicarlo.",
    "Resulta afirmativa. Queda aprobado en general.",
    "Continua la sesion. Tiene la palabra {el_la} {trat} {nombre}, del bloque {partido}.",
    "Se cierra la lista de oradores.",
    "Por Secretaria se dara lectura al dictamen.",
]


def _num(rng, lo=1, hi=60):
    return f"{rng.randint(lo, hi)}"


def _pct(rng):
    return f"{rng.randint(3, 88)},{rng.randint(0, 9)}"


def generar_intervencion(rng, dip, padron) -> str:
    partido = next(p for p in PARTIDOS if p["sigla"] == dip["partido"])
    marcos = MARCOS[partido["eje"]]
    tema = rng.choice(list(TEMAS))
    ley = rng.choice(LEYES)
    partes = [rng.choice(APERTURAS)]
    n_parr = rng.randint(2, 5)
    # sin reposicion: una intervencion no repite la misma plantilla dos veces
    plantillas = rng.sample(CUERPOS, min(n_parr, len(CUERPOS)))
    for plantilla in plantillas:
        partes.append(plantilla.format(
            tema=rng.choice(TEMAS[tema]),
            tema_nombre=tema,
            conector=rng.choice(CONECTORES),
            marco=rng.choice(marcos),
            provincia=dip["provincia"] if rng.random() < .6 else rng.choice(PROVINCIAS),
            partido_nombre=partido["nombre"],
            ley_num=ley[0], ley_tit=ley[1], ley_anio=ley[3],
            art=_num(rng, 1, 42),
            n1=_pct(rng), n2=_pct(rng),
            a1=rng.randint(2005, 2015), a2=rng.randint(2016, 2024),
            meses=rng.randint(2, 11), n_expo=rng.randint(6, 40),
            sustantivo=rng.choice(SUSTANTIVOS),
            sustantivo_f=rng.choice(SUSTANTIVOS_F),
            verbo=rng.choice(VERBOS),
            adjetivo_m=rng.choice(ADJETIVOS_M),
            adjetivo_f=rng.choice(ADJETIVOS_F),
        ))
        if rng.random() < 0.12:
            partes.append(rng.choice(INTERRUPCIONES))
    partes.append(rng.choice(CIERRES))
    return " ".join(partes)


def generar_sesion(rng, padron, nro, anio) -> str:
    ley = rng.choice(LEYES)
    out = [
        f"=== DIARIO DE SESIONES — CAMARA DE DIPUTADOS DE AGUASCLARAS ===",
        f"Sesion ordinaria numero {nro} — {rng.randint(1,28)} de "
        f"{rng.choice(['marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre'])} de {anio}",
        f"Orden del dia: tratamiento del proyecto {ley[0]} {ley[1]}.",
        "",
    ]
    oradores = rng.sample(padron["diputados"], rng.randint(4, 9))
    for dip in oradores:
        fem = dip["tratamiento"] == "diputada"
        out.append(rng.choice(PRESIDENCIA).format(
            trat=dip["tratamiento"], provincia=dip["provincia"],
            nombre=dip["nombre"], partido=dip["partido"],
            el_la="la" if fem else "el",
            senor="señora" if fem else "señor"))
        out.append(f"{dip['tratamiento'].capitalize()} {dip['nombre']} ({dip['partido']} — {dip['provincia']}).")
        out.append(generar_intervencion(rng, dip, padron))
        out.append("")
    out.append("Se levanta la sesion.")
    out.append("")
    return "\n".join(out)


# ----------------------------------------------------------------------
# PRENSA
# ----------------------------------------------------------------------
TITULARES = [
    "{diario}: Diputados aprobo en general el proyecto de {tema}",
    "{diario}: Fuerte cruce en el recinto por la {ley_num}",
    "{diario}: El bloque {sigla} anticipo que no acompaña la reforma de {tema}",
    "{diario}: Vecinos de {provincia} se movilizaron frente a la sede del ministerio",
    "{diario}: Corte de ruta en {provincia} por reclamos de {tema}",
    "{diario}: {nombre} pidio la insercion de su discurso en el Diario de Sesiones",
    "{diario}: La comision de {tema} recibio a intendentes de {provincia}",
    "{diario}: Cayo la actividad en {provincia} segun el ultimo informe oficial",
    "{diario}: Sin acuerdo por el presupuesto, la sesion pasa a cuarto intermedio",
    "{diario}: Docentes de {provincia} anunciaron un paro de 48 horas",
    "{diario}: El oficialismo reunio los votos para sancionar la {ley_num}",
    "{diario}: Denuncian demoras en la obra de agua potable de {provincia}",
]


def generar_prensa(rng, padron, n=1400):
    filas = []
    for i in range(n):
        d = rng.choice(DIARIOS)
        dip = rng.choice(padron["diputados"])
        ley = rng.choice(LEYES)
        tema = rng.choice(list(TEMAS))
        t = rng.choice(TITULARES).format(
            diario="", tema=tema, ley_num=ley[0], sigla=rch(rng),
            provincia=rng.choice(PROVINCIAS), nombre=dip["nombre"]).strip().lstrip(":").strip()
        protesta = any(k in t.lower() for k in
                       ["moviliz", "corte de ruta", "paro", "reclam", "denuncian"])
        filas.append({
            "id": f"AC{i:05d}",
            "anio": rng.randint(2015, 2024),
            "diario": d["nombre"],
            "linea_editorial": d["linea"],
            "titular": t,
            "tema": tema,
            "menciona_protesta": int(protesta),
        })
    return filas


def rch(rng):
    return rng.choice([p["sigla"] for p in PARTIDOS])


# ----------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--salida", default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                     "muestras", "aguasclaras"))
    ap.add_argument("--mb", type=float, default=1.1, help="megabytes de texto de sesiones")
    ap.add_argument("--semilla", type=int, default=SEMILLA)
    args = ap.parse_args()

    rng = random.Random(args.semilla)
    os.makedirs(args.salida, exist_ok=True)
    padron = construir_padron(rng)

    with open(os.path.join(args.salida, "verdad.json"), "w", encoding="utf-8") as fh:
        json.dump(padron, fh, ensure_ascii=False, indent=1)

    objetivo = int(args.mb * 1_000_000)
    partes, total, nro = [], 0, 1
    anio = 2015
    while total < objetivo:
        s = generar_sesion(rng, padron, nro, anio)
        partes.append(s)
        total += len(s.encode("utf-8"))
        nro += 1
        if nro % 12 == 0:
            anio = min(2024, anio + 1)
    corpus = "\n".join(partes)

    cab = ("# CORPUS SINTETICO — Republica de Aguasclaras (pais ficticio)\n"
           "# Generado por datos/generar_aguasclaras.py con semilla %d.\n"
           "# NINGUNA de estas personas, partidos o leyes existe.\n"
           "# Uso didactico unicamente. Ver datos/README.md.\n\n" % args.semilla)
    with open(os.path.join(args.salida, "debates.txt"), "w", encoding="utf-8") as fh:
        fh.write(cab + corpus)

    import csv
    prensa = generar_prensa(rng, padron)
    with open(os.path.join(args.salida, "prensa.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(prensa[0]))
        w.writeheader()
        w.writerows(prensa)

    print(f"[aguasclaras] verdad.json  : {len(padron['diputados'])} diputados, "
          f"{len(PARTIDOS)} partidos, {len(LEYES)} leyes")
    print(f"[aguasclaras] debates.txt  : {len(corpus):,} caracteres "
          f"({len(corpus.encode('utf-8'))/1e6:.2f} MB), {nro-1} sesiones")
    print(f"[aguasclaras] prensa.csv   : {len(prensa)} titulares, "
          f"{sum(f['menciona_protesta'] for f in prensa)} con protesta "
          f"({100*sum(f['menciona_protesta'] for f in prensa)/len(prensa):.1f}%)")
    print(f"[aguasclaras] salida       : {args.salida}")


if __name__ == "__main__":
    main()
