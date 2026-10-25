from rich import print
from time import sleep


class Livro:
    def __init__(self,nome_do_livro:str, paginas:int):
        self.nome = nome_do_livro
        self.paginas = paginas
        self.ini = 1
        print(f'Você acobou de abrir o livro [red bold]{self.nome}[/] que tem [blue bold]{self.paginas} páginas[/] agora você está na [purple bold]página 1[/].')


    def avancar_paginas(self,avanca_pagina):
        if self.ini + avanca_pagina <= self.paginas:
            if avanca_pagina + self.ini > 0:
                sleep(0.5)
                if avanca_pagina >= 0:
                    for c in range(self.ini + 1, self.ini + avanca_pagina + 1):
                        print(f'Pág{c} :arrow_right: ', end='')
                        sleep(0.5)
                else:
                    for c in range(self.ini, self.ini + avanca_pagina -1,-1):
                        print(f'Pág{c} :arrow_right: ', end='')
                        sleep(0.5)
                self.ini = avanca_pagina+self.ini
                print(f'Você avançou {avanca_pagina} páginas e agora está na [purple]página {self.ini}[/].')
            else:
                print('[red bold]Não existe página nula e negativa[/]')
        else:
            sleep(0.5)
            for c in range(self.ini + 1, self.paginas + 1):
                print(f'Pág{c} :arrow_right: ', end='')
                sleep(0.5)
            self.ini = self.paginas
            print(f'Você avançou {self.paginas-self.ini} páginas e agora está na [purple]página {self.ini}[/].')
            print(f'[red]:book: Você chegou ao final do livro {self.nome}')


l1 = Livro('10 coisas que aprendi', 20)
for c in range(0,int(input('Quantos cometários você quer?: '))):
    l1.avancar_paginas(int(input('Quantas páginas deseja avançar?: ')))