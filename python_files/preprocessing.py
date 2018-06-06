import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
import math
from pandas import ExcelWriter

# unzipping and reading full dataset
zf = zipfile.ZipFile('datasets/full_dataset_raw.csv.zip')

data = pd.read_csv(zf.open('stage3.csv'))


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
    new_column.append(item)
data["incident_characteristics"] = new_column

#write processed dataframe to Excel testing sheet
writer = ExcelWriter('datasets/full_dataset_excel_testing.xlsx')
data.to_excel(writer,'testingsheet')
writer.save()
print("Written to Excel")
