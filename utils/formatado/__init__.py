def print_(word, digit = '-', num_digits = 60):
    print(digit*num_digits)
    print(f'{word:^{num_digits}}')
    print(digit*num_digits)