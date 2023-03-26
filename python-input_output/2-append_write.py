#!/usr/bin/python3
"""Task 0"""


def append_write(filename="", text=""):
    """function to write file using with"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
