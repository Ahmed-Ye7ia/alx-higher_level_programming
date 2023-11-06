#!/usr/bin/python3
'''Defines a function that adds attributes to objects.'''


def add_attribute(obj, attribute, value):
    '''Add a new attribute to an object if possible.'''
    if not ('__dict__' in dir(obj)):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
