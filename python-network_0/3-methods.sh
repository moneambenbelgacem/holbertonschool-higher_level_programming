#!/bin/bash
#function
curl -s -X OPTIONS -i "$1" | awk '/Allow/ {print $2}'
