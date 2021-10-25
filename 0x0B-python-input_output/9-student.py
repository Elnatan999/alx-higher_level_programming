#!/usr/bin/python3
#9-student.py
"""for task 9"""

class Student:
   """A student class
   """

   def __init__(self, first_name, last_name, age):
       """Initalizes an object
       """

       self.first_name = first_name
       self.last_name = last_name
       self.age = age

   def to_json(self):
       """returns json representation
       """

       return self.__dict__
