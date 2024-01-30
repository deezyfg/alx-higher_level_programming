#!/usr/bin/python3
"""
101-locked_class.py - Module defining a locked class.

Attributes:
    __slots__ (list): A list of allowed attribute names.
                      Only 'first_name' is permitted.
"""


class LockedClass:
    """
    A class that restricts attribute creation to 'first_name' only.

    Attributes:
        first_name (str): The only allowed attribute for instantiation.
    """

    __slots__ = ["first_name"]
