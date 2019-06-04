from math import *
import numpy as np
import matplotlib.pyplot as plt

def simpson13(n, a, b, f):
    h = (b - a) / n

    suma = 0.0

    for i in range(1, n):
        x = a + i * h

        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        else:
            suma = suma + 4 * fx(x, f)

    suma = suma + fx(a, f) + fx(b, f)
    rest = suma * (h / 3)

    return (rest)
    return print("el emú")


def fx(x, f):
    return eval(f)
