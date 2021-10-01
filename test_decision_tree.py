
from decision_tree import *
import math
import random
'''
data = {'x': [(2, 1), (2, 2), (3, 2), (3, 3)], 'o': [(2, 3), (2, 4), (3, 4)]}

decision_tree = DecisionTree(data)
assert decision_tree.point_data == data
assert round(decision_tree.entropy, 3) == 0.683
assert decision_tree.get_best_split() == (1, 2.5)

decision_tree.fit()
assert decision_tree.predict((0, -1)) == 'x'
assert decision_tree.predict((5, 6)) == 'o'
assert decision_tree.predict((2, 3)) == 'o'
assert decision_tree.predict((5, 3)) == 'x'


data = {'x': [(1, 3), (1, 2), (2, 2)], 'o': [(1, 1), (2, 1), (3, 1), (3, 2)]}

decision_tree = DecisionTree(data)
assert decision_tree.point_data == data
assert round(decision_tree.entropy, 3) == 0.683
assert decision_tree.get_best_split() == (1, 1.5)

decision_tree.fit()
assert decision_tree.predict((100, 100)) == 'o'
assert decision_tree.predict((-10, -10)) == 'o'
assert decision_tree.predict((1, 3)) == 'x'

print('PASSED')

data = {'x': [(1, 7), (2, 7), (3, 7), (3, 8), (3, 9), (7, 1)], 'o': [(1, 9), (5, 3), (6, 3), (7, 3), (5, 2), (5, 1)]}
decision_tree = DecisionTree(data, 7)
decision_tree.fit()

assert decision_tree.predict((2, 8)) == 'x'
assert decision_tree.predict((6, 2)) == 'o'
assert decision_tree.predict((-10, 2)) == 'x'
assert decision_tree.predict((100, 2)) == 'o'
assert decision_tree.predict((4, 5)) == 'o'
assert len(decision_tree.branches[0].branches) == 0
assert len(decision_tree.branches[1].branches) == 0

data = {'x': [(1, 5), (2, 5), (1, 3), (2, 4)], 'o': [(1, 4), (2, 3)]}

decision_tree = DecisionTree(data, 5)
decision_tree.fit()
assert decision_tree.predict((2, 8)) == 'x'
assert decision_tree.predict((-10, 100)) == 'x'

random.seed(0)
initial_prediction = decision_tree.predict((-2, -5))

for n in range(-10, 4):
    random.seed(0)
    assert decision_tree.predict((0, n)) == initial_prediction

assert decision_tree.predict((2, 5)) == 'x'
assert decision_tree.predict((0, 10)) == 'x'
assert len(decision_tree.branches[0].branches) == 0
assert len(decision_tree.branches[1].branches) == 0
'''
data = {'x': [(0, 1), (0, 1), (0, 2), (1, 1), (1, 2), (1, 2)], 'o': [(0, 2), (1, 1), (1, 1), (1, 2)]}
decision_tree = DecisionTree(data, 1)
decision_tree.fit()

assert decision_tree.predict((3, 5)) == 'x'
assert decision_tree.predict((0, 0)) == 'x'
assert decision_tree.predict((3, 1)) == 'o'

random.seed(0)
initial_prediction = decision_tree.predict((0, 4))

for n in range(-10, 0):
    for num in range(2, 12):
        random.seed(0)
        assert decision_tree.predict((n, num)) == initial_prediction

print('PASSED')