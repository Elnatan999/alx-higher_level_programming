#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class MyList.
"""


class MyList(list):
    """Implements sorted printing for list class.
    """

    def print_sorted(self):
        """Print a list in an ascending order.
    """
        print(sorted(self))
