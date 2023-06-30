# from numpy import *
# from matplotlib.pyplot import *
import numpy as np
from matplotlib import pyplot as plt

# Task 1
def approx_ln(x,n):
    '''
    Function for approximation of logratithms.
    x is where the approximation takes place.
    n is the number of iterations of approxiamtion. 
    Bigger n -> closer approximation
    '''
    a = (1+x)/2
    g = np.sqrt(x)
    
    for i in range(0, n):
        a = (a + g)/2
        g = np.sqrt(a*g)
    
    return (x-1)/a


# Task 2
xlist = range(1, 100)

# Exact vs approximation
plt.figure(1)
y1 = [np.log(x) for x in xlist]
plt.plot(xlist, y1, label = 'Exact')
for i in range(1, 4)   : 
    y2 = [approx_ln(x, i) for x in xlist]
    plt.plot(xlist, y2, label = f'n={i}', linestyle="--")

plt.title('Exact vs approximation')
plt.legend()
plt.xlabel("x")
plt.ylabel("ln(x)")

# Difference
plt.figure(2)
y1 = [np.log(x) for x in xlist]
for i in range(1, 11)   : 
    y2 = [approx_ln(x, i) for x in xlist]
    diff = [np.abs(y1[j] - y2[j]) for j in range(0, len(y2)) ]
    plt.plot(xlist, diff, label = f'n={i}')

plt.legend()
plt.title('Difference')
plt.xlabel("x")
plt.ylabel("|ln(x) - approx|")

# Task 3
plt.figure(3)
nlist = range(1, 20)
x = 1.41
e = [np.abs(np.log(x) - approx_ln(x, nlist[i-1])) for i in nlist]
plt.plot(nlist, e)
plt.xlabel("n")
plt.ylabel("|Error|")
plt.title("e as a function of n for x = 1.41")


# Task 4
def fast_approx_ln(x,n):
    '''
    Function for approximation of logratithms.
    Similiar to the previous one but converges faster.
    x is where the approximation takes place.
    n is the number of iterations of approxiamtion. 
    '''
    d = [[0] * (n+1) for _ in range(n+1)]  # Initialize the 2D list to store the values of d
    a = (1+x)/2
    g = np.sqrt(x)
    for i in range(0, n+1):
        d[i][0] = a
        a = (a + g)/2
        g = np.sqrt(a*g)
        for k in range(1, i+1):
            d[i][k] = (d[i][k-1] - 4**(-k)*d[i-1][k-1]) / (1-4**(-k))
        
    
    return (x-1)/d[n][n]
    

# Task 5
plt.figure(4)

x = np.linspace(0.01, 20, 100)
exact = [np.log(val) for val in x]

for i in range(2,7):
    approx_log_values = [fast_approx_ln(val, i) for val in x]
    y = [np.abs(exact[val] - approx_log_values[val]) for val in range(0,100)]
    plt.plot(x, y, '--', label = f'iteration {i}')

plt.legend()
plt.ylabel("error")
plt.xlabel("x")
plt.title("Error of accelerated version")
plt.yscale('log')

plt.show()



