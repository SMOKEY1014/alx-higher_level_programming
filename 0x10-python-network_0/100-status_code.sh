#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL,
curl -so /dev/null -w "%{http_code}" "$1"
