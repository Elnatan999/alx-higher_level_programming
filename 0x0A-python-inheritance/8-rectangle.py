#!/usr/bin/python3
#8-rectangle.py
"""for task 8"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initializes class rectangle"""
    def __init__(self, width, height):
        """Initialize a new super function"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
