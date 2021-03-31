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

        try:
            self.coefficients = self.calc_coefficients()

        except:
            coefficients = [column for column in self.dataframe.columns if column != self.dependent_variable]
            coefficients.insert(0, 'constant')
            self.coefficients = {element:None for element in coefficients}

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

        for key in columns:
            if key not in input_dict and " * " not in key:
                input_dict[key] = 0

            if key not in input_dict and " * " in key:
                keys = key.split(" * ")
                input_dict[key] = input_dict[keys[0]] * input_dict[keys[1]]

        prediction = 0

        for key in self.coefficients:
            if key in input_dict:
                prediction += self.coefficients[key] * input_dict[key]

            else:
                prediction += self.coefficients[key]

        return self.upper_bound / (1 + math.exp(prediction))

    def copy(self):
        return LogisticRegressor(self.dataframe, self.dependent_variable, self.upper_bound)

    def calc_rss(self):  
        rss = 0
        independent_variables = [column for column in self.dataframe.columns if column != self.dependent_variable]

        for row in self.dataframe.to_array():
            y = row[self.dataframe.columns.index(self.dependent_variable)]
            predict = {independent_variables[n]:row[n] for n in range(len(independent_variables))}
            rss += (self.predict(predict) - y) ** 2

        return rss

    def set_coefficients(self, coeffs):
        self.coefficients = coeffs

    def calc_gradient(self, delta):
        reg1 = self.copy()
        reg2 = self.copy()
        gradient = {}

        for key in dict(self.coefficients):
            grad1 = dict(self.coefficients)
            grad2 = dict(self.coefficients)
            grad1[key] += 0.5 * delta
            grad2[key] -= 0.5 * delta
            reg1.set_coefficients(grad1)
            reg2.set_coefficients(grad2)
            gradient[key] = (reg1.calc_rss() - reg2.calc_rss()) / delta

        return gradient

    def gradient_descent(self, alpha, delta, num_steps, debug_mode=False):
        for n in range(num_steps):
            gradient = self.calc_gradient(delta)
            if debug_mode:
                print("Step #{}:".format(n))
                print("\tGradient:", gradient)
                print("\Coefficients:", self.coefficients)
                print("\tRSS:", self.calc_rss())

            for key in gradient:
                self.coefficients[key] -= gradient[key] * alpha
