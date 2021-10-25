#!/usr/bin/python3
# 6-load_from_json_file.py
"""for task 6
"""
import json


def load_from_json_file(filename):
    """Create a Python object
    """
    with open(filename) as f:
        return json.load(f)
