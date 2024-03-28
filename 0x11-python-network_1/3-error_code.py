#!/usr/bin/python3
""" module doc """
import urllib.request
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
