import pytest
from src.Rectangle import Rectangle
from src.Triangle import Triangle

def test_name():
    rectangle = Rectangle(4,5)
    assert rectangle.name == 'Rectangle'

rect_area = [(4,5,20)]
@pytest.mark.parametrize('side1, side2, area', rect_area)
def test_area(side1,side2,area):
    rectangle = Rectangle(side1,side2)
    assert rectangle.area == area

rect_perimeter = [(5,10,30)]
@pytest.mark.parametrize('side1, side2, perimeter', rect_perimeter)
def test_perimeter(side1,side2,perimeter):
    rectangle = Rectangle(side1,side2)
    assert rectangle.perimeter == perimeter

def test_add_area():
    rectangle = Rectangle(2,7)
    triangle = Triangle(5,3,6)
    assert rectangle.add_area(triangle) == 21.483314773547883