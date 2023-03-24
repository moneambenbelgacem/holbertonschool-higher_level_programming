#!/usr/bin/python3
"""read file """


def read_file(filename=""):
    """ read file """

    with open(filename, mode='r') as f:
        for line in f.readlines():
            print(line, end="")
