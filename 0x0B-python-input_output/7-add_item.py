#!/usr/bin/python3
"""
a script that adds all arguments to a Python list
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    old_content = load_from_json_file('add_item.json')
except Exception:
    old_content=[]

old_content.extend(arglist)
save_to_json_file(old_cotent, 'add_item.json')
