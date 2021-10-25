#!/usr/bin/python3
# 100-my_int.py
"""Defines a class MyInt
"""


class MyInt(int):
    """Invert int operators
    """

    def __eq__(self, value):
        """Override opeartor with behavior.
    """
        return self.real != value

    def __ne__(self, value):
        """Override operator with behavior.
    """
        return self.real == value
