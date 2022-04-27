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
        strictest_constraint = 0

        for n in range(0, len(constraints)):
            if abs(constraints[n][-1] / constraints[n][increase_var_index]) < abs(constraints[strictest_constraint][-1] / constraints[strictest_constraint][increase_var_index]):
                strictest_constraint = n

        return strictest_constraint

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

    def run(self):
        self.insert_slack_variables()
        num_iteration = 0

        while self.keep_going():
            #print("Interation:", num_iteration)
            increase_var_index = simplex.increase_var_index()
            strictest_constraint_index = simplex.get_strictest_constraint(increase_var_index)
            simplex.reduce(strictest_constraint_index, increase_var_index)
            simplex.kill_columns(strictest_constraint_index, increase_var_index)
            num_iteration += 1


        return self.matrix_representation




simplex = Simplex([[3, 2, 5, 55], [2, 1, 1, 26], [1, 1, 3, 30], [5, 2, 4,  57], [20, 10, 15, 0]])
#simplex = Simplex([[2, 1, 1, 14], [4, 2, 3, 28], [2, 5, 5, 30], [1, 2, 1, 0]])
print(simplex.run())