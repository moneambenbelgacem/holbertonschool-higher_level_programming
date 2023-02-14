#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self) -> str:
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join("{}".format((self.print_symbol)) *
                         self.width for _ in range(self.height))

    def __repr__(self) -> str:
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self) -> None:
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        return self.__height * self.__width

    def perimeter(self) -> int:
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2) -> object:
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
