#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance
    """
    if type(obj) == a_class:
        return True
    return False
