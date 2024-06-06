class InvalidInterval(Exception):
    pass


class InvalidType(Exception):
    pass


def f_1(a):
    print('Возведение в квадрат целого числа в интервале от 5 до 20 ')
    if isinstance(a, int):
        pass
    else:
        raise InvalidType("Тип данных противоречит условию")
    if 5 < a < 20:
        b = a ** 2
    else:
        raise InvalidInterval("Введённое число вне заданного интервала")

    return b


try:
    result = f_1('cucu')
    print(result)
except InvalidType as e:
    print(f'Ошибка: {e}')
except InvalidInterval as e:
    print(f'Ошибка: {e}')
