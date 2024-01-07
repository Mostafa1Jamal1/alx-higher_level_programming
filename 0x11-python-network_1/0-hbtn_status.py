#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status  '''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print(f'''Body response:
        \t- type: {type(content)}
        \t- content: {content}
        \t- utf8 content: OK''')
