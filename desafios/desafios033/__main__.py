from rich import inspect
from classes import *
import dnovo.classes


def main():
    c = Aluno('Enzo', 2000, 'ADM')
    c.nascimento = 1900
    inspect(c, private=True, methods=True)
    c = dnovo.classes.Aluno('Enzo', 2000, 'njr')
    inspect(c)
if __name__ == '__main__':
    main()