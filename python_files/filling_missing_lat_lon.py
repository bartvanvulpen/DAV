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
count = 0
for index, item in data["latitude"].iteritems():
    city = data["city_or_county"][index]
    if index > 100095:
        if pd.isna(item):
            print(city, index)
            geolocator = geocoders.Nominatim()
            location = geolocator.geocode(city)
            count = count + 1
            if location:
                lat= location.latitude
                lon= location.longitude
                list_city.append(city)
                list_lat.append(lat)
                list_long.append(lon)
                list_index.append(index)
            else:
                list_city.append(city)
                list_lat.append("unknown")
                list_long.append("unknown")
                list_index.append(index)
            if index > 120000:
                break

            time.sleep(0.5)

print("count", count)
columns = ['city', 'lat', 'long', 'index']
df = pd.DataFrame(columns=columns)
df['city'] = list_city
df['lat'] = list_lat
df['long'] = list_long
df['index'] = list_index
writer = ExcelWriter('datasets/ll_test.xlsx')
df.to_excel(writer,'testingsheet_ll')
writer.save()
