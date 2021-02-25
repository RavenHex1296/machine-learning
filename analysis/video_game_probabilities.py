import sys
sys.path.append('src')
from logistic_regressor import *
from dataframe import *

data = [(10, 0.05), (100, 0.35), (1000, 0.95)]
df = DataFrame.from_array(data, ['x', 'y'])
log_reg = LogisticRegressor(df, 'y', 1)
print(log_reg.coefficients, "\n")
print(log_reg.predict({'x': 500}))
