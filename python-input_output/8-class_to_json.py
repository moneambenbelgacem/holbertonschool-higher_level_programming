#!/usr/bin/python3
"""Dic of class"""


def class_to_json(obj):
    """dic of class"""
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
