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
'''

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0.1],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0.1],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0.1],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0.1],
    [5, 5, [],                0.1],
    [5, 5, ['mayo'],          0.1],
    [5, 5, ['jelly'],         0.1],
    [5, 5, ['mayo', 'jelly'], 0.1]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)

df = df.create_dummy_variables('condiments')

df = df.create_interaction_terms('beef', 'pb')
df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo')
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')


log_reg = LogisticRegressor(df, 'rating', 10)

print("Asserting updated observations for LogisticRegressor class")

observation = {'beef': 8, 'mayo': 1}
assert round(log_reg.predict(observation), 2) == 9.72

observation = {'beef': 8, 'pb': 4, 'mayo': 1}
assert round(log_reg.predict(observation), 2) == 0.77

observation = {'beef': 8, 'mayo': 1, 'jelly': 1}
assert round(log_reg.predict(observation), 2) == 0.79

print("PASSED")
