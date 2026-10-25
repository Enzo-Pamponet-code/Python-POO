from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    salario_minimo = 1612
    inss = 7.5
    def __init__(self, nome):
        self.nome = nome



    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        painel = Panel(title='Analise de Salário', renderable=f'O salário de [purple]{self.nome} ([yellow]{self.__class__.__name__}[/])[/] é de [blue]R${self.__class__.calcular_salario(self):.2f}[/] e corresponde a [yellow]{self.__class__.calcular_salario(self)/Funcionario.salario_minimo:.1f} salários mínimos[/].', expand=False)
        print(painel)

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora,quantidade_horas):
        super().__init__(nome)
        self.valor = valor_hora
        self.q_hora = quantidade_horas
        self.salario_bruto = valor_hora * self.q_hora
        self.salario = self.salario_bruto - (self.salario_bruto*Funcionario.inss/100)

    def calcular_salario(self):
        return self.salario


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, valor_mensal):
        super().__init__(nome)
        self.nome = nome
        self.valor = valor_mensal

    def calcular_salario(self):
        return self.valor - (self.valor*Funcionario.inss/100)
