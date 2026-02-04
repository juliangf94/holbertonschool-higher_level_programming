# Python - Abstract Base Classes (ABC) and Advanced OOP

## Description
This project explores advanced Object-Oriented Programming (OOP) concepts in Python, focusing on **Abstract Base Classes (ABC)**, **Interfaces**, **Duck Typing**, and **Mixins**. The goal is to move beyond basic inheritance to create robust, modular, and maintainable code structures.

## Learning Objectives
By the end of this project, I can explain:
* How to use the `abc` module to create abstract classes.
* The importance of the `@abstractmethod` decorator.
* The concept of **Duck Typing** ("If it walks like a duck...").
* How to extend standard Python built-in classes (`list`, `iter`).
* The mechanics of **Multiple Inheritance** and **Method Resolution Order (MRO)**.
* How to use **Mixins** to add modular behavior to unrelated classes.

## Requirements
* **Environment:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style:** `pycodestyle` (version 2.7.*)
* **Execution:** All files must be executable and start with `#!/usr/bin/python3`.

## Task Summary

| File | Description |
| :--- | :--- |
| `task_00_abc.py` | Implementation of an abstract `Animal` class with mandatory `sound` methods for `Dog` and `Cat`. |
| `task_01_duck_typing.py` | Using a `Shape` interface and duck typing to calculate area and perimeter for different shapes. |
| `task_02_verboselist.py` | Extending the built-in `list` class to print notifications when items are added or removed. |
| `task_03_countediterator.py` | A wrapper for iterators that keeps track of the number of items processed. |
| `task_04_flyingfish.py` | Exploring Multiple Inheritance and MRO with `Fish`, `Bird`, and `FlyingFish`. |
| `task_05_dragon.py` | Using Mixins (`SwimMixin`, `FlyMixin`) to compose a `Dragon` class with multiple behaviors. |

[Image of Python inheritance and mixin design pattern diagram]

## How to Test
You can run the provided main files for each task to verify the output:

```bash
# Example for Task 0
./main_00_abc.py

# Example for Task 5
./main_05_dragon.py
```
