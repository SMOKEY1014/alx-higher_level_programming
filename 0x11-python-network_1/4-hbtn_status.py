#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
Usage: ./4-hbtn_status.py | cat -e
  - Handles HTTP errors.
"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
