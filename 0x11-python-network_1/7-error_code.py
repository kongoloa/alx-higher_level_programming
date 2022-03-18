#!/usr/bin/python3
"""
script to send requests to url and display body of response
"""
from sys import argv
import requests

if __name__ == "__main__":
    response = requests.get(argv[1])
    code = response.status_code
    if code > 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
