import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from matrix import Matrix
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor

'''
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
print("Linear Regressor: ", regressor.coefficients)

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
print("Logistic Regressor: ", log_reg.coefficients, "\n")

print("Linear Regressor: ", regressor.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))

print("Logistic Regressor: ", log_reg.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 0
}), "\n")

print("Linear Regressor: ", regressor.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 0,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 4,
    'mayo * jelly': 0
}))

print("Logistic Regressor: ", log_reg.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 0,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 0,
    'pb * jelly': 4,
    'mayo * jelly': 0
}), "\n")

print("Linear Regressor: ", regressor.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))

print("Logistic Regressor: ", log_reg.predict({
    'beef': 0,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 0,
    'beef * mayo': 0,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}), "\n")

print("Linear Regressor: ", regressor.predict({
    'beef': 8,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 32,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}))

print("Logistic Regressor: ", log_reg.predict({
    'beef': 8,
    'pb': 4,
    'mayo': 1,
    'jelly': 0,
    'beef * pb': 32,
    'beef * mayo': 8,
    'beef * jelly': 0,
    'pb * mayo': 4,
    'pb * jelly': 0,
    'mayo * jelly': 0
}), "\n")

print("Linear Regressor: ", regressor.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 8,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 1
}))

print("Logistic Regressor: ", log_reg.predict({
    'beef': 8,
    'pb': 0,
    'mayo': 1,
    'jelly': 1,
    'beef * pb': 0,
    'beef * mayo': 8,
    'beef * jelly': 8,
    'pb * mayo': 0,
    'pb * jelly': 0,
    'mayo * jelly': 1
}))
