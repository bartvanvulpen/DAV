import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
from sklearn import preprocessing
import math
from pandas import ExcelWriter
import re
from geopy import geocoders
import time
import geocoder
from pygeocoder import Geocoder
from geopy import exc
# unzipping and reading full dataset
zf = zipfile.ZipFile('datasets/full_dataset_raw.csv.zip')

data = pd.read_csv(zf.open('stage3.csv'))
print('Starting preprocessing...')

# removing parentheses in city_or_county
newcitylist = []
for city in data["city_or_county"]:
    city = re.sub(" [\(\[].*?[\)\]]", "", city)
    if city == "Harrison":
        city = "Cadiz"
    elif city == "Liberty":
        city = "Liberty County"
    elif city == "Midland":
        city = "Midland County"
    elif city == "Mc Kees Rocks":
        city = "Pittsburgh"
    elif city == "Haywood":
        city = "Waynesville"
    elif city == "Taylor":
        city = "Abilene"
    newcitylist.append(city)

data["city_or_county"] = newcitylist

# creating new dataframe and .xlsx file for missing lon and lat values
list_city = []
list_lat = []
list_long = []
list_index = []
list_state = []
count = 0
for index, item in data["latitude"].iteritems():
    if index >= 0:
        if pd.isna(item):

            count = count + 1
        if index > 100000:
            break
print(count)
geolocator = geocoders.Nominatim()
# recursive function to get around the timeout
def do_geocode(query):
    try:
        return geolocator.geocode(query)
    # if there's an time out error, just try again
    except exc.GeocoderTimedOut:
        return do_geocode(query)
# the loop to get the geocodes using do_geocode recursive function
count = 0


for index, item in data["latitude"].iteritems():
    city = data["city_or_county"][index]
    state = data["state"][index]
    query = str(city + ", " + state)


    if pd.isna(item):
        #print(query, index)
        count = count + 1

        #location = do_geocode(query)
        #print((count / 2262)*100)
        #if location:
            #lat = location.latitude
            #lon = location.longitude
            #list_city.append(city)
            #list_lat.append(lat)
            #list_long.append(lon)
            #list_index.append(index)
        list_state.append(state)




    






columns = ['state']
df = pd.DataFrame(columns=columns)
print(list_state)
df['state'] = list_state

writer = ExcelWriter('datasets/ll_test_states.xlsx')
df.to_excel(writer,'testingsheet_ll')
writer.save()
print("testingsheet written")
