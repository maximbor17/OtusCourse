import pytest
from src.Triangle import Triangle
from src.Square import Square

def test_name():
    triangle = Triangle(5,3,6)
    assert triangle.name == 'Triangle'

triangle_area = [(5,3,6,7.483314773547883)]
@pytest.mark.parametrize('side1, side2, side3, area', triangle_area)
def test_area(side1, side2, side3, area):
    triangle = Triangle(side1, side2, side3)
    triangle.area == area

triangle_perimeter = [(5,3,6,14)]
@pytest.mark.parametrize('side1, side2, side3, perimeter', triangle_perimeter)
def test_perimeter(side1, side2, side3, perimeter):
    triangle = Triangle(side1, side2, side3)
    triangle.perimeter == perimeter

def test_add_area():
    triangle = Triangle(5,3,6)
    square = Square(4)
    assert triangle.add_area(square) == 23.483314773547883