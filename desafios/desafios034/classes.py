from abc import ABC


class Funcionario(ABC):
    def __init__(self, nome:str, salario:int|float):
        self.nome = nome
        self.__salario = salario

    def __str__(self) -> str:
        return f'{self.nome} ganha R${self.__salario:,.2f} e por ser {self.__class__.__name__} e bônus será de R${float(self.__salario*self.__class__.bonus):,.2f}'

    def calcular_bonus(self):
        pass

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, value):
        if not value < self.__salario:
            self.__salario = value
        else:
            raise ValueError('Não pde reduzir o salário de um funcionário.')


class Gerente(Funcionario):
    def calcular_bonus(self):
        self.salario += self.salario*0.15


class Designer(Funcionario):
    def calcular_bonus(self):
        self.salario += self.salario*0.08


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        self.salario += self.salario*0.1