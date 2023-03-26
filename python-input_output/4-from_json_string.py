#!/usr/bin/python3
"""Task 0"""


import json


def from_json_string(my_str):
    """function to write file using with"""
    res = json.loads(my_str)
    return res
