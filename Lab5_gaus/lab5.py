# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна робота №5

import numpy as np


def gaus(matrix_a, matrix_b):
    n = len(matrix_b)
    k = 1

    while k <= n - 1:
        i = k + 1

        while i < n:
            if matrix_a[i, k] != 0.0:
                l = matrix_a[i, k] / matrix_a[k, k]
                matrix_a[i, k + 1:n] = matrix_a[i, k + 1:n] - 1 * matrix_a[k, k + 1:n]
                matrix_b[i] = matrix_b[i] - l * matrix_b[k]
            i += 1
        k += 1

    k = n - 1
    while k > -1:
        matrix_b[k] = (matrix_b[k] - np.dot(matrix_a[k, k + 1:n], matrix_b[k + 1:n])) / matrix_a[k, k]
        k -= 1

    print('Checking: ', np.linalg.solve(matrix_a, matrix_b))

    jordanGausResult = jordanGaus(matrix_a, matrix_b)
    print('Method of Jordan - Gaus: ', jordanGausResult)
    return matrix_b


def jordanGaus(a, b):
    return np.linalg.inv(a) * b


if __name__ == '__main__':
    print('Gaus: ', gaus(np.matrix('1 -2 3; 4 2 -3; 3 -3 5'), np.matrix('-5; 0; -9')))
