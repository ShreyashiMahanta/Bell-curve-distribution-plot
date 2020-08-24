import csv
import plotly.figure_factory as ff
import pandas as pd

dd = pd.read_csv('mobile.csv')
fig = ff.create_distplot([dd['Avg Rating'].tolist()],['Average rating'],show_hist = False,)
fig.show()