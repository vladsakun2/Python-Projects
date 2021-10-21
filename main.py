import re


def boundary_accuracy(x1, accurate_x1):
    """Функція повернтає граничну відносну похибку
    х1 - приблизне число, accurate_x1 - значення із більшою кількістю десяткових знаків"""
    delta_accuracy = round(abs(x1 - accurate_x1), 7)
    delta_accuracy_string = str(delta_accuracy).strip('0').strip('.')
    delta_accuracy = delta_accuracy + pow(10, 0 - len(delta_accuracy_string))
    boundary_accuracy_value = abs((x1 - accurate_x1) / x1)
    return boundary_accuracy_value


def exercise_1():
    # x1 = float(input("Введіть х1: \n"))
    # accurate_x1 = float(input("Введіть точне значення X1: \n"))
    # x2 = float(input("Введіть х2: \n"))
    # accurate_x2 = float(input("Введіть точне значення X2: \n"))

    if boundary_accuracy(4.24, 4.2426) > boundary_accuracy(0.818, 0.81818):
        print("The second accuracy is more accurate ")
    else:
        print("The first accuracy is more accurate ")


def num_decimal_places(value):
    m = re.match(r"^[0-9]*\.([1-9]([0-9]*[1-9])?)0*$", value)
    return len(m.group(1)) if m is not None else 0


def compute_n(x, accuracy):
    integer_number = int(x)
    m = 0
    if integer_number == 0:
        for char in str(x):
            m = m - 1
            if char != '0':
                break
    else:
        m = (x // 10 % 10) - 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 1

    b = 2

    c = 3

    d = 4

    e = 5

    if a >= b >= c >= d >= e:
        print("The biggest number: ", str(a))
    elif b >= c >= a >= d >= e:
        print("The biggest number: ", str(b))
    elif c >= b >= a >= d >= e:
        print("The biggest number: ", str(c))
    elif d >= a >= b >= c >= e:
        print("The biggest number: ", str(d))
    elif e >= a >= b >= c >= d:
        print("The biggest number: ", str(e))
