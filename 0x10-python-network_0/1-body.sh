#!/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

status_code=$(curl -s -L -o text.txt -w "%{http_code}" "$1")

if [ "$status_code" == "200" ]; then
    cat text.txt
fi
rm -f text.txt
