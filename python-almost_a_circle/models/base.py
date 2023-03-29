#!/usr/bin/python3
"""almost a cercle"""
import json
from os import path
import csv


class Base:
    """ base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
