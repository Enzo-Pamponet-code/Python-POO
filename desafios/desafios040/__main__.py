from classes import *
from rich import print_json, inspect

u = [Usuario('Enzo', 'neymar2314@gmail.com'),
     Usuario('Grazi', 'grazinha@gmail.com')]
b = [Aluno('Enzo', 'programação', '1 ano')]

exportar_dados(XML(), u)
exportar_dados(JSON(), b)