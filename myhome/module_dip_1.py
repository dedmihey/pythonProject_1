import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Пример построения линейных графиков

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

# Пример построения столбчатой диаграммы

x = ['p1', 'p2', 'p3', 'p4', 'p5']
y = [2, 6, 3, 6, 9]
plt.bar(x, y)
plt.title('Пример столбчатой диаграммы')
plt.show()

# Распределение электромобилей по некоторым округам штата Вашингтон.

a = ['Pierce', 'San Juan', 'Skagit', 'Skamania', 'Snohomish', 'Spokane', 'Stevens', 'Thurston',
     'Wahkiakum', 'Walla Walla', 'Whatcom', 'Whitman', 'Yakima']
b = [16197, 1036, 2266, 214, 24721, 5460, 249, 7526, 70, 524, 4978, 397, 1225]

state = {'Округ': a,
         'Число электромобилей': b}

df = pd.DataFrame(state)
print(df)
plt.figure(figsize=(9, 9))

plt.subplot(1, 2, 1)
plt.plot(a, b, 'o-y')
plt.xticks(rotation=90)
plt.ylabel('Число электромобилей')
plt.title('Число электромобилей по округам штата Вашингтон', loc='left')

plt.subplot(1, 2, 2)
plt.xticks(rotation=90)
plt.bar(a, b, color='r')
plt.show()

# Покажем распределение электромобилей по другим округам штата Вашингтон с
# помощью круговой диаграммы.

county = ['Grays Harbor', 'Island', 'Jefferson', 'Kittitas', 'Klickitat',
          'Lewis', 'Lincoln', 'Mason', 'Okanogan', 'Pacific', 'Pend Oreille']
cnt = [753, 2206, 1114, 761, 341, 930, 59, 947, 316, 246, 63]
fig, ax = plt.subplots(figsize=(8, 8))
explode = (0, 0.1, 0, 0, 0, 0, 0.15, 0, 0, 0, 0)
ax.pie(cnt, labels=county, explode=explode)
ax.axis('equal')
plt.title('Число электромобилей по округам штата Вашингтон', loc='center')
plt.show()

# Несколько графиков в одном поле с использованием subplots()

x = np.linspace(0, 2 * np.pi, 400)
y1 = np.sin(x)
y2 = np.sin(x ** 2)
y3 = y1 ** 2
y4 = y2 ** 2

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 9))
ax[0, 0].plot(x, y1, c='red')
ax[0, 1].plot(x, y2, c='red')
ax[1, 0].plot(x, y3, c='blue')
ax[1, 1].plot(x, y3, c='blue')

ax[0, 0].set_title('Линейный график sin(x)')
ax[0, 1].set_title('Линейный график sin(x**2)')
ax[1, 0].set_title('Линейный график sin(x)**2')
ax[1, 1].set_title('Линейный график sin(x**2)**2')

fig.suptitle('Подсюжеты в двух направлениях')
plt.show()

# Графики разных типов на одном поле с использованием subplots()
# Исходные данные для линейных графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Исходные данные для столбчатой диаграммы
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 1, 5]

# Исходные данные для круговой диаграммы
labels = ['Category 1', 'Category 2', 'Category 3']
sizes = [30, 40, 30]

# Ещё пара линейных графиков
x_custom = np.linspace(0, 5, 50)
y3 = x_custom ** 2
y4 = np.exp(x_custom)

# Создание сетки графиков
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))

axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].set_title('Линейный 1')
axes[0, 0].legend()

axes[0, 1].plot(x, y2, label='cos(x)', color='orange')
axes[0, 1].set_title('Линейный 2')
axes[0, 1].legend()

axes[0, 2].bar(categories, values, color='green')
axes[0, 2].set_title('Столбчатая диаграмма')

axes[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'yellow', 'green'])
axes[1, 0].set_title('Круговая диаграмма')

axes[1, 1].plot(x_custom, y3, label='x^2', color='purple')
axes[1, 1].set_title('Линейный 3')
axes[1, 1].legend()

axes[1, 2].plot(x_custom, y4, label='e^x', color='brown')
axes[1, 2].set_title('Линейный 4')
axes[1, 2].legend()

plt.tight_layout()

plt.show()
