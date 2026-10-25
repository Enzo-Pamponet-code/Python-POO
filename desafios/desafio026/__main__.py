from classes import *

def main():
    a = FuncionarioHorista('Paulo', 12, 200)
    a.analisar_salario()

    b = FuncionarioMensalista('Amanda', 9500)
    b.analisar_salario()

if __name__ == '__main__':
    main()