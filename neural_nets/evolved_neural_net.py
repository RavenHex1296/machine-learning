import math
import random
import itertools
import numpy as np
import matplotlib.pyplot as plt
import time

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
bias_node_nums = [12, 19, 23]

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
        self.mutation_rate = mutation_rate

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


def make_new_gen(parents):
    children = []

    for parent in parents:
        child_weights = {}

        for weight in parent.node_weights:
            child_weights[weight] = parent.node_weights[weight] + parent.mutation_rate * np.random.normal(0, 1)

        child_mutation_rate = parent.mutation_rate * math.exp(np.random.normal(0, 1) / ((2 ** 0.5) * (len(child_weights.keys()) ** 0.25)))

        child = EvolvedNeuralNet(24, child_weights, bias_node_nums, child_mutation_rate)
        children.append(child)

    return children


def make_first_gen(population_size):
    first_gen = []

    for n in range(population_size):
        weight_ids = get_weight_ids([1, 10, 6, 3, 1], bias_node_nums)
        weights = {}

        for weight_id in weight_ids:
            weights[weight_id] = random.uniform(-0.2, 0.2)	
        
        neural_net = EvolvedNeuralNet(24, weights, bias_node_nums, 0.05)
        first_gen.append(neural_net)

    return first_gen


def get_avg_rss_value(neural_nets, points):
    rss_total = 0

    for neural_net in neural_nets:
        rss = RSS(points, neural_net)
        rss_total += rss

    return rss_total / len(neural_nets)


def get_sorted_by_rss_nets(neural_nets):
    population_list_of_tuples = []

    for neural_net in neural_nets:
        rss = RSS(normalized_data, neural_net)
        population_list_of_tuples.append((neural_net, rss))

    return (sorted(population_list_of_tuples, key = lambda x: x[1]))


x_values = []


for n in range(1):
    for num in range(0, 101):
        x_values.append(n + num * 0.01)


def run(num_generations): 
    avg_rss_values = []
    first_gen = make_first_gen(30)
    plt.scatter([point[0] for point in normalized_data], [point[1] for point in normalized_data])

    for neural_net in first_gen:

        initial_predicted_values = []

        for x in x_values:
            neural_net.build_neural_net(x)
            initial_predicted_values.append(neural_net.get_node(24).node_output)

        plt.plot([x for x in x_values], initial_predicted_values, color="red")



    avg_rss_values.append(get_avg_rss_value(first_gen, normalized_data))

    sorted_tuple_list = get_sorted_by_rss_nets(first_gen)
    parents = [x for x, y in sorted_tuple_list[:15]]

    for _ in range(num_generations - 1):
        current_gen = make_new_gen(parents) + parents
        avg_rss_values.append(get_avg_rss_value(current_gen, normalized_data))
        sorted_tuple_list = get_sorted_by_rss_nets(current_gen)
        parents = [x for x, y in sorted_tuple_list[:15]]

    for neural_net in current_gen:

        final_predicted_values = []

        for x in x_values:
            neural_net.build_neural_net(x)
            final_predicted_values.append(neural_net.get_node(24).node_output)

        plt.plot([x for x in x_values], final_predicted_values, color="blue")
        plt.xlabel('x')
        plt.ylabel('predicted values')
    plt.savefig('initial_vs_final_neural_nets.png')
    plt.clf()

    return avg_rss_values



start_time = time.time()
num_generations = 5000
avg_values = run(num_generations)
print(avg_values)
plt.plot([x for x in range(num_generations)], avg_values)
plt.xlabel('# generations completed')
plt.ylabel('avg rss values')
plt.savefig('avg_rss_evolved_neural_net.png')
print(time.time() - start_time)


