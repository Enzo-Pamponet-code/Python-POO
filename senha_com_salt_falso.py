from getpass import getpass
from hashlib import sha256


# ScSF
class ScSF:
    def __init__(self):
        self.__salt_hash = sha256((sha256(getpass('Digite seu nome: ', echo_char='*').encode()).hexdigest() + sha256(getpass('Digite sua senha: ', echo_char='*').encode()).hexdigest()).encode()).hexdigest()
        print(self.__salt_hash)


c = ScSF()
