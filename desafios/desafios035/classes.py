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
        self.nome = f"'{self.nome}.{self.extensao}'({self.tamanho/1000000:.2f}MB)"

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
    def __init__(self, nome:str, tamanho:int|float ):
        super().__init__(nome, 'pdf', tamanho)
    def abrir(self):
        print(f"Abrindo o arquivo {self.nome} no Adobe Reader")


class DOC(Arquivo):
    def __init__(self, nome:str, tamanho:int|float ):
        super().__init__(nome, 'docx', tamanho)
    def abrir(self):
        print(f"Abrindo o arquivo {self.nome} no Microsoft Word")

class Python(Arquivo):
    def __init__(self, nome:str, tamanho:int|float ):
        super().__init__(nome, 'py', tamanho)
    def abrir(self):
        print(f"Abrindo o arquivo {self.nome} no PyCharm")

def abrir_arquivo(arquivo):
    arquivo.abrir()