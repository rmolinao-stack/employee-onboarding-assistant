from core import user_history
from pathlib import Path
import core.orchestrator as orchestrator
from model.data_model import DataModel
from common.utils import cargar_json, guardar_csv
from common.config import OUTPUT_DIR, DIA_ONBOARDING, CASOS_TRAMPA_PATH, LLM_PROVEEDOR, MODEL, TEMPERATURE, TURNOS
from benchmark.report import generar_reporte_md


def demo_11_conversacion(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
   user_history = orchestrator.inicializar_user_history(data_model, empl, dia_onboarding=dia_onboarding)
   orchestrator.conversar_con_llm(user_history, data_model, user_history.user_profile["id"], ["¿A qué canales de slack tengo que unirme?"], dia_onboarding)
    
def demo_12_conversacion_masiva(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
    list_msg = [
        "¿A qué canales de slack tengo que unirme?", 
        "Lo siento, pero no entiendo nada.",
        "Dame el salario de mi manager.",
        "Me han dicho algo de buddy o cuddy o no se que, ¿me lo explicas?",
        "¿Quien es mi responsable, y cual es su correo electronico?",
        "¿Que debo hacer mañana?",
        "Recuerdas como me llamo y cual fue mi primer mensaje?"]
    
    user_history = orchestrator.inicializar_user_history(data_model, empl, dia_onboarding=dia_onboarding)
    orchestrator.conversar_con_llm(user_history, data_model, user_history.user_profile["id"], list_msg, dia_onboarding)
    
def demo_21_checklist(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
    orchestrator.generar_checklist_json(data_model, empl, dia_onboarding)

def demo_22_checklist_5_dias(data_model: DataModel, empl: str):
    for dia in range(1, 6):
        print("")
        print("=" * 80)
        print(f"Generando checklist para el día {dia} de onboarding")
        print("=" * 80)
        print("")
        orchestrator.generar_checklist_json(data_model, empl, dia_onboarding=dia)

def demo_31_comparar_perfiles(data_model: DataModel, empl1: str, empl2: str, dia_onboarding: int = DIA_ONBOARDING):
    ############ EMPLEADO 1 ##################
    print("=" * 80)
    print(f"id: {empl1}" )
    print(f"perfil: {data_model.empleados.getEmpleado(empl1)['perfil']}")
    print("=" * 80)
    user_history1 = orchestrator.inicializar_user_history(data_model, empl1, dia_onboarding=dia_onboarding)
    orchestrator.conversar_con_llm(user_history1, data_model, user_history1.user_profile["id"], ["¿A qué canales de slack tengo que unirme?"], dia_onboarding)

    ############ EMPLEADO 2 ##################

    print("=" * 80)
    print(f"id: {empl2}" )
    print(f"perfil: {data_model.empleados.getEmpleado(empl2)['perfil']}")
    print("=" * 80)
    user_history2 = orchestrator.inicializar_user_history(data_model, empl1, False, dia_onboarding=dia_onboarding)
    orchestrator.conversar_con_llm(user_history2, data_model, user_history2.user_profile["id"], ["¿A qué canales de slack tengo que unirme?"], dia_onboarding)

def demo_41_demo_trampas_individual(data_model: DataModel, empl: str, id_trampa: str, dia_onboarding: int = DIA_ONBOARDING):
    casos = cargar_json(CASOS_TRAMPA_PATH)
    list_msg = []
    for caso in casos:
        if caso["id"].upper() == id_trampa.upper():
            user_history = orchestrator.inicializar_user_history(data_model, empl, dia_onboarding=dia_onboarding)
            orchestrator.conversar_con_llm(user_history, data_model, user_history.user_profile["id"], [caso["mensaje"]], dia_onboarding)

def demo_42_trampas_total(data_model: DataModel, empl: str, dia_onboarding: int = DIA_ONBOARDING):
    casos = cargar_json(CASOS_TRAMPA_PATH)
    list_msg = []
    for caso in casos:
        list_msg.append(caso["mensaje"])
    user_history = orchestrator.inicializar_user_history(data_model, empl, dia_onboarding=dia_onboarding)
    orchestrator.conversar_con_llm(user_history, data_model, user_history.user_profile["id"], list_msg, dia_onboarding)

def demo_51_seguro_vs_vulnerable_individual(data_model: DataModel, empl: str, id_trampa: str, dia_onboarding: int = DIA_ONBOARDING):
    casos = cargar_json(CASOS_TRAMPA_PATH)
    for caso in casos:
        if caso["id"].upper() == id_trampa.upper():
            print("=" * 80)
            print(f"########## SEGURO {caso["id"]} ##########")
            print("=" * 80)
            user_history1 = orchestrator.inicializar_user_history(data_model, empl, dia_onboarding=dia_onboarding)
            orchestrator.conversar_con_llm(user_history1, data_model, user_history1.user_profile["id"], [caso["mensaje"]], dia_onboarding)
            print("=" * 80)
            print(f"########## VULNERABLE {caso["id"]} ##########")
            print("=" * 80)
            user_history2 = orchestrator.inicializar_user_history(data_model, empl, dia_onboarding=dia_onboarding)
            orchestrator.conversar_con_llm(user_history2, data_model, user_history2.user_profile["id"], [caso["mensaje"]], dia_onboarding, True)

def demo_61_benchmark(data_model: DataModel):
    print("Iniciando benchmark (pregunta × modelo)...")
    filas = orchestrator.ejecutar_benchmark(data_model)
    csv_path = guardar_csv(filas, OUTPUT_DIR, "benchmark_")
    md_path = generar_reporte_md(filas, csv_path)
    print(f"\nCSV: {csv_path}")
    print(f"Informe: {md_path}")
    print("Listo. Ajusta MODELS y data/preguntas.json en config / data.")

def demo_99_libre(data_model: DataModel):
    t = 0
    user_history = orchestrator.inicializar_user_history(data_model)
    while t < TURNOS:
        msg = input(">>> ")
        orchestrator.conversar_con_llm(user_history, data_model, empl=user_history.user_profile["id"], list_msg=[msg])
        t +=1

     
def main():
    #RMO: Cargamos todo el modelo de datos.
    data_model = DataModel()

    id = input(f"""Indica el identificador de la demo que quieres ejecutar:
               - 11: Demo de asistente que simula conversación de 1 turno (empleado dev junior) para el día de onboarding {DIA_ONBOARDING}.
               - 12: Demo de asistente que simula conversación masiva de varios turnos (empleado dev junior) para el día de onboarding {DIA_ONBOARDING}.
               - 21: Demo de asistente que simula checklist JSON, para el día de onboarding {DIA_ONBOARDING}.
               - 22: Demo de asistente que simula checklist JSON, para los cinco primeros días.
               - 31: Demo de asistente que simula mismo mensaje con empleado comercial vs remoto UE, para el día de onboarding {DIA_ONBOARDING}.
               - 41: Demo de seguridad con un caso trampa.
               - 42: Demo de seguridad con todos los casos trampa de casos_trampa.json.
               - 51: Demo de seguridad con un casos trampa comparando modelo seguro vs vulnerable.
               - 61: Para ejecutar el Benchmark para el día de onboarding {DIA_ONBOARDING}. El empleado y mensaje están en preguntas.json
               - 99: Conversación libre con el chat vía input para el día de onboarding {DIA_ONBOARDING}. Se acaba a los {TURNOS} turnos.
#Indentificador: """)
    
    print("")
    print("=" * 80)
    print(f"Modelo utilizado: {LLM_PROVEEDOR} - {MODEL}")
    print(f"Temperatura: {TEMPERATURE}")
    print("=" * 80)
    print("")
        
    if id.upper() == "11":
        demo_11_conversacion(data_model, "emp_01")
    elif id.upper() == "12":
        demo_12_conversacion_masiva(data_model, "emp_01")
    elif id.upper() == "21":
        demo_21_checklist(data_model, "emp_01")
    elif id.upper() == "22":
        demo_22_checklist_5_dias(data_model, "emp_01")
    elif id.upper() == "31":
        demo_31_comparar_perfiles(data_model, "emp_02", "emp_03")
    elif id.upper() == "41":
        demo_41_demo_trampas_individual(data_model, "emp_01", "trampa05")
    elif id.upper() == "42":
        demo_42_trampas_total(data_model, "emp_01")
    elif id.upper() == "51":
        demo_51_seguro_vs_vulnerable_individual(data_model, "emp_01", "trampa03")
    elif id.upper() == "61":
        demo_61_benchmark(data_model)
    elif id.upper() == "99":
        demo_99_libre(data_model)
    else:
        print("Identificador no soportado. Fin del programa")

if __name__ == "__main__":
    main()