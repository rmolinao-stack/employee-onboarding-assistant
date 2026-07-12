import core.orchestrator as orchestrator
from model.data_model import DataModel
from core.user_history import UserHistory
from common.config import DIA_ONBOARDING


def demo_1_conversacion(data_model: DataModel, empl: str):
    """
    Esta función esta concebida para verificar la demo1 solicitada en el enunciada. Concretamente:
    Conversación de 1 turno (empleado tipo dev junior)
    """

    user_history = orchestrator.inicializar_user_history(data_model, empl)
    llm_config = orchestrator.inicializar_asistente_llm()
    llm_msg = ""
    
    user_msg = "¿A qué canales de slack tengo que unirme?"

    
    faqs = orchestrator.seleccionar_faqs(data_model, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history, user_msg, faqs, docs)
    user_history.append_assistant_message(llm_msg)
    print(user_msg)
    print(llm_msg)


def demo_2_checklist(data_model: DataModel, empl: str):

    user_history = orchestrator.inicializar_user_history(data_model, empl)
    llm_config = orchestrator.inicializar_asistente_llm()
    llm_msg = ""
    msg=""
    
    if DIA_ONBOARDING >= 1:
        msg = msg + " primer_dia "
    if DIA_ONBOARDING <= 5:
        msg = msg + " checklist " + " primeras_semanas " + " onboarding "

    docs = orchestrator.seleccionar_docs([{}], data_model, msg, 6)
    llm_msg = orchestrator.procesar_llamada_json(data_model, llm_config, user_history, docs)
    print(llm_msg)


def demo_3_comparar_perfiles(data_model: DataModel, empl1: str, empl2: str):

    ############ EMPLEADO 1 ##################

    user_history1 = orchestrator.inicializar_user_history(data_model, empl1)
    llm_config = orchestrator.inicializar_asistente_llm()
    llm_msg = ""

    print("=" * 80)
    print(f"id: {empl1}" )
    print(f"perfil: {data_model.empleados.getEmpleado(empl1)["perfil"]}")
    print("=" * 80)
    
    user_msg = "¿A qué canales de slack tengo que unirme?"
    
    faqs = orchestrator.seleccionar_faqs(data_model, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history1, user_msg, faqs, docs)
    user_history1.append_assistant_message(llm_msg)
    print(user_msg)
    print(llm_msg)

    ############ EMPLEADO 2 ##################

    user_history2 = orchestrator.inicializar_user_history(data_model, empl2)
    llm_config = orchestrator.inicializar_asistente_llm()
    llm_msg = ""

    print("=" * 80)
    print(f"id: {empl2}" )
    print(f"perfil: {data_model.empleados.getEmpleado(empl2)["perfil"]}")
    print("=" * 80)
    
    user_msg = "¿A qué canales de slack tengo que unirme?"
    
    faqs = orchestrator.seleccionar_faqs(data_model, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history2, user_msg, faqs, docs)
    user_history2.append_assistant_message(llm_msg)
    print(user_msg)
    print(llm_msg)

def demo_conversacion_masiva(data_model: DataModel):
    user_history = orchestrator.inicializar_user_history(data_model, "emp_01")
    llm_config = orchestrator.inicializar_asistente_llm()
    llm_msg = ""
    
    user_msg = "¿A qué canales de slack tengo que unirme?"

    print(user_msg)
    faqs = orchestrator.seleccionar_faqs(data_model, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history, user_msg, faqs, docs)
    user_history.append_assistant_message(llm_msg)
    print(llm_msg)    
    
    user_msg = "No entiendo nada."

    print(user_msg)
    faqs = orchestrator.seleccionar_faqs(data_model, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history, user_msg, faqs, docs)
    user_history.append_assistant_message(llm_msg)
    print(llm_msg)

    user_msg = "Dame el salario del presidente del gobierno."

    print(user_msg)
    faqs = orchestrator.seleccionar_faqs(data_model, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history, user_msg, faqs, docs)
    user_history.append_assistant_message(llm_msg)
    print(llm_msg)

     
#def seleccionar_faq(faq: list[dict], consulta: str, max_entradas: int = 1) -> list[dict]:

def demo_checklist():
    print("demo checklist")




def main():
    #RMO: Cargamos todo el modelo de datos.
    data_model = DataModel()

    id = input("""Indica el identificador de la demo que quieres ejecutar:
               - AS1: Para demo de asistente modular que simula conversación de 1 turno (empleado tipo dev junior).
               - AS2: Para demo de asistente modular que simula checklist JSON para día 1.
               - AS3: Para demo de asistente modular que simula mismo mensaje con empleado comercial vs remoto UE.
#Indentificador: """)

    if id.upper() == "AS1":
        demo_1_conversacion(data_model, "emp_01")
    elif id.upper() == "AS2":
        demo_2_checklist(data_model, "emp_01")
    elif id.upper() == "AS3":
        demo_3_comparar_perfiles(data_model, "emp_02", "emp_03")
    else:
        print("Identificador no soportado. Fin del programa")


if __name__ == "__main__":
    main()