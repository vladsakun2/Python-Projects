# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №10
# Варіант 23

import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *

x = [1.2, 1.5, 1.9, 2.4, 3.1]
y = [0.82, 1.38, 0.45, 2.67, 1.5]
spl = UnivariateSpline(x, y)
xs = linspace(0, 3.1, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'b')
plt.grid(True)
plt.title("Sakun Spline")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(['Lab 10'], loc='upper right')
plt.show()
