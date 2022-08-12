import math


data = {"Scam": [False, True, True, False, False, True, False, False, True, False], 
        "Errors": [False, True, True, False, False, True, True, False, True, False], 
        "Links": [False, True, True, False, True, True, False, True, False, True]}

test_data = {"Errors": [False, True, True, False], "Links": [False, True, False, True]}


class NaiveBayes():
    def __init__(self, original_data, test_data, interest_class):
        self.original_data = original_data
        self.test_data = test_data
        self.interest_class = interest_class

    def get_row_indices_yes_no(self):
        row_indices_yes = []

        for n in range(0, len(self.original_data[self.interest_class])):
            if self.original_data[self.interest_class][n]:
                row_indices_yes.append(n)

        row_indices_no = [n for n in range(0, len(self.original_data[self.interest_class])) if n not in row_indices_yes]

        return row_indices_yes, row_indices_no

    def calculate_probabilities(self, yes_id_var_vals, no_id_var_vals, independent_var_vals, totals):
        interest_class_data = [element for element in self.original_data[self.interest_class]]
        num_data_points = len(self.original_data[self.interest_class])

        p1 = len([element for element in interest_class_data if element]) / num_data_points
        p2 = len([element for element in interest_class_data if not element]) / num_data_points

        for n in range(0, len(yes_id_var_vals)):
            match1 = 0
            match2 = 0

            for point in yes_id_var_vals[n]:
                if point == independent_var_vals[n]:
                    match1 += 1

            for point in no_id_var_vals[n]:
                if point == independent_var_vals[n]:
                    match2 += 1


            p1 *= match1 / len(totals[0])
            p2 *= match2 / len(totals[1])

        return p1, p2


    def predict(self, independent_var_vals):

        row_indices_yes, row_indices_no = self.get_row_indices_yes_no()

        independent_vars = [key for key in self.original_data.keys() if key != self.interest_class]
        yes_id_var_vals = []
        no_id_var_vals = []

        for var in independent_vars:
            yes_id_var_vals.append([self.original_data[var][n] for n in row_indices_yes])
            no_id_var_vals.append([self.original_data[var][n] for n in row_indices_no])

        p1, p2 = self.calculate_probabilities(yes_id_var_vals, no_id_var_vals, independent_var_vals, [row_indices_yes, row_indices_no])
        print(p1, p2)

        if p1 > p2:
            return True

        return False

    def predict_all(self):
        results = []
        key1 = list(self.test_data.keys())[0]

        for n in range(0, len(self.test_data[key1])):
            independent_var_vals = []

            for key in self.test_data.keys():
                independent_var_vals.append(self.test_data[key][n])

            results.append(self.predict(independent_var_vals))

        return results
        

naive_bayes = NaiveBayes(data, test_data, "Scam")
print(naive_bayes.predict_all())