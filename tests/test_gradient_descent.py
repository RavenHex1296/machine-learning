import sys
sys.path.append('src')
from gradient_descent import GradientDescent


def single_variable_function(x):
    return (x-1)**2


def two_variable_function(x, y):
    return (x-1)**2 + (y-1)**3


def three_variable_function(x, y, z):
    return (x-1)**2 + (y-1)**3 + (z-1)**4


def six_variable_function(x1, x2, x3, x4, x5, x6):
    return (x1-1)**2 + (x2-1)**3 + (x3-1)**4 + x4 + 2*x5 + 3*x6

print("Asserting the gradient descent of a single variable function")
minimizer = GradientDescent(single_variable_function, [0])
assert minimizer.points == [0], "Incorrect output"
print("PASSED")

print("Asserting the gradient of a single variable function")
gradient_list = minimizer.compute_gradient(0.01)
for n in range(len(gradient_list)):
    gradient_list[n] = round(gradient_list[n], 3)
assert gradient_list == [-2.00000], "Incorrect output"
print("PASSED")

print("Asserting the descend of a single variable function")
minimizer.descend(0.001, 0.01, 1)
for n in range(len(minimizer.points)):
    minimizer.points[n] = round(minimizer.points[n], 3)
assert minimizer.points == [0.00200]
print("PASSED")

print("Asserting the gradient descent of a two variable function")
minimizer = GradientDescent(two_variable_function, [0, 0])
assert minimizer.points == [0, 0]
print("PASSED")

print("Asserting the gradient of a two variable function")
gradient_list = minimizer.compute_gradient(0.01)
for n in range(len(gradient_list)):
    gradient_list[n] = round(gradient_list[n], 3)
assert gradient_list == [-2.00000, 3.000]
print("PASSED")

print("Asserting the descend of a two variable function")
minimizer.descend(0.001, 0.01, 1)
for n in range(len(minimizer.points)):
    minimizer.points[n] = round(minimizer.points[n], 3)
assert minimizer.points == [0.00200, -0.00300]
print("PASSED")

print("Asserting the gradient descent of a three variable function")
minimizer = GradientDescent(three_variable_function, [0, 0, 0])
assert minimizer.points == [0, 0, 0]
print("PASSED")

print("Asserting the gradient of a three variable function")
gradient_list = minimizer.compute_gradient(0.01)
for n in range(len(gradient_list)):
    gradient_list[n] = round(gradient_list[n], 3)
assert gradient_list == [-2.00000, 3.000, -4.000]
print("PASSED")

print("Asserting the descend of a three variable function")
minimizer.descend(0.001, 0.01, 1)
for n in range(len(minimizer.points)):
    minimizer.points[n] = round(minimizer.points[n], 3)
assert minimizer.points == [0.00200, -0.00300, 0.00400]
print("PASSED")

print("Asserting the gradient descent of a six variable function")
minimizer = GradientDescent(six_variable_function, [0, 0, 0, 0, 0, 0])
assert minimizer.points == [0, 0, 0, 0, 0, 0]
print("PASSED")

print("Asserting the gradient of a six variable function")
gradient_list = minimizer.compute_gradient(0.01)
for n in range(len(gradient_list)):
    gradient_list[n] = round(gradient_list[n], 3)
assert gradient_list == [-2.00000, 3.000, -4.000, 1.00000, 2.00000, 3.00000]
print("PASSED")

print("Asserting the descend of a six variable function")
minimizer.descend(0.001, 0.01, 1)
for n in range(len(minimizer.points)):
    minimizer.points[n] = round(minimizer.points[n], 3)
assert minimizer.points == [0.00200, -0.00300, 0.00400, -0.00100, -0.00200, -0.00300]
print("PASSED")
