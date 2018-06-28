import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
from sklearn import preprocessing
import math
from pandas import ExcelWriter
import re
from pandas import ExcelFile
from geopy import geocoders
import time
import sklearn
# unzipping and reading full dataset
zf = zipfile.ZipFile('datasets/full_dataset_raw.csv.zip')

data = pd.read_csv(zf.open('stage3.csv'))
print('Starting preprocessing...')
missing_cd = pd.read_csv(zf.open('stage3.csv'))
# testing functions with smaller dataset
#data = pd.read_csv('datasets/small_test_set.csv')

# function to delete column if more than 40% of the values is unknown
total_count = len(data)


for column in data.columns:
    items = data[column]
    count = items.isnull().sum()
    percentage = (count / total_count) * 100
    print(column, "=", percentage)
    if percentage >= 40.0:
        data = data.drop(column, 1)
# remove other irrelevent columns
data = data.drop("address", 1)
data = data.drop("incident_url", 1)
data = data.drop("source_url", 1)
data = data.drop("incident_url_fields_missing", 1)
data = data.drop("congressional_district", 1)
data = data.drop("sources", 1)
data = data.drop("state_house_district", 1)
data = data.drop("state_senate_district", 1)
data = data.drop("notes", 1)
data = data.drop("participant_status", 1)
data = data.drop("participant_type", 1)
data = data.drop("participant_age", 1)
# bewerkingen aan incidents_characteristics kolom
data["incident_characteristics"] = data["incident_characteristics"].fillna('shot')
data["incident_characteristics"] = data["incident_characteristics"].str.lower()
new_column = []
for item in data["incident_characteristics"]:
    item = item.replace(" -", ",")
    item = item.replace(" and/or", ",")
    item = item.replace("/", ",")
    item = item.replace("||", ",")
    item = item.replace("gun(s)", "guns")
    item = item.replace(" (", ", ")
    item = item.replace(", ", ",")
    item = item.replace(")", "")
    item = item.replace("suicide^", "suicide")
    item = item.replace("armed robbery with injury", "robbery")
    item = item.replace("officer involved incident", "officer involved")
    item = item.replace("officer involved shooting", "officer involved")
    new_column.append(item)

data["incident_characteristics"] = new_column

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
missing_cd = pd.read_excel('datasets/best_missing_lat_lon.xlsx')
#filling the missing coordinates with the missing_lon_lat data file
for index, item in data["latitude"].iteritems():
    if pd.isna(item):
        for idx, item2 in missing_cd["index"].iteritems():
            if index == item2:
                data.at[index, 'latitude'] = missing_cd["lat"][idx]
                data.at[index, 'longitude'] = missing_cd["long"][idx]

# bewerkingen gender kolom
data["participant_gender"] = data["participant_gender"].fillna('male')
data["participant_gender"] = data["participant_gender"].str.lower()
data["male"] = 0
data["female"] = 0
for index, gender in data["participant_gender"].iteritems():
    gender = gender.replace("||", ",")
    gender = gender.replace("|", ",")
    gender = re.sub(r'\d::','' ,gender)
    gender = re.sub(r'\d:','' ,gender)
    gender = re.sub(r'\dmale','male' ,gender)
    genderList = gender.split(",")
    # male  involved, give value 1
    if "male" in genderList:
        data.at[index, 'male'] = 1
    # female involved, give value 1
    if "female" in genderList:
        data.at[index, 'female'] = 1

data = data.drop("participant_gender", 1)


# bewerkingen gender kolom
data["participant_age_group"] = data["participant_age_group"].fillna('Adult 18+')
data["participant_age_group"] = data["participant_age_group"].str.lower()
new_agegroup_column = []
for agegroup in data["participant_age_group"]:
    agegroup = agegroup.replace("||", ",")
    agegroup = agegroup.replace("|", ",")
    agegroup = re.sub(r'\d::','' , agegroup)
    agegroup = re.sub(r'\d:','' , agegroup)
    agegroup = agegroup.replace("adult 18+", "18+")
    agegroup = agegroup.replace("child 0-11", "0-11")
    agegroup = agegroup.replace("teen 12-17", "12-17")
    new_agegroup_column.append(agegroup)



data["participant_age_group"] = new_agegroup_column
data
data.rename(columns={'participant_gender':'participant_gender_involved'}, inplace=True)
# reorganizing date structure

date = "2014-01-01"
new_datecolumn = []
for date in data["date"]:
    date = date.replace("-","")
    date = date[2:6]
    new_datecolumn.append(date)
data["date"] = new_datecolumn

itemcount = 0
for item in data["incident_characteristics"]:
    itemlist = item.split(",")
    if "evidence of dgu found" in itemlist:
        itemcount = itemcount + 1


data['domestic_violence'] = 0
data['robbery'] = 0
data['home_invasion'] = 0
data['drug_involvement'] = 0
data['suicide'] = 0
data['officer_involved'] = 0
data['accidental'] = 0
data['dgu_evidence'] = 0
data['gang_involvement'] = 0
data['adults_involved'] = 0
data['children_involved'] = 0
data['teens_involved'] = 0

# setting boolean columns for participant_age_group, after that, removing participant_age_group column
for index, item in data["participant_age_group"].iteritems():
    itemlist = item.split(",")
    if "18+" in itemlist:
        data.at[index, 'adults_involved'] = 1
    if "12-17" in itemlist:
        data.at[index, 'teens_involved'] = 1
    if "0-11" in itemlist:
        data.at[index, 'children_involved'] = 1

data = data.drop("participant_age_group", 1)

# setting boolean columns for incident_characteristics, after that, removing incident_characteristics column
for index, item in data["incident_characteristics"].iteritems():
    itemlist = item.split(",")
    if "domestic violence" in itemlist:
        data.at[index, 'domestic_violence'] = 1
    if "robbery" in itemlist:
        data.at[index, 'robbery'] = 1
    if "home invasion" in itemlist:
        data.at[index, 'home_invasion'] = 1
    if "drug involvement" in itemlist:
        data.at[index, 'drug_involvement'] = 1
    if "suicide" in itemlist:
        data.at[index, 'suicide'] = 1
    if "officer involved" in itemlist:
        data.at[index, 'officer_involved'] = 1
    if "accidental" in itemlist:
        data.at[index, 'accidental'] = 1
    if "evidence of dgu found" in itemlist:
        data.at[index, 'dgu_evidence'] = 1
    if "gang involvement" in itemlist:
        data.at[index, 'gang_involvement'] = 1


data = data.drop("incident_characteristics", 1)
#print("itemcount = ",itemcount)
# counting fatal incidents



dead_count = 0
for number_killed in data["n_killed"]:
    if number_killed > 0:
        dead_count = dead_count + 1
#print(dead_count)

# labelling cities and states with digits
#le = preprocessing.LabelEncoder()
#data['city_or_county'] = le.fit_transform(data['city_or_county'])
#data['state'] = le.fit_transform(data['state'])

# reverse LabelEncoder
#data['city_or_county'] = le.inverse_transform(data['city_or_county'])

#----- Add state_population--------

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

population_list = []

for state in data['state']:
    population_list.append(dictio[state])

data['state_population'] = population_list


print("Preprocessing successful!")
print("Writing output to .xlsx file...")
# write processed dataframe to Excel testing sheet
writer = ExcelWriter('datasets/MASTER_DATASET.xlsx')
data.to_excel(writer,'testingsheet')
writer.save()
print("Output written to .xlsx file!")
