#!/usr/bin/python3
"""Save in JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Save in json file"""
    with open(filename, "w", encoding='utf8') as json_file:
        json_file.write(json.dumps(my_obj))
