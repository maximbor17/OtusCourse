from src.main import Figure

class Rectangle(Figure):
    def __init__(self,s1,s2):
        self.side1=s1
        self.side2=s2

    @property
    def area(self):
        #self.area=self.side1*self.side2
        return self.side1*self.side2

    @property
    def perimeter(self):
        #self.perimeter=2*(self.side1+self.side2)
        return 2*(self.side1+self.side2)

    #def add_area(self, figure):
     #   self.area=self.area+figure.area()
      #  return self.area

    name = 'Rectangle'