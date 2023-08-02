from ex4 import complexFunc
import unittest
import numpy as np

class TestComplexFunc(unittest.TestCase):
    def test_one(self):
        result = complexFunc(0, 1)
        expected = 1. + 0.j
        self.assertEqual(expected, result)
    def test_j(self):
        result = complexFunc(np.pi / 2, 1)
        expected = 0. + 1.j
        self.assertAlmostqual(expected, result)

if __name__=='__main__':
    unittest.main()


