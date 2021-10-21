# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №6
# Варіант 23: sin(x) + 2y = 1.6
#             cos(y-1) + x = 1

import math
from scipy import optimize

f1 = lambda x: 0.8 - 0.5 * math.sin(x)
f2 = lambda y: 1 - math.cos(y - 1)


def iter(x, y, e):
    x1 = f1(x)
    y1 = f2(y)
    while (abs(x1 - x0) < e) and (abs(y1 - y0) < e):
        x1 = f1(x1)
        y1 = f2(y1)

    print(x1, y1)


def f(x):
    # x = x[0]
    # y = x[1]
    return math.sin(x[0]) + 2 * x[1] - 1.6, math.cos(x[1]) + x[0] - 1


if __name__ == '__main__':
    # x є [0; 0,1]
    # y є [0,7; 0,8]
    x0 = 0.1
    y0 = 0.8
    iter(x0, y0, 0.001)
    s = optimize.root(f, [0, 0], method='hybr')
    print(s.x)
