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
#train = train.drop(train.index[10000:239399])
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



print("Clustering with KMeans...")
# k means determine k for tsne_data using elbow method
X = train
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Plot the elbow
plt.figure(figsize=(18, 16), dpi=180)
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k for tsne_data')
plt.savefig("figures/elbowmethodt.png")
#plt.show()

## Cluster dimension-reduced data with KMeans, with n_cluster equal to k

K = 2
km = KMeans(n_clusters=K, init='k-means++', n_init=100)
km.fit(train)
x = km.fit_predict(train)

embedding_array = bhtsne.run_bh_tsne(train, no_dims=2, perplexity=4, initial_dims=train.shape[1], verbose=True)
tsne_data = pd.DataFrame(embedding_array[0:, 0:,])

# plot tsne_dat
tsne_data["cluster"] = x
tsne_data = tsne_data.sort_values('cluster')
print("tsne-data")
print(tsne_data)
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

plt.figure(figsize=(18, 16), dpi=360)
plt.scatter(tsne_data[0], tsne_data[1], s=1,c=tsne_data['color'], alpha=0.3)
plt.savefig("figures/kmeans_tsnet.png")
plt.title('Clustered with k-Means')
plt.show()


plt.figure(figsize=(18, 16), dpi=180)
plt.scatter(tsne_data[0] , tsne_data[1], s=1,c='g', alpha=0.3)
plt.title("Non-clustered data")
plt.savefig("figures/tsnet.png")
plt.show()



print("Done!")

#print("Preprocessing successful!")
#print("Writing output to .xlsx file...")
#write processed dataframe to Excel testing sheet
#writer = ExcelWriter('datasets/clustered_dataset.xlsx')
#train.to_excel(writer,'testingsheet')
#writer.save()
#print("Output written to .xlsx file!")
