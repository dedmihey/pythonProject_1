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
fig.add_trace(go.Scatter(x=x, y=f(x)))
fig.add_trace(go.Scatter(x=x, y=x))
fig.show()

df = pd.read_csv("nba.csv")
print('Данные по игрокам NBA')
print(df)


