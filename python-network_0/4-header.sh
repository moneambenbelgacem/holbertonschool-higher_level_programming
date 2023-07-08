#!/bin/bash
#function
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1" | grep "route validation with header parameter"
