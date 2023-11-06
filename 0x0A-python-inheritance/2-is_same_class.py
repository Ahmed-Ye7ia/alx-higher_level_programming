#!/usr/bin/python3
"""
contain method thatreturns True if 
object is exactly an instance of specified class.
"""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of a class.
    """
    return type(obj) == a_class
