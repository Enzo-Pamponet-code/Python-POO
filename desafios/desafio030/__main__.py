from rich import inspect
from classes import *



c = Credencial()
c.senha = input('Digite a senha: ')
print(c.senha)
inspect(c, private=True, methods=True)