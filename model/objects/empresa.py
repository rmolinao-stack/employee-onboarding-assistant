import common.utils as utils
import common.constants as constants

class Empresa:
    def __init__(self):
        self.data = utils.cargar_json(constants.EMPLEADOS_DEMO_PATH)
            
    def getEmpresa(self) -> dict:
        return self.data