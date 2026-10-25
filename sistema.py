from sys import *

stdout.write('ex')
print()



def print(string:str|int|float|list|tuple|dict|input|print = ''):
    stdout.write(f'{string}\n')



print(2.5)
print((1,2,3,4))