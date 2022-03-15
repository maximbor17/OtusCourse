from src.main import Figure
import math

class Triangle(Figure):

    def __init__(self,s1,s2,s3):
        self.side1=s1
        self.side2=s2
        self.side3=s3

    def figure(self):
        self.figure1=Triangle(Figure)

    @property
    def area(self):
        if (self.side1 + self.side2) > self.side3 and (self.side2 + self.side3) > self.side1 and (
                self.side3 + self.side1) > self.side2:
            p2 = (self.side3+self.side2+self.side1)/2
            return math.sqrt(p2*(p2-self.side1)*(p2-self.side2)*(p2-self.side3))
        else:
            return None

    @property
    def perimeter(self):
        if (self.side1+self.side2)>self.side3 and (self.side2+self.side3)>self.side1 and (self.side3+self.side1)>self.side2:
            return self.side3+self.side2+self.side1
        else:
            return None

    #def add_area(self, figure):
     #   self.area=self.area+figure.area()
      #  return self.area

    name = 'Triangle'



