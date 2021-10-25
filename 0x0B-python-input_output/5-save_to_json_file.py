#!/usr/bin/python3
# 5-save_to_json_file.py
"""for task 5
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
