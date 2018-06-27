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
import pandas as pd

dictio ={'California': 39144818,
'Texas': 27469114,
'Florida':20271272,
'New York': 19795791,
'Illinois':12859995,
'Pennsylvania':12802503,
'Ohio':11613423,
'Georgia':10214860,
'North Carolina':10042802,
'Michigan':9922576,
'New Jersey':8958013,
'Virginia':8382993,
'Washington':7170351,
'Arizona':6828065,
'Massachusetts':6794422,
'Indiana':6619680,
'Tennessee':6600299,
'Missouri':6083672,
'Maryland':6006401,
'Wisconsin':5771337,
'Minnesota':5489594,
'Colorado':5456574,
'South Carolina':4896146,
'Alabama':4858979,
'Louisiana':4670724,
'Kentucky':4425092,
'Oregon':4028977,
'Oklahoma':3911338,
'Connecticut':3590886,
'Iowa':3123899,
'Utah':2995919,
'Mississippi':2992333,
'Arkansas':2978204,
'Kansas':2911641,
'Nevada':2890845,
'New Mexico':2085109,
'Nebraska':1896190,
'West Virginia':1844128,
'Idaho':1654930,
'Hawaii':1431603,
'New Hampshire':1330608,
'Maine':1329328,
'Rhode Island':1056298,
'Montana':1032949,
'Delaware':945934,
'South Dakota':858469,
'North Dakota':756927,
'Alaska':738432,
'Vermont':626042,
'Wyoming':586107,
'District of Columbia': 693972}


statename_to_abbr = {
    # Other
    'District of Columbia': 'DC',

    # States
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY',
}

# --------Making separate dataframe for pyplot map-------------


data2 = pd.DataFrame(list(dictio.items()), columns=['state_name', 'state_population'])
data2['state_code']= ''
for index,state in data2['state_name'].iteritems():
    for state2 in statename_to_abbr:
        if state == state2:
            data2.at[index, 'state_code'] = statename_to_abbr[state2]

data2['n_incidents'] = 0
for index, state in data2['state_name'].iteritems():
    data2.at[index, 'n_incidents'] = (data['state'] == state).sum()

data2['domestic_violence'] = 0
data2['robbery'] = 0
data2['home_invasion'] = 0
data2['drug_involvement'] = 0
data2['suicide'] = 0
data2['officer_involved'] = 0
data2['accidental'] = 0
data2['dgu_evidence'] = 0
data2['gang_involvement'] = 0
data2['n_killed'] = 0
data2['n_injured'] = 0
data2['adults_involved'] = 0
data2['children_involved'] = 0
data2['teens_involved'] = 0
data2['male'] = 0
data2['female'] = 0
for index, state in data2['state_name'].iteritems():
    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'n_killed'] = selected_data['n_killed'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'n_injured'] = selected_data['n_injured'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'domestic_violence'] = selected_data['domestic_violence'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'robbery'] = selected_data['robbery'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'home_invasion'] = selected_data['home_invasion'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'drug_involvement'] = selected_data['drug_involvement'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'suicide'] = selected_data['suicide'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'officer_involved'] = selected_data['officer_involved'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'accidental'] = selected_data['accidental'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'dgu_evidence'] = selected_data['dgu_evidence'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'gang_involvement'] = selected_data['gang_involvement'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'teens_involved'] = selected_data['gang_involvement'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'adults_involved'] = selected_data['adults_involved'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'children_involved'] = selected_data['children_involved'].sum()

    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'male'] = selected_data['male'].sum()
    selected_data = data.loc[data['state'] == state]
    data2.at[index, 'female'] = selected_data['female'].sum()


print(data2)
for col in data2.columns:
    data2[col] = data2[col].astype(str)

scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]



data2['text'] = 'State: ' +data2['state_name'] + '<br>' + 'Killed: ' + data2['n_killed'] + '<br>' + \
'Injured: ' + data2['n_injured'] + '<br>' + 'Suicide: ' + data2['suicide'] + '<br>' + 'Robberies: ' + data2['robbery'] \
+ '<br>' + 'Drugs involved: ' + data2['drug_involvement'] + '<br>' + 'Officer involved: ' + data2['officer_involved'] +\
 '<br>' + 'Gangs involved: ' + data2['gang_involvement'] + '<br>' + 'Home invasion: ' + data2['home_invasion'] + \
 '<br>' + 'Domestic violence: ' + data2['domestic_violence'] + '<br>' + 'Self-defense: ' + data2['dgu_evidence'] + \
 '<br>' + 'Male involved: ' + data2['male'] + '<br>' + 'Female involved: ' + data2['female'] + \
 '<br>' + 'Adults involved: ' + data2['adults_involved'] + '<br>' + 'Teens involved: ' + data2['teens_involved'] + \
 '<br>' + 'Children involved: ' + data2['children_involved']
#+' TEST '+df['dairy']+'<br>'+\
#     'Fruits '+df['total fruits']+' Veggies ' + df['total veggies']+'<br>'+\
#     'Wheat '+df['wheat']+' Corn '+df['corn']

data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = data2['state_code'],
        text = data2['text'],
        z = data2['n_incidents'],
        locationmode = 'USA-states',
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Number of Incidents")
        ) ]

layout = dict(
        title = '',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = False,
            lakecolor = 'rgb(255, 255, 255)'),
             )

fig = dict( data=data, layout=layout )
py.iplot(fig, filename='d3-cloropleth-map')
