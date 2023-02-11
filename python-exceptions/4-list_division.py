#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        msg = None
    try:
        res.append(my_list_1[i]/my_list_2[i])
    except TypeError:
        msg = "wrong type"
        res.append(0)
    except ZeroDivisionError:
        msg = "division by 0"
        res.append(0)
    except IndexError:
        msg = "out of range"
        res.append(0)
    finally:
        if msg:
            print(msg)
    return(res)
