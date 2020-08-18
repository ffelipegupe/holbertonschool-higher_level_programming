#!/bin/bash
# Bash script that takes in a URL, displays the size of the response
curl -sI "$1" | grep "Content-Lenght" | cut -d' ' -f 2
