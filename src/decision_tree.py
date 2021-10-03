import math
import random

class DecisionTree():
    def __init__(self, data_dict, min_size_to_split):
        self.point_data = data_dict
        self.entropy = self.calculate_entropy()
        self.branches = []
        self.best_split = None
        self.min_size_to_split = min_size_to_split

    def get_all_points(self, data_dict=None):
        all_points = []

        if data_dict == None:
            data_dict = self.point_data

        for key in data_dict:
            all_points += data_dict[key]

        return all_points

    def remove_from_dict(self, input_dict, values):
        new_dict = input_dict.copy()

        if type(values) is not list:
            values = [values]

        for key in new_dict:
            new_values = []

            for value in list(new_dict[key]):
                if value in values:
                    continue

                new_values.append(value)

            new_dict[key] = new_values

        return new_dict

    def calculate_entropy(self, data_dict=None):
        entropy = 0

        if data_dict == None:
            data_dict = self.point_data

        for point_type in data_dict:
            proportion = len(data_dict[point_type]) / len(self.get_all_points(data_dict))

            if proportion == 0:
                continue

            entropy += -1 * proportion * math.log(proportion)

        return entropy

    def calculate_weighted_average(self, data):
        weighted_average = 0
        num_points = sum([len(self.get_all_points(data_dict)) for data_dict in data])

        for data_dict in data:
            weighted_average += self.calculate_entropy(data_dict) * len(self.get_all_points(data_dict)) / num_points

        return weighted_average

    def calculate_splits(self, unique_values):
        midpoints = []

        for n in range(len(unique_values) - 1):
            midpoints.append((unique_values[n] + unique_values[n + 1]) / 2)

        return midpoints

    def split(self, split_info, data_dict=None):
        set_branches = False

        if data_dict == None:
            set_branches = True
            data_dict = self.point_data

        above = [point for point in self.get_all_points(data_dict) if point[split_info[0]] >= split_info[1]]
        below = [point for point in self.get_all_points(data_dict) if point[split_info[0]] < split_info[1]]

        above_midpoint = self.remove_from_dict(data_dict, below)
        below_midpoint = self.remove_from_dict(data_dict, above)

        if set_branches:
            self.branches = [DecisionTree(above_midpoint, self.min_size_to_split), DecisionTree(below_midpoint, self.min_size_to_split)]

        return [above_midpoint, below_midpoint]

    def get_all_possible_splits(self, data_dict=None):
        possible_splits = []

        if data_dict == None:
            data_dict = self.point_data

        all_points = self.get_all_points(data_dict)

        for n in range(len(all_points[0])):
            unique = list(set([point[n] for point in all_points]))
            midpoints = self.calculate_splits(unique)

            for midpoint in midpoints:
                possible_splits.append((n, midpoint))

        return possible_splits

    def get_best_split(self, data_dict=None):
        set_best_split = False

        if data_dict == None:
            set_best_split = True
            data_dict = self.point_data

        all_splits = self.get_all_possible_splits(data_dict)
        best_split = all_splits[0]

        best_entropy = self.calculate_weighted_average(self.split(best_split, data_dict))

        for split in all_splits:
            branches = self.split(split, data_dict)
            weighted_entropy = self.calculate_weighted_average(branches)

            if weighted_entropy < best_entropy:
                best_split = split
                best_entropy = weighted_entropy

        if set_best_split:
            self.best_split = best_split

        return best_split

    def fit(self, decision_tree=None):
        if decision_tree == None:
            decision_tree = self

        if len(decision_tree.branches) != 0 or len(decision_tree.get_all_points()) <= self.min_size_to_split:
            return

        decision_tree.get_best_split()
        decision_tree.split(decision_tree.best_split)
        branches = [branch for branch in decision_tree.branches if branch.entropy != 0]
        next_branches = []

        while True:
            for branch in branches:
                if len(branch.get_all_points()) <= self.min_size_to_split or len(set(branch.get_all_points())) == 1:
                    continue

                branch.get_best_split()
                branch.split(branch.best_split)
                next_branches += [next_branch for next_branch in branch.branches if next_branch.entropy != 0]

            branches = next_branches
            next_branches = []

            if len(branches) == 0:
                break

    def get_point_type(self, decision_tree=None):
        if decision_tree == None:
            decision_tree = self

        if decision_tree.entropy != 0:
            sample_sizes = [(key, len(decision_tree.point_data[key])) for key in decision_tree.point_data]
            majority = max([sample_size[1] for sample_size in sample_sizes])
            new_lengths = [sample_size for sample_size in sample_sizes if sample_size[1] == majority]

            if len(new_lengths) > 1:
                return new_lengths[random.randint(0, len(new_lengths) - 1)][0]

            return new_lengths[0][0]

        point_type = [key for key in decision_tree.point_data.keys() if len(decision_tree.point_data[key]) != 0]
        return point_type[0]

    def predict(self, unknown_point, decision_tree=None):
        if decision_tree == None:
            decision_tree = self

        while decision_tree.entropy != 0 and len(decision_tree.get_all_points()) > self.min_size_to_split and len(set(decision_tree.get_all_points())) != 1:

            if unknown_point[decision_tree.best_split[0]] >= decision_tree.best_split[1]:
                decision_tree = decision_tree.branches[0]

            elif unknown_point[decision_tree.best_split[0]] < decision_tree.best_split[1]:
                decision_tree = decision_tree.branches[1]

        return decision_tree.get_point_type()
