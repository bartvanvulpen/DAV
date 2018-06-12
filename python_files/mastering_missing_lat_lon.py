import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
from pandas import ExcelFile
from pandas import ExcelWriter
import re
from geopy import geocoders
import time
import geocoder
from pygeocoder import Geocoder
from geopy import exc
data = pd.read_excel('datasets/missing_ll.xlsx')
geolocator = geocoders.Nominatim()
def do_geocode(city):
    try:
        return geolocator.geocode(city, language='en')
    # if there's an time out error, just try again
    except exc.GeocoderTimedOut:
        return do_geocode(city)
for index, item in data["long"].iteritems():


    if  data["city"][index] == "Cambridge":
        data.at[index, "lat"] = float(42.375)
        data.at[index, "long"] = float(-71.106111)
    if  data["city"][index] == "Saint Paul":
        data.at[index, "lat"] = float(44.944167)
        data.at[index, "long"] = float(-93.093611)
    if  data["city"][index] == "Albuquerque":
        data.at[index, "lat"] = float(35.110833)
        data.at[index, "long"] = float(-106.61)
    if  data["city"][index] == "Durham":
        data.at[index, "lat"] = float(35.988611)
        data.at[index, "long"] = float(-78.907222)
    if  data["city"][index] == "Norfolk":
        data.at[index, "lat"] = float(36.854628)
        data.at[index, "long"] = float(-76.274394)
    if  data["city"][index] == "Saint Petersburg":
        data.at[index, "lat"] = float(27.773056)
        data.at[index, "long"] = float(-82.64)
    if  data["city"][index] == "Birmingham":
        data.at[index, "lat"] = float(33.543682)
        data.at[index, "long"] = float(-86.779633)
    if  data["city"][index] == "York":
        data.at[index, "lat"] = float(39.962778)
        data.at[index, "long"] = float(-76.728056)
    if  data["city"][index] == "Flint":
        data.at[index, "lat"] = float(43.01)
        data.at[index, "long"] = float(-83.69)
    if  data["city"][index] == "Batavia":
        data.at[index, "lat"] = float(42.998611)
        data.at[index, "long"] = float(-78.184167)
    if  data["city"][index] == "Cadiz":
        data.at[index, "lat"] = float(36.867778)
        data.at[index, "long"] = float(-87.8175)
    if  data["city"][index] == "Aberdeen":
        data.at[index, "lat"] = float(45.464722)
        data.at[index, "long"] = float(-98.486389)
    if  data["city"][index] == "Salisbury":
        data.at[index, "lat"] = float(38.365833)
        data.at[index, "long"] = float(-75.593333)
    if  data["city"][index] == "Alexandria":
        data.at[index, "lat"] = float(31.292778)
        data.at[index, "long"] = float(-92.458889)
    if  data["city"][index] == "Worcester":
        data.at[index, "lat"] = float(42.266667)
        data.at[index, "long"] = float(-71.8)
    if  data["city"][index] == "Dover":
        data.at[index, "lat"] = float(39.158056)
        data.at[index, "long"] = float(-75.524444)
    if  data["city"][index] == "Aberdeen":
        data.at[index, "lat"] = float(45.464722)
        data.at[index, "long"] = float(-98.486389)
    if  data["city"][index] == "Manchester":
        data.at[index, "lat"] = float(38.365833)
        data.at[index, "long"] = float(-75.593333)
    if  data["city"][index] == "Alexandria":
        data.at[index, "lat"] = float(31.292778)
        data.at[index, "long"] = float(-92.458889)
    if  data["city"][index] == "Canton":
        data.at[index, "lat"] = float(40.805)
        data.at[index, "long"] = float(-81.375833)
    if  data["city"][index] == "Florence":
        data.at[index, "lat"] = float(34.183889)
        data.at[index, "long"] = float(-79.774167)
    if  data["city"][index] == "Lula":
        data.at[index, "lat"] = float(34.389722)
        data.at[index, "long"] = float(-83.664167)
    if  data["city"][index] == "Fenton":
        data.at[index, "lat"] = float(38.528056)
        data.at[index, "long"] = float(-90.444167)
    if  data["city"][index] == "Casa":
        data.at[index, "lat"] = float(29.762778)
        data.at[index, "long"] = float(-95.383056)
    if  data["city"][index] == "Odessa":
        data.at[index, "lat"] = float(31.863333)
        data.at[index, "long"] = float(-102.365556)
    if  data["city"][index] == "Verona":
        data.at[index, "lat"] = float(34.188333)
        data.at[index, "long"] = float(-88.718056)
    if  data["city"][index] == "Portsmouth":
        data.at[index, "lat"] = float(43.075556)
        data.at[index, "long"] = float(-70.760556)
    if  data["city"][index] == "Santa Fe":
        data.at[index, "lat"] = float(35.667222)
        data.at[index, "long"] = float(-105.964444)
    if  data["city"][index] == "Mc Donald":
        data.at[index, "lat"] = float(39.785278)
        data.at[index, "long"] = float(-101.370556)
    if  data["city"][index] == "Chester":
        data.at[index, "lat"] = float(39.847222)
        data.at[index, "long"] = float(-75.372778)
    if  data["city"][index] == "Bristol":
        data.at[index, "lat"] = float(36.583333)
        data.at[index, "long"] = float(-82.183333)
    

ucount = 0
wcount = 0
writer = ExcelWriter('datasets/mastered_ll.xlsx')
data.to_excel(writer,'mastered_ll')
writer.save()
print("Output written to .xlsx file!")

for index, item in data["long"].iteritems():


    if item == "unknown":
        ucount = ucount + 1
        print("unknown", data["city"][index])
    elif item > -64.0:
        print("Wrong:", data["city"][index])
        wcount = wcount + 1


print(ucount)
print(wcount)
