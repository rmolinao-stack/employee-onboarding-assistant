import common.utils as utils
import common.constants as constants

class Empleados:
    def __init__(self):
        self.data = utils.cargar_json(constants.EMPLEADOS_DEMO_PATH)
            
    def getData(self) -> list[dict]:
        return self.data