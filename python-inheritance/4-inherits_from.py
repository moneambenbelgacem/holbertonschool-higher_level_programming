#!/usr/bin/python3
"""Module class rectangle"""


def inherits_from(obj, a_class):
    """instance or subclass"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
