from rich import inspect
from classes import *


c = ContaBancaria(123, 'Manuel', 2000, 'terraplana')
c.sacar(2000, 'terraplana')
c.depositar(10)

inspect(c, methods=True, private=True)