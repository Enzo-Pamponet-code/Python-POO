from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.dis = distancia

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    fator = 0.5
    def __init__(self, distancia):
        super().__init__(distancia)
        self.dis = distancia
    def calcular_frete(self):
        return f'R${float(self.dis * Moto.fator):.2f}'

class Caminhao(Transporte):
    fator = 1.2
    def __init__(self, distancia):
        super().__init__(distancia)
        self.dis = distancia
    def calcular_frete(self):
        if self.dis >= 50:
            return f'R${float(self.dis * Caminhao.fator):.2f}'
        else:
            return 'No mínimo 50 km para Transporte de caminhão'

class Drone(Transporte):
    fator = 9.5
    def __init__(self, distancia):
        super().__init__(distancia)
        self.dis = distancia
    def calcular_frete(self):
        if self.dis <= 10:
            return f'R${float(self.dis * Drone.fator):.2f}'
        else:
            return 'No máximo 10 km para o transporte de Drone'