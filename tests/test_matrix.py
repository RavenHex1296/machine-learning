import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1, 3], [2, 4]])

print("Asserting A.elements")
assert A.elements == [[1, 3], [2, 4]], "Incorrect output"
print("PASSED")

B = A.copy()
A = 'resetting A to a string'
print("Asserting method 'copy'...")
assert B.elements == [[1, 3], [2, 4]], "Incorrect output"
print("PASSED")

C = Matrix([[1, 0], [2, -1]])
D = B.add(C)
print("Asserting method 'add'...")
assert D.elements == [[2, 3], [4, 3]], "Incorrect output"
print("PASSED")

E = B.subtract(C)
print("Asserting method 'subtract'...")
assert E.elements == [[0, 3], [0, 5]], "Incorrect output"
print("PASSED")

F = B.scalar_multiply(2)
print("Asserting method 'scalar_multiply'...")
assert F.elements == [[2, 6], [4, 8]], "Incorrect output"
print("PASSED")

G = B.matrix_multiply(C)
print("Asserting method 'matrix_multiply'...")
assert G.elements == [[7, -3], [10, -4]], "Incorrect output"
print("PASSED")
