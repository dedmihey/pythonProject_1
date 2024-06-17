def my_decor(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        for i in range(2, s + 1):
            if s % i == 0 and i == s:
                print('Сумма чисел - простое число')
            else:
                print('Сумма чисел - составное число')
                break
        return wrapper


@my_decor
def sum_three(a, b, c):
    return a + b + c
    # print(s)
    # return s


sum_three(4, 7, 14)
