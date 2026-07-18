from pathlib import Path

####################################
# PARAMETROS DEL SISTEMA GENERALES # 
####################################

# RMO: CONFIGURACIÓN DE RUTAS PARA LAS DEMOS
DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

# RMO: CONFIGURACIÓN DE FICHEROS JSON A CARGAR
EMPLEADOS_DEMO_PATH = DATA_DIR / "empleados_demo.json"
EMPRESA_PATH = DATA_DIR / "empresa.json"
FAQ_PATH = DATA_DIR / "faq_onboarding.json"
DOCS_PATH = DATA_DIR / "onboarding_docs.json"
PREGUNTAS_PATH = DATA_DIR / "preguntas.json"
CASOS_TRAMPA_PATH = DATA_DIR / "casos_trampa.json"

# RMO: Se indica que proveedor de LLM se va a utilizar 
# por si en un futuro se utiliza otro. Actualmente el sistema solo soporta
# GEMINI.
LLM_PROVEEDOR = "GEMINI"

# RMO: Modelo principal del proyecto. Se utliza este y no los recomendados
# por la limitación de la capa gratuita
#MODEL ="gemini-3-flash-preview"
MODEL ="gemini-3.1-flash-lite-preview"

#RMO: Modelo par realizar la comparativa.
MODELS_BENCHMARK = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
]

# RMO: Temperartura de los modelos.
TEMPERATURE = 0.2

#RMO: Límite de los mensaje de entrada del usuario.
MSG_LENGTH_LIMIT = 400

# RMO: PERFILES SOPORTADOS POR EL ASISTENTE
PERFILES = {
    "dev_junior": {
        "perfil": (
            "Orientado a la ingeniería."
            "Es su primero empleo."
        ),
        "tono": "Debes tener un tono didáctico, amable y compensivo.",
    },
    "comercial": {
        "perfil": (
            "Comercial orientado a ventas."
            "Poco técnico."
            "Con conocimientos en herramientas comerciales."
        ),
        "tono": "Debes tener un tono poco técnico y orientado orientado a ventas.",
    },
    "remoto_eu": {
        "perfil": (
            "Orientado a políticas cross-border."
            "Trabaja en remoto internacionalmente."
        ),
        "tono": "Debes tener un tono arientadoa políticas cross-border.",
    },
}

# RMO: IDIOMAS PERMITIDOS
IDIOMAS_PERMITIDOS = {"es": "Español", "en": "Inglés", "default": "Español"}

# RMO: TURNOS DE RECUERDO PERMITIDO POR EL ASISTENTE
TURNOS = 4
# RMO: MAXIMO NUMERO DE MENSAJES (LO QUE RECUERDA EL LLM) QUE SOPORTA EL SISTEMA
# 4 TURNOS SON 8 MENSAJES (4 DEL USUARIO Y 4 DEL ASISTENTE)
MSG_LIMIT_CONTEXT = TURNOS * 2

# RMO: LIMTE DE FAQS Y DOCUMENTOS A CARGAR.
FAQS_LIMIT = 2
DOCS_LIMIT = 4

#############################
# PARAMETROS PARA DEMOS     # 
#############################
DIA_ONBOARDING = 1

TAGS_DIA_ONBOARDING = {
    1: ["bienvenida", "primer_dia", "onboarding", "primeras_semanas"],
    2: ["onboarding", "primeras_semanas"],
    3: ["onboarding", "primeras_semanas"],
    4: ["onboarding", "primeras_semanas"],
    5: ["onboarding", "primeras_semanas"],
}

CUERPO_DIA_ONBOARDING = {
    1: ["DÍA 1", "DIA 1", "PRIMER DÍA", "PRIMER DIA"],
    2: ["DÍA 2", "DIA 2", "SEGUNDO DÍA", "SEGUNDO DIA"],
    3: ["DÍA 3", "DIA 3", "TERCER DÍA", "TERCER DIA"],
    4: ["DÍA 4", "DIA 4", "CUARTO DÍA", "CUARTO DIA"],
    5: ["DÍA 5", "DIA 5", "QUINTO DÍA", "QUINTO DIA"],
}

############################################
# PARAMETROS PARA SEGURIDAD Y ROBUSTEZ     # 
###########################################

SUSPICIOUS_INJECTION_PATTERNS = [
    r"ignora(?:r)? (?:todas |las |mis |estas |tus )*(?:instrucciones|reglas|prioridades|indicaciones|todo)",
    r"olvida(?:r)? (?:que|lo|todo)",
    r"ahora eres",
    r"revela(?:r)?",
    r"contrase(?:\u00f1|n)a",
    r"token",
    r"api key",
    r"secreto",
]
    
    