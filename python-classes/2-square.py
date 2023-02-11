#!/usr/bin/python3
"""Fist Document"""


class Square:
    """Fist method"""
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError ("size must be >= 0")
            elif not isinstance(size, int):
                raise TypeError ("size must be an integer")
        except:
            pass
