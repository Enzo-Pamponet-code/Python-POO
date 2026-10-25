from abc import ABC, abstractmethod
from rich import print
from random import randint
from apoiador import *


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.socos = []
        self.dicionario = {}

    def atacar(self, alvo,forca):
        ataque(alvo, forca, self.nome, self.socos, self.dicionario, self.vida)

    def receber_dano(self, alvo, dano_real):
        receber_ataque(alvo, self.dicionario, dano_real)

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self,nome, vida):
        super().__init__(nome, vida)
        self.socos = ['Soco', 'pulo giratório', 'Golpe de Machado']
        self.dicionario = {}

    def curar(self):
        if self.vida > 0:
            valor_cura = randint(0,100)
            print(f'[purple]{self.nome}[/] enrolou uma atadura no ferimentos e ganhou [green]{valor_cura} HP[/]')
            self.vida += valor_cura
        else:
            print(f'[red bold]{self.nome} está Morto[/]')


class Mago(Personagem):
    def __init__(self,nome, vida):
        super().__init__(nome, vida)
        self.socos = ['Bola de fogo']
        self.dicionario = {}

    def curar(self):
        if self.vida == 0:
            self.vivo = False
        if self.vivo:
            valor_cura = randint(0,100)
            print(f'[blue]{self.nome}[/] fez uma magia e ganhou [green]{valor_cura} HP[/]')
            self.vida += valor_cura
        else:
            print(f'[red bold]{self.nome} está Morto[/]')