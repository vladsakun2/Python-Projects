# @copyright Сакун Владислав Олександрович ФІТ 2-4
# Лабораторна №3
# Варіант 24(6) - 6*x^4+8*x^3-24*x^2-7=0

# функція
f = lambda x: 6 * x ** 4 + 8 * x ** 3 - 24 * x ** 2 - 7

# похідна 1 порядку
f_1 = lambda x: 24 * x ** 3 + 24 * x ** 2 - 48 * x

# похідна 2 порядку
f_2 = lambda x: 72 * x ** 2 + 48 * x - 48

# xn2
calculate_XN2 = lambda xp2: xp2 - f(xp2) / f_1(xp2)

# xn1
calculate_XN1 = lambda xp1, xp2: xp1 - f(xp1) * (xp2 - xp1) / (f(xp2) - f(xp1))


# Метод Ньютона
def nuton_method(a, b, e):
    if f_1(b) * f_2(b) > 0:
        x = b
    else:
        x = a

    h = f(x) / f_1(x)
    x = x - h

    if abs(h) <= e:
        print(f(x))
    else:
        h = f(x) / f_1(x)
        x = x - h

    return x


# Комбінований метод
def combination_method(a, b, e):
    if f_1(a) * f_2(a) < 0:
        a0 = b
        b0 = a
    else:
        a0 = a
        b0 = b

    xp1 = f(b) - f(a)
    xp2 = b0

    xn1 = calculate_XN1(xp1, xp2)
    xn2 = calculate_XN2(xp2)
    xp1 = xn1
    xp2 = xn2

    while xp2 - xp1 >= e:
        xn1 = calculate_XN1(xp1, xp2)
        xn2 = calculate_XN2(xp2)
        xp1 = xn1
        xp2 = xn2

    x = (xp1 + xp2) / 2

    return x


if __name__ == '__main__':
    print(nuton_method(1, 2, 0.0001))
    print(combination_method(-1, 0, 0.0001))
