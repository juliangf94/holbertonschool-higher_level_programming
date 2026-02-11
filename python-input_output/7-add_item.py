#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list
and saves them to a JSON file named add_item.json.
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
# Checks if the file exists
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Only the words we use
my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
