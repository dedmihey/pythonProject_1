def square(x):
    return x ** 2


def odd_num(x):
    return x % 2


list_1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = list(map(square, list_1))
result_1 = filter(odd_num, result)
print(list(result_1))
