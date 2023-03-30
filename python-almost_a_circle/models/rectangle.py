#!/usr/bin/python3
"""Create class Rectangle"""
from models.base import Base


class Rectangle (Base):
    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not width > 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not height > 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not x >= 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if not y >= 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self) -> int:
        """get width"""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self) -> int:
        """get height"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self) -> int:
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if not value >= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self) -> int:
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if not value >= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get area of this rectangle"""
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the Rectangle instance """
        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(" "*self.__x + "#"*self.__width)

    def __str__(self) -> str:
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Update elements"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Make class ti dictionary"""
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
