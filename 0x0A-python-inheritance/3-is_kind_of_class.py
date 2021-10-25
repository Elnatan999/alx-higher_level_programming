#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines a class
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited
    """
    if isinstance(obj, a_class):
        return True
    return False
