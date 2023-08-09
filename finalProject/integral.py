import matplotlib.pyplot as plt
import numpy as np

class Mesh:
    '''
    Class for representing a mesh.
    First argument is coordinates and second is triangle elements
    '''
    triangles = []
    jacobians = []

    def __init__(self, coordinates, elements):
        self.coordinates = coordinates
        self.elements = elements
        # print(self.coordinates)
        # print(self.elements)
        self.__createTriangle()
        # self.__determinant()

    def __determinant(self):
        for i in range(len(self.coordinates[0])):
            # if np.isclose(self.minAngle(i), 0.0):
            #     raise Exception("Too small angle") 
            self.jacobians.append(self.jacobian(i))
        

    def jacobian(self, elementIndex):
        upperL = self.coordinates[0][int(self.elements[1][elementIndex])-1] - self.coordinates[0][int(self.elements[0][elementIndex])-1]
        upperR = self.coordinates[0][int(self.elements[2][elementIndex])-1] - self.coordinates[0][int(self.elements[0][elementIndex])-1]

        lowerL = self.coordinates[1][int(self.elements[1][elementIndex])-1] - self.coordinates[1][int(self.elements[0][elementIndex])-1]
        lowerR = self.coordinates[1][int(self.elements[2][elementIndex])-1] - self.coordinates[1][int(self.elements[0][elementIndex])-1]
        matrix = np.array([[upperL, upperR],
                  [lowerL, lowerR]])
        return np.linalg.det(matrix)

    def minAngle(self, elementIndex):
        #create x.s and y.s
        # print(self.coordinates[0][int(self.elements[1][elementIndex])-1])
        pointA = np.array([self.coordinates[0][int(self.elements[0][elementIndex])-1], self.coordinates[1][int(self.elements[0][elementIndex])-1]])
        pointB = np.array([self.coordinates[0][int(self.elements[1][elementIndex])-1], self.coordinates[1][int(self.elements[1][elementIndex])-1]])
        pointC = np.array([self.coordinates[0][int(self.elements[2][elementIndex])-1], self.coordinates[1][int(self.elements[2][elementIndex])-1]])

        print("A: ", pointA)
        print("B: ", pointB)
        print("C: ", pointC)
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
    def plotTriangles(self):
        # plt.fill(self.coordinates[0])
        for i in range(len(self.triangles)):
            plt.fill(np.hsplit(self.triangles[i],2)[0], np.hsplit(self.triangles[i],2)[1])
            # plt.fill(self.triangles[i])
        plt.show()

    def __createTriangle(self):
        # self.triangles = [len(self.coordinates[0])]
        for i, item in enumerate(self.elements[0]):
            self.triangles.append(np.array([
                    [self.coordinates[0][int(self.elements[0][i])-1], self.coordinates[1][int(self.elements[0][i])-1]],
                    [self.coordinates[0][int(self.elements[1][i])-1], self.coordinates[1][int(self.elements[1][i])-1]],
                    [self.coordinates[0][int(self.elements[2][i])-1], self.coordinates[1][int(self.elements[2][i])-1]]
                    ]))
    #     pass
    # class Triangle:
    #     def __init__(self, coordinates, elements):
    #         self.coordinates = coordinates
    #         self.elements = elements





#import file
coord_data = np.genfromtxt("./data/coordinates_unitcircle_400.txt")
elements = np.genfromtxt("./data/nodes_unitcircle_400.txt")
# print(coord_data)

arr = np.array([[0, 0], [1, 0], [0, 1]
                ])
# print(arr)

coor = np.array([[0., 1., 0.], 
                 [0., 0., 1.]])
# print(coor)

# mesh = Mesh(coord_data, elements)
# print(mesh.minAngle(0))
# mesh.plotTriangles()

# print(np.hsplit(arr, 2))
# plt.fill(np.hsplit(arr,2)[0], np.hsplit(arr,2)[1])
# plt.show()




