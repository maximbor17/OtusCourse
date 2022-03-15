import math
from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError






#square = Square(5)
#rectangle = Rectangle(4,6)
#triangle = Triangle(3,2,3)
#circle = Circle(6)
#square.get_name()
#print(square.area())
#print(square.perimeter())
#print(triangle.perimeter())
#print(triangle.area())
#print(rectangle.perimeter())
#print(rectangle.area())
#print(circle.area())
#print(circle.perimeter())
#print(square.add_area(triangle))
#print(circle.add_area(square))
