#!/bin/bash
#function
response=$(curl -s -L -o /dev/null -w "%{http_code}\n%{redirect_url}" "$1")

redirect_count=$(grep -c "http://" <<< "$response")

if [ "$redirect_count" -eq 1 ]; then
  curl -s -L "$response"
fi