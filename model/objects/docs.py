import common.utils as utils
import common.config as config

class Docs:
    def __init__(self):
        self.data = utils.cargar_json(config.DOCS_PATH)
            
    def getData(self) -> list[dict]:
        return self.data