from rich import print


class Diario:
    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos:list = []
        self.__senha = senhamestra
    def escrever(self, msg:str):
        self.__segredos.append(msg)


    def ler(self,senha=''):
        if senha == self.__senha:
            print('[green]Diário Liberado![/]')
            for c in self.__segredos:
                if self.__segredos.index(c) != len(self.__segredos)-1:
                    print('-',c)
                else:
                    print('-',c, end='')
        else:
            raise PermissionError('Você não tem permissão para ler o diário!')
