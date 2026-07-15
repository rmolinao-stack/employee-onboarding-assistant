import core.orchestrator as orchestrator
from model.data_model import DataModel
from core.user_history import UserHistory
from common.config import DIA_ONBOARDING, DOCS_LIMIT


def demo_11_conversacion(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
   ### FALTA AÑADIR EL DÍA DE ONBOARDING PARA QUE EL SISTEMA PUEDA SELECCIONAR LOS DOCUMENTOS CORRECTOS
   orchestrator.simular_conversacion(data_model, empl, ["¿A qué canales de slack tengo que unirme?"], dia_onboarding)
    
def demo_12_conversacion_masiva(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
    ### FALTA AÑADIR EL DÍA DE ONBOARDING PARA QUE EL SISTEMA PUEDA SELECCIONAR LOS DOCUMENTOS CORRECTOS
    list_msg = [
        "¿A qué canales de slack tengo que unirme?", 
        "No entiendo nada.",
        "Dame el salario de mi manager.",
        "Me han dicho algo de buddy o cuddy o no se que, ¿me lo explicas?",
        "¿Quien es mi responsable, y cual es su correo electronico?",
        "Recuerdas como me llamo y cual fue mi primer mensaje?"]
    
    orchestrator.simular_conversacion(data_model, empl, list_msg, dia_onboarding)

def demo_13_conversacion_5_dias(data_model: DataModel, empl: str):
    for dia in range(1, 6):
        print("=" * 80)
        print(f"Simulando conversación para el día {dia} de onboarding")
        print("=" * 80)
        demo_11_conversacion(data_model, empl, dia_onboarding=dia)
    
def demo_21_checklist(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
    orchestrator.generar_checklist_json(data_model, empl, dia_onboarding)

def demo_22_checklist_5_dias(data_model: DataModel, empl: str):
    for dia in range(1, 6):
        print("=" * 80)
        print(f"Generando checklist para el día {dia} de onboarding")
        print("=" * 80)
        orchestrator.generar_checklist_json(data_model, empl, dia_onboarding=dia)

def demo_31_comparar_perfiles(data_model: DataModel, empl1: str, empl2: str, dia_onboarding: int = DIA_ONBOARDING):
    ############ EMPLEADO 1 ##################
    print("=" * 80)
    print(f"id: {empl1}" )
    print(f"perfil: {data_model.empleados.getEmpleado(empl1)["perfil"]}")
    print("=" * 80)
    
    orchestrator.simular_conversacion(data_model, empl1, ["¿A qué canales de slack tengo que unirme?"], dia_onboarding)

    ############ EMPLEADO 2 ##################

    print("=" * 80)
    print(f"id: {empl2}" )
    print(f"perfil: {data_model.empleados.getEmpleado(empl2)["perfil"]}")
    print("=" * 80)
    
    orchestrator.simular_conversacion(data_model, empl2, ["¿A qué canales de slack tengo que unirme?"], dia_onboarding)
     
def main():
    #RMO: Cargamos todo el modelo de datos.
    data_model = DataModel()

    id = input(f"""Indica el identificador de la demo que quieres ejecutar:
               - AS11: Demo de asistente que simula conversación de 1 turno (empleado dev junior) para el día de onboarding {DIA_ONBOARDING}.
               - AS12: Demo de asistente que simula conversación masiva de varios turnos (empleado dev junior) para el día de onboarding {DIA_ONBOARDING}.
               - AS13: Demo de asistente que simula conversación de 1 turno (empleado dev junior) para los cinco primeros días.
               - AS21: Demo de asistente que simula checklist JSON, para el día de onboarding {DIA_ONBOARDING}.
               - AS22: Demo de asistente que simula checklist JSON, para los cinco primeros días.
               - AS31: Demo de asistente que simula mismo mensaje con empleado comercial vs remoto UE, para el día de onboarding {DIA_ONBOARDING}.
               
#Indentificador: """)

    if id.upper() == "AS11":
        demo_11_conversacion(data_model, "emp_01")
    elif id.upper() == "AS12":
        demo_12_conversacion_masiva(data_model, "emp_01")
    elif id.upper() == "AS13":
        demo_13_conversacion_5_dias(data_model, "emp_01")
    elif id.upper() == "AS21":
        demo_21_checklist(data_model, "emp_01")
    elif id.upper() == "AS22":
        demo_22_checklist_5_dias(data_model, "emp_01")
    elif id.upper() == "AS31":
        demo_31_comparar_perfiles(data_model, "emp_02", "emp_03")
    
    else:
        print("Identificador no soportado. Fin del programa")

if __name__ == "__main__":
    main()