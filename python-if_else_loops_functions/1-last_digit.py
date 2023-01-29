#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld > 0 and ld < 6:
    print("Last digit of {} is {:d} and is less than 6 and not 0".format(number,int(ld)))
elif ld > 5:
    print("Last digit of {} is {:d} and is greater than 5".format(number,int(ld)))
elif ld == 0:
    print("Last digit of {} is {:d} and is 0".format(number,int(ld)))
elif number < 0:
    print("Last digit of {} is {:d} and is 0".format(number,int(ld -10)))