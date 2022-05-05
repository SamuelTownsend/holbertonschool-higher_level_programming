#!/usr/bin/python3


def no_c(my_list):
    new_list = my_list.translate({ord(i): None for i in 'cC'})
    return new_list
