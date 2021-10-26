import sys
sys.path.append('datasets')
from semi_random_data import *
sys.path.append('src')
from decision_tree import *
import matplotlib.pyplot as plt
from random_forest import *
import math
import time

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
        key = random.choice(keys)

        if len(point_data[key]) == 0:
            keys.remove(key)
            key = random.choice(keys)

        values = point_data[key]
        value = random.choice(values)
        fold[key].append(value)
        remove_from_dict(point_data, key, value)

    return fold


def get_multiple_folds(fold_number, point_data, fold_size):
    folds = []

    for _ in range(fold_number):
        folds.append(random_fold(point_data, fold_size))

    return folds


def get_accuracy(forest, test_points):
    all_predictions = 0
    correct_predictions = 0

    for key in test_points:
        for point in test_points[key]:
            if forest.get_majority_decision(point) == key:
                correct_predictions += 1

            all_predictions += 1

    return correct_predictions / all_predictions


def get_training_set(training_folds, testing_fold):
    points = [fold for fold in all_folds if fold != testing_fold]
    return add_to_dict(points)


'''
point_data = get_semi_random_data(200)
all_folds = get_multiple_folds(5, point_data, 40)
num_trees = [1, 10, 20, 50, 100, 500, 1000]
accuracies = []

start_time = time.time()

for num_tree in num_trees:
    accuracy = 0

    for fold in all_folds:
        training_set = get_training_set(all_folds, fold)
        forest = RandomForest(training_set, 1, num_tree, True)
        forest.get_forest()
        accuracy += get_accuracy(forest, fold)

    accuracy /= len(all_folds)
    accuracies.append(accuracy)

print(time.time() - start_time)


plt.style.use('bmh')
plt.plot(num_trees, accuracies)
plt.xlabel('num_trees')
plt.ylabel('5-fold Cross Valiation Accuracy')
plt.savefig('random_split_forest.png')


'''
point_data = get_semi_random_data(200)
all_folds = get_multiple_folds(5, point_data, 40)
num_trees = [1, 10, 20, 50, 100, 500]
accuracies = []

start_time = time.time()

for num_tree in num_trees:
    accuracy = 0

    for fold in all_folds:
        training_set = get_training_set(all_folds, fold)
        forest = RandomForest(training_set, 10, num_tree, random_splits=None, p=0.8)
        forest.get_forest()
        accuracy += get_accuracy(forest, fold)

    accuracy /= len(all_folds)
    accuracies.append(accuracy)

print(time.time() - start_time)

plt.style.use('bmh')
plt.plot(num_trees, accuracies)
plt.xlabel('num_trees')
plt.ylabel('5-fold Cross Valiation Accuracy')
plt.savefig('random_tree_best_split.png')
