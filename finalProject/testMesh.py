import numpy as np
import unittest
from integral import Mesh
from scipy import integrate as integrate

class TestMesh(unittest.TestCase):
    def construct_mesh(self):
        coor = np.array([[0., 1., 0., 1.0], 
                         [0., 0., 1., 1.0]])
        elements = np.array([[1.0, 2.0],
                             [2.0, 3.0],
                             [3.0, 4.0]])
        mesh = Mesh(coor, elements)
        return mesh

    def test_computeJacobian(self): 
        mesh = self.construct_mesh()
        result = mesh.computeJacobian(0)
        excpected = 1.0
        self.assertAlmostEqual(excpected, result)

    def test_minAngle(self):
        mesh = self.construct_mesh()
        result = mesh.minAngle(0)
        excpected = np.pi/4.
        self.assertAlmostEqual(excpected, result)
        # print(angle)
    def test_plotTriangles(self):
        mesh = self.construct_mesh()
        mesh.plotTriangles()

    def test_degenereteTriangle(self):
        coor = np.array([[0., 1., -1.], 
                        [0., 0., 0.]])
        elements = np.array([[1.],[2.],[3.]])
        self.assertRaises(ValueError, Mesh, *(coor, elements))

    def test_triangleArea(self):
        coor = np.array([[0., 1., 0., 1.0], [0., 0., 1., 1.0]])
        elements = np.array([[1.0, 2.0],[2.0, 3.0],[3.0, 4.0]])
        mesh = Mesh(coor, elements)
        excpected = 0.5
        result = mesh.triangleArea(0)
        # self.assertAlmostEqual(excpected, result)

    def test_totalArea(self):
        mesh = self.construct_mesh()
        result = mesh.totalArea()
        excpected = 1
        # self.assertAlmostEqual(excpected, result)

    def test_approximateIntegral(self):
        mesh = self.construct_mesh()
        def f(y, x):
            return 1. - x**2 -y**2
        result = mesh.approximanteIntegral(f)
        excpected, err = integrate.dblquad(f, 0., 1., 0., 1.)
        print("EX: ", excpected)
        print("RES: ", result)
        self.assertAlmostEqual(excpected, result)


        pass



if __name__=='__main__':
    unittest.main()
