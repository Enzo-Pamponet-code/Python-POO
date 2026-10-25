from rich import print
from rich.traceback import install
from utils.primitivos import numero as n


install()

def hp_bar(nome, vida_com_dano, vida_total, tamanho_da_barra = 10):
    print(nome, end=' ')
    print(barra(tamanho_da_barra, vida_com_dano/vida_total*100, printar_conteudo=False, vida=vida_com_dano), end=' ')
    print(vida_total)

def barra(fim:int, porcentagem_inteira, printar_conteudo=True, vida = ' '):
    conteudo = ''
    vida = str(vida)
    if porcentagem_inteira >= 50:
        base = f'green'
    else:
        base = f'red'
    porcentagem = int(fim*porcentagem_inteira/100)
    if not fim % 2 == 0:
        fim += 1
    for i in range(0,fim):
        if int(fim/3) <= int(i) :
            if i <= porcentagem:
                try:
                    conteudo += f'[{base} on cyan]{vida[i-int(fim/3)]}[/]'
                except IndexError:
                    conteudo += f'[on cyan] [/]'
            else:
                try:
                    conteudo += f'[{base} on white]{vida[i-int(fim/3)]}[/]'
                except IndexError:
                    conteudo += f'[on white] [/]'
        else:
            if porcentagem == 0:
                conteudo += f'[on white] [/]'
            elif i <= porcentagem:
                conteudo += f'[on cyan] [/]'
            else:
                conteudo += f'[on white] [/]'
    if printar_conteudo:
        print(conteudo)
        return None
    else:
        return conteudo


class Ciclo:
    def __init__(self, inicio, fim, numero):
        self.ini = inicio
        self.end = fim
        self.num = numero
        self.q = self.end - (self.ini - 1)
        self.final = 0


    def calcular(self):
        if self.num > self.end:
            self.final = (self.num % self.q) + self.ini
        elif self.ini <= self.num <= self.end:
            self.final = self.num
        else:
            self.final = self.num % self.q
        return self.final


    def mostra(self):
        print(Ciclo.calcular(self))


class Real:
    def __init__(self, numero):
        self.num = numero
        self.cuidado = n(self.num)


    def __class__(self) -> str:
        return '<class Real>'

    def __int__(self):
        return self.cuidado

    def __float__(self):
        return self.cuidado

    def __add__(self, other):
        return Real(self.cuidado) + Real(other)


