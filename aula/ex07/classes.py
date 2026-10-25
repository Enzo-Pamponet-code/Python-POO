from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade +=1

    @abstractmethod
    def estudar(self):
        pass




class Aluno(Pessoa):
    def __init__(self, nome,idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma


    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matricula!')

    def estudar(self):
        print(f'O aluno {self.nome} está estudando no {self.curso} na turno {self.turma}')




class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f'Professor {self.nome} deu aula')

    def estudar(self):
        print(f'{self.nome} é especialista em {self.especialidade} no nivel {self.nivel}')




class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f'{self.nome} acabou de bater o ponto')

    def estudar(self):
        print(f'{self.nome} se especializa para {self.cargo}')