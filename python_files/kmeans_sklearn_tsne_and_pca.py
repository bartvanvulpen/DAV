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
from tsne import tsne
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn import metrics
from scipy.spatial.distance import cdist
import random
print("Starting reading data...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')

# ----- Machine Learning Preprocessing ------

# One Hot Encoder for States
data['state'] = pd.Categorical(data['state'])
dfStates = pd.get_dummies(data['state'], prefix = 'state')
data = pd.concat([data, dfStates], axis=1)

# Drop columns
data.drop("incident_id", 1)
data.drop("city_or_county", 1)

#--------------------t-SNE and KMEANS CLUSTERING-----------------------

print('Starting KMeans, first reducing dimensions with t-SNE and PCA')

# dropping columns
data1 = data.drop("incident_id", axis =1)

#----Training and Testing set definition----
# Using trainingset
data1 = data1.sample(frac=0.8)
print(len(data1))
data1 = data1.drop(data1.index[20000:239398])

# Using testingset
#data1 = data1.sample(frac=0.2)
#print(len(data1))

print("Reducing with t-SNE...")

## reduce dimensions using TSNE
model = TSNE(n_components=2, random_state=0)
res = model.fit_transform(data1)
tsne_data = pd.DataFrame(res[0:, 0:,])
print("Done")

plt.scatter(tsne_data[0] , tsne_data[1], s=1,c='g', alpha=0.2)
plt.title("t-SNE")
plt.show()

print("Reducing with PCA...")

## Reduce dimensions using PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data1)
pca_data = pd.DataFrame(pca_result[0:, 0:,])
plt.scatter(pca_data[0] , pca_data[1], s=1,c='r', alpha=0.2 )
plt.title("PCA")
plt.show()
print("Done")


#-----------------------KMEANS TSNE_DATA-----------------
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

#-----------------------KMEANS PCA_DATA-----------------
print("KMeans PCA...")
# k means determine k for pca_data usign elbow method
X = pca_data
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
plt.title('The Elbow Method showing the optimal k for pca_data')
plt.show()

## Cluster dimension-reduced data with KMeans, with n_cluster equal to k

K = 2
km = KMeans(n_clusters=K, init='k-means++', n_init=100)
km.fit(pca_data)
x = km.fit_predict(pca_data)

# plot tsne_dat
pca_data["cluster"] = x
color_list = []
for cluster in pca_data['cluster']:
    if cluster == 0:
        color_list.append('blue')
    if cluster == 1:
        color_list.append('orange')

pca_data['color'] = color_list


plt.scatter(pca_data[0], pca_data[1], s=1,c=pca_data['color'], alpha=0.2)
plt.show()
print("Finished")
