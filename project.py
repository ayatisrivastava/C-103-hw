import pandas as pd
import plotly.express as px

df = pd.read_csv("xcel.csv")
fig = px.scatter(df, x="date", y="country",size="cases",color="Country")
fig.show()
