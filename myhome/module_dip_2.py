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

plt.figure(figsize=(15, 7))
plot = sns.FacetGrid(df, col='region')
#plt.figure(figsize=(15, 7))
plot.map(plt.scatter, 'annual_income', 'purchase_amount')
plt.show()

