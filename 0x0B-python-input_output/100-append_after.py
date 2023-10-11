#!/usr/bin/python3
'''Module of only one function
append_after(filename="", search_string="", new_string="")'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file,
    after each line containing a specific string'''
    with open(filename, mode="r+", encoding="utf-8") as afile:
        text = afile.readlines()
        afile.seek(0)

        for line in text:
            afile.write(line)
            if search_string in line:
                afile.write(new_string)
