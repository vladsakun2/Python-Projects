# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №7

from numpy import *
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

x = array([-2, 0, 1, 2], dtype=float)
y = array([30, -4, 3, 18], dtype=float)


def defaultPlotConfings():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)


def L(x, y, k):
    sum = 0
    for i in range(len(y)):
        p1 = 1
        p2 = 1
        for j in range(len(x)):
            if j == i:
                p1 *= 1
                p2 *= 1
            else:
                p1 *= k - x[j]
                p2 *= x[i] - x[j]
        sum += y[i] * p1 / p2
    return sum


xnew = linspace(min(x), max(x))
ynew = [L(x, y, i) for i in xnew]
plt.plot(x, y, 'r+', xnew, ynew)
plt.title('Sakun Vlad')
plt.legend("Lab 7")
defaultPlotConfings()
plt.show()

f = lagrange(x, y)
fig = plt.figure(figsize=(10, 8))
plt.plot(xnew, f(xnew), 'y', x, y, 'r+')
plt.title('Lagrange polynom')
defaultPlotConfings()
plt.show()
