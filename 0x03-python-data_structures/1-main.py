#!/usr/bin/python3
element_at = __import__('1-element_at').element_at
my_list = [1, 2, 3, 4, 5]
idx = -2
print("Element at index {0} is {1}".format(idx, element_at(my_list, idx)))
