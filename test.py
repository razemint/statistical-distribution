import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

a = int(input("inserta mu"))
b = int(input("inserta mu"))
c = int(input("inserta mu"))


x = np.random.normal(a, b, c)
print(x)


print(np.var(x))
print(np.average(x))
