from rich import print, layout
from rich import inspect
from rich.panel import Panel
from rich.traceback import install


install()
preco = '1000'
nome = 'Redmi'
total = f'{nome}\n{'_'*8}\n{preco}'
painel = Panel(total,title='Produto',expand=False)
print(painel)
