import numpy as np
from matplotlib import pyplot as plt

class Interval:
    def __init__(self, lpoint, rpoint = None):
        self.lpoint = lpoint
        if not rpoint:
            self.rpoint = lpoint
        else:
            self.rpoint = rpoint

    def __contains__(self, number):
        if number > self.lpoint and number < self.rpoint:
            return True
        else:
            return False

    def __str__(self,):
        return f'[{self.lpoint}, {self.rpoint}]'

    def __add__(a, other):
        if isinstance(other, Interval):
            return (a.lpoint + other.lpoint, a.rpoint + other.rpoint)
        elif isinstance(other, float) or isinstance(other, int):
            return (a.lpoint + other, a.rpoint + other)

    def __radd__(a, other):
        return a + other 

    def __sub__(a, other):
        if isinstance(other, Interval):
            return (a.lpoint - other.rpoint, a.rpoint - other.lpoint)
        elif isinstance(other, float) or isinstance(other, int):
            return (a.lpoint - other, a.rpoint - other)

    def __rsub__(a, other):
        return a - other

    def __mul__(a, other):
        if isinstance(other, Interval):
            return (min(
                a.rpoint * other.rpoint,     
                a.rpoint * other.lpoint,
                a.lpoint * other.rpoint,     
                a.lpoint * other.lpoint
                ), max(
                a.rpoint * other.rpoint,     
                a.rpoint * other.lpoint,
                a.lpoint * other.rpoint,     
                a.lpoint * other.lpoint
                ))
        elif isinstance(other, float) or isinstance(other, int):
            return (a.lpoint * other, a.rpoint * other)
    def __rmul__(a, other):
        return a * other

    def __truediv__(a, b):
        if b.rpoint and b.lpoint != 0:
            return (min(
                a.rpoint / b.rpoint,     
                a.rpoint / b.lpoint,
                a.lpoint / b.rpoint,     
                a.lpoint / b.lpoint
                ), max(
                a.rpoint / b.rpoint,     
                a.rpoint / b.lpoint,
                a.lpoint / b.rpoint,     
                a.lpoint / b.lpoint
                    ))
        else:
            raise Exception("zero zero")

    def __neg__(self):
        return (self.rpoint * -1, self.lpoint * -1)

    def __pow__(self, other):
        if other % 2 == 1:
            return (self.lpoint**other, self.rpoint**other)
        else:
            return "hej"


A = Interval(2, 2)
B = Interval(-2, -1)
C = Interval(4)

print(A**5)

# print(A+B)
# print(A-B)
# print(A*B)
# print(A/B)
#
# print(A)
# print(A.__contains__(9))
