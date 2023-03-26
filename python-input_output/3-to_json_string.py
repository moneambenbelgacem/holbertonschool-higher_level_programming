#!/usr/bin/python3
"""Task 0"""


import json


def to_json_string(my_obj):
    """function to write file using with"""
    res = json.dumps(my_obj)
    return res
