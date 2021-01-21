#!/usr/bin/python3
"""
a script that adds all arguments to a Python list, and then save them to a file
"""


import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
with open(filename, 'a+') as f:
    pass

try:
    loaded = load_from_json_file(filename)
except ValueError:
    loaded = []
newitems = sys.argv[1:]
loaded += newitems
save_to_json_file(loaded, filename)
