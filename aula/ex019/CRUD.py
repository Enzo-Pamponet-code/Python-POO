from rich.panel import Panel
from rich import print
import sqlite3



def continuar():
    continuar = input('Não encontramos só uma pessoa, deseja tentar novamente [S/N]:\n')
    if continuar == 'Nn':
        return False
    return True


def buscar(prompt):
    busca = acesso_banco('''SELECT *
    FROM pessoas
    WHERE nome LIKE ?''', (f'%{prompt}%',))
    return busca
def contador_fetchall(fetchall):
    total = 0
    for total in fetchall:
        total += 1
    return total


def tabular(string, numeric:int):
    string = f'{string}'
    space = ' '*(numeric - len(string))
    return string+space

def mtabular(prompt:tuple, numeric:int):
    string = ''
    for c in prompt:
        string +=tabular(c,numeric)
    return string


def acesso_banco(program, busca=None):
    with sqlite3.connect('cadastro.db') as sql:
        cursor = sql.cursor()
        if busca is None:
            cursor.execute(program)
            return cursor
        else:
            cursor.execute(program, busca)
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
            dados_to_panel = f'{mtabular(('cod','nome','altura'), 25)}\n'
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
                system(2)
                nome = input('Digite o nome da pessoa que você deseja atualizar: ')
                acessando = buscar(nome)
                salvar = acessando.fetchall()
                if len(salvar) != 1:
                    if not continuar():
                        break
                else:
                    string = f'{mtabular(('cod','nome','altura'), 20)}\n'
                    for c in salvar:
                        for p in c:
                            string += tabular(p, 20)
                    painel = Panel(string, title='Pessoa', expand=False)
                    print(painel)
                    nome = input('Digite o nome da pessoa: ')
                    while True:
                        try:
                            altura = float(input('Digite a altura da pessoa: '))
                            break
                        except ValueError:
                            print('[red bold]Valor invalido[/]')
                    c = salvar[0][0]
                    acesso_banco('''UPDATE pessoas
                    SET nome = ?, altura =?
                    WHERE cod = ?''', (nome, altura,c))
                input()
                break
            #-----------------------------opção 4-------------------------------
        elif opcao == 4:
            system(2)
            while True:
                try:
                    pessoa = input('Escreva o nome da pessoa que deseja [red]excluir[/]: ')
                    resultado = buscar(pessoa).fetchall()
                    if len(resultado) != 1:
                        print('Nós não encontramos só um resultado :(')
                        if not continuar():
                            break
                    else:
                        acesso_banco('''DELETE FROM pessoas
                        WHERE nome LIKE ?''', (f'%{resultado[0][1]}%',))
                        break
                except:
                    print('Erro')
        #---------------------------------opção 5------------------------------------
        elif opcao == 5:
            print('\n'*30)
            lista = buscar(input('Digite o nome da pessoa que você quer encontrar: ')).fetchall()
            string = f'{mtabular(('cod', 'nome', 'altura'), 20)}\n'
            for c in lista:
                for p in c:
                    string += tabular(p, 20)
            painel = Panel(string, title='Pessoa', expand=False)
            print(painel)
            input('Aperte ENTER')
        #--------------------------------opção 6---------------------------------------------------
        elif opcao == 6:
            return True


    except Exception as erro:
        print(erro)


while True:
    public_interface()
    sistema = input_('Escolha uma opção: ')
    sair = system(sistema)
    if sair:
        print('[blue]Volte sempre[/]')
        break
    print('\n'*30)
