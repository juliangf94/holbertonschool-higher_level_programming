# Python - Exceptions

## Description
This project covers how to handle errors and exceptions in Python. Instead of checking for errors before they happen (LBYL), Python encourages "asking for forgiveness rather than permission" (**EAFP**). This repository demonstrates how to use `try`, `except`, `else`, and `finally` to create robust and crash-proof programs.

## Learning Objectives
* Why Python programming is awesome.
* What is the difference between errors and exceptions.
* What are exceptions and how to use them.
* When do we need to use exceptions.
* How to correctly handle an exception.
* What is the purpose of catching exceptions.
* How to raise a builtin exception.
* When do we need to implement a clean-up action after an exception.

## Tasks

| File | Task Name | Description |
| :--- | :--- | :--- |
| `0-safe_print_list.py` | Safe list printing | Prints `x` elements of a list using `try/except` without using `len()`. |
| `1-safe_print_integer.py` | Safe integer printing | Prints an integer with `"{:d}".format()` and returns `True` if successful. |
| `2-safe_print_list_integers.py` | Print and count integers | Prints only integers from a list, skipping other types silently. |
| `3-safe_print_division.py` | Integers division with debug | Divides 2 integers and prints the result in a `finally` block. |
| `4-list_division.py` | Divide a list | Divides elements of two lists one by one, handling multiple exceptions. |
| `5-raise_exception.py` | Raise exception | A function that raises a `TypeError`. |
| `6-raise_exception_msg.py` | Raise a message | A function that raises a `NameError` with a custom message. |

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`.
* All files interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5).
* All files should end with a new line.
* The first line of all files should be exactly `#!/usr/bin/python3`.
* Your code should use the `pycodestyle` (version 2.8.*).

## Key Concept: EAFP vs LBYL
* **LBYL** (Look Before You Leap): Checking if a file exists before opening it.
* **EAFP** (Easier to Ask for Forgiveness than Permission): Trying to open the file and catching the error if it fails. This is the "Pythonic" way.

