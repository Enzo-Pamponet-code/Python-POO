from rich import print
from rich.table import Table


tabela = Table(title='Tabela de preço')

tabela.add_column('Nome')
tabela.add_column('Preço')
tabela.add_column('neymar')
tabela.add_row('lapis','R$1,50', 'True')
tabela.add_row('Borracha', 'R$3,50', 'False')

print(tabela)