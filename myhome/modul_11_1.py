import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y1 = x
y2 = x ** 2
plt.title('Первый график')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.grid()
plt.plot(x, y1, 'r--', label='y = x')
plt.plot(x, y2, label='y = x^2')
plt.legend()
plt.show()

x = ['p1', 'p2', 'p3', 'p4', 'p5']
y = [2, 6, 3, 6, 9]
plt.bar(x, y)
plt.title('Пример столбчатой диаграммы')
plt.show()
