import random
import math
#import matplotlib.pyplot as plt

centers = {'x': [(2, 2), (-2, -2)], 'o': [(2, -2), (-2, 2)]}


def calculate_distance(initial_point, ending_point):
    x = ending_point[0] - initial_point[0]
    y = ending_point[1] - initial_point[1]
    return (x ** 2 + y ** 2) ** 0.5


def find_closest_center(point, point_type):
    possible_centers = []

    for key in centers:
        if point_type == key:
            possible_centers = centers[key]

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


def get_semi_random_data(data_set_size):
    num_points = 0
    point_data = {'x': [], 'o': []}

    while num_points < data_set_size:
        x = random.uniform(-4, 4)
        y = random.uniform(-4, 4)

        point_type = 'x'

        if num_points < data_set_size / 2:
            point_type = 'o'

        closest_center = find_closest_center((x, y), point_type)

        distance = calculate_distance((x, y), closest_center)

        if probability(distance) >= random.uniform(0, 1):
            point_data[point_type].append((x, y))
            num_points += 1

    return point_data


'''
plt.style.use('bmh')
plt.plot([point[0] for point in point_data['x']], [point[1] for point in point_data['x']], 'ro')
plt.plot([point[0] for point in point_data['o']], [point[1] for point in point_data['o']], 'bo')
plt.savefig('semi_random_data.png')
'''