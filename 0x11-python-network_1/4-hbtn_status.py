#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status
    Using the package 'requests'
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
