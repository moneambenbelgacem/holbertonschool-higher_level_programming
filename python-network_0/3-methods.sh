#!/bin/bash
#function
curl -s -I -X OPTIONS "$1" | awk -F ': ' '/Allow/ {print $2}'
