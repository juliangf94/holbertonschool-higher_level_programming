# Python - Everything is object

## Description
This project is part of the curriculum at **Holberton School**. It explores the fundamental design of Python: the fact that **everything is an object**. Understanding how Python handles variable assignment, memory allocation, and the distinction between mutable and immutable objects is crucial for writing efficient and bug-free code.

## Learning Objectives
By the end of this project, I was able to explain:
* Why Python is an object-oriented programming language.
* The difference between an **object** and a **reference**.
* The difference between **mutable** and **immutable** objects.
* How Python treats mutable and immutable objects differently.
* How arguments are passed to functions (**Pass by object reference**).
* The use of `id()`, `type()`, and the `is` vs `==` operators.

## Practical Examples Covered

### 1. Identity vs. Equality
* `==` checks for **value equality** (if the data inside is the same).
* `is` checks for **identity** (if both variables point to the same memory address).

### 2. Mutability
* **Mutable objects** (e.g., `list`, `dict`, `set`) can be changed after creation. Modifications happen "in-place" without changing the object's ID.
* **Immutable objects** (e.g., `int`, `float`, `str`, `tuple`) cannot be changed. Any "modification" actually creates a new object in memory.

### 3. Function Arguments
In Python, arguments are passed by **assignment**. 
* Modifying a mutable object inside a function **affects** the original object.
* Reassigning an immutable object inside a function **does not affect** the original variable in the calling scope.

## Project Files
| File | Task | Description |
| --- | --- | --- |
| `0-answer.txt` | type | What is the type of a number? |
| `19-copy_list.py` | copy_list | Function that returns a copy of a list. |
| `...-answer.txt` | Logic tests | Answers to logic questions regarding `is`, `==`, and memory. |

## Author
* **Julian Gonzalez** - [GitHub](https://github.com/your-username)
