# Python - Input/Output
---
## Description
This project covers the fundamental concepts of file handling in Python. It transitions from basic reading and writing of text files to more complex data serialization using the JSON format. The project culminates in the implementation of object-to-dictionary mapping and the creation of a Pascal's Triangle algorithm.
---
## Learning Objectives
* How to open a file and handle its closure using the `with` statement.
* How to read and write text files efficiently.
* Understanding the JSON format (JavaScript Object Notation).
* How to convert Python data structures to JSON strings and vice versa.
* How to serialize and deserialize an object (Class to JSON).
* How to use command-line arguments in a Python script.
---
## Technologies
* Scripts written in **Python 3.10** (or higher).
* Tested on **Ubuntu 20.04 LTS**.
* Style compliance with `pycodestyle` (version 2.8.*).
---
## Files

| File | Description |
| --- | --- |
| `0-read_file.py` | Function that reads a text file (UTF8) and prints it to stdout. |
| `1-write_file.py` | Function that writes a string to a text file and returns the number of characters written. |
| `2-append_write.py` | Function that appends a string at the end of a text file. |
| `3-to_json_string.py` | Function that returns the JSON representation of an object (string). |
| `4-from_json_string.py` | Function that returns an object represented by a JSON string. |
| `5-save_to_json_file.py` | Function that writes an Object to a text file, using a JSON representation. |
| `6-load_from_json_file.py` | Function that creates an Object from a JSON file. |
| `7-add_item.py` | Script that adds all arguments to a Python list, and then save them to a file. |
| `8-class_to_json.py` | Function that returns the dictionary description for JSON serialization of an object. |
| `9-student.py` | Class `Student` that defines a student by first_name, last_name, and age. |
| `10-student.py` | Class `Student` with a `to_json` method that allows attribute filtering. |
| `11-student.py` | Class `Student` with a `reload_from_json` method to update attributes. |
| `12-pascal_triangle.py` | Function that returns a list of lists representing Pascal’s triangle of `n`. |
---
## Requirements

### General
* Allowed editors: `vi`, `vim`, `emacs`.
* All files should end with a new line.
* The first line of all your files should be exactly `#!/usr/bin/python3`.
* A `README.md` file, at the root of the folder of the project, is mandatory.
* Your code should use the `pycodestyle` style.
* All your modules, classes, and functions should have a documentation (`__doc__`).
---
## Usage
To test the scripts, you can use the provided main files (e.g., `0-main.py`).

```bash
# Example: Reading a file
./0-main.py

# Example: Adding arguments to a persistent JSON list
./7-add_item.py Holberton School 89
cat add_item.json
# Output: ["Holberton", "School", "89"]
```
---
## Author
Julian - juliangf94
