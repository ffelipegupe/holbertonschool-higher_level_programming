#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    psw = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(usr, psw))
    print(req.json().get('id'))
