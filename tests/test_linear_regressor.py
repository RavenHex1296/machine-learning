import sys
sys.path.append('src')
from linear_regressor import *
from matrix import *
from dataframe import *

'''
df = DataFrame.from_array([[1,0.2], [2,0.25], [3,0.5]], columns = ['hours worked', 'progress'])
regressor = LinearRegressor(df, 'progress')

print("Asserting method 'calculate_coefficients'")
assert regressor.coefficients.round(6).elements == [[0.01667], [0.15]], "Incorrect output"
print("PASSED")

print("Asserting method 'predict'")
assert round(regressor.predict({'hours worked': 4}), 5) == 0.61667, "Incorrect output"
print("PASSED")



df = DataFrame.from_array([[0, 0, 0.1], [1, 0, 0.2], [0, 2, 0.5], [4,5,0.6]], columns = ['scoops of chocolate', 'scoops of vanilla', 'taste rating'])
regressor = LinearRegressor(df, 'taste rating')

coefficients = regressor.coefficients
for key in coefficients:
    coefficients[key] = round(coefficients[key], 8)

print("Asserting method 'calculate_coefficients'")
assert coefficients == {
    'constant': 0.19252336,
    'scoops of chocolate': -0.05981308,
    'scoops of vanilla': 0.13271028
    }, "Incorrect output"
print("PASSED")

print("Asserting method 'predict'")
assert round(regressor.predict({
    'scoops of chocolate': 2,
    'scoops of vanilla': 3
    }), 8) == 0.47102804, "Incorrect output"
print("PASSED")


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
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating']
)
df = df.create_interaction_terms('beef', 'pb')
regressor = LinearRegressor(df, 'rating')

print(regressor.coefficients)

print(regressor.predict({
    'beef': 5,
    'pb': 0,
    'beef * pb': 0
}))

print(regressor.predict({
    'beef': 5,
    'pb': 5,
    'beef * pb': 25
}))
'''

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)

df = df.create_dummy_variables('condiments')

df = df.create_interaction_terms('beef', 'pb')
df = df.create_interaction_terms('beef', 'mayo')
df = df.create_interaction_terms('beef', 'jelly')
df = df.create_interaction_terms('pb', 'mayo')
df = df.create_interaction_terms('pb', 'jelly')
df = df.create_interaction_terms('mayo', 'jelly')

regressor = LinearRegressor(df, 'rating')

print("Asserting updated observations for LinearRegressor class")

observation = {'beef': 8, 'mayo': 1}
assert round(regressor.predict(observation), 2) == 11.34

observation = {'beef': 8, 'pb': 4, 'mayo': 1}
assert round(regressor.predict(observation), 2) == 3.62


observation = {'beef': 8, 'mayo': 1, 'jelly': 1}
assert round(regressor.predict(observation), 2) == 2.79

print("PASSED")
