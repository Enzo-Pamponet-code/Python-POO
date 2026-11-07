from abc import ABC


class Pagamento(ABC):
    def __init__(self, valor:int|float = 0):
        self._valor = valor
        self.valor = valor

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, value):
        if value < 0:
            raise ValueError('Deposito não pode ser negativo.')
        self._valor = value

    @property
    def fvalor(self):
        return f'{convesor(self._valor)}'
    @fvalor.setter
    def fvalor(self,value:int|float):
        if value < 0:
            raise ValueError('Valor Incorreto!')
        self._valor = value

class Pix(Pagamento):
    pass

class CartaoCredito(Pagamento):
    pass

class Boleto(Pagamento):
    pass


def convesor(value:int|float):
    try:
        value = float(value)
        if type(value) is float:
            inte = int(value)
            deci = str(value - inte)[2:4]
            if len(str(deci)) == 1:
                inte = f'{inte:,}'.replace(',','.')
                return f'R$ {inte},{deci}0'
            else:
                return f'R$ {inte},{deci}'
    except:
        raise ValueError


def finalizar_compra(metodo_pagamento, valor):
    classe = metodo_pagamento
    classe.__init__(valor)
    print(f'Pagamento CONFIRMADO de {classe.fvalor} via {metodo_pagamento.__class__.__name__}')