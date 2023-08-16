import matplotlib.pyplot as plt
import numpy as np

class Mesh:
    '''
    Class for representing a mesh.
    First argument is coordinates and second is triangle elements
    '''
    triangles = []
    jacobianList = []

    def __init__(self, coordinates, elements):
        self.coordinates = coordinates
        self.elements = elements
        # print(self.coordinates)
        # print(self.elements)
        self.__determinant()
        self.__createTriangle()

    def __determinant(self):
        # print(len(self.coordinates[0]))
        for i in range(len(self.elements[0])):
            if np.isclose(self.minAngle(i), 0.0):
                raise ValueError("Too small angle") 
            self.jacobianList.append(self.computeJacobian(i))
        

    def computeJacobian(self, elementIndex):
        upperL = self.coordinates[0][int(self.elements[1][elementIndex])-1] - self.coordinates[0][int(self.elements[0][elementIndex])-1]
        upperR = self.coordinates[0][int(self.elements[2][elementIndex])-1] - self.coordinates[0][int(self.elements[0][elementIndex])-1]

        lowerL = self.coordinates[1][int(self.elements[1][elementIndex])-1] - self.coordinates[1][int(self.elements[0][elementIndex])-1]
        lowerR = self.coordinates[1][int(self.elements[2][elementIndex])-1] - self.coordinates[1][int(self.elements[0][elementIndex])-1]
        matrix = np.array([[upperL, upperR],
                  [lowerL, lowerR]])
        return np.abs(np.linalg.det(matrix))

    def minAngle(self, elementIndex):
        #create x.s and y.s
        # print(self.coordinates[0][int(self.elements[1][elementIndex])-1])
        pointA = np.array([self.coordinates[0][int(self.elements[0][elementIndex])-1], self.coordinates[1][int(self.elements[0][elementIndex])-1]])
        pointB = np.array([self.coordinates[0][int(self.elements[1][elementIndex])-1], self.coordinates[1][int(self.elements[1][elementIndex])-1]])
        pointC = np.array([self.coordinates[0][int(self.elements[2][elementIndex])-1], self.coordinates[1][int(self.elements[2][elementIndex])-1]])

        # print("A: ", pointA)
        # print("B: ", pointB)
        # print("C: ", pointC)
        #first angle
        edgeAB = pointB - pointA
        edgeAB = edgeAB / np.linalg.norm(edgeAB)
        edgeAC = pointC - pointA
        edgeAC = edgeAC / np.linalg.norm(edgeAC)
        angleA = np.arccos(np.clip((np.dot(edgeAB, edgeAC)), -1, 1))

        #second angle
        edgeBC = pointC - pointB
        edgeBC = edgeBC / np.linalg.norm(edgeBC)
        edgeBA = pointA - pointB
        edgeBA = edgeBA / np.linalg.norm(edgeBA)
        angleB = np.arccos(np.clip((edgeBA @ edgeBC), -1, 1))

        #third angle
        edgeCA = pointA - pointC
        # print("normie: ", np.linalg.norm(edgeCA))
        edgeCA = edgeCA / np.linalg.norm(edgeCA)
        edgeCB = pointB - pointC
        edgeCB = edgeCB / np.linalg.norm(edgeCB)
        angleC = np.arccos(np.clip((edgeCA @ edgeCB), -1, 1))

        return min(angleA, angleB, angleC)

    def calulateCenter(self, index):
        centerX = (1/3) * (self.triangles[index][0][0] + self.triangles[index][1][0] + self.triangles[index][2][0])
        centerY = (1/3) * (self.triangles[index][0][1] + self.triangles[index][1][1] + self.triangles[index][2][1])
        return np.array([centerX, centerY])

    def scaleTriangle(self, index, scaleFactor):
        center = self.calulateCenter(index)
        newTriangle = np.array([[0., 0.],[0., 0.],[0., 0.]])
        for i in range(len(self.triangles[index])):
            newTriangle[i][0] = ((self.triangles[index][i][0] - center[0]) * scaleFactor) + center[0]
            newTriangle[i][1] = ((self.triangles[index][i][1] - center[1]) * scaleFactor) + center[1]
        return newTriangle


    def plotTriangles(self, scaleFactor = 1):
        # plt.fill(self.coordinates[0])
        colors = ('red', 'purple', 'black', 'pink', 'blue', 'orange')
        randNr = 0
        for i in range(len(self.triangles)):
            #scale triangle
            newTriangle = self.scaleTriangle(i, scaleFactor)

            #random number for color
            randNr = np.random.randint(0, len(colors))
            # plt.fill(np.hsplit(self.triangles[i],2)[0], np.hsplit(self.triangles[i],2)[1], facecolor='none', edgecolor=colors[randNr], linewidth=1, sketch_params=0.2)
            plt.fill(np.hsplit(newTriangle,2)[0], np.hsplit(newTriangle,2)[1], facecolor='none', edgecolor=colors[randNr], linewidth=1, sketch_params=0.2)
        plt.show()

    def __createTriangle(self):
        '''
        Stores each triangle in a matrix [[x1, y1],
                                            [x2, y2]]
        '''
        # self.triangles = [len(self.coordinates[0])]
        # print("elements: ", self.elements[0])
        for i, item in enumerate(self.elements[0]):
            self.triangles.append(np.array([
                    [self.coordinates[0][int(self.elements[0][i])-1], self.coordinates[1][int(self.elements[0][i])-1]],
                    [self.coordinates[0][int(self.elements[1][i])-1], self.coordinates[1][int(self.elements[1][i])-1]],
                    [self.coordinates[0][int(self.elements[2][i])-1], self.coordinates[1][int(self.elements[2][i])-1]]
                    ]))

    def transForm(self, f, index):
        x_1 = self.triangles[index][0][0]
        x_2 = self.triangles[index][1][0]
        x_3 = self.triangles[index][2][0]
        y_1 = self.triangles[index][0][1]
        y_2 = self.triangles[index][1][1]
        y_3 = self.triangles[index][2][1]
        # print("x_1: ", x_1)
        # print("y_1: ", y_1)
        # print("x_2: ", x_2)
        # print("y_2: ", y_2)
        # print("x_3: ", x_3)
        # print("y_3: ", y_3)
        # print("x, y ->", x_3, y_3)
        def tranfsformedFunc(e, n):
            x_e = x_1 +(x_2 - x_1)*e + (x_3 - x_1)*n
            y_n = y_1 +(y_2 - y_1)*e + (y_3 - y_1)*n
            # print("X_e: ", x_e)
            # print("Y_e: ", y_n)
            result = f(x_e, y_n)
            return result
        return tranfsformedFunc

    def approximanteIntegral(self, f):
        sum = 0.
        for index in range(len(self.elements[0])):
            transformedF = self.transForm(f, index)
            # print("0,0: " ,transformedF(0,0))
            # print("0,1: ", transformedF(1,0))
            # print("1,0: ", transformedF(0,1))
            approxIntegral = (1/2) * self.jacobianList[index] * ((1/3) * transformedF(0., 0.) + (1/3) * transformedF(0., 1.) + (1/3) * transformedF(1., 0.))
            sum += approxIntegral
            # print("JACOB: ", self.jacobianList[index])
            # print("APPROX: ", approxIntegral)
            # print("SUM: ", sum)

        return sum

    def triangleArea(self, index):
        matrix = np.append(self.triangles[index],[[1.],[1.],[1.]], 1)
        area = 0.5  * np.linalg.det(matrix)
        return np.abs(area)

    def totalArea(self):
        sum = 0
        for i in range(len(self.elements[0])):
            sum += self.triangleArea(i)
        return sum


    #     pass
    # class Triangle:
    #     def __init__(self, coordinates, elements):
    #         self.coordinates = coordinates
    #         self.elements = elements





#import file
coord_datas = np.genfromtxt("./data/coordinates_unitcircle_1024.txt")
elementss = np.genfromtxt("./data/nodes_unitcircle_1024.txt")
# print(coord_data)

arr = np.array([[0, 0], [1, 0], [0, 1]
                ])
# print(arr)

coor = np.array([[0., 1., 0.], 
                 [0., 0., 1.]])
# print(coor)

mesh = Mesh(coord_datas, elementss)
# print(mesh.totalArea())
# print(mesh.minAngle(0))
# mesh.plotTriangles(0.8)
def func(x, y):
    return 1

print(mesh.approximanteIntegral(func))
print(mesh.totalArea())

# print(np.hsplit(arr, 2))
# plt.fill(np.hsplit(arr,2)[0], np.hsplit(arr,2)[1])
# plt.show()




