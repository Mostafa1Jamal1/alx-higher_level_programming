#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status  '''
import urllib.request


if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        utf8content = content.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {utf8content}")
