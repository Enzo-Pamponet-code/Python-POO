class Retangulo:
    def __init__(self):
        self._base = 1
        self._altura = 1
        self._area = None

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, value):
        try:
            float(value)
            self._base = float(f'{value:.2f}')
        except ValueError:
            print('Somente números')
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, value):
        try:
            float(value)
            self._altura = float(f'{value:.2f}')
        except ValueError:
            print('Somente números')
    @property
    def area(self):
        return self._altura * self._base
    @area.setter
    def area(self):
        self._area = self._altura * self._base

    @property
    def medidas(self):
        conteudo = ''
        conteudo += f'Base = {self.base}\n'
        conteudo+= f'Altura = {self.altura}\n'
        conteudo += f'Área = {self.area}'
        return conteudo
    @medidas.setter
    def medidas(self, values:tuple):
        self.altura = values[1]
        self.base = values[0]