import sqlite3

busca = input('Quem você está procurando?').strip()
try:
    with sqlite3.connect('meu banco.db') as banco:
        banco.row_factory = sqlite3.Row
        curso = banco.cursor()
        curso.execute('SELECT * FROM amigos WHERE nome LIKE ?', (f'%{busca}%',))
        #lista = curso.fetchall()
        #print(lista)
        total =0
        for total, amigo in enumerate(curso, start=1):
            print(f'{amigo['nome']} nasceu no ano {amigo['nascimento']}')
        print(f'Ao todo encontrei {total} amigos com "{busca}"')
except sqlite3.Error as erro:
    print(f'falha no banco: {erro}')
except Exception as erro:
    print((f'Algo deu errado {erro}'))
