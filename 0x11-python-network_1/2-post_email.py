#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    url_pa = {'email': email}

    data = urllib.parse.urlencode(url_pa)
    data = data.encode('utf8')
    req = urllib.request.Reques(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf8'))
