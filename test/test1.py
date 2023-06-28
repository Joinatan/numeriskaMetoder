import numpy as np 
import matplotlib.pyplot as plt

#--------------------------uppgift 1
x = 0.5
a = 0.5 
found = False

for i in range(200):
    x = np.sin(x) - a * x + 30
    x2 = np.sin(x) - a * x + 30
    if abs(x2 - x) < 1.e-8:
        found = True
        break
print (f'The result after { i + 1 } iterations is { x } ')
print(found) 

#---------------------------uppgift 2
x2 = np.linspace(5, 30)

plt.plot(x2, np.sin(x2) - a * x2 + 30)
plt.plot(x2, x2)
# plt.show()

#---------------------------uppgift 3
def sinFunc(n):
    return np.sin(n)**2/n

n=1
nList = []

def appendList():
    while x > 1.e-9:
        x = sinFunc(n)
        nList.append(x)
        n+=1

print(len(nList))

#---------------------------uppgift 4
def convFunc(x, a):
    return 0.2 * x - a*(x**2 - 5)

def task4():
    q = 1
    q_old = 0
    a = 0.5
    while(abs(q - q_old) > 1.e-9):
        q_old = q
        q = convFunc(q, a)
        # if q < 0:
            # print("negative value")
    print("converged to ", q)


