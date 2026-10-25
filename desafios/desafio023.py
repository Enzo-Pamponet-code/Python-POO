from abc import ABC, abstractmethod


#----------------classe abstrata-----------------------------
class Poligono(ABC):
    def __init__(self,quantidade_lados):
        #Atributos
        self.lados = quantidade_lados


    #Métodos Abstratos
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Quadrado(Poligono):
    def __init__(self,quantidade_lados):
        super().__init__(quantidade_lados)
        self.lados = quantidade_lados

    def area(self):
        return float(self.lados**2)

    def perimetro(self):
        return float(self.lados*4)

class Circulo(Poligono):
    def __init__(self,raio):
        super().__init__(raio)
        self.raio = raio

    def area(self):
        pi = 9801/(2206*(2**(1/2)))
        return float(self.raio**2 * pi)

    def perimetro(self):
        pi = 9801 / (2206 * (2 ** (1 / 2)))
        return float(self.raio*2*pi)


def main():
    p1 = Circulo(20)

    print(f'Área do quadrado é {p1.area():.1f} ')
    print(f'Perímetro do quadrado é {p1.perimetro():.1f}')


if __name__ == '__main__':
    main()