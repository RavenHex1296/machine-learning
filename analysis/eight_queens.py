import random


def show_board(locations):
    for n in range(8):
        row_array = ['.', '.', '.', '.', '.', '.', '.', '.']

        for position in locations:
            if position[0] == n:
                row_array[position[1]] = str(locations.index(position))

        print(' '.join(row_array))


def same_row(locations_1, locations_2):
    if locations_1[0] == locations_2[0]:
        return True

    return False


def same_column(locations_1, locations_2):
    if locations_1[1] == locations_2[1]:
        return True

    return False


def same_diagonal(locations_1, locations_2):
    slope = (locations_2[1] - locations_1[1]) / (locations_2[0] - locations_1[0])

    if slope == 1 or slope == -1:
        return True

    return False


def calc_cost(locations):
    cost = 0
    for row in range(len(locations)):
        for column in range(len(locations)):
            if row == column:
                break

            if same_row(locations[column], locations[row]) == True or same_column(locations[column], locations[row]) == True or same_diagonal(locations[column], locations[row]) == True:
                cost += 1

    return cost


def random_optimizer(n):
    cost_dict = {}
    all_locations = []

    for _ in range(n):
        location = []

        for _ in range(8):
            location.append((random.randint(0, 7), random.randint(0, 7)))

        all_locations.append(location)

    min_cost = calc_cost(all_locations[0])
    min_cost_locations = all_locations[0]

    for positions in all_locations:
        if calc_cost(positions) < min_cost:
            min_cost = calc_cost(positions)
            min_cost_locations = positions

    return {'locations': min_cost_locations, 'cost': min_cost}
'''
locations = [(0, 0), (6, 1), (2, 2), (5, 3), (4, 4), (7, 5), (1, 6), (2, 6)]
show_board(locations)

print("Asserting cost")
assert calc_cost(locations) == 10
print("PASSED")

for n in [10, 50, 100, 500, 1000]:
    print("n = " + str(n) + ": " + str(random_optimizer(n)))
'''