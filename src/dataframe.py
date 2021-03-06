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

    def select(self, column_order):
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

    def where(self, function):
        copied_arr = self.to_array()
        rows = []

        for row in copied_arr:
            row_dict = self.arr_row_to_dict(row, self.columns)

            if function(row_dict):
                rows.append(row)

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

        return DataFrame.from_array(new_arr[::-1], self.columns)

    @classmethod
    def from_csv(cls, path_to_csv, header, data_types, parser):
        with open(path_to_csv, "r") as file:
            splitted_file = []

            for n in file.read().split('\n'):
                splitted_file.append(n.split(',  '))

            columns = parser(splitted_file[0][0].split(', ')[0])
            parsed_file = []

            for row in splitted_file[1:]:
                if row != [""]:
                    parsed_file.append(parser(row[0]))

            data = [[data_types[columns[n]](row[n]) if row[n] != "" else None for n in range(len(columns))] for row in parsed_file]

        return cls.from_array(data, columns)

    def create_interaction_terms(self, column_1, column_2):
        data = self.data_dict.copy()
        new_terms = [column for column in self.columns]
        new_key = column_1 + ' * ' + column_2
        new_terms.append(new_key)
        data[new_key] = [data[column_1][n] * data[column_2][n] for n in range(len(data[column_1]))]

        return DataFrame(data, new_terms)

    def create_dummy_variables(self, dummy_variables):
        dummy_column = []
        dummys = []
        columns = []
        data = dict(self.data_dict)

        for variable in self.data_dict[dummy_variables]:
            dummy_column.append(variable)
        
        for dummy in dummy_column:
            for variable in dummy:
                if variable not in dummys:
                    dummys.append(variable)


        for column in self.columns:
            if column == dummy_variables:
                for variable in dummys:
                    columns.append(variable)

            else:
                columns.append(column)

        for dummy_variable in dummys:
            data[dummy_variable] = []

            for variables in dummy_column:
                if dummy_variable in variables:
                    data[dummy_variable].append(1)

                else:
                    data[dummy_variable].append(0)

        return DataFrame(data, columns)

    def convert_column_type(self, column_name, new_type):
        converted_column = []

        for element in self.data_dict[column_name]:
            if element == None:
                converted_column.append(None)
                continue

            try:
                converted_column.append(new_type(element))

            except ValueError:
                if '.' in element:
                    return None

                else:
                    converted_column.append(None)

            except TypeError:
                return None

        self.data_dict[column_name] = converted_column

    def group_by(self, colname):
        data = {}
        groups = []

        for item in self.data_dict[colname]:
            if item not in groups:
                groups.append(item)

        columns = [colname] + [column for column in self.columns]

        for column in columns:
            col_index = self.columns.index(column)

            if column == colname:
                data[column] = groups
                continue

            grouped_column = []

            for group in groups:
                grouped_column.append([row[col_index] for row in self.to_array() if row[self.columns.index(colname)] == group])

            data[column] = grouped_column

        return DataFrame(data, columns)   

    def aggregate(self, colname, how):
        data = {key:self.data_dict[key] for key in self.data_dict}

        if how == 'count':
            data[colname] = [len(group) for group in data[colname]]

        elif how == 'max':
            data[colname] = [max(group) for group in data[colname]]

        elif how == 'min':
            data[colname] = [min(group) for group in data[colname]]

        elif how == 'sum':
            data[colname] = [sum(group) for group in data[colname]]

        elif how == 'avg':
            data[colname] = [sum(group) / len(group) for group in data[colname]]

        return DataFrame(data, self.columns)

    def query(self, query):
        columns = query.split(" ")
        order_bys = []

        if "ORDER" in columns:
            order_bys = columns[columns.index("ORDER"):]
            order_bys.remove("ORDER")
            order_bys.remove("BY")
            columns = columns[:columns.index("ORDER")]

        columns.remove("SELECT")

        for n in range(len(columns)):
            if "," in columns[n]:
                column = list(columns[n])
                column.remove(",")
                columns[n] = "".join(element for element in column)

        for n in range(len(order_bys)):
            if "," in order_bys[n]:
                order_by = list(order_bys[n])
                order_by.remove(",")
                order_bys[n] = "".join(element for element in order_by)

        order_bys_with_ascending = [(order_bys[n - 1], order_bys[n]) for n in range(len(order_bys)) if n % 2 == 1]

        for a, b in order_bys_with_ascending[::-1]:
            if b == "DESC":
                self = self.order_by(a, False).select(columns)

            if b == "ASC":
                self = self.order_by(a, True).select(columns)

        return self.select(columns)
