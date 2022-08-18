import math

import pytest

from src.Figure import Figure


class Circle(Figure):
    name = "Circle"

    def __init__(self, radius):
        self.__radius = radius

    @property
    def get_area(self): return round(math.pi * (self.__radius ** 2))

    @property
    def get_perimeter(self):
        circle = round(2 * math.pi * self.__radius)
        return circle
