from pathlib import Path

####################################
# PARAMETROS DEL SISTEMA GENERALES # 
####################################

# RMO: CONFIGURACIÓN DE RUTAS PARA LAS DEMOS
DATA_DIR = Path(__file__).parent.parent / "data"

EMPLEADOS_DEMO_PATH = DATA_DIR / "empleados_demo.json"
EMPRESA_PATH = DATA_DIR / "empresa.json"
FAQ_PATH = DATA_DIR / "faq_onboarding.json"
DOCS_PATH = DATA_DIR / "onboarding_docs.json"

# RMO: Se indica que proveedor de LLM se va a utilizar.git 
LLM_PROVEEDOR = "GEMINI"
# RMO: Modelo principal del proyecto
#MODEL = "gemini-3-flash-preview"
MODEL ="gemini-3.1-flash-lite-preview"
# RMO: Modelo secundario para hacer las pruebas de benchmark
# LLM_MODEL_B = "gemini-3-flash-preview"
# RMO: Temperartura de los modelos.
TEMPERATURE = 0.2
MSG_LENGTH_LIMIT = 400

# RMO: PERFILES SOPORTADOS POR LA DEMO
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



# RMO: MAXIMO NUMERO DE MENSAJES (LO QUE RECUERDA EL LLM) QUE SOPORTA EL SISTEMA
# 4 TURNOS SON 8 MENSAJES (4 DEL USUARIO Y 4 DEL ASISTENTE)
MSG_LIMIT_CONTEXT = 8

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
    r"ignora(?:r)? (?:las )?(?:instrucciones|reglas|prioridades|indicaciones|todo)",
    r"olvida(?:r)? (?:que|lo)",
    r"ahora eres",
    r"revela(?:r)?",
    r"contrase(?:\u00f1|n)a",
    r"token",
    r"api key",
    r"secreto",
]
    
    