#!/usr/bin/python3
# prints body returned by post request
import requests
import sys

url = sys.argv[1]
mail = requests.post(url, data={'email': sys.argv[2]})
print(mail.text)
