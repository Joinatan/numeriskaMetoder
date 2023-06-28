import numpy as np
from matplotlib import pyplot as plt

def arct(x):
    return np.tan(x)

def geomSeq(n):
    return 1 * 2**n

x = np.linspace(0, 10, 10)

plt.plot(x, arct(x), 'o-r')

plt.show()

