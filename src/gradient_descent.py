class GradientDescent():
    def __init__(self, function, initial_point):
        self.function = function
        self.points = initial_point

    def compute_gradient(self, delta):
        dimension = self.function.__code__.co_argcount
        gradient_list = []

        for n in range(dimension):
            args = list(self.points)
            args_2 = list(self.points)
            args[n] += 0.5 * delta
            args_2[n] -= 0.5 * delta
            derivative = ((self.function(*args) - self.function(*args_2))) / delta
            gradient_list.append(derivative)

        return gradient_list

    def descend(self, alpha, delta, num_steps):
        gradient_list = self.compute_gradient(delta)

        for _ in range(num_steps):
            for n in range(len(gradient_list)):
                self.points[n] -= alpha * gradient_list[n]

        return gradient_list
