#!/usr/bin/python3
def uppercase(str):
 for c in range(len(str)):
    new_str = ord(str[c])
    if( (ord(c) >= 97) and (ord(c) < 123) ):
        new_str += ord(c)-32
    print("{}".format(chr(new_str)),end="")
print("")
