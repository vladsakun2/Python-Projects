# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №7_0
# Варіант 23 Y(x)=cos(x^4)/x, x=[0...1]
from numpy import linspace
from numpy import cos
import matplotlib.pyplot as plt

f = lambda x: cos(x ** 4) / x


def drawPlot(x1, x2):
    t = linspace(x1, x2, 100)
    y = f(t)
    plt.plot(t, y)
    plt.show()


if __name__ == '__main__':
    drawPlot(0, 1)
