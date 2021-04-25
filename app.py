import plotly.figure_factory as px
import pandas as pd

df = pd.read_csv("csv/data.csv")

data = df["Avg Rating"].tolist()


fig = px.create_distplot([data], ["Rating"], show_hist=False)
fig.show()
