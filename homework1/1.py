import numpy as np
from matplotlib import pyplot as plt
#--------------------Approximate Log-function
def fast_approx_ln(x, n):
    n = n + 1
    g = np.sqrt(x)
    a = (1 + x)/2
    d_list = [[]]
    for i in range(0, n):
       a = (a + g)/2
       d_list[0].append(a)
       g = np.sqrt(a * g)

    for k in range(1, n):
        d_list.append([x*0 for x in range(0, n)])
        for s in range(k, n):
            d = (d_list[k-1][s] -4**(-k) * d_list[k-1][s-1]) / (1-4**(-k))
            d_list[k][s] = d
    return (x-1)/d_list[n-1][n-1]

def approx_ln(x, n):
    n = n+1
    g = np.sqrt(x)
    a = (1 + x)/2
    for i in range(0, n):
       a = (a + g)/2
       g = np.sqrt(a * g)
    return (x-1)/a

x = np.linspace(1, 2000, 2000)

#subplots
ncols=3
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=ncols, layout="constrained")
ax1[0].set_title("Approximation of ln(x) and actual ln(x)")
ax2[0].set_title("The error from above")

#uppgift 2
n = 1
for i in range(0, ncols):
    n_s = n * (i+1) *2 
    # ax1[i].set_title("Approximation of ln(x) and actual ln(x)")
    ax1[i].plot(x, np.log(x), label='ln(x)')
    ax1[i].plot(x, fast_approx_ln(x, n_s), label="approx ln(x), n=" + str(n_s), linestyle = "--")
    ax1[i].legend()
    ax1[i].set_xlabel("x")
    # ax2[i].set_title("The error from above")
    ax2[i].plot(x, abs(np.log(x) - approx_ln(x, n_s)))
    ax2[i].set_xlabel("x")

# plt.constrained_layout()
# plt.show()


#uppgift 3
ns = 20
ln_141 = np.log(1.41)
nList = np.linspace(1, ns, ns)
n2 = []
for i, x in enumerate(range(1, ns+1)):
    n2.append(abs(ln_141 - (approx_ln(1.41, x))))

ax3[0].set_title("Error of approximation (1.41)")
ax3[0].set_xlabel("n")
ax3[0].plot(nList, n2)
plt.show()

#uppgift 4
plt.figure(2)
x3 = np.linspace(0.01, 20, 50)
accel_list = []
for i in range(2, 7):
    accel_list.append([])
    for j in range(1, 51):
        accel_list[i-2].append(abs(np.log(x3[j-1])- fast_approx_ln(x3[j-1], i)))
    plt.plot(x3, accel_list[i-2], label="Iterations: " + str(i),linestyle="--", color=np.random.rand(3))
    # print(accel_list[i-2][19])

plt.legend()
plt.ylabel("Error")
plt.title("Error of accelerated version")
plt.yscale('log')

plt.show()

