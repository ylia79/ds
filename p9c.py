import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

data, _ = make_blobs(n_samples=300, centers=4, random_state=42)

optimal_k = 4

kmeans = KMeans(n_clusters=optimal_k, n_init=10, random_state=42)
kmeans.fit(data)

labels = kmeans.labels_
centers = kmeans.cluster_centers_

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', alpha=0.7, edgecolors='k')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Cluster Centers')
plt.title('K-Means Clustering Results')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

for cluster_num in range(optimal_k):
    cluster_points = data[labels == cluster_num]
    cluster_center = centers[cluster_num]
    print(f"\nCluster {cluster_num + 1} Characteristics:")
    print(f"Number of points in cluster: {len(cluster_points)}")
    print(f"Cluster Center: {cluster_center}")
    print(f"Average Distance to Center: {np.mean(np.linalg.norm(cluster_points - cluster_center, axis=1)):.2f}")
