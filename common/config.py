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
TEMPERATURE = 0.3

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

# RMO: MAXIMO NUMERO DE TURNOS (LO QUE RECUERDA EL LLM) QUE SOPORTA 
# EL SISTEMA
TURNOS = 4

#############################
# PARAMETROS PARA DEMOS     # 
#############################

DIA_ONBOARDING = 1