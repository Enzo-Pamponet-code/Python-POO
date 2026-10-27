from getpass import getpass

from rich import print


class Diario:
    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos:list = []
        self.__senha = senhamestra
    def escrever(self, msg:str):
        if msg is str and bool(msg):
            self.__segredos.append(msg)


    def ler(self,senha=''):
        if senha == self.__senha:
            print('[green]Diário Liberado![/]')
            for c in self.__segredos:
                if self.__segredos.index(c) != len(self.__segredos)-1:
                    print('-',c)
                else:
                    print('-',c)
        else:
            raise PermissionError('Você não tem permissão para ler o diário!')

    #eu esqueci
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, novasenha):
        conferidor = getpass('Digite sua senha antiga: ', echo_char='*')
        if conferidor == self.__senha:
            if bool(novasenha):
                self.__senha = novasenha
            else:
                print('Nova senha incoerente')
        else:
            print('Senha invalida')