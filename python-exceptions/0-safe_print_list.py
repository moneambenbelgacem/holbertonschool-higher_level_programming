#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr_print = 0
    try:
        for i in range(x):
            print(my_list[i],end='')
            nbr_print += 1
    except IndexError:
        pass
    print()
    return nbr_print
