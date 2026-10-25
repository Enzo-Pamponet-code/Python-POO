from rich.panel import Panel
from rich.traceback import install
from rich import print


class Produto:
    def __init__(self, nome:str, preco:str):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        conteudo = f'''[blue]{self.nome.center(30," ")}[/]
{"-"*30}
[yellow]{self.preco.center(30, ".")}[/]'''
        painel = Panel(conteudo, title='Produto', expand=False)
        print(painel)


install()
redmi = Produto('Redmi note 9', '1000')
redmi.etiqueta()