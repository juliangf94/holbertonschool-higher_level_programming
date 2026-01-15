# Python Fundamentals: Higher Level Programming

This repository contains a comprehensive overview and practical exercises for Python 3 fundamentals, covering the interpreter, data types, string manipulation, and coding standards (PEP 8).



---

## 1. General Concepts

### How to use the Python Interpreter
The interpreter is the engine that executes your code. You can use it in two ways:
- **Interactive Mode:** - Simply type `python3` in your terminal. 
    - You will see the `>>>` prompt, where you can type code and get immediate results. 
    - To exit, type `exit()` or press `Ctrl + D`.
- **Script Mode:** - Write your code in a file ending in `.py` (e.g., `myscript.py`). 
    - Run it by typing `python3 myscript.py` in the terminal, or by making the file executable and running `./myscript.py`.

### Printing Text and Variables
The `print()` function displays information on the screen:
- **Strings:** `print("Hello World")`
- **Variables:** `name = "Julian" -> print(name)`
- **Formatted Output:** Use f-strings for efficiency:
    ```python
    age = 30
    print(f"I am {age} years old.")
    ```

### Working with Strings
Strings are sequences of characters wrapped in single (') or double (") quotes:
- **Concatenation:** Combining strings using `+`.
- **Repetition:** Using `*` (e.g., `"Holberton" * 3`).
- **Immutability:** Once a string is created, its characters cannot be changed individually.

### Indexing and Slicing
- **Indexing:** Accessing a single character by its position. Indices start at 0.
    ```python
    word = "Python"
    # word[0] is 'P', word[-1] is 'n' (last character)
    ```
- **Slicing:** Extracting a part of a string using the syntax `[start:stop:step]`.
    ```python
    word = "Python"
    # word[1:4]   -> 'yth'
    # word[0:2]   -> 'Py' (from index 0 up to, but NOT including, index 2)
    # word[::-1]  -> 'nohtyP' (reverses the word)
    ```

---

## 2. Coding Style and Standards
- **Official Style:** **PEP 8** (Python Enhancement Proposal 8). It provides guidelines for naming conventions (`snake_case`), indentation (4 spaces), and whitespace.
- **Checking Style:** Use `pycodestyle` to check for violations:
    ```bash
    pycodestyle filename.py
    ```

---

## 3. Knowledge Check (Quiz)

- [ ] **#0 print("Holberton school")** -> Result: `Holberton school`
- [x] **#1 print(f"{98} Battery street")** -> Result: `98 Battery street`
- [ ] **#2 print(f"{98} Battery street, {'San Francisco'}")** -> Result: `98 Battery street, San Francisco`
- [x] **#3 a = "Python is cool"; print(a[4])** -> Result: `o`
- [ ] **#4 a = "Python is cool"; print(a[0:6])** -> Result: `Python`
- [x] **#5 a = "Python is cool"; print(a[:6])** -> Result: `Python`
- [ ] **#6 a = "Python is cool"; print(a[7:])** -> Result: `is cool`
- [x] **#7 a = "Python is cool"; print(a[7:-5])** -> Result: `is`
- [ ] **#8 a = "Python is cool"; print(a[-2])** -> Result: `o`

---

## 4. Exercises

### [2-print.py](./2-print.py)
```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
