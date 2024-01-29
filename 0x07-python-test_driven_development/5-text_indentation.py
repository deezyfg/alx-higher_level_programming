#!/usr/bin/python3
"""
Module defining a function for text indentation.
"""


def text_indentation(text):
    """Function that prints 2 new lines after ".?:" characters.

    Args:
        text: The input string.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
