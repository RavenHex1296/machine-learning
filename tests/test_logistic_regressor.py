import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor
import matplotlib.pyplot as plt
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

#assignment 76 part (a)
df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    ['x', 'y'])

plt.style.use('bmh')
plt.plot([x for x, y in df.to_array()], [y for x, y in df.to_array()],'ro')

def hack(dataframe, y, delta):
    hacky_data = []

    for row in dataframe.to_array():
        if row[dataframe.columns.index(y)] == 0:
            row[dataframe.columns.index(y)] += delta

        elif row[dataframe.columns.index(y)] == 1:
            row[dataframe.columns.index(y)] -= delta

        hacky_data.append(row)

    return DataFrame.from_array(hacky_data, dataframe.columns)

logistic_regressor = LogisticRegressor(hack(df, 'y', 0.1), 'y', 1)
plt.plot([n * 0.01 for n in range(501)], [logistic_regressor.predict({'x': n * 0.01}) for n in range(501)], label='0.1')

logistic_regressor2 = LogisticRegressor(hack(df, 'y', 0.01), 'y', 1)
plt.plot([n * 0.01 for n in range(501)], [logistic_regressor2.predict({'x':n * 0.01}) for n in range(501)], label='0.01')

logistic_regressor3 = LogisticRegressor(hack(df, 'y', 0.001), 'y', 1)
plt.plot([n * 0.01 for n in range(501)], [logistic_regressor3.predict({'x': n * 0.01}) for n in range(501)], label='0.001')

logistic_regressor4 = LogisticRegressor(hack(df, 'y', 0.0001), 'y', 1)
plt.plot([n * 0.01 for n in range(501)], [logistic_regressor4.predict({'x': n * 0.01}) for n in range(501)], label='0.0001')
plt.legend(loc='best')
plt.savefig('hacky_logistic_regressor.png')

'''
df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    columns = ['x', 'y'])

reg = LogisticRegressor(df, dependent_variable='y', upper_bound=1)

reg.set_coefficients({'constant': 0.5, 'x': 0.5})

alpha = 0.01
delta = 0.01
num_steps = 20000
reg.gradient_descent(alpha, delta, num_steps)

print(reg.coefficients)

plt.style.use('bmh')
plt.plot([x for x, y in df.to_array()], [y for x, y in df.to_array()],'ro')
plt.plot([n * 0.01 for n in range(501)], [reg.predict({'x': n * 0.01}) for n in range(501)], label='Gradient descent')
plt.legend(loc='best')
plt.savefig('logistic_regressor_gradient_descent.png')
