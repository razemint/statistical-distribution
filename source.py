import pip
import seaborn as sns
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython


np.random.seed(2019)

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

mu, sigma = 0, 0.2
datos = np.random.normal(mu, sigma, 1000)

cuenta, cajas, ignorar = plt.hist(datos, 20)
plt.ylabel('memo')
plt.xlabel('irvinho')
plt.title('memo sobre irvinho')
plt.show()
