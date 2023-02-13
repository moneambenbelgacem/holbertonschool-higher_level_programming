#!/usr/bin/python3
"""Module have one function"""


def add_integer(a, b=98):
    """add two integer"""
    if not(isinstance(a, int) or isinstance (a, float)):
        raise TypeError ("a must be an integer")
    elif not(isinstance(b, float) or isinstance (b, int)):
        raise TypeError ("a must be an integer")
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b) 
    return a + b
