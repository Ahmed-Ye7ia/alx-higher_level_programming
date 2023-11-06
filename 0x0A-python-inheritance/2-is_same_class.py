#!/usr/bin/python3
'''Module for check if object is instance of the specified class.'''


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of a class.
    """
    return type(obj) == a_class
