class DataFrame():
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.columns = column_order

    def to_array(self):
        data_array = []
        j = 0

        for n in range(len(self.data_dict[self.columns[0]])):
            data_array.append([])

            for key in self.columns:
                data_array[j].append(self.data_dict[key][n])

            j += 1

        return data_array

    def select_columns(self, column_order):
        return DataFrame(self.data_dict, column_order)

    def select_rows(self, row_order):
        copied_dict = self.data_dict

        for key in self.columns:
            row = []

            for j in range(len(copied_dict[key])):
                if j in row_order:
                    row.append(copied_dict[key][j])

            copied_dict[key] = row

        return DataFrame(copied_dict, self.columns)

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
