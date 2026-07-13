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

    
    faqs = orchestrator.seleccionar_faqs(data_model, empl, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, empl, data_model, user_msg, 4)

    print(faqs)
    print("**" * 80)
    print(docs)
    print("**" * 80)


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

    docs = orchestrator.seleccionar_docs([{}], empl, data_model, msg, 6)
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
    
    faqs = orchestrator.seleccionar_faqs(data_model, empl1, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, empl1, data_model, user_msg, 4)
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
    
    faqs = orchestrator.seleccionar_faqs(data_model, empl2, user_msg, 2)
    docs = orchestrator.seleccionar_docs(faqs, empl2, data_model, user_msg, 4)
    llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history2, user_msg, faqs, docs)
    user_history2.append_assistant_message(llm_msg)
    print(user_msg)
    print(llm_msg)

def demo_4_conversacion_masiva(data_model: DataModel, emp_id: str):
    user_history = orchestrator.inicializar_user_history(data_model, emp_id)
    llm_config = orchestrator.inicializar_asistente_llm()
    llm_msg = ""
    list_msg = [
        "¿A qué canales de slack tengo que unirme?", 
        "No entiendo nada.",
        "Dame el salario de mi manager.",
        "Me han dicho algo de buddy o cuddy o no se que, ¿me lo explicas?",
        "¿Quien es mi responsable, y cual es su correo electronico?",
        "Recuerdas como me llamo y cual fue mi primer mensaje?"]
    
    for user_msg in list_msg:
        print(user_msg)
        faqs = orchestrator.seleccionar_faqs(data_model, emp_id, user_msg, 2)
        docs = orchestrator.seleccionar_docs(faqs, emp_id, data_model, user_msg, 4)
        llm_msg = orchestrator.procesar_llamada(data_model, llm_config, user_history, user_msg, faqs, docs)
        user_history.append_assistant_message(llm_msg)
        print(llm_msg)

        # print(faqs)
        # print("**" * 80)
        # print(docs)
        # print("**" * 80)
     
def main():
    #RMO: Cargamos todo el modelo de datos.
    data_model = DataModel()

    id = input("""Indica el identificador de la demo que quieres ejecutar:
               - AS1: Para demo de asistente modular que simula conversación de 1 turno (empleado tipo dev junior).
               - AS2: Para demo de asistente modular que simula checklist JSON para día 1.
               - AS3: Para demo de asistente modular que simula mismo mensaje con empleado comercial vs remoto UE.
               - AS4: Para demo de asistente modular que simula conversación masiva de varios turnos (empleado tipo dev junior).
#Indentificador: """)

    if id.upper() == "AS1":
        demo_1_conversacion(data_model, "emp_01")
    elif id.upper() == "AS2":
        demo_2_checklist(data_model, "emp_01")
    elif id.upper() == "AS3":
        demo_3_comparar_perfiles(data_model, "emp_02", "emp_03")
    elif id.upper() == "AS4":
        demo_4_conversacion_masiva(data_model, "emp_01")
    else:
        print("Identificador no soportado. Fin del programa")


if __name__ == "__main__":
    main()