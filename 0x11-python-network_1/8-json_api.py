#!/usr/bin/python3
''' takes in a letter and sends a POST request
to http://36595c7ea186.6ad0eb84.alx-cod.online:5000/search_user
with the letter as a parameter.
for more information see README.md'''
import requests
import sys


if __name__ == "__main__":

    url = 'http://36595c7ea186.6ad0eb84.alx-cod.online:5000/search_user'
    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}

    r = requests.post(url, data=data)

    try:
        jsond = r.json()
        if not jsond == {}:
            print(f"[{jsond.get('id')}] {jsond.get('name')}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
