#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"
