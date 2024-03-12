import numpy as np 

from sklearn.decomposition import PCA 

import matplotlib.pyplot as plt 

np.random.seed(42) 

X = np.random.rand(100, 5) 

num_components = min(X.shape[1], 5) 

explained_variances = [] 

for n_components in range(1, num_components + 1): 
    pca = PCA(n_components=n_components) 
    X_pca = pca.fit_transform(X) 
    explained_variances.append(np.sum(pca.explained_variance_ratio_)) 
plt.plot(range(1, num_components + 1), explained_variances, marker='o') 

plt.xlabel('Number of Components') 

plt.ylabel('Explained Variance') 

plt.title('Explained Variance vs. Number of Components') 

plt.grid(True) 

plt.show() 
