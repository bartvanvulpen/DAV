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
from pylab import figure, axes, pie, title, show
plotly.tools.set_credentials_file(username='BartvanVulpen', api_key='f6VVqnMdHc9sa7KWDJMq')
print("Starting reading data...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')

import plotly.plotly as py
from plotly.grid_objs import Grid, Column
from plotly.tools import FigureFactory as FF
import time

dictio ={'California': 1,
'Texas': 1,
'Florida':0,
'New York': 0,
'Illinois':0,
'Pennsylvania':0,
'Ohio':0,
'Georgia':0,
'North Carolina':0,
'Michigan':0,
'New Jersey':0,
'Virginia':0,
'Washington':1,
'Arizona':1,
'Massachusetts':0,
'Indiana':0,
'Tennessee':0,
'Missouri':0,
'Maryland':0,
'Wisconsin':0,
'Minnesota':0,
'Colorado':1,
'South Carolina':0,
'Alabama':0,
'Louisiana':0,
'Kentucky':0,
'Oregon':1,
'Oklahoma':1,
'Connecticut':0,
'Iowa':0,
'Utah':1,
'Mississippi':0,
'Arkansas':0,
'Kansas':1,
'Nevada':1,
'New Mexico':1,
'Nebraska':1,
'West Virginia':0,
'Idaho':1,
'Hawaii':1,
'New Hampshire':0,
'Maine':0,
'Rhode Island':0,
'Montana':1,
'Delaware':0,
'South Dakota':1,
'North Dakota':1,
'Alaska':1,
'Vermont':0,
'Wyoming':1,
'District of Columbia': 0}


#-----Algorithm to get data in right structure for time_slider------

print("Structuring data for time slider...")
data2 = pd.DataFrame(list(dictio.items()), columns=['state_name', 'state_population'])
#data = data.drop(data.index[10000:239399])
slider_data = pd.DataFrame(columns=('state', 'side', 'month', 'n_incidents', 'n_teens', 'n_children', 'n_male', 'n_female','n_killed', 'n_injured', "suicide", "robbery", "drug_involvement", 'accidental'))

for date in range(1401, 1804):
    print(date)
    if date > 1412 and date < 1501:
        continue
    if date > 1512 and date < 1601:
        continue
    if date > 1612 and date < 1701:
        continue
    if date > 1712 and date < 1801:
        continue

    select_data = data[data['date'] == date]
    for state1 in data2['state_name']:
        select_data = data[data['date'] == date]
        select_data = select_data[select_data['state'] == state1]
        month = date
        state = state1
        n_killed = sum(select_data['n_killed'])
        n_male = sum(select_data['male'])
        n_female = sum(select_data['female'])
        n_injured = sum(select_data['n_injured'])
        suicide = sum(select_data['suicide'])
        robbery = sum(select_data['robbery'])
        teens = sum(select_data['teens_involved'])
        children = sum(select_data['children_involved'])
        n_incidents = len(select_data)
        if dictio[state1] == 1:
            side = 'West'
        else:
            side = 'East'
        drug_involvement = sum(select_data['drug_involvement'])
        accidental = sum(select_data['accidental'])
        list = [state, side, month, n_incidents,teens, children, n_male, n_female, n_killed, n_injured, suicide, robbery, drug_involvement, accidental]
        slider_data.loc[slider_data.shape[0]] = list
slider_data = slider_data.sort_values(['state', 'month'])
print(slider_data)
print("Done.")


print("Structuring successful!")
print("Writing output to .xlsx file...")
# write processed dataframe to Excel testing sheet
writer = ExcelWriter('datasets/slider_data.xlsx')
slider_data.to_excel(writer,'testingsheet')
writer.save()
print("Output written to .xlsx file!")
