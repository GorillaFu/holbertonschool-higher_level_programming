#!/usr/bin/python3
# Python script that takes in a URL, displays val of X-Request-Id
import urllib.request
import sys

# script
with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.headers['X-Request-Id']
    print(html)
