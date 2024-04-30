#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as
    a parameter, and displays the body of the response (decoded in utf-8)
    Usage: ./2-post_email.py <URL> <email>
    - Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
