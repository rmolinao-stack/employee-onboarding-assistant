from model.data_model import DataModel
from llm.llm_orchestrator import llamar_llm

def demo_conversacion():
    print(llamar_llm("Hola, me puedes decir que modelo de IA eres?"))
    

def demo_checklist():
    print("demo checklist")

def demo_check_comparar_perfiles():
    print("demo comprar perciles")


def main():
    #RMO: Cargamos todo el modelo de datos.
    data_model = DataModel()

    id = input("""Indica el identificador de la demo que quieres ejecutar:
               - AS1: Para demo de asistente modular que simula conversación de 1 turno (empleado tipo dev junior).
               - AS2: Para demo de asistente modular que simula checklist JSON para día 1.
               - AS3: Para demo de asistente modular que simula mismo mensaje con empleado comercial vs remoto UE.
Indentificador: """)

    if id == "AS1":
        demo_conversacion()
    elif id == "AS2":
        demo_checklist()
    elif id == "AS3":
        demo_check_comparar_perfiles()
    else:
        print("Identificador no soportado. Fin del programa")


if __name__ == "__main__":
    main()