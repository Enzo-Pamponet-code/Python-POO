from rich import inspect
from rich import print
from classes import *


def main():
    t = Termostato()
    t.temperatura = 25.3
    inspect(t, private=True, methods=True)
    print(f'A temperatura é {t.ftemperatura}')
if __name__ == '__main__':
    main()