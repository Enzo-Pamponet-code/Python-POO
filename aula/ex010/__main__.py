from rich import inspect
from classes import *

def main():
    av1 = Avaliacao('Enzo', 'Matemática', 9.5)
    av1.nota = -7
    print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')
    inspect(av1, private=True)
if __name__ == '__main__':
    main()
