#!/usr/bin/python3
"""read file """

def read_file(filename=""):
    """ read file """

    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read())
