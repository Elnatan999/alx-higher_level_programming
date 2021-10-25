#!/usr/bin/python3
# 4-inherits_from.py
"""Defines an inherited class
"""


def inherits_from(obj, a_class):
    """Checks if an object is inherited
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
