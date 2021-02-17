import sys
import random
sys.path.append('analysis')
from eight_queens import *

def steepest_descent_optimizer(n):
    initial_board = random_optimizer(100)
    locations = initial_board['locations']
    costs = initial_board['cost']

    for _ in range(n):
        for coordinates in range(len(locations)):
            next_possible_moves = []

            for x_change in [-1, 0, 1]:
                for y_change in [-1, 0, 1]:
                    next_possible_moves.append((locations[coordinates][0] + x_change, locations[coordinates][1] + y_change))

            for new_locations in next_possible_moves:
                if not 0 <= new_locations[0] < 8 or not 0 <= new_locations[1] < 8:
                    next_possible_moves.remove(new_locations)
                    continue

                elif new_locations in locations:
                    next_possible_moves.remove(new_locations)
                    continue

                new_location = [location for location in locations]
                new_location[coordinates] = new_locations

                if calc_cost(new_location) < costs:
                    locations = new_location
                    costs = calc_cost(new_location)

    return {'locations': locations, 'cost': costs}

for n in [10, 50, 100, 500, 1000]:
    print("n =", n, ":", steepest_descent_optimizer(n), "\n")
