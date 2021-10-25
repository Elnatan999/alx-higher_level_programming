#!/usr/bin/python3
# 0-read_file.py
"""for task 1"""


def read_file(filename=""):
    """Print the contents of a utf-8
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
