import sys
sys.path.append('src')
from k_means_clustering import *
import matplotlib.pyplot as plt
import numpy as np

data = [[0.14, 0.14, 0.28, 0.44],
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
        [0.2, 0.18, 0.3, 0.4]]
'''
initial_clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
    }

kmeans = KMeans(initial_clusters, data)
kmeans.run()

print("Clusters:", kmeans.clusters , "\n")

print("Centers:", kmeans.centers, "\n")

'''
k_values = [n for n in range(1, 6)]
distortions = []


def get_clusters(k):
    clusters = {n:[] for n in range(1, k + 1)}

    for n in range(len(data)):
        clusters[(n % k) + 1].append(n)

    return clusters

def get_distortion(clusters, centers):
    distortion = 0

    for center in centers:

        for cluster in clusters[center]:
            distortion += np.linalg.norm(np.array(centers[center]) - np.array(data[cluster])) ** 2

    return distortion

for k in k_values:
    kmeans = KMeans(get_clusters(k), data)
    kmeans.run()
    distortions.append(get_distortion(kmeans.clusters, kmeans.centers))


plt.style.use('bmh')
plt.plot(k_values, distortions)
plt.xlabel('k')
plt.ylabel('sum squared accuracy')
plt.savefig('elbow_method.png')
