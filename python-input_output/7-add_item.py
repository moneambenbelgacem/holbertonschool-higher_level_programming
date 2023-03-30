#!/usr/bin/python3
"""Management system in json file"""

from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    if not path.exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    data = load_from_json_file("add_item.json")
    if len(argv) != 1:
        for i in range(1, len(argv)):
            data.append(argv[i])

    save_to_json_file(data, "add_item.json")
