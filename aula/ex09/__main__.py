from rich import inspect
from classes import *

def main():
    av1 = Avaliacao('Enzo', 'Matemática', 9.5)
    av1.set_nota(7.5)
    print(av1.get_nota())
    inspect(av1, private=True)
if __name__ == '__main__':
    main()
