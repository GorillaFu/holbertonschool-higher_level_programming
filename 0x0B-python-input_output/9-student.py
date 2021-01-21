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

    def to_json(self):
        """
        Method that returns dictionary representation
        """
        return self.__dict__
