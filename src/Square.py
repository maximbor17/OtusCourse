from src.main import Figure

class Square(Figure):
    def __init__(self, s):
        self.side=s

    @property
    def area(self):
        #self.area=self.side**2
        return self.side**2

    @property
    def perimeter(self):
        #self.perimeter=self.side*4
        return self.side*4

   # def add_area(self, figure):
        #if isinstance(Figure())
    #    self.area=self.area+figure.area()
     #   return self.area
        #else:
        #raise ValueError

    name = 'Square'

#square = Square(6)
#print(square.area())