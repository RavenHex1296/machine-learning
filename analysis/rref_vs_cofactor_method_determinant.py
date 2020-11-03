import sys
sys.path.append('src')
from matrix import Matrix
import random

test_matrix = Matrix([[random.random() for i in range(10)] for j in range(10)])

print("RREF determinant:")
print(test_matrix.determinant())
print("Cofactor determinant")
print(test_matrix.cofactor_method_determinant())

#The RREF method is faster. I believe it is faster because the cofactor method has to keep breaking down a matrix until it gets to a bunch of scalars multiplied by a 3 x 3. When we have a matrix is as large as a 10 x 10, it becomes apparent that the number of operations is very large and thus time consuming.
