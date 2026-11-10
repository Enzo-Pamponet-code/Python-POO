import xml.etree.ElementTree as ET
from desafios.desafios039.classe import Email


class XML:
    def exportar(self, dados):
        nome = dados[0].__class__.__name__.lower()
        raiz = ET.Element('dados')
        for c in dados:
            sub = ET.SubElement(raiz, nome)
            for k,v in c.__dict__.items():
                subb = ET.SubElement(sub, k)
                subb.text = str(v)
        ET.indent(raiz, space='       ')
        return ET.tostring(raiz, encoding='utf-8').decode()



class JSON:

   def exportar(self, dados):
       from json import dumps
       lista = []
       for c in dados:
           lista.append(c.__dict__)
       texto = dumps(lista, ensure_ascii=False, indent=2)
       return texto

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

class Aluno:

    def __init__(self, nome, curso ,serie):
        self.nome = nome
        self.curso =curso
        self.serie = serie

def exportar_dados(formato, dados):
    print(formato.exportar(dados))