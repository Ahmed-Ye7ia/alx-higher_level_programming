#!/usr/bin/python3
"""
a script that adds all arguments to a Python list
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

old_content = load_from_json_file('add_item.json')

old_content.extend(arglist)
save_to_json_file(arglist, 'add_item.json')
