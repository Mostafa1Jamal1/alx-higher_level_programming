#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response
If any urllib.error.HTTPError exception occur it will print:
"Error code: followed by the HTTP status code"'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except Exception:
        print(f"Error code: {r.status_code}")
