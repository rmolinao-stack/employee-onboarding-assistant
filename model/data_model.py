from model.objects.empresa import Empresa
from model.objects.empleados import Empleados
from model.objects.docs import Docs
from model.objects.faqs import Faqs


class DataModel:
    def __init__(self):
        self.empresa = Empresa()
        self.empleados = Empleados()
        self.docs = Docs()
        self.faqs = Faqs()
    
    def getEmpresa(self) -> dict:
        return self.empresa.getData()
    
    def getEmpleados(self) -> list[dict]:
        return self.empleados.getData()
    
    def getDocs(self) -> list[dict]:
        return self.docs.getData()
    
    def getFaqs(self) -> list[dict]:
        return self.faqs.getData()