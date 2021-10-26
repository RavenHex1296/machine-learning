import sys
sys.path.append('datasets')
from semi_random_data import *
sys.path.append('src')
from decision_tree import *
import time

class RandomForest():
    def __init__(self, point_data, min_size_to_split, num_trees, random_splits=None, p=None):
        self.point_data = point_data
        self.min_size_to_split = min_size_to_split
        self.num_trees = num_trees
        self.forest = []
        self.random_splits = random_splits
        self.p = p

    def get_all_points(self, point_data):
        all_points = []

        for key in point_data:
            all_points += point_data[key]

        return all_points

    def get_random_p_percent(self, input_data, p):
        p_percent = round(p * len(self.get_all_points(input_data)))
        new_data = {'x': [], 'o': []}
        used_points = {'x': [], 'o': []}

        for _ in range(p_percent):
            random_key = random.choice(list(input_data.keys()))
            random_value = random.choice(input_data[random_key])
            index = input_data[random_key].index(random_value)

            if random_value not in used_points[random_key]:
                new_data[random_key].append((input_data[random_key][index]))
                used_points[random_key].append((input_data[random_key][index]))

        return new_data

    def get_tree(self, point_data):
        if self.random_splits == True:
            return DecisionTree(point_data, self.min_size_to_split, True)

        else:
            training_set = self.get_random_p_percent(point_data, self.p)
            return DecisionTree(training_set, self.min_size_to_split)

    def get_forest(self):
        for _ in range(self.num_trees):
            tree = self.get_tree(self.point_data)
            tree.fit(tree)
            self.forest.append(tree)

        return self.forest

    def get_majority_decision(self, unknown_point):
        predictions = {'x': 0, 'o': 0}

        for tree in self.forest:
            predictions[tree.predict(unknown_point)] += 1

        return max(predictions, key= lambda x: predictions[x])
