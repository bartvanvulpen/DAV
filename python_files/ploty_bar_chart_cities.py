import sys
import pandas as pd
import numpy as np
import plotly.plotly as py
import matplotlib.pyplot as plt
import zipfile
import sys
import plotly
from sklearn import preprocessing
import math
from pandas import ExcelWriter
import re
from pandas import ExcelFile
from geopy import geocoders
import time
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
import plotly.graph_objs as go
from pylab import figure, axes, pie, title, show
plotly.tools.set_credentials_file(username='BartvanVulpen', api_key='f6VVqnMdHc9sa7KWDJMq')
print("Starting reading data...")
data = pd.read_excel('datasets/city_data.xlsx')
data = data.sort_index()
# trace1 = go.Bar(
#     x= data['city'],
#     y= data['robbery'],
#     name='Robbery'
# )
# trace2 = go.Bar(
#     x= data['city'],
#     y= data['drug_involvement'],
#     name='Drug involvement'
# )
#
# trace3 = go.Bar(
#     x= data['city'],
#     y= data['accidental'],
#     name='Accidental'
# )
# trace4 = go.Bar(
#     x= data['city'],
#     y= data['suicide'],
#     name='Suicide'
# )
# trace5 = go.Bar(
#     x= data['city'],
#     y= data['gang_involvement'],
#     name='Gang involvement'
# )
# trace6 = go.Bar(
#     x= data['city'],
#     y= data['officer_involved'],
#     name='Officer involved'
# )
# trace7 = go.Bar(
#     x= data['city'],
#     y= data['domestic_violence'],
#     name='Domestic violence'
# )
#
# data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]
# layout = go.Layout(
#     barmode='group'
# )
#
# fig = go.Figure(data=data, layout=layout)
# py.iplot(fig, filename='grouped-bar')


trace1 = go.Bar(
    x= data['city'],
    y= data['n_injured'],
    name='People killed'
)
trace2 = go.Bar(
    x= data['city'],
    y= data['n_killed'],
    name='People injured'
)

trace3 = go.Bar(
    x= data['city'],
    y= data['n_incidents'],
    name='Number of incidents'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stack')
