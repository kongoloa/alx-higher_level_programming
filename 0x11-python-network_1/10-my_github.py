#!/usr/bin/python3
"""
Takes GitHub credentials (username and password) and uses the GitHub API to display id
"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in r:
        print(r['id'])
    else:
        print(None)
