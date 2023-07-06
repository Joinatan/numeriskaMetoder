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
        if number >= self.lpoint and number <= self.rpoint:
            return True
        else:
            return False

    def __str__(self,):
        return f'[{self.lpoint}, {self.rpoint}]'

    def __add__(a, other):
        if isinstance(other, Interval):
            return Interval(a.lpoint + other.lpoint, a.rpoint + other.rpoint)
        elif isinstance(other, float) or isinstance(other, int):
            return Interval(a.lpoint + other, a.rpoint + other)

    def __radd__(a, other):
        return Interval(a + other)

    def __sub__(a, other):
        if isinstance(other, Interval):
            return Interval(a.lpoint - other.rpoint, a.rpoint - other.lpoint)
        elif isinstance(other, float) or isinstance(other, int):
            return Interval(a.lpoint - other, a.rpoint - other)

    def __rsub__(a, other):
        return Interval(a - other)

    def __mul__(a, other):
        if isinstance(other, Interval):
            return Interval(min(
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
            return Interval(min(a.lpoint * other, a.rpoint * other), max(a.lpoint * other, a.rpoint * other))
    def __rmul__(self, other):
        return Interval(self.lpoint, self.rpoint) * other

    def __truediv__(a, b):
        if b.rpoint and b.lpoint != 0:
            return Interval(min(
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
        return Interval(self.rpoint * -1, self.lpoint * -1)

    def __pow__(self, exponent):
        if exponent % 2 == 1:
            return Interval(self.lpoint**exponent, self.rpoint**exponent)
        elif self.lpoint >= 0:
            return Interval(self.lpoint**exponent, self.rpoint**exponent)
        elif self.rpoint < 0:
            return Interval(self.rpoint**exponent, self.lpoint**exponent)
        else:
            return Interval(0, max(self.lpoint**exponent, self.rpoint**exponent))



A = Interval(2, 4)
B = Interval(-2, -1)
C = Interval(4)

xl = np.linspace(0., 1, 1000)
xu = np.linspace(0., 1, 1000)+0.5
intervalList = []

for i, l in enumerate(xl):
    interval = Interval(xl[i], xu[i])
    intervalList.append(interval)

polynomialList = []
for i, interval in enumerate(intervalList):
    polynomialList.append(3*intervalList[i]**3 - 2*intervalList[i]**2 - 5 * intervalList[i] - 1)


lowerBounds = []
upperBounds = []
for i, x in enumerate(polynomialList):
    lowerBounds.append(polynomialList[i].lpoint)
    upperBounds.append(polynomialList[i].rpoint)


plt.title(r'$p(I) = 3I^{3} - 2I^2 - 5I - 1$')
plt.ylabel('p(I')
plt.plot(xl, upperBounds, label='Upper bounds')
plt.plot(xl, lowerBounds, label='Lower bounds')
plt.legend()
plt.show()

