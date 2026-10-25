def classi(num:int):
    match num:
        case 0:
            return 'caso 1'
        case 1:
            return 'caso 2'
        case 2:
            return 'caso 3'
        case _:
            return 'caso não classificado'


def classi_if(num:int):
    if num == 0:
        return 'caso 1'
    elif num == 1:
        return 'caso 2'
    elif num == 2:
        return 'caso 3'
    else:
        return 'caso não classificado'


print(classi(10))
print(classi_if(10))