def add_everything_up(a, b):
    try:
        c = a + b

    except TypeError as exc:
        print(exc)
        if type(a) == str and type(b) != str:
            c = a + str(b)
        if type(b) == str and type(a) != str:
            c = str(a) + b
    return c


print(add_everything_up(4, '5'))
print(add_everything_up('cucu', 'haha'))
print(add_everything_up(32, 51))
print(add_everything_up(5.4, 5))
