#!/usr/bin/python3
"""Student class definition"""


class Student:
    """
    Studnet Class
    """
    def __init__(self, first_name, last_name, age):
        """
        student attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that returns dict representation
        and retrieves attributes based on attrs
        """
        if type(attrs) is not list:
            return self.__dict__

        attributes = {}

        for i in attrs:
            temp = getattr(self, i, None)
            if temp is not None:
                attributes[i] = temp
        return attributes

    def reload_from_json(self, json):
        """
        Reloads JSON file
        """

        for i in json:
            self.__dict__[i] = json[i]
