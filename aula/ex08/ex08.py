class ContaBancaria:
    """
    Cria um conta Bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f'Conta criada {self.id} criada com sucesso.')


    def __str__(self):
        formatado = f'{self.__saldo:.2f}'.replace('.', ',')
        #return f'A conta {self.id} de {self._titular} tem saldo R${formatado} de saldo'
        return f'Estado atuado da conta: {self.__dict__}'


    def deposito(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Deposito de R${valor:.2f} autorizado na conta {self.id}')


    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'\033[31mSaque negado na conta {self.id}\033[m')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')