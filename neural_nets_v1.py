import matplotlib.pyplot as plt


def predict(x, w13, w36, w14, w46, w56, w23, w24):
    return f(w36 * f(w13 * f(x) + w23) + w46 * f(w14 * f(x) + w24) + w56)


def f(x):
    return max(0, x)


def derivatve_f(x):
    if x <= 0:
        return 0

    return 1


def dRSS_dw13(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        i3 = w13 * f(point[0]) + w23
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * w36 * derivatve_f(i3) * f(point[0])

    return rss


def dRSS_dw36(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * f(w13 * f(point[0]) + w23)

    return rss


def dRSS_dw14(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        i4 = w14 * f(point[0]) + w24
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * w46 * derivatve_f(i4) * f(point[0])

    return rss


def dRSS_dw46(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * f(w14 * f(point[0]) + w24)

    return rss


def dRSS_dw56(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * 1

    return rss


def dRSS_dw23(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        i3 = w13 * f(point[0]) + w23
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * w36 * derivatve_f(i3) * 1

    return rss


def dRSS_dw24(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        i6 = w36 * f(w13 * f(point[0]) + w23) + w46 * f(w14 * f(point[0]) + w24) + w56
        i4 = w14 * f(point[0]) + w24
        rss += 2 * (predict(point[0], w13, w36, w14, w46, w56, w23, w24) - point[1]) * derivatve_f(i6) * w46 * derivatve_f(i4) * 1

    return rss


def RSS(points, w13, w36, w14, w46, w56, w23, w24):
    rss = 0

    for point in points:
        x, y = point
        prediction = predict(x, w13, w36, w14, w46, w56, w23, w24)
        rss += (y - prediction) ** 2

    return rss


rss_values = []

def run(points, alpha, num_steps, w13, w36, w14, w46, w56, w23, w24):
    num_step = 0
    print("Initial RSS: ", RSS(points, w13, w36, w14, w46, w56, w23, w24))

    for _ in range(num_steps):
        w13 = w13 - dRSS_dw13(points, w13, w36, w14, w46, w56, w23, w24) * alpha
        w36 = w36 - dRSS_dw36(points, w13, w36, w14, w46, w56, w23, w24) * alpha
        w14 = w14 - dRSS_dw14(points, w13, w36, w14, w46, w56, w23, w24) * alpha
        w46 = w46 - dRSS_dw46(points, w13, w36, w14, w46, w56, w23, w24) * alpha
        w56 = w56 - dRSS_dw56(points, w13, w36, w14, w46, w56, w23, w24) * alpha
        w23 = w23 - dRSS_dw23(points, w13, w36, w14, w46, w56, w23, w24) * alpha
        w24 = w24 - dRSS_dw24(points, w13, w36, w14, w46, w56, w23, w24) * alpha

        if num_step % 100 == 0:
            print("RSS at step ", num_step, ": ", RSS(points, w13, w36, w14, w46, w56, w23, w24))

        rss_values.append(RSS(points, w13, w36, w14, w46, w56, w23, w24))
        num_step += 1


    print("Final RSS: ", RSS(points, w13, w36, w14, w46, w56, w23, w24))


    return [w13, w36, w14, w46, w56, w23, w24]


final_values = run([(0, 5), (2,3), (5, 10)], 0.001, 1000, 1, 1, 1, 1, 1, 1, 1)


plt.style.use('bmh')
plt.plot([n for n in range(1, 1000 + 1)], [n for n in rss_values])
plt.xlabel('num_steps')
plt.ylabel('rss')
plt.savefig('neural_nets.png')

'''
x_values = []


for n in range(10):
    for num in range(0, 101):
        x_values.append(n + num * 0.01)

points = [(0, 5), (2,3), (5, 10)]

plt.scatter([point[0] for point in points], [point[1] for point in points])
plt.plot(x_values, [predict(x, 1, 1, 1, 1, 1, 1, 1) for x in x_values], label='Initial')
plt.plot(x_values, [predict(x, final_values[0], final_values[1], final_values[2], final_values[3], final_values[4], final_values[5], final_values[6]) for x in x_values], label='Final')
plt.savefig('regression.png')
'''