#!/usr/bin/python3
"""Get Obj from json file"""
import json


def load_from_json_file(filename):
    """Get Obj from json file function"""
    with open(filename) as json_file:
        return json.load(json_file)
