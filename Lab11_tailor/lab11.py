# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №11
# Варіант 13


import numpy as np
import matplotlib.pyplot as plt
from numpy import cos
from numpy import sin

# функція
f = lambda x: 5 * cos(x)

# похідна 1 порядку
f1 = lambda x: -5 * sin(x)

# похідна 2 порядку
f2 = lambda x: -5 * cos(x)

# похідна 3 порядку
f3 = lambda x: 5 * sin(x)

# функція наближення за многочленом Тейлора
tailor = lambda a, x: f(a) + f1(a) + f2(a) * (x ** 2 / 2) + f3(a) * (x ** 3 / 6)

if __name__ == '__main__':
    x = np.linspace(-1, 1)
    y = f(x)
    tailor_value = tailor(0, x)
    plt.plot(x, y, 'r', x, tailor_value, 'b')
    plt.grid(True)
    plt.title('Сакун В.О.')
    plt.legend(['Наближення Тейлора'])
    plt.show()
