#!/bin/bash
#function
if [ $# -eq 0 ]; then
  echo "Usage: ./get_response_body.sh <URL>"
  exit 1
fi

url=$1

response=$(curl -s -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
  curl -s "$url"
fi
