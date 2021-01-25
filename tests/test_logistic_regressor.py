import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor
'''
df = DataFrame.from_array(
    [[1, 0.2],
     [2, 0.25],
     [3, 0.5]],
    columns = ['x','y']
)

log_reg = LogisticRegressor(df, dependent_variable = 'y')
print(log_reg.coefficients)
print(log_reg.predict({'x': 5}))
'''

df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0.1],
    [3, 4, 0.1]],
    columns = ['beef', 'pb', 'rating'])

df = df.create_interaction_terms('beef', 'pb')

log_reg = LogisticRegressor(df, dependent_variable = 'rating', upper_bound = 10)
print(log_reg.coefficients, "\n")

print(log_reg.predict({
    'beef': 5,
    'pb': 0,
    'beef * pb': 0}), "\n")

print(log_reg.predict({
    'beef': 12,
    'pb': 0,
    'beef * pb': 0}), "\n")

print(log_reg.predict({
    'beef': 5,
    'pb': 5,
    'beef * pb': 5*5
}))
