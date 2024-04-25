#!/bin/bash
# A Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -L -I -X OPTIONS "$1" | grep -i "Allow:" | cut -d ':' -f2 | tr -d ''
