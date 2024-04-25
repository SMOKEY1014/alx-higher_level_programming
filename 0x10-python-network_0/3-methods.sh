#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept.

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument." >&2
  exit 1
fi

# Define the URL from the first argument
url="$1"

# Use curl with the OPTIONS method and capture the response headers
curl -s -L -I -o text -X OPTIONS "$url"
# Extract the line containing the Allow header (if it exists)
allow_header=$(grep -i "Allow:" text)

# Check if the Allow header is found and extract allowed methods
if [ -n "$allow_header" ]; then
  # Extract methods after "Allow: " (using cut)
  methods=$(echo "$allow_header" | cut -d ':' -f2 | tr -d '')
  echo "$methods"
else
  echo "No Allow header found. Server may not support method enumeration." >&2
fi

rm -f text
