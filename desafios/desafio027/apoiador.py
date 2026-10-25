from classes import *
from test_adv import barra
from rich import print
from test_adv import hp_bar

def ataque(alvo, forca,nome_do_personagem, socos:list, dicionario_de_personagens_atacados:dict, vida_do_proprio_personagem):
    vida = vida_do_proprio_personagem
    dicionario = dicionario_de_personagens_atacados
    nome = nome_do_personagem
    classe_name = alvo.__class__.__name__
    if classe_name == 'Guerreiro' or classe_name == 'Mago':
        if vida > 0 and alvo.vida > 0:
            if nome != alvo.nome:
                soco = socos[randint(0, len(socos) - 1)]
                dano_real = randint(0, int(float(forca)))
                print(f'[blue]{nome}[/] deu um [red bold]{soco}[/] com dano de [purple]{dano_real}[/] em [turquoise2]{alvo.nome}[/] com [spring_green3]{forca} de força[/].')
                alvo.receber_dano(alvo, dano_real)
                if alvo.vida == 0:
                    print(f'[red bold]{alvo.nome} está Morto![/]')
        else:
            if alvo.vida == 0:
                print(f'[red bold]{alvo.nome} está Morto[/]')



def receber_ataque(alvo,dicionario_de_personagens_atacados:dict , dano_real):
    classe_name = alvo.__class__.__name__
    dicionario = dicionario_de_personagens_atacados
    if classe_name in dicionario:
        vida = dicionario[classe_name]
    else:
        dicionario[classe_name] = alvo.vida
        vida = dicionario[classe_name]
    alvo.vida -= dano_real
    if alvo.vida <= 0:
        alvo.vida = 0
    hp_bar(alvo.nome, alvo.vida, vida)


