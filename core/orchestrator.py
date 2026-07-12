from model.data_model import DataModel
from common.config import TEMPERATURE, LLM_PROVEEDOR
from llm.gemini.gemini_auth import configurar_gemini_api_key
from llm.gemini.gemini_client import llamar_gemini
from core.user_history import UserHistory
from core.llm_config import LlmConfig
import core.context_delimiter as context_delimiter
import core.prompt_builder as prompt_builder
import sys


def inicializar_user_history(data_model: DataModel, id_empl: str | None = None) -> UserHistory:
    empleado: dict = None
    intentos = 0
    initial_msg1 = f"""Bienvenido a {data_model.empresa.data["producto_reto"]} de {data_model.empresa.data["nombre"]}. 
Mi objetivo es resolver todas las preguntas que tengas referente al proceso de Onboardig en {data_model.empresa.data["nombre"]}."""

    while not empleado:
        if not id_empl:
            id_empl = input(f"""Para continuar necesito que me indiques el identificador de empleado valido que te debería haber proporcionado RRHH: """)
        empleado = obtener_datos_usuario(data_model, id_empl)
        if not empleado: 
            print("El empleado indicado no es valido.")
            id_empl = None
            intentos += 1
        if intentos == 3:
            print("Has indicado 3 códigos de empleados invalidos. El chat va a finalizar.")
            sys.exit()
    
    initial_msg2 = f"Te has identificado como {empleado["nombre"]}, ¿en que puedo ayudarte?"
    print(initial_msg1 + "\n" + initial_msg2)

    return UserHistory(empleado, [{"role": "assistant", "text": initial_msg1 + "\n" + initial_msg2}])

def obtener_datos_usuario(data_model: DataModel, id_empl: str) -> dict:
    return data_model.empleados.getEmpleado(id_empl)

def inicializar_asistente_llm() -> LlmConfig:
    return LlmConfig()

def seleccionar_faqs(data_model: DataModel, consulta: str, max_entradas: int = 2) -> list[dict]:
    return context_delimiter.seleccionar_faqs(data_model, consulta, max_entradas)

def seleccionar_docs(faqs: list[dict], data_model: DataModel, consulta: str, max_entradas: int = 4) -> list[dict]:
    return context_delimiter.seleccionar_docs(faqs, data_model, consulta, max_entradas)

def procesar_llamada(data_model: DataModel, llm_config: LlmConfig, user_history: UserHistory, user_msg: str, faqs: list[dict], docs: list[dict]) -> str:
    prompt = prompt_builder.build_assistant_prompt(data_model, llm_config, user_history, user_msg, faqs, docs)
    # print (prompt)
    user_history.append_user_message(user_msg)
    return llamar_llm(prompt, temperature=TEMPERATURE)
    # return ""

def procesar_llamada_json(data_model: DataModel, llm_config: LlmConfig, user_history: UserHistory, docs: list[dict]) -> str:
    print("PENDIENTE DE PROGRAMAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def llamar_llm(prompt: str,
    *,
    temperature: float = TEMPERATURE,
):
    if LLM_PROVEEDOR == "GEMINI":
        configurar_gemini_api_key()
        return llamar_gemini(prompt=prompt, temperature=temperature)
    else:
        raise ValueError(f"Proveedor {LLM_PROVEEDOR} de LLM no está soportado.")

