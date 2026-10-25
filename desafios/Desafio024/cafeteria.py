from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def ferver_agua(self):
        print('1. Fervendo água a 100 Graus Celsius')

    def preparar(self):
        print(f'---Iniciando o Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('---Bebida Pronta---')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print('2. Passando água pressurizada pelo pó de café moido.')
    def servir(self):
        print('3. Servindo em xícara pequena.')

class Cha(BebidaQuente):
    def misturar(self):
        print('2. Mergulhando o sachê de ervas na água.')
    def servir(self):
        print('3. Servindo na caneca de porcelana com limão')

class Leite(BebidaQuente):
    def misturar(self):
        print('2. Passando vapor pressurizado pelo bico do leite.')
    def servir(self):
        print('3. Servindo na caneca grande, já com café')