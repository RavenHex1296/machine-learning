import numpy as np
import math

class Simplex:
    def __init__(self, problem):
        self.matrix_representation = problem
        self.num_constrants = len(problem) - 1

    def insert_slack_variables(self):
        num_variables = len(self.matrix_representation[0]) - 1

        for n in range(0, len(self.matrix_representation)):
            row = self.matrix_representation[n]
            constant = row[len(row) - 1]
            row.remove(constant)
            slack_var_values = []

            for num in range(0, self.num_constrants):
                if num == n and 1 not in slack_var_values:
                    row.append(1)
                    slack_var_values.append(1)

                if num != n:
                    row.append(0)
                    slack_var_values.append(0)

            row.append(constant)

    def keep_going(self):
        max_equation = self.matrix_representation[-1]

        for n in max_equation:
            if n > 0:
                return True

        return False

    def increase_var_index(self): #returns index of variable we want to increase
        max_equation = self.matrix_representation[-1]

        index_of_variable_of_interest = 0

        for n in range(0, len(max_equation)):
            if max_equation[n] > max_equation[index_of_variable_of_interest]:
                index_of_variable_of_interest = n

        return index_of_variable_of_interest

    def get_strictest_constraint(self, increase_var_index): #returns index of strictest constraint
        constraints = self.matrix_representation[:-1]
        strictest_constraint = self.matrix_representation[:-1][0]
        stricted_constraint_value = 100000

        for constraint in constraints:
            if constraint[increase_var_index] > 0 and constraint[-1] / constraint[increase_var_index] < stricted_constraint_value:
                stricted_constraint_value = constraint[-1] / constraint[increase_var_index]
                strictest_constraint = constraint

        return self.matrix_representation.index(strictest_constraint)


    def reduce(self, strictest_constraint_index, increase_var_index):   
        reduced_constraint_row = []
     
        for n in self.matrix_representation[strictest_constraint_index]:
            reduced_constraint_row.append(n / self.matrix_representation[strictest_constraint_index][increase_var_index])

        self.matrix_representation[strictest_constraint_index] = reduced_constraint_row

        return self.matrix_representation

    def kill_columns(self, strictest_constraint_index, increase_var_index):
        strictest_constraint = self.matrix_representation[strictest_constraint_index]
        old_matrix = self.matrix_representation

        self.matrix_representation = [strictest_constraint]
        #print("constraint", strictest_constraint)
        #print("var", increase_var_index + 1)

        for n in range(0, len(old_matrix)):
            row = old_matrix[n]

            if row != strictest_constraint:
                scalar_multiple = row[increase_var_index]
                row = list(np.array(row) - scalar_multiple * np.array(strictest_constraint))
                self.matrix_representation.append(row) 

        return self.matrix_representation

    def get_columns(self):
        columns = []

        for column_index in range(len(self.matrix_representation[0])):
            columns.append([row[column_index] for row in self.matrix_representation])

        return columns

    def get_original_variables(self):
        num_variables = len(self.matrix_representation[0]) - 1 - self.num_constrants
        variables = {}
        columns = self.get_columns()

        for variable_index in range(num_variables):
            variables[variable_index + 1] = None

        for n in range(0, num_variables):
            num_ones = len([num for num in columns[n] if num == 1])

            if num_ones == 1:
                variables[n + 1] = self.matrix_representation[columns[n].index(1)][-1]

            else:
                variables[n + 1] = 0


        return variables

    def run(self):
        self.insert_slack_variables()
        num_iteration = 0
        print(self.matrix_representation)

        while self.keep_going():
            #print("Interation:", num_iteration)
            increase_var_index = simplex.increase_var_index()
            strictest_constraint_index = simplex.get_strictest_constraint(increase_var_index)
            simplex.reduce(strictest_constraint_index, increase_var_index)
            simplex.kill_columns(strictest_constraint_index, increase_var_index)
            num_iteration += 1


        max_equation = self.matrix_representation[-1]
        variables = self.get_original_variables()
        variables['max'] = -max_equation[-1]

        print(self.matrix_representation)

        return variables



#simplex = Simplex([[3, 2, 5, 55], [2, 1, 1, 26], [1, 1, 3, 30], [5, 2, 4,  57], [20, 10, 15, 0]])
#simplex = Simplex([[2, 1, 1, 14], [4, 2, 3, 28], [2, 5, 5, 30], [1, 2, 1, 0]])
#simplex = Simplex([[3, 2, 0, 5], [2, 1, -1, 13], [0, 0, 1, 4], [2, 3, 1, 0]])
#simplex = Simplex([[4, 2, 0, 400], [2, 2, 2, 252], [1, 2, 3, 200], [1, 1, 2, 900], [1, 1, 1, 0]])
#simplex = Simplex([[2, 3, 6], [3, 7, 12], [7, 12, 0]])
print(simplex.run())