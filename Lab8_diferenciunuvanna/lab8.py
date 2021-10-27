# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №8
# Варіант 23
# Числове диференціювання

# Умова
import decimal

x = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
y = [0.8607, 0.8187, 0.7788, 0.7408, 0.7046, 0.6703]

# Крок таблиці
h = x[1] - x[0]

decimal.getcontext().prec = 20

def nuton():
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

    derivative_1 = (1 / h) * (delta_y[1] - (delta2_y[1] / 2) + (delta3_y[1] / 3) - (delta4_y[1] / 4))
    print("Derivative 1: ", derivative_1)

    derivative_2 = (1 / h ** 2) * (delta2_y[1] - delta3_y[1] + (11 / 12) * delta4_y[1])
    print("Derivative 2: ", derivative_2)


def delta_fun(prev_delta_y):
    delta_y = []
    for i in range(1, len(prev_delta_y)):
        delta_y.append(decimal.Decimal(prev_delta_y[i]) - decimal.Decimal(prev_delta_y[i - 1]))
    return delta_y


if __name__ == '__main__':
    nuton()
