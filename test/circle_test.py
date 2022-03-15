import pytest
from src.Circle import Circle
from src.Square import Square

def test_name():
    circle=Circle(2)
    assert circle.name == 'Circle'

circle_area = [(0,0),(2,6.283185307179586)]

@pytest.mark.parametrize('radius,area', circle_area)
def test_area(radius,area):
    circle=Circle(radius)
    assert circle.area == area

circle_perimeter = [(0,0),(2,12.566370614359172)]

@pytest.mark.parametrize('radius,perimeter', circle_perimeter)
def test_perim(radius,perimeter):
    circle=Circle(radius)
    assert circle.perimeter == perimeter

def test_add_area():
    circle = Circle(2)
    square = Square(5)
    assert circle.add_area(square) == 31.283185307179586