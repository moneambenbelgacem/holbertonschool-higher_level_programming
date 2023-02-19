#!/usr/bin/python3
"""Module class rectangle"""


def inherits_from(obj, a_class):
    """instance or subclass"""
    return isinstance(obj, type) and issubclass(obj, a_class)
