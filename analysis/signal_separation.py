import sys
sys.path.append('src')
from dataframe import *
from linear_regressor import *
import matplotlib.pyplot as plt
import math

dataset = [(0.0, 7.0),
 (0.2, 5.6),
 (0.4, 3.56),
 (0.6, 1.23),
 (0.8, -1.03),
 (1.0, -2.89),
 (1.2, -4.06),
 (1.4, -4.39),
 (1.6, -3.88),
 (1.8, -2.64),
 (2.0, -0.92),
 (2.2, 0.95),
 (2.4, 2.63),
 (2.6, 3.79),
 (2.8, 4.22),
 (3.0, 3.8),
 (3.2, 2.56),
 (3.4, 0.68),
 (3.6, -1.58),
 (3.8, -3.84),
 (4.0, -5.76),
 (4.2, -7.01),
 (4.4, -7.38),
 (4.6, -6.76),
 (4.8, -5.22)]

updated_dataset = []

for data in dataset:
    updated_dataset.append([math.sin(data[0]), math.cos(data[0]), math.sin(2 * data[0]), math.cos(2 * data[0]), data[1]])

columns = ['sin(x)', 'cos(x)', 'sin(2x)', 'cos(2x)', 'y']

df = DataFrame.from_array(updated_dataset, columns)
regressor = LinearRegressor(df, 'y')


def signal_transformation(x):
    constant = regressor.coefficients['constant']
    sin_x = regressor.coefficients['sin(x)'] * math.sin(x)
    cos_x = regressor.coefficients['cos(x)'] * math.cos(x)
    sin_2x = regressor.coefficients['sin(2x)'] * math.sin(2*x)
    cos_2x = regressor.coefficients['cos(2x)'] * math.cos(2*x)
    return constant + sin_x + cos_x + sin_2x + cos_2x

plt.style.use('bmh')
plt.plot([data[0] for data in dataset], [data[1] for data in dataset], 'ro', label='data')
plt.plot([data[0] for data in dataset], [signal_transformation(data[0]) for data in dataset], label='Plotted curve')
plt.legend(loc='best')
plt.savefig('signal_separation.png')
