# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:52:48 2023

@author: Victo
"""
from numpy import *
from matplotlib.pyplot import *

class Interval:
    def __init__(self, a, b = None):
        self.a = a
        if  b is None:
            self.b = a
        else:
            self.b = b
            
    def __repr__(self):
        return f"[{self.a}, {self.b}]"
    
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Interval(other)
        return Interval(self.a + other.a, self.b + other.b)
    
    def __radd__(self, other):
        return self + other
        
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Interval(other)
        return Interval(self.a - other.b, self.b - other.a)
    
    def __rsub__(self, other):
        return Interval(other) - self
        
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = Interval(other)
        return Interval(min([self.a*other.a, self.a*other.b, self.b*other.a, self.b*other.b]),
                        max([self.a*other.a, self.a*other.b, self.b*other.a, self.b*other.b]))
    
    def __rmul__(self, other):
        return self * other
        
    def __truediv__(self, other):
        if not isinstance(other, Interval):
            other = Interval(other);
            print("hej", other)
        if self.__contains__(0) or other.__contains__(0):
            raise ZeroDivisionError()
        else:
            return Interval(min([self.a/other.a, self.a/other.b, self.b/other.a, self.b/other.b]),
                            max([self.a/other.a, self.a/other.b, self.b/other.a, self.b/other.b]))

        # try:
        #     return Interval(min([self.a/other.a, self.a/other.b, self.b/other.a, self.b/other.b]),
        #                     max([self.a/other.a, self.a/other.b, self.b/other.a, self.b/other.b]))
        # except ZeroDivisionError:
        #     print("The dividing interval contains zero!")
        # except Exception():
        #     print("The resulting interval is infinitely large!")
    
    def __contains__(self, nbr):
        if nbr >= self.a and nbr <= self.b:
            return True
        else:
            return False
    def __neg__(self):
        return Interval(-self.a, -self.b)
    
    def __pow__(self, n):
        if n%2 == 0 and n > 0:
            if self.a >= 0:
                return Interval(self.a**n, self.b**n)
            elif self.b < 0:
                return Interval(self.b**n, self.a**n)
            else:
                return Interval(0, max([self.a**n, self.b**n]))
        else:
            return Interval(self.a**n, self.b**n)
            
        
        
# Task 1-7
I1 = Interval(1,4)

I2 = Interval(2, 1)
add = I1 + I2
sub = I1 - I2
mult = I1 * I2
div = I1 / I2 
print("Test 1:")
print(add)
print(sub)
print(mult)
print(div)
print(I1.__contains__(4))
I3 = Interval(1)
print(I3)

# Task 8
print("Test 2:")
print(Interval(2,3) + 1) # [3, 4]
print(1 + Interval(2,3)) # [3, 4]
print(1.0 + Interval(2,3)) # [3.0, 4.0]
print(Interval(2,3) + 1.0) # [3.0, 4.0]
print(1 - Interval(2,3)) # [-2, -1]
print(Interval(2,3) -1) # [1, 2]
print(1.0 - Interval(2,3)) # [-2.0, -1.0]
print(Interval(2,3) - 1.0) # [1.0, 2.0]
print(Interval(2,3) * 1) # [2, 3]
print(1 * Interval(2,3)) # [2, 3]
print(1.0 * Interval(2,3)) # [2.0, 3.0]
print(Interval(2,3) * 1.0) # [2.0, 3.0]
print(-Interval(4,5)) # see the special method __neg__

# Task 9
x = Interval(-2,2)
print(x**2)
print(x**3)

# Task 10
xl = linspace(0., 1, 1000)
xu = linspace(0., 1, 1000) + 0.5

intervalList = [Interval(a,b) for a, b in zip(xl, xu)]
pList = [3*I**3 - 2*I**2 - 5*I - 1 for I in intervalList]
yl = [I.a for I in pList]
yu = [I.b for I in pList]
plot(xl, yl)
plot(xl, yu)
title("$p(I) = 3I^3 - 2I^2 - 5I - 1, I = Interval(x,x+0.5)$")
ylabel("p(I)")
xlabel("x")

show()

