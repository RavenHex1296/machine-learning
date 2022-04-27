from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import time
import sys
sys.path.append('datasets')
from semi_random_data import *
import matplotlib.pyplot as plt
import time



'''
accuracies = []
min_size_to_split_values = [2, 5, 10, 15, 20, 30, 50, 100, 200, 250, 300]

for min_size_to_split in min_size_to_split_values:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    dt = DecisionTreeClassifier(min_samples_split=min_size_to_split, random_state=1)
    dt.fit(X_train, y_train)
    y_predict = dt.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_predict))

plt.style.use('bmh')
plt.plot(min_size_to_split_values, accuracies)
plt.xlabel('min_size_to_split')
plt.ylabel('5-fold Cross Valiation Accuracy')
plt.savefig('sklearn_dt_plot.png')

num_trees = [1, 10, 20, 50, 100, 500, 1000]

for num_tree in num_trees:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    rf = RandomForestClassifier(n_estimators=num_tree)
    rf.fit(X_train,y_train)
    y_predict = rf.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_predict))

plt.style.use('bmh')
plt.plot(num_trees, accuracies)
plt.xlabel('num_trees')
plt.ylabel('5-fold Cross Valiation Accuracy')
plt.savefig('sklearn_rf_plot.png')

'''

start_time = time.time()
point_data = get_semi_random_data(200)
point_data_dict = point_data.copy()
x_values = []
y_values = []
point_types = []

for point_type in point_data:
    for point in point_data[point_type]:
        point_types.append(point_type)
        x_values.append(point[0])
        y_values.append(point[1])

point_data = {'x_value': x_values, 'y_value': y_values, 'point_type': point_types}

point_data = pd.DataFrame.from_dict(point_data)
X = point_data[['x_value', 'y_value']]
y = point_data['point_type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train,y_train)


test_points = {'x_value': [random.uniform(-6, 6) for _ in range(2500)], 'y_value': [random.uniform(-6, 6) for _ in range(2500)]}
test_point_predictions = {'x': [], 'o': []}
test_points = pd.DataFrame.from_dict(test_points)
predicted_point_types = rf.predict(test_points)

for n in range(0, len(predicted_point_types)):
    x = test_points['x_value'][n]
    y = test_points['y_value'][n]
    test_point_predictions[predicted_point_types[n]].append((x, y))

plt.style.use('bmh')
plt.scatter([point[0] for point in test_point_predictions['x']], [point[1] for point in test_point_predictions['x']], s=25,c='lightcoral')
plt.scatter([point[0] for point in test_point_predictions['o']], [point[1] for point in test_point_predictions['o']], s=25,c='lightblue')
plt.scatter([point[0] for point in point_data_dict['x']], [point[1] for point in point_data_dict['x']], s=75, c='red')
plt.scatter([point[0] for point in point_data_dict['o']], [point[1] for point in point_data_dict['o']], s=75,c='blue')
plt.savefig('rf.png')
print(time.time() - start_time)