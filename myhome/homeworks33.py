def my_decor(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        for i in range(2, s):
            if s % i == 0:
                print('Сумма чисел - ', s, ' составное число')
                break
            if i == s - 1:
                print('Сумма чисел - ', s, 'простое число')

    return wrapper


@my_decor
def sum_three(a, b, c):
    return a + b + c


sum_three(3, 7, 3)
