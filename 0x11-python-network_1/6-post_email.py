#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    par = {"email": sys.argv[2]}
    req = requests.post(url, data=par)
    print(req.text)
