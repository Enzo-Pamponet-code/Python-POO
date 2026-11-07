from classes import *


def main():
    c = Carteira(1_0_0_0)
    c0 = Carteira(1000)
    c += 50
    print(c == c0)
    print(c>50)
    print(c, c0)
if __name__ == '__main__':
    main()