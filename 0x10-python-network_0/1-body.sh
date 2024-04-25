#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
# Display only body of a 200 status code response


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
