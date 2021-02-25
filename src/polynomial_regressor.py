import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix
from linear_regressor import LinearRegressor


class PolynomialRegressor():
    def __init__(self, degree):
        self.degree = degree
        self.dependent_variable = None
        self.dataframe = None
        self.coefficients = None

    def fit(self, dataframe, dependent_variable):
        self.dependent_variable = dependent_variable
        data = []
        columns = [column for column in dataframe.columns]

        if self.degree < 1:
            data = [[pair[1]] for pair in dataframe.to_array()]
            columns.remove('x')
            self.dataframe = DataFrame.from_array(data, columns)
            self.coefficients = self.calculate_coefficients()

        else:
            columns.remove(dependent_variable)

            for n in range(len(dataframe.to_array())):
                data.append([])

                for num in range(1, self.degree + 1):
                    if num != 1 and "x^" + str(num) not in columns:
                        columns.append("x^" + str(num))

                    data[n].append(dataframe.to_array()[n][0] ** num)

                data[n].append(dataframe.to_array()[n][1])

            columns.append(dependent_variable)
            self.dataframe = DataFrame.from_array(data, columns)
            self.coefficients = self.calculate_coefficients()

        return

    def calculate_coefficients(self):
        return LinearRegressor(self.dataframe, self.dependent_variable).coefficients

    def predict(self, input_dict):
        columns = [variable for variable in self.dataframe.columns if variable != self.dependent_variable]
        prediction = 0

        for key in columns:
            if key not in input_dict and "^" in key:
                input_dict[key] = input_dict[key.split("^")[0]] ** int(key.split("^")[1])

        for key in self.coefficients:
            if key in input_dict:
                prediction += self.coefficients[key] * input_dict[key]

            elif key not in input_dict:
                prediction += self.coefficients[key]

        return prediction
