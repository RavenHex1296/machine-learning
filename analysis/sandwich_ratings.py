import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from matrix import Matrix
from dataframe import DataFrame

df = DataFrame.from_array([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]], columns = ['Slices of Roast Beef', 'Tablespoons of Peanut Butter', 'Rating'])
regressor = LinearRegressor(df, 'Rating')

print("Coefficients: " + str(regressor.coefficients))

print("Predicted rating of a sandwich with  5  slices of roast beef and no peanut butter: " + str(regressor.predict({
    'Slices of Roast Beef': 5,
    'Tablespoons of Peanut Butter': 0
    })))

print("Predicted rating of a sandwich with  5  slices of roast beef and 5 tablespoons of peanut butter: " + str(regressor.predict({
    'Slices of Roast Beef': 5,
    'Tablespoons of Peanut Butter': 5
    })))
