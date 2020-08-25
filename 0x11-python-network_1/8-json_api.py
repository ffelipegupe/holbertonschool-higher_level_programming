#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
"""
import requests
import sys


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    payload = {'q': letter}

    req = requests.post("http://0.0.0.0:500/search_user", data=payload)
    try:
        req_data = req.json()
        if not req_data:
            print("No result")
        else:
            print("[{}] {}".format(req_data.get("id"), req_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
