import pytest

from src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b
        if not isinstance(side_a or side_b, (float, int)):
            raise TypeError("стороны прямоугольника должны быть типа float или int")
        elif (side_a or side_b) <= 0:
            raise AssertionError("значение должно быть больше 0")

    @property
    def get_area(self): return self.__side_a * self.__side_b

    @property
    def get_perimeter(self):
        rectangle = 2 * (self.__side_a + self.__side_b)
        return rectangle
