from src.main import Figure
from src.Square import Square
import math

class Circle(Figure):
    def __init__(self,r):
        self.radius=r

    @property
    def area(self):
        #self.area=math.pi*self.radius
        return math.pi*self.radius

    @property
    def perimeter(self):
        #self.perimeter=2*math.pi*self.radius
        return 2*math.pi*self.radius

    #def add_area(self, figure):
     #   self.area=self.area+figure.area()
      #  return self.area

    name = "Circle"

circle = Circle(2)
#print(circle.perimeter())
#print(circle.add_area(square))