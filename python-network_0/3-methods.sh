#!/bin/bash
#function 
curl -sI "$1" | awk '/Allow/ {print $2}'
