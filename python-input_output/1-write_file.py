#!/usr/bin/python3
"""Task 0"""


def write_file(filename="", text=""):
    """function to write file using with"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    return len(text)