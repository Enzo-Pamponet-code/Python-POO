from classes import *


def main():
    a1 = DOC('prova', 250000)
    a2 = PDF('Livro de Flask', 1000000)
    a3 = Python('__main__', 1000)
    print(a1.nome_completo)
    abrir_arquivo(a1)
    abrir_arquivo(a2)
    abrir_arquivo(a3)
if __name__ == '__main__':
    main()