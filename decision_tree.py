import math
'''
class Point():
    def __init__(self, point_type, location):
        self.point_type = point_type
        self.location = location
'''
class DecisionTree():
    def __init__(self, data):
        self.point_data = data
        self.set_points(data)
        self.possible_splits = self.get_all_possible_splits()
        self.best_split = self.get_best_split()
        self.branches = []
'''
    def set_points(self, data_dict):
        for key in data_dict:
            for point in point_data[key]:
                point = Point(key, point)
'''
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

            new_dict[key] = new_items

        return new_dict

    def get_all_points(self, data_dict):
        all_points = []

        for key in data_dict:
            all_points += data_dict[key]

        return all_points

    def calculate_entropy(self, data_dict):
        entropy = 0

        for point_type in data_dict:
            p = len(data_dict[point_type]) / len(self.get_all_points(data_dict))
            entropy += -1 * p * math.log(p, math.e)

        return entropy

    def calculate_weighted_average(self, data_dict):
        num_values = len(self.get_all_points(data_dict))
        #have to figure out how to actually carry out the split

    def get_all_unique_x_values(self):
        x_vales = [data[0] for data in self.get_all_points() if data[0] not in x_values]
        return x_values

    def get_all_unique_y_values(self):
        y_values = [data[1] for data in self.get_all_points() if data[1] not in y_values]
        return y_values

    def get_all_possible_splits(self):
        possible_splits = {0: [], 1: []}

        x_values = self.get_all_unique_x_values().sort()
        y_values = self.get_all_unique_y_values().sort()

        for n in range(len(x_values) - 1):
            possible_splits[0].append((x_values[n] + x_values[n + 1]) / 2)
            possible_splits[1].append((y_values[n] + y_values[n + 1]) / 2)

        return possible_splits

    def split(self, split_info, data_dict):
        above_midpoint = [point for point  in self.get_all_points(data_dict) if point[split_tuple[0]] >= split_tuple[1]]
        below_midpoint = [point for point in self.get_all_points(data_dict) if point[split_tuple[0]] < split_tuple[1]]

        above_dict = self.remove_from_dict(point_dict, lesser)
        below_dict = self.remove_from_dict(point_dict, greater)

        return [DecisionTree(above_dict), DecisionTree(below_dict)]

    def get_best_split():
        for key in self.possible_splits():
            for n in range(0, len(self.get_all_possible_splits[key])):
                midpoint = self.get_all_possible_splits[key][n]

                above_midpoint = []
                below_midpoint = []

                for point in self.get_all_points(self.get_all_points):
                    if point[key] > midpoint:
                        above_midpoint.append(point)

                    if point[key] < midpoint:
                        below_midpoint.append(point)

                for point in above_midpoint: