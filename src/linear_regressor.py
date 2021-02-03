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
        columns = []

        for row_index in range(len(data)):
            columns.append([])
            columns[row_index].append(data[row_index][index])

        columns = Matrix(columns)
        system_of_equations = []

        for row_index in range(len(data)):
            system_of_equations.append([])

            for column_index in range(len(data[0])):
                if column_index == 0:
                    system_of_equations[row_index].append(1)

                if column_index != index:
                    system_of_equations[row_index].append(data[row_index][column_index])

        sys_matrix = Matrix(system_of_equations)
        tranposed_matrix = sys_matrix.transpose()
        new_sys_matrix = tranposed_matrix @ sys_matrix
        sys_matrix_inverse = new_sys_matrix.inverse()
        coefficients = sys_matrix_inverse @ tranposed_matrix @ columns
        coefficients_dict = {}
        indpendent_variables = []

        for column in self.dataframe.columns:
            indpendent_variables.append(column)

        indpendent_variables.remove(self.dependent_variable)

        for n in range(len(indpendent_variables) + 1):
            if n == 0:
                coefficients_dict['constant'] = coefficients.elements[n][0]

            else:
                coefficients_dict[indpendent_variables[n - 1]] = coefficients.elements[n][0]

        return coefficients_dict
        

    def predict(self, input_dict):
        prediction = 0
        columns = [variable for variable in self.dataframe.columns if variable != self.dependent_variable]

        for variable in columns:
            if variable not in input_dict and " * " not in variable:
                input_dict[variable] = 0

            elif variable not in input_dict and " * " in variable:
                input_dict[variable] = input_dict[variable.split(" * ")[0]] * input_dict[variable.split(" * ")[1]]

        for key in self.coefficients:
            if key in input_dict:
                prediction += self.coefficients[key] * input_dict[key]
                
            elif key not in input_dict:
                prediction += self.coefficients[key]

        return prediction
