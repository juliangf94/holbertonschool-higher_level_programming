# Python - More Classes and Objects

## Description
This project continues the journey into **Object-Oriented Programming (OOP)** in Python. While the previous project focused on basic class structure and encapsulation, this repository explores more advanced concepts such as **Class Attributes**, **Static Methods**, **Class Methods**, and the lifecycle of an object (including the destructor).

Throughout the project, we develop a robust `Rectangle` class capable of self-validation, mathematical computations, and dynamic visual representation.

## Learning Objectives
By the end of this project, I have learned:
* Why Python programming is awesome.
* What is the difference between a **Class Attribute** and an **Instance Attribute**.
* How to use public and private attributes safely.
* What are the special methods `__str__` and `__repr__` and how to use them.
* What is the difference between `__str__` and `__repr__`.
* What is the `__del__` method (Destructor) and when it is called.
* What is a **Static Method** (`@staticmethod`) and why use it.
* What is a **Class Method** (`@classmethod`) and how it serves as an alternative constructor.
* How to protect data using property getters and setters.

## Requirements
* **Environment:** Ubuntu 20.04 LTS.
* **Language:** Python 3.8.5.
* **Style Guide:** `pycodestyle` (version 2.8.*).
* **Documentation:** Mandatory docstrings for modules, classes, and methods.

---

## Project Structure

| File | Description |
| :--- | :--- |
| `0-rectangle.py` | Defines an empty class `Rectangle`. |
| `1-rectangle.py` | Adds `width` and `height` with private validation. |
| `2-rectangle.py` | Implements `area()` and `perimeter()` methods. |
| `3-rectangle.py` | Adds `__str__` to print the rectangle using the `#` character. |
| `4-rectangle.py` | Adds `__repr__` to allow recreation of the instance via `eval()`. |
| `5-rectangle.py` | Implements the destructor `__del__` with a "Bye" message. |
| `6-rectangle.py` | Adds a class attribute `number_of_instances` to track active objects. |
| `7-rectangle.py` | Adds a class attribute `print_symbol` to customize the drawing character. |
| `8-rectangle.py` | Implements a `@staticmethod` to compare two rectangles by area. |
| `9-rectangle.py` | Implements a `@classmethod` to create a Square instance. |

---

## Key Technical Concepts

### Instance vs Class Attributes
We implemented `number_of_
