from utils import formatado


#Declaração de Classe
class Gafanhoto:
    def __init__(self):
        # Atributos de instancia
        self.nome = ''
        self.idade = 0

    #Métodos de instancia
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'


#Declaração de Objeto
g1 = Gafanhoto() #esse é o instaciamento
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())


g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()
print(g2.mensagem())


g3 = Gafanhoto()
g3.nome = 'Enzo'
g3.idade = 15
g3.aniversario()
print(g3.mensagem())

formatado.print_('Orientado a objeto')
g4 = Gafanhoto()
g4.nome = input('Digite seu nome: ')
g4.idade = int(input('Digite sua idade: '))
print(g4.mensagem())