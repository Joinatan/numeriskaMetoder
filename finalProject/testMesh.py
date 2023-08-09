import numpy as np
import unittest
from integral import Mesh

class TestMesh(unittest.TestCase):
    def construct_mesh(self):
        coor = np.array([[0., 1., 0.], [0., 0., 1.]])
        # print(len(coor))
        elements = np.array([[1.0],[2.0],[3.0]])
        # print(elements)
        mesh = Mesh(coor, elements)
        return mesh

    def test_jacobian(self): 
        mesh = self.construct_mesh()
        result = mesh.jacobian(0)
        excpected = 1
        self.assertAlmostEqual(excpected, result)

    def test_minAngle(self):
        mesh = self.construct_mesh()
        result = mesh.minAngle(0)
        excpected = np.pi/4
        self.assertAlmostEqual(excpected, result)
        # print(angle)
    def test_plotTriangles(self):
        mesh = self.construct_mesh()
        mesh.plotTriangles()

    def test_degenereteTriangle(self):
        coor = np.array([[0, 1, -1], 
                        [0, 0, 0]])
        elements = np.array([[1],[1],[1]])
        mesh = Mesh(coor, elements)



if __name__=='__main__':
    unittest.main()
