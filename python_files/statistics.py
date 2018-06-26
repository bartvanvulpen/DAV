import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import sys
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

print("Starting reading data...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')
#data = pd.read_csv('datasets/small_test_set.csv')

#-------------------------Aantal doden per staat---------------------
# state_death = {}
# for index, item in data['state'].iteritems():
#     index_deads = data['n_killed'][index]
#
#     if not item in state_death:
#         state_death[item] = index_deads
#     elif item in state_death:
#         state_death[item] = state_death[item] + index_deads
#
# print(state_death)
#
# # plotting number of killed in every state
# plt.bar(list(state_death.keys()), state_death.values(), color='g')
# plt.show()

# -----------Gun violence by characteristics 2014-2017-------------
#
# robbery_count = []
# drug_count = []
# accidental_count = []
# suicide_count = []
# gang_count = []
# officer_count = []
# domestic_count = []
# year_characts = {}
# for index, date in data['date'].iteritems():
#     robbery_count.append(data['robbery'][index])
#     drug_count.append(data['drug_involvement'][index])
#     accidental_count.append(data['accidental'][index])
#     suicide_count.append(data['suicide'][index])
#     gang_count.append(data['gang_involvement'][index])
#     officer_count.append(data['officer_involved'][index])
#     domestic_count.append(data['domestic_violence'][index])
#     #print(index)
#     if date == 1412 and data['date'][index + 1] == 1501:
#         year_characts['2014'] = [sum(robbery_count), sum(drug_count), sum(accidental_count), sum(suicide_count), sum(gang_count), sum(officer_count), sum(domestic_count)]
#         robbery_count = []
#         drug_count = []
#         accidental_count = []
#         suicide_count = []
#         gang_count = []
#         officer_count = []
#         domestic_count = []
#     if date == 1512 and data['date'][index + 1] == 1601:
#         year_characts['2015'] = [sum(robbery_count), sum(drug_count), sum(accidental_count), sum(suicide_count), sum(gang_count), sum(officer_count), sum(domestic_count)]
#         robbery_count = []
#         drug_count = []
#         accidental_count = []
#         suicide_count = []
#         gang_count = []
#         officer_count = []
#         domestic_count = []
#     if date == 1612 and data['date'][index + 1] == 1701:
#         year_characts['2016'] = [sum(robbery_count), sum(drug_count), sum(accidental_count), sum(suicide_count), sum(gang_count), sum(officer_count), sum(domestic_count)]
#         robbery_count = []
#         drug_count = []
#         accidental_count = []
#         suicide_count = []
#         gang_count = []
#         officer_count = []
#         domestic_count = []
#     if date == 1712 and data['date'][index + 1] == 1801:
#         year_characts['2017'] = [sum(robbery_count), sum(drug_count), sum(accidental_count), sum(suicide_count), sum(gang_count), sum(officer_count), sum(domestic_count)]
#         robbery_count = []
#         drug_count = []
#         accidental_count = []
#         suicide_count = []
#         gang_count = []
#         officer_count = []
#         domestic_count = []
#         break
#
#
#
# print(year_characts)
#
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from io import StringIO
#
#
#
#
# columns = ['year', 'robbery', 'drug', 'accidental', 'suicide', 'gang', 'officer', 'domestic']
# df = pd.DataFrame(columns=columns)
# years = []
# robbery_count = []
# drug_count = []
# accidental_count = []
# suicide_count = []
# gang_count = []
# officer_count = []
# domestic_count = []
# for key in year_characts:
#     years.append(key)
#     robbery_count.append(year_characts[key][0])
#     drug_count.append(year_characts[key][1])
#     accidental_count.append(year_characts[key][2])
#     suicide_count.append(year_characts[key][3])
#     gang_count.append(year_characts[key][4])
#     officer_count.append(year_characts[key][5])
#     domestic_count.append(year_characts[key][6])
#
#
#
# df['year'] = years
# df['robbery'] = robbery_count
# df['drug'] = drug_count
# df['accidental'] = accidental_count
# df['suicide'] = suicide_count
# df['gang'] = gang_count
# df['officer'] = officer_count
# df['domestic'] = domestic_count
#
# print (df)
#
#
#
# # Setting the positions and width for the bars
# pos = list(range(len(df['robbery'])))
# width = 0.11
#
# # Plotting the bars
# fig, ax = plt.subplots(figsize=(10,5))
#
# # Create a bar with pre_score data,
# # in position pos,
# plt.bar(pos,
#         #using df['pre_score'] data,
#         df['robbery'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='orange',
#         # with label the first value in first_name
#         label=df['year'][0])
#
# # Create a bar with mid_score data,
# # in position pos + some width buffer,
# plt.bar([p + width for p in pos],
#         #using df['mid_score'] data,
#         df['drug'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='red',
#         # with label the second value in first_name
#         label=df['year'][1])
#
# # Create a bar with post_score data,
# # in position pos + some width buffer,
# plt.bar([p + width*2 for p in pos],
#         #using df['post_score'] data,
#         df['accidental'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='yellow',
#         # with label the third value in first_name
#         label=df['year'][2])
#
# plt.bar([p + width*3 for p in pos],
#         #using df['post_score'] data,
#         df['suicide'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='blue',
#         # with label the third value in first_name
#         label=df['year'][3])
# plt.bar([p + width*4 for p in pos],
#         #using df['post_score'] data,
#         df['gang'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='black',
#         # with label the third value in first_name
#         label=df['year'][0])
#
# plt.bar([p + width*5 for p in pos],
#         #using df['post_score'] data,
#         df['officer'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='green',
#         # with label the third value in first_name
#         label=df['year'][1])
#
# plt.bar([p + width*6 for p in pos],
#         #using df['post_score'] data,
#         df['domestic'],
#         # of width
#         width,
#         # with alpha 0.5
#         alpha=0.5,
#         # with color
#         color='grey',
#         # with label the third value in first_name
#         label=df['year'][2])
#
# # Set the y axis label
# ax.set_ylabel('Amount')
#
# # Set the chart's title
# ax.set_title('Gun incidents by characteristics')
#
# # Set the position of the x ticks
# ax.set_xticks([p + 3 * width for p in pos])
#
# # Set the labels for the x ticks
# ax.set_xticklabels(df['year'])
#
# # Setting the x-axis and y-axis limits
# plt.xlim(min(pos)-width*2, max(pos)+width*8)
# plt.ylim([0, 23000] )
#
# # Adding the legend and showing the plot
# plt.legend(['Robbery', 'Drug involvement', 'Accidental', 'Suicide', 'Gang involvement', 'Officer involved', 'Domestic Violence'], loc='upper left')
# plt.grid()
# plt.show()

#------------------------Mapping lat and longitudes on US Map using offline map + Google Maps----------------------
from bokeh.sampledata import us_states
from bokeh.plotting import *
from bokeh.plotting import figure
from bokeh.embed import components
us_states = us_states.data.copy()

del us_states["HI"]
del us_states["AK"]

# separate latitude and longitude points for the borders
#   of the states.
state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

# init figure
p1 = figure(title="",
           toolbar_location="left", plot_width=800, plot_height=509, x_range=(-126, -66), y_range=(24, 50))

# Draw state lines
p1.patches(state_xs, state_ys, fill_alpha=0.0,
    line_color="#884444", line_width=1.5)



# Now group these values together into a lists of x (longitude) and y (latitude)
x = data['longitude'].values
y = data['latitude'].values

# The scatter markers
p1.circle(x, y, size=5, color='red', alpha=0.2)

# output to static HTML file
output_file("figures/mapped_long_lat.html")

# show results
#show(p1)

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

output_file("figures/gmap.html")

map_options = GMapOptions(lat=38.5, lng=-95.7394,  map_type="roadmap", zoom=4,)

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
api_key = "AIzaSyDhp4ma4XSYbiklD8oh9CwscyHx_EX6slE"
p = gmap(api_key, map_options, title="", plot_width=800, plot_height=475,)

source = ColumnDataSource(
    data=dict(lat=y,
              lon=x)
)

p.circle(x="lon", y="lat", size=2, color="red", alpha=0.2, source=source)

show(p)
