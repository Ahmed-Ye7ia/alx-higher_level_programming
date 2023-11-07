#!/usr/bin/python3
"""
 contain a script that adds all arguments to a Python list,
 and then save them to a file:
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = "add_item.json"

try:
    old_content = load_from_json_file(f)
except FileNotFoundError:
    existing_content = []

save_to_json_file(old_content + argv[1:], f)
