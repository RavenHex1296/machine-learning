import sys
sys.path.append('src')
from dataframe import DataFrame


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
