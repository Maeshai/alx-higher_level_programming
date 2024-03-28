#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if (res.status_code >= 400):
        print(f"Error code: {res.status_code}")
        exit()
    print(res.text)
