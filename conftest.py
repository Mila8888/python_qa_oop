import pytest

from src.Circle import *
from src.Square import *
from src.Triangle import *
from src.Rectangle import *


@pytest.fixture
def default_square():
    return Square(side_square=10)


@pytest.fixture
def default_triangle():
    return Triangle(side_a=13, side_b=14, side_c=15)


@pytest.fixture
def default_circle():
    return Circle(radius=10)


@pytest.fixture
def default_rectangle():
    return Rectangle(side_a=2, side_b=4)
