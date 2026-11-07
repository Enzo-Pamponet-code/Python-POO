import xml.etree.ElementTree as ET
from desafios.desafios039.classe import Email


class XML:
    def exportar(self):
        topo = ET.Element('dados')



class JSON:
   pass


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.email_ = email
    @property
    def email_(self):
        return self.email
    @email_.setter
    def email_(self, value):
        if Email().validar(self.email):
            self.email = value
        else:
            raise ValueError
