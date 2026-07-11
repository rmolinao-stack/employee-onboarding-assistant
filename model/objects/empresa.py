import common.utils as utils
import common.constants as constants

class Empresa:
    def __init__(self):
        self.data = utils.cargar_json(constants.EMPRESA_PATH)
                    
    def getData(self) -> dict:
        return self.data