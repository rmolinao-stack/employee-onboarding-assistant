import common.utils as utils
import common.constants as constants

class Docs:
    def __init__(self):
        self.data = utils.cargar_json(constants.DOCS_PATH)
            
    def getData(self) -> list[dict]:
        return self.data