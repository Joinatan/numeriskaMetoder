import numpy as np
L=[0, 1, 2, 3, 4, 5, 6, 7]
L2= [11, 12, 13]
# L[3:4] = [L2]


    
# def f(m):
#     L = [n - m/2 for n in range(m)]
#     for e in L:
#         print(e)
#     return 1 + L[0] + L[-1]
#
# f(4)
# print(f(4)) 

distanceTable = [
        [0, 20, 30, 40],
        [20, 0, 50, 60],
        [30, 50, 0, 70],
        [40, 60, 70, 0],
        ]

reddistance = []
# i = 0
# for i, x in  enumerate(distanceTable):
#     # print(distanceTable[i][0:i])
#     if i > 0:
#         reddistance.append(distanceTable[i][0:i])
#
# print(reddistance)

reddistance = [j[0:i] for i, j in enumerate(distanceTable) if i != 0]
# print(reddistance)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = {x for x in A.union(B) if x not in A.intersection(B)}
D = A.symmetric_difference(B)
# print(C)
# print(D)

def arc(x):
    return np.arctan(x)

def f(x):
    return 3 * x**2 -5

def bisec(a, b, f, m):
    while(b - a > m):
        if (f(a) * f((a+b)/2)) < 0:
            b = (a+b)/2
        elif (f((a+b)/2)* f(b)) < 0:
            a = (a+b)/2
        else:
            print("no roots in interval")
            break
        return [(b+a)/2, a, b] 

print(bisec(-1.5, .4, f, 0.001))
 
