import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import *
from dataframe import DataFrame

df = pd.DataFrame(
    [['A', 0],
     ['A', 1],
     ['B', 2],
     ['B', 3]],
     columns = ['letter', 'number']
)

knn = KNearestNeighborsClassifier(k=4)
knn.fit(df, dependent_variable = 'letter')
observation = {
    'number': 1.6
}

print(knn.classify(observation))