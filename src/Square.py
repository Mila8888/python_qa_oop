from src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side_square):
        self.__side_square = side_square
        if not isinstance(side_square, (float, int)):
            raise TypeError("стороны квадрата должны быть типа float или int")
        elif side_square <= 0:
            raise AssertionError("значение должно быть больше 0")

    @property
    def get_area(self): return self.__side_square ** 2

    @property
    def get_perimeter(self): return self.__side_square * 4
