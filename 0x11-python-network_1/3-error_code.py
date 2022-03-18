#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
from sys import argv
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    rep = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(rep) as response:
            print(response.read().decode(encoding="utf-8"))
    except URLError as err:
        print("Error code: {}".format(err.code))
