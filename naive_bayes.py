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

    def predict(self, independent_var_vals):

        p1 = len([element for element in self.original_data[self.interest_class] if element]) / len(self.original_data[self.interest_class])
        p2 = len([element for element in self.original_data[self.interest_class] if not element]) / len(self.original_data[self.interest_class])

        row_indices_yes = []

        for n in range(0, len(self.original_data[self.interest_class])):
            if self.original_data[self.interest_class][n]:
                row_indices_yes.append(n)

        row_indices_no = [n for n in range(0, len(self.original_data[self.interest_class])) if n not in row_indices_yes]

        independent_vars = [key for key in self.original_data.keys() if key != self.interest_class]
        yes_data = []
        no_data = []

        for var in independent_vars:
            yes_data.append([self.original_data[var][n] for n in row_indices_yes])
            no_data.append([self.original_data[var][n] for n in row_indices_no])

        for n in range(0, len(yes_data)):
            match1 = 0
            match2 = 0

            for point in yes_data[n]:
                if point == independent_var_vals[n]:
                    match1 += 1

            for point in no_data[n]:
                if point == independent_var_vals[n]:
                    match2 += 1


            p1 *= match1 / len(row_indices_yes)
            p2 *= match2 / len(row_indices_no)

        print(p1, p2)

        if p1 > p2:
            return "Scam"

        return "Not a Scam"

    def predict_all(self):
        results = []

        for n in range(0, len(self.test_data[0])):
            independent_var_vals = []

            for point in self.test_data[n]:
                independent_var_vals.append(point)

            results.append(self.predict(independent_var_vals))

        return results
        

naive_bayes = NaiveBayes(data, test_data, "Scam")
print(naive_bayes.predict([False, False]))
print(naive_bayes.predict([True, True]))
print(naive_bayes.predict([True, False]))
print(naive_bayes.predict([False, True]))