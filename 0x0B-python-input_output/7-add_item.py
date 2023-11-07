#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file:
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(argv[1:])

try:
    old_content = load_from_json_file("add_item.json")
except FileNotFoundError:
    old_content = []

old_content.extend(arglist)
save_to_json_file(old_cotent, "add_item.json")
