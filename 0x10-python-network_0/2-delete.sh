#!/bin/bash
# A Bash script that sends a DELETE request to the URL passed as
# the first argument and displays the body of the response

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

status_code=$(curl -s -L -o text.txt -w "%{http_code}" "$1")

if [ "$status_code" == "200" ]; then
    curl -s -X DELETE "$1"
fi
rm -f text.txt