// Generado por medir-clase10.py — NO editar a mano.
// Todos estos numeros salen de correr el codigo sobre los datos reales del curso.
window.DATOS10 = {
 "modelo": {
  "tarea": "¿la nota de prensa es sobre politica?",
  "corpus": "Spanish Fake News Corpus 2.0 (prensa real, CC BY 4.0)",
  "n_total": 1471,
  "n_train": 1103,
  "n_test": 368,
  "vocabulario": 6534,
  "prevalencia": 0.2808,
  "piso": 0.7192,
  "metricas": {
   "vp": 66,
   "fp": 25,
   "vn": 240,
   "fn": 37,
   "accuracy": 0.8315,
   "precision": 0.7253,
   "recall": 0.6408,
   "f1": 0.6804,
   "prevalencia": 0.2799
  },
  "top_positivos": [
   {
    "termino": "presidencial",
    "peso": 1.0981
   },
   {
    "termino": "pri",
    "peso": 0.9223
   },
   {
    "termino": "caso",
    "peso": 0.8596
   },
   {
    "termino": "gobierno",
    "peso": 0.8386
   },
   {
    "termino": "lópez",
    "peso": 0.739
   },
   {
    "termino": "meade",
    "peso": 0.7285
   },
   {
    "termino": "políticos",
    "peso": 0.7046
   },
   {
    "termino": "presidente",
    "peso": 0.6958
   },
   {
    "termino": "federal",
    "peso": 0.686
   },
   {
    "termino": "país",
    "peso": 0.6714
   },
   {
    "termino": "amlo",
    "peso": 0.6705
   },
   {
    "termino": "va",
    "peso": 0.6698
   },
   {
    "termino": "morena",
    "peso": 0.6644
   },
   {
    "termino": "ejecutivo",
    "peso": 0.65
   },
   {
    "termino": "candidato",
    "peso": 0.6443
   },
   {
    "termino": "gobernador",
    "peso": 0.6168
   },
   {
    "termino": "expresidente",
    "peso": 0.6038
   },
   {
    "termino": "electoral",
    "peso": 0.6015
   },
   {
    "termino": "lopezobrador_",
    "peso": 0.6009
   },
   {
    "termino": "argumentos",
    "peso": 0.5984
   }
  ],
  "top_negativos": [
   {
    "termino": "estamos",
    "peso": -0.5334
   },
   {
    "termino": "victoria",
    "peso": -0.5356
   },
   {
    "termino": "propuesta",
    "peso": -0.538
   },
   {
    "termino": "usuarios",
    "peso": -0.5392
   },
   {
    "termino": "mexicano",
    "peso": -0.5685
   },
   {
    "termino": "19",
    "peso": -0.5703
   },
   {
    "termino": "son",
    "peso": -0.5815
   },
   {
    "termino": "fuera",
    "peso": -0.598
   },
   {
    "termino": "vida",
    "peso": -0.6259
   },
   {
    "termino": "sociales",
    "peso": -0.6418
   },
   {
    "termino": "hacer",
    "peso": -0.6708
   },
   {
    "termino": "coronavirus",
    "peso": -0.6756
   }
  ]
 },
 "ruido_de_particion": {
  "n_particiones": 25,
  "media": 0.6801,
  "sd": 0.0262,
  "minimo": 0.6263,
  "maximo": 0.7333,
  "rango": 0.1071,
  "valores": [
   0.6878,
   0.6798,
   0.69,
   0.6263,
   0.7087,
   0.6559,
   0.7333,
   0.6766,
   0.6369,
   0.6703,
   0.6965,
   0.6599,
   0.6596,
   0.6601,
   0.709,
   0.6869,
   0.7129,
   0.6633,
   0.697,
   0.6734,
   0.7083,
   0.6597,
   0.7005,
   0.7071,
   0.6425
  ]
 },
 "ablacion": [
  {
   "quitado": "nada (el modelo original)",
   "n_quitados": 0,
   "metricas": {
    "vp": 66,
    "fp": 25,
    "vn": 240,
    "fn": 37,
    "accuracy": 0.8315,
    "precision": 0.7253,
    "recall": 0.6408,
    "f1": 0.6804,
    "prevalencia": 0.2799
   },
   "f1": 0.6804
  },
  {
   "quitado": "el termino n.o 1",
   "n_quitados": 1,
   "metricas": {
    "vp": 67,
    "fp": 25,
    "vn": 240,
    "fn": 36,
    "accuracy": 0.8342,
    "precision": 0.7283,
    "recall": 0.6505,
    "f1": 0.6872,
    "prevalencia": 0.2799
   },
   "f1": 0.6872
  },
  {
   "quitado": "los 5 primeros",
   "n_quitados": 5,
   "metricas": {
    "vp": 71,
    "fp": 25,
    "vn": 240,
    "fn": 32,
    "accuracy": 0.8451,
    "precision": 0.7396,
    "recall": 0.6893,
    "f1": 0.7136,
    "prevalencia": 0.2799
   },
   "f1": 0.7136
  },
  {
   "quitado": "los 20 primeros",
   "n_quitados": 20,
   "metricas": {
    "vp": 68,
    "fp": 28,
    "vn": 237,
    "fn": 35,
    "accuracy": 0.8288,
    "precision": 0.7083,
    "recall": 0.6602,
    "f1": 0.6834,
    "prevalencia": 0.2799
   },
   "f1": 0.6834
  },
  {
   "quitado": "los 18 nombres propios",
   "n_quitados": 18,
   "metricas": {
    "vp": 65,
    "fp": 26,
    "vn": 239,
    "fn": 38,
    "accuracy": 0.8261,
    "precision": 0.7143,
    "recall": 0.6311,
    "f1": 0.6701,
    "prevalencia": 0.2799
   },
   "f1": 0.6701
  }
 ],
 "ablacion_vs_ruido": {
  "movimiento_maximo": 0.0332,
  "rango_del_ruido": 0.1071
 },
 "placebo": {
  "casarosada": {
   "n": 600,
   "proporcion_marcada": 0.2083,
   "esperado": 1.0,
   "que_es": "fragmentos de discursos presidenciales argentinos 2015-2024",
   "recall_alli": 0.2083,
   "recall_en_su_test": 0.6408
  },
  "barajado": {
   "proporcion_predicciones_identicas": 1.0,
   "positivos_original": 0.2473,
   "positivos_barajado": 0.2473
  },
  "aguasclaras": {
   "n": 1400,
   "proporcion_marcada": 0.1857,
   "proporcion_realmente_politica": 0.0929
  }
 },
 "pares_minimos": [
  {
   "tipo": "negacion",
   "a": "El gobierno aprobó la ley de presupuesto",
   "b": "El gobierno no aprobó la ley de presupuesto",
   "score_a": 0.8003,
   "score_b": 0.7586,
   "delta": -0.0417
  },
  {
   "tipo": "negacion",
   "a": "El senado rechazó el proyecto",
   "b": "El senado no rechazó el proyecto",
   "score_a": 0.6146,
   "score_b": 0.5557,
   "delta": -0.0589
  },
  {
   "tipo": "cambio de pais",
   "a": "AMLO anunció una reforma al sistema de salud",
   "b": "El presidente de Uruguay anunció una reforma al sistema de salud",
   "score_a": 0.5437,
   "score_b": 0.5785,
   "delta": 0.0348
  },
  {
   "tipo": "cambio de pais",
   "a": "Morena ganó las elecciones en el estado",
   "b": "El Frente Amplio ganó las elecciones en el departamento",
   "score_a": 0.7725,
   "score_b": 0.5165,
   "delta": -0.2561
  },
  {
   "tipo": "cambio de agente",
   "a": "El diputado presentó un proyecto sobre vivienda",
   "b": "El futbolista presentó su nuevo club",
   "score_a": 0.5417,
   "score_b": 0.4845,
   "delta": -0.0572
  },
  {
   "tipo": "cambio de agente",
   "a": "El ministro visitó el hospital de la ciudad",
   "b": "El cantante visitó el hospital de la ciudad",
   "score_a": 0.5458,
   "score_b": 0.3916,
   "delta": -0.1542
  },
  {
   "tipo": "mismo tema, otras palabras",
   "a": "El congreso debate la reforma electoral",
   "b": "La cámara discute los cambios al sistema de votación",
   "score_a": 0.7128,
   "score_b": 0.3174,
   "delta": -0.3954
  },
  {
   "tipo": "cambio de epoca",
   "a": "El presidente presentó su plan de gobierno",
   "b": "El primer mandatario expuso su programa de gestión",
   "score_a": 0.8531,
   "score_b": 0.6697,
   "delta": -0.1834
  }
 ],
 "sesgo": {
  "plantilla": "{} reclamó frente a la sede del ministerio",
  "filas": [
   {
    "dimension": "genero",
    "sujeto": "las médicas",
    "score": 0.3462,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "origen",
    "sujeto": "los migrantes",
    "score": 0.3439,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "genero",
    "sujeto": "las trabajadoras",
    "score": 0.3069,
    "fuera_de_vocabulario": [
     "trabajadoras"
    ]
   },
   {
    "dimension": "genero",
    "sujeto": "las empresarias",
    "score": 0.3069,
    "fuera_de_vocabulario": [
     "empresarias"
    ]
   },
   {
    "dimension": "ocupacion",
    "sujeto": "los estudiantes",
    "score": 0.2816,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "genero",
    "sujeto": "los médicos",
    "score": 0.2752,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "ocupacion",
    "sujeto": "los taxistas",
    "score": 0.2721,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "ocupacion",
    "sujeto": "los docentes",
    "score": 0.2654,
    "fuera_de_vocabulario": [
     "docentes"
    ]
   },
   {
    "dimension": "ocupacion",
    "sujeto": "los enfermeros",
    "score": 0.2654,
    "fuera_de_vocabulario": [
     "enfermeros"
    ]
   },
   {
    "dimension": "origen",
    "sujeto": "los campesinos",
    "score": 0.2654,
    "fuera_de_vocabulario": [
     "campesinos"
    ]
   },
   {
    "dimension": "origen",
    "sujeto": "los indígenas",
    "score": 0.2654,
    "fuera_de_vocabulario": [
     "indígenas"
    ]
   },
   {
    "dimension": "genero",
    "sujeto": "los trabajadores",
    "score": 0.2623,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "genero",
    "sujeto": "los empresarios",
    "score": 0.2574,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "origen",
    "sujeto": "los vecinos",
    "score": 0.2482,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "origen",
    "sujeto": "los venezolanos",
    "score": 0.2339,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "ocupacion",
    "sujeto": "los policías",
    "score": 0.231,
    "fuera_de_vocabulario": []
   },
   {
    "dimension": "origen",
    "sujeto": "los mexicanos",
    "score": 0.1834,
    "fuera_de_vocabulario": []
   }
  ],
  "diferencia_maxima": 0.1628,
  "score_max": 0.3462,
  "score_min": 0.1834,
  "pares_genero": [
   {
    "masculino": "los trabajadores",
    "femenino": "las trabajadoras",
    "score_m": 0.2623,
    "score_f": 0.3069,
    "delta": 0.0446,
    "sustantivo_en_vocabulario": 1
   },
   {
    "masculino": "los médicos",
    "femenino": "las médicas",
    "score_m": 0.2752,
    "score_f": 0.3462,
    "delta": 0.071,
    "sustantivo_en_vocabulario": 1
   },
   {
    "masculino": "los empresarios",
    "femenino": "las empresarias",
    "score_m": 0.2574,
    "score_f": 0.3069,
    "delta": 0.0495,
    "sustantivo_en_vocabulario": 1
   },
   {
    "masculino": "los docentes",
    "femenino": "las docentes",
    "score_m": 0.2654,
    "score_f": 0.3069,
    "delta": 0.0415,
    "sustantivo_en_vocabulario": 0
   },
   {
    "masculino": "los enfermeros",
    "femenino": "las enfermeras",
    "score_m": 0.2654,
    "score_f": 0.3069,
    "delta": 0.0415,
    "sustantivo_en_vocabulario": 0
   },
   {
    "masculino": "los vecinos",
    "femenino": "las vecinas",
    "score_m": 0.2482,
    "score_f": 0.3069,
    "delta": 0.0587,
    "sustantivo_en_vocabulario": 1
   },
   {
    "masculino": "los estudiantes",
    "femenino": "las estudiantes",
    "score_m": 0.2816,
    "score_f": 0.3246,
    "delta": 0.0429,
    "sustantivo_en_vocabulario": 1
   },
   {
    "masculino": "los jubilados",
    "femenino": "las jubiladas",
    "score_m": 0.2654,
    "score_f": 0.3069,
    "delta": 0.0415,
    "sustantivo_en_vocabulario": 0
   },
   {
    "masculino": "los abogados",
    "femenino": "las abogadas",
    "score_m": 0.2654,
    "score_f": 0.3069,
    "delta": 0.0415,
    "sustantivo_en_vocabulario": 0
   },
   {
    "masculino": "los periodistas",
    "femenino": "las periodistas",
    "score_m": 0.2941,
    "score_f": 0.3381,
    "delta": 0.044,
    "sustantivo_en_vocabulario": 1
   }
  ],
  "peso_los": -0.339,
  "peso_las": -0.1355,
  "permutacion": {
   "diferencia_media": 0.0477,
   "p_valor": 0.0024,
   "n_pares": 10,
   "n_permutaciones": 20000
  }
 },
 "confusor_temporal": {
  "n": 110,
  "n_train": 77,
  "n_test": 33,
  "metricas_orador": {
   "vp": 14,
   "fp": 3,
   "vn": 13,
   "fn": 3,
   "accuracy": 0.8182,
   "precision": 0.8235,
   "recall": 0.8235,
   "f1": 0.8235,
   "prevalencia": 0.5152
  },
  "metricas_periodo": {
   "vp": 14,
   "fp": 3,
   "vn": 13,
   "fn": 3,
   "accuracy": 0.8182,
   "precision": 0.8235,
   "recall": 0.8235,
   "f1": 0.8235,
   "prevalencia": 0.5152
  },
  "coincidencia_etiquetas": 1.0,
  "anios_macri": [
   2015,
   2016,
   2017,
   2018,
   2019
  ],
  "anios_fernandez": [
   2020,
   2021,
   2022,
   2023
  ],
  "anios_solapados": [],
  "n_solapados": 0
 },
 "cobertura_parcial": {
  "aclaracion": "Corpus CONSTRUIDOS a mano para mostrar el mecanismo. No son datos.",
  "tono_foro_a": 20.8333,
  "tono_foro_b": 20.8333,
  "interlocutores_distintos_a": 2,
  "interlocutores_distintos_b": 1,
  "foro_a": [
   "Lo que propone el bloque de enfrente es un absurdo y una vergüenza",
   "Responder eso es un error grave, la mentira ya es un escándalo",
   "Su desastre de gestión es inaceptable, y decirlo no es ridículo",
   "El fracaso es de ellos y sostener lo contrario es una mentira"
  ],
  "foro_b": [
   "Lo que hizo la empresa es un absurdo y una vergüenza",
   "El error grave fue de la empresa, y su mentira es un escándalo",
   "Su desastre de gestión es inaceptable, coincido, y no es ridículo",
   "El fracaso es de la empresa y sostener lo contrario es una mentira"
  ],
  "lexico": [
   "absurdo",
   "vergüenza",
   "mentira",
   "fracaso",
   "desastre",
   "escandaloso",
   "inaceptable",
   "ridículo",
   "grave",
   "error"
  ]
 },
 "etiqueta_circular": {
  "corpus": "prensa de Aguasclaras — SINTETICO, pais ficticio",
  "n": 1400,
  "prevalencia": 0.3471,
  "original": {
   "vp": 121,
   "fp": 0,
   "vn": 229,
   "fn": 0,
   "accuracy": 1.0,
   "precision": 1.0,
   "recall": 1.0,
   "f1": 1.0,
   "prevalencia": 0.3457
  },
  "sin_protesta": {
   "vp": 121,
   "fp": 0,
   "vn": 229,
   "fn": 0,
   "accuracy": 1.0,
   "precision": 1.0,
   "recall": 1.0,
   "f1": 1.0,
   "prevalencia": 0.3457
  },
  "sin_cinco_palabras": {
   "vp": 121,
   "fp": 0,
   "vn": 229,
   "fn": 0,
   "accuracy": 1.0,
   "precision": 1.0,
   "recall": 1.0,
   "f1": 1.0,
   "prevalencia": 0.3457
  }
 },
 "fuga_por_fuente": {
  "tarea": "¿la nota es falsa?",
  "al_azar": {
   "vp": 121,
   "fp": 46,
   "vn": 148,
   "fn": 53,
   "accuracy": 0.731,
   "precision": 0.7246,
   "recall": 0.6954,
   "f1": 0.7097,
   "prevalencia": 0.4728
  },
  "por_medio": {
   "vp": 118,
   "fp": 31,
   "vn": 69,
   "fn": 110,
   "accuracy": 0.5701,
   "precision": 0.7919,
   "recall": 0.5175,
   "f1": 0.626,
   "prevalencia": 0.6951
  },
  "piso_por_medio": 0.6951,
  "n_medios": 346,
  "medios_con_una_sola_clase": 332
 }
};
