from rich import inspect
from classes import *


def main():
    c = Aluno('Enzo', 2000, 'ADM')
    c.nascimento = 1900
    inspect(c, private=True, methods=True)
if __name__ == '__main__':
    main()