import math
import random
import itertools
from itertools import permutations

data_set = [(0.0 , 7) , (0.2 , 5.6) , (0.4 , 3.56) , (0.6 , 1.23) , (0.8 , -1.03) ,
(1.0 , -2.89) , (1.2 , -4.06) , (1.4 , -4.39) , (1.6 , -3.88) , (1.8 , -2.64) ,
(2.0 , -0.92) , (2.2 , 0.95) , (2.4 , 2.63) , (2.6 , 3.79) , (2.8 , 4.22) ,
(3.0 , 3.8) , (3.2 , 2.56) , (3.4 , 0.68) , (3.6 , -1.58) , (3.8 , -3.84) ,
(4.0 , -5.76) , (4.2 , -7.01) , (4.4 , -7.38) , (4.6 , -6.76) , (4.8 , -5.22)]

normalized_data = []
min_x = min([x for x, y in data_set])
max_x = max([x for x, y in data_set])
min_y = min([y for x, y in data_set])
max_y = max([y for x, y in data_set])

for x, y in data_set:
    normalized_x = (x - min_x) / (max_x - min_y)
    normalized_y = (y - min_y) / (max_y - min_y) * 2 - 1
    normalized_data.append((normalized_x, normalized_y))

def activation_function(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))


class Node:
    def __init__(self, node_num):
        self.node_num = node_num
        self.parents = []
        self.node_input = None
        self.node_output = 0


class EvolvedNeuralNet:
    def __init__(self, num_nodes, node_weights, bias_node_nums, mutation_rate):
        self.nodes = [Node(n + 1) for n in range(num_nodes)]
        self.node_weights = node_weights
        self.bias_nodes = bias_node_nums

        for bias_node_num in self.bias_nodes:
            self.nodes[bias_node_num - 1].node_output = 1

        for weight in node_weights:
            i, n = weight.split(',')
            current_node = self.nodes[int(i) - 1]
            next_node = self.nodes[int(n) - 1]
            next_node.parents.append(current_node)

    def build_neural_net(self, input_value):
        self.nodes[0].node_input = input_value
        self.nodes[0].node_output = activation_function(input_value)

        for node in self.nodes:
            if node.node_num == 1 or node.node_num in self.bias_nodes:
                continue

            total_input = 0

            for input_node in node.parents:
                total_input += input_node.node_output * self.node_weights[str(input_node.node_num) + ',' + str(node.node_num)]

            node.node_input = total_input

            node.node_output = activation_function(total_input)

        return self

    def get_node_outputs(self):
        info_dict = {}

        for node in self.nodes:
            info_dict[node.node_num] = node.node_output

        return info_dict

    def get_node(self, node_num):
        return self.nodes[node_num - 1]


def get_weight_ids(layer_sizes, bias_node_nums):
    weight_ids = []
    num_nodes_in_layer = {}
    num_nodes = 0
    nodes = {}

    for n in range(1, len(layer_sizes) + 1):
        num_nodes_in_layer[n] = []
        nodes[n] = []

    for key in num_nodes_in_layer:
        max_node_num_in_layer = layer_sizes[key - 1]

        if key == 1 or key == len(layer_sizes):
            num_nodes_in_layer[key] = [n for n in range(1, layer_sizes[key - 1] + 1)]
        
        else:
            num_nodes_in_layer[key] = [n for n in range(1, layer_sizes[key - 1] + 2)]


    for key in num_nodes_in_layer:
            
        for node_num in num_nodes_in_layer[key]:
            num_nodes += 1
            nodes[key].append(str(num_nodes))

    
    for key in range(1, len(nodes.keys())):
        for n in nodes[key]:

            for num in nodes[key + 1]:
                if int(num) not in bias_node_nums:
                    weight_ids.append(n + ',' + num)


    return weight_ids

    
def RSS(points, neural_net):
    rss = 0

    for x, y in points:
        neural_net.build_neural_net(x)
        prediction = neural_net.get_node(24).node_output
        rss += (y - prediction) ** 2

    return rss


            
population = {}
bias_node_nums = [12, 19, 23]

for n in range(30):
    weight_ids = get_weight_ids([1, 10, 6, 3, 1], bias_node_nums)
    weights = {}

    for weight_id in weight_ids:
        weights[weight_id] = random.uniform(-0.2, 0.2)	
    
    neural_net = EvolvedNeuralNet(24, weights, bias_node_nums, 0.05)
    population[neural_net] = None

population_list_of_tuples = []

for neural_net in population:
    rss = RSS(normalized_data, neural_net)
    population[neural_net] = rss
    population_list_of_tuples.append((neural_net, rss))

sorted_tuple_list = (sorted(population_list_of_tuples, key = lambda x: x[1]))
parents = [x for x, y in sorted_tuple_list[:15]]

print(len(parents))