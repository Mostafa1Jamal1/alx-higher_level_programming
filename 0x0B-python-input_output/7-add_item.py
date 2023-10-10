#!/usr/bin/python3
'''adds all arguments to a Python list, and then save them to a file
the file named add_item.json
If the file doesn’t exist, it should be created'''


from sys import argv as argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    thelist = load_from_json_file("add_item.json")
except Exception:
    thelist = []

for i, arg in enumerate(argv):
    if i != 0:
        thelist.append(arg)

save_to_json_file(thelist, "add_item.json")
