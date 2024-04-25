#!/bin/bash
# A Bash script that takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response
# A variable email must be sent with the value `test@gmail.com``
# A variable subject must be sent with the value `I will always be here for PLD`


# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define the URL from the first argument
url="$1"

# Define variables for email and subject
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request with the variables and display the response body
curl -s -X POST -d "email=$email&subject=$subject" "$url"
