import getpass
from hashlib import sha256
from rich import print


class ContaBancaria:
    def __init__(self, id, nome:str='', saldo:float = 0, chave = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = None
        if chave is None:
            self.__hash = sha256(getpass.getpass('Digite sua senha:', echo_char='*').encode('utf-8')).hexdigest()
        else:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
    @property
    def nome(self):
        return self._titular


    @nome.setter
    def nome(self, value:str):
        if self.pede_senha() == self.__hash:
            self._titular = value
        else:
            print('[red bold]Senha não confere. Nome não autorizado.[/]')


    def pede_senha(self)-> str:
        key_str = getpass.getpass('Digite sua senha: ', echo_char='*')
        key_sha = sha256(key_str.encode()).hexdigest()
        return key_sha


    def validar_senha(self, key_sha)->bool:
        boolean = key_sha == self.__hash
        return boolean


    def depositar(self,valor):
        self.__saldo += abs(valor)
        print(f'Deposito de R${valor} na conta {self._id}')


    def sacar(self, valor:float,chave = None):
        if not (valor is float or int):
            raise ValueError('\033[31mo parâmetro valor precisar ser um número!\033[m')
        if chave is None:
            chave = self.pede_senha()
            if self.validar_senha(chave):
                self.__saldo -= abs(valor)
            else:
                print('[red bold]Senha não confere. Saque não autorizado.[/]')
        else:
            chave = sha256(chave.encode()).hexdigest()
            if self.validar_senha(chave):
                self.__saldo -= abs(valor)
            else:
                print('[red bold]Senha não confere. Saque não autorizado.[/]')