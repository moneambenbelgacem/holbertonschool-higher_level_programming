#!/usr/bin/python3
"""Module class rectangle"""


class BaseGeometry:
    """base class    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
