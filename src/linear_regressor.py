import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix


class LinearRegressor:
    def __init__(self, dataframe, dependent_variable):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):
        data = self.dataframe.to_array()
        index = self.dataframe.columns.index(self.dependent_variable)
        column = []

        for i in range(len(data)):
            column.append([])
            column[i].append(data[i][index])

        column = Matrix(column)
        system_of_equations = []

        for i in range(len(data)):
            system_of_equations.append([])

            for j in range(len(data[0])):
                if j == 0:
                    system_of_equations[i].append(1)

                else:
                    for n in range(len(data[i])):
                        if n != index:
                            system_of_equations[i].append(data[i][n])
                            break

        sys_matrix = Matrix(system_of_equations)
        tranposed_matrix = sys_matrix.transpose()
        new_sys_matrix = tranposed_matrix @ sys_matrix
        sys_matrix_inverse = new_sys_matrix.inverse()
        coefficients = sys_matrix_inverse @ tranposed_matrix @ column
        return coefficients

    def predict(self, input_dict):
        for element in self.coefficients.elements[0]:
            a = element

        for element in self.coefficients.elements[1]:
            b = element

        for key in input_dict:
            return a + b * input_dict[key]
