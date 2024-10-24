import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

x = np.arange(0, 5, 0.1)


def f(x):
    return x ** 2


fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=f(x), name='$$y=x^2$$'))
fig.add_trace(go.Scatter(x=x, y=x, name='$$y=x$$'))
fig.update_layout(legend_orientation='h',
                  legend=dict(x=0.4, xanchor='center'),
                  title='Линейные графики y=x^2, y=x',
                  xaxis_title='Ось х',
                  yaxis_title='Ось y'
                  )
fig.show()


df = pd.read_csv("nba.csv")
print('Данные по игрокам NBA')
print(df)

fig = px.scatter_3d(df, x='Team', y='Height', z='Salary')
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(x=[x[0]], y=[f(x)[0]], mode='lines+markers',  name='f(x)=x<sup>2</sup>'))

frames=[]
for i in range(1, len(x)):
    frames.append(go.Frame(data=[go.Scatter(x=x[:i+1], y=f(x[:i+1]))]))

fig.frames = frames

fig.update_layout(legend_orientation="h",
                  legend=dict(x=.5, xanchor="center"),
                  updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])],
                  margin=dict(l=0, r=0, t=0, b=0))
fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
fig.show()


feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

# Создаём 2-D сетку по координатам
[X, Y] = np.meshgrid(feature_x, feature_y)

Z = np.cos(X / 2) + np.sin(Y / 4)

# Рисуем картинку
fig = go.Figure(data=
                go.Heatmap(x=feature_x, y=feature_y, z=Z, ))
fig.update_layout( title='Тепловая диаграмма',
                  xaxis_title='Ось х',
                  yaxis_title='Ось y')
fig.show()

