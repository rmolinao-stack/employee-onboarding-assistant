from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

EMPLEADOS_DEMO_PATH = DATA_DIR / "empleados_demo.json"
EMPRESA_PATH = DATA_DIR / "empresa.json"
FAQ_PATH = DATA_DIR / "faq_onboarding.json"
DOCS_PATH = DATA_DIR / "onboarding_docs.json"

# RMO: Se indica que proveedor de LLM se va a utilizar.git 
LLM_PROVEEDOR = "GEMINI"
# RMO: Modelo principal del proyecto
LLM_MODEL_A = "gemini-3-flash-preview"
# RMO: Modelo secundario para hacer las pruebas de benchmark
LLM_MODEL_B = "gemini-3-flash-preview"

# # RMO: PENDIETNE DE IMPLEMENTAR
# PERFILES = {
#     "dev_junior": {
#         "rol": (
#             "Eres un compañero de estudio amable. "
#             "Explicas con ejemplos cortos y vocabulario accesible."
#         ),
#         "nivel_explicacion": "tono didáctico",
#     },
#     "comercial": {
#         "rol": (
#             "Eres un ingeniero senior. "
#             "Vas al grano y asumes conocimientos previos de Python y APIs."
#         ),
#         "nivel_explicacion": "poco técnico y orientado a comerciales",
#     },
#     "remoto_UE": {
#         "rol": (
#             "Eres un mentor pedagógico. "
#             "Guías con pasos y preguntas reflexivas, sin abrumar."
#         ),
#         "nivel_explicacion": "intermedio",
#     },
# }