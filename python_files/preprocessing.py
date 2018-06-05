import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
import math

# unzipping and reading full dataset
#zf = zipfile.ZipFile('DAV/datasets/stage3.csv.zip')
#data = pd.read_csv(zf.open('stage3.csv'))

# testing functions with smaller dataset
data = pd.read_csv('datasets/small_test_set.csv')

# function to delete column if more than 40% of the values is unknowm
total_count = len(data)

for column in data.columns:
    items = data[column]
    count = items.isnull().sum()
    percentage = (count / total_count) * 100
    print(column, "=", percentage)
    if percentage >= 40.0:
        data = data.drop(column, 1)

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
print(data["incident_characteristics"])
# write processed dataframe to CSV
# data.to_csv('DAV/datasets/full_dataset_clean.csv', sep=",")
