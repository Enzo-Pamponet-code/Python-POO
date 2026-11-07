from functools import singledispatchmethod



class Analisador:
    def __init__(self):
        pass

    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possível analisar o valor {valor}')

    @analisar.register
    def _(self, valor:int):
        print(f'{valor} é um número Inteiro')

    @analisar.register
    def _(self, valor: float):
        print(f'{valor} é um número Real')

    @analisar.register
    def _(self, valor: list|tuple|dict):
        print(f'{valor} é um literal')

    @analisar.register
    def _(self, valor:str):
        print(f'{valor} é uma cadeia de caracteres')