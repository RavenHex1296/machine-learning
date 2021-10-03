import random
import matplotlib.pyplot as plt
import math

x_points = []
o_points = []

x_centers = [(2, 2), (-2, -2)]
o_centers = [(2, -2), (-2, 2)]


def calculate_distance(initial_point, ending_point):
    x = ending_point[0] - initial_point[0]
    y = ending_point[1] - initial_point[1]
    return (x ** 2 + y ** 2) ** 0.5


def find_closest_center(point, point_type):
    possible_centers = []

    if point_type == 'x':
        possible_centers = x_centers

    if point_type == 'o':
        possible_centers = o_centers

    min_distance = 100000
    closest_center = (100, 100)

    for center in possible_centers:
        distance = calculate_distance(point, center)

        if distance < min_distance:
            min_distance = distance
            closest_center = center

    return closest_center


def probability(x):
    return 2 ** (-1 * x)


num_points = 0

while num_points < 100:
    x = random.uniform(-4, 4)
    y = random.uniform(-4, 4)

    closest_center = find_closest_center((x, y), 'x')

    distance = calculate_distance((x, y), closest_center)

    if probability(distance) >= random.uniform(0, 1):
        x_points.append((x, y))
        num_points += 1
  

num_points = 0

while num_points < 100:
    x = random.uniform(-4, 4)
    y = random.uniform(-4, 4)

    closest_center = find_closest_center((x, y), 'o')

    distance = calculate_distance((x, y), closest_center)


    if probability(distance) >= random.uniform(0, 1):
        o_points.append((x, y))
        num_points += 1


plt.style.use('bmh')
plt.plot([x[0] for x in x_points], [y[1] for y in x_points], 'ro')
plt.plot([x[0] for x in o_points], [y[1] for y in o_points], 'bo')
plt.savefig('semi_random_data.png')
