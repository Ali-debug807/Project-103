import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.line(df, x = "Year", y = "Per capita income", labels = "Country")
fig.show()