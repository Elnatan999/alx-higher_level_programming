#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        y = a ** b
        return (y)
    else:
        x = 1/(a ** -b)
        return (x)
