import numpy as np 

import matplotlib.pyplot as plt 

from sklearn.cluster import KMeans 

from sklearn.datasets import make_blobs 

data, _ = make_blobs(n_samples=300, centers=4, random_state=42) 

kmeans = KMeans(n_clusters=4, n_init=10) 

kmeans.fit(data) 

labels = kmeans.labels_ 

centers = kmeans.cluster_centers_ 

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.7, edgecolors='k') 

plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200) 

plt.title('K-Means Clustering') 

plt.xlabel('Feature 1') 

plt.ylabel('Feature 2') 

plt.show() 
