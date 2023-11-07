#!/usr/bin/python3
"""
Contains class Student that defines a student by
"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            my_dict = dict()
            for att in attrs:
                if att in self.__dict__.keys():
                    my_dict[att] = self.__dict__[att]
            return my_dict

    def reload_from_json(self, json):
        for key,value in json.items():
            setattr(self, key, value)
