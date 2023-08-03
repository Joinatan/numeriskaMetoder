import numpy as np
from numpy.linalg import norm
#task 1
def symmetricMatrix(matrix):
    if np.array_equal(matrix, np.array(matrix).transpose()):
        return 1
    else:
        return -1

# i = np.identity(3)
# i[0, 2] = 3
# print(i)

# print(symmetricMatrix(i))

# task 2
def testOrthogonality(v1, v2):
    '''
    test if two vectors are orthogonal
    returns true if they are, else false
    '''
    if np.allclose(np.dot(v1, v2), 0):
        return True
    else:
        return False

v1 = np.array([0, 0, 3]) 
v2 = np.array([0, 3, 0]) 

# print(testOrthogonality(v1, v2))

# task 3
def computeNorm(v):
    sum = 0
    for item in v:
        sum += item**2
    return v/np.sqrt(sum)

def computeNorm2(v):
    return v/norm(v)

v3 = np.array([1, 1, 1])
# print(computeNorm(v3))

# task 4
theta = 4
A = np.array([[np.cos(theta), np.sin(theta)],
              [-np.sin(theta), np.cos(theta)]
               ])
# print(A)
B = A.transpose(1,0).copy()
print(A)
print(B)

print(A @ B)


#todo eigenvalues
