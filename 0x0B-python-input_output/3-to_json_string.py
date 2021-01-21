#!/usr/bin/python3
"""method definition for to_json_string"""


def to_json_string(my_obj):
    """
    a function that returns the JSON representation of an object (string)
    """
    import json
    return json.dumps(my_obj)
