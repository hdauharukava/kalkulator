import math


def subtraction(a, b):
    return a - b


def root(a):
    if a <= 0:
        return f"You can't find square root of {a}"
    else:
        return math.sqrt(a)
