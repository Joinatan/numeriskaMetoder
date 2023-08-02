import numpy as np
import matplotlib.pyplot as plt


def complexFunc(phase, r):
    '''
    Takes phase and radius and returns the complex number
    :param phase: phase of the complex function
    :param r: radius
    '''
    return r * np.exp(1j*phase)



x = np.linspace(0, 2 * np.pi, 40)
r_s = np.linspace(0.1, 1.0, 4)

list1 = []

for i in range(0, len(r_s)):
    for j in range(0, len(x)):
        list1.append(complexFunc(x[j],r_s[i]))

for item in r_s:
    plt.plot(complexFunc(x,item).real, complexFunc(x, item).imag)

plt.title('Plot of complexFunc with radius 0.1 to 1')
# plt.show()

def newton(f, fp, x_0, tol):
    '''
    find root of function by Newtons method
    :param f: function to find the root
    :param fp: derivative of function
    :param x_0: start value
    :param tol: tolerance
    '''
    x_n = x_0
    x_n_old = 0.
    for i in range(0, 400):
        x_n_old = x_n
        x_n = x_n - (f(x_n)/fp(x_n))
        if np.abs(x_n - x_n_old) < tol:
            return [x_n, True]
    else: return [x_n, False]

def polynom_3(x):
    return x**3 

def polynom_3_derivative(x):
    return 3*x**2

print(newton(polynom_3, polynom_3_derivative, -1, 0.000001))
