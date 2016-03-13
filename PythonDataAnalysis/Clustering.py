# load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv("Dataset.csv",header=0).dropna()

# subset
subset = data[['Income','Rent_Amount']]
pos_rent_and_income = (subset['Income']>0) & (subset['Rent_Amount']>0)
subset = subset[pos_rent_and_income]
subset.head()

# data distribution
plt.scatter(subset['Income'],subset['Rent_Amount'],linewidth='0')
plt.show()

# K-means clustering
# Only need to select the number of clusters, K
from sklearn.cluster import KMeans
# instantiate a Kmeans object to process data into KMeans
kmeans = KMeans(n_clusters=5,init="random")
# produce kmeans from out subset of data
cluster = kmeans.fit_predict(subset)
# plot income versus rent and color them by out cluster output
plt.scatter(subset['Income'],subset['Rent_Amount'],c=cluster,cmap=cm.rainbow,linewidth='0')
# plot the centroids for each cluster
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c=range(5),cmap=cm.rainbow)
plt.show()

# DBSCAN
from sklearn.cluster import DBSCAN
# eps = maximum distance between reachable core data points
# min_sample = minimum number of reachable data point for a core data point
dbscan = DBSCAN(eps=50,min_samples=5)
# produce dbscan based clusters
db_cluster = dbscan.fit_predict(subset)
isnoise = dbscan.labels_==-1
# plot clustered data points
plt.scatter(subset[isnoise == False]['Income'],
            subset[isnoise == False]['Rent_Amount'],
            c=db_cluster[isnoise==False],
            cmap=cm.rainbow,
            linewidth='0')
plt.show()