import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
from sklearn import preprocessing
import math
from pandas import ExcelWriter
import re

# unzipping and reading full dataset
zf = zipfile.ZipFile('datasets/full_dataset_raw.csv.zip')

data = pd.read_csv(zf.open('stage3.csv'))
print('Starting preprocessing...')

# testing functions with smaller dataset
#data = pd.read_csv('datasets/small_test_set.csv')

# function to delete column if more than 40% of the values is unknowm
total_count = len(data)

for column in data.columns:
    items = data[column]
    count = items.isnull().sum()
    percentage = (count / total_count) * 100
    #print(column, "=", percentage)
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

# bewerkingen gender kolom
data["participant_gender"] = data["participant_gender"].fillna('male')
data["participant_gender"] = data["participant_gender"].str.lower()
new_gender_column = []
for gender in data["participant_gender"]:
    gender = gender.replace("||", ",")
    gender = gender.replace("|", ",")
    gender = re.sub(r'\d::','' ,gender)
    gender = re.sub(r'\d:','' ,gender)
    gender = re.sub(r'\dmale','male' ,gender)
    genderList = gender.split(",")
    # male only involved, give value 0
    if "male" in genderList and not "female" in genderList:
        new_gender_column.append('0')
    # female only involved, give value 1
    elif "female" in genderList and not "male" in genderList:
        new_gender_column.append('1')
    # male and female involved, give value 2
    elif "male" in genderList and "female" in genderList:
        new_gender_column.append('2')

data["participant_gender"] = new_gender_column

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

# setting boolean columns for incident_characteristics, after that, removing incident_characteristics column
data['domestic_violence'] = 0
data['robbery'] = 0
data['home_invasion'] = 0
data['drug_involvement'] = 0
data['suicide'] = 0
data['officer_involved'] = 0
data['accidental'] = 0

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


# counting characterics
itemcount = 0
for item in data["incident_characteristics"]:
    itemlist = item.split(",")
    if "domestic violence" in itemlist and not "murder" in itemlist:
        itemcount = itemcount + 1

data = data.drop("incident_characteristics", 1)
#print("itemcount = ",itemcount)
# counting fatal incidents
dead_count = 0
for number_killed in data["n_killed"]:
    if number_killed > 0:
        dead_count = dead_count + 1
#print(dead_count)

# labelling cities and states with digits
le = preprocessing.LabelEncoder()
data['city_or_county'] = le.fit_transform(data['city_or_county'])
data['state'] = le.fit_transform(data['state'])

# reverse LabelEncoder
# data['city_or_county'] = le.inverse_transform(data['city_or_county'])

print("Preprocessing successful!")
print("Writing output to .xlsx file...")
# write processed dataframe to Excel testing sheet
writer = ExcelWriter('datasets/full_dataset_excel_testing.xlsx')
data.to_excel(writer,'testingsheet')
writer.save()
print("Output written to .xlsx file!")
