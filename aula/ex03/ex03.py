class ContaBancaria:
    """
    Cria um conta Bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta criada {self.id} crianda com sucesso. saldo')


    def __str__(self):
        formatado = f'{self.saldo:.2f}'.replace('.', ',')
        return f'A conta {self.id} de {self.titular} tem saldo R${formatado} de saldo'


    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:.2f} autorizado na conta {self.id}')


    def sacar(self, valor):
        if valor > self.saldo:
            print(f'\033[31mSaque negado na conta {self.id}\033[m')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')


c1 = ContaBancaria(17, 'Enzo', 4000)
c1.deposito(500)
c1.sacar(2000000)
print(c1)