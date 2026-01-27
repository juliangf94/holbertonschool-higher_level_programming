# Python - Classes and Objects

## Description
This project marks the beginning of **Object-Oriented Programming (OOP)** in Python. The goal is to understand how to encapsulate data, validate attributes using properties (getters and setters), and define the behavior of objects through methods. Throughout the project, we build an increasingly complex `Square` class that handles its own state and visual representation.

## Learning Objectives
By the end of this project, I have learned:
* Why Python programming is awesome.
* What is an object and a class.
* The difference between a class and an instance.
* What is an attribute and how to use them.
* The difference between public, protected, and private attributes.
* The importance of the `self` keyword.
* What is a method and how it defines object behavior.
* The **Pythonic way** to write getters and setters using `@property`.
* How to use data encapsulation to protect the integrity of a class.

## Requirements
* **Environment:** Ubuntu 20.04 LTS.
* **Language:** Python 3.8.5.
* **Style Guide:** `pycodestyle` (version 2.8.*).
* **Documentation:** All modules, classes, and methods include comprehensive docstrings.

---

## Project Structure

| File | Description |
| :--- | :--- |
| `0-square.py` | Defines an empty class `Square`. |
| `1-square.py` | Adds a private instance attribute `size`. |
| `2-square.py` | Adds type and value validation for the `size` attribute. |
| `3-square.py` | Implements the public method `area()` to return the square's surface. |
| `4-square.py` | Uses `@property` and `@size.setter` for Pythonic data access. |
| `5-square.py` | Adds `my_print()` to display the square using the `#` character. |
| `6-square.py` | Adds `position` attribute to handle (x, y) coordinates for printing. |

---

## Key Concepts Mastered

### Data Encapsulation
Used private attributes (e.g., `__size`) to prevent direct modification from outside the class. This ensures that the internal state of the object remains consistent.



### Property Getters & Setters
Implemented the `@property` decorator to retrieve values and the `@attribute.setter` decorator to validate data before assignment. This allows the class to raise `TypeError` or `ValueError` if the data is invalid.

### Method Implementation
Developed the `area()` method for mathematical computation and `my_print()` for visual output, demonstrating how objects can perform actions based on their internal data.



### Coordinate Logic
Task 6 involved complex spatial logic where the `position` tuple controls leading spaces (x-axis) and leading new lines (y-axis) during the printing process.

---

## Author
* **Julian Gonzalez** - [juliangf94](https://github.com/juliangf94)
