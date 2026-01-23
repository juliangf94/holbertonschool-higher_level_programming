# Python - Test-driven development

## Description
This project focuses on the importance of testing in Python. It covers the use of the `doctest` module for interactive testing through documentation strings and the `unittest` framework for more complex and automated testing scenarios. The goal is to write clean, reliable code by validating edge cases and ensuring all functions meet specific requirements.

## Files

| File | Description |
| --- | --- |
| `2-matrix_divided.py` | Function that divides all elements of a matrix. |
| `3-say_my_name.py` | Function that prints "My name is <first name> <last name>". |
| `4-print_square.py` | Function that prints a square with the character `#`. |
| `5-text_indentation.py` | Function that prints a text with 2 new lines after `.`, `?` and `:`. |
| `6-max_integer.py` | Function to find the maximum integer in a list. |
| `tests/` | Directory containing all test files (`.txt` for doctests and `.py` for unittests). |

## Requirements
* All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* All files should end with a new line.
* The first line of all files should be exactly `#!/usr/bin/python3`.
* Code follows the `pycodestyle` style (version 2.8.*).
* All modules, classes, and functions have documentation.

## How to Run Tests

### Using Doctest
To run doctests for a specific file:
```bash
python3 -m doctest -v ./tests/file_name.txt
