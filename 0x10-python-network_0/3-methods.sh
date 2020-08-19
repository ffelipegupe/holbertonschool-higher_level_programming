#!/bin/bash
# Bash script that takes in a URL, displays all methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
