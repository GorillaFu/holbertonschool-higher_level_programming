#!/usr/bin/python3
# print error code if error code >= 400

import requests
import sys

url = sys.argv[1]
error = requests.get(url)
if error.status_code < 400:
    print(error.text)
else:
    print("Error code: {}".format(error.status_code))
