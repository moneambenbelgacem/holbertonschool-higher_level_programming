#!/usr/bin/python3
"""Fist Document"""


class Square:
    """Fist method"""

    def __init__(self, size=0, position=(0, 0)):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

            """add position"""
            if not isinstance(position, tuple) or len(position) != 2:
                raise TypeError("position must be a tuple \
                    of 2 positive integers")
            if not all(isinstance(i, int) and i >= 0 for i in position):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = position

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                print("#"*self.__size)
        else:
            print()

    def my_print(self):
        if not self.__size == 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()

    @property
    def position(self):
       return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    
