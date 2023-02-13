#!/usr/bin/python3
"""Module have one function"""


def text_indentation(text):
    """function text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for ch in text:
        if ch in ".?:":
            new_text += ch + "\n\n"
        else:
            new_text += ch
    lines = new_text.split("\n")
    for line in lines:
        if line == lines[-1]:
            print(line.strip(), end="")
        else:
            print(line.strip())
