import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix
from linear_regressor import LinearRegressor
import math


class LogisticRegressor:
    def __init__(self, dataframe, dependent_variable, upper_bound):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.upper_bound = upper_bound
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):
        transformation = {}

        for key in self.dataframe.data_dict:
            transformation[key] = self.dataframe.data_dict[key]

        transformation[self.dependent_variable] = [math.log(self.upper_bound / y - 1) for y in transformation[self.dependent_variable]]

        transformation = DataFrame(transformation, self.dataframe.columns)
        regressor = LinearRegressor(transformation, self.dependent_variable)
        return regressor.coefficients

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

            else:
                prediction += self.coefficients[key]

        return self.upper_bound / (1 + math.exp(prediction))
