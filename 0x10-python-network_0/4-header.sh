#!/bin/bash
# A Bash script that takes in a URL as an argument,
# sends a GET request to the URL, and displays the body of the response
#A header variable X-School-User-Id must be sent with the value 98


# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument." >&2
  exit 1
fi

# Define the URL from the first argument
url="$1"

# Send a GET request with the custom header and display the response body
curl -s -L -H "X-School-User-Id: 98" "$url"
echo ""
