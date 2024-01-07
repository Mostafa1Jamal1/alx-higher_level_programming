#!/usr/bin/python3
''' takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
for more information see README.md'''
import requests
import sys


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': sys.argv[1][0] if len(sys.argv) > 1 else ""}

    r = requests.post(url, data=data)

    try:
        jsond = r.json()
        if not jsond == {}:
            print(f"[{jsond.get('id')}] {jsond.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
