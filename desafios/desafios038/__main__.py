from classes import *


def main():
    p = Produto('Notebook', 2000)
    p2 = Produto('chapéu', 20)
    c = Carrinho()
    c0 = Carrinho()
    p0 = Produto('jato', 1000000)
    p1 = Produto('Casa', 100000)
    c += p
    c0 = c0 + p0 + p1 + p +p2
    print(c)
    print()
    print(c0)

if __name__ == '__main__':
    main()