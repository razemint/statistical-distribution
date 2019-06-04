import numpy as np
from cal.simpson import simpson13, fx

n = int(input("inserta el número de iteraciones\n"))
a = float(input("inserta intervalo inferior\n"))
b = float(input("inserta intervalo superior\n"))
f = str(input("inserta la función\n"))


print("el resultado de la integral es: ")
print(simpson13(n, a, b, f))
