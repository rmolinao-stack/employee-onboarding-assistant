import core.orchestrator as orchestrator
from model.data_model import DataModel
from core.user_history import UserHistory

def demo_conversacion(data_model: DataModel):
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

  

    #doc = seleccion_doc(data_model, user_msg)
#
    #imprimir_resultado(sel)
    # if faq["status"] != "ok":
    #    return
    #faq_entry = [faq["data"]["entry"]]




    # procesar_llamada(data_model, llm_config, user_history, user_msg, faqs, docs)




    # prompt = build_assistant_prompt(
    #     assistant_config=config,
    #     user_state=state,
    #     user_message=user_message,
    #     extra_context=faq_entries or [],
    #     recent_messages=ultimos_n(state, ventana),
    # )


    # print(llamar_llm("Hola, me puedes decir que modelo de IA eres?"))


    
#def seleccionar_faq(faq: list[dict], consulta: str, max_entradas: int = 1) -> list[dict]:

def demo_checklist():
    print("demo checklist")

def demo_check_comparar_perfiles():
    print("demo comprar perciles")


def main():
    #RMO: Cargamos todo el modelo de datos.
    data_model = DataModel()

#    id = input("""Indica el identificador de la demo que quieres ejecutar:
#               - AS1: Para demo de asistente modular que simula conversación de 1 turno (empleado tipo dev junior).
#               - AS2: Para demo de asistente modular que simula checklist JSON para día 1.
#               - AS3: Para demo de asistente modular que simula mismo mensaje con empleado comercial vs remoto UE.
#Indentificador: """)

    id = "AS1" 
    
    

    if id.upper() == "AS1":
        demo_conversacion(data_model)
    elif id.upper() == "AS2":
        demo_checklist()
    elif id.upper() == "AS3":
        demo_check_comparar_perfiles()
    else:
        print("Identificador no soportado. Fin del programa")


if __name__ == "__main__":
    main()