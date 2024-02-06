#!/usr/bin/python3
"""This module defines class representing a student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student

        Args:
        first_name: The first name of the student.
        last_name: The last name of the student.
        age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student object.

        Args:
            attrs : List of attributes to include in the
            dictionary. If not specified, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
