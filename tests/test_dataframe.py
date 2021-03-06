import sys
sys.path.append('src')
from dataframe import DataFrame

''''
data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, ['Pete', 'John', 'Sarah'])

print("Asserting method 'data_dict'")
assert df1.data_dict == {'Pete': [1, 0, 1, 0], 'John': [2, 1, 0, 2], 'Sarah': [3, 1, 4, 0]}
print("PASSED")

print("Asserting columns")
assert df1.columns == ['Pete', 'John', 'Sarah']
print("PASSED")

print("Asserting method 'to_array'")
assert df1.to_array() == [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]]
print("PASSED")

df2 = df1.select_columns(['Sarah', 'Pete'])

print("Asserting to_array")
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]]
print("PASSED")

print("Asserting columns")
assert df2.columns == ['Sarah', 'Pete']
print("PASSED")

df3 = df1.select_rows([1, 3])

print("Asserting method 'to_array'")
assert df3.to_array() == [[0, 1, 1], [0, 2, 0]]
print("PASSED")


data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])
df2 = df1.apply('John', lambda x: 7 * x)

print("Asserting method 'apply'")
assert df2.data_dict == {
    'Pete': [1, 0, 1, 0],
    'John': [14, 7, 0, 14],
    'Sarah': [3, 1, 4, 0]
}, "Incorrect output"
print("PASSED")

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13], ['Sylvia', 'Mendez', 9]]

df = DataFrame.from_array(arr, columns)

print("Asserting method 'select_rows_where'")
assert df.select_rows_where(lambda row: len(row['firstname']) >= len(row['lastname']) and row['age'] > 10).to_array() == [['Charles', 'Trapp', 17]], "Incorrect output"
print("PASSED")

print("Asserting method 'to_array'")
assert df.order_by('age', True).to_array() == [['Kevin', 'Fray', 5], ['Sylvia', 'Mendez', 9], ['Anna', 'Smith', 13], ['Charles', 'Trapp', 17]], "Incorrect output"
print("PASSED")

print("Asserting method 'order_by'")
assert df.order_by('firstname', False).to_array() == [['Sylvia', 'Mendez', 9], ['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13]], "Incorrect output"
print("PASSED")


path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'airtravel.csv' 
filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath, True)

print(df.columns)
print(df.to_array())


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
print("Asserting create_dummy_variables")
assert df.columns == ['beef', 'pb', 'mayo', 'jelly', 'rating']
assert df.to_array() == [[0, 0, 0, 0, 1],
[0, 0, 1, 0, 1],
[0, 0, 0, 1, 4],
[0, 0, 1, 1, 0],
[5, 0, 0, 0, 4],
[5, 0, 1, 0, 8],
[5, 0, 0, 1, 1],
[5, 0, 1, 1, 0],
[0, 5, 0, 0, 5],
[0, 5, 1, 0, 0],
[0, 5, 0, 1, 9],
[0, 5, 1, 1, 0],
[5, 5, 0, 0, 0],
[5, 5, 1, 0, 0],
[5, 5, 0, 1, 0],
[5, 5, 1, 1, 0]]
print("PASSED")


df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)
assert df.select(['firstname','age']).to_array() == [['Kevin', 5],
['Charles', 17],
['Anna', 13],
['Sylvia', 9]]

assert df.where(lambda row: row['age'] > 10).to_array() == [['Charles', 'Trapp', 17],
['Anna', 'Smith', 13]]

assert df.select(['firstname','age']).order_by('firstname', ascending=True).to_array() == [['Anna', 13],
['Charles', 17],
['Kevin', 5],
['Sylvia', 9]]

assert df.select(['firstname', 'age']).order_by('firstname', ascending=False).to_array() == [['Sylvia', 9],
['Kevin', 5],
['Charles', 17],
['Anna', 13]]

assert df.select(['firstname','age']).where(lambda row: row['age'] > 10).order_by('age', ascending=True).to_array() == [['Anna', 13],
['Charles', 17]]

df = DataFrame.from_array(
    [
        ['Kevin Fray', 52, 100],
        ['Charles Trapp', 52, 75],
        ['Anna Smith', 52, 50],
        ['Sylvia Mendez', 52, 100],
        ['Kevin Fray', 53, 80],
        ['Charles Trapp', 53, 95],
        ['Anna Smith', 53, 70],
        ['Sylvia Mendez', 53, 90],
        ['Anna Smith', 54, 90],
        ['Sylvia Mendez', 54, 80],
    ],
    columns = ['name', 'assignmentId', 'score']
)

assert df.group_by('name').to_array() == [
    ['Kevin Fray', [52, 53], [100, 80]],
    ['Charles Trapp', [52, 53], [75, 95]],
    ['Anna Smith', [52, 53, 54], [50, 70, 90]],
    ['Sylvia Mendez', [52, 53, 54], [100, 90, 80]],
]

assert df.group_by('name').aggregate('score', 'count').to_array() == [
    ['Kevin Fray', [52, 53], 2],
    ['Charles Trapp', [52, 53], 2],
    ['Anna Smith', [52, 53, 54], 3],
    ['Sylvia Mendez', [52, 53, 54], 3],
]

assert df.group_by('name').aggregate('score', 'max').to_array() == [
    ['Kevin Fray', [52, 53], 100],
    ['Charles Trapp', [52, 53], 95],
    ['Anna Smith', [52, 53, 54], 90],
    ['Sylvia Mendez', [52, 53, 54], 100],
]

assert df.group_by('name').aggregate('score', 'min').to_array() == [
    ['Kevin Fray', [52, 53], 80],
    ['Charles Trapp', [52, 53], 75],
    ['Anna Smith', [52, 53, 54], 50],
    ['Sylvia Mendez', [52, 53, 54], 80],
]

assert df.group_by('name').aggregate('score', 'sum').to_array() == [
    ['Kevin Fray', [52, 53], 180],
    ['Charles Trapp', [52, 53], 170],
    ['Anna Smith', [52, 53, 54], 210],
    ['Sylvia Mendez', [52, 53, 54], 270],
]

assert df.group_by('name').aggregate('score', 'avg').to_array() == [
    ['Kevin Fray', [52, 53], 90],
    ['Charles Trapp', [52, 53], 85],
    ['Anna Smith', [52, 53, 54], 70],
    ['Sylvia Mendez', [52, 53, 54], 90],
]

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age'])
assert df.query('SELECT firstname, age').to_array() == [
    ['Kevin', 5], ['Charles', 17], ['Anna', 13], ['Sylvia', 9]]
'''

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

print("Asserting that query supports ORDER BY")

assert df.query("SELECT lastname, firstname, age ORDER BY age DESC").to_array() == [['Trapp', 'Charles', 17],
['Smith', 'Anna', 13],
['Mendez', 'Sylvia', 9],
['Fray', 'Kevin', 5]]

assert df.query("SELECT firstname ORDER BY lastname ASC").to_array() == [['Kevin'],
['Sylvia'],
['Anna'],
['Charles']]

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Melvin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Carl', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Hannah', 'Smith', 13],
    ['Sylvia', 'Mendez', 9],
    ['Cynthia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query("SELECT lastname, firstname, age ORDER BY age ASC, firstname DESC").to_array() == [['Fray', 'Melvin', 5],
['Fray', 'Kevin', 5],
['Mendez', 'Sylvia', 9],
['Mendez', 'Cynthia', 9],
['Smith', 'Hannah', 13],
['Smith', 'Anna', 13],
['Trapp', 'Charles', 17],
['Trapp', 'Carl', 17]]

print("PASSED")
