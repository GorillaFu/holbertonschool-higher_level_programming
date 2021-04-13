#!/usr/bin/python3
# python script that takes in a URL, displays val of X-Request-Id
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.headers['X-Request-Id']
    print(html)
