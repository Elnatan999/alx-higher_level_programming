#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0:
        if idx < len(my_list):
            sec_list = list(my_list)
            sec_list[idx] = element
            return (sec_list)
        else:
            return (my_list)
    else:
        return (my_list)
