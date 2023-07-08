#!/bin/bash
#function
curl -s -I "$1" | awk '/Allow/ {split($0, methods, ": "); split(methods[2], arr, ", "); for (i in arr) print arr[i]}'
