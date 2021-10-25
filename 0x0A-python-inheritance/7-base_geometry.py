#!/usr/bin/python3
#7-base_geometry.py
"""for task 7"""


class BaseGeometry:
    """BaseGeometry class"""
    def __init__(self):
        """Define init"""
        pass

    def area(self):
        """Defines area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """defines base geometry """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
