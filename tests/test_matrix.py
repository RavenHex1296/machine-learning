import sys
sys.path.append('src')
from matrix import Matrix
''''
A = Matrix([[1, 3], [2, 4]])

print("Asserting A.elements")
assert A.elements == [[1, 3], [2, 4]], "Incorrect output"
print("PASSED")

B = A.copy()
A = 'resetting A to a string'
print("Asserting method 'copy'")
assert B.elements == [[1, 3], [2, 4]], "Incorrect output"
print("PASSED")

C = Matrix([[1, 0], [2, -1]])
D = B.add(C)
print("Asserting method 'add'")
assert D.elements == [[2, 3], [4, 3]], "Incorrect output"
print("PASSED")

E = B.subtract(C)
print("Asserting method 'subtract'")
assert E.elements == [[0, 3], [0, 5]], "Incorrect output"
print("PASSED")

F = B.scalar_multiply(2)
print("Asserting method 'scalar_multiply'")
assert F.elements == [[2, 6], [4, 8]], "Incorrect output"
print("PASSED")

G = B.matrix_multiply(C)
print("Asserting method 'matrix_multiply'")
assert G.elements == [[7, -3], [10, -4]], "Incorrect output"
print("PASSED")

A = Matrix([[1, 0, 2, 0, 3], [0, 4, 0, 5, 0], [6, 0, 7, 0, 8], [-1, -2, -3, -4, -5]])
print("Asserting num_rows and num_cols")
assert (A.num_rows, A.num_cols) == (4, 5), "Incorrect output"
print("PASSED")

A_t = A.transpose()
print("Asserting method 'transpose'")
assert A_t.elements == [[1, 0, 6, -1], [0, 4, 0, -2], [2, 0, 7, -3], [0, 5, 0, -4], [3, 0, 8, -5]], "Incorrect output"
print("PASSED")

print("Asserting that the 'transpose' method works with other methods")
B = A_t.matrix_multiply(A)
assert B.elements == [[38, 2, 47, 4, 56], [2, 20, 6, 28, 10], [47, 6, 62, 12, 77], [4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], "Incorrect output"

C = B.scalar_multiply(0.1).round(5)
assert C.elements == [[3.8, .2, 4.7, .4, 5.6], [.2, 2.0, .6, 2.8, 1.0], [4.7, .6, 6.2, 1.2, 7.7], [.4, 2.8, 1.2, 4.1, 2.0], [5.6, 1.0, 7.7, 2.0, 9.8]], "Incorrect output"

D = B.subtract(C)
assert D.elements == [[34.2, 1.8, 42.3, 3.6, 50.4], [1.8, 18., 5.4, 25.2, 9.], [42.3, 5.4, 55.8, 10.8, 69.3], [3.6, 25.2, 10.8, 36.9, 18.], [50.4, 9., 69.3, 18., 88.2]], "Incorrect output"

E = D.add(C)
assert E.elements == [[38, 2, 47, 4, 56], [2, 20, 6, 28, 10], [47, 6, 62, 12, 77], [4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], "Incorrect output"

assert (E.is_equal(B), E.is_equal(C)) == (True, False), "Incorrect output"

print("PASSED")

A = Matrix([[0, 1, 2], [3, 6, 9], [2, 6, 8]])
print("Asserting A.elements")
assert A.elements == [[0, 1, 2], [3, 6, 9], [2, 6, 8]], "Incorrect output"
print("PASSED")

print("Testing method 'get_pivot_row(0)'")
assert A.get_pivot_row(0) == 1, "Incorrect output"
print("PASSED")


A = Matrix([[0, 1, 2], [3, 6, 9], [2, 6, 8]])

print("Asserting method 'get_pivot_row(0)'")
assert A.get_pivot_row(0) == 1, "Incorrect output"
print("PASSED")

A = A.swap_rows(0, 1)
print("Asserting method 'swap_rows(0, 1)'")
assert A.elements == [[3, 6, 9], [0, 1, 2], [2, 6, 8]], "Incorrect output"
print("PASSED")

A = A.normalize_row(0)
print("Asserting method 'normalize_row(0)'")
assert A.elements == [[1, 2, 3], [0, 1, 2], [2, 6, 8]], "Incorrect output"
print("PASSED")

A = A.clear_below(0)
print("Asserting method 'clear_below(0)'")
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]], "Incorrect output"
print("PASSED")

print("Asserting method 'get_pivot_row(1)'")
assert A.get_pivot_row(1) == 1, "Incorrect output"
print("PASSED")

A = A.normalize_row(1)
print("Asserting method 'normalize_row(1)'")
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]], "Incorrect output"
print("PASSED")

A = A.clear_below(1)
print("Asserting method 'clear_below(1)'")
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, -2]], "Incorrect output"
print("PASSED")

print("Asserting method 'get_pivot_row(2)'")
assert A.get_pivot_row(2) == 2, "Incorrect output"
print("PASSED")

A = A.normalize_row(2)
print("Asserting method 'normalize_row(2)'")
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, 1]], "Incorrect output"
print("PASSED")

A = A.clear_above(2)
print("Asserting method 'clear_above(2)'")
assert A.elements == [[1, 2, 0], [0, 1, 0], [0, 0, 1]], "Incorrect output"
print("PASSED")

A = A.clear_above(1)
print("Asserting method 'clear_above(1)'")
assert A.elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "Incorrect output"
print("PASSED")

A = Matrix([[0, 1, 2], [3, 6, 9], [2, 6, 8]])
A = A.rref()
print("Testing method 'rref([[0, 1, 2], [3, 6, 9], [2, 6, 8]])'")
assert A.elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "Incorrect output"
print("PASSED")

B = Matrix([[0, 0, -4, 0], [0, 0, 0.3, 0], [0, 2, 1, 0]])
B = B.rref()
print("Testing method 'rref([[0, 0, -4, 0], [0, 0, 0.3, 0], [0, 2, 1, 0]])'")
assert B.elements == [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], "Incorrect output"
print("PASSED")


A = Matrix([
    [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9, 10, 11, 12]
])
B = B = Matrix([
    [13, 14],
    [15, 16],
    [17, 18]
])

A_augmented = A.augment(B)
print("Asserting method 'augment'")
assert A_augmented.elements == [
    [1, 2,   3,  4, 13, 14],
    [5, 6,   7,  8, 15, 16],
    [9, 10, 11, 12, 17, 18]
], "Incorrect output"
print("PASSED")

rows_02 = A_augmented.get_rows([0, 2])
print("Asserting method 'get_rows'")
assert rows_02.elements == [
    [1, 2,   3,  4, 13, 14],
    [9, 10, 11, 12, 17, 18]
], "Incorrect output"
print("PASSED")

cols_0123 = A_augmented.get_columns([0, 1, 2, 3])
print("Asserting method 'get_columns'")
assert cols_0123.elements == [
    [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9, 10, 11, 12]
], "Incorrect output"
print("PASSED")

cols_45 = A_augmented.get_columns([4, 5])
print("Asserting method 'get_columns'")
assert cols_45.elements == [
    [13, 14],
    [15, 16],
    [17, 18]
], "Incorrect output"
print("PASSED")

A = Matrix([[1, 2], [3, 4]])

A_inv = A.inverse()

print("Asserting method 'inverse' on input [[1, 2], [3, 4]]")
assert A_inv.elements == [[-2,   1], [1.5, -0.5]], "Incorrect output"
print("PASSED")

A = Matrix([[1,   2,  3], [1,   0, -1], [0.5, 0,  0]])
A_inv = A.inverse()

print("Asserting method 'inverse' on input [[1,   2,  3], [1,   0, -1], [0.5, 0,  0]]")
assert A_inv.elements == [[0,   0,    2], [0.5, 1.5, -4], [0,  -1,    2]], "Incorrect output"
print("PASSED")

A = Matrix([[1, 2, 3, 0], [1, 0, 1, 0], [0, 1, 0, 0]])

print("Asserting [[1, 2, 3, 0], [1, 0, 1, 0], [0, 1, 0, 0]] has no inverse")
A_inv = A.inverse()

A = Matrix([[1, 2, 3], [3, 2, 1], [1, 1, 1]])

print("Asserting [[1, 2, 3], [3, 2, 1], [1, 1, 1]] has no inverse")
A_inv = A.inverse()


A = Matrix([[1, 2], [3, 4]])
ans = A.determinant()

print("Asserting method 'determinant'")
assert round(ans, 6) == -2, "Incorrect output"
print("PASSED")

A = Matrix([[1, 2, 0.5], [3, 4, -1], [8, 7, -2]])
ans = A.determinant()

print("Asserting method 'determinant'")
assert round(ans, 6) == -10.5, "Incorrect output"
print("PASSED")

A = Matrix([[1, 2, 0.5, 0, 1, 0], [3, 4, -1, 1, 0, 1], [8, 7, -2, 1, 1, 1], [-1, 1, 0, 1, 0, 1], [0, 0.35, 0, -5, 1, 1], [1, 1, 1, 1, 1, 0]])
ans = A.determinant()

print("Asserting method 'determinant'")
assert round(ans, 6) == -37.3, "Incorrect output"
print("PASSED")

A = Matrix([[1, 2, 0.5, 0, 1, 0], [3, 4, -1, 1, 0, 1], [8, 7, -2, 1, 1, 1], [-1, 1, 0, 1, 0, 1], [0, 0.35, 0, -5, 1, 1], [1, 1, 1, 1, 1, 0], [2, 3, 1.5, 1, 2, 0]])

print("Asserting method 'determinant' for a matrix with no determinant")
print(A.determinant())

A = Matrix([[1, 2, 0.5, 0, 1, 0, 1], [3, 4, -1, 1, 0, 1, 0], [8, 7, -2, 1, 1, 1, 0], [-1, 1, 0, 1, 0, 1, 0], [0, 0.35, 0, -5, 1, 1, 0], [1, 1, 1, 1, 1, 0, 0], [2, 3, 1.5, 1, 2, 0, 1]])
ans = A.determinant()

print("Asserting method 'determinant'")
assert round(ans, 6) == 0, "Incorrect output"
print("PASSED")
'''

