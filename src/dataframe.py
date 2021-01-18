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

    def to_array(self):
        result = []
        counter = 0
        for j in range(len(self.data_dict[self.columns[0]])):
            result.append([])
            for key in self.columns:
                result[counter].append(self.data_dict[key][j])
            counter += 1
        return result

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

    @classmethod
    def from_array(cls, arr, columns):
        data_dict = {}

        for i in range(len(columns)):
            data_dict[columns[i]] = []

            for j in range(len(arr)):
                data_dict[columns[i]].append(arr[j][i])

        return cls(data_dict, columns)

    def arr_row_to_dict(self, row, columns):
        data_dict = {}

        for i in range(len(columns)):
            data_dict[columns[i]] = row[i]

        return data_dict

    def select_rows_where(self, function):
        copied_arr = self.to_array()
        rows = []

        for row in copied_arr:
            row_dict = self.arr_row_to_dict(row, self.columns)

            if function(row_dict):
                rows.append(row)

            else:
                continue

        return DataFrame.from_array(rows, self.columns)

    def order_by(self, key, ascending):
        copied_arr = self.to_array()
        key_index = self.columns.index(key)
        new_arr = []

        while len(copied_arr) > 0:
            last_row = copied_arr[0]

            for row in copied_arr:
                if row[key_index] < last_row[key_index]:
                    last_row = row

            new_arr.append(last_row)
            copied_arr.remove(last_row)

        if ascending:
            return DataFrame.from_array(new_arr, self.columns)

        else:
            return DataFrame.from_array(new_arr[::-1], self.columns)

    @classmethod
    def from_csv(cls, path_to_csv, header):
        with open(path_to_csv, "r") as file:
            data = {}
            columns = []
            splitted_file = []

            for row in file.read().split('\n'):
                splitted_file.append(row.split(', '))

            for element in splitted_file[0]:
                columns.append(element)

        for n in range(len(columns)):
            data[columns[n]] = []

            for num in range(len(splitted_file)):
                data[columns[n]].append(splitted_file[num][n])

        for key in data:
            data[key] = data[key][1:]

        return cls(data, columns)

    def create_interaction_terms(self, column_1, column_2):
        data = {}
        new_terms = []

        for key in self.data_dict:
            data[key] = self.data_dict[key]

        for column in self.columns:
            new_terms.append(column)


        new_terms.append(column_1 + ' * ' + column_2)
        first_column = self.data_dict[column_1]
        second_column = self.data_dict[column_2]

        interaction_terms = []

        for n in range(len(first_column)):
            interaction_terms.append(first_column[n] * second_column[n])

        data[column_1 + ' * ' + column_2] = interaction_terms

        return DataFrame(data, new_terms)
