import sqlite3

busca = input('Quem você está procurando?').strip()
try:
    with sqlite3.connect('meu banco.db') as banco:
        banco.row_factory = sqlite3.Row
        curso = banco.cursor()
        curso.execute('SELECT * FROM amigos WHERE nome LIKE ?', (f'%{busca}%',))
        #lista = curso.fetchall()
        #print(lista)
        for amigo in curso:
            print(f'{amigo['nome']} nasceu no ano {amigo['nascimento']}')
except sqlite3.Error as erro:
    print(f'falha no banco: {erro}')
except Exception as erro:
    print((f'Algo deu errado {erro}'))
