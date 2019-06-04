import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

media, desviacion_estandar = 16.666, 3.7267
normal = ss.norm(media, desviacion_estandar)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf((x))
plt.plot(x, fp)
plt.title('Distribución de probabilidad Normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
