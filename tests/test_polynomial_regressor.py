import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix
from dataframe import DataFrame

df = DataFrame.from_array(
    [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)],
    columns = ['x', 'y']
)

constant_regressor = PolynomialRegressor(degree=0)
constant_regressor.fit(df, dependent_variable='y')
print("constant_regressor coefficients:", (constant_regressor.coefficients))
print("constant_regressor prediction:", constant_regressor.predict({'x': 2}), "\n")

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(df, dependent_variable='y')
print("linear_regressor coefficients:", (linear_regressor.coefficients))
print("linear_regressor prediction:", linear_regressor.predict({'x': 2}), "\n")

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, dependent_variable='y')
print("quadratic_regressor coefficients:", (quadratic_regressor.coefficients))
print("quadratic_regressor prediction:", quadratic_regressor.predict({'x': 2}), "\n")

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, dependent_variable='y')
print("cubic_regressor coefficients:", (cubic_regressor.coefficients))
print("cubic_regressor prediction:", cubic_regressor.predict({'x': 2}), "\n")

quintic_regressor = PolynomialRegressor(degree=5)
quintic_regressor.fit(df, dependent_variable='y')
print("quintic_regressor coefficients:", (quintic_regressor.coefficients))
print("quintic_regressor prediction:", quintic_regressor.predict({'x': 2}), "\n")
