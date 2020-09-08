class Matrix():
    def __init__(self, input_elements):
        self.elements = input_elements

    def copy(self):
        copied_matrix = Matrix(self.elements)

        return copied_matrix

    def add(self, input_matrix):
        sum_matrix = [[0, 0], [0, 0]]

        for element in range(len(self.elements)):
            for component in range(len(self.elements[0])):
                sum_matrix[element][component] = (
                    self.elements[element][component] + input_matrix.elements[element][component])

        return Matrix(sum_matrix)

    def subtract(self, input_matrix):
        difference_matrix = [[0, 0], [0, 0]]

        for element in range(len(self.elements)):
            for component in range(len(self.elements[0])):
                difference_matrix[element][component] = (
                    self.elements[element][component] - input_matrix.elements[element][component])

        return Matrix(difference_matrix)

    def scalar_multiply(self, input_scalar):
        rescaled_matrix = [[0, 0], [0, 0]]

        for element in range(len(self.elements)):
            for component in range(len(self.elements[0])):
                rescaled_matrix[element][component] = self.elements[element][component] * input_scalar

        return Matrix(rescaled_matrix)

    def matrix_multiply(self, input_matrix):
        product_matrix = [[0, 0], [0, 0]]

        for elements in range(len(self.elements)):
            for component in range(len(input_matrix.elements[0])):
                for factor in range(len(input_matrix.elements)):
                    product_matrix[elements][component] += (
                        self.elements[elements][factor] * input_matrix.elements[factor][component])

        return Matrix(product_matrix)
