#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response
If any urllib.error.HTTPError exception occur it will print:
"Error code: followed by the HTTP status code"'''
import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            content = response.read()
            decoded_content = content.decode('utf-8')
            print(decoded_content)
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
