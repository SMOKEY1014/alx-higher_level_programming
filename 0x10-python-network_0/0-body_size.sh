#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL,
# and displays the size(bytes) of the body of the response

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the provided URL and get the size of the response body in bytes
size=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')

# Display the size of the response body
echo "$size"