A = Matrix([[1, 1, 0], [2, -1, 0], [0, 0, 3]])

print("Asserting method 'exponent'")
assert A.exponent(3).elements == [[3, 3, 0], [6, -3, 0], [0, 0, 27]], "Incorrect output"
print("PASSED")

A = Matrix([[1, 0, 2, 0, 3], [0, 4, 0, 5, 0], [6, 0, 7, 0, 8], [-1, -2, -3, -4, -5]])

print("Asserting overloaded operations")
A_t = A.transpose()

print("Asserting method 'transpose'")
assert A_t.elements == [[1,  0,  6, -1], [0,  4,  0, -2], [2,  0,  7, -3], [0,  5,  0, -4], [3,  0,  8, -5]], "Incorrect output"
print("PASSED")

B = A_t @ A
print("Asserting overloaded operation 'matmul'")
assert B.elements == [[38,  2, 47,  4, 56], [2, 20,  6, 28, 10], [47,  6, 62, 12, 77], [4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], "Incorrect output"
print("PASSED")

C = B * 0.1
print("Asserting overloaded operation 'mul'")
assert C.elements == [[3.8, 0.2, 4.7, 0.4, 5.6], [0.2, 2.0, 0.6, 2.8, 1.0], [4.7, 0.6, 6.2, 1.2, 7.7], [0.4, 2.8, 1.2, 4.1, 2.0], [5.6, 1.0, 7.7, 2.0, 9.8]], "Incorrect output"
print("PASSED")

D = B - C
print("Asserting overloaded operation 'sub'")
assert D.elements == [[34.2, 1.8, 42.3, 3.6, 50.4], [1.8, 18., 5.4, 25.2, 9.], [42.3, 5.4, 55.8, 10.8, 69.3], [3.6, 25.2, 10.8, 36.9, 18.], [50.4, 9., 69.3, 18., 88.2]], "Incorrect output"
print("PASSED")

E = D + C
print("Asserting overloaded operation 'add'")
assert E.elements == [[38,  2, 47,  4, 56], [2, 20,  6, 28, 10], [47,  6, 62, 12, 77], [4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], "Incorrect output"
print("PASSED")

print("Asserting overloaded operation 'eq'")
assert (E == B) == True
print("PASSED")

print("Asserting overloaded operation 'eq'")
assert (E == C) == False
print("PASSED")


A = Matrix([[1, 2], [3, 4]])
ans = A.cofactor_method_determinant()
print("Asserting method 'cofactor_method_determinant'")
assert round(ans, 6) == -2, "Incorrect output"
print("PASSED")

A = Matrix([[1, 2, 0.5], [3, 4, -1], [8, 7, -2]])
ans = A.cofactor_method_determinant()
print("Asserting method 'cofactor_method_determinant'")
assert round(ans, 6) == -10.5
print("PASSED")

A = Matrix([[1, 2, 0.5, 0, 1, 0], [3, 4, -1, 1, 0, 1], [8, 7, -2, 1, 1, 1], [-1, 1, 0, 1, 0, 1], [0, 0.35, 0, -5, 1, 1], [1, 1, 1, 1, 1, 0]])
ans = A.cofactor_method_determinant()
print("Asserting method 'cofactor_method_determinant'")
assert round(ans, 6) == -37.3
print("PASSED")

A = Matrix([[1, 2, 0.5, 0, 1, 0], [3, 4, -1, 1, 0, 1], [8, 7, -2, 1, 1, 1], [-1, 1, 0, 1, 0, 1], [0, 0.35, 0, -5, 1, 1], [1, 1, 1, 1, 1, 0], [2, 3, 1.5, 1, 2, 0]])
ans = A.cofactor_method_determinant()
print("Asserting method 'cofactor_method_determinant' detects non-square matrix")
print(ans)

A = Matrix([[1, 2, 0.5, 0, 1, 0, 1], [3, 4, -1, 1, 0, 1, 0], [8, 7, -2, 1, 1, 1, 0], [-1, 1, 0, 1, 0, 1, 0], [0, 0.35, 0, -5, 1, 1, 0], [1, 1, 1, 1, 1, 0, 0], [2, 3, 1.5, 1, 2, 0, 1]])
ans = A.cofactor_method_determinant()
print("Asserting method 'cofactor_method_determinant'")
assert round(ans, 6) == 0
print("PASSED")
