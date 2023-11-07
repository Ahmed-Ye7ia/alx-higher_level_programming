#!/usr/bin/python3
"""
Contains function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """writes to text file and retunrs num chars written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
