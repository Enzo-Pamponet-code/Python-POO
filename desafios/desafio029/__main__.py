from rich import inspect

from classe import *
import dnovo.classe

def main():
    # classe
    diario = Diario()
    diario.escrever('Neymar')
    diario.ler('CeV!@')
    # classe dnovo
    print()
    mediador = dnovo.classe.Diario()
    mediador.senha = 'mbappe'
    inspect(mediador)
if __name__ == '__main__':
    main()