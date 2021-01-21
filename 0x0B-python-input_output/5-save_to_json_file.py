#!/usr/bin/python3
"""method definition for save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
