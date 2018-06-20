import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
from copy import deepcopy
from sklearn import preprocessing
from sklearn import datasets
import pandas as pd
import numpy as np
from pandas import ExcelWriter
print("Starting reading data...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')


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
le = preprocessing.LabelEncoder()
data['city_or_county'] = le.fit_transform(data['city_or_county'])
data['state'] = le.fit_transform(data['state'])







print(len(population_list))
print('hello')

#--------------------K-Means 3 clusters-----------------------
# dropping columns
data1 = data.drop(["date","city_or_county","state", "latitude", "n_injured","incident_id", "suicide", "participant_gender_involved", "domestic_violence", "home_invasion", "drug_involvement", "officer_involved", "dgu_evidence", "gang_involvement", "adults_involved", "teens_involved", "children_involved"], axis =1)
print(data1.head())




km = KMeans(n_clusters=2, init='k-means++', n_init=10)
km.fit(data1)
x = km.fit_predict(data1)

data["cluster"]= x
color_list = []
for cluster in data['cluster']:
    if cluster == 0:
        color_list.append('r')
    if cluster == 1:
        color_list.append('b')
    if cluster == 2:
        color_list.append('g')
data['color'] = color_list

print(data.head())
# printing sorted dataset on cluster
data1 = data.sort_values(['cluster'])
print(data1)
plt.scatter(data['n_killed'], data['state_population'], color=data['color'], alpha=0.5, edgecolor='k')
plt.show()

# print("Preprocessing successful!")
# print("Writing output to .xlsx file...")
# # write processed dataframe to Excel testing sheet
# writer = ExcelWriter('datasets/kmeans_testing.xlsx')
# data1.to_excel(writer,'testingsheet')
# writer.save()
# print("Output written to .xlsx file!")
