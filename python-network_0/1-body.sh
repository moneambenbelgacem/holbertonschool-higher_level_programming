#!/bin/bash
#function
curl -s -L -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -s -L "$1"