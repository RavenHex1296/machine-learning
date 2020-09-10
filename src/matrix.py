class Matrix():
    def __init__(self, input_elements):
        self.elements = input_elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])

    def copy(self):
        copied_matrix = Matrix(self.elements)

        return copied_matrix

    def add(self, input_matrix):
        sum_matrix = [[0, 0], [0, 0]]

        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                sum_matrix[i][j] = (
                    self.elements[i][j] + input_matrix.elements[i][j])

        return Matrix(sum_matrix)

    def subtract(self, input_matrix):
        difference_matrix = [[0, 0], [0, 0]]

        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                difference_matrix[i][j] = (
                    self.elements[i][j] - input_matrix.elements[i][j])

        return Matrix(difference_matrix)

    def scalar_multiply(self, input_scalar):
        rescaled_elements = [[0, 0], [0, 0]]

        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                rescaled_elements[i][j] = self.elements[i][j] * input_scalar

        return Matrix(rescaled_elements)

    def matrix_multiply(self, input_matrix):
        product_matrix = [[0, 0], [0, 0]]

        for i in range(len(self.elements)):
            for j in range(len(input_matrix.elements[0])):
                for k in range(len(input_matrix.elements)):
                    product_matrix[i][j] += (
                        self.elements[i][k] * input_matrix.elements[k][j])

        return Matrix(product_matrix)

