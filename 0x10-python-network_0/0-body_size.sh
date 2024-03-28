#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -si "$1" | grep Content-Length | tail -c 4
