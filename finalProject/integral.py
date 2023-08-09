import matplotlib.pyplot as plt
import numpy as np

class Mesh:
    '''
    Class for representing a mesh.
    First argument is coordinates and second is triangle elements
    '''
    triangles = []

    def __init__(self, coordinates, elements):
        self.coordinates = coordinates
        self.elements = elements
        self._createTriangle()

    def jacobian(self, elementIndex):
        upperR = self.coordinates[0][self.elements[1][elementIndex]] - self.coordinates[0][self.elements[0][elementIndex]]
        upperL = self.coordinates[0][self.elements[2][elementIndex]] - self.coordinates[0][self.elements[0][elementIndex]]

        lowerL = self.coordinates[1][self.elements[1][elementIndex]] - self.coordinates[1][self.elements[0][elementIndex]]
        lowerR = self.coordinates[1][self.elements[2][elementIndex]] - self.coordinates[1][self.elements[0][elementIndex]]
        matrix = np.array([[upperR, upperL],
                  [lowerL, lowerR]])
        return np.linalg.det(matrix)

    def minAngle(self, elementIndex):
        #create x.s and y.s
        pointA = np.array((self.coordinates[0][int(self.elements[0][elementIndex])], self.coordinates[1][int(self.elements[0][elementIndex])]))
        pointB = np.array((self.coordinates[0][int(self.elements[1][elementIndex])], self.coordinates[1][int(self.elements[1][elementIndex])]))
        pointC = np.array((self.coordinates[0][int(self.elements[2][elementIndex])], self.coordinates[1][int(self.elements[2][elementIndex])]))

        #first angle
        edgeAB = pointB - pointA
        edgeAB = edgeAB / np.linalg.norm(edgeAB)
        edgeAC = pointC - pointA
        edgeAC = edgeAC / np.linalg.norm(edgeAC)
        angleA = np.arccos(np.clip((edgeAB @ edgeAC), -1, 1))

        #second angle
        edgeBC = pointC - pointB
        edgeBC = edgeBC / np.linalg.norm(edgeBC)
        edgeBA = pointA - pointB
        edgeBA = edgeBA / np.linalg.norm(edgeBA)
        angleB = np.arccos(np.clip((edgeBA @ edgeBC), -1, 1))

        #third angle
        edgeCA = pointA - pointC
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

    def _createTriangle(self):
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

mesh = Mesh(coord_data, elements)
print(mesh.minAngle(0))
mesh.plotTriangles()

# print(np.hsplit(arr, 2))
# plt.fill(np.hsplit(arr,2)[0], np.hsplit(arr,2)[1])
# plt.show()




