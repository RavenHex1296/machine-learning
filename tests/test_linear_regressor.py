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
'''


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
