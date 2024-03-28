#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response A header variable X-School-User-Id must be sent with the value 98
curl -s -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
