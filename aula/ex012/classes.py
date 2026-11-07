from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome:str):
        self.nome =nome


    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e está emitindo um som.')



class Pato(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de grasnar "Quack!"')

class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer "AU!AU!AU!AU"')
class Spitz(Cachorro):
    pass
class PitBull(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer "RUF!RUF!RUF"')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de miar "Miau!"')

class Galinha(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de cacarejar "córocó"')