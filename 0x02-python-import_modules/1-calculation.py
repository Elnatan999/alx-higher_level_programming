#!/usr/bin/python3
def main():
   from calculator_1 import add, sub, mul, div
   a = 10
   b = 5
   print("{0}".format(a), "+", "{0}".format(b), "=", add(a, b))
   print("{0}".format(a), "-", "{0}".format(b), "=", sub(a, b))
   print("{0}".format(a), "*", "{0}".format(b), "=", mul(a, b))
   print("{0}".format(a), "/", "{0}".format(b), "=", div(a, b))


if __name__ == "__main__":
   main()
