def math_operation(oper):
    if oper == 'mult':
        def mult(a, b):
            return a * b

        return mult
    elif oper == 'div':
        def div(a, b):
            try:
                return a / b
            except ZeroDivisionError as e:
                print(f"Ошибка: {e}")

        return div


f_mult = math_operation('mult')
print(f_mult(5, 4))
f_div = math_operation('div')
print(f_div(4, 2))

square = lambda x: x ** 2
print(square(9))


def square(x):
    print(x ** 2)


square(9)


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return [self.a * self.b]


f_rect = Rect(6, 5)
print(f_rect())
