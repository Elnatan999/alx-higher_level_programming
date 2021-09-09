#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
newnumber = abs(number) % 10
if newnumber > 5:
   print("Last digit of", number, "is", newnumber, "and is greater than 5")
elif newnumber == 0:
   print("Last digit of", number, "is", newnumber, "and is 0")
elif newnumber < 6 and newnumber != 0:
   print("Last digit of", number, "is", newnumber, "and less than 6 and not 0")
else:
   print("invalid entry")
