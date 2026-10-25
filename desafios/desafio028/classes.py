class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
         return self.__temperatura
    @temperatura.setter
    def temperatura(self, valor):
        if 16<= valor <= 30:
            if valor%0.5 == 0:
                self.__temperatura = valor
            else:
                raise ValueError('Este valor não é permitido, pois o resto da divisão por 0,5 não retorna zero.')
        else:
            if valor < 16:
                self.__temperatura = 16
            else:
                self.__temperatura = 30
    @property
    def ftemperatura(self):
        return f'{self.__temperatura}°C'