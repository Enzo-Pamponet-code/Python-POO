from classes import *
from rich import print
from rich.table import Table


def main():
    dist = 100

    t0 = Moto(dist)
    t1 = Caminhao(dist)
    t2 = Drone(dist)

    tabela = Table(title='Tabela de frete')
    tabela.add_column('Distância')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')
    tabela.add_row(f'{dist}Km', type(t0).__name__, t0.calcular_frete())
    tabela.add_row(f'{dist}Km', type(t1).__name__, t1.calcular_frete())
    tabela.add_row(f'{dist}Km', type(t2).__name__, t2.calcular_frete())
    print(tabela)
if __name__ == '__main__':
    main()