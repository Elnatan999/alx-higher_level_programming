#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
  z = chr(i)
  if z not in 'qe':
     print(z, end="")
