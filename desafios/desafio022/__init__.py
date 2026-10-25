import traceback

from rich import inspect


def identificador(begin,end, number_mark, mark_color = 'yellow'):
    string_vazia = ''
    for c in range(begin, end):
        if c == number_mark:
            string_vazia += f'[on {mark_color}] {c} [/]'
        else:
            string_vazia += f' {c} '
    string_cheia = string_vazia
    return string_cheia




