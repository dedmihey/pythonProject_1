import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("Laptop-Price.csv")
print(df)
plt.figure(figsize=(12, 7))
sns.barplot(
    x='Company',
    y='Price_euros',
    hue='Cpu Brand',
    data=df
)
plt.xticks(rotation=90)
plt.show()

df = pd.read_csv("Customer.csv")
print('Таблица данных')
print(df)
print('Корреляционная матрица')
print(df.corr(method='pearson', numeric_only=True))

#plt.figure(figsize=(15, 7))
plot = sns.FacetGrid(df, col='region')
plot.map(plt.scatter, 'annual_income', 'purchase_amount')
plot.fig.set_size_inches(15, 7)
plt.show()

sns.violinplot(x='region', y='purchase_frequency', color='orange', data=df)
plt.show()

plt.figure(figsize=(15, 6))
sns.stripplot(x='region', y='purchase_frequency', color='green', data=df)
plt.show()

# df = pd.read_csv("nba.csv")
# print('Данные по игрокам NBA')
# print(df)

df = sns.load_dataset('penguins')

sns.catplot(data=df, x='island', y='bill_length_mm', kind='violin', hue='sex')
plt.show()