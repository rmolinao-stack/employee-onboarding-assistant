import common.utils as utils
import common.config as config

class Empresa:
    def __init__(self):
        self.data = utils.cargar_json(config.EMPRESA_PATH)
                    
    def getData(self) -> dict:
        return self.data