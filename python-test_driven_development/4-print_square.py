#!/usr/bin/python3
"""Module have one function"""


def print_square(size):
    """the size for square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#"*size)