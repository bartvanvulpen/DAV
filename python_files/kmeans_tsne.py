import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
from copy import deepcopy
from sklearn import preprocessing
from sklearn import datasets
import pandas as pd
import numpy as np
import tsne
import bhtsne
from pandas import ExcelWriter
from tsne import tsne
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn import metrics
from scipy.spatial.distance import cdist
import random
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
print('Starting KMeans, first reducing dimensions with t-SNE')
data1 = data.drop("incident_id", axis=1)

#----Training and Testing set definition----
# Using trainingset
data1 = data1.sample(frac=0.8)
print(len(data1))
data1 = data1.drop(data1.index[100000:239398])

embedding_array = tsne(data1, no_dims=2, initial_dims=21, perplexity=21)
tsne_data = pd.DataFrame(embedding_array[0:, 0:,])
plt.scatter(tsne_data[0] , tsne_data[1], s=1,c='g', alpha=0.2)
plt.title("t-SNE")
plt.show()

print("KMeans t-SNE...")
# k means determine k for tsne_data using elbow method
X = tsne_data
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k for tsne_data')
plt.show()

## Cluster dimension-reduced data with KMeans, with n_cluster equal to k

K = 3
km = KMeans(n_clusters=K, init='k-means++', n_init=100)
km.fit(tsne_data)
x = km.fit_predict(tsne_data)

# plot tsne_dat
tsne_data["cluster"] = x
color_list = []
for cluster in tsne_data['cluster']:
    if cluster == 0:
        color_list.append('red')
    if cluster == 1:
        color_list.append('green')
    if cluster == 2:
        color_list.append('blue')
    if cluster == 3:
        color_list.append('orange')
tsne_data['color'] = color_list


plt.scatter(tsne_data[0], tsne_data[1], s=1,c=tsne_data['color'], alpha=0.2)
plt.show()
