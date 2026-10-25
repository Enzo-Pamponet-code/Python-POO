from rich import print
from rich.panel import Panel
from rich.bar import Bar
from rich.traceback import install
from rich.console import Group
from rich.columns import Columns
from desafio022 import identificador


class ControleRemoto:
    def __init__(self):
        self.canal = 1
        self.volume = 1
        self.ligada = False


    def ligar_des(self):
        self.ligada = not self.ligada


    def canal_(self, simbolo:str):
        if simbolo == '>' or simbolo =='<':
            if simbolo == '>':
                if self.canal == 5:
                    self.canal = 1
                else:
                    self.canal += 1
            else:
                if self.canal == 1:
                    self.canal = 5
                else:
                    self.canal -= 1
        else:
            print('[red bold]Error[/]')


    def volume_(self,sinal:str):
        if sinal == '+' or sinal == '-':
            if sinal == '+':
                if self.volume == 5:
                    self.volume += 0
                else:
                    self.volume += 1
            else:
                if self.volume == 1:
                    self.volume -= 0
                else:
                    self.volume -= 1
        else:
            print('[red bold]Error[/]')


    def definidor(self):
        while True:
            stri = f'Canal = {identificador(1,6, self.canal)}'
            ba = Bar(1, 0, (self.volume / 5), width=5, color='blue', bgcolor='white')
            v = Columns(['Volume = ', ba], expand=False)
            if self.ligada:
                final = Group(
                stri,
                v
                )
            else:
                final = '[red bold]Tv Desligada.[/]'
            print(Panel(final,title='[TV]', expand=False))
            put = input(f'<CH{self.canal}> -Vol{self.volume}+  ')
            if put == '@':
                self.ligar_des()
            if self.ligada:
                if put == '>' or put == '<':
                    controle.canal_(put)
                elif put == '+' or put == '-':
                    controle.volume_(put)
            if put == '0':
                break
            print('\n' * 30)



    def dados(self):
        return self.volume, self.ligada, self.canal



install()
controle = ControleRemoto()
controle.definidor()
