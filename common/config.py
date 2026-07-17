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

#MODEL ="gemini-3-flash-preview"
MODEL ="gemini-3.1-flash-lite-preview"
#MODEL = "gemini-2.0-flash-lite"

# gemini-2.5-flash
# gemini-2.5-pro
# gemini-2.0-flash
# gemini-2.0-flash-001
# gemini-2.0-flash-lite-001
# gemini-2.0-flash-lite
# gemini-2.5-flash-preview-tts
# gemini-2.5-pro-preview-tts
# gemma-4-26b-a4b-it
# gemma-4-31b-it
# gemini-flash-latest
# gemini-flash-lite-latest
# gemini-pro-latest
# gemini-2.5-flash-lite
# gemini-2.5-flash-image
# gemini-3-pro-preview
# gemini-3-flash-preview
# gemini-3.1-pro-preview
# gemini-3.1-pro-preview-customtools
# gemini-3.1-flash-lite-preview
# gemini-3.1-flash-lite
# gemini-3-pro-image-preview
# gemini-3-pro-image
# nano-banana-pro-preview
# gemini-3.1-flash-image-preview
# gemini-3.1-flash-image
# gemini-3.1-flash-lite-image
# gemini-3.5-flash
# gemini-omni-flash-preview
# lyria-3-clip-preview
# lyria-3-pro-preview
# gemini-3.1-flash-tts-preview
# gemini-robotics-er-1.5-preview
# gemini-robotics-er-1.6-preview
# gemini-2.5-computer-use-preview-10-2025
# antigravity-preview-05-2026
# deep-research-max-preview-04-2026
# deep-research-preview-04-2026
# deep-research-pro-preview-12-2025


# RMO: Modelo secundario para hacer las pruebas de benchmark
# LLM_MODEL_B = "gemini-3-flash-preview"
# RMO: Temperartura de los modelos.
TEMPERATURE = 0.3
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

# RMO: IDIOMAS PERMITIDOS
IDIOMAS_PERMITIDOS = {"es": "Español", "en": "Inglés", "default": "Español"}



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
    r"ignora(?:r)? (?:todas |las |mis |estas )*(?:instrucciones|reglas|prioridades|indicaciones|todo)",
    r"olvida(?:r)? (?:que|lo|todo)",
    r"ahora eres",
    r"revela(?:r)?",
    r"contrase(?:\u00f1|n)a",
    r"token",
    r"api key",
    r"secreto",
]
    
    