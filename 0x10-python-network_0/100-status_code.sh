#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL,
curl -s -L -o text.txt -w "%{http_code}" "$1" | rm -f text.txt | echo "$status_code"
