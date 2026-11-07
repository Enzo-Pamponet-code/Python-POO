from desafios.desafios036.classes import convesor


class Carrinho:
    def __init__(self):
        self.produtos = []

    def __add__(self, other):
        if type(other) == Produto:
            dici = {other.nome:other.preco}
            self.produtos.append(dici)
            return self
        else:
            try:
                for c in other.produtos:
                    self.produtos.append(c)
            except AttributeError:
                dici = {other.nome: other.preco}
                self.produtos.append(dici)
            return self

    def __iadd__(self, other:Produto):
        self.__add__(other)
        return self

    def __str__(self) -> str:
        conteudo = ''
        for c in self.produtos:
            k = None
            v = 0
            for l in c.keys(): k = l
            for l in c.values(): v = l
            conteudo += '-'*30
            conteudo += f'\n{k} ({convesor(v)})\n'
            conteudo += '-'*30
        conteudo += f'\ntotal: {convesor(self.total)}'
        return conteudo

    @property
    def total(self):
        tot = 0
        for c in self.produtos:
            for l in c.values(): tot += l
        return tot

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f'{self.nome} (R$ {convesor(self.preco)})'

    def __add__(self, other):
        c = Carrinho()
        c += self
        c += other
        return c