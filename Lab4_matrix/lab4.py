# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна робота №4
# Всюди виконував перший приклад, окрім 10 завдання

import numpy as np
import numpy.linalg


# 1. Знайти матрицю 𝐴𝐵−𝐵𝐴:
def num_1():
    a = np.matrix([[1, 2],
                   [4, -1]])

    b = np.matrix([[2, -3],
                   [-4, 1]])

    ab = np.dot(a, b)
    ba = np.dot(b, a)

    print(np.subtract(ab, ba))


# 2. Піднести матриці до степеня:
def num_2():
    i = np.matrix([[-1, 2], [0, 1]])
    print(numpy.linalg.matrix_power(i, 2))


# 3. Знайти добуток матриць
def num_3():
    a = np.matrix([[3, 5],
                   [6, -1]])
    b = np.matrix([[2, 1],
                   [-3, 2]])
    print(np.dot(a, b))


# 4.Обчислити визначники:
def num_4():
    a = np.matrix('2 3 4; 1 0 6; 7 8 9')
    print(np.linalg.det(a))


# 5.Обчислити визначники.
def num_5():
    a = np.matrix('1 2 3 4; -2 1 -4 3; 3 -4 -1 2; 4 3 -2 -1')
    print(np.linalg.det(a))


# 6.Знайти обернену матрицю до матриць:
def num_6():
    a = np.matrix('1 2 -3; 0 1 2; 0 0 1')
    print(np.linalg.inv(a))


# 7. Визначити ранг матриці:
def num_7():
    a = np.matrix('1 2 3 4; 3 -1 2 5; 1 2 3 4; 1 3 4 5')
    print(np.linalg.matrix_rank(a))


# 8. Розв’язати систему лінійних рівняньза формулами Крамера:
def num_8(a_matrix, b_matrix):
    a_det = np.linalg.det(a_matrix)

    x_matrix = np.matrix(a_matrix)
    x_matrix[:, 0] = b_matrix

    y_matrix = np.matrix(a_matrix)
    y_matrix[:, 1] = b_matrix

    z_matrix = np.matrix(a_matrix)
    z_matrix[:, 2] = b_matrix

    x = np.linalg.det(x_matrix) / a_det
    y = np.linalg.det(y_matrix) / a_det
    z = np.linalg.det(z_matrix) / a_det

    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')


# 9. Розв’язати матричним методом системи рівнянь:
def num_9(a_matrix, b_matrix):
    result = np.linalg.solve(a_matrix, b_matrix)
    print(f'x = {result[0, 0]}')
    print(f'y = {result[1, 0]}')
    print(f'z = {result[2, 0]}')


# Створіть прямокутну матрицю A з N рядками та стовпцями M звипадкових елементів.
# Знайдіть найнижче значення серед середніх значень для кожного рядка матриці.
def num_10(n, m):
    a = np.random.random((n, m))
    print("Matrix:")
    print(a)

    average_of_rows = np.mean(a, axis=0)
    print(f'Min average value of row = {min(average_of_rows)}')


if __name__ == '__main__':
    num_1()

    print("Task 2")
    num_2()

    print("Task 3")
    num_3()

    print("Task 4")
    num_4()

    print("Task 5")
    num_5()

    print("Task 6")
    num_6()

    print("Task 7")
    num_7()

    print("Task 8")
    num_8(np.matrix('14 4 6; 5 -3 2; 10 -11 5'), np.matrix('30; 15; 36'))

    print("Task 9")
    a = np.matrix('1 2 -1; 3 4 1; 5 1 -3')
    b = np.matrix('-3; 1; -2')
    num_9(a, b)

    print("Task 10 (2)")
    num_10(2, 2)