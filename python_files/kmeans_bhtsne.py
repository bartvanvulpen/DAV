import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
from copy import deepcopy
from sklearn import preprocessing
from sklearn import datasets
import pandas as pd
import numpy as np
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
from sklearn.model_selection import train_test_split
print("Done.")

print("Using One Hot Encoder and optimizing data for Machine Learning...")
# One Hot Encoder for States
data['state'] = pd.Categorical(data['state'])
dfStates = pd.get_dummies(data['state'], prefix = 'state')
data = pd.concat([data, dfStates], axis=1)

# data['state'] = pd.Categorical(data['city_or_county'])
# dfCities = pd.get_dummies(data['city_or_county'], prefix = 'city')
# data = pd.concat([data, dfCities], axis=1)

# Drop columns
data = data.drop("incident_id", 1)
data = data.drop("city_or_county", 1)
data = data.drop("state", 1)
print(data)
print("Done.")

#----Split dataset in training set and test set----

print("Splitting dataset into training set and test set...")
train, test = train_test_split(data, test_size=0.2)
train = train.drop(train.index[1000:239398])
print("Number of dimensions:", len(train.columns))
print(train)
print("Done.")
#----Running run_bh_tsne------------------

print('Starting KMeans, first reducing dimensions with Barnes-Hut t-SNE...')

# state of data: train of test
data1 = train
train_bool = True
if train_bool:
    print("State of learning: TRAIN")
else:
    print("State of learning: TEST")

embedding_array = bhtsne.run_bh_tsne(data1, no_dims=2, perplexity=4, initial_dims=data1.shape[1], verbose=True)
tsne_data = pd.DataFrame(embedding_array[0:, 0:,])
plt.scatter(tsne_data[0] , tsne_data[1], s=1,c='g', alpha=0.3)
plt.title("Dimension reduced with t-SNE")
plt.savefig("figures/tsne.png")
plt.show()

print("Clustering with KMeans...")
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
plt.savefig("figures/elbowmethod.png")
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

plt.scatter(tsne_data[0], tsne_data[1], s=1,c=tsne_data['color'], alpha=0.3)
plt.savefig("figures/kmeans_tsne.png")
plt.title('Clustered t-SNE')
plt.show()
print("Done!")
