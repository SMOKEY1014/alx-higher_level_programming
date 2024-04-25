#!/bin/bash
# A Bash script that takes in a URL as an argument,
# sends a GET request to the URL, and displays the body of the response
#A header variable X-School-User-Id must be sent with the value 98


# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define the URL from the first argument
url="$1"

# Send a GET request with the custom header and display the response body
curl -s -L -H "X-School-User-Id: 98" "$url"
echo ""
