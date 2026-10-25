from classes import *


def main():
    p1 = Guerreiro('Kratos', 2000)
    p2 = Mago('Merlin', 3000)
    p1.atacar(p2, 3000)
    p2.atacar(p1, 3000)
    p1.atacar(p2, 3000)
    p2.atacar(p1, 3000)
    p1.curar()
    hp_bar(p1.nome, p1.vida, 2000)
    hp_bar(p2.nome, p2.vida, 3000)

if __name__ == '__main__':
    main()