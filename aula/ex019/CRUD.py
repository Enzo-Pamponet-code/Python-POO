from rich.panel import Panel
from rich import print
import sqlite3



def contador_fetchall(fetchall):
    total = 0
    for c in fetchall:
        total += 1
    return total


def tabular(string, numeric:int):
    string = f'{string}'
    space = ' '*(numeric - len(string))
    return string+space


def acesso_banco(program, buscar=None):
    with sqlite3.connect('cadastro.db') as sql:
        cursor = sql.cursor()
        if buscar is None:
            cursor.execute(program)
            return cursor
        else:
            cursor.execute(program, buscar)
            return cursor


def number(numbe):
    return f'[yellow]{numbe}-[/]'


def public_interface():
    string = f'''{"="*60}
[yellow]{"SISTEMA DE CADASTRO":^60}[/]
{"="*60}
{number(1)} Cadastrar novas pessoas
{number(2)} listar pessoas
{number(3)} Atualizar pessoa
{number(4)} Excluir pessoa
{number(5)} Busca por nome
{number(6)} Sair'''
    painel = Panel(string, expand=False)
    print(painel)

def input_(string):
    while True:
        opcao = input(string)
        try:
            if 1<= int(opcao) <= 6:
                return int(opcao)
            print('[red]Fora dos limites[/]')
        except ValueError:
            print('[red]Valor invalido[/]')

def system(opcao):
    try:
        #----------------------------------------------opção 1--------------------------------------------------------------------
        if opcao == 1:
            nome = input('Digite o nome da pessoa:')
            while True:
                altura = input('Digite a altura dessa pessoa (Em metros):')
                try:
                    if 0.45 <= float(altura) <= 2.60:
                        altura = float(altura)
                        break
                except ValueError:
                    print('[red]Valor incorreto.[/]')
            acesso_banco(f'''INSERT INTO pessoas
(nome, altura)
VALUES 
    ("{nome}","{altura}");''')
        #-----------------------------------------opção 2------------------------------------------------------------------
        elif opcao == 2:
            print('\n'*30)
            dados_to_panel = f'{tabular("cod", 25)}{tabular("nome",25)}{tabular("altura",25)}\n'
            for microdados in acesso_banco('''SELECT *
FROM pessoas'''):
                for c in microdados:
                    dados_to_panel += f'{tabular(c, 25)}'
                dados_to_panel += '\n'
            painel = Panel(dados_to_panel, title='Pessoas', expand=False)
            print(painel)
            input('Aperte ENTER para continuar:')
        #---------------------------------------------opção 3---------------------------------------------
        elif opcao == 3:
            print('\n'*30)
            while True:
                escolher = input('Qual é nome da pessoa que você quer atualizar?: ')
                acessando = acesso_banco('''SELECT * FROM pessoas
WHERE nome LIKE ?''', buscar=(f'%{escolher}%',))
                salvar = acessando.fetchall()
                print(salvar)
                if len(salvar) != 1:
                    continuar = input('Não encontramos só uma pessoa, deseja tentar novamente [S/N]:\n')
                    if continuar == 'Nn':
                        break
                else:
                    string = f'{tabular('cod', 20)}{tabular("nome", 20)}{tabular("altura", 20)}\n'
                    for c in salvar:
                        for p in c:
                            string += tabular(p, 20)
                    painel = Panel(string, title='Pessoa', expand=False)
                    print(painel)
                input()

    except Exception as erro:
        print(erro)


while True:
    public_interface()
    sistema = input_('Escolha uma opção: ')
    system(sistema)
    print('\n'*30)
