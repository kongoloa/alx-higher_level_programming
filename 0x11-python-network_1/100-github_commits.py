#!/usr/bin/python3
"""
Takes 2 arguments in order to list 10 commits (newest to oldest).
"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1])).json()
    count = 0
    for commit in r:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, name))
        count += 1
        if count == 10:
            break
