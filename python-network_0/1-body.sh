#!/bin/bash
#function
curl -sIL "$1" | grep -q "HTTP/.* 200" && curl -sL "$1"
