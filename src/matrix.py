class Matrix():
    def __init__(self, input_elements):
        self.elements = input_elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])

    def copy(self):
        copied_elements = [[num for num in row] for row in self.elements]
        return Matrix(copied_elements)

    def add(self, input_matrix):
        sum_matrix = []
        for i in range(self.num_rows):
            sum_matrix.append([])

            for j in range(self.num_cols):
                sum_matrix[i].append(
                    self.elements[i][j] + input_matrix.elements[i][j])

        return Matrix(sum_matrix)

    def subtract(self, input_matrix):
        difference_matrix = []

        for i in range(self.num_rows):
            difference_matrix.append([])

            for j in range(self.num_cols):
                difference_matrix[i].append(
                    self.elements[i][j] - input_matrix.elements[i][j])

        return Matrix(difference_matrix)

    def scalar_multiply(self, input_scalar):
        rescaled_elements = []

        for i in range(self.num_rows):
            rescaled_elements.append([])

            for j in range(self.num_cols):
                rescaled_elements[i].append(
                    self.elements[i][j] * input_scalar)

        return Matrix(rescaled_elements)

    def matrix_multiply(self, input_matrix):
        product_matrix = []

        for i in range(self.num_rows):
            product_matrix.append([])

            for j in range(input_matrix.num_cols):
                product_matrix[i].append(0)

        for i in range(self.num_rows):
            for j in range(input_matrix.num_cols):
                for k in range(input_matrix.num_rows):
                    product_matrix[i][j] += (
                        self.elements[i][k] * input_matrix.elements[k][j])

        return Matrix(product_matrix)

    def transpose(self):
        transposed_matrix = []

        for i in range(self.num_cols):
            transposed_matrix.append([])

            for j in range(self.num_rows):
                transposed_matrix[i].append(self.elements[j][i])

        return Matrix(transposed_matrix)

    def is_equal(self, input_matrix):
        if self.elements == input_matrix.elements:
            return True

        else:
            return False

    def round(self, decimal_places):
        for i in self.elements:
            for j in range(len(i)):
                i[j] = round(i[j], 5)

        return Matrix(self.elements)

    def get_pivot_row(self, column_index):
        for i in range(self.num_rows):
            if column_index == 0:
                if self.elements[i][column_index] != 0:
                    return i

            elif column_index > 0:
                if self.elements[i][column_index] != 0:
                    reference_num = 0

                    for j in self.elements[i][:column_index]:
                        reference_num += j

                    if reference_num == 0:
                        return i

                else:
                    continue

            else:
                return None

    def swap_rows(self, row_index1, row_index2):
        copied_matrix = self.copy()
        replacement = copied_matrix.elements[row_index1]
        copied_matrix.elements[row_index1] = copied_matrix.elements[row_index2]
        copied_matrix.elements[row_index2] = replacement
        return copied_matrix

    def normalize_row(self, row_index):
        copied_matrix = self.copy()

        for j in copied_matrix.elements[row_index]:

            if j != 0:
                original_entry = j
                break

        for j in range(len(copied_matrix.elements[0])):
            copied_matrix.elements[row_index][j] /= original_entry

        return copied_matrix

    def clear_below(self, row_index):
        copied_matrix = self.copy()

        for num in copied_matrix.elements[row_index]:
            if num != 0:
                j = num
                col_index = copied_matrix.elements[row_index].index(j)
                break

        for row in copied_matrix.elements[row_index + 1:]:
            while row[col_index] != 0:
                reference_num = row[col_index]

                for n in range(len(copied_matrix.elements[0])):
                    row[n] -= copied_matrix.elements[row_index][n] * reference_num

        return copied_matrix

    def clear_above(self, row_index):
        copied_matrix = self.copy()

        for num in copied_matrix.elements[row_index]:
            if num != 0:
                j = num
                col_index = copied_matrix.elements[row_index].index(j)
                break

        for row in copied_matrix.elements[:row_index]:
            while row[col_index] != 0:
                reference_num = row[col_index]

                for n in range(len(copied_matrix.elements[0])):
                    row[n] -= copied_matrix.elements[row_index][n] * reference_num

        return copied_matrix

    def rref(self):
        copied_matrix = self.copy()
        i = 0

        for j in range(copied_matrix.num_cols):
            pivot_index = copied_matrix.get_pivot_row(j)

            if pivot_index != None:
                if i not in range(copied_matrix.num_rows):
                    continue

                if pivot_index != i:
                    copied_matrix = copied_matrix.swap_rows(i, pivot_index)
                copied_matrix = copied_matrix.normalize_row(i)
                copied_matrix = copied_matrix.clear_above(i)
                copied_matrix = copied_matrix.clear_below(i)
                i += 1

            else:
                continue

        return copied_matrix

    def augment(self, other_matrix):
        copied_matrix = self.copy()

        for i in range(other_matrix.num_rows):
            for j in range(other_matrix.num_cols):
                copied_matrix.elements[i].append(other_matrix.elements[i][j])

        return copied_matrix

    def get_rows(self, row_nums):
        copied_matrix = self.copy()
        row_matrix = []

        for row in row_nums:
            row_matrix.append(copied_matrix.elements[row])

        return Matrix(row_matrix)

    def get_columns(self, col_nums):
        copied_matrix = self.copy()
        column_matrix = []

        for i in range(copied_matrix.num_rows):
            column_matrix.append([])

        for i in range(copied_matrix.num_rows):
            for column in col_nums:
                column_matrix[i].append(copied_matrix.elements[i][column])

        return Matrix(column_matrix)

    def inverse(self):
        copied_matrix = self.copy()
        identity_matrix = Matrix([[1 if j == i else 0 for j in range(copied_matrix.num_cols)] for i in range(copied_matrix.num_rows)])
        rref_matrix = copied_matrix.augment(identity_matrix).rref()

        if copied_matrix.num_rows != copied_matrix.num_cols:
            print("Error: cannot invert a non-square matrix")
            return

        for i in range(copied_matrix.num_rows):
            if rref_matrix.get_pivot_row(i) != i:
                print("Error: cannot invert a singular matrix")
                return

        result_matrix = []

        for i in range(copied_matrix.num_rows):
            result_matrix.append([])

            for j in range(copied_matrix.num_cols, rref_matrix.num_cols):
                result_matrix[i].append(rref_matrix.elements[i][j])

        return Matrix(result_matrix)

    def determinant(self):
        determinant = 1
        copied_matrix = self.copy()
        i = 0

        if copied_matrix.num_cols != copied_matrix.num_rows:
           return ("Error: Cannot take determinant of non-square matrix")

        for j in range(copied_matrix.num_cols):
            pivot_index = copied_matrix.get_pivot_row(j)

            if pivot_index != None:
                if i not in range(copied_matrix.num_rows):
                    continue

                if pivot_index != i:
                    copied_matrix = copied_matrix.swap_rows(i, pivot_index)

                determinant *= copied_matrix.elements[pivot_index][j]
                copied_matrix = copied_matrix.normalize_row(i)
                copied_matrix = copied_matrix.clear_above(i)
                copied_matrix = copied_matrix.clear_below(i)
                i += 1

            else:
                determinant *= 0
                continue

        return determinant
