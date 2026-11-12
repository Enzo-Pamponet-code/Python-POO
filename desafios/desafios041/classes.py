import sqlite3
from rich import print

busca = input('Pesquise: ')

try:
    with sqlite3.connect('banco_dados.db') as banco:
        c = banco.cursor()
        c.execute('''SELECT *
        FROM amigos
        WHERE nome LIKE ?''', (f'%{busca}%',))
        lista = c.fetchall()
        if len(lista).__eq__(0):
            print('[red]Nenhum dado encontrado[/]')
        else:
            
except sqlite3.Error:
    print('Erro com o Banco de dados')