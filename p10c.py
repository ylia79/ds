import numpy as np 

from sklearn.decomposition import PCA 

import matplotlib.pyplot as plt 

np.random.seed(42) 

X = np.random.rand(100, 5) 

n_components = 2 

pca = PCA(n_components=n_components) 

X_pca = pca.fit_transform(X) 

plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.8) 

plt.title(f'Reduced-dimensional Space (First {n_components} Components)') 

plt.xlabel(f'Principal Component 1 (Explained Variance: {pca.explained_variance_ratio_[0]:.2f})') 

plt.ylabel(f'Principal Component 2 (Explained Variance: {pca.explained_variance_ratio_[1]:.2f})') 

plt.grid(True) 

plt.show() 
