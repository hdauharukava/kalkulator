import math


def substraction(a, b):
    return a - b


def root(a):
    return math.sqrt(a)


def division(a, b):
    if b != 0:
        return round(a / b, 3)
    else:
        return f"You can't divide by zero!"
