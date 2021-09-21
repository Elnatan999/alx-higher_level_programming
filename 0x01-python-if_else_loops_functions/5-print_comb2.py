#!/usr/bin/python3
for i in range(00, 100):
    if i < 99:
        print("%02d,"%i,"", end = "")
    elif i > 98:
        print(i)
    else:
        break
