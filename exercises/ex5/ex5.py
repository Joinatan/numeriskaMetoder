from scipy.integrate import quad
import scipy as sp
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# task 1
def sinez(x, w):
    return np.sin(np.pi * 2 * x * w)

# print(quad(sinez, 0, np.pi/2, args=(2*np.pi,)))

# task 2
w_s = np.linspace(0, np.pi * 2, 1000)
# print(w_s)

integrandList = []
for item in w_s:
    # print(item)
    integrandList.append(quad(sinez, 0, np.pi/2, args=(item,))[0])


# plt.plot(w_s, integrandList)
# plt.xlabel('radian freq')
# plt.ylabel('integral')
# plt.show()

# print(integrandList)

# task3
def func3(x):
    return x**2 + x - 3

# print(fsolve(func3, 1))


#task4
def func4(x, a):
    return a * x**2 + x - 3

a_list = np.linspace(1, 5, 10)

zeros_list = []
for item in a_list:
    zeros_list.append(fsolve(func4, 1, args=(item)))

plt.plot(a_list, zeros_list)
plt.show()

