# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №9
# Варіант 23
import math
import matplotlib.pyplot as plt


def nuton_interpolation(x, y, x1, x2, h):
    delta_y = delta_fun(y)
    print("Delta y: ", delta_y)

    delta2_y = delta_fun(delta_y)
    print("Delta 2 y: ", delta2_y)

    delta3_y = delta_fun(delta2_y)
    print("Delta 3 y: ", delta3_y)

    delta4_y = delta_fun(delta3_y)
    print("Delta 4 y: ", delta4_y)

    delta5_y = delta_fun(delta4_y)
    print("Delta 5 y: ", delta5_y)

    q1 = q(x1, x[0], h)
    q2 = q(x2, x[len(x) - 1], h)

    print("q1: ", q1)
    print("q2: ", q2)

    firstInterpol = firstInterpolation(y[0], delta_y[0], delta2_y[0], delta3_y[0], delta4_y[0], delta5_y[0], q1)
    print("Результат обчислення за першою інтерполяційною формулою Ньютона: ", firstInterpol)

    secondIntepol = secondInterpolation(last_y=y[-1],
                                        last_delta=delta_y[-1],
                                        last_delta_2=delta2_y[-1],
                                        last_delta_3=delta3_y[-1],
                                        last_delta_4=delta4_y[-1],
                                        last_delta_5=delta5_y[-1],
                                        q=q2)

    print("Результат обчислення за другою інтерполяційною формулою Ньютона: ", secondIntepol)

    point1 = [x1, firstInterpol]
    point2 = [x2, secondIntepol]

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]

    plt.plot(x_values, y_values)
    plt.grid(True)
    plt.title("Sakun Vlad #23")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# Розрахунок дельты
def delta_fun(prev_delta_y):
    delta_y = []
    for i in range(1, len(prev_delta_y)):
        delta_y.append(prev_delta_y[i] - prev_delta_y[i - 1])
    return delta_y


# q = (x-x0)/h
q = lambda x, x0, h: (x - x0) / h


# перша нтерполяційна формула Ньютона:
def firstInterpolation(y0, delta_y0, delta_2_y0, delta_3_y0, delta_4_y0, delta_5_y0, q):
    return y0 + q * delta_y0 + ((q * (q - 1)) / math.factorial(2)) * delta_2_y0 + (
            (q * (q - 1) * (q - 2)) / math.factorial(3)) * delta_3_y0 + (
                   (q * (q - 1) * (q - 2) * (q - 3)) / math.factorial(4)) * delta_4_y0 + (
                   (q * (q - 1) * (q - 2) * (q - 3) * (q - 4)) / math.factorial(5)) * delta_5_y0


# друга нтерполяційна формула Ньютона
def secondInterpolation(last_y, last_delta, last_delta_2, last_delta_3, last_delta_4, last_delta_5, q):
    return last_y + q * last_delta + ((q * (q + 1)) / math.factorial(2)) * last_delta_2 + (
            (q * (q + 1) * (q + 2)) / math.factorial(3)) * last_delta_3 + (
                   (q * (q + 1) * (q + 2) * (q + 3)) / math.factorial(4)) * last_delta_4 + (
                   (q * (q + 1) * (q + 2) * (q + 3) * (q + 4)) / math.factorial(5)) * last_delta_5


if __name__ == '__main__':
    # Значення за умовою для варіанту 23
    x = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
    y = [0.8607, 0.8187, 0.7788, 0.7408, 0.7046, 0.6703]

    # Крок таблиці
    h = x[1] - x[0]

    # Значення за умовою для варіанту 23
    x1 = 0.252
    x2 = 0.457
    nuton_interpolation(x, y, x1, x2, h)
