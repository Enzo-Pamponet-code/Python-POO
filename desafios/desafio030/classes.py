from hashlib import sha256
from rich import print


class Credencial:
    def __init__(self):
        self.__hash = None


    @property
    def senha(self):
        return self.__hash
    @senha.setter
    def senha(self, value:str):
        match value:
            case None:
                raise TypeError('É necessário colocar um valor.')
            case _:
                value = sha256(value.encode('utf-8')).hexdigest()
                self.__hash = value
    def validar(self, chave):
        encript_key = sha256(chave.encode('utf-8')).hexdigest()
        match encript_key:
            case self.__hash:
                print('Senha confere')
                print(True)
            case _:
                print('Senha não bate!')
                print(False)