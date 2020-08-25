#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(reques) as res:
            print(res.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
