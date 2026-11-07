class Numero:
    def __init__(self, valor:int|float = 0):
        self.num = valor
    def __str__(self) -> str:
        return f'O número dentro dele é {self.num}'
    def dobra(self):
        self.num *= 2


class Texto:
    def __init__(self, string:str = ""):
        self.texto = string
    def __str__(self) -> str:
        return f'Tenho o texto "{self.texto}" dentro de Texto'
    def dobra(self):
        self.texto += f' {self.texto}'


class Lista:
    def __init__(self, lista:list = []):
        self.lista = lista
    def __str__(self) -> str:
        return f'Tenho os itens {self.lista} dento de Lista'
    def dobra(self):
        self.lista += self.lista


class Papel:
    def __init__(self):
        self.dobrado = False
    def __str__(self) -> str:
        return f'O Papel está dobrado? {"novo" if not self.dobrado else "dobrado"}'
    def dobra(self):
        self.dobrado = True


class Casa:
    def __init__(self):
        pass
    def __str__(self) -> str:
        return f'Era uma casa, muito engraçada...'

def tente_dobrar(objeto):
    try:
        objeto.dobra()
    except:
        print(f'Não é possível dobra {objeto.__class__.__name__}')