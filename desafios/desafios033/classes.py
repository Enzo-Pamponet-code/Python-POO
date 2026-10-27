from abc import ABC
from datetime import date


class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int|float):
        self._nome = nome
        self._nascimento = nascimento


    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self, ano):
        if ano > int(str(date.today()).split('-')[0]) or ano < 1900:
            raise ValueError(f'Ano {ano} invalido')
        else:
            self._nascimento = ano


    @property
    def idade(self):
        return int(str(date.today()).split('-')[0]) - self._nascimento
    @idade.setter
    def idade(self, value):
        if self.idade < 0:
            raise ValueError('Não existe idade negativa.')
        if self.idade != value:
            raise  PermissionError('Não pode mudar a idade!')


class Aluno(Pessoa):
    def __init__(self, nome:str, nascimento:int|float, curso:str):
        super().__init__(nome, nascimento)
        self.nome = nome
        self.nascimento = nascimento
        self.cursos_oficiais = ['ADM', 'ADS','ENG','CONT']
        #gambiarra
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f'O Curso {curso} não está na lista de cursos oficiais.')


    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self,curso:str):
        if self._curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f'O Curso {curso} não está na lista de cursos oficiais.')

    def add_curso(self, value:str):
        self.cursos_oficiais.append(value)