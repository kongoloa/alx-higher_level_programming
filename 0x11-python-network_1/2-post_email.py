#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response
"""
from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    info = {'email': argv[2]}
    data = urllib.parse.urlencode(info)
    data = data.encode('ascii')
    url = argv[1]
    reply = urllib.request.Request(url, data)
    with urllib.request.urlopen(reply) as response:
        body = response.read()
    print(body.decode(encoding="utf-8"))
