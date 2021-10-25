#!/usr/bin/python3
# 1-write_file.py
"""for task 2
"""


def write_file(filename="", text=""):
    """Write a string to UTF8
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
