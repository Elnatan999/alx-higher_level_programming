#!/usr/bin/python3
def main():
   import sys
   i = len(sys.argv)
   if i - 1 > 0:
      print("{0}".format(i - 1),"argument:")
   elif i - 1 > 1:
      print("{0}".format(i - 1),"arguments:")
   else:
      print("{0}".format(i - 1),"argument.")
   for counter in range(0, i - 1):
      print("{0}: {1}".format(counter + 1, sys.argv[counter + 1]))
if __name__ == "__main__":
   main()   
