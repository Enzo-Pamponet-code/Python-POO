from rich import inspect


class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade +=1




class Aluno(Pessoa):
    def __init__(self, nome,idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma


    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matricula!')




class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f'Professor {self.nome} deu aula')




class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f'{self.nome} acabou de bater o ponto')


a1 = Aluno('Enzo', 15, None, '1b')
a1.fazer_aniversario()
inspect(a1, methods=True)
a1.fazer_matricula()

p1 = Professor('Gustavo', 50, 'Programador', 'Mestrado')
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1)