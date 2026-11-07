from rich import print
from rich.panel import Panel

class Mensagem:
    color = 'black'
    def __init__(self, msg:str):
        self._mensagem = msg
        self._tipo = 'Aviso'
        self._icone = ':speech_balloon:'

    def mostrar(self):
        painel = Panel(title=f'{self._icone}{self._tipo}{self._icone}', renderable=self._mensagem,style=f'bold on {self.__class__.color}',border_style=f'on {self.__class__.color}')
        print(painel)


class Erro(Mensagem):
    color = 'red'
    def __init__(self, msg:str):
        super().__init__(msg)
        self._tipo = 'ERRO'
        self._icone = ':prohibited:'


class Aviso(Mensagem):
    color = 'yellow'
    def __init__(self, msg:str):
        super().__init__(msg)
        self._tipo = 'Alerta'
        self._icone = ':warning:'