from rich import print


class Funcionario:
    #Atributos de classe
    empresa = 'Curso em Vídeo'
    def __init__(self, nome, setor, cargo ):
        #Atributos
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentar(self):
        return f'olá :hand:, meu nome é [red bold]{self.nome}[/]:graduation_cap:, eu sou [bold purple]{self.cargo}[/]:sunglasses: do setor de [bold blue]{self.setor}[/] da empresa {Funcionario.empresa}.'


funcionario = Funcionario('Enzo', 'TI', 'Programador')
print(funcionario.apresentar())
funcionario2 = Funcionario('Maria', 'Administração', 'Diretora')
funcionario2.__class__.empresa = 'Njr'
print(funcionario2.apresentar())