import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from matrix import Matrix
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor

df = DataFrame.from_array(
    [[1, 0.2],
     [2, 0.25],
     [3, 0.5]],
    columns = ['x','y']
)

log_reg = LogisticRegressor(df, dependent_variable = 'y')
print(log_reg.coefficients)
print(log_reg.predict({'x': 5}))