import numpy as np
import cmath as cmath

class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def realPart(self):
        return np.real(self.number)

    def imagPart(self):
        return np.imag(self.number)*1j

    def rectangularForm(self):
        return self.realPart() + self.imagPart()

    def argument(self):
        return np.angle(self.number)
        # return np.arctangent(self)

    @staticmethod
    def checkEquality(n1, n2):
        if np.isclose(n1.realPart(), n2.realPart()) and cmath.isclose(n1.imagPart(), n2.imagPart()):
            return True
        else:
            return False
