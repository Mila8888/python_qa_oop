import pytest

from src.Square import *
from src.Triangle import *


def test_create_area_triangle(default_triangle):
    """Определить площадь треугольника"""
    assert default_triangle.get_area == 84


def test_create_area_perimeter(default_triangle):
    """Определить периметр треугольника"""
    assert default_triangle.get_perimeter == 42


def test_existence_triangle():
    """Определить существование треугольника по трем сторонам"""
    with pytest.raises(ValueError):
        Triangle(side_a=1, side_b=2, side_c=3)


def test_check_sides_triangle_type_error():
    """Проверка сторон треугольника на подходящий тип"""
    with pytest.raises(TypeError):
        Triangle(side_a="side", side_b=3, side_c=5)


def test_check_negative_sides_triangle():
    """Проверка на отрицательные значения сторон треугольника"""
    with pytest.raises(AssertionError):
        Triangle(side_a=-1, side_b=3, side_c=2)


def test_create_area_square(default_square):
    """Определить площадь кватрада"""
    assert default_square.get_area == 100


def test_create_perimeter_square(default_square):
    """Определить периметра кватрада"""
    assert default_square.get_perimeter == 40


def test_check_sides_square_type_error():
    """Проверка сторон квадрата на подходящий тип"""
    with pytest.raises(TypeError):
        Square(side_square="side")


def test_check_negative_sides_square():
    """Проверка на отрицательные значения сторон квадрата"""
    with pytest.raises(AssertionError):
        Square(side_square=-5)


def test_create_area_circle(default_circle):
    """Определить площадь круга"""
    assert default_circle.get_area == 314


def test_create_perimeter_circle(default_circle):
    """Определить периметр круга"""
    assert default_circle.get_perimeter == 63


def test_create_area_rectangle(default_rectangle):
    """Определить площадь прямоугольника"""
    assert default_rectangle.get_area == 8


def test_create_perimeter_rectangle(default_rectangle):
    """Определить периметр прямоугольника"""
    assert default_rectangle.get_perimeter == 12


def test_create_area_triangle(default_triangle, default_square):
    """Сумма площадей треугольника и квадрата"""
    assert default_triangle.add_area(default_square) == 184
