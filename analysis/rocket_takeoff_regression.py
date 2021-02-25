import sys
sys.path.append('src')
from polynomial_regressor import PolynomialRegressor
from matrix import Matrix
from dataframe import DataFrame
import matplotlib.pyplot as plt

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

df = DataFrame.from_array(
    [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)],
    columns = ['x', 'y']
)

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, dependent_variable='y')
print("quadratic_regressor:", "\n", quadratic_regressor.coefficients)
print("5 sec:", quadratic_regressor.predict({'x': 5}))
print("10 sec:", quadratic_regressor.predict({'x': 10}))
print("200 sec:", quadratic_regressor.predict({'x': 200}), "\n")

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, dependent_variable='y')
print("cubic_regressor:", "\n", cubic_regressor.coefficients)
print("5 sec:", cubic_regressor.predict({'x': 5}))
print("10 sec:", cubic_regressor.predict({'x': 10}))
print("200 sec:", cubic_regressor.predict({'x': 200}), "\n")

plt.style.use('bmh')
times = [n for n in range(0, 11)]
plt.plot([element[0] for element in data], [element[1] for element in data], 'ro', label="data")
plt.plot(times, [quadratic_regressor.predict({'x': t}) for t in times], label="Quadratic regressor")
plt.plot(times, [cubic_regressor.predict({'x': t}) for t in times], label="Cubic regressor")
plt.title('Rocket Takeoff Regression Plot')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend(loc="best")
plt.savefig('rocket_takeoff_regression.png')

#d. Quadratic is better. Looking at rocket_takeoff.png (where 0 <= t <= 200), we can see that the cubic regressor eventually goes into negative distance. Theoretically, a rocket at 200 seconds should still be gaining distance. However, according to our cubic regression graph, it'll lose distance and even go into the negatives in distance (which shouldn't be possible). Therefore, the quadratic regressor is better since it never goes into negative distance and keeps increasing in distance, which indicates a rockets increase in acceleration.
