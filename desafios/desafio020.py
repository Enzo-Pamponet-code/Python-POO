from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome: str, nick: str) -> None:
        self.nome = nome
        self.nick = nick
        self.lista = []


    def add_favoritos(self, nome: str) -> None:
        self.lista.append(nome)


    def ficha(self)->None:
        self.lista = sorted(self.lista)
        coisa = f'Nome real: [on blue]{self.nome}[/]\nJogos favoritos:'
        for c in self.lista:
            coisa += f'\n[blue]:video_game: {c}[/]'
        painel = Panel(coisa, title=f'jogador <{self.nick}>')
        print(painel)


j: Gamer = Gamer('Enzo','neymar123')
j.add_favoritos('Mario')
j.add_favoritos('Clash Royale')
j.ficha()