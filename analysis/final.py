import math

a = 1
b = 1

coefficients = [a, b]

data = [(0.5,2), (0.9,0.9), (1,0.3)]

def function(x):
    return a * math.sin(b)

def rss(a, b, function):
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    rss = 0

    for n in range(len(x)):
        y_predict = function(x[n])
        rss += (y[n]-y_predict) ** 2
    
    return rss


def compute_gradient(function, delta):
    gradient_list = []

    for n in range(len(coefficients)):
        coefficients1 = list(coefficients)
        coefficients2 = list(coefficients)
        coefficients1 += 0.5 * delta
        coefficients2 -= 0.5 * delta