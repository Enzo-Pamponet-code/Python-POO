class Carteira:
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self) -> str:
        return f'Você tem R${self.__saldo:,.2f} na carteira'

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,valor):
        raise PermissionError('Você não tem permissão para alterar!')

    def __eq__(self, other) -> bool:
        if isinstance(other, Carteira):
            return self.__saldo == other.__saldo
        return False
    def __gt__(self, other):
        if isinstance(other, Carteira):
            return self.__saldo > other.__saldo
        return False
    def __lt__(self, other):
        if self < other:
            return True
        else:
            return False
    def __ne__(self, other):
        if isinstance(other, Carteira):
            return self.__saldo != other.__saldo
        return False
    def __le__(self, other):
        if isinstance(other, Carteira):
            return self.__saldo <= other.__saldo
        return False
    def __ge__(self, other):
        if isinstance(other, Carteira):
            return self.__saldo >= other.__saldo
        return False
    def __iadd__(self, other):
        self.__saldo += other
        return self
