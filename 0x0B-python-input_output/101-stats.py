#!/usr/bin/python3
'''Module of Log parsing script'''

import sys

numline = 0
totalSize = 0
stcodes = {"200": 0, "301": 0, "400": 0,
           "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

while True:
    try:
        for line in sys.stdin:
            linelist = line.split(" ")
            totalSize += int(linelist[8])
            stcodes[linelist[7]] += 1

            numline += 1
            if numline == 10:
                numline = 0
                print("File size: {}".format(totalSize))
                for code in sorted(stcodes.keys()):
                    if stcodes[code] != 0:
                        print("{}: {}".format(code, stcodes[code]))
    except KeyboardInterrupt:
        print("File size: {}".format(totalSize))
        for code in sorted(stcodes.keys()):
            if stcodes[code] != 0:
                print("{}: {}".format(code, stcodes[code]))
        exit()
