import math

def f(x):
    if x > 0:
        return x

    return 0


def derivatve_f(x):
    if x <= 0:
        return 0

    return 1


class Node:
    def __init__(self, node_num):
        self.node_num = node_num
        self.parents = []
        self.node_input = None
        self.node_output = 0


class NeuralNet:
    def __init__(self, num_nodes, node_weights, initial_input_value, bias_node_nums):
        self.nodes = [Node(n + 1) for n in range(num_nodes)]
        self.initial_input_value = initial_input_value
        self.node_weights = node_weights
        self.bias_nodes = bias_node_nums

        self.nodes[0].node_input = initial_input_value
        self.nodes[0].node_output = f(initial_input_value)

        for bias_node_num in self.bias_nodes:
            self.nodes[bias_node_num - 1].node_output = 1

        for weight in node_weights:
            current_node = self.nodes[int(weight[0]) - 1]
            next_node = self.nodes[int(weight[1]) - 1]
            next_node.parents.append(current_node)

    def build_neural_net(self):
        for node in self.nodes:
            if node.node_num == 1 or node.node_num in self.bias_nodes:
                continue

            total_input = 0

            for input_node in node.parents:
                total_input += input_node.node_output * self.node_weights[str(input_node.node_num) + str(node.node_num)]

            node.node_input = total_input
            node.node_output = f(total_input)

        return self

    def get_node_outputs(self):
        info_dict = {}

        for node in self.nodes:
            info_dict[node.node_num] = node.node_output

        return info_dict

    def get_node(self, node_num):
        return self.nodes[node_num - 1]


def set_up_multiple_initial_points(num_nodes, node_weights, points, bias_node_nums):
    points_data = {}

    for point in points:
        neural_net = NeuralNet(num_nodes, node_weights, point[0], bias_node_nums)
        points_data[point] = neural_net.build_neural_net()

    return points_data


def get_node_derivatives(points_with_nets):
    node_derivatives = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    individual_stuff = {}

    for point in points_with_nets:
        individual_stuff[point] = {}
    

    for key in points_with_nets:
        for node in reversed(points_with_nets[key].nodes):
            if node.node_num == 6:
                individual_stuff[key][node.node_num] = 2 * (points_with_nets[key].get_node(6).node_output - key[1])

            if node.node_num == 5:
                individual_stuff[key][node.node_num] = individual_stuff[key][6] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['56']

            if node.node_num == 4:
                individual_stuff[key][node.node_num] = individual_stuff[key][6] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['46']

            if node.node_num == 3:
                individual_stuff[key][node.node_num] = individual_stuff[key][6] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['36']

            if node.node_num == 2:
                individual_stuff[key][node.node_num] =  individual_stuff[key][4] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['24'] +  individual_stuff[key][3] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['23']

            if node.node_num == 1:
                individual_stuff[key][node.node_num] =  individual_stuff[key][4] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['14'] +  individual_stuff[key][3] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['13']

    #for point in individual_stuff:
        #for node in individual_stuff[point]:
            #node_derivatives[node] += individual_stuff[point][node]

    return individual_stuff


def get_weight_derivatives(num_nodes, node_weights, points, bias_nodes):
    weight_derivatives = {}
    individual_stuff = {}

    for point in points:
        individual_stuff[point] = {}

    for weight in node_weights:
        weight_derivatives[weight] = 0

    points_with_nets = set_up_multiple_initial_points(num_nodes, node_weights, points, bias_nodes)

    node_derivatives = get_node_derivatives(points_with_nets)

    for point in points_with_nets:
        for x, y in node_weights:
            individual_stuff[point][x + y] = node_derivatives[point][int(y)] * derivatve_f(points_with_nets[point].get_node(int(y)).node_input) * points_with_nets[point].get_node(int(x)).node_output


    for point in individual_stuff:
        for weight in individual_stuff[point]:
            weight_derivatives[weight] += individual_stuff[point][weight]

    return weight_derivatives


def RSS(points, node_weights, bias_nodes):
    rss = 0

    for x, y in points:
        neural_net = NeuralNet(6, node_weights, x, bias_nodes)
        neural_net.build_neural_net()
        prediction = neural_net.get_node(6).node_output
        rss += (y - prediction) ** 2

    return rss


rss_values = []


def run(points, alpha, num_steps, num_nodes, node_weights, bias_nodes):
    num_step = 0

    for _ in range(num_steps):
        weight_derivatives = get_weight_derivatives(num_nodes, node_weights, points, bias_nodes)
        print(num_step, weight_derivatives)

        for weight in node_weights:
            node_weights[weight] = node_weights[weight] - weight_derivatives[weight] * alpha

        if num_step % 100 == 0:
            print("RSS at step ", num_step, ": ", RSS(points, node_weights, bias_nodes))

        rss_values.append(RSS(points, node_weights, bias_nodes))
        num_step += 1

    print("Final RSS: ", RSS(points, node_weights, bias_nodes))

    return node_weights

print(run([(0, 5), (2,3), (5, 10)], 0.0001, 2, 6, {'13': 1, '36': 1, '14': 1, '46': 1, '56': 1, '23': 1, '24': 1}, [2, 5]))

#print(get_node_derivatives(set_up_multiple_initial_points(6, {'13': 1, '36': 1, '14': 1, '46': 1, '56': 1, '23': 1, '24': 1},[(0, 5), (2,3), (5, 10)], [2, 5])))
#3, 7, 13 respectively

'''
def get_node_derivatives(points_with_nets):
    node_derivatives = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    individual_stuff = {}

    for point in points_with_nets:
        individual_stuff[point] = node_derivatives
    

    for key in points_with_nets:
        for node in reversed(points_with_nets[key].nodes):
            if node.node_num == 6:
                node_derivatives[node.node_num] += 2 * (points_with_nets[key].get_node(6).node_output - key[1])

            if node.node_num == 5:
                print("d", node_derivatives[6])
                node_derivatives[node.node_num] += node_derivatives[6] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['56']

            if node.node_num == 4:
                node_derivatives[node.node_num] += node_derivatives[6] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['46']

            if node.node_num == 3:
                node_derivatives[node.node_num] += node_derivatives[6] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['36']

            if node.node_num == 2:
                node_derivatives[node.node_num] +=  node_derivatives[4] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['24'] +  node_derivatives[3] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['23']

            if node.node_num == 1:
                node_derivatives[node.node_num] +=  node_derivatives[4] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['14'] +  node_derivatives[3] * derivatve_f(points_with_nets[key].get_node(6).node_input) * points_with_nets[key].node_weights['13']

    return node_derivatives

def get_weight_derivatives(num_nodes, node_weights, points, bias_nodes):
    weight_derivatives = {}
    weight_ids = []

    for weight in node_weights:
        weight_derivatives[weight] = 0
        weight_ids.append(weight)

    points_with_nets = set_up_multiple_initial_points(num_nodes, node_weights, points, bias_nodes)

    node_derivatives = get_node_derivatives(points_with_nets)

    for x, y in weight_ids:
        for key in points_with_nets:
            weight_derivatives[x + y] += node_derivatives[int(y)] * derivatve_f(points_with_nets[key].get_node(int(y)).node_input) * points_with_nets[key].get_node(int(x)).node_output

    return weight_derivatives
'''