import random

x = random.randint(3, 20)
n = 1
k = 2
list_ = []
for j in range(2, x):
    for i in range(1, x):
        if x % (n + k) == 0:
            list_.append(n)
            list_.append(k)
        k += 1
    n += 1
    k = n + 1
print('Случайное число = ', x)
print('Пароли: ', list_)

