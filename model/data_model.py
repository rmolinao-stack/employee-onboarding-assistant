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