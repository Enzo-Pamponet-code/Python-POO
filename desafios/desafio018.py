from rich.panel import Panel
from rich import print


class Churrasco:
    def __init__(self,nome, total_pessoas):
        self.nome = nome
        self.total = total_pessoas
        self.q_carne = 0.4
        self.custo = 82.4
        self.custo_total = float(self.custo*self.q_carne*self.total)
        self.carne_total = float(self.total*self.q_carne)


    def analisar(self):
        painel = Panel(f'Analizando o [green]{self.nome}[/] com [blue bold]{self.total} convidados[/]\nCada participante comerá 0.4kg e cda kg custa R$82,40\nRecomendo [blue]comprar {self.carne_total:.2f}kg[/]\nO custo total será de [purple]R${self.custo_total:.2f}[/].\nCada pessoa pagará [yellow]R${float(self.custo_total/self.total):.2f} para participar', title=self.nome)
        print(painel)


test = Churrasco('Churrasco Pamponet', 15)
test.analisar()