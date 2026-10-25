from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario




a1 = Aluno('Enzo', 15, None, '1b')
a1.fazer_aniversario()


p1 = Professor('Gustavo', 50, 'Programador', 'Mestrado')
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario