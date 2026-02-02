# Python - Inheritance

## Description
This project focuses on the implementation of **Inheritance** in Python. It explores how to create hierarchical relationships between classes, reuse code efficiently, and understand how Python resolves methods and attributes across different levels of inheritance. The project culminates in building a geometry module featuring data validation and multi-level inheritance (BaseGeometry -> Rectangle -> Square).

## Learning Objectives
By the end of this project, I am able to explain:
* The differences between a **Superclass**, **Baseclass**, and **Parentclass**.
* What a **Subclass** is and how it functions.
* How to use `dir()` to list all attributes and methods of an object.
* How to inherit a class from another and define multiple base classes.
* The default class that every class inherits from in Python 3 (`object`).
* How to **override** methods and attributes.
* The purpose and benefits of inheritance (Code reusability and extensibility).
* How to use built-in functions: `isinstance`, `issubclass`, `type`, and `super`.

## Requirements
* **Environment:** Ubuntu 20.04 LTS.
* **Language:** Python 3.8.5.
* **Style:** `pycodestyle` (version 2.7.*).
* **Documentation:** All modules, classes, and methods must have a documentation string that explains their purpose in a full sentence.
* **Execution:** All files must be executable and start with `#!/usr/bin/python3`.

## File Hierarchy

| File | Description |
| :--- | :--- |
| `0-lookup.py` | Returns the list of available attributes and methods of an object. |
| `1-my_list.py` | A class `MyList` that inherits from `list` and includes a `print_sorted` method. |
| `2-is_same_class.py` | Function that returns `True` if the object is **exactly** an instance of the specified class. |
| `3-is_kind_of_class.py` | Function that returns `True` if the object is an instance of, or inherited from, the specified class. |
| `4-inherits_from.py` | Function that returns `True` if the object is an inherited instance (strictly) of a class. |
| `5-base_geometry.py` | An empty class `BaseGeometry`. |
| `6-base_geometry.py` | Adds the `area()` method that raises an `Exception` (Interface design). |
| `7-base_geometry.py` | Adds `integer_validator()` to ensure inputs are positive integers. |
| `8-rectangle.py` | Class `Rectangle` inheriting from `BaseGeometry` with private attributes. |
| `9-rectangle.py` | Implements `area()` and `__str__` for the `Rectangle` class. |
| `10-square.py` | Class `Square` inheriting from `Rectangle` using `super()`. |
| `11-square.py` | Specialized `__str__` for `Square` to print `[Square] <width>/<height>`. |



## Testing
Test cases are stored in the `tests/` folder. They are written in `doctest` format and can be executed with the following command:

```bash
python3 -m doctest ./tests/*
