from numpy import histogram
import plotly.figure_factory as pff
import pandas as pd

df = pd.read_csv("data.csv")
fig = pff.create_distplot([df["Height(Inches)"].tolist()], ["Height"], show_hist = True)
fig.show()