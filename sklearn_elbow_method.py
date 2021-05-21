import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]])


k_values = [n for n in range(1, 10)]
distortions = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data)
    distortions.append(kmeans.inertia_)


plt.style.use('bmh')
plt.plot(k_values, distortions)
plt.xlabel('k')
plt.ylabel('sum squared accuracy')
plt.savefig('elbow_method_sk_learn.png')
