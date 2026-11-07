from abc import ABC


class Arquivo(ABC):
    tipo = None
    abridor = None
    def __init__(self, nome:str, extensao,tamanho:int|float ):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho
        self.nome_completo = nome
    @property
    def nome_completo(self):
        return self.nome
    @nome_completo.setter
    def nome_completo(self,value):
        self.nome = f"'{self.nome}{self.__class__.tipo}'({self.tamanho/1000000:.2f}MB)"

    @property
    def extensao(self):
        return self._extensao
    @extensao.setter
    def extensao(self, ext):
        formatos = ['pdf', 'doc', 'py']
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError



class PDF(Arquivo):
    tipo = '.pdf'
    abridor = 'Adobe Reader'


class DOC(Arquivo):
    tipo = '.docx'
    abridor = 'Microsoft Word'

class Python(Arquivo):
    tipo = '.py'
    abridor = 'PyCharm'

def abrir_arquivo(arquivo):
    print(f'Abrindo o arquivo {arquivo.nome_completo} no {arquivo.__class__.abridor}')