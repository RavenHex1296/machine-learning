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

    def apply(self, key, function):
        applied_dict = self.data_dict
        old_list = applied_dict[key]
        applied_dict[key] = []
        updated_values = applied_dict[key]

        for element in old_list:
            updated_values.append(function(element))

        return DataFrame(applied_dict, self.columns)
