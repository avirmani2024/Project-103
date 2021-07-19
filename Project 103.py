import pandas as pd
import plotly.express as px

x_coordinate = 'date'
y_coordinate = 'cases'
Color_Country = 'country'

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(df, x = x_coordinate, y = y_coordinate, color = Color_Country, size_max = 60)
fig.show()