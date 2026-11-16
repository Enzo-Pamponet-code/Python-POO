import sqlite3
from rich import print
from rich.panel import Panel
from datetime import date





class BancoDados:
    def __init__(self, banco_de_dados):
        self.bd = banco_de_dados

    def encontrar(self):
        busca = input('Pesquise: ')
        try:
            with sqlite3.connect(self.bd) as banco:
                c = banco.cursor()
                c.execute('''SELECT *
                FROM amigos
                WHERE nome LIKE ?''', (f'%{busca}%',))
                lista = c.fetchall()
                if len(lista).__eq__(0):
                    print('[red]Nenhum dado encontrado[/]')
                else:
                    prenel = ''
                    for c in lista:
                        lista_ = []
                        for p in c:
                            lista_.append(p)
                        try:
                            ano_atual = date.today()
                            data = date.fromisoformat(lista_[2])
                            if ano_atual.month < data.month:
                                lista_.append(str(ano_atual.year - data.year-1)+' anos')
                            else:
                                lista_.append(str(ano_atual.year - data.year) + ' anos')
                            lista_[2] = f'[blue]{data:%d/%m/%Y}[/]'
                            prenel += f'{lista_}\n'
                        except AttributeError:
                            prenel += f'[red]{lista_[0]}. Esse dado é invalido[/]'
                        except TypeError:
                            prenel += f'A data desse da pessoa {lista_[1]} é invalida'
                    painel = Panel(prenel, expand=False, title='Pessoa(s)')
                    print(painel)
                    print(f'O total de pessoa(s) foi(ram) {len(lista)}')
        except sqlite3.Error:
            print('[red bold]Erro com o Banco de dados[/]')
        except Exception as erro:
            print(f'Algo deu errado {erro}')
#busca = input('Pesquise: ')

#try:
    #with sqlite3.connect('banco_dados.db') as banco:
        #c = banco.cursor()
        #c.execute('''#SELECT *
        # FROM amigos
        #WHERE nome LIKE ?''', (f'%{busca}%',))
        #'''lista = c.fetchall()
        #if len(lista).__eq__(0):
            #print('[red]Nenhum dado encontrado[/]')
        #else:
            #for c in lista:
                #lista_ = []
                #for p in c:
                    #lista_.append(p)
                #ano_atual = date.today()
                #pre_form = lista_[2].split('-')
                #p = pre_form
                #ano_de_nasce = date(int(p[0]),int(p[1]), int(p[2]) )
                #lista_[2] = int((ano_atual - ano_de_nasce).days/ 365.25)
                #print(lista_)
#except sqlite3.Error:
    #print('Erro com o Banco de dados')