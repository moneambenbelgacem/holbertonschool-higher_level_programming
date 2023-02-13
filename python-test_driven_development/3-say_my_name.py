#!/usr/bin/python3
"""Module have one function"""


def say_my_name(first_name, last_name=""):
    """function say my name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")