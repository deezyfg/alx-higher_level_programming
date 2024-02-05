#!/usr/bin/python3
"""
    This module provides a function to retrieve the list of
    attributes and methods of an object
"""


def lookup(obj):
    """Retrieve the list of attributes and methods of an object."""
    return dir(obj)
