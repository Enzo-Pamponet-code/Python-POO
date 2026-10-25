from rich import print
from rich.traceback import install
from test21 import tradutor

install()


class Caneta:
    def __init__(self, cor:str):
        self.tampada = True
        self.cor = tradutor(cor)


    def tampar(self):
        self.tampada = True


    def destampar(self):
        self.tampada = False


    def escrever(self,frase):
        if not self.tampada:
            print(f'[{self.cor}]{frase}[/]', end='')
        else:
            print('[red bold]A caneta está tampada[/]')



    def quebra_linha(self,numero):
        if numero <= 0:
            pass
        else:
            print('\n'*(numero-1))


c = Caneta('azul')
c.escrever('Olá, mundo')
c.destampar()
c.quebra_linha(1)
c.escrever('Neymar é lindo')