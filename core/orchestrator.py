from common.utils import imprimir_contexto_seleccionado
from core.validators import construir_respuesta_segura, validar_mensaje_usuario
from model.data_model import DataModel
from common.config import DOCS_LIMIT, FAQS_LIMIT, TEMPERATURE, LLM_PROVEEDOR, DIA_ONBOARDING
from llm.gemini.gemini_auth import configurar_gemini_api_key
from llm.gemini.gemini_client import llamar_gemini
from core.user_history import UserHistory
import core.context_delimiter as context_delimiter
import core.prompt_builder as prompt_builder
import sys


def inicializar_user_history(data_model: DataModel, id_empl: str | None = None, print_initial_messages: bool = True, dia_onboarding: int = DIA_ONBOARDING) -> UserHistory:
    empleado: dict = None
    intentos = 0
    initial_msg1 = f"""Bienvenido a {data_model.empresa.data["producto_reto"]} de {data_model.empresa.data["nombre"]}. 
Mi objetivo es resolver todas las preguntas que tengas referente al proceso de Onboardig en {data_model.empresa.data["nombre"]}."""

    while not empleado:
        if not id_empl:
            id_empl = input(f"""Para continuar necesito que me indiques el identificador de empleado valido que te debería haber proporcionado RRHH: """)
        empleado = data_model.empleados.getEmpleado(id_empl)
        if not empleado: 
            print("El empleado indicado no es valido.")
            id_empl = None
            intentos += 1
        if intentos == 3:
            print("Has indicado 3 códigos de empleados invalidos. El chat va a finalizar.")
            sys.exit()
    
    initial_msg2 = f"Te has identificado como {empleado['nombre']}, ¿en que puedo ayudarte?"
    if print_initial_messages:
        print(f"|SISTEMA|: {initial_msg1}\n{initial_msg2}")
    
    user_history = UserHistory(empleado, dia_onboarding=dia_onboarding)
    user_history.append_assistant_message(initial_msg1 + "\n" + initial_msg2)

    return user_history

def seleccionar_faqs(data_model: DataModel, empl: str, consulta: str, max_entradas: int, dia_onboarding: int) -> list[dict]:
    return context_delimiter.seleccionar_faqs(data_model, empl, consulta, max_entradas, dia_onboarding)

def seleccionar_docs(faqs: list[dict], empl: str, data_model: DataModel, consulta: str, max_entradas: int, dia_onboarding: int) -> list[dict]:
    return context_delimiter.seleccionar_docs(faqs, empl, data_model, consulta, max_entradas, dia_onboarding)

def procesar_llamada(data_model: DataModel, user_history: UserHistory, user_msg: str, faqs: list[dict], docs: list[dict], vulnerable: bool = False) -> str:
    if not vulnerable:
        valido, razon = validar_mensaje_usuario(user_msg)
        user_history.append_user_message(user_msg)
        if not valido:
            llm_msg = construir_respuesta_segura(razon)
        else:
            prompt = prompt_builder.build_assistant_prompt(data_model, user_history, user_msg, faqs, docs)
    else:
        prompt = prompt_builder.build_assistant_prompt_vulnerable(data_model, user_history, user_msg, faqs, docs)
    
    llm_msg = llamar_llm(prompt, temperature=TEMPERATURE)
    user_history.append_assistant_message(llm_msg)
        
    return llm_msg
    #return ""

# RMO SI LLAMAMOS A ESTO NO GUARDAMOS EL CONTEXTO. NO ES NECESARIO
def procesar_llamada_json(data_model: DataModel, user_history: UserHistory, docs: list[dict], dia_onboarding: int) -> str:
    prompt = prompt_builder.build_checklist_json_prompt(data_model, user_history, docs, dia_onboarding)
    # print (prompt)
    return llamar_llm(prompt, temperature=TEMPERATURE)
    # return ""


def llamar_llm(prompt: str,
    *,
    temperature: float = TEMPERATURE,
):
    if LLM_PROVEEDOR == "GEMINI":
        configurar_gemini_api_key()
        return llamar_gemini(prompt=prompt, temperature=temperature)
    else:
        raise ValueError(f"Proveedor {LLM_PROVEEDOR} de LLM no está soportado.")
    
def simular_conversacion(data_model: DataModel, empl: str, list_msg: list[str], dia_onboarding: int, vulnerable: bool = False):
    user_history = inicializar_user_history(data_model, empl, False, dia_onboarding=dia_onboarding)    
    for user_msg in list_msg:
        print("")
        print("=" * 80)
        print(f"Turno de conversación: {user_history.turno}")
        print("=" * 80)
        print("")
        print(f"|USUARIO|: {user_msg}")
        faqs = seleccionar_faqs(data_model, empl, user_msg, FAQS_LIMIT, dia_onboarding)
        docs = seleccionar_docs(faqs, empl, data_model, user_msg, DOCS_LIMIT, dia_onboarding)
        # imprimir_contexto_seleccionado(faqs, docs)
        llm_msg = procesar_llamada(data_model, user_history, user_msg, faqs, docs, vulnerable)
        print(f"|SISTEMA|: {llm_msg}")


def generar_checklist_json(data_model: DataModel, empl: str, dia_onboarding: int):
    user_history = inicializar_user_history(data_model, empl, False, dia_onboarding=dia_onboarding)
    
    docs = seleccionar_docs([{}], empl, data_model, "", DOCS_LIMIT, dia_onboarding)
    llm_msg = procesar_llamada_json(data_model, user_history, docs, dia_onboarding)
    print(llm_msg)

