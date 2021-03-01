import sys
sys.path.append('src')
from dataframe import *
from linear_regressor import *
from polynomial_regressor import *
import matplotlib.pyplot as plt

dataset = [(-4, 11.0),
 (-2, 5.0),
 (0, 3.0),
 (2, 5.0),
 (4, 11.1),
 (6, 21.1),
 (8, 35.1),
 (10, 52.8),
 (12, 74.8),
 (14, 101.2)]

training_data = [(data[0], data[1]) for data in dataset if dataset.index(data) % 2 == 0]
testing_data = [(data[0], data[1]) for data in dataset if dataset.index(data) % 2 != 0]

training_set_df = DataFrame.from_array(training_data, ['x', 'y'])
testing_set_df = DataFrame.from_array(testing_data, ['x', 'y'])

linear_regressor = LinearRegressor(training_set_df, 'y')

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(training_set_df, 'y')

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(training_set_df, 'y')

quartic_regressor = PolynomialRegressor(degree=4)
quartic_regressor.fit(training_set_df, 'y')

linear_regressor_training_set_rss = 0
linear_regressor_testing_set_rss = 0

print("Linear Regressor:")
for data in training_data:
    linear_regressor_training_set_rss += (data[1] - linear_regressor.predict({'x': data[0]})) ** 2
print("Training set rss:", linear_regressor_training_set_rss)

for data in testing_data:
    linear_regressor_testing_set_rss += (data[1] - linear_regressor.predict({'x': data[0]})) ** 2
print("Testing set rss:", linear_regressor_testing_set_rss, "\n")

quadratic_regressor_training_set_rss = 0
quadratic_regressor_testing_set_rss = 0

print("Quadratic Regressor:")
for data in training_data:
    quadratic_regressor_training_set_rss += (data[1] - quadratic_regressor.predict({'x': data[0]})) ** 2
print("Training set rss:", quadratic_regressor_training_set_rss)

for data in testing_data:
    quadratic_regressor_testing_set_rss += (data[1] - quadratic_regressor.predict({'x': data[0]})) ** 2
print("Testing set rss:", quadratic_regressor_testing_set_rss, "\n")

cubic_regressor_training_set_rss = 0
cubic_regressor_testing_set_rss = 0

print("Cubic Regressor:")
for data in training_data:
    cubic_regressor_training_set_rss += (data[1] - cubic_regressor.predict({'x': data[0]})) ** 2
print("Training set rss:", cubic_regressor_training_set_rss)

for data in testing_data:
    cubic_regressor_testing_set_rss += (data[1] - cubic_regressor.predict({'x': data[0]})) ** 2
print("Testing set rss:", cubic_regressor_testing_set_rss, "\n")

quartic_regressor_training_set_rss = 0
quartic_regressor_testing_set_rss = 0

print("Quartic Regressor:")
for data in training_data:
    quartic_regressor_training_set_rss += (data[1] - quartic_regressor.predict({'x': data[0]})) ** 2
print("Training set rss:", quartic_regressor_training_set_rss)

for data in testing_data:
    quartic_regressor_testing_set_rss += (data[1] - quartic_regressor.predict({'x': data[0]})) ** 2
print("Testing set rss:", quartic_regressor_testing_set_rss, "\n")

plt.style.use('bmh')
plt.plot([data[0] for data in dataset], [data[1] for data in dataset], 'ro', label='data')
plt.plot([n for n in range(-4, 16)], [linear_regressor.predict({'x': n}) for n in range(-4, 16)], label='Linear Regressor')
plt.plot([n for n in range(-4, 16)], [quadratic_regressor.predict({'x': n}) for n in range(-4, 16)], label='Quadratic Regressor')
plt.plot([n for n in range(-4, 16)], [cubic_regressor.predict({'x': n}) for n in range(-4, 16)], label='Cubic Regressor')
plt.plot([n for n in range(-4, 16)], [quartic_regressor.predict({'x': n}) for n in range(-4, 16)], label='Quartic Regressor')
plt.legend(loc='best')
plt.savefig('training_and_testing_sets.png')