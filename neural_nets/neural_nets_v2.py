#import matplotlib.pyplot as plt
import math

def f(x):
    return max(0, x)


def derivatve_f(x):
    if x <= 0:
        return 0

    return 1


class Node:
    def __init__(self, node_num):
        self.node_num = node_num
        self.input_list = []
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
            next_node.input_list.append(current_node)

    def build_neural_net(self):
        for node in self.nodes:
            if node.node_num == 1 or node.node_num in self.bias_nodes:
                continue

            total_input = 0

            for input_node in node.input_list:
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


def get_node_derivatives(initial_points, node_weights, bias_nodes):
    node_derivatives = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    random_net = NeuralNet(6, node_weights, 2, bias_nodes)

    for node in reversed(random_net.nodes):
        for x, y in initial_points:
            neural_net = NeuralNet(6, node_weights, x, bias_nodes)
            neural_net.build_neural_net()

            if node.node_num == 6:
                node_derivatives[node.node_num] += 2 * (neural_net.get_node(6).node_output - y)

            if node.node_num == 5:
                node_derivatives[node.node_num] += node_derivatives[6] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['56']

            if node.node_num == 4:
                node_derivatives[node.node_num] += node_derivatives[6] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['46']

            if node.node_num == 3:
                node_derivatives[node.node_num] += node_derivatives[6] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['36']

            if node.node_num == 2:
                node_derivatives[node.node_num] +=  node_derivatives[4] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['24'] +  node_derivatives[3] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['23']

            if node.node_num == 1:
                node_derivatives[node.node_num] +=  node_derivatives[4] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['14'] +  node_derivatives[3] * derivatve_f(neural_net.get_node(6).node_input) * node_weights['13']

    return node_derivatives


def get_weight_derivatives(initial_points, node_weights, bias_nodes):
    weight_derivatives = {'13': 0, '36': 0, '14': 0, '46': 0, '56': 0, '23': 0, '24': 0}
    weight_ids = ['13', '36', '14', '46', '56', '23', '24']
    node_derivatives = get_node_derivatives(initial_points, node_weights, bias_nodes)

    for x, y in weight_ids:
        for point in initial_points:
            neural_net = NeuralNet(6, node_weights, point[0], bias_nodes)
            neural_net.build_neural_net()
            weight_derivatives[x + y] += node_derivatives[int(y)] * derivatve_f(neural_net.get_node(int(y)).node_input) * neural_net.get_node(int(x)).node_output

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


def run(points, alpha, num_steps, node_weights, bias_nodes):
    num_step = 0

    for _ in range(num_steps):
        weight_derivatives = get_weight_derivatives([(0, 5), (2, 3), (5, 10)], node_weights, bias_nodes)

        for weight in node_weights:
            node_weights[weight] = node_weights[weight] - weight_derivatives[weight] * alpha

        if num_step % 100 == 0:
            print("RSS at step ", num_step, ": ", RSS(points, node_weights, bias_nodes))

        rss_values.append(RSS(points, node_weights, bias_nodes))
        print(num_step, weight_derivatives)
        num_step += 1

    print("Final RSS: ", RSS(points, node_weights, bias_nodes))

    return node_weights

node_weights = {'13': 1, '36': 1, '14': 1, '46': 1, '56': 1, '23': 1, '24': 1}
bias_nodes = [2, 5]
neural_net = NeuralNet(6, node_weights, 2, bias_nodes)
print(neural_net.build_neural_net().get_node(6).node_output)


'''
final_values = run([(0, 5), (2,3), (5, 10)], 0.0001, 2, node_weights, bias_nodes)
print(final_values)
plt.style.use('bmh')
plt.plot([n for n in range(1, len(rss_values) + 1)], [n for n in rss_values])
plt.xlabel('num_steps')
plt.ylabel('rss')
plt.savefig('backward_propagation.png')


x_values = []


for n in range(10):
    for num in range(0, 101):
        x_values.append(n + num * 0.01)

points = [(0, 5), (2,3), (5, 10)]

plt.scatter([point[0] for point in points], [point[1] for point in points])

initial_predicted_values = []
final_predicted_values = []
initial_node_weights = {'13': 1, '36': 1, '14': 1, '46': 1, '56': 1, '23': 1, '24': 1}

for x in x_values:
    neural_net = NeuralNet(6, initial_node_weights, x, bias_nodes)
    neural_net.build_neural_net()
    initial_predicted_values.append(neural_net.get_node(6).node_output)

    final_net = NeuralNet(6, final_values, x, bias_nodes)
    final_net.build_neural_net()
    final_predicted_values.append(final_net.get_node(6).node_output)


plt.plot(x_values, initial_predicted_values, label='Initial')
plt.plot(x_values, final_predicted_values, label='Final')
plt.xlim([-1, 11])
plt.ylim([-1, 11])
plt.savefig('backward_propagation_regression-xd.png')
'''
#x^2 diverges, probs because exponentially always increasing
#same for e^x and e^e^x
#1/x and 1/x^5 diverges because 0 cant be an input
