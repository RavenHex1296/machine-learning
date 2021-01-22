import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix
from linear_regressor import LinearRegressor
import math


class LogisticRegressor:
    def __init__(self, dataframe, dependent_variable):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):
        transformation = {}
        transformed_values = []

        for key in self.dataframe.data_dict:
            transformation[key] = self.dataframe.data_dict[key]

        for y in self.dataframe.data_dict[self.dependent_variable]:
            transformed_values.append(math.log((1 / y) - 1))

        for key in self.dependent_variable:
            transformation[key] = transformed_values

        transformation = DataFrame(transformation, self.dataframe.columns)
        regressor = LinearRegressor(transformation, self.dependent_variable)
        return regressor.coefficients

    def predict(self, input_dict):
        prediction = 0

        for key in self.coefficients:
            if key in input_dict:
                prediction += self.coefficients[key] * input_dict[key]

            else:
                prediction += self.coefficients[key]

        return 1 / (1 + math.exp(prediction))
