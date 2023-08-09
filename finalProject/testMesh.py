import numpy as np
import unittest
from integral import Mesh

class TestMesh(unittest.TestCase):
    def construct_mesh(self):
        coor = np.array([[0, 1, 0], 
                        [0, 0, 1]])
        elements = np.array([[1],[1],[1]])
        mesh = Mesh(coor, elements)
        return mesh

    def test_jacobian(self): 
        mesh = self.construct_mesh()
        result = mesh.jacobian(0)
        excpected = 0
        self.assertAlmostEqual(excpected, result)

    def test_minAngle(self):
        mesh = self.construct_mesh()
        result = mesh.minAngle(0)
        excpected = np.pi/4
        # print(result)
        # self.assertAlmostEqual(excpected, result)
        # print(angle)
    def test_plotTriangles(self):
        mesh = self.construct_mesh()
        mesh.plotTriangles()


if __name__=='__main__':
    unittest.main()
