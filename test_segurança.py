from rich import inspect


class Test:
    def __init__(self,sec):
        self.__sec = sec

class Protegido:
    def __init__(self, valor_secreto):
        self.__vs = valor_secreto

    def valor(self):
        return self.__vs

    @property
    def _Protegido__vs(self):
        return None
    @_Protegido__vs.setter
    def _Protegido__vs(self, valor):
        if valor != self.__vs:
            raise PermissionError()
        else:
            self.__vs = self.__vs

a = Protegido(10)
inspect(a, private=True, methods=True)