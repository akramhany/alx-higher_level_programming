#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file.
"""
import json
import sys

load_from_json = __import__("6-load_from_json_file").load_from_json_file
save_to_json = __import__("5-save_to_json_file").save_to_json_file


filename = "add_item.json"
args_list = []
file_data = []

# if the file doesn't exist, we would create it
with open(filename, 'a', encoding="utf-8") as f:
    pass

# load data from the file if it contains data
with open(filename, 'r', encoding="utf-8") as f:
    if f.read() != "":
        file_data = load_from_json(filename)

args_list = file_data

for i in range(1, len(sys.argv)):
    args_list.append(sys.argv[i])

save_to_json(args_list, filename)
