import common.utils as utils
import common.config as config

class Faqs:
    def __init__(self):
        self.data = utils.cargar_json(config.FAQ_PATH)
            
    def getData(self) -> list[dict]:
        return self.data