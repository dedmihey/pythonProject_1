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
          'Lewis', 'Lincoln','Mason', 'Okanogan', 'Pacific', 'Pend Oreille']
cnt = [753, 2206, 1114, 761, 341, 930, 59, 947, 316, 246, 63]
fig, ax = plt.subplots(figsize=(8, 8))
explode = (0, 0.1, 0, 0, 0, 0, 0.15, 0, 0, 0, 0)
ax.pie(cnt, labels=county, explode=explode)
ax.axis('equal')
plt.title('Число электромобилей по округам штата Вашингтон', loc='center')
plt.show()