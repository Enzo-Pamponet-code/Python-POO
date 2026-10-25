from classes import Aluno, Professor, Funcionario



def main():
    a1 = Aluno('Enzo', 15, None, '1b')
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Gustavo', 50, 'Programador', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario('Jose', 30,'secretário', 'administração')

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == '__main__':
    main()
