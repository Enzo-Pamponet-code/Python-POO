class Porta:
    def abrir(self):
        print('Empurre a maçaneta para baixo e empurre/puxe a porta.')
class Empresa:
    def abrir(self):
        print('Faça as documentações e leve para o lugar necessário para fazer o CNPJ')
class Ovo:
    def abrir(self):
        print('Quebre e coloque na frigideira.')
class Pedra:
    pass


def tente_abrir(objeto):
    try:
        a = objeto.abrir()
        return a
    except:
        print(f'O objeto {objeto.__class__.__name__} não tem como abrir')