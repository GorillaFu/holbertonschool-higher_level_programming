#!/usr/bin/python3
"""define a base  class for making subclasses"""
import json
import os


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            l = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """onverts json to string"""
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object"""
        if cls.__name__ == "Rectangle":
            obj = cls(11, 1)
            obj.update(**dictionary)
            return obj
        if cls.__name__ == "Square":
            obj = cls(11)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Create"""
        load = []
        name = cls.__name__ + ".json"
        if os.path.isfile(name):
            with open(name, "r") as file:
                str = cls.from_json_string(file.read())
            for i in str:
                load.append(cls.create(**i))
            return load
        return []
