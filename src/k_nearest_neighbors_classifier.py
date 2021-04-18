import pandas as pd
import numpy as np
import math
from collections import Counter

class KNearestNeighborsClassifier():
    def __init__(self, k):
        self.k = k

    def fit(self, df, dependent_variable):
        self.df = df
        self.columns = df.columns
        self.dependent_variable = dependent_variable

    def compute_distances(self, observation):
        columns = [column for column in self.columns if column != self.dependent_variable]
        df = self.df[columns]

        distances = []

        for n in range(len(list(df[df.columns[0]]))):
            distance = 0

            for key in observation:
                distance += (float(observation[key]) - float(df[key][n])) ** 2

            distances.append(math.sqrt(distance))

        data = {}
        data['Distance'] = distances
        data[self.dependent_variable] = [dependent_variable for dependent_variable in list(self.df[self.dependent_variable])]
        return pd.DataFrame.from_dict(data)

    def nearest_neighbors(self, observation):
        self.df = self.compute_distances(observation)
        return self.df.sort_values(by=['Distance'])

    def classify(self, observation):
        self.df = self.nearest_neighbors(observation)[:self.k]
        counter = Counter(self.df[self.dependent_variable])
        frequency_list = counter.most_common()

        for n in range(1, len(frequency_list) - 1):
            if frequency_list[n][1] == frequency_list[0][1]:
                averages = {}

                for variable in self.df[self.dependent_variable].unique():
                      averages[variable] = self.df.loc[self.df[self.dependent_variable] == variable].mean()[0]
                      return min(averages.items(), key=lambda x: x[1])[0]

        return frequency_list[0][0]
