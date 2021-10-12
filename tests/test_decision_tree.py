import sys
sys.path.append('datasets')
from semi_random_data import *
sys.path.append('src')
from decision_tree import *
import math
import random
#import matplotlib.pyplot as plt
'''
data = {'x': [(2, 1), (2, 2), (3, 2), (3, 3)], 'o': [(2, 3), (2, 4), (3, 4)]}

decision_tree = DecisionTree(data)
assert decision_tree.point_data == data
assert round(decision_tree.entropy, 3) == 0.683
assert decision_tree.get_best_split() == (1, 2.5)

decision_tree.fit()
assert decision_tree.predict((0, -1)) == 'x'
assert decision_tree.predict((5, 6)) == 'o'
assert decision_tree.predict((2, 3)) == 'o'
assert decision_tree.predict((5, 3)) == 'x'


data = {'x': [(1, 3), (1, 2), (2, 2)], 'o': [(1, 1), (2, 1), (3, 1), (3, 2)]}

decision_tree = DecisionTree(data)
assert decision_tree.point_data == data
assert round(decision_tree.entropy, 3) == 0.683
assert decision_tree.get_best_split() == (1, 1.5)

decision_tree.fit()
assert decision_tree.predict((100, 100)) == 'o'
assert decision_tree.predict((-10, -10)) == 'o'
assert decision_tree.predict((1, 3)) == 'x'

print('PASSED')

data = {'x': [(1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (7, 1)], 'o': [(1, 9), (5, 3), (6, 3), (7, 3), (5, 2), (5, 1)]}
decision_tree = DecisionTree(data, 7)
decision_tree.fit()

assert decision_tree.predict((2, 8)) == 'x'
assert decision_tree.predict((6, 2)) == 'o'
assert decision_tree.predict((-10, 2)) == 'x'
assert decision_tree.predict((100, 2)) == 'o'
assert decision_tree.predict((4, 5)) == 'o'
assert len(decision_tree.branches[0].branches) == 0
assert len(decision_tree.branches[1].branches) == 0

data = {'x': [(1, 5), (2, 5), (1, 3), (2, 4)], 'o': [(1, 4), (2, 3)]}

decision_tree = DecisionTree(data, 5)
decision_tree.fit()
assert decision_tree.predict((2, 8)) == 'x'
assert decision_tree.predict((-10, 100)) == 'x'

random.seed(0)
initial_prediction = decision_tree.predict((-2, -5))

for n in range(-10, 4):
    random.seed(0)
    assert decision_tree.predict((0, n)) == initial_prediction

assert decision_tree.predict((2, 5)) == 'x'
assert decision_tree.predict((0, 10)) == 'x'
assert len(decision_tree.branches[0].branches) == 0
assert len(decision_tree.branches[1].branches) == 0

data = {'x': [(0, 1), (0, 1), (0, 2), (1, 1), (1, 2), (1, 2)], 'o': [(0, 2), (1, 1), (1, 1), (1, 2)]}
decision_tree = DecisionTree(data, 1)
decision_tree.fit()

assert decision_tree.predict((3, 5)) == 'x'
assert decision_tree.predict((0, 0)) == 'x'
assert decision_tree.predict((3, 1)) == 'o'

random.seed(0)
initial_prediction = decision_tree.predict((0, 4))

for n in range(-10, 0):
    for num in range(2, 12):
        random.seed(0)
        assert decision_tree.predict((n, num)) == initial_prediction

print('PASSED')

def remove_from_dict(input_dict, key, value):
    new_dict = input_dict.copy()
    new_items = new_dict[key].remove(value)
    new_dict[key] = new_items
    return new_dict


def add_to_dict(points):
    new_dict = {key:[] for key in points[0]}

    for point_dict in points:
        for key in point_dict:
            new_dict[key] += point_dict[key]

    return new_dict


def get_all_points(point_data):
    all_points = []

    for key in point_data:
        all_points += point_data[key]

    return all_points


def random_fold(point_data, fold_size):
    keys = list(point_data.keys())
    fold = {key:[] for key in keys}

    for _ in range(fold_size):
        key = keys[random.randint(0, len(keys) - 1)]

        if len(point_data[key]) == 0:
            keys.remove(key)
            key = keys[random.randint(0, len(keys) - 1)]

        values = point_data[key]
        value = values[random.randint(0, len(values) - 1)]
        fold[key].append(value)
        remove_from_dict(point_data, key, value)

    return fold


def get_multiple_folds(fold_number, point_data, fold_size):
    folds = []

    for _ in range(fold_number):
        folds.append(random_fold(point_data, fold_size))

    return folds


def get_accuracy(decision_tree, test_points):
    all_predictions = 0
    correct_predictions = 0

    for key in test_points:
        for point in test_points[key]:
            if decision_tree.predict(point) == key:
                correct_predictions += 1

            all_predictions += 1

    return correct_predictions / all_predictions


def get_traning_set(training_folds, testing_fold):
    points = [fold for fold in all_folds if fold != testing_fold]
    return add_to_dict(points)


all_folds = get_multiple_folds(5, point_data, 40)

min_size_to_split_values = [1, 2, 5, 10, 15, 20, 30, 50, 100]

accuracies = []

for min_size_to_split in min_size_to_split_values:
    accuracy = 0

    for fold in all_folds:
        training_set = get_traning_set(all_folds, fold)
        decision_tree = DecisionTree(training_set, min_size_to_split)
        decision_tree.fit()
        accuracy += get_accuracy(decision_tree, fold)

    accuracy /= len(all_folds)
    accuracies.append(accuracy)


plt.style.use('bmh')
plt.plot([min_size_to_split for min_size_to_split in min_size_to_split_values], [accuracy for accuracy in accuracies])
plt.xlabel('min_size_to_split')
plt.ylabel('5-fold Cross Valiation Accuracy')
plt.savefig('test.png')
'''

data = {'x': [(1, 5), (2, 5), (1, 3), (2, 4)], 'o': [(1, 4), (2, 3)]}
'''
decision_tree = DecisionTree(data, 5)
random_tree = DecisionTree(data, 1, True)
assert decision_tree.predict((2, 8)) == random_tree.predict((2, 8))
assert decision_tree.predict((-10, 100)) == 'x'
'''

random_tree = DecisionTree(data, 1, True)
print(random_tree.random_splits)