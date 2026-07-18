import common.utils as utils
import common.config as config

class Empleados:
    def __init__(self):
        self.data = utils.cargar_json(config.EMPLEADOS_DEMO_PATH)
            
    def getData(self) -> list[dict]:
        return self.data
    
    def getEmpleado(self, id_empl: str) -> dict:
        empleado = None
        for data in self.data:
            if str(data["id"]).upper() == id_empl.upper().strip():
                empleado = data

        return empleado