#!/usr/bin/python3
"""Defines function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
