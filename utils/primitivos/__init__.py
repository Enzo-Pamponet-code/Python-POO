def numero(num: object, conversor: object = True) -> int | float | str:
    if conversor:
        try:
            if float(num) == int(float(num)):
                return int(float(num))
            else:
                return float(num)
        except ValueError as e:
            return f'{e.with_traceback}'
    else:
        try:
            try:
                int(num)
                return int(num)
            except ValueError:
                return float(num)
        except ValueError as e:
            return f'{e.with_traceback}'