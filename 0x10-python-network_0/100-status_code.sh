#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
curl -s "$1" -o /dev/null -w "%{http_code}"
