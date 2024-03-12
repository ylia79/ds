import numpy as np 

from sklearn.decomposition import PCA 

import matplotlib.pyplot as plt 

np.random.seed(42) 

X = np.random.rand(100, 2) 

n_components = 1 

pca = PCA(n_components=n_components) 

X_pca = pca.fit_transform(X) 

print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}") 

plt.figure(figsize=(10, 5)) 

plt.subplot(1, 2, 1) 

plt.scatter(X[:, 0], X[:, 1], alpha=0.8) 

plt.title("Original Data") 

plt.subplot(1, 2, 2) 

plt.scatter(X_pca, np.zeros_like(X_pca), alpha=0.8) 

plt.title(f"Data after PCA ({n_components} component)") 

plt.show()
