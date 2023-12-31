#!/usr/bin/python3
'''Module for check if the object is an instance of a class that inherited.'''


def inherits_from(obj, a_class):
    '''Determines if an object is a subclass of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
