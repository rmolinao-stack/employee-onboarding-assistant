import common.utils as utils
import common.config as config

class Empleados:
    def __init__(self):
        self.data = utils.cargar_json(config.EMPLEADOS_DEMO_PATH)
            
    def getData(self) -> list[dict]:
        return self.data