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

data

#groupby_city = data['state'].groupby(data['n_killed'])
#groupby_city.describe()
#meeste non-dodelijke incidenten in illinois,
#meeste dodelijke incidenten in california
#newDF = pd.DataFrame()
#newDF["states"] = 

groupby_state1 = data['n_killed'].groupby(data['state'])
n_killed = groupby_state1.describe()
groupby_state2 = data['n_injured'].groupby(data['state'])
n_injured = groupby_state2.describe()
n_injured
groupby_state3 = data.groupby(data['state'])
state = groupby_state3.describe()
state
pd.options.display.max_columns = None
display(state)

state["state_population"]["mean"]


#Alle aankomende grafieken zijn per staat ingedeeld,
#elk datapunt is een staat, dus elke grafiek heeft 51 datapunten.
#

#
#Graph 1
#
plt.scatter(n_killed['mean'], n_killed['count'])
z = np.polyfit(n_killed['mean'], n_killed['count'], 1)
plt.plot(n_killed['mean'],p(n_killed['mean']),"r--")
plt.ylabel('Incidents')
plt.xlabel('Average deaths per incident')
plt.title('Incidents and average deaths per incident')
p = np.poly1d(z)
plt.show()

#
#Graph 2
#
plt.scatter(n_injured['mean'], n_injured['count'])
z = np.polyfit(n_injured['mean'], n_injured['count'], 1)
p = np.poly1d(z)
plt.plot(n_injured['mean'],p(n_injured['mean']),"r--")
plt.ylabel('Incidents')
plt.xlabel('Average injured per incident')
plt.title('Incidents and average injured per incident')
plt.show()


#
#Graph 3
#
plt.scatter(n_injured['mean'], n_killed['mean'])
#z = np.polyfit(n_injured['mean'], n_killed['mean'], 1)
#plt.plot(n_injured['mean'],p(n_injured['mean']),"r--")
#p = np.poly1d(z)
plt.ylabel('Average death')
plt.xlabel('Average injured')
plt.title('Dead vs Injured')
plt.show()


#
#Graph 4
#
plt.scatter(n_injured['mean'], state["state_population"]["mean"])
z = np.polyfit(n_injured['mean'], state["state_population"]["mean"], 1)
p = np.poly1d(z)
plt.plot(n_injured['mean'],p(n_injured['mean']),"r--")
plt.ylabel('Population')
plt.xlabel('Average injured')
plt.title('Population and injuries')
plt.show()


#
#Graph 5
#
plt.scatter(n_killed['mean'], state["state_population"]["mean"])
z = np.polyfit(n_killed['mean'], state["state_population"]["mean"], 1)
p = np.poly1d(z)
plt.plot(n_killed['mean'],p(n_killed['mean']),"r--")
plt.ylabel('Population')
plt.xlabel('Average deaths')
plt.title('Population and deaths')
plt.show()