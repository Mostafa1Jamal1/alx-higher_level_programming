#!/usr/bin/python3
''' fetches https://alx-intranet.hbtn.io/status  '''
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(f'''Body response:
        \t- type: {type(content)}
        \t- content: {content}
        \t- utf8 content: {content.decode('utf-8')}''')
