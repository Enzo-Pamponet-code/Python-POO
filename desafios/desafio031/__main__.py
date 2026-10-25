from rich import inspect, print
from classes import *


r = Retangulo()
r.medidas = (1,5)
print(r.medidas)
inspect(r, private=True, methods=True)