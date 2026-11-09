from abc import ABC
import re


class Validador(ABC):
    def validar(self, string):
        pass


class Usuario(Validador):
    def validar(self, string):
        if 5 <= len(string) <= 20:
            try:
                re.search('[a-z]', string).span()
                if  len(re.findall('[A-Z]', string)):
                    raise ValueError
                for c in re.findall('[^a-z0-9]', string):
                    if c != '_':
                        raise ValueError
                return True
            except AttributeError:
                return False
            except ValueError:
                return False
        else:
            return False


class Email(Validador):
    def validar(self, string):
        try:
            if len(re.findall('@', string)) != 1:
                raise AttributeError
            re.search('[.][a-z][a-z]+', string).span()
            for c in string:
                if c.isspace():
                    raise AttributeError
            return True
        except AttributeError:
            return False


class Senha(Validador):
    def validar(self, string):
        if len(string) >= 8:
            try:
                re.search('[a-z]', string).span()
                re.search('[A-Z]', string).span()
                re.search('[^a-zA-z0-9]', string).span()
                return True
            except AttributeError:
                return False
        else:
            return False


def validar_dado(validador:Validador, valor):
    a = validador.validar(valor)
    if a:
        print(f'valor: {valor} é valido? SIM')
    else:
        print(f'valor: {valor} é valido? NÃO')