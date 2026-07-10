import utils

class Empresa:
    def __init__(self, json_path):
        self.data = utils.cargar_json(json_path)
            
    def getEmpresa(self) -> dict:
        return self.data