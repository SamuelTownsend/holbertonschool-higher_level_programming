#!/usr/bin/python3
def print_reversed_list_interger(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
    else:
        return