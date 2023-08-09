import matplotlib.pyplot as plt
import numpy as np
from abc import ABC, abstractmethod

class PolyGon(ABC):
    @abstractmethod
    def __init__(self, *corners):
        self.corners = np.array(corners)
        # self.edges = 

    @abstractmethod
    def print(self):
        x = [a for a, b in self.corners]
        y = [b for a, b in self.corners]
        plt.fill(x, y)
        plt.show()
        # print(self.corners[1])
        

# arr = np.array([1, 1])

class Rectangle(PolyGon):
    def __init__(self, *corners):
        self.corners = np.array(corners)

    def print(self):
        x = [a for a, b in self.corners]
        y = [b for a, b in self.corners]
        plt.fill(x, y)
        plt.show()

    def area(self):
        height = self.corners[-1] - self.corners[0]
        height = np.sqrt(height[0]**2 + height[1]**2)
        length = self.corners[1] - self.corners[0]
        length = np.sqrt(length[0]**2 + length[1]**2)
        return height * length

# poly = PolyGon([1,0], [2,0], [5,6])
# poly.print()

rect = Rectangle([1,1], [3,1], [3,2], [1, 2])
# rect.print()
print(rect.area())
