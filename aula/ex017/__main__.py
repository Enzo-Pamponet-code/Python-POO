from classes import *


def main():
    a = Numero(100)
    b = Texto('Olá mundo')
    c = Lista([2,3,5,7])
    d = Papel()
    e = Casa()

    tente_dobrar(a)
    tente_dobrar(b)
    tente_dobrar(c)
    tente_dobrar(d)
    tente_dobrar(e)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


if __name__ == '__main__':
    main()