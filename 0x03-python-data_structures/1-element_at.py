#!/usr/bin/python3
def element_at(my_list, idx):
   my_list = my_list[idx]
   i = len(my_list)
   

   if idx < i:
      print("{:d}".format(my_list))
   else:
      print("wooooow")
element_at(my_list, idx)
