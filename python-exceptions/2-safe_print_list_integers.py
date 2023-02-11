#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbr_print = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            nbr_print += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return nbr_print
