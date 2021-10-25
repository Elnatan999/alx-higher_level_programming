#!/usr/bin/python3
# 2-append_write.py
"""for task 2
"""


def append_write(filename="", text=""):
    """Appends a string
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
