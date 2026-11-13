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
                            pre_form = lista_[2].split('-')
                            p = pre_form
                            ano_de_nasce = date(int(p[0]), int(p[1]), int(p[2]))
                            lista_.append(str(int((ano_atual - ano_de_nasce).days / 365.25))+' anos')
                            stri = '[blue]'
                            for w in pre_form[::-1]:
                                if pre_form.index(w) == 0:
                                    stri += w
                                else:
                                    stri += f'{w}/'
                            lista_[2] = f'{stri}[/]'
                            prenel += f'{lista_}\n'
                        except AttributeError:
                            prenel += f'[red]{lista_[0]}. Esse dado é invalido[/]'
                    painel = Panel(prenel, expand=False, title='Pessoa(s)')
                    print(painel)
        except sqlite3.Error:
            print('Erro com o Banco de dados')
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