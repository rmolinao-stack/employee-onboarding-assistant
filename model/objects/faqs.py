import common.utils as utils
import common.constants as constants

class Faqs:
    def __init__(self):
        self.data = utils.cargar_json(constants.FAQ_PATH)
            
    def getData(self) -> list[dict]:
        return self.data