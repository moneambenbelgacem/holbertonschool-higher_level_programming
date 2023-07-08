#!/bin/bash
#function
if [ $# -eq 0 ]; then
  echo "Usage: ./get_response_size.sh <URL>"
  exit 1
fi

url=$1

response=$(curl -s -w "%{size_download}" -o /dev/null "$url")

echo "Response size: $response bytes"
