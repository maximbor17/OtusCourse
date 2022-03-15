import pytest
from src.Square import Square
from src.Rectangle import Rectangle

def test_name():
    square = Square(5)
    assert square.name == 'Square'

square_area = [(5,25)]

@pytest.mark.parametrize('side,area', square_area)
def test_area(side,area):
    square = Square(side)
    assert square.area == area

square_perimeter = [(7,28)]

@pytest.mark.parametrize('side,perimeter', square_perimeter)
def test_perimeter(side,perimeter):
    square = Square(side)
    assert square.perimeter == perimeter

def test_add_area():
    square = Square(5)
    rectangle = Rectangle(3,8)
    assert square.add_area(rectangle) == 49
